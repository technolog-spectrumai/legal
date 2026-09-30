#!/usr/bin/env python3
"""Pobiera akty prawa UE z EUR-Lex prawdziwą przeglądarką (headless Chromium przez Playwright), bo serwis
odpowiada pustą treścią albo stroną zastępczą na zapytania curl.

Instalacja (raz):   pip install playwright && python -m playwright install chromium
Użycie:             ./src/tools/download_eu.py            # wszystkie pozycje
                    ./src/tools/download_eu.py --show     # z widocznym oknem przeglądarki (gdy trzeba kliknąć zgodę)
                    ./src/tools/download_eu.py 32021R0697 # wybrane CELEX
Pliki: src/legal/eu_<CELEX>_<nazwa>_<jezyk>.html, potem ./src/tools/extract_text.py zamienia je na .txt.
"""
import sys, os, time, re

LEGAL = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "legal")
ITEMS = [  # (CELEX, nazwa, jezyk)
    ("32021R0697", "edf", "PL"), ("32021R0697", "edf", "EN"),
    ("32021R0821", "dual_use", "PL"),
    ("32019R0452", "fdi_screening", "PL"),
    ("32026R0877", "ttber_2026", "PL"), ("32026R0877", "ttber_2026", "EN"),
    ("32014R0316", "ttber_2014", "PL"),
    ("32024R1689", "ai_act", "PL"),
    ("32023R1230", "maszynowe", "PL"),
    ("32024R2847", "cra", "PL"),
    ("32019R0945", "uas_945", "PL"), ("32019R0947", "uas_947", "PL"),
    ("32014R0269", "sankcje_269", "PL"), ("32014R0833", "sankcje_833", "PL"),
    ("12016E/TXT", "tfue", "PL"), ("12016E/TXT", "tfue", "EN"),
]

def valid(html: str) -> bool:
    return len(html) > 20000 and re.search(r"Artyku|Article|Artikel", html) is not None

def main(argv):
    show = "--show" in argv
    only = {a for a in argv if not a.startswith("--")}
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Brak Playwright: pip install playwright && python -m playwright install chromium"); return 2
    os.makedirs(LEGAL, exist_ok=True)
    ok = bad = skip = 0
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not show)
        ctx = browser.new_context(locale="pl-PL", viewport={"width": 1280, "height": 900},
                                  user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36")
        page = ctx.new_page()
        # pierwsze wejście ustawia ciasteczka i ewentualne wyzwanie anty-botowe
        try:
            page.goto("https://eur-lex.europa.eu/homepage.html?locale=pl", wait_until="domcontentloaded", timeout=60000)
            for sel in ("button:has-text('Akceptuj')", "a:has-text('Akceptuję')", "a.wt-ecl-button:has-text('Accept')", "button:has-text('Accept all')"):
                try:
                    page.locator(sel).first.click(timeout=2000); break
                except Exception: pass
        except Exception as e:
            print(f"UWAGA strona główna: {e}")
        for celex, name, lang in ITEMS:
            if only and celex not in only: continue
            safe = celex.replace("/", "_")
            out = os.path.join(LEGAL, f"eu_{safe}_{name}_{lang}.html")
            txt = os.path.splitext(out)[0] + ".txt"
            if (os.path.exists(out) and os.path.getsize(out) > 20000) or os.path.exists(txt):
                print(f"SKIP  {os.path.basename(out)}"); skip += 1; continue
            url = f"https://eur-lex.europa.eu/legal-content/{lang}/TXT/HTML/?uri=CELEX:{celex}"
            html = ""
            for attempt in range(3):
                try:
                    page.goto(url, wait_until="domcontentloaded", timeout=90000)
                    # czekaj na treść aktu (do 60 s), strony bywają duże
                    for _ in range(60):
                        html = page.content()
                        if valid(html): break
                        time.sleep(1)
                    if valid(html): break
                except Exception as e:
                    print(f"  próba {attempt+1} {celex}: {e}")
                time.sleep(3)
            if valid(html):
                with open(out, "w", encoding="utf-8") as fh: fh.write(html)
                print(f"OK    {os.path.basename(out)}  ({len(html)//1000} kB)"); ok += 1
            else:
                snippet = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html))[:160]
                print(f"BLAD  {os.path.basename(out)}  <- {url}\n      odpowiedź: {len(html)} B: {snippet}"); bad += 1
        browser.close()
    print(f"\npobrane: {ok}, pominięte: {skip}, błędy: {bad}")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
