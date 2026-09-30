#!/usr/bin/env python3
"""Pobiera prawdziwą przeglądarką (headless Chromium przez Playwright) wszystkie źródła, których nie da się
pobrać przez curl: akty prawa UE z EUR-Lex (serwis oddaje pustą treść), orzeczenia SN, strony z zaporą
cookie/JS (PFR Ventures, BVCA) oraz pozostałe strony rynkowe, jeżeli ich pliki w src/legal/ są puste
albo zawierają stronę błędu.

Instalacja (raz):   pip install playwright && python -m playwright install chromium
Użycie:             ./src/tools/download_eu.py              # wszystko, czego brakuje albo co jest uszkodzone
                    ./src/tools/download_eu.py --show       # z widocznym oknem przeglądarki (gdy trzeba kliknąć zgodę)
                    ./src/tools/download_eu.py -f           # pobierz ponownie także pozycje już poprawne
                    ./src/tools/download_eu.py 32021R0697 sn_III_CZP_109_22   # wybrane pozycje (CELEX albo nazwa pliku)
                    ./src/tools/download_eu.py --list       # wypisz pozycje i ich stan, nic nie pobieraj
Wynik: src/legal/<nazwa>.html; potem ./src/tools/extract_text.py zamienia je na .txt (uszkodzone .txt są usuwane,
żeby extract_text.py je nadpisał).
"""
import sys, os, time, re

LEGAL = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "legal")

# --- prawo UE: (CELEX, nazwa, język) -> eu_<CELEX>_<nazwa>_<jezyk>.html
EU = [
    ("32021R0697", "edf", "PL"), ("32021R0697", "edf", "EN"),
    ("32021R0821", "dual_use", "PL"),
    ("32019R0452", "fdi_screening", "PL"),
    ("32026R0877", "ttber_2026", "PL"), ("32026R0877", "ttber_2026", "EN"),
    ("32014R0316", "ttber_2014", "PL"),
    ("32024R1689", "ai_act", "PL"),
    ("32023R1230", "maszynowe", "PL"),
    ("32024R2847", "cra", "PL"),
    ("32018R1139", "easa_1139", "PL"),
    ("32019R0945", "uas_945", "PL"), ("32019R0947", "uas_947", "PL"),
    ("32014R0269", "sankcje_269", "PL"), ("32014R0833", "sankcje_833", "PL"),
    ("12016E/TXT", "tfue", "PL"), ("12016E/TXT", "tfue", "EN"),
]

# --- pozostałe strony: (nazwa pliku bez rozszerzenia, [adresy do spróbowania po kolei], opis, wymagany ciąg w treści)
PAGES = [
    # orzeczenia SN: baza orzeczeń (wynik wyszukiwania po sygnaturze) i strony zagadnień prawnych
    ("sn_V_CSK_522_18", ["https://www.sn.pl/orzecznictwo/SitePages/Baza_orzeczen.aspx?Sygnatura=V%20CSK%20522/18",
                         "https://www.sn.pl/sites/orzecznictwo/OrzeczeniaHTML/v%20csk%20522-18-1.docx.html"],
     "SN V CSK 522/18 (pełnomocnictwo nieodwołalne)", "522/18"),
    ("sn_II_CSKP_593_22", ["https://www.sn.pl/orzecznictwo/SitePages/Baza_orzeczen.aspx?Sygnatura=II%20CSKP%20593/22",
                           "https://www.sn.pl/sites/orzecznictwo/OrzeczeniaHTML/ii%20cskp%20593-22.docx.html"],
     "SN II CSKP 593/22 (art. 64 KC)", "593/22"),
    ("sn_III_CSKP_65_21", ["https://www.sn.pl/orzecznictwo/SitePages/Baza_orzeczen.aspx?Sygnatura=III%20CSKP%2065/21",
                           "https://www.sn.pl/sites/orzecznictwo/OrzeczeniaHTML/iii%20cskp%2065-21-1.docx.html"],
     "SN III CSKP 65/21 (małżonek)", "65/21"),
    ("sn_III_CZP_109_22", ["https://www.sn.pl/orzecznictwo/SitePages/Baza_orzeczen.aspx?Sygnatura=III%20CZP%20109/22",
                           "https://www.sn.pl/sprawy/SitePages/Zagadnienia_prawne_SN.aspx?ItemSID=1718-301f4741-66aa-4980-b9fa-873e90506a11&ListName=Zagadnienia_prawne&Rok=2022"],
     "SN III CZP 109/22 (akcje a wspólność małżeńska)", "109/22"),
    ("sn_III_CZP_32_16", ["https://www.sn.pl/orzecznictwo/SitePages/Baza_orzeczen.aspx?Sygnatura=III%20CZP%2032/16",
                          "https://www.sn.pl/sprawy/SitePages/Zagadnienia_prawne_SN.aspx?ItemSID=786-16544171-be1b-4089-b74b-413997467af2&ListName=Zagadnienia_prawne&Rok=2016"],
     "SN III CZP 32/16", "32/16"),
    # strony z zaporą cookie / JS
    ("web_pfrv_feng_dokumentacja", ["https://pfrventures.pl/dokumentacja-programow-opartych-o-feng"],
     "PFR Ventures: dokumentacja programów FENG (wzory term sheet)", "term sheet"),
    ("web_pfrv_otwarte_innowacje", ["https://pfrventures.pl/program-dla-vc/pfr-otwarte-innowacje",
                                    "https://pfrventures.pl/en/program-dla-vc/pfr-otwarte-innowacje"],
     "PFR Otwarte Innowacje", "Otwarte Innowacje"),
    ("web_bvca_model_docs", ["https://www.bvca.co.uk/resource/model-documents/",
                             "https://www.bvca.co.uk/our-industry/model-documents/",
                             "https://www.bvca.co.uk/resource/model-documents-for-early-stage-investments"],
     "BVCA: model documents", "odel document"),
    # pozostałe strony rynkowe (pobierane tylko, gdy plik w src/legal/ jest pusty albo uszkodzony)
    ("web_pfr_umowa_inwestycyjna", ["https://startup.pfr.pl/artykul/prawo-w-umowie-z-vc-umowa-inwestycyjna"], "PFR: prawo w umowie z VC", "umow"),
    ("web_pfr_jak_wyglada_umowa", ["https://startup.pfr.pl/artykul/jak-wyglada-umowa-inwestycyjna-z-vc"], "PFR: jak wygląda umowa inwestycyjna", "umow"),
    ("web_pfr_term_sheet", ["https://startup.pfr.pl/artykul/co-jest-term-sheet-i-jak-wyglada"], "PFR: term sheet", "term sheet"),
    ("web_startuppoland_termsheet", ["https://standardy.startuppoland.org/wiedza/przed-inwestycja/term-sheet/"], "Startup Poland: standardy term sheet", "term sheet"),
    ("web_nvca_2025_press", ["https://nvca.org/press_releases/nvca-releases-2025-updates-to-model-legal-documents/"], "NVCA: aktualizacja 2025", "NVCA"),
    ("web_nvca_2025_foley", ["https://www.foley.com/insights/publications/2025/10/breaking-down-the-nvca-what-founders-and-vcs-need-to-know/"], "Foley: omówienie NVCA 10/2025", "NVCA"),
    ("web_nvca_model_docs", ["https://nvca.org/model-legal-documents/"], "NVCA: model legal documents", "NVCA"),
    ("web_nif_about", ["https://www.nif.fund/about/"], "NATO Innovation Fund", "NATO"),
    ("web_eu_startups_defence_investors", ["https://www.eu-startups.com/2026/09/the-21-european-investors-funding-natos-defence/"], "Inwestorzy obronni w Europie", "defence"),
    ("web_edf_gowling", ["https://gowlingwlg.com/en/insights-resources/articles/2026/the-european-defence-fund"], "EDF omówienie", "Defence Fund"),
    ("web_olesinski_poz471", ["https://olesinski.com/aktualnosci/nowe-zasady-obrotu-towarami-strategicznymi-8-kluczowych-zmian-dla-sektora-dual-use-i-zbrojeniowego/"], "Omówienie ustawy Dz.U. 2026 poz. 471", "strategiczn"),
    ("web_cgolegal_koncesja", ["https://cgolegal.pl/baza-wiedzy/biezace-doradztwo-prawne/koncesja-na-obrot-specjalny/"], "Wymogi koncesji MSWiA", "koncesj"),
    ("web_psa_uprzywilejowanie", ["https://prosta-spolka.pl/uprzywilejowanie-akcji-w-prostej-spolce-akcyjnej/"], "Uprzywilejowanie akcji w P.S.A.", "uprzywilejowan"),
    ("web_psa_biznes_gov", ["https://www.biznes.gov.pl/pl/portal/00168"], "biznes.gov.pl: P.S.A.", "prost"),
    ("web_prs_info", ["https://prs.ms.gov.pl/"], "Portal Rejestrów Sądowych", "Rejestr"),
    ("web_gus_pkd2025", ["https://www.biznes.gov.pl/pl/klasyfikacja-pkd"], "Wyszukiwarka PKD 2025", "PKD"),
]

BAD_MARKERS = ("Strona nie znaleziona", "Nie znaleziono strony", "404 Not found", "Page not found", "Title: 404",
               "Access Denied", "Just a moment", "Request Rejected")

def strip_tags(html: str) -> str:
    html = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", html)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html))

def valid_eu(html: str) -> bool:
    return len(html) > 20000 and re.search(r"Artyku|Article|Artikel", html) is not None

def valid_page(html: str, needle: str) -> bool:
    text = strip_tags(html)
    if len(text) < 1500: return False
    if any(m.lower() in text[:3000].lower() for m in BAD_MARKERS): return False
    return needle.lower() in text.lower()

def file_ok(path: str, needle: str = None) -> bool:
    """Czy istniejący plik (.html albo .txt) zawiera użyteczną treść."""
    if not os.path.exists(path) or os.path.getsize(path) < 1500: return False
    try:
        data = open(path, encoding="utf-8", errors="ignore").read()
    except OSError:
        return False
    if path.endswith(".html"):
        return valid_eu(data) if needle is None else valid_page(data, needle)
    head = data[:3000]
    if any(m.lower() in head.lower() for m in BAD_MARKERS): return False
    if needle is None: return re.search(r"Artyku|Article|Artikel", data) is not None
    return needle.lower() in data.lower()

def state(html_path: str, needle=None) -> str:
    txt = os.path.splitext(html_path)[0] + ".txt"
    if file_ok(txt, needle) or file_ok(html_path, needle): return "OK"
    if os.path.exists(txt) or os.path.exists(html_path): return "USZKODZONY"
    return "BRAK"

def targets():
    """Lista (klucze, ścieżka .html, adresy, opis, needle); needle=None oznacza akt UE."""
    out = []
    for celex, name, lang in EU:
        safe = celex.replace("/", "_")
        fn = f"eu_{safe}_{name}_{lang}"
        out.append(({celex, fn}, os.path.join(LEGAL, fn + ".html"),
                    [f"https://eur-lex.europa.eu/legal-content/{lang}/TXT/HTML/?uri=CELEX:{celex}",
                     f"https://eur-lex.europa.eu/legal-content/{lang}/TXT/?uri=CELEX:{celex}"],
                    f"EUR-Lex {celex} ({lang})", None))
    for fn, urls, desc, needle in PAGES:
        out.append(({fn}, os.path.join(LEGAL, fn + ".html"), urls, desc, needle))
    return out

def accept_cookies(page):
    for sel in ("button:has-text('Akceptuj')", "button:has-text('Akceptuję')", "a:has-text('Akceptuję')",
                "button:has-text('Zgadzam')", "a.wt-ecl-button:has-text('Accept')", "button:has-text('Accept all')",
                "button:has-text('Accept')", "button:has-text('Allow all')", "#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll",
                "button:has-text('Zezwól na wszystkie')", "button:has-text('OK')"):
        try:
            page.locator(sel).first.click(timeout=1500); return True
        except Exception:
            pass
    return False

def fetch(page, url: str, ok, wait_s: int = 60) -> str:
    html = ""
    for attempt in range(3):
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=90000)
            accept_cookies(page)
            for _ in range(wait_s):
                html = page.content()
                if ok(html): return html
                time.sleep(1)
        except Exception as e:
            print(f"  próba {attempt+1}: {e}")
        time.sleep(3)
    return html

def main(argv):
    show = "--show" in argv; force = "-f" in argv or "--force" in argv; only_list = "--list" in argv
    only = {a for a in argv if not a.startswith("-")}
    os.makedirs(LEGAL, exist_ok=True)
    todo = []
    for keys, out, urls, desc, needle in targets():
        if only and not (keys & only): continue
        st = state(out, needle)
        if only_list: print(f"{st:10} {os.path.basename(out)}  {desc}")
        if st == "OK" and not force: continue
        todo.append((out, urls, desc, needle))
    if only_list:
        print(f"\ndo pobrania: {len(todo)}"); return 0
    if not todo:
        print("Wszystkie pozycje są już pobrane (użyj -f, żeby pobrać ponownie)."); return 0
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Brak Playwright: pip install playwright && python -m playwright install chromium"); return 2
    ok = bad = 0
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not show)
        ctx = browser.new_context(locale="pl-PL", viewport={"width": 1280, "height": 900},
                                  user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36")
        page = ctx.new_page()
        if any(u.startswith("https://eur-lex") for _, urls, _, _ in todo for u in urls):
            try:  # pierwsze wejście ustawia ciasteczka EUR-Lex
                page.goto("https://eur-lex.europa.eu/homepage.html?locale=pl", wait_until="domcontentloaded", timeout=60000)
                accept_cookies(page)
            except Exception as e:
                print(f"UWAGA strona główna EUR-Lex: {e}")
        for out, urls, desc, needle in todo:
            check = valid_eu if needle is None else (lambda h, n=needle: valid_page(h, n))
            html = ""
            for url in urls:
                html = fetch(page, url, check, wait_s=60 if needle is None else 20)
                if check(html): break
            base = os.path.basename(out)
            if check(html):
                with open(out, "w", encoding="utf-8") as fh: fh.write(html)
                txt = os.path.splitext(out)[0] + ".txt"
                if os.path.exists(txt) and not file_ok(txt, needle):
                    os.remove(txt)  # uszkodzony .txt; extract_text.py zapisze nowy
                print(f"OK    {base}  ({len(html)//1000} kB)  {desc}"); ok += 1
            else:
                snippet = strip_tags(html)[:160]
                print(f"BLAD  {base}  {desc}\n      adresy: {' | '.join(urls)}\n      odpowiedź: {len(html)} B: {snippet}"); bad += 1
        browser.close()
    print(f"\npobrane: {ok}, błędy: {bad}")
    if ok: print("Teraz: ./src/tools/extract_text.py  (zamiana .html na .txt)")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
