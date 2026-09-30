#!/usr/bin/env python3
"""Wyciąga tekst z plików PDF (i HTML) w katalogu src/ i zapisuje obok jako .txt.

Użycie:  ./src/extract_text.py            # wszystkie *.pdf i *.html w src/
         ./src/extract_text.py plik.pdf   # wybrane pliki
Kolejność narzędzi dla PDF: pdftotext (poppler-utils) -> pypdf -> pdfminer.six.
Instalacja zapasowa: pip install pypdf   (albo: apt install poppler-utils)
Istniejące .txt nowsze niż źródło są pomijane; -f wymusza nadpisanie.
"""
import sys, os, subprocess, shutil, re, html, glob
from html.parser import HTMLParser

SRC = os.path.dirname(os.path.abspath(__file__))

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
    SKIP = {"script", "style", "noscript", "svg"}
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
    files = [a for a in argv if a != "-f"]
    if not files:
        files = sorted(glob.glob(os.path.join(SRC, "*.pdf")) + glob.glob(os.path.join(SRC, "*.html")))
    ok = bad = skip = 0
    for f in files:
        out = os.path.splitext(f)[0] + ".txt"
        if not force and os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(f):
            skip += 1; continue
        try:
            text, tool = pdf_to_text(f) if f.lower().endswith(".pdf") else html_to_text(f)
            with open(out, "w", encoding="utf-8") as fh: fh.write(text)
            print(f"OK    {os.path.basename(out)}  ({tool}, {len(text)//1000} kB)"); ok += 1
        except Exception as e:
            print(f"BLAD  {os.path.basename(f)}: {e}"); bad += 1
    print(f"\nzapisane: {ok}, pominięte: {skip}, błędy: {bad}")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
