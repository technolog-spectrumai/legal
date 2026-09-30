# Źródła prawne do weryfikacji memorandum

`tools/download.sh` pobiera akty prawne (ELI, ISAP, EUR-Lex), orzeczenia SN i strony rynkowe, na których opierają się `memorandum.tex` i `vc.md`. Uruchomić na komputerze bez proxy blokującego te serwisy:

```
./src/tools/download.sh
```

Pliki trafiają do katalogu `src/legal/` (wersjonowane razem z `src/tools/`); `MANIFEST.txt` zawiera status każdej pozycji, `BLEDY.txt` pozycje nieudane. Po pobraniu można zweryfikować tezy oznaczone [W] w memorandum i zmienić je na [Z] albo poprawić.

Numery pozycji Dz.U. dla tekstów ujednoliconych ISAP są podane według pierwotnej publikacji aktu (ISAP udostępnia pod nią aktualny tekst ujednolicony). Jeżeli wzorzec adresu nie zadziała dla którejś pozycji, otwórz ją w ISAP ręcznie i zapisz pod nazwą z listy.

## Tekst z pobranych plików

`tools/extract_text.py` wyciąga tekst z każdego `*.pdf` i `*.html` w katalogu `src/` i zapisuje plik `*.txt` (do przeszukiwania i cytowania w memorandum). Oryginał jest wcześniej kopiowany do `bkp/`, a po udanym zapisie usuwany z `src/`, więc po przebiegu w `src/` zostają tylko pliki `.txt`; `--keep` zostawia oryginały. `download.sh` traktuje plik jako pobrany, jeżeli istnieje w `src/`, w `bkp/` albo jako `.txt`.

```
./src/tools/extract_text.py          # wszystkie pliki
./src/tools/extract_text.py -f       # nadpisz istniejące .txt (także z bkp/)
./src/tools/extract_text.py --keep   # nie usuwaj oryginałów
```

Wymaga `pdftotext` (pakiet poppler-utils) albo `pip install pypdf`. Pliki `.txt` też są poza git.

## Prawo UE

EUR-Lex odpowiada pustą treścią na proste zapytania, dlatego akty UE pobiera osobny skrypt z kilkoma strategiami (adresy ELI z sesją, negocjacja treści, serwer Urzędu Publikacji, PDF) i kontrolą, czy odpowiedź zawiera tekst aktu:

```
./src/tools/download_eu.sh
./src/tools/extract_text.py
```

Pozycje nieudane są w `src/legal/BLEDY_EU.txt` z adresem do zapisania strony ręcznie z przeglądarki.
