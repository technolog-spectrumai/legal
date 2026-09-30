#!/usr/bin/env python3
"""Wyciąga tekst z plików PDF (i HTML) w katalogu src/ i zapisuje obok jako .txt.

Użycie:  ./src/tools/extract_text.py            # wszystkie *.pdf, *.html, *.htm, *.xhtml w src/
         ./src/tools/extract_text.py plik.pdf   # wybrane pliki
         ./src/tools/extract_text.py -f         # nadpisz istniejące .txt (także z plików leżących już tylko w bkp/)
         ./src/tools/extract_text.py --keep     # nie usuwaj oryginałów z src/
Przebieg: oryginał jest kopiowany do src/bkp/, tekst zapisany jako <nazwa>.txt w src/, a po udanym zapisie
niepustego .txt oryginał jest usuwany z src/ (zostaje w bkp/). Przy błędzie oryginał zostaje.
Kolejność narzędzi dla PDF: pdftotext (poppler-utils) -> pypdf -> pdfminer.six.
Instalacja zapasowa: pip install pypdf   (albo: apt install poppler-utils)
"""
import sys, os, subprocess, shutil, re, html, glob
from html.parser import HTMLParser

SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # katalog src/ (skrypt leży w src/tools/)
BKP = os.path.join(SRC, "bkp")
EXTS = ("pdf", "html", "htm", "xhtml")

def pdf_to_text(path):
    if shutil.which("pdftotext"):
        r = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", path, "-"],
                           capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout, "pdftotext"
    try:
        from pypdf import PdfReader
        rd = PdfReader(path)
        pages = [(p.extract_text() or "") for p in rd.pages]
        return "\n\f".join(pages), "pypdf"
    except ImportError:
        pass
    try:
        from pdfminer.high_level import extract_text
        return extract_text(path), "pdfminer"
    except ImportError:
        raise RuntimeError("brak narzędzia: zainstaluj poppler-utils (pdftotext) albo `pip install pypdf`")

class _Text(HTMLParser):
    SKIP = {"script", "style", "noscript", "svg", "head", "nav", "header", "footer", "aside", "iframe"}
    def __init__(self):
        super().__init__(); self.out = []; self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP: self.skip += 1
        if tag in {"p", "div", "br", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6", "section", "article", "table"}:
            self.out.append("\n")
    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip: self.skip -= 1
        if tag in {"p", "div", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6"}:
            self.out.append("\n")
    def handle_data(self, data):
        if not self.skip: self.out.append(data)

def html_to_text(path):
    raw = open(path, "rb").read()
    for enc in ("utf-8", "cp1250", "iso-8859-2"):
        try: s = raw.decode(enc); break
        except UnicodeDecodeError: continue
    else: s = raw.decode("utf-8", "replace")
    p = _Text(); p.feed(s)
    t = html.unescape("".join(p.out))
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n\n", t)
    return t.strip() + "\n", "html.parser"

def main(argv):
    force = "-f" in argv
    keep = "--keep" in argv
    files = [a for a in argv if a not in ("-f", "--keep")]
    os.makedirs(BKP, exist_ok=True)
    if not files:
        files = sorted(sum((glob.glob(os.path.join(SRC, "*." + e)) for e in EXTS), []))
        if force:  # przy -f także pliki, które są już tylko w bkp/
            have = {os.path.basename(f) for f in files}
            files += sorted(f for f in sum((glob.glob(os.path.join(BKP, "*." + e)) for e in EXTS), [])
                            if os.path.basename(f) not in have)
    ok = bad = skip = 0
    for f in files:
        base = os.path.basename(f)
        in_bkp = os.path.dirname(os.path.abspath(f)) == os.path.abspath(BKP)
        out = os.path.join(SRC, os.path.splitext(base)[0] + ".txt")
        if not force and os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(f):
            # .txt aktualny: oryginał i tak przenosimy do bkp/ (np. pliki przepisane wcześniejszą wersją skryptu)
            if not in_bkp and not keep:
                dst = os.path.join(BKP, base)
                if not os.path.exists(dst) or os.path.getmtime(f) > os.path.getmtime(dst):
                    shutil.copy2(f, dst)
                os.remove(f)
                print(f"BKP   {base}  (.txt aktualny, oryginał -> bkp/)")
            skip += 1; continue
        try:
            text, tool = pdf_to_text(f) if f.lower().endswith(".pdf") else html_to_text(f)
            if not text.strip():
                raise RuntimeError("pusty wynik ekstrakcji (skan bez warstwy tekstowej?)")
            if not in_bkp:
                dst = os.path.join(BKP, base)
                if not os.path.exists(dst) or os.path.getmtime(f) > os.path.getmtime(dst):
                    shutil.copy2(f, dst)
            with open(out, "w", encoding="utf-8") as fh: fh.write(text)
            removed = ""
            if not in_bkp and not keep:
                os.remove(f); removed = ", oryginał -> bkp/"
            print(f"OK    {os.path.basename(out)}  ({tool}, {len(text)//1000} kB{removed})"); ok += 1
        except Exception as e:
            print(f"BLAD  {base}: {e} (oryginał zostaje)"); bad += 1
    print(f"\nzapisane: {ok}, pominięte: {skip}, błędy: {bad}; kopie oryginałów: {BKP}")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
