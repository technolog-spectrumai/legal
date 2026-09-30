# Źródła prawne do weryfikacji memorandum

`download.sh` pobiera akty prawne (ELI, ISAP, EUR-Lex), orzeczenia SN i strony rynkowe, na których opierają się `memorandum.tex` i `vc.md`. Uruchomić na komputerze bez proxy blokującego te serwisy:

```
./src/download.sh
```

Pliki trafiają do tego katalogu (poza git); `MANIFEST.txt` zawiera status każdej pozycji, `BLEDY.txt` pozycje nieudane. Po pobraniu można zweryfikować tezy oznaczone [W] w memorandum i zmienić je na [Z] albo poprawić.

Numery pozycji Dz.U. dla tekstów ujednoliconych ISAP są podane według pierwotnej publikacji aktu (ISAP udostępnia pod nią aktualny tekst ujednolicony). Jeżeli wzorzec adresu nie zadziała dla którejś pozycji, otwórz ją w ISAP ręcznie i zapisz pod nazwą z listy.

## Tekst z pobranych plików

`extract_text.py` wyciąga tekst z każdego `*.pdf` i `*.html` w tym katalogu i zapisuje plik `*.txt` (do przeszukiwania i cytowania w memorandum). Oryginał jest wcześniej kopiowany do `bkp/`, a po udanym zapisie usuwany z `src/`, więc po przebiegu w `src/` zostają tylko pliki `.txt`; `--keep` zostawia oryginały. `download.sh` traktuje plik jako pobrany, jeżeli istnieje w `src/`, w `bkp/` albo jako `.txt`.

```
./src/extract_text.py          # wszystkie pliki
./src/extract_text.py -f       # nadpisz istniejące .txt (także z bkp/)
./src/extract_text.py --keep   # nie usuwaj oryginałów
```

Wymaga `pdftotext` (pakiet poppler-utils) albo `pip install pypdf`. Pliki `.txt` też są poza git.
