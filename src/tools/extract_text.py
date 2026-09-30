#!/usr/bin/env python3
"""Wyciąga tekst z plików PDF, HTML i DOCX w katalogu src/legal/ i zapisuje obok jako .txt.

Użycie:  ./src/tools/extract_text.py            # wszystkie *.pdf, *.html, *.docx w src/legal/ i podkatalogach (eu/, pfr/, web/)
         ./src/tools/extract_text.py plik.pdf   # wybrane pliki
         ./src/tools/extract_text.py -f         # nadpisz istniejące .txt (także z plików leżących już tylko w bkp/)
         ./src/tools/extract_text.py --keep     # nie usuwaj oryginałów z src/
Porządek przed konwersją: pliki 0-bajtowe są usuwane, katalogi *_files zapisane przez przeglądarkę idą do bkp/,
a strony EUR-Lex zapisane z przeglądarki (CELEX_..._EN_TXT.html, OJ_L_..._EN_TXT.html, "Traktat ... _ EUR-Lex.html")
dostają nazwy eu_<CELEX>_<nazwa>_<JEZYK>.html. Po przebiegu w src/legal/ zostają tylko pliki .txt (i .md).
Przebieg: oryginał jest kopiowany do src/legal/bkp/<podkatalog>/, tekst zapisany jako <nazwa>.txt obok oryginału,
a po udanym zapisie niepustego .txt oryginał jest usuwany (zostaje w bkp/). Przy błędzie oryginał zostaje.
Kolejność narzędzi dla PDF: pdftotext (poppler-utils) -> pypdf -> pdfminer.six.
Instalacja zapasowa: pip install pypdf   (albo: apt install poppler-utils)
"""
import sys, os, subprocess, shutil, re, html, glob
from html.parser import HTMLParser

SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "legal")  # katalog src/legal/
BKP = os.path.join(SRC, "bkp")
EXTS = ("pdf", "html", "htm", "xhtml", "docx")

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

def docx_to_text(path):
    """DOCX bez zależności: word/document.xml z archiwum ZIP, akapity i komórki tabel jako linie."""
    import zipfile
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8", "replace")
    xml = re.sub(r"<w:tab/>", "\t", xml)
    xml = re.sub(r"<w:(br|cr)/>", "\n", xml)
    xml = re.sub(r"</w:p>", "\n", xml)
    xml = re.sub(r"</w:tc>", "\t", xml)
    t = html.unescape(re.sub(r"<[^>]+>", "", xml))
    t = re.sub(r"[ \t]+\n", "\n", t)
    t = re.sub(r"\n\s*\n+", "\n\n", t)
    return t.strip() + "\n", "zipfile"

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

def eu_names():
    """CELEX -> nazwa z listy w download_eu.py (np. 32021R0821 -> dual_use)."""
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from download_eu import EU
        return {c: n for c, n, _ in EU}
    except Exception:
        return {}

def normalize_eu(path):
    """Strona EUR-Lex zapisana z przeglądarki (CELEX_..., OJ_L_..., 'Traktat ... _ EUR-Lex.html') -> eu_<CELEX>_<nazwa>_<JEZYK>.html.
    Wersja skonsolidowana (0YYYYRNNNN-data) jest zapisywana pod CELEX aktu podstawowego (3YYYYRNNNN)."""
    base = os.path.basename(path)
    if base.startswith("eu_") or not base.lower().endswith((".html", ".htm")): return path
    stem = os.path.splitext(base)[0]
    celex = lang = None
    m = re.match(r"CELEX[_:](\d)(\d{4})([A-Z])(\d{4})(?:-\d{8})?_([A-Z]{2})", stem)
    if m: celex, lang = f"3{m.group(2)}{m.group(3)}{m.group(4)}", m.group(5)
    m = re.match(r"OJ_L_(\d{4})(\d{5})_([A-Z]{2})", stem)
    if m: celex, lang = f"3{m.group(1)}R{int(m.group(2)):04d}", m.group(3)
    if "Traktat o funkcjonowaniu Unii Europejskiej" in stem: celex, lang = "12016E/TXT", "PL"
    if "Treaty on the Functioning of the European Union" in stem: celex, lang = "12016E/TXT", "EN"
    if not celex: return path
    name = eu_names().get(celex, "akt")
    new = os.path.join(os.path.dirname(path), f"eu_{celex.replace('/', '_')}_{name}_{lang}.html")
    if os.path.exists(new) and os.path.getsize(new) >= os.path.getsize(path): return path
    os.replace(path, new)
    print(f"NAZWA {base} -> {os.path.basename(new)}")
    return new

def tidy(root):
    """Porządek przed konwersją: usuwa pliki 0-bajtowe, przenosi katalogi *_files zapisane przez przeglądarkę do bkp/."""
    for d, dirs, names in os.walk(root):
        if os.path.abspath(d).startswith(os.path.abspath(BKP)): continue
        for n in names:
            f = os.path.join(d, n)
            if os.path.getsize(f) == 0:
                os.remove(f); print(f"PUSTY {os.path.relpath(f, root)}  (usunięty)")
        for x in list(dirs):
            if x.endswith("_files"):
                src = os.path.join(d, x); dst = os.path.join(BKP, os.path.relpath(src, root))
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                if os.path.exists(dst): shutil.rmtree(dst)
                shutil.move(src, dst); dirs.remove(x)
                print(f"BKP   {os.path.relpath(src, root)}/  (zasoby strony -> bkp/)")

def rel_of(f):
    """Ścieżka względem src/legal/ (albo bkp/), np. eu/plik.html; decyduje o miejscu .txt i kopii w bkp/."""
    f = os.path.abspath(f)
    for root in (os.path.abspath(BKP), os.path.abspath(SRC)):
        if f.startswith(root + os.sep):
            return os.path.relpath(f, root), root == os.path.abspath(BKP)
    return os.path.basename(f), False

def find(root):
    out = []
    for d, dirs, names in os.walk(root):
        dirs[:] = [x for x in dirs if os.path.join(d, x) != os.path.abspath(BKP) and x != "bkp"]
        out += [os.path.join(d, n) for n in names if n.lower().rsplit(".", 1)[-1] in EXTS]
    return sorted(out)

def main(argv):
    force = "-f" in argv
    keep = "--keep" in argv
    files = [a for a in argv if a not in ("-f", "--keep")]
    os.makedirs(BKP, exist_ok=True)
    if not files:
        tidy(SRC)
        files = [normalize_eu(f) for f in find(SRC)]
        if force:  # przy -f także pliki, które są już tylko w bkp/
            have = {rel_of(f)[0] for f in files}
            files += [f for f in find(BKP) if rel_of(f)[0] not in have]
    ok = bad = skip = 0
    for f in files:
        rel, in_bkp = rel_of(f)
        base = os.path.basename(f)
        out = os.path.join(SRC, os.path.splitext(rel)[0] + ".txt")
        dst = os.path.join(BKP, rel)
        os.makedirs(os.path.dirname(out), exist_ok=True); os.makedirs(os.path.dirname(dst), exist_ok=True)
        if not force and os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(f):
            # .txt aktualny: oryginał i tak przenosimy do bkp/ (np. pliki przepisane wcześniejszą wersją skryptu)
            if not in_bkp and not keep:
                if not os.path.exists(dst) or os.path.getmtime(f) > os.path.getmtime(dst):
                    shutil.copy2(f, dst)
                os.remove(f)
                print(f"BKP   {rel}  (.txt aktualny, oryginał -> bkp/)")
            skip += 1; continue
        try:
            low = f.lower()
            text, tool = pdf_to_text(f) if low.endswith(".pdf") else docx_to_text(f) if low.endswith(".docx") else html_to_text(f)
            if not text.strip():
                raise RuntimeError("pusty wynik ekstrakcji (skan bez warstwy tekstowej albo pusty plik)")
            if not in_bkp:
                if not os.path.exists(dst) or os.path.getmtime(f) > os.path.getmtime(dst):
                    shutil.copy2(f, dst)
            with open(out, "w", encoding="utf-8") as fh: fh.write(text)
            removed = ""
            if not in_bkp and not keep:
                os.remove(f); removed = ", oryginał -> bkp/"
            print(f"OK    {os.path.relpath(out, SRC)}  ({tool}, {len(text)//1000} kB{removed})"); ok += 1
        except Exception as e:
            print(f"BLAD  {rel}: {e} (oryginał zostaje)"); bad += 1
    print(f"\nzapisane: {ok}, pominięte: {skip}, błędy: {bad}; kopie oryginałów: {BKP}")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
