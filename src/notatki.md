# Notatki robocze (źródła, narzędzia, spostrzeżenia)

Luźne obserwacje z prac nad memorandum i pobieraniem źródeł; rzeczy, które nie mieszczą się w memorandum, a mogą się przydać. Najnowsze na górze sekcji.

## Źródła i pobieranie

- **EUR-Lex** oddaje pustą treść zapytaniom bez przeglądarki (curl, także z nagłówkami), ale działa przez `context.request.get` Playwright po wejściu na stronę główną (ciasteczka). Adres `legal-content/<JEZYK>/TXT/HTML/?uri=CELEX:…` daje sam tekst aktu; strona „landing” aktu (tytuł „… | EUR-Lex”) zapisana z przeglądarki zawiera tylko metadane i nawigację, nie treść — `extract_text.py` po konwersji da krótki `.txt`, wtedy trzeba zapisać stronę z zakładki „Tekst”.
- **Wersje skonsolidowane** EUR-Lex mają CELEX z zerem na początku i datą (`02021R0821-20230526`); `extract_text.py` zapisuje je pod CELEX aktu podstawowego (`32021R0821`). Dla 2021/821 załącznik I jest aktualizowany co roku rozporządzeniem delegowanym; wersja z 26.05.2023 nie zawiera późniejszych zmian listy (2023, 2024, 2025) — do klasyfikacji produktu brać najnowszą konsolidację.
- **Rozporządzenie (UE) 2026/1386 z 17.06.2026 r. o kontroli inwestycji zagranicznych** (zapisane przez użytkownika jako `OJ_L_202601386_EN_TXT.html`, teraz `eu/eu_32026R1386_fdi_screening_2026_EN.txt`): uchyla 2019/452 z dniem 17.01.2028 r., stosowane od 17.01.2028 r., a art. 3 ust. 2, 15 ust. 2, 18 i 27–29 już od 16.07.2026 r. Memorandum (1.1.2, 1.4.1, T1) powołuje jeszcze 2019/452 — do memorandum 1.2 trzeba dodać nowy akt: podstawa art. 114 i 207 ust. 2 TFUE, obowiązkowe krajowe mechanizmy kontroli i minimalny zakres sektorowy (prawdopodobnie obejmie technologie podwójnego zastosowania i obronność), co może objąć Spółkę wcześniej niż polski próg 10 mln EUR. Dopisane do `download_eu.py` (PL i EN) i `todo.md`.
- **Strona „Traktat o funkcjonowaniu Unii Europejskiej _ EUR-Lex.html”** zapisana z przeglądarki to streszczenie (Summaries of EU legislation), nie tekst traktatu — usunięta; TFUE nadal do pobrania z adresu `TXT/HTML`.
- **sn.pl**: dawne adresy `OrzeczeniaHTML/*.docx.html` nie istnieją (404); orzeczenia trzeba szukać w bazie po sygnaturze (`Baza_orzeczen.aspx?Sygnatura=…`).
- **PFR Ventures**: strony mają zaporę cookie/JS (curl i czytnik r.jina.ai widzą tylko baner). Wzory term sheet FENG leżą pod `https://pfrventures.pl/document/1192` … `1196` (Starter, Biznest, OI, KOFFI — tylko EN, CVC), wersje EN pod `/en/document/NNNN`; nazwa pliku w nagłówku Content-Disposition.
- **ISAP** dla aktów sprzed 2012 r. wymaga identyfikatora z numerem Dziennika (`WDU20000941037`); prościej przez ELI API (`/api/acts/DU/<rok>/<poz>` → `fileName` → `/text/U/…Lj.pdf`).
- Pliki zapisane „stroną kompletną” z przeglądarki tworzą katalogi `*_files` — `extract_text.py` przenosi je do `bkp/`; w `src/legal/` mają zostać tylko `.txt` (i `.md`).

## Prawo — spostrzeżenia z weryfikacji (poza memorandum)

- **PCC a P.S.A.**: ustawa o PCC definiuje spółkę kapitałową jako sp. z o.o., S.A. i S.E. (art. 1a pkt 2) i liczy podstawę od kapitału zakładowego; P.S.A. literalnie nie podlega PCC przy zawiązaniu i podwyższeniu, ale też pożyczka akcjonariusza dla P.S.A. nie korzysta ze zwolnienia z art. 9 pkt 10 lit. i. Warto objąć interpretacją indywidualną (pkt 27 zakresu).
- **Program motywacyjny**: KSH ma dla P.S.A. warunkową emisję akcji (art. 300¹¹⁴–300¹¹⁸) i upoważnienie Rady do emisji na 5 lat do 1/4 akcji (art. 300¹¹⁰–300¹¹³); to gotowe ustawowe narzędzia ESOP, których projekt umowy nie używa. Wersja 1.0 memorandum błędnie twierdziła, że P.S.A. nie zna delegacji emisyjnej.
- **Nowelizacja KSH (Dz.U. 2026 poz. 176)**: od 18.02.2027 r. zgłoszenie podmiotu prowadzącego rejestr do KRS, 7 dni na zgłaszanie zmian danych do rejestru (grzywna do 20 000 zł, art. 594 § 1 pkt 2¹), PESEL niejawny dla innych akcjonariuszy, zastaw rejestrowy bez wpisu w rejestrze akcjonariuszy; spółki istniejące mają 2 lata na dostosowanie umów (do 18.02.2029).
- **Ustawa z 13.03.2026 r. (poz. 471)** w ustawie koncesyjnej zmienia tylko art. 44 (głębokość oznakowania broni 0,0762 mm) i art. 56; omówienia w sieci sugerowały szerszy zakres.
- **Kontrola inwestycji**: organem jest minister ds. gospodarki, nie Prezes UOKiK; ochrona dopiero przy przychodzie > 10 mln EUR (art. 12d ust. 4) — startup na starcie nie podlega.
- **PKD 2025**: wszystkie 19 kodów z § 4 umowy zgadza się co do znaku z rozporządzeniem; 72.10.Z istnieje.
- **Wykaz WT**: BSP są w WT V ust. 3 („oraz ich systemy i urządzenia… kierowania i kontroli lotu”); wyłączenie dla statków cywilnych dotyczy tylko WT V ust. 2 (załogowe). Oprogramowanie autonomii może być „technologią” z definicji pkt 12 i 15 załącznika.

## Prawo UE — spostrzeżenia z weryfikacji 1.2

- **EDF (2021/697)**: art. 5 określa państwa stowarzyszone jako członków EFTA będących członkami EOG; tekst nie wymienia Norwegii z nazwy. „Kontrola” to decydujący wpływ, także pośredni (art. 2 pkt 6); podmiot z siedzibą w UE, którego zarządcza struktura wykonawcza jest w państwie trzecim, traktuje się jak podmiot z państwa trzeciego (art. 2 pkt 24). Derogacja z art. 9 ust. 4 wymaga gwarancji zatwierdzonych przez państwo członkowskie.
- **2021/821, załącznik I (konsolidacja 2023)**: 9A012.b.1–b.2 mają status „Not used” — hipoteza „9A012.b.2 = autonomia” z `regulations.md` jest nieaktualna; BSP to 9A012.a, oprogramowanie do ich działania 9D004.e, technologia 9E001; 9A120 to zbiorniki paliwa rakietowego, nie BSP. Załącznik I zmieniano po 2023 r. — do klasyfikacji brać najnowszą konsolidację.
- **EU001** nie obejmuje Turcji; z krajów NATO/EOG obejmuje m.in. Norwegię, Islandię, Kanadę, USA, UK i Szwajcarię z Liechtensteinem — katalog UE/EOG/NATO w umowie (§ 27 ust. 6) nie pokrywa się z EU001.
- **AI Act**: wyłączenie z art. 2 ust. 3 dotyczy systemów wprowadzanych „wyłącznie” do celów wojskowych, obronnych lub bezpieczeństwa narodowego; produkt dual-use sprzedawany także cywilnie podlega rozporządzeniu. Stosowanie od 2.08.2026 r., art. 6 ust. 1 od 2.08.2027 r.
- **2026/877 (TTBER)**: art. 5 ust. 1 lit. a wyłącza spod zwolnienia grupowego także obowiązek przeniesienia (nie tylko licencji wyłącznej) ulepszeń na licencjodawcę; obowiązuje od 1.05.2026 do 30.04.2038.
- **PFR Otwarte Innowacje**: strona jest wewnętrznie niespójna — opis programu mówi o do 40% portfela w spółkach z zagraniczną siedzibą i polskimi founderami, FAQ o do 15% w spółkach z UE/EFTA/EOG+UK znacząco obecnych w Polsce. Memorandum podaje obie liczby.

## Narzędzia i repozytorium

- `build.sh` kompiluje `psa.tex` jako pierwszy, bo `memorandum.tex` i `psa_feedback.tex` biorą numery § z `psa.aux` (`xr-hyper`).
- `.gitignore`: `src/*` z wyjątkami `src/tools/`, `src/legal/`, `src/notatki.md`; `src/legal/bkp/` poza repozytorium.
- Memorandum jest składane z fragmentów w katalogu roboczym sesji (`memo_A1..A6.tex`, `memo_T.tex`, `assemble.py`, `check.sh`); komentarze `% UWAGA|`, `% DECYZJA|`, `% WERYFIKACJA|`, `% ZMIANA-W|` w fragmentach zasilają załączniki i podsumowanie.
