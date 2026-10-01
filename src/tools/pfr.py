#!/usr/bin/env python3
"""Pobiera materiały PFR: strony PFR Ventures i startup.pfr.pl oraz wszystkie podlinkowane z nich dokumenty
(term sheet, umowy inwestycyjne, dokumentacja programów FENG, regulaminy) — prawdziwą przeglądarką
(Playwright), bo serwisy PFR stawiają zaporę cookie/JS i oddają pustą treść zapytaniom curl.

Instalacja (raz):   pip install playwright && python -m playwright install chromium
Użycie:             ./src/tools/pfr.py                 # strony startowe + dokumenty z nich podlinkowane
                    ./src/tools/pfr.py --deep          # dodatkowo podstrony PFR Ventures o programach i dokumentach
                    ./src/tools/pfr.py --list          # co zostałoby pobrane (bez pobierania dokumentów)
                    ./src/tools/pfr.py -f              # pobierz ponownie także istniejące pliki
                    ./src/tools/pfr.py --show          # z widocznym oknem przeglądarki
Wynik: src/legal/pfr/pfr_<nazwa>.html (strony) i src/legal/pfr/pfr_<nazwa>.<pdf|docx|xlsx> (dokumenty);
potem ./src/tools/extract_text.py zamienia PDF, HTML i DOCX na .txt.
"""
import sys, os, re, time, asyncio
from urllib.parse import urljoin, urlparse, unquote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from download_eu import LEGAL as _LEGAL, BAD_MARKERS, strip_tags, accept_cookies, route_filter  # noqa: E402
LEGAL = os.path.join(_LEGAL, "pfr")

# strony startowe: (nazwa pliku bez rozszerzenia, adres)
SEEDS = [
    ("pfr_pfrv_feng_dokumentacja", "https://pfrventures.pl/dokumentacja-programow-opartych-o-feng"),
    ("pfr_pfrv_otwarte_innowacje", "https://pfrventures.pl/program-dla-vc/pfr-otwarte-innowacje"),
    ("pfr_pfrv_starter", "https://pfrventures.pl/program-dla-vc/pfr-starter"),
    ("pfr_pfrv_biznest", "https://pfrventures.pl/program-dla-vc/pfr-biznest"),
    ("pfr_pfrv_koffi", "https://pfrventures.pl/program-dla-vc/pfr-koffi"),
    ("pfr_pfrv_programy", "https://pfrventures.pl/program-dla-vc"),
    ("pfr_pfrv_dla_startupow", "https://pfrventures.pl/dla-startupow"),
    ("pfr_startup_umowa_inwestycyjna", "https://startup.pfr.pl/artykul/prawo-w-umowie-z-vc-umowa-inwestycyjna"),
    ("pfr_startup_jak_wyglada_umowa", "https://startup.pfr.pl/artykul/jak-wyglada-umowa-inwestycyjna-z-vc"),
    ("pfr_startup_term_sheet", "https://startup.pfr.pl/artykul/co-jest-term-sheet-i-jak-wyglada"),
    ("pfr_startup_baza_wiedzy", "https://startup.pfr.pl/baza-wiedzy"),
]
DOC_EXT = (".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".zip")
PFR_HOSTS = ("pfrventures.pl", "pfr.pl", "startup.pfr.pl", "pfrsa.pl")
# słowa w adresie/tekście linku, które kwalifikują podstronę do pobrania w trybie --deep
PAGE_KEYS = ("dokument", "term-sheet", "termsheet", "umow", "wzor", "wzór", "feng", "program", "regulamin", "startup", "inwest")

def slug(s: str) -> str:
    s = unquote(s).lower()
    s = re.sub(r"[ąćęłńóśźż]", lambda m: "acelnoszz"["ąćęłńóśźż".index(m.group(0))], s)
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    return s[:80] or "plik"

def is_pfr(url: str) -> bool:
    return any(urlparse(url).netloc.endswith(h) for h in PFR_HOSTS)

def page_ok(html: str) -> bool:
    text = strip_tags(html)
    return len(text) > 1500 and not any(m.lower() in text[:3000].lower() for m in BAD_MARKERS)

async def get_page(ctx, url: str, wait_s: int = 10) -> str:
    page = await ctx.new_page()
    try:
        await page.goto(url, wait_until="domcontentloaded", timeout=45000)
        await accept_cookies(page)
        try:
            await page.wait_for_function("document.body && document.body.innerText.length > 1500", timeout=wait_s * 1000)
        except Exception:
            pass
        # listy dokumentów bywają renderowane skryptem po przewinięciu: przewiń i poczekaj na linki do plików
        try:
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await page.wait_for_selector("a[href$='.pdf'], a[href$='.docx'], a[href$='.xlsx'], a[href*='download']", timeout=6000)
        except Exception:
            pass
        await page.wait_for_timeout(1000)
        return await page.content()
    except Exception as e:
        print(f"  {url[:70]}: {str(e).splitlines()[0][:100]}"); return ""
    finally:
        await page.close()

def links(html: str, base: str):
    out = []
    for m in re.finditer(r"""<a\s[^>]*href\s*=\s*["']([^"'#]+)["'][^>]*>(.*?)</a>""", html, re.I | re.S):
        href = urljoin(base, m.group(1).strip()); text = strip_tags(m.group(2)).strip()
        out.append((href, text))
    return out

CT_EXT = {"application/pdf": ".pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document": ".docx",
          "application/msword": ".doc", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": ".xlsx",
          "application/vnd.ms-excel": ".xls", "application/zip": ".zip"}

async def save_doc(ctx, url: str, text: str, force: bool) -> str:
    """Pobiera dokument; nazwę i rozszerzenie bierze z nagłówka Content-Disposition, a gdy go nie ma — z adresu i Content-Type."""
    try:
        resp = await ctx.request.get(url, timeout=120000, max_redirects=5)
        if resp.status >= 400: return f"BLAD HTTP {resp.status}"
        cd = resp.headers.get("content-disposition", "")
        m = re.search(r"filename\*?=(?:UTF-8\'\')?\"?([^\";]+)", cd, re.I)
        fname = unquote(m.group(1)).strip() if m else os.path.basename(urlparse(url).path)
        stem, ext = os.path.splitext(fname)
        ext = ext.lower() if ext.lower() in DOC_EXT else CT_EXT.get(resp.headers.get("content-type", "").split(";")[0].strip(), "")
        if not ext: return "BLAD nie plik (HTML?)"
        name = slug(stem if m else (text or stem) + ("_" + stem if not m else ""))
        if "/en/" in url.lower() and not name.endswith("_en"): name += "_en"
        out = os.path.join(LEGAL, f"pfr_{name}{ext}")
        txt = os.path.splitext(out)[0] + ".txt"
        if not force and ((os.path.exists(out) and os.path.getsize(out) > 1000) or os.path.exists(txt)):
            return "SKIP"
        body = await resp.body()
        if len(body) < 1000: return f"BLAD {len(body)} B"
        os.makedirs(LEGAL, exist_ok=True)
        with open(out, "wb") as fh: fh.write(body)
        return f"OK {len(body)//1024} kB -> {os.path.basename(out)}"
    except Exception as e:
        return f"BLAD {str(e).splitlines()[0][:80]}"

async def run(argv):
    show = "--show" in argv; force = "-f" in argv; deep = "--deep" in argv; only_list = "--list" in argv
    from playwright.async_api import async_playwright
    os.makedirs(LEGAL, exist_ok=True)
    seen_pages, docs, pages_ok, pages_bad = set(), {}, 0, 0
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=not show)
        ctx = await browser.new_context(locale="pl-PL", viewport={"width": 1280, "height": 900},
                                        user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36")
        await ctx.route("**/*", route_filter)
        queue = list(SEEDS)
        while queue:
            name, url = queue.pop(0)
            if url in seen_pages: continue
            seen_pages.add(url)
            out = os.path.join(LEGAL, name + ".html"); txt = os.path.splitext(out)[0] + ".txt"
            html = await get_page(ctx, url)
            if not page_ok(html):
                print(f"BLAD  {name}  <- {url}  ({len(html)} B)"); pages_bad += 1; continue
            if force or not os.path.exists(txt):
                with open(out, "w", encoding="utf-8") as fh: fh.write(html)
            n_docs = len(re.findall(r"\.(pdf|docx|xlsx)", html, re.I))
            print(f"OK    {name}.html  ({len(html)//1000} kB, linków do plików: {n_docs})"); pages_ok += 1
            if n_docs == 0 and "dokumentacja" in name:
                print(f"      UWAGA: brak linków do dokumentów na {url}; pobierz je ręcznie z przeglądarki do src/legal/pfr/")
            for href, text in links(html, url):
                low = href.lower()
                if low.endswith(DOC_EXT) or "/document/" in low or "/download" in low or "/pobierz" in low or "/files/" in low or "/uploads/" in low:
                    docs.setdefault(href.split("?")[0] if low.endswith(DOC_EXT) else href, text)
                elif deep and is_pfr(href) and href not in seen_pages and any(k in low or k in text.lower() for k in PAGE_KEYS):
                    sub = "pfr_" + slug(urlparse(href).netloc.split(".")[0] + "_" + urlparse(href).path)
                    queue.append((sub, href))
        print(f"\nstrony: {pages_ok} OK, {pages_bad} błędów; dokumenty do pobrania: {len(docs)}")
        ok = bad = 0
        for href, text in docs.items():
            if only_list:
                print(f"  {href}  [{text[:60]}]"); continue
            r = await save_doc(ctx, href, text, force)
            print(f"{r:8.8} {href}" if r.startswith(("OK", "SKIP")) else f"{r}  {href}")
            ok += r.startswith("OK"); bad += r.startswith("BLAD")
        await browser.close()
    if not only_list:
        print(f"\ndokumenty: {ok} pobrane, {bad} błędów. Teraz: ./src/tools/extract_text.py")
    return 1 if (pages_bad or bad) else 0

def main(argv):
    try:
        import playwright.async_api  # noqa: F401
    except ImportError:
        print("Brak Playwright: pip install playwright && python -m playwright install chromium"); return 2
    return asyncio.run(run(argv))

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
