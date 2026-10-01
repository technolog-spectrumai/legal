# Oczekiwania funduszy VC a projekt umowy P.S.A.: mapowanie, zalecenia i wnioski z case studies

Dokument wewnętrzny Basilisk Systems, informacyjny. Nie jest opinią prawną i nie zmienia umowy spółki. Zbiera w jednym miejscu wszystko, co z analizy funduszy venture capital, typów inwestorów, programów grantowych i studiów przypadku wynika dla projektu umowy spółki (`psa.tex`, wersja 0.9.4-C; numery § według `spis_tresci.md`): mapowanie oczekiwań funduszy na paragrafy, zalecenia zmian przed rundą i w rundzie, listę dokumentów do due diligence, mapowanie lekcji z czternastu studiów przypadku oraz odpowiedzi na pytania odłożone w `psa_todo.md`, `plan_prac.md` i memorandum.

Część rynkowa tej analizy (standard światowy, praktyka polska, fundusze zagraniczne i obronne, sprzeczności między funduszami), studia przypadku, typy inwestorów, inwestorzy polscy i sektorowi oraz programy grantowe są w repozytorium strategikon: `strategikon/vc/vc.md`, `strategikon/vc/case_studies/`, `strategikon/vc/vc_types.md`, `strategikon/vc/polish_vc.md`, `strategikon/vc/investors.md`, `strategikon/vc/grant.md` i `strategikon/strategy/biz/conclusions.md`. Tamte dokumenty nie odwołują się do numerów § umowy; każde odesłanie do umowy jest tutaj.

Stan na 1 października 2026 r. Oznaczenia wiarygodności jak w `regulations.md`: **[Z]** sprawdzone w źródle (lista na końcu), **[M]** prasa albo baza danych ze streszczenia wyszukiwarki, **[W]** wiedza ogólna o praktyce rynkowej, do potwierdzenia u kancelarii albo w rozmowie z funduszem, **[?]** hipoteza.

Numeracja sekcji zmieniła się wobec poprzedniej wersji tego pliku, na którą powołują się `memorandum.tex`, `plan_prac.md` i katalog `jurisdictions/`: dawne sekcje 2–7 (standard światowy, Polska, fundusze zagraniczne, różnice, fundusze obronne, sprzeczności) są teraz sekcjami 1–6 w `strategikon/vc/vc.md`; dawna sekcja 8 (mapowanie) to sekcja 2 poniżej, dawna 9 (zalecenia) to sekcja 3, dawna 10 (due diligence) to sekcja 4, dawna 11 (źródła) to sekcja 8.

## Spis treści

1. [Główny wniosek](#1-główny-wniosek)
2. [Mapowanie oczekiwań funduszy na projekt umowy](#2-mapowanie-oczekiwań-funduszy-na-projekt-umowy)
3. [Zalecenia: przed rundą i w rundzie](#3-zalecenia-przed-rundą-i-w-rundzie)
4. [Co fundusz sprawdzi w due diligence i gdzie to jest w repozytorium](#4-co-fundusz-sprawdzi-w-due-diligence-i-gdzie-to-jest-w-repozytorium)
5. [Mapowanie lekcji z case studies na projekt umowy](#5-mapowanie-lekcji-z-case-studies-na-projekt-umowy)
6. [Odpowiedzi na otwarte pytania z dokumentów Basiliska i decyzje przed rundą A](#6-odpowiedzi-na-otwarte-pytania-z-dokumentów-basiliska-i-decyzje-przed-rundą-a)
7. [Wnioski dla umowy z analiz typów inwestorów, inwestorów polskich i sektorowych oraz grantów](#7-wnioski-dla-umowy-z-analiz-typów-inwestorów-inwestorów-polskich-i-sektorowych-oraz-grantów)
8. [Źródła](#8-źródła)

---

## 1. Główny wniosek

Projekt umowy jest bliżej standardu VC niż typowa polska umowa założycielska: ma vesting założycieli, pulę ESOP, tag i drag, prawo pierwszeństwa, standard wyceny, katalog spraw zastrzeżonych i tryb rundy z listą dopuszczalnych warunków inwestorskich (§ 32 ust. 4). Cztery elementy będą przedmiotem negocjacji z każdym funduszem i warto je rozstrzygnąć przed rundą, nie w jej trakcie:

1. **Kryterium Bezpieczeństwa EU/NATO wobec funduszu i jego inwestorów** (§ 11 ust. 6 lit. b: beneficjenci rzeczywiści) — fundusz z inwestorami (LP) spoza UE/EOG/NATO nie spełni Kryterium bez zgody Walnego Zgromadzenia, a przekreślony wyjątek dla funduszy (§ 11 ust. 14) to jedyna furtka. Fundusze obronne i deep tech akceptują ograniczenia właścicielskie, ale nie akceptują badania każdego LP **[W]**.
2. **Swoboda obrotu wtórnego funduszu**: zgoda Spółki na każde rozporządzenie akcją (§ 12), prawo pierwszeństwa (§ 14) i Kryterium przy każdym nabyciu oznaczają, że fundusz nie może bez procedury przenieść akcji do funduszu następcy, spółki celowej albo wydać ich swoim LP przy likwidacji funduszu. Standard rynkowy to „permitted transfers” do podmiotów powiązanych **[W]**.
3. **Prawo weta inwestora**: umowa zna tylko progi 75 % wszystkich głosów (§ 25). Fundusz wymaga listy spraw wymagających jego zgody jako klasy akcji (protective provisions), niezależnie od tego, ile ma głosów **[W]**.
4. **Drag-along 75 % bez ochrony inwestora** (§ 16): fundusz zażąda, aby przymusowe współzbycie wymagało jego zgody, minimalnej ceny albo upływu okresu, oraz aby wypłata szła według waterfall z preferencją likwidacyjną **[W]**.

Reszta różnic to kwestia parametrów (wysokość puli, próg rundy, długość lock-upu), nie konstrukcji.

---

## 2. Mapowanie oczekiwań na projekt umowy

Oznaczenia stanu: **OK** — projekt spełnia standard; **CZ** — spełnia częściowo, do doprecyzowania; **BRAK** — nie ma, dodać w rundzie albo przed nią; **KOL** — koliduje ze standardem, do negocjacji.

| Oczekiwanie funduszu | § umowy | Stan | Co zrobić i kiedy |
|---|---|---|---|
| Czysty cap table, jedna klasa akcji zwykłych | § 5–6 | OK | wypełnić Załącznik nr 1 przed data room |
| Pula ESOP 10–15 % post-money przed rundą | § 8 (176 471 akcji, 15 % FD) | OK | po rundzie uzupełnienie puli wymaga uchwały 75 % (§ 8 ust. 9); ustalić w term sheet, kto ponosi rozwodnienie |
| Późniejsi współzałożyciele | § 9 (seria F, do 250 000 akcji) | CZ | fundusz zażąda, aby emisje serii F po rundzie wymagały jego zgody albo mieściły się w limicie ustalonym w rundzie **[W]** |
| Vesting założycieli 4 lata / 1 rok cliff | § 10 ust. 2 (48 miesięcy, 12 miesięcy) | OK | fundusz może chcieć „restartu” części vestingu przy rundzie albo uznania części za nabytą; Załącznik nr 2 musi być wypełniony |
| Bad leaver | § 10 ust. 5, 8 (80 % Wartości Godziwej dla nabytych, cena emisyjna dla nienabytych) | OK | standard rynkowy jest ostrzejszy (nabyte po niższej z ceny objęcia i FV); 80 % FV to pozycja pro-założycielska **[W]** |
| Double trigger po zmianie kontroli | § 10 ust. 10 | OK | doprecyzować „istotną przyczynę” (pytanie 1.5.6) |
| Wykonanie vestingu bez podpisu założyciela | § 10 ust. 13–15, umowa wykonawcza | CZ | fundusz przeczyta umowę wykonawczą w due diligence; musi istnieć przed rundą (etap C pkt 21) |
| Kryterium EU/NATO wobec inwestora | § 11 ust. 5–6, § 32 ust. 1 | KOL | przywrócić wyjątek dla funduszy (§ 11 ust. 14) w brzmieniu uszczelnionym: test na poziomie zarządzającego, siedziby i kontroli, wyłączenie wehikułów jednego inwestora, oświadczenie funduszu o braku kontroli LP spoza Kryterium (pytanie 1.4.3) |
| Utrata Kryterium przez inwestora | § 11 ust. 15 (zbycie w 6 miesięcy) | KOL | fundusz nie zaakceptuje przymusowego zbycia z powodu zmiany po stronie swoich LP; wyłączyć zdarzenia po stronie LP, zostawić zmianę kontroli nad zarządzającym **[W]** |
| Zgoda Spółki na zbycie akcji inwestora | § 12 ust. 1–3 | KOL | dodać „permitted transfers”: podmioty powiązane funduszu, fundusz następca, wydanie LP; bez zgody, bez prawa pierwszeństwa, z zachowaniem testu sankcyjnego i Kryterium na poziomie zarządzającego |
| Wariant A (ratalny) vs B (wyłączający) | § 12 ust. 3 | CZ | dla funduszu wariant A jest bezpieczniejszy (zawsze istnieje ścieżka wyjścia za Wartość Godziwą); wariant B bez „wentyla” będzie kwestionowany (pytania 1.2.4–1.2.5) |
| Lock-up założycieli | § 13 (12 miesięcy od wpisu) | CZ | fundusz oczekuje lock-upu do wyjścia albo 3–5 lat z wyjątkami; do ustalenia w rundzie, w umowie akcjonariuszy |
| ROFR: spółka, potem akcjonariusze | § 14 | CZ | inwestor chce pierwszeństwa dla siebie przed innymi akcjonariuszami i wyłączenia własnych przeniesień; nabycie własne przez Spółkę ograniczone art. 300⁴⁷ KSH |
| Tag-along | § 15 (powyżej 50 % głosów) | OK | fundusz może chcieć proporcjonalnego tag przy każdej sprzedaży założyciela **[W]** |
| Drag-along | § 16 (75 % wszystkich głosów) | KOL | dodać: zgoda inwestora (większość akcji uprzywilejowanych) albo okres ochronny, minimalna cena, wypłata według waterfall; po rundzie 20 % założyciele nie mają sami 75 % (`emisja/inwestor.md` sekcja 6 pkt 7) |
| Dziedziczenie, małżonek | § 17–18 | OK | rzadko negocjowane; fundusz sprawdzi spłatę spadkobierców jako ryzyko płynności |
| Standard wyceny | § 19 | OK | fundusz może chcieć własnego udziału w wyborze eksperta |
| Rada Dyrektorów: miejsce dla inwestora | § 21, § 32 ust. 4 lit. c | CZ | § 21 ust. 3 (Kryterium wobec dyrektora) może wykluczyć wskazaną osobę; obserwator jako alternatywa; rozważyć wyjątek za zgodą WZ |
| Głos dyrektora ds. zgodności | § 23 ust. 2 | CZ | fundusz zapyta, czy to weto jednej osoby; uzasadnienie eksportowe zwykle wystarcza, ale trzeba je opisać **[W]** |
| Protective provisions inwestora | § 25 (75 % wszystkich głosów) | BRAK | dodać w rundzie katalog spraw wymagających zgody serii inwestorskiej (zmiana praw serii, nowa seria równa lub wyższa, sprzedaż spółki, dług, dywidenda, wykup, podmioty powiązane, ESOP, budżet); umowa spółki plus umowa inwestycyjna |
| Prawa informacyjne | § 32 ust. 4 lit. d | CZ | szczegóły (kwartalne, roczne, budżet, inspekcja) w umowie inwestycyjnej |
| Pro-rata | § 32 ust. 4 lit. e | OK | mechanika w P.S.A. przez prawo poboru (art. 300¹⁰⁶ KSH) — sprawdzić, czy prawo poboru ustawowe nie jest szersze niż pro-rata (pytanie 3.3.3) |
| Preferencja likwidacyjna 1× non-participating | § 32 ust. 4 lit. a | OK | wymaga uprzywilejowania serii w umowie spółki i waterfall w umowie inwestycyjnej i przy drag (§ 16); § 37 ust. 4 przewiduje „prawa szczególne” |
| Antyrozwodnienie BBWA | § 32 ust. 4 lit. b | OK | mechanika emisji dodatkowych akcji wymaga uchwały o emisji (75 %); prawo poboru może z góry wyłączyć sama umowa spółki (art. 300¹⁰⁶ § 1 KSH), a większość 4/5 dotyczy tylko pozbawienia uchwałą; zobowiązanie do głosowania z § 32 ust. 3 (pytanie 3.3.1) |
| Zobowiązanie do głosowania za rundą | § 32 ust. 3 | CZ | skuteczność wobec akcjonariuszy do potwierdzenia; fundusz zażąda tego samego w umowie akcjonariuszy z karą umowną **[W]** |
| Instrumenty zamienne (SAFE, pożyczka) | § 31 ust. 4 | OK | uchwała 75 % jako Sprawa Zastrzeżona; konwersja to emisja z prawem poboru do wyłączenia (`emisja/inwestor.md` sekcja 4) |
| Ograniczenia finansowania | § 31 ust. 3–4, § 11 ust. 13 | OK | ust. 3 odsyła do testu Dopuszczalnego Nabywcy (sankcje), nie do Kryterium, więc venture debt spoza UE/NATO nie jest zakazany; Kryterium działa dopiero przy prawach do akcji (§ 11 ust. 13); zabezpieczenie na IP i warranty wymagają uchwały 75 % (ust. 4) — fundusz to zaakceptuje, ale zakres zabezpieczeń dla venture debt warto ustalić z góry w umowie akcjonariuszy **[W]** |
| Zakaz konkurencji założycieli | § 29 ust. 1–3 | CZ | po odejściu tylko na podstawie odrębnej umowy (umowa akcjonariuszy § Zakaz konkurencji); fundusz oczekuje 18 miesięcy–3 lat **[Z]** (web_pfr_umowa_inwestycyjna.txt) i kar umownych |
| Transakcje z podmiotami powiązanymi | § 29–30 | CZ | § 30 „[WYMAGA OPINII PRAWNIKA]”: fundusz zażąda zgody inwestora powyżej progu i pełnego ujawnienia |
| IP w spółce | § 7, § 26 | CZ | warunek zawieszający rundy: podpisane umowy przeniesienia praw od wszystkich Założycieli, pracowników i B2B (etap B, `krs/przeniesienie_praw.tex` w `plan_prac.md`) |
| Kontrola eksportu i sankcje | § 27–28 | OK | fundusze obronne uznają za atut; fundusz z USA sprawdzi ITAR |
| Dywidenda | § 34 ust. 2 (reinwestycja 36 miesięcy) | OK | fundusz i tak nie oczekuje dywidend |
| Impas | § 35 | OK | fundusze wolą brak mechanizmów buy-sell |
| Zgoda indywidualna na zmianę umowy | § 38 ust. 3 | BRAK | fundusz wymaga, aby zmiana praw jego serii wymagała jego zgody (pytanie 3.4.2); w P.S.A. częściowo wynika z ustawy przy uszczupleniu praw |
| Spory | § 38 ust. 4 | CZ | umowa inwestycyjna może mieć arbitraż; umowa spółki zostaje przy sądzie |
| Exit po 5–7 latach | — | BRAK | zobowiązanie do współdziałania przy wyjściu i zasady procesu sprzedaży w umowie akcjonariuszy |
| Oświadczenia i zapewnienia założycieli, no-shop, koszty | — | BRAK | wyłącznie w term sheet i umowie inwestycyjnej; poza umową spółki |

---

## 3. Zalecenia: przed rundą i w rundzie

**Przed rundą (etap A i B z `plan_prac.md`), w umowie spółki:**

1. Przywrócić § 11 ust. 14 w brzmieniu uszczelnionym (test zarządzającego i kontroli; wyłączenie wehikułów jednego inwestora; oświadczenie funduszu) — to jedyna zmiana, bez której rozmowa z większością funduszy deep tech zaczyna się od zgody WZ (pytania 1.4.1–1.4.3).
2. Dodać w § 12 ust. 7 kategorię „przeniesień dozwolonych” dla inwestora finansowego (podmioty powiązane, fundusz następca, wydanie LP), z zachowaniem testu sankcyjnego i Kryterium na poziomie zarządzającego.
3. W § 16 przewidzieć, że po Kwalifikowanej Rundzie przymusowe współzbycie wymaga zgody większości akcji serii inwestorskiej albo upływu okresu ochronnego oraz podziału ceny według uprzywilejowania.
4. W § 21 ust. 3 dopuścić dyrektora niespełniającego Kryterium za zgodą WZ 75 % (jak przy nabywcy), z ograniczeniem dostępu do Kluczowej Własności Intelektualnej według § 27 ust. 6.
5. Rozważyć zdefiniowanie już w umowie „serii I” z upoważnieniem do emisji (art. 300¹⁰³ KSH: maksymalna liczba, termin) i uprzywilejowaniem 1× non-participating, aby runda nie wymagała pełnej zmiany umowy w akcie notarialnym; do potwierdzenia u kancelarii, czy uprzywilejowanie serii można ustalić z góry dla akcji jeszcze niewyemitowanych **[?]**.
6. Wypełnić progi § 32 ust. 1 (D9) i Załączniki nr 1–3; podpisać umowę wykonawczą vestingu i przeniesienia IP — bez nich due diligence zatrzyma się na pierwszym tygodniu.

**W rundzie, w umowie inwestycyjnej i umowie akcjonariuszy (nie w umowie spółki):** protective provisions, prawa informacyjne, lock-up do wyjścia, exit, oświadczenia i zapewnienia, kary umowne, zobowiązania do głosowania, no-shop, koszty, prawo właściwe i arbitraż, waterfall. Podział między umowę spółki a umowę akcjonariuszy porządkuje sekcja T8 memorandum (pkt 13 zakresu).

**Czego nie oddawać:** Kryterium co do kontroli nad Spółką (warunek EDF, AGILE, DIANA i koncesji), § 27 ust. 6 i § 28 (bez nich programy obronne są niedostępne), obowiązki związane z akcją w rejestrze (§ 10 ust. 14). Fundusze obronne oczekują tych ograniczeń; fundusze generalistyczne trzeba do nich przekonać opisem programów, do których dają dostęp (`regulations.md` sekcja 3).

---

## 4. Co fundusz sprawdzi w due diligence i gdzie to jest w repozytorium

| Pytanie inwestora | Dokument |
|---|---|
| Kto ma jakie akcje, po jakiej cenie, za jaki wkład | `psa.tex` § 5–7, Załącznik nr 1 |
| Czy IP należy do spółki | § 26, umowy przeniesienia praw (do przygotowania), Załącznik nr 3 (licencje OSS, prawa osób trzecich) |
| Czy założyciele mają vesting i jak jest wykonywany | § 10, Załącznik nr 2, umowa wykonawcza (`shareholder_agreement.tex`) |
| Kto może kupić akcje i jak wychodzi inwestor | § 11–16, sekcja 2 tego dokumentu |
| Jak spółka podejmuje decyzje | § 21–25, `extra.tex` Dokument nr 3, regulamin Rady (do przygotowania) |
| Zgodność eksportowa i sankcyjna, klasyfikacja produktów | § 27–28, `regulations.md`, program zgodności (do przygotowania) |
| Podatki ESOP i aportu | `extra.tex` Dokument nr 6, interpretacja indywidualna (pkt 27) |
| Zakaz konkurencji i inne aktywności założycieli | § 29, Załącznik nr 3, umowa akcjonariuszy |
| Umowy z pracownikami i B2B | do przygotowania (`psa_todo.md` sekcja 4) |

---

## 5. Mapowanie lekcji z case studies na projekt umowy

Studia przypadku (Swarmer, WB Electronics, ICEYE, Catalyst, Anduril, Shield AI, Helsing, Destinus, Tekever, Milrem, Creotech, APS, Figure AI, Nomagic) są w repozytorium strategikon w katalogu `strategikon/vc/case_studies/`; tutaj zebrano wyłącznie ich część dotyczącą umowy spółki. Oznaczenia stanu jak w sekcji 2: **OK** — umowa to przewiduje; **CZ** — częściowo; **BRAK** — dodać; **KOL** — koliduje; **DEC** — wymaga decyzji Założycieli.

### 5.1 Przegląd: wspólne lekcje z trzynastu case studies

| Lekcja | Skąd | Gdzie u nas | Stan | Co zrobić |
|---|---|---|---|---|
| P.S.A. nie może być notowana (art. 300³⁶ § 2 KSH); droga na giełdę zaczyna się od przekształcenia w S.A. i zdjęcia ograniczeń obrotu | Swarmer, WB | § 25 ust. 1 lit. e; § 10–16; sekcja 2 tego dokumentu („Exit": BRAK) | BRAK | ścieżka giełdowa w umowie akcjonariuszy: przekształcenie, zobowiązanie do głosowania, lock-up, co zastępuje Kryterium po debiucie |
| Kryterium § 11 zderza się z każdą z trzech dróg: matka w USA (Swarmer), JV z Koreą i produkcja w Ukrainie (WB), inwestorzy z Japonii i Kataru (ICEYE) | wszystkie | § 11 ust. 6 i 14, § 33 ust. 4, § 25 ust. 1 lit. n; `regulations.md` sekcja 3 (art. 9 EDF: kontrola, nie udział) | DEC | rozstrzygnąć przed rundą: limit kontroli spoza UE/EOG dla programów UE, ścieżka zgody 75 % dla mniejszościowych inwestorów i partnerów spoza Kryterium, przywrócenie ust. 14 dla funduszy |
| Kapitał państwowy wchodzi późno i jako mniejszość: PFR po 20 latach, Solidium po 10, Tesi po 4; dla startupu droga wiedzie przez fundusze PFR, EIF, EIC Fund i wehikuły BGK | WB, ICEYE | `regulations.md` sekcja 3; `psa_todo.md` sekcja 6 | CZ | plan finansowania w szczeblach z nazwanymi wehikułami państwowymi; wszystkie spełniają Kryterium (kontrola państwa UE) |
| Punktem przegięcia jest pierwszy kontrakt publiczny, nie runda: WB 1998, ICEYE 2020 i 2025; Swarmer bez niego ma 0,3 mln USD przychodów mimo 100 tys. misji | wszystkie | § 31 ust. 1 (zamówienia, zaliczki, programy B+R), § 33 | CZ | pierwszy płatny pilot z producentem albo praca rozwojowa dla Agencji Uzbrojenia przed rundą A |
| Granty obniżają rozwodnienie, ale nie zastępują klienta: ICEYE ok. 83 mln EUR (7 % kapitału) użyte jako dźwignia do VC; Swarmer 50 tys. USD; WB zero | ICEYE, Swarmer | `psa_todo.md` sekcja 6 (EIC, SMART, DIANA) | OK | wniosek do EIC przed rundą A; grant jako argument w wycenie |
| JV i konsorcja z koncernami: Rheinmetall 60/40 jako strona kontraktu 1,7 mld EUR, Hanwha 51/49, ICEYE Polska z WZŁ-1 | ICEYE, WB | § 33 ust. 1–5 (mniejszość dopuszczalna, IP w Spółce, licencja niewyłączna, prawa przy braku kontroli) | OK | wzór umowy JV (etap C pkt 25) według modelu ICEYE–Rheinmetall; PGZ jako partner konsorcjum |
| Próg 25 %: PFR z 26,44 % blokuje uchwały kwalifikowane; w umowie Basiliska 75 % wszystkich głosów oznacza, że każdy pakiet powyżej 25 % blokuje | WB | § 25 ust. 1; § 32 ust. 2; § 25 ust. 1 lit. j (umorzenie zmienia proporcje) | CZ | maksymalny udział inwestora w uchwale kierunkowej; skutki umorzeń w umowie akcjonariuszy |
| Ład przez wzrost: przewodniczący z własną spółką i odejście założyciela-CEO cztery miesiące po IPO (Swarmer) kontra kontrola założycieli przez 29 lat (WB) | Swarmer, WB | § 10 (vesting, Odejście Dobrowolne), § 21 ust. 3, § 23 ust. 2, § 25 ust. 1 lit. h, § 29–30 | OK | nie oddawać tych postanowień w rundzie; vesting przeżywa przekształcenie |
| Dług dopiero przy przepływach: WB pierwsze obligacje po 17 latach, przy 300 mln zł przychodów, WIBOR + 2–3,7 pp; obligacje nie wymagają S.A. | WB | `catalyst.md`; § 31 ust. 4–5; § 25 ust. 1 lit. k; § 34 ust. 3 | OK | Plan Finansowania z kategorią „dług publiczny"; klauzula o obligacjach w § 31 do rozważenia |
| Płynność bez IPO: odsprzedaż ok. 600 mln EUR w rundach ICEYE; u Swarmera lock-up i −41 % w tydzień; u WB brak płynności do dziś | ICEYE, Swarmer | § 12, § 14, § 11 (Kryterium przy każdym nabyciu); sekcja 2 tego dokumentu („permitted transfers") | KOL | szybka ścieżka zgody Spółki i wyłączenia prawa pierwszeństwa dla nabywców zweryfikowanych w rundzie |
| Horyzont: 34 miesiące (Swarmer, software), 11 lat do rentowności (ICEYE, sprzęt), 29 lat (WB, produkcja) | wszystkie | § 34 ust. 2 (reinwestycja 36 miesięcy); `strategikon/vc/vc.md` sekcja 5 | CZ | horyzont w umowie akcjonariuszy zależnie od wariantu: softwarowy albo produkcyjny |
| Miejsce rejestracji a polski „nexus": ICEYE fińskie z centrum operacyjnym w Warszawie i kontraktem MON; Swarmer amerykańskie z zespołem w Kijowie i Warszawie; WB polskie z produkcją w Ukrainie | wszystkie | `psa_todo.md` sekcja 1 | DEC | zamówienia publiczne wymagają podmiotu i zdolności w kraju zamawiającego, nie siedziby matki; struktura holdingowa tylko przed pierwszą rundą |
| Autonomia może być kupowana jako osobna pozycja pod rządową architekturą referencyjną (USAF A-GRA, niemiecki CFSN) i licencjonowana suwerennym OEM | Shield AI, Helsing | § 33 ust. 3; `regulations.md` sekcja 4 | BRAK | interfejsy zgodne z A-GRA i CFSN; produkt typu „Enterprise" dla producentów; precedens A-GRA w rozmowach z MON i PGZ |
| Czyste oprogramowanie dochodzi do programów of record przez platformę prima albo własny nośnik; posiadanie sprzętu kosztuje (V-BAT, HX-2) | Anduril, Shield AI, Helsing | § 33; sekcja 3a tego pliku | DEC | pakiet autonomii w konsorcjum sprzętowym (PGZ, WB, Saab); rozdzielić w umowach metryki autonomii od płatowca i wyrzutni |
| Siedziba holdingu idzie za prawem eksportowym i budżetami klientów; spółka zależna w kraju zamawiającego założona wcześnie | Destinus, Tekever, Anduril | `jurisdictions/README.md` sekcje 1 i 4.2; § 33 | OK | matka w Polsce; pierwsza spółka zależna po pierwszym kontrakcie (kolejność w `jurisdictions/README.md` sekcja 4.2) |
| Exit albo inwestor większościowy spoza UE uruchamia art. 9 EDF; ratunkiem są gwarancje państwa członkowskiego | Milrem | § 11; `jurisdictions/kryteria.md` sekcja 3 | OK | w umowie inwestycyjnej: exit poza Kryterium tylko po uchwale 75 % i rozmowie z MON o gwarancjach |
| Inwestor kotwiczny z mandatem wielorundowym obniża ryzyko każdej kolejnej rundy (Founders Fund 5 z 9 rund, Prima Materia A i D, Khosla każda runda) | Anduril, Helsing, Nomagic | `strategikon/vc/vc.md` sekcje 2–3; § 32 | CZ | szukać inwestora rundy A z kapitałem na B i C (NIF, PFR, EIF); pro-rata w umowie inwestycyjnej |
| Kapitał uprzywilejowany PE i banków przed akcjami zwykłymi pojawia się przy 5–13 mld USD (Blackstone w Shield AI) | Shield AI | § 31 ust. 4; § 6–8 (rodzaje akcji) | CZ | sprawdzić, czy umowa dopuszcza serie uprzywilejowane o stałej stopie i liquidation preference |
| Polska giełda działa dla deep techu z kotwicą publiczną: NewConnect (11 mln zł) → GPW (40 mln zł) → emisje po kontraktach; wymaga S.A. i rozwadnia założycieli do 6–7 % | Creotech, APS | § 25 ust. 1 lit. e; art. 300³⁶ § 2 KSH | DEC | zdecydować, czy Założyciele akceptują rozwodnienie poniżej 25 % w zamian za giełdę; jeśli nie, droga WB i APS |
| MON przychodzi po sojusznikach (APS: UK dla Ukrainy 2022 r., SAN 2026 r.; Creotech: MikroGlob po 12 latach), ale wtedy mnoży przychód | APS, Creotech | `jurisdictions/polska.md` sekcja 7; `psa_todo.md` sekcja 6 | DEC | plan etapu C z pierwszym klientem sojuszniczym finansowanym przez darczyńcę i MON jako drugim |
| Banki rozwoju (EBI venture debt, EBOR) i gwarancje bankowe pod prime'a wypełniają lukę serii B bez rozwodnienia | Nomagic, APS | § 31; `strategikon/vc/vc.md` sekcja 5 | BRAK | EBI, EBOR, EIF Defence Equity Facility i gwarancje BGK w planie finansowania etapu C |
| Fizyczne AI pełnego stosu kosztuje 1–2 mld USD przed przychodem; własność modelu i danych z wdrożeń to aktywo, za które płacą inwestorzy | Figure AI, Nomagic | § 26; wzór umowy pilota (etap C pkt 25) | BRAK | prawa do danych treningowych w każdym pilocie; Basilisk jako warstwa oprogramowania |
| Dokumentacja bezpieczeństwa pokazana inwestorom musi przetrwać rundę; zamrożona specyfikacja u powolnego zamawiającego niszczy reputację | Figure AI, APS | § 23 ust. 2; § 29–30 | CZ | polityka bezpieczeństwa systemów autonomicznych w data room; klauzula spiralnej aktualizacji w umowach z MON |

### 5.2 Swarmer

| Lekcja ze Swarmera | Gdzie u nas | Stan | Co zrobić i kiedy |
|---|---|---|---|
| **Spółka-matka w USA daje dostęp do kapitału i Nasdaq, ale oddaje kontrolę poza UE.** Kryterium § 11 dopuszcza kontrolę z USA (NATO), lecz art. 9 EDF wyklucza firmę kontrolowaną przez podmiot z państwa niestowarzyszonego; to samo AGILE i EUDIS | § 11 ust. 6; `regulations.md` sekcje 3 i 3a; `psa_todo.md` sekcja 1 (pytanie o jurysdykcję) | DEC | Traktować „drogę Swarmera" (matka w USA) i „drogę EDF" jako wykluczające się. Jeżeli kapitał z USA, to przez spółkę zależną w USA dla kontraktów amerykańskich (wzór: ICEYE US), nie przez matkę. Rozstrzygnąć przed uchwałą kierunkową z § 32 ust. 2 **[W]** |
| **P.S.A. nie może być notowana**: art. 300³⁶ § 2 KSH zakazuje dopuszczenia i wprowadzenia jej akcji do obrotu zorganizowanego, czyli także na NewConnect **[Z]/[W]** | § 25 ust. 1 lit. e (przekształcenie: 75 % wszystkich głosów); sekcja 2 tego dokumentu, wiersz „Exit" (BRAK) | BRAK | W umowie akcjonariuszy zapisać ścieżkę giełdową: przekształcenie w S.A. (art. 551 KSH **[W]**), zobowiązanie do głosowania, harmonogram 12–18 miesięcy, które ograniczenia (§ 10–16, Kryterium) wygasają, a które przechodzą do umowy akcjonariuszy. Do rozmowy z kancelarią na etapie C |
| **Ograniczenia obrotu nie przeżyją giełdy**: zgoda Spółki na zbycie, prawo pierwszeństwa, Kryterium przy każdym nabyciu, obowiązki związane z akcją w rejestrze | § 10 ust. 14, § 11, § 12, § 14 | KOL | Świadomie: te mechanizmy są na fazę prywatną; po debiucie zdematerializowane akcje w KDPW nie niosą obowiązków z rejestru P.S.A. Zapisać w umowie akcjonariuszy, co zastępuje Kryterium po debiucie (lock-up, zobowiązania wobec MON, statut S.A.) **[W]** |
| **SAFE z kilkoma capami zamieniają się na kilka podserii uprzywilejowanych po różnych cenach** | § 31 ust. 4 (instrument zamienny jako Sprawa Zastrzeżona 75 %); konwersja jako emisja z pozbawieniem prawa poboru 4/5 (§ 25 ust. 2); `emisja/inwestor.md` sekcja 4 | CZ | Jeżeli pre-seed na SAFE: jedna uchwała 75 % dla wszystkich SAFE, jednolity cap albo z góry policzone ceny konwersji, oświadczenia z § 11 ust. 8 w treści SAFE; konwersję zaplanować jako jedną emisję z kilkoma cenami emisyjnymi **[W]** |
| **Nieprzejrzysty wehikuł jako największy akcjonariusz** (Theseus Capital Partners LLC, 22 %, nigdy nienazwany) | § 11 ust. 4 i ust. 6 lit. b (beneficjenci rzeczywiści), ust. 8–10 (dokumenty, wstrzymanie transakcji), przekreślony ust. 14 | KOL | Utrzymać wymóg ujawnienia beneficjentów rzeczywistych przed emisją; przywrócić ust. 14 w brzmieniu z sekcja 3 tego dokumentu pkt 1; wehikuł jednego inwestora bez ujawnienia beneficjentów nie przechodzi weryfikacji |
| **Odejście założyciela-CEO po 38 miesiącach i wykonanie opcji na 4 mln akcji** | § 10 ust. 2 (48 miesięcy, klif 12), ust. 5 i 8 (Odejście Dobrowolne: akcje nienabyte po cenie emisyjnej), ust. 10 (double trigger) | OK | Umowa jest surowsza niż praktyka Swarmera. W umowie akcjonariuszy dopisać, że vesting przeżywa przekształcenie i IPO, z zamianą obowiązku związanego z akcją na zobowiązanie umowne **[W]** |
| **Przewodniczący rady z własną spółką, w której emitent bierze 20 %** (Vectus), i zmiana strategii cztery miesiące po IPO | § 21 ust. 3 (Kryterium wobec dyrektora), § 23 ust. 2 (głos dyrektora ds. zgodności), § 25 ust. 1 lit. h (zmiana strategii: 75 %), § 29 ust. 4–13 i § 30 (transakcje z podmiotami powiązanymi) | OK | Bez zmian; przy rundzie nie oddawać § 25 lit. h ani § 29–30 (sekcja 3 tego dokumentu, „czego nie oddawać") |
| **Lock-up 180 dni na 59 % kapitału i −41 % po jego wygaśnięciu** | § 13 (12 miesięcy od wpisu; inny cel); sekcja 2 tego dokumentu, wiersz „Lock-up" (CZ) | CZ | Lock-up giełdowy negocjuje się z gwarantem; w umowie akcjonariuszy zobowiązanie Założycieli do zwyczajowego lock-upu (180–360 dni) i do skoordynowanej sprzedaży po nim **[W]** |
| **Model B2B2G: licencje dla producentów, przychód dopiero z kontraktów wolumenowych** (16 tys. licencji za 2,86 mln USD) | § 33 ust. 3 (licencja niewyłączna, ograniczona zakresem, wypowiadalna przy zmianie kontroli), § 28 (eksport), § 23 ust. 1 lit. h | OK | We wzorze umowy spółki celowej (etap C pkt 25 w `plan_prac.md`) dodać licencję liczoną „na platformę" z raportowaniem wolumenów i audytem; w data room pokazać koncentrację klientów jako ryzyko znane i zarządzane |
| **Kontraktowanie z klientami z NATO przez spółkę w UE** (Swarmer Estonia OÜ) | `regulations.md` sekcje 2.2 i 4 (bramki G2, G5), § 28 | OK | Basilisk jest w UE od początku; odpowiednikiem problemu Swarmera jest eksport do UK i USA (EU001, rejestracja w MRiT przed pierwszym transferem) |
| **Pieniądze bezzwrotne nie zastąpiły klienta**: 50 tys. USD grantu, 0,3 mln USD przychodu, potem giełda | § 31 ust. 1 (katalog: zaliczki, zamówienia, programy B+R); `psa_todo.md` sekcja 6 (EIC, SMART, DIANA) | CZ | Granty planować jako obniżenie rozwodnienia w fazie TRL 4–6, nie jako model przychodowy; pierwszy płatny pilot z producentem (odpowiednik SkyKnight) przed rundą A |
| **Próg Kwalifikowanej Rundy 2 mln zł jest na poziomie seedu Swarmera**; wycena serii A ≈ 66 mln USD przy 0,3 mln USD przychodów | § 32 ust. 1 (pola do uzupełnienia) | CZ | Uzupełnić próg kwotowy i próg wyceny (D9 w `plan_prac.md`); nie kopiować wycen z 2026 r., bo rynek defense tech jest w „hype cycle" (określenie CEO Andurila) |
| **Spółka-matka zarejestrowana od pierwszego dnia, bez późniejszego flipu** | § 1–2; `psa_todo.md` sekcja 1 | DEC | Jeżeli struktura holdingowa ma powstać, to przed pierwszą rundą; przekształcenie transgraniczne po rundzie kosztuje (podatek od niezrealizowanych zysków, ciągłość programu motywacyjnego, ponowna weryfikacja Kryterium) |

Czego Swarmer nie rozstrzyga, a co Basilisk musi wiedzieć przed rundą: polskie odpowiedniki mikro-IPO to NewConnect i rynek główny GPW, oba dostępne dopiero po przekształceniu w S.A.; w 2022–2023 r. tą drogą poszły polskie spółki kosmiczne Creotech Instruments (rynek główny) i Scanway (NewConnect) **[W]**, a w 2026 r. IPO na GPW przygotowuje WB Electronics (`strategikon/vc/case_studies/wb_electronics.md`). Fundusze obronne (NIF, Expeditions, Balnord) i EIC Fund są w 2026–2027 r. realniejszymi partnerami niż rynek publiczny (`strategikon/vc/vc.md` sekcje 5 i 7).

### 5.3 WB Electronics

| Lekcja z WB | Gdzie u nas | Stan | Co zrobić i kiedy |
|---|---|---|---|
| **Wzrost z zamówień, zaliczek i przepływów, nie z kapitału**; gwarancje wadialne i należytego wykonania jako codzienne narzędzie w zamówieniach publicznych | § 31 ust. 1 (katalog źródeł: zaliczki i przedpłaty od zamawiających, finansowanie eksportu, gwarancje), § 31 ust. 5 (Plan Finansowania z limitami gwarancji) | OK | Pierwszy Plan Finansowania po zawiązaniu: limity gwarancji bankowych i ubezpieczeniowych pod przetargi AU oraz linii faktoringowej pod należności od MON **[W]** |
| **Inwestor państwowy wchodzi przez nowe akcje jako mniejszość i zostaje na lata**; przy 26,44 % ma mniejszość blokującą | § 25 ust. 1 (75 % wszystkich głosów: każdy pakiet powyżej 25 % blokuje), § 32 ust. 2 (uchwała kierunkowa: maksymalna liczba akcji), § 25 ust. 1 lit. j (umorzenie zmienia proporcje) | CZ | W uchwale kierunkowej z § 32 ust. 2 ustalać maksymalny udział inwestora względem progu 25 %; w umowie akcjonariuszy zapisać, że umorzenie akcji odchodzącego Założyciela nie zmienia uzgodnionych progów albo uruchamia ich renegocjację **[W]** |
| **PFR inwestuje bezpośrednio w dojrzałe firmy** (WB: 20 lat, 300 mln zł przychodów); dla startupu droga do kapitału państwowego wiedzie przez fundusze PFR i wehikuły BGK (Vinci w ICEYE) | `regulations.md` sekcja 3 (PFR Deep Tech, Otwarte Innowacje); `psa_todo.md` sekcja 6; `strategikon/vc/vc.md` sekcja 2 | CZ | Do planu finansowania dopisać etapy: (1) granty i fundusze VC z udziałem PFR, (2) inwestor branżowy albo państwowy wehikuł przy pierwszym kontrakcie wolumenowym, (3) dług pod zamówienia. Fundusze kontrolowane przez Skarb Państwa spełniają Kryterium § 11 ust. 6 lit. b bez osobnej uchwały **[W]** |
| **Obligacje pod zastaw akcji spółki zależnej, z kowenantami dywidendowymi i dźwigni**; P.S.A. może emitować obligacje **[W]** | § 31 ust. 4 (zabezpieczenie na Kluczowej Własności Intelektualnej wymaga WZ; na innych aktywach do progu z § 25 ust. 1 lit. k nie), § 33 ust. 8 (zabezpieczenia za Przedsięwzięcie Produkcyjne), § 34 ust. 3 (dywidenda zgodna z umowami finansowania) | OK | W Planie Finansowania przewidzieć zastaw na udziałach Przedsięwzięć Produkcyjnych jako dopuszczalne zabezpieczenie długu; nie publikować prognoz jako warunków emisji bez marginesu (lekcja z celów 2018–2022) |
| **Publikowane cele finansowe stały się zobowiązaniem** (odwołane po roku) | § 32 ust. 4 lit. d (prawa informacyjne inwestora); umowa inwestycyjna | CZ | W umowie inwestycyjnej prognozy i budżety jako informacja, nie zapewnienie; brak kar za odchylenia od planu **[W]** |
| **Grupa zbudowana z przejęć aktywów państwowych i JV z partnerami spoza UE/NATO** (Hanwha 51/49: Korea nie jest w NATO ani UE; WB Ukraina) | § 33 ust. 1–2 (udział mniejszościowy dopuszczalny; uchwała Rady, a powyżej progów WZ), § 33 ust. 4 i § 25 ust. 1 lit. n (partner niespełniający Kryterium z dostępem do IP albo kontrolą: WZ 75 %), § 33 ust. 3 (licencja zwrotna, ulepszenia); `regulations.md` sekcja 3b | OK | We wzorze umowy JV (etap C pkt 25 w `plan_prac.md`) odwzorować model WB–Hanwha: partner większościowy w JV produkcyjnym, Basilisk zachowuje IP i licencjonuje; uchwała WZ 75 % planowana z góry, jeżeli partner jest spoza Kryterium |
| **Współpraca z PGZ jako droga do programów MON** (podwykonawcy z PGZ w Gladiusie, porozumienie 2025) | § 33 (konsorcjum), § 23 ust. 1 lit. h | OK | W mapie rundy i w planie sprzedaży uwzględnić PGZ jako partnera konsorcjum, nie tylko konkurenta; PGZ spełnia Kryterium (kontrola Skarbu Państwa) |
| **IPO spółki obronnej: tajemnice wojskowe kontra obowiązki informacyjne**; WB „miał wnioskować do MON" | § 27 (poufność, bezpieczeństwo informacji), `regulations.md` sekcja 4 (bramka G4: świadectwo bezpieczeństwa przemysłowego), art. 300³⁶ § 2 KSH (P.S.A. nie może być notowana) | BRAK | W ścieżce giełdowej z umowy akcjonariuszy (patrz sekcja 5.2 poniżej) dodać warunek: uzgodnienie z zamawiającym zakresu ujawnień w prospekcie i raportach oraz reżim informacji niejawnych **[W]** |
| **Kalendarz IPO zależny od kalendarza zamówień publicznych** (SAFE) | § 32 ust. 2 (uchwała kierunkowa), umowa akcjonariuszy (exit) | CZ | Klauzula exit w umowie akcjonariuszy z elastycznym oknem (12–18 miesięcy procesu), bez sztywnej daty; wyjście inwestora nie może wymuszać IPO w środku kontraktu |
| **Odejście trzeciego założyciela** i umorzenie jego akcji **[?]** | § 10 (zwrotne zbycie), § 19 (Wartość Godziwa), § 25 ust. 1 lit. j (nabycie akcji własnych i umorzenie) | OK | Umowa ma mechanizm; przy jego wykonaniu policzyć skutki dla progów 75 % i 25 % (wiersz 2) |
| **Ład rodzinny wystarcza spółce prywatnej, nie giełdowej** | § 21 (Rada 3–7 osób, dyrektorzy niewykonawczy), § 29 ust. 4–13 (Osoba Bliska, wyłączenie dyrektora), § 30 | OK | Bez zmian; przy planowaniu debiutu dopisać do regulaminu Rady (etap C pkt 22) wymóg niezależnych dyrektorów niewykonawczych **[W]** |
| **Skala i czas**: 20 lat do 300 mln zł przychodów, 4 lata do 3 mld zł; giełda po 29 latach nadal opcją | § 34 ust. 2 (reinwestycja zysku 36 miesięcy), `strategikon/vc/vc.md` sekcja 5 (fundusze obronne: horyzont 10–15 lat) | CZ | Nie obiecywać inwestorom wyjścia w 5–7 lat w modelu produkcyjnym; jeżeli Basilisk pozostanie softwarowy, horyzont może być krótszy (`strategikon/vc/case_studies/swarmer.md`), jeżeli produkcyjny, to horyzont WB i ICEYE |
| **Przejrzystość z Catalyst przed giełdą** | `psa_todo.md` sekcja 7 | DEC | Emisja obligacji notowanych to sposób na dług i na wiarygodność bez oddania akcji; sens dopiero przy przychodach z kontraktów; do decyzji na etapie długu **[W]** |

### 5.4 ICEYE

| Lekcja z ICEYE | Gdzie u nas | Stan | Co zrobić i kiedy |
|---|---|---|---|
| **Drabina finansowania**: granty na prototyp, VC na pierwsze wdrożenia, państwo i koncerny jako kapitał cierpliwy, kontrakty rządowe jako przegięcie, growth equity po rentowności | § 31 ust. 1 (katalog źródeł), § 32 (runda), § 33 (partnerzy); `regulations.md` sekcja 3; `psa_todo.md` sekcja 6 | CZ | Spisać plan finansowania w pięciu szczeblach z warunkami przejścia (TRL, pierwszy płatny pilot, pierwszy kontrakt wieloletni); EIC, Ścieżka SMART i DIANA to odpowiedniki Tekes i H2020 dla szczebla 1 |
| **Grant UE jako dźwignia do VC**: 2,4 mln EUR z H2020 „aby przyciągnąć prywatne inwestycje" | `psa_todo.md` sekcja 6 (EIC Accelerator: grant do 2,5 mln EUR i inwestycja do 30 mln EUR) | OK | Wniosek do EIC planować przed rundą A, nie po; grant zmniejsza rozwodnienie i podnosi wycenę |
| **Inwestorzy państwowi spełniają Kryterium**: Tesi, Solidium, Vinci/BGK to podmioty kontrolowane przez państwa UE | § 11 ust. 6 lit. b; `strategikon/vc/vc.md` sekcja 2 | OK | Uwzględnić PFR (przez fundusze), BGK (Vinci) i EIF jako inwestorów zgodnych z Kryterium bez uchwały WZ; sprawdzić wymogi ich programów (`regulations.md` sekcja 3) |
| **Inwestorzy strategiczni spoza UE/NATO na etapie growth** (Kajima, IHI: Japonia; QIA: Katar) | § 11 ust. 6 (zgoda WZ 75 %), ust. 14 (przekreślony wyjątek dla funduszy), § 12 ust. 2 lit. b; `regulations.md` sekcja 3 (art. 9 EDF: liczy się kontrola, nie udział) | KOL | Przewidzieć ścieżkę: mniejszościowy inwestor spoza Kryterium dopuszczony uchwałą 75 % z ograniczeniem dostępu do IP (§ 27 ust. 6) i bez praw kontrolnych; to zachowuje kwalifikowalność do EDF, bo art. 9 zakazuje kontroli, nie udziału **[W]** |
| **Koncern-klient jako akcjonariusz** (BAE, Kajima, Tokio Marine, Nokia) | § 29–30 (transakcje z Akcjonariuszami na warunkach rynkowych, ujawnienie konfliktu) | OK | Bez zmian; w umowie inwestycyjnej z koncernem dopisać brak wyłączności sprzedażowej i brak prawa pierwszeństwa do IP |
| **Mniejszość w JV z koncernem jako cena wejścia do zamówień** (Rheinmetall 60/40 jako strona kontraktu 1,7 mld EUR) | § 33 ust. 1–2 (udział mniejszościowy dopuszczalny), ust. 3 (IP zostaje w Spółce, licencja niewyłączna, ulepszenia dla Spółki), ust. 5 (prawa informacyjne, weto w sprawach IP i bezpieczeństwa przy braku kontroli) | OK | We wzorze umowy JV (etap C pkt 25 w `plan_prac.md`) użyć modelu ICEYE–Rheinmetall: JV jest stroną kontraktu, Basilisk dostawcą technologii; Rheinmetall (UE) spełnia Kryterium, Hanwha (Korea, zob. `wb_electronics.md`) nie |
| **Konsorcjum z polskim przemysłem państwowym** (ICEYE Polska + WZŁ-1 z PGZ w MikroSAR; porozumienie z PGZ) | § 33 (konsorcjum), § 23 ust. 1 lit. h | OK | Szablon dla programów MON: Basilisk liderem w warstwie autonomii, spółka PGZ w segmencie sprzętowym albo odwrotnie |
| **Państwo jako inwestor i klient jednocześnie** (Finlandia, Polska) | § 30 (transakcje z Akcjonariuszami), § 11 | OK | Jeżeli wehikuł Skarbu Państwa zostanie akcjonariuszem, kontrakty z MON podlegają § 30 (warunki rynkowe, ujawnienie); nie jest to przeszkoda, ale wymaga procedury |
| **Lokalizacja produkcji jako narzędzie sprzedaży**, IP w spółce-matce | § 33 ust. 3, § 26 (Kluczowa Własność Intelektualna), § 28 | OK | Przy pierwszym kontrakcie zagranicznym zakładać, że zamawiający zażąda montażu u siebie; § 33 to przewiduje |
| **Horyzont 10 lat do rentowności**; strata operacyjna w roku poprzedzającym przegięcie | § 34 ust. 2 (rekomendowana reinwestycja 36 miesięcy), `strategikon/vc/vc.md` sekcja 5 (fundusze obronne: 10–15 lat) | CZ | 36 miesięcy to horyzont softwarowy; przy modelu produkcyjnym zapisać w umowie akcjonariuszy politykę reinwestycji do pierwszego roku dodatnich przepływów |
| **Płynność przez odsprzedaż w rundach zamiast IPO** (ok. 600 mln EUR w 2025–2026 r.) | § 12 (zgoda Spółki na zbycie), § 14 (prawo pierwszeństwa), § 11 (Kryterium przy każdym nabyciu); sekcja 2 tego dokumentu (permitted transfers) | KOL | Odsprzedaż w rundzie musi mieć szybką ścieżkę: zgoda Spółki i wyłączenie prawa pierwszeństwa dla nabywców zweryfikowanych w rundzie, w jednej uchwale z emisją; dopisać do § 12 ust. 7 albo do umowy akcjonariuszy **[W]** |
| **Miejsce w radzie dla inwestora państwowego** (Solidium 2024) przy ośmiu rundach | § 21 ust. 1 (Rada 3–7 osób), § 32 ust. 4 lit. c (jeden dyrektor albo obserwator na rundę) | CZ | Po trzeciej rundzie liczba miejsc się kończy; w umowie akcjonariuszy ustalić, że lider każdej rundy wskazuje dyrektora, pozostali obserwatora, z rotacją |
| **Pierwszy klient wojskowy przez fundację charytatywną** (Prytuła, 16 mln USD dla Ukrainy) | `regulations.md` sekcja 2.2b (klient spoza NATO), § 23 ust. 1 lit. h, § 28 (użytkownik końcowy) | OK | Procedura z `regulations.md` obejmuje taki przypadek: nabywcą jest fundacja, użytkownikiem końcowym armia państwa spoza NATO; certyfikat użytkownika końcowego i zezwolenie MRiT przed dostawą **[W]** |
| **„Dlaczego Finlandia": grant uczelniany 50 tys. EUR, budżet projektu 0,5 mln EUR, wsparcie grantowe** | `psa_todo.md` sekcja 1 (pytanie o jurysdykcję) | DEC | Argument za pozostaniem w Polsce, o ile Basilisk realnie sięgnie po granty (EIC, SMART, DIANA); argument za Estonią albo Finlandią, jeżeli o decyzji ma przesądzać dostęp do wsparcia na wczesnym etapie. Rozstrzygnąć razem z pytaniem o strukturę holdingową |

### 5.5 Catalyst (obligacje)

| Pytanie | Odpowiedź | Gdzie w dokumentach | Wiar. |
|---|---|---|---|
| Czy P.S.A. może wyemitować obligacje? | Tak; ustawa o obligacjach nie ogranicza emitentów do S.A. Obligacje zamienne: tylko przez firmę inwestycyjną albo tylko dla akcjonariuszy; umowa spółki powinna wprost dopuszczać ich emisję | § 25 ust. 1 lit. b (emisja instrumentów zamiennych: 75 %), § 31 ust. 4 (instrument z prawem konwersji, warrantem, prawem nominacji dyrektora, wetem albo zabezpieczeniem na IP: Sprawa Zastrzeżona); do rozważenia zdanie w § 31, że Spółka może emitować obligacje, w tym zamienne i z prawem pierwszeństwa **[W]** | [W]/[Z] |
| Kiedy obligacje mają sens? | Gdy są przepływy z kontraktów i majątek do zabezpieczenia: WB po 17 latach, przy 300 mln zł przychodów. Dla Basiliska realny moment to pierwszy wieloletni kontrakt z zamawiającym publicznym, gdy potrzebny jest kapitał obrotowy na produkcję przed płatnościami | § 31 ust. 1 (finansowanie eksportu, zaliczki), § 31 ust. 5 (Plan Finansowania) | [?] |
| Co do tego czasu zamiast obligacji? | Granty i pożyczki publiczne (EIC, Ścieżka SMART, BGK, PARP), venture debt przy rundzie VC (zwykle z warrantami, czyli Sprawa Zastrzeżona z § 31 ust. 4), zaliczki zamawiającego, faktoring należności od MON | `psa_todo.md` sekcja 6; sekcja 2 tego dokumentu („Ograniczenia finansowania") | [W] |
| Jakie zgody w spółce? | Emisja w ramach budżetu i Planu Finansowania: Rada Dyrektorów (§ 23 ust. 1 lit. d); poza budżetem albo z zabezpieczeniem powyżej 500 tys. zł: WZ 75 % (§ 25 ust. 1 lit. k); zabezpieczenie na Kluczowej Własności Intelektualnej: zawsze WZ (§ 31 ust. 4); kowenanty dywidendowe wiążą przez § 34 ust. 3 | § 23, § 25, § 31, § 34 | [W] |
| Co z tajemnicą? | Obligacje notowane oznaczają raporty EBI/ESPI, sprawozdania roczne i półroczne oraz MAR; treść kontraktów wojskowych i klasyfikacja produktów nie muszą być ujawniane, ale wyniki, zadłużenie i zdarzenia istotne tak. To ten sam problem, który WB dostrzegło przy IPO („co z wojskowymi tajemnicami") | § 27 (poufność), `regulations.md` sekcja 4 (bramka G4) | [W] |
| Jaka cena? | Dla firmy z kontraktami MON i zabezpieczeniem: WIBOR plus 2–4 pp (WB, Kruk jako punkty odniesienia); dla małego emitenta bez historii: 4–6 pp albo brak popytu | sekcja 4.4 | [?] |
| Czy Catalyst zastępuje giełdę akcji? | Nie, ale ją poprzedza: WB zbudowało 9 lat historii raportowania przed rozmowami o IPO. Obligacje nie wymagają przekształcenia P.S.A. w S.A. (zakaz z art. 300³⁶ § 2 KSH dotyczy akcji, nie obligacji) **[W]**, więc to jedyna droga Basiliska na rynek publiczny bez zmiany formy prawnej | sekcja 5.2 poniżej, sekcja 5.3 poniżej | [W] |

Trzy zadania do `psa_todo.md` po decyzji Założycieli **[?]**: (1) zdanie w § 31 dopuszczające emisję obligacji, w tym zamiennych i z prawem pierwszeństwa, ze wskazaniem organu (uchwała WZ jako Sprawa Zastrzeżona); (2) w Planie Finansowania z § 31 ust. 5 kategoria „dług publiczny" z limitem i listą dopuszczalnych zabezpieczeń (udziały w Przedsięwzięciach Produkcyjnych, wierzytelności z kontraktów; nigdy Kluczowa Własność Intelektualna); (3) w umowie akcjonariuszy zgoda inwestorów na przyszłe kowenanty dywidendowe i informacyjne wynikające z obligacji.

### 5.6 Anduril

| Lekcja z Andurila | Gdzie u nas | Stan | Co zrobić i kiedy |
|---|---|---|---|
| **Sekwencja: szybki klient cywilny → OTA i prototypy → własny nośnik dla oprogramowania → produkcja lokalna u sojusznika** | `regulations.md` sekcja 4 (bramki G1–G6); `psa_todo.md` sekcja 6; `plan_prac.md` etap C | CZ | Odpowiedniki: klient cywilny (infrastruktura krytyczna, straż graniczna) przed MON; EDF, EDIP, DIANA i Brave1 jako „OTA"; integracja z platformą polskiego producenta przed przetargiem |
| **Czyste oprogramowanie nie dochodzi do budżetów programów of record bez platformy albo prima** (umowa Armii wiąże Lattice ze sprzętem) | § 33; sekcja 5.7 poniżej (A-GRA jako wyjątek) | DEC | Zdecydować: dron referencyjny (JV z producentem) albo firma integracja OEM; nie własna produkcja |
| **Nawet archetypowy disruptor wchodzi do Europy przez prime'a i hasło suwerenności** (Rheinmetall, czerwiec 2025 r.) | § 11; `kryteria.md` K1–K2; `jurisdictions/README.md` sekcja 1 | OK | Polska własność w 100 % to kwalifikowalność do EDF i SAFE, którą Anduril musi kupić partnerem; napisać to wprost w każdym wniosku konsorcjalnym |
| **Jeden sponsor przez dziewięć lat** (Founders Fund w 5 z 9 rund) | `strategikon/vc/vc.md` sekcje 2–3; § 32 (Kwalifikowana Runda) | CZ | Szukać inwestora z mandatem na kolejne rundy (NIF, PFR, EIF); w umowie inwestycyjnej pro-rata dla lead inwestora |
| **„Buduj przed kontraktem" w skali, którą można sfinansować samemu** | § 31 ust. 1; sekcja 5.10 poniżej | DEC | Zamiast fabryki: zintegrować autonomię z dwiema platformami przed pierwszym przetargiem MON |
| **Earn-out i spory z przejętymi założycielami** (Area-I) | § 25 ust. 1 lit. e (zbycie 75 %), sekcja 2 tego dokumentu wiersz „Exit" | BRAK | Przy exicie do nabywcy typu Anduril: earn-out z obiektywnymi kamieniami i arbitrażem; klauzula w umowie akcjonariuszy |
| **Płynność pracowników przez tender offers** (100 mln USD, 2025 r.) | § 27 (ESOP), § 12–14 | CZ | Zaplanować okna odsprzedaży w rundach od serii B (wzór ICEYE) |
| **Spalanie 800–900 mln USD finansowane rundami**: model nie do skopiowania | `plan_prac.md`; `strategikon/vc/vc.md` sekcja 7 | OK | Kopiować sekwencję, nie burn |

### 5.7 Shield AI

| Lekcja z Shield AI | Gdzie u nas | Stan | Co zrobić i kiedy |
|---|---|---|---|
| **Autonomia jako samodzielna pozycja w kontrakcie pod rządową architekturą referencyjną** (A-GRA, CCA, czerwiec 2026 r.) | `regulations.md` sekcja 4; § 33 ust. 3; `psa_todo.md` sekcja 6 | BRAK | Użyć precedensu w rozmowach z MON, PGZ, WB i w EDF: autonomia roju jako otwarta, konkurowana warstwa oprogramowania; projektować interfejsy pod architektury referencyjne (A-GRA, niemiecki CFSN, `strategikon/vc/case_studies/helsing.md`) |
| **Licencje dla suwerennych OEM (KAI, Northrop, Kratos, Airbus)** zamiast własnych płatowców | § 33 ust. 3 (licencja niewyłączna, ograniczona zakresem, wypowiadalna przy zmianie kontroli); sekcja 5.2 poniżej (B2B2G) | OK | Produkt typu „Enterprise/Forge" (runtime, API, wsparcie) w mapie produktu etapu C; wzór licencji „na platformę" z audytem wolumenów |
| **Kontrakt prototypowy (DIU 2016) przed serią A** | `regulations.md` sekcja 4 (G1–G3); `psa_todo.md` sekcja 6 (DIANA, EIC) | CZ | Pierwszy kontrakt albo grant przed Kwalifikowaną Rundą (§ 32); DIANA Fort Kraków i Brave1 jako polskie DIU |
| **Szybkość integracji jako mierzalne KPI** (3 lata → 180 dni → 3 miesiące) | `emisja/inwestor.md` (data room) | BRAK | Mierzyć i publikować czas integracji z każdą nową platformą |
| **Obecność w Ukrainie przed dużymi kontraktami** (Kijów, Brave1) | `jurisdictions/ukraina.md` sekcja 6; § 28 | DEC | Polska bliskość Ukrainy jest tańsza niż dla firmy z San Diego; ukraińska TOV albo estońska spółka kontraktowa po pierwszym grancie Brave1 |
| **Posiadanie sprzętu = odpowiedzialność za wypadki** (V-BAT) | `regulations.md` sekcja 2.2; § 33 | OK | Zostać przy oprogramowaniu; w umowach rozdzielać odpowiedzialność za autonomię od płatowca i wyrzutni |
| **Kapitał uprzywilejowany PE przed akcjami zwykłymi na późnym etapie** | § 31 ust. 4 (instrumenty: WZ 75 %); art. 300²⁶ KSH (uprzywilejowanie akcji P.S.A.) [W] | CZ | Umowa spółki musi dopuszczać akcje uprzywilejowane o stałej stopie i liquidation preference; sprawdzić § 6–8 pod kątem serii uprzywilejowanych |
| **Założyciele oddają fotel prezesa operatorowi** przy 5 mld USD | § 10 (vesting), § 21 (Rada), sekcja 3 tego dokumentu | DEC | Zdecydować z góry, kiedy Założyciele przechodzą na role strategiczne; zapisać w umowie akcjonariuszy |
| **Inwestorzy strategiczni z branży (L3Harris, Hanwha)** w rundzie | § 11 (NATO: USA, Korea spełniają), § 25 ust. 1 | OK | Dopuścić prima z UE/NATO w rundzie B z ograniczeniem informacji konkurencyjnych (§ 29–30) |

### 5.8 Helsing

| Lekcja z Helsinga | Gdzie u nas | Stan | Co zrobić i kiedy |
|---|---|---|---|
| **Kapitał kotwiczny zamiast drabiny SBIR/OTA**: 100 mln EUR przed kontraktem | `strategikon/vc/vc.md` sekcje 3 i 7; `psa_todo.md` sekcja 6; `jurisdictions/README.md` sekcja 3 | DEC | Bez Daniela Eka: EDF, EDIP, zamówienia MON z SAFE i współpraca z Ukrainą jako substytut cierpliwego kapitału; szukać inwestora kotwicznego z mandatem wielorundowym (NIF, Prima Materia-podobne family office z UE) |
| **Certyfikowana warstwa AI wewnątrz programu prima** (Cirra w Arexis, AI w Wingmanie) | § 33 ust. 3; sekcja 5.7 poniżej; `strategikon/vc/case_studies/iceye.md` (JV) | BRAK | Cel etapu C: umowa podwykonawcza z PGZ, WB albo Saabem, w której autonomia roju jest wyodrębnionym pakietem z własnym IP (§ 26) |
| **Rządowe architektury referencyjne** (CFSN „dla przyszłych dostawców", A-GRA) | `regulations.md` sekcja 4; `psa_todo.md` sekcja 6 | BRAK | Zgodność interfejsów z niemieckim CFSN i amerykańskim A-GRA jako wymaganie produktowe |
| **Ukraina jako poligon i baza dostawców** (HF-1 z Ukrainy) | `jurisdictions/ukraina.md` sekcja 6; § 28 | DEC | Polska bliskość i Brave1 są tańsze niż dla Monachium; TOV albo spółka estońska po pierwszym grancie |
| **Suwerenność jako cecha produktu**: 80 % europejskiej własności, Resilience Factories | § 11; `kryteria.md` K1–K2; `jurisdictions/README.md` sekcja 1 | OK | P.S.A. w 100 % polska jest kwalifikowalna do EDF z definicji; dokumentować łańcuch własności (§ 11 ust. 4) jako aktywo sprzedażowe w każdym wniosku |
| **Zwrot ku sprzętowi = odpowiedzialność za wyrzutnie i płatowce** (HX-2) | § 33; `regulations.md` sekcja 2.2 | OK | Zostać przy oprogramowaniu; w umowach rozdzielić metryki autonomii od metryk platformy i wyrzutni |
| **Luka: brak Helsinga w Polsce mimo 43,7 mld EUR SAFE** | `jurisdictions/polska.md` sekcja 6; sekcja 5.13 poniżej | DEC | Narracja „polskiego czempiona autonomii" jest wolna; MON i PGZ nie mają krajowego dostawcy warstwy AI roju |
| **Rada z byłym prezesem Airbusa i byłym szefem sztabu** | § 21 (Rada Dyrektorów), § 21 ust. 3 (Kryterium) | CZ | Dyrektor niewykonawczy z MON/NATO od etapu C (jak sekcja 5 poniżej (Destinus)) |
| **Krytyka cen i lobbingu przy zamówieniach z ograniczoną konkurencją** | § 29–30 (transakcje z podmiotami powiązanymi), § 23 ust. 2 (zgodność) | OK | Polityka antykorupcyjna i rejestr kontaktów z zamawiającym od pierwszej umowy z MON |

### 5.9 Destinus

| Lekcja z Destinusa | Gdzie u nas | Stan | Co zrobić i kiedy |
|---|---|---|---|
| **Siedziba holdingu idzie za prawem eksportowym i budżetami klientów** (Szwajcaria → Holandia) | `jurisdictions/README.md` sekcje 1 i 6; `jurisdictions/poza_kryterium.md` sekcja 2; `psa_todo.md` sekcja 1 | OK | Polska jest w UE/NATO i eksportuje do Ukrainy; zachować matkę w Polsce; nie rozważać Szwajcarii nawet jako miejsca B+R bez analizy KMG dla oprogramowania |
| **Eksport do Ukrainy wymaga licencji indywidualnej** (Szwajcaria: zakaz; Polska: brak zezwolenia generalnego na Ukrainę) | § 28; `regulations.md` sekcja 3; `jurisdictions/ukraina.md` sekcja 6 | BRAK | Wniosek o licencję indywidualną przed pierwszą dostawą; dostawy przez pakiety finansowane przez państwa NATO (Holandia płaci za Rutę) |
| **Instrumenty zamienne i pożyczki wspólników zamiast wycenionych rund** chronią większość założycieli | § 31 ust. 4 (instrument zamienny: WZ 75 %); `emisja/inwestor.md` sekcja 4; sekcja 5.2 poniżej (SAFE) | CZ | P.S.A. dopuszcza akcje za pracę i instrumenty zamienne; ustalić w umowie inwestycyjnej limit łącznej kwoty konwertowalnej i jednolity mechanizm konwersji; dług bankowy dopiero przy kontraktach (Commerzbank po ok. 350 mln EUR kapitału) |
| **JV 49/51 z koncernem** jako bilet do zamówień krajowych kosztem kontroli nad linią produktu | § 33 (spółki celowe, licencja niewyłączna, wypowiedzenie przy zmianie kontroli); `strategikon/vc/case_studies/iceye.md` (JV z Rheinmetallem) | OK | W JV oddawać produkt, nie platformę autonomii; licencja z § 33 ust. 3 ograniczona zakresem i wypowiadalna |
| **Rada z byłych ministrów i oficerów jako aktywo kapitałowe** | § 21 (Rada Dyrektorów; Kryterium wobec dyrektora), § 23 ust. 2 | CZ | Rozważyć dyrektora niewykonawczego z doświadczeniem w MON lub NATO od etapu C; Kryterium § 21 ust. 3 dopuszcza obywateli UE/EOG/NATO |
| **Autonomia AI jako aktywo przejmowane** (Daedalean 225 mln USD) | § 26 (IP w Spółce), § 25 ust. 1 lit. e (zbycie przedsiębiorstwa 75 %), `strategikon/vc/vc.md` sekcja 7 | OK | Utrzymać IP w P.S.A.; w umowie akcjonariuszy klauzula drag-along z progiem wyceny, by exit do grupy typu Destinus nie omijał Założycieli |
| **Pochodzenie założyciela jako ryzyko dla ŚBP i FDI** | `regulations.md` sekcja 3; ŚBP art. 64 (`jurisdictions/polska.md` sekcja 5) | OK | Basilisk: założyciele polscy; przy każdym inwestorze sprawdzać beneficjentów rzeczywistych (§ 11 ust. 4) |
| **Rosyjska lista celów po dostawach dla Ukrainy** | `regulations.md` sekcja 2.2 | BRAK | Budżet bezpieczeństwa i polityka informacyjna przed pierwszą dostawą (jak w sekcja 5 poniżej (Milrem)) |

### 5.10 Tekever

| Lekcja z Tekevera | Gdzie u nas | Stan | Co zrobić i kiedy |
|---|---|---|---|
| **Spółka zależna w kraju docelowego zamawiającego, założona wcześnie i obsadzona** (Tekever Ltd 2013 r.) zamiast przenoszenia matki | § 33 (spółki celowe); `jurisdictions/wielka_brytania.md` sekcja 6; `jurisdictions/README.md` sekcja 4.2 | CZ | Wpisać do planu etapu C (`plan_prac.md`) pierwszą spółkę zależną po pierwszym kontrakcie; UK wymaga brytyjskich dyrektorów do FSC i nie daje EMI spółce zależnej |
| **Fundusz suwerenny (NSSIF) i NIF jako inwestorzy uwiarygadniający** przed zamawiającym | `strategikon/vc/vc.md` sekcje 5 i 7; § 11 (NIF spełnia Kryterium) | OK | Polska jest LP NIF; celować w NIF jako inwestora rundy A obok PFR; NSSIF dostępny wyłącznie dla spółki brytyjskiej |
| **Matka w Portugalii, operacje w UK, restrukturyzacja przed rundą** (listopad 2023 r.) | `jurisdictions/przeniesienie_i_podatki.md` sekcja 4; `jurisdictions/portugalia.md` | DEC | Analogia: P.S.A. w Polsce jako matka, spółka zależna w UK/USA; jeśli inwestor wymaga spółki szczytowej w UE, zrobić to przed rundą, pierwszą wymianą udziałów (art. 24 ust. 8b pkt 3 PIT) |
| **Bootstrap przez usługi programistyczne przez dekadę** | § 31 ust. 1 (przychody z usług i zamówień jako finansowanie); `psa_todo.md` sekcja 6 | OK | Model dopuszczalny, ale sprzeczny z tempem rynku 2026 r.; w Polsce alternatywą jest pierwszy kontrakt MON albo DIANA |
| **Rynek macierzysty jako klient referencyjny, nie silnik wzrostu** | `jurisdictions/polska.md` sekcja 7; sekcja 5.3 poniżej | DEC | Polska ma 43,7 mld EUR SAFE, więc odwrotnie niż Portugalia: MON może być silnikiem; nie rezygnować z niego na rzecz eksportu |
| **Kontrola założyciela 25–50 % po 1,2 mld USD kapitału** | § 10 (vesting), § 25 ust. 1 (Sprawy Zastrzeżone), sekcja 3 tego dokumentu („czego nie oddawać") | OK | Utrzymać pakiet blokujący Założycieli przez rundy A–C; w umowie inwestycyjnej zapisać, że seria D nie pozbawia Założycieli praw z § 25 |
| **Wycena oderwana od przychodów jako ryzyko dla następnej rundy** | § 32 ust. 1 (progi Kwalifikowanej Rundy), D9 w `plan_prac.md` | CZ | Nie wpisywać do umowy progów wyceny z rynku 2026 r.; wyceny defence tech w 2026 r. to cykl hossy |
| **Brak długu mimo skali** | § 31 (dług: WZ 75 %) | OK | Dług bankowy po pierwszym programie of record, nie wcześniej |

### 5.11 Milrem Robotics

| Lekcja z Milrem | Gdzie u nas | Stan | Co zrobić i kiedy |
|---|---|---|---|
| **Inwestor spoza UE/EOG/NATO z pakietem kontrolnym uruchamia art. 9 EDF; ratunkiem są gwarancje państwa członkowskiego** (Estonia, lipiec 2023 r.) | § 11 (Kryterium UE/EOG/NATO, bez wyjątku funduszowego); `kryteria.md` sekcja 3; `jurisdictions/poza_kryterium.md` sekcja 5 | OK | zachować § 11; w umowie inwestycyjnej dopisać, że exit do nabywcy spoza Kryterium wymaga (a) uchwały 75 %, (b) wcześniejszej rozmowy z MON o gwarancjach z art. 9 ust. 4 EDF **[W]** |
| **Inwestor strategiczny na 24,9 % zamiast VC** (KMW 2021 r.): kapitał, kanał sprzedaży, centrum kompetencji, bez konsolidacji | § 25 ust. 1 (Sprawy Zastrzeżone 75 %), § 32 (Kwalifikowana Runda), `strategikon/vc/vc.md` sekcje 2–3 | CZ | Rozważyć koncern z UE/NATO (WB, PGZ, KNDS, Rheinmetall, Saab) jako inwestora rundy A obok funduszu; określić w umowie inwestycyjnej, że strategiczny inwestor nie dostaje wyłączności ani prawa pierwokupu technologii (§ 33 ust. 3 licencja niewyłączna) |
| **EDF i EDIDP jako główne źródło B+R platformy**; Milrem był liderem sprzętowym, a partnerzy dostarczali „funkcje inteligentne" | `psa_todo.md` sekcja 6; `regulations.md` sekcja 4 (bramka G4); `plan_prac.md` etap C | BRAK | Zgłosić się do konsorcjów EDF 2027 jako dostawca pakietu autonomii roju (odpowiednik „intelligent functions" w iMUGS2); wymaga podmiotu z UE bez kontroli z państwa trzeciego, czyli P.S.A. w Polsce (`jurisdictions/README.md` sekcja 6) |
| **Eksport finansowany przez darczyńcę** (Niemcy, Holandia płacą za Ukrainę) | § 28 (eksport), `regulations.md` sekcja 3, `jurisdictions/ukraina.md` sekcja 6 | CZ | Celować w pakiety pomocowe finansowane przez państwa NATO i SAFE, a nie w bezpośrednią sprzedaż Ukrainie; licencja eksportowa i tak jest potrzebna (ZG-PL-U-1 nie obejmuje Ukrainy) |
| **Produkcja u wykonawcy w kraju klienta** (VDL Born) zamiast własnej fabryki | § 33 (spółki celowe), `jurisdictions/README.md` sekcja 4.2 | OK | Dla oprogramowania odpowiednikiem jest integracja u producenta platformy w kraju klienta; wzór umowy licencyjnej „na platformę" (sekcja 5.2 poniżej) |
| **Ujemny kapitał własny finansowany pożyczkami wspólników** | § 31 (finansowanie dłużne i instrumenty zamienne: WZ 75 %) | OK | Pożyczki od akcjonariuszy dopuszczalne tylko uchwałą; w umowie inwestycyjnej limit zadłużenia wobec akcjonariuszy i zakaz zabezpieczeń na IP (§ 31 ust. 4) |
| **Zamknięcie transakcji przed wejściem w życie ustawy o kontroli inwestycji** | `jurisdictions/polska.md` sekcja 4 (polski screening stały od 24 lipca 2025 r., próg 20 %) | OK | W Polsce nie ma „okna": każde nabycie ≥20 % przez podmiot spoza UE/EOG/OECD przez inwestora w spółce obronnej podlega UOKiK **[W]**; wpisać do harmonogramu rund |
| **Bezpieczeństwo fizyczne i cybernetyczne jako koszt dostaw do Ukrainy** | `regulations.md` sekcja 2.2; ŚBP (`jurisdictions/polska.md` sekcja 5) | BRAK | Budżet ochrony w planie etapu C; polityka bezpieczeństwa przed pierwszą dostawą do Ukrainy |

### 5.12 Creotech

| Lekcja z Creotechu | Gdzie u nas | Stan | Co zrobić i kiedy |
|---|---|---|---|
| **NewConnect → GPW jako seria rund publicznych; wymaga S.A. od początku** (Creotech S.A. od 2012 r.) | § 25 ust. 1 lit. e (przekształcenie 75 %); art. 300³⁶ § 2 KSH; sekcja 5.2 poniżej | BRAK | Zapisać w umowie akcjonariuszy ścieżkę: P.S.A. do rundy A, przekształcenie w S.A. 12–18 miesięcy przed planowanym NewConnect; oferta do 2,5 mln EUR bez prospektu jako pierwszy krok **[W]** |
| **Państwo jako pierwszy inwestor** (ARP 17,1 %) zamiast VC, które odmawia deep techowi | `strategikon/vc/vc.md` sekcje 2 i 5; `jurisdictions/polska.md` sekcja 6 (PFR, Vinci, ARP) | CZ | Dopisać ARP i Vinci (BGK) do listy inwestorów rundy A obok PFR i NIF; wszyscy spełniają Kryterium § 11 |
| **Drabina grantów NCBR → ESA → SMART → MON** z emisją sparowaną z każdym kontraktem | `psa_todo.md` sekcja 6; `regulations.md` sekcja 4 (G4); `plan_prac.md` etap C | CZ | Harmonogram: SMART (nabór 29 października – 29 grudnia 2026 r.) → DIANA/EIC → pierwszy kontrakt MON; każdą Kwalifikowaną Rundę (§ 32) wiązać z konkretnym kontraktem |
| **MON jako punkt przegięcia**: jedno zamówienie z KPO/SAFE mnoży przychód 4×, ale kamienie milowe dyktują zmienność | `jurisdictions/polska.md` sekcja 7; sekcja 5.3 poniżej | DEC | Planować rozpoznawanie przychodów kamieniami; w data room pokazać koncentrację na jednym programie jako ryzyko zarządzane |
| **Kontrola polska przez OFE i TFI zamiast zagranicznego VC**; założyciele do 6–7 % każdy, ale zarząd zostaje | § 25 (Sprawy Zastrzeżone), § 10 (vesting), sekcja 3 tego dokumentu | DEC | Zdecydować, czy Założyciele akceptują rozwodnienie poniżej 25 % łącznie w zamian za giełdę; jeśli nie, droga WB/APS (dług i inwestor mniejszościowy) |
| **4–6 emisji w 5 lat i jedno rozwodnienie ok. 20 % pod skok strategiczny (100 mln EUR)** | § 25 ust. 2 (pozbawienie prawa poboru 4/5), § 32 | OK | Umowa przewiduje emisje z wyłączeniem prawa poboru; w umowie inwestycyjnej zabezpieczyć pre-emptive rights inwestorów z progiem, by ABB było możliwe |
| **Sprzedaż akcji przez prezesa pod lupą rynku** | § 13 (lock-up 12 miesięcy), sekcja 2 tego dokumentu wiersz „Lock-up" | CZ | Po debiucie polityka sprzedaży insiderów (okna, limity) w umowie akcjonariuszy |
| **Podział spółki jako wycena segmentu** (Quantum 350 mln zł) | § 25 ust. 1 lit. e (podział 75 %); § 33 | OK | Rozważyć wydzielenie segmentu cywilnego do odrębnej spółki przed ewentualnym exitem obronnym |

### 5.13 APS

| Lekcja z APS | Gdzie u nas | Stan | Co zrobić i kiedy |
|---|---|---|---|
| **Prospekt KNF nie jest szybką drogą** (2018 r.: zwrócony, bez debiutu); memorandum do 2,5 mln EUR jest szybkie, ale małe | § 25 ust. 1 lit. e (przekształcenie w S.A.: 75 %); art. 300³⁶ § 2 KSH; `catalyst.md` sekcja 5 | OK | Przekształcać P.S.A. w S.A. dopiero przy realnym oknie giełdowym; nie robić tego „na zapas" |
| **MON przychodzi po sojusznikach** (UK kupuje dla Ukrainy w 2022 r., SAN dopiero w 2026 r.) | `jurisdictions/polska.md` sekcja 7; `psa_todo.md` sekcja 6; `regulations.md` sekcja 4 (G5) | DEC | Plan przychodów etapu C z pierwszym klientem zagranicznym finansowanym przez darczyńcę; MON jako drugi klient |
| **Zamrożona specyfikacja w umowie z powolnym zamawiającym niszczy reputację** (SKYctrl 2022 r.) | § 33 ust. 3 (licencja), wzór umowy spółki celowej (etap C pkt 25 w `plan_prac.md`) | BRAK | W umowach z MON klauzula aktualizacji konfiguracji i oprogramowania (spiralna modernizacja) zamiast odbioru zamrożonej wersji **[W]** |
| **Gwarancje bankowe zamiast equity pod duży program** (450–600 mln zł) — dostępne dopiero przy umowie z primem | § 31 (dług: WZ 75 %), `catalyst.md` sekcja 5 | OK | Dług dopiero po pierwszej umowie z konsorcjum PGZ/Kongsberg/WB; do tego czasu granty i kapitał |
| **Jeden inwestor PE zamiast VC chroni kontrolę, ale uruchamia zegar wyjścia** (2023 → 2026) | § 25 (Sprawy Zastrzeżone), sekcja 2 tego dokumentu wiersz „Exit"; `emisja/inwestor.md` | CZ | W umowie inwestycyjnej zapisać horyzont wyjścia i mechanizm (IPO, sprzedaż, odkup) zgodny z planem Założycieli; unikać klauzul wymuszających sprzedaż w 3 lata |
| **Oprogramowanie jedzie na sprzęcie prima** (APS jako „najważniejsze komponenty" w SAN pod PGZ–Kongsberg) | § 33; `case_studies/README.md` sekcja 4 | OK | Basilisk jako warstwa autonomii u polskiego prima (WB, PGZ) — ten sam model |
| **Sprzeczne dane finansowe spółki prywatnej** | `emisja/inwestor.md` (data room) | OK | Od pierwszej rundy jedna, spójna seria KPI dla inwestorów |

### 5.14 Figure AI

| Lekcja z Figure AI | Gdzie u nas | Stan | Co zrobić i kiedy |
|---|---|---|---|
| **Pełny stos fizycznego AI kosztuje 1–2 mld USD przed przychodem** | `plan_prac.md` etap C; § 32; `strategikon/vc/vc.md` sekcja 7 | DEC | Basilisk jako warstwa autonomii na sprzęcie primów (jak APS na PGZ–Kongsberg, Nomagic na standardowych ramionach); nie budować własnych platform |
| **Własność modelu i danych z wdrożeń to aktywo, za które płacą inwestorzy** (Helix zamiast OpenAI) | § 26 (IP w Spółce), § 33 ust. 3 (licencja), wzór umowy pilota (etap C pkt 25) | BRAK | Prawa do danych treningowych i telemetrycznych w każdej umowie pilotażowej z MON i producentem; zakaz wyłączności modelu dla jednego klienta |
| **Jeden pilot flagowy niesie wycenę przez 18 miesięcy, ale jego koniec musi mieć następcę** | `psa_todo.md` sekcja 6; `regulations.md` sekcja 4 (G5) | DEC | Jedno widoczne ćwiczenie z Siłami Zbrojnymi RP jako odpowiednik BMW; równolegle drugi pilot u sojusznika |
| **Kontrola założyciela kupiona własnym kapitałem** jest niedostępna; polscy założyciele utrzymują kontrolę przez syndykaty instytucji (Creotech), PE mniejszość (APS) albo VC pod matką w USA (Nomagic) | § 10, § 25, sekcja 3 tego dokumentu | OK | Wybrać świadomie jedną z trzech dróg przed rundą A; umowa daje Założycielom Sprawy Zastrzeżone 75 % |
| **Dokumentacja bezpieczeństwa pokazana inwestorom musi przetrwać rundę** (pozew Gruendela) | § 23 ust. 2 (głos dyrektora ds. zgodności), § 29–30, `regulations.md` sekcja 2.2 | CZ | Polityka bezpieczeństwa systemów autonomicznych jako załącznik do data room i do umowy inwestycyjnej (oświadczenia i zapewnienia) **[W]** |
| **Blokowanie secondaries** chroni narrację, ale odbiera płynność pracownikom | § 12–14 (ograniczenia obrotu), § 27 (ESOP) | OK | Zaplanować okna odsprzedaży dla pracowników w rundach (wzór ICEYE), zamiast zakazu |
| **Brak zamówień rządowych w fizycznym AI USA**: finansowanie w 100 % prywatne | `jurisdictions/usa.md` sekcja 5 | OK | Dla Basiliska odwrotnie: klient rządowy jest źródłem przychodu i wiarygodności; nie kopiować modelu Figure |

### 5.15 Nomagic

| Lekcja z Nomagica | Gdzie u nas | Stan | Co zrobić i kiedy |
|---|---|---|---|
| **Amerykański lead w polskiej spółce prowadzi do flipu w ok. 20 miesięcy**; dla Basiliska flip do USA łamie Kryterium § 11 i EDF, a w Polsce jest opodatkowany 19 % | § 11; `jurisdictions/przeniesienie_i_podatki.md` sekcje 3.1 i 4; `jurisdictions/usa.md` sekcja 6 | OK | Przy amerykańskim inwestorze zapisać w umowie inwestycyjnej, że matka zostaje w UE/EOG; rozważyć holding holenderski zamiast Delaware, jeśli fundusz wymaga struktury poza Polską |
| **Substancja może zostać w Polsce pod zagraniczną matką** (zespół, B+R, EBI) | `jurisdictions/polska.md` sekcja 7 (SMART, koncesja wymagają polskiego podmiotu) | OK | Jeśli kiedykolwiek S2/S3 z `jurisdictions/README.md`, P.S.A. zostaje spółką operacyjną z IP |
| **Banki rozwoju (EBI venture debt, EBOR equity) jako pomost serii B**, gdy brakuje VC wzrostowego | § 31 (dług: WZ 75 %); `strategikon/vc/vc.md` sekcja 5; `psa_todo.md` sekcja 6 | BRAK | Dopisać EBI (InvestEU, venture debt), EBOR i EIF (Defence Equity Facility) do listy źródeł etapu C; wymagają siedziby w UE |
| **Klient jako inwestor mniejszościowy** (Zalando) buduje koło danych | § 11 (Kryterium: klient z UE spełnia), § 25 ust. 1, § 33 ust. 3 (licencja) | CZ | Dopuścić w umowie inwestycyjnej inwestora branżowego (producent platform, prime) z pakietem do 10 % bez praw blokujących; prawa do danych treningowych w każdym pilocie od pierwszego dnia |
| **Fizyczne AI jest wolne: 8 lat i ok. 85 mln USD do dwucyfrowej floty** | `plan_prac.md` etap C; § 32 (progi rund) | DEC | Basilisk jako warstwa oprogramowania na cudzym sprzęcie skraca ten cykl; nie planować własnej produkcji platform |
| **Brak polskiego pieniądza publicznego w historii Nomagica** to wybór, nie konieczność | `jurisdictions/polska.md` sekcja 6; sekcja 5.12 poniżej | OK | Basilisk powinien łączyć obie drogi: PFR/SMART/NCBR i zagraniczne VC spełniające Kryterium |
| **Polska spółka jako centrum kosztów: przychód KRS 5,3 mln zł** zniekształca obraz dla zamawiających i banków | `emisja/inwestor.md`; ŚBP (`jurisdictions/polska.md` sekcja 5) | CZ | Jeśli struktura holdingowa, kontrakty MON i koncesja muszą być w polskiej spółce z realnym przychodem |

---

## 6. Odpowiedzi na otwarte pytania z dokumentów Basiliska i decyzje przed rundą A

### 6.1 Odpowiedzi z case studies

| Pytanie | Odpowiedź z case studies | Wiar. |
|---|---|---|
| D1 (memorandum), `psa_todo.md` sekcja 1: gdzie siedziba? | P.S.A. w Polsce jako matka co najmniej do rundy A; spółki zależne według rynku po pierwszym kontrakcie (kolejność: Niemcy, Francja, Estonia, USA, UK, Finlandia, Litwa, Holandia, Ukraina, Portugalia w wariancie morskim); matka w UE/EOG tylko na żądanie inwestora wiodącego i pierwszą wymianą udziałów; Delaware nigdy przed rezygnacją z programów UE (`jurisdictions/README.md` sekcja 6) | [Z]/[?] |
| U.5 (`law_uzup.md`): koszty późniejszego przekształcenia | flip poza UE/EOG opodatkowany 19 %, exit tax przy przeprowadzce założycieli, utrata estońskiego CIT i „polskiego nexusa" PFR; Nomagic pokazuje, że substancja może zostać w Polsce, Swarmer, że programy UE się traci (`jurisdictions/przeniesienie_i_podatki.md`) | [Z] |
| `psa_todo.md` sekcja 6: plan finansowania | szczeble: (1) SMART, DIANA Fort Kraków, Brave1, EIC dual-use do 28 października 2026 r.; (2) pierwszy płatny pilot z producentem albo klientem sojuszniczym; (3) runda A z PFR, NIF, ARP lub Vinci i inwestorem kotwicznym z mandatem na B; (4) EBI venture debt i EBOR po przychodzie; (5) gwarancje BGK i banków pod umowę z primem; (6) przekształcenie w S.A. tylko przy oknie giełdowym | [?] |
| sekcja 2 tego dokumentu („Exit": BRAK) | trzy ścieżki do zapisania w umowie akcjonariuszy: giełda w Polsce po przekształceniu (Creotech), sprzedaż do prima z UE/NATO z earn-outem i arbitrażem (Anduril–Area-I jako ostrzeżenie), odsprzedaż w rundach (ICEYE); exit poza Kryterium tylko uchwałą 75 % i po rozmowie o gwarancjach (Milrem) | [?] |
| sekcja 3 tego dokumentu („czego nie oddawać") | § 25 ust. 1 lit. h (strategia), § 29–30 (podmioty powiązane), § 10 (vesting), § 26 (IP): potwierdzone przez Swarmera (przewodniczący z własną spółką), Figure (pozew o bezpieczeństwo), Shield AI (utrata fotela prezesa) | [M]/[?] |
| `regulations.md` sekcja 4 (bramki G1–G6) | G4 (pieniądze publiczne) potwierdzone jako warunek każdej skutecznej drogi; G5 (pierwszy kontrakt) jako punkt przegięcia; dodać bramkę „architektura referencyjna" (A-GRA, CFSN) przed G5 | [?] |

### 6.2 Przykłady, które uzasadniają odpowiedzi

| Pytanie | Przykład, który uzasadnia odpowiedź | Wiar. |
|---|---|---|
| D1 (memorandum), `psa_todo.md` sekcja 1: gdzie siedziba? | Destinus przeniósł holding do Holandii, żeby dostać holenderskie 400 mln USD i zamówienia NATO; Swarmer z Delaware jest poza EDF; Tekever zrestrukturyzował grupę (listopad 2023) przed pierwszą rundą, nie po | [Z]/[?] |
| U.5 (`law_uzup.md`): koszty późniejszego przekształcenia | Nomagic pokazuje, że substancja może zostać w Polsce (zespół, B+R, EBI), a Swarmer, że programy UE się traci; szczegóły w `jurisdictions/przeniesienie_i_podatki.md` | [Z] |
| `psa_todo.md` sekcja 6: plan finansowania | ICEYE: pięć szczebli z innym inwestorem na każdym; Creotech: NCBR → ESA → SMART → MON | [?] |
| sekcja 2 tego dokumentu, wiersz „Exit" (BRAK) | Creotech (NewConnect → GPW); Anduril–Area-I jako ostrzeżenie (pozew założyciela o ≥15 mln USD za zaniżony earn-out); ICEYE (ok. 600 mln EUR odsprzedaży w seriach E i F zamiast IPO); Milrem (gwarancje) | [?] |
| sekcja 3 tego dokumentu („czego nie oddawać") | Swarmer: przewodniczący z własną spółką Vectus (80 % Prince, 20 % emitent) i zmiana strategii cztery miesiące po IPO; Figure: pozew o „wypatroszoną" mapę bezpieczeństwa w miesiącu zamknięcia rundy; Shield AI: utrata fotela prezesa przy 5 mld USD | [M]/[?] |
| `regulations.md` sekcja 4 (bramki G1–G6) | Shield AI: A-GRA; Helsing: CFSN „dla przyszłych dostawców" | [?] |

### 6.3 Decyzje do podjęcia przed rundą A

1. **Wariant produktowy:** warstwa autonomii licencjonowana producentom i primom (Shield AI Enterprise) plus pakiet w konsorcjach EDF (Milrem „intelligent functions"); bez własnego nośnika. Konsekwencja: § 33 ust. 3 (licencja niewyłączna, ograniczona zakresem, wypowiadalna przy zmianie kontroli) i wzór umowy „na platformę" z audytem wolumenów (sekcja 5 poniżej (Swarmer)).
2. **Pierwszy klient:** cywilny (infrastruktura krytyczna, straż graniczna) albo sojuszniczy finansowany przez darczyńcę; MON jako drugi. Konsekwencja: plan przychodów etapu C i klauzula spiralnej aktualizacji w umowach z MON (sekcja 5 poniżej (Aps)).
3. **Struktura:** P.S.A. w Polsce z estońskim CIT do wejścia osoby prawnej; klauzula anty-flipowa i klauzula współdziałania przy wymianie udziałów do UE/EOG w umowie akcjonariuszy; ścieżka exitu poza Kryterium z gwarancjami państwa (`jurisdictions/przeniesienie_i_podatki.md` sekcja 4; sekcja 5 poniżej (Milrem)).
4. **Kapitał:** inwestor kotwiczny z mandatem wielorundowym (NIF, PFR, ARP, Vinci, EIF) i prime z UE/NATO jako inwestor mniejszościowy bez wyłączności technologii; EBI i EBOR w planie po przychodzie; kapitał uprzywilejowany dopuszczony w umowie na późny etap (sekcja 5 poniżej (Shield AI)).
5. **Kontrola:** Założyciele wybierają świadomie między drogą giełdową (rozwodnienie do 20–25 % łącznie, Creotech) a drogą kontroli (WB, APS: klient, dług, jeden inwestor mniejszościowy); od tego zależą progi § 32 i horyzont w umowie akcjonariuszy.
6. **Dane i bezpieczeństwo:** prawa do danych treningowych i telemetrycznych w każdym pilocie; polityka bezpieczeństwa systemów autonomicznych jako załącznik do data room i do oświadczeń w umowie inwestycyjnej (sekcja 5 poniżej (Figure AI); sekcja 5 poniżej (Nomagic)).
7. **Ukraina i bezpieczeństwo fizyczne:** obecność (biuro, Brave1) przed dużymi kontraktami, przez pakiety darczyńców; licencja eksportowa indywidualna; budżet ochrony po sabotażu u Milrem i liście celów Destinusa (`ukraina.md` sekcja 6).
8. **Rada:** dyrektor niewykonawczy z MON lub NATO od etapu C, zgodny z § 21 ust. 3 (`destinus.md`, sekcja 5 poniżej (Helsing)).

---

## 7. Wnioski dla umowy z analiz typów inwestorów, inwestorów polskich i sektorowych oraz grantów

Analizy `strategikon/vc/vc_types.md` (typy inwestorów), `strategikon/vc/polish_vc.md` (inwestorzy w Polsce), `strategikon/vc/investors.md` (inwestorzy sektora physical AI), `strategikon/vc/grant.md` (programy grantowe) i `strategikon/strategy/biz/phys_ai_startups.md` (startupy physical AI) opisują rynek bez odesłań do umowy. Poniżej zebrano, co z każdej z nich wynika dla konkretnych paragrafów projektu. Oznaczenia stanu jak w sekcji 2.

### 7.1 Kryterium Bezpieczeństwa (§ 11) wobec różnych typów inwestorów

| Typ inwestora (źródło) | Co wynika z analizy | Gdzie u nas | Stan | Co zrobić |
|---|---|---|---|---|
| Fundusz VC z LP spoza UE/EOG/NATO (vc_types 2.1, investors sekcje 2–4) | fundusze z USA, Izraela, Szwajcarii, Singapuru, Japonii i Zatoki nie ujawnią pełnej listy LP i nie zgodzą się na ich indywidualną weryfikację **[W]**; bez wyjątku funduszowego każdy taki fundusz wymaga uchwały WZ 75 % | § 11 ust. 4 (beneficjenci rzeczywiści), § 11 ust. 6 lit. b, skreślony § 11 ust. 14 | KOL | przywrócić § 11 ust. 14 w wersji uszczelnionej: test na poziomie zarządzającego (GP) z siedzibą i kontrolą w UE/EOG/NATO, look-through do LP tylko powyżej 25 % funduszu; to pierwsza z dwóch zmian, które odblokowują rozmowę z każdym typem inwestora |
| Syndykat aniołów, SPV jednego inwestora (vc_types 1.3) | wehikuł z wieloma uczestnikami jest problemem dla testu beneficjentów: każdy uczestnik powyżej 25 % wehikułu musi być ustalony **[Z]** (próg z ustawy AML) | § 11 ust. 4 | CZ | w umowie inwestycyjnej z syndykatem: oświadczenie o uczestnikach powyżej 25 % i obowiązek aktualizacji; w § 11 ust. 4 wprost odesłać do progu 25 % |
| Family office z Zatoki, Szwajcarii, Izraela (vc_types 5.1, investors sekcja 6) | nie spełni Kryterium; jako mniejszość bez praw kontrolnych i bez dostępu do Kluczowej IP zachowuje kwalifikowalność do EDF, bo art. 9 zakazuje kontroli, nie udziału | § 11 ust. 6, § 25 ust. 1 lit. n, § 27 ust. 6 | DEC | ścieżka wyjątku uchwałą 75 % dla mniejszościowego inwestora spoza Kryterium, z ograniczeniem dostępu do IP według § 27 ust. 6 (wzór ICEYE: Kajima, IHI, QIA) |
| Fundusze suwerenne spoza sojuszu, kapitał koreański, japoński, chiński (investors sekcje 3 i 7) | SoftBank, Samsung, LG, Hanwha, Temasek, QIA, Tether, fundusze chińskie: poza Kryterium; jako kontrolujący kolidują z art. 9 EDF (decyzja D6) | § 11 ust. 6, § 27 ust. 6; D6 | OK | utrzymać; nigdy jako inwestor kontrolujący przy ścieżce EDF; Korea przy każdym nabyciu wymaga uchwały WZ |
| Wehikuły państwowe i wielostronne UE: PFR, NIF, ARP, EIF, EBI, EBOR, Vinci, BGK (vc_types 4.3, polish_vc sekcja 3) | wszystkie spełniają Kryterium bez uchwały (kontrola państwa UE/NATO) **[W]** i art. 9 EDF; NIF wymaga tylko siedziby w państwie-LP; Kryterium § 11 jest gotową odpowiedzią na wymogi PFR Deep Tech i FTP | § 11 ust. 6 lit. b | OK | pokazać Kryterium jako aktywo w rozmowie z PFR, NIF i EIF; jeżeli wehikuł Skarbu Państwa zostanie akcjonariuszem, kontrakty z MON podlegają § 30 (warunki rynkowe, ujawnienie) jako procedura, nie przeszkoda |
| Branżowe VC z USA i Kanady (investors sekcja 2) | spełniają Kryterium (NATO), ale jako lead w polskiej spółce każdy zapyta o matkę w Delaware (decyzja D1) i o miejsce w radzie | § 11 ust. 14, § 21 ust. 3 (kryterium dla dyrektorów); D1 | DEC | holding tylko w UE/EOG (D1 potwierdzona przez case studies); obserwator zamiast dyrektora, jeśli § 21 ust. 3 wyklucza nominata |
| Nieprzejrzysty wehikuł bez ujawnienia beneficjentów (vc_types sekcja 7, wzór Theseus 22 % w Swarmerze) | ryzyko sankcyjne i reputacyjne; test beneficjentów jest jedyną obroną | § 11 ust. 4 | OK | nie rozluźniać § 11 ust. 4; dołączyć do data room procedurę KYC akcjonariusza |

### 7.2 Obrót akcjami, podmioty powiązane i koncerny

| Temat (źródło) | Co wynika z analizy | Gdzie u nas | Stan | Co zrobić |
|---|---|---|---|---|
| Przeniesienia dozwolone (vc_types sekcja 9, polish_vc sekcja 5) | fundusz musi móc przenieść akcje do funduszu następcy, spółki celowej albo do LP przy likwidacji; zgoda Spółki i prawo pierwszeństwa przy każdym nabyciu blokują też odsprzedaż w rundzie | § 12 ust. 7, § 14 | BRAK | rozszerzyć katalog przeniesień dozwolonych w § 12 ust. 7 o podmioty powiązane funduszu spełniające Kryterium; to druga z dwóch zmian odblokowujących rozmowę z każdym typem inwestora; szybka ścieżka zgody dla nabywców zweryfikowanych pod § 11 |
| CVC i prime jako inwestor mniejszościowy (vc_types 4.2, investors sekcja 5, phys_ai_startups sekcja 10 pkt 6) | koncern z UE/NATO na 10–24,9 % bez wyłączności i bez prawa pierwszeństwa do IP; licencja niewyłączna, ograniczona zakresem, wypowiadalna przy zmianie kontroli; Hanwha (WB JV 51/49) jako partner spoza Kryterium z dostępem do IP wymaga WZ 75 % | § 29–30 (transakcje z podmiotami powiązanymi), § 33 ust. 3 (licencja niewyłączna), § 33 ust. 4, § 25 ust. 1 lit. n | OK | nie oddawać § 29–30; wyłączność technologii dla CVC albo prime'a (§ 33 ust. 3) jest na liście „czego nie oddawać" w `polish_vc.md`; JV z koncernem według modelu ICEYE–Rheinmetall (JV stroną kontraktu, Basilisk dostawcą technologii, IP w Spółce) jako wzór dla § 33 |
| Wehikuł członka rady jako kontrahent (vc_types sekcja 7; Vectus: Prince 80 %, Swarmer 20 %) | precedens, którego umowa ma nie dopuścić | § 29–30 | OK | utrzymać; w umowie inwestycyjnej obowiązek ujawnienia spółek osobistych członków rady |
| Fundusze z wykluczeniem broni (vc_types 2.4, polish_vc sekcja 5) | mogą wejść tylko wtedy, gdy wariant obronny jest w osobnej spółce celowej, w której nie mają udziału; zwykle szkoda na nich czasu | § 33 | DEC | nie prowadzić rozmów z funduszami z wykluczeniem broni bez spółki celowej z § 33 |
| Ścieżka wyjścia do PGZ (polish_vc sekcja 4) | PGZ i wehikuły MON jako inwestor rundy B lub nabywca; Założyciele muszą rozstrzygnąć, czy exit do PGZ jest dla nich akceptowalny | § 25, decyzja 5 z `strategikon/strategy/biz/conclusions.md` | DEC | zapisać w umowie akcjonariuszy jako jedną z trzech ścieżek exitu albo ją wykluczyć |

### 7.3 Kapitał, instrumenty i dług

| Temat (źródło) | Co wynika z analizy | Gdzie u nas | Stan | Co zrobić |
|---|---|---|---|---|
| Wkłady i vesting Założycieli (vc_types 1.1) | fundusz w rundzie A pyta najpierw o wkłady Założycieli i o to, czy vesting obejmuje także akcje za wkład pieniężny | § 5–7 i Załącznik nr 1, § 10 | OK | utrzymać; w data room pokazać ewidencję wkładów według Załącznika nr 1 |
| SAFE i instrumenty zamienne (vc_types 1.4) | SAFE wymaga uchwały 75 %; kilka SAFE z różnymi capami daje przy konwersji kilka podserii po różnych cenach (wzór Swarmera) | § 31 ust. 4 | CZ | jeden wzór SAFE z jednym capem na rundę pre-seed; uchwała ramowa 75 % na limit kwotowy zamiast uchwały na każdy instrument |
| Venture debt, banki rozwoju, dług spoza UE/NATO (vc_types sekcja 6, investors sekcja 6) | § 31 ust. 3 odsyła do testu sankcyjnego, nie do Kryterium, więc dług spoza UE/NATO nie jest zakazany; zabezpieczenie na Kluczowej IP i warranty wymagają uchwały 75 % | § 31 ust. 3–4 | CZ | w umowie akcjonariuszy z góry ustalić dopuszczalny zakres zabezpieczeń dla venture debt (zastaw na należnościach i sprzęcie, nigdy na Kluczowej IP) i limit warrantów; EBI, EBOR i gwarancje BGK w planie etapu C |
| Serie uprzywilejowane PE i banków (investors sekcja 6, phys_ai_startups sekcja 10) | kapitał uprzywilejowany o stałej stopie i liquidation preference pojawia się przy 5–13 mld USD (Blackstone w Shield AI); umowa musi go dopuszczać dopiero na etapie C i później | § 6–8, § 31 ust. 4; art. 300²⁵ KSH | CZ | sprawdzić, czy § 6–8 dopuszczają serie uprzywilejowane o stałej stopie; horyzont zapisać w umowie akcjonariuszy, nie w umowie spółki |
| Progi Kwalifikowanej Rundy (phys_ai_startups sekcja 10 pkt 7, decyzja D9) | mnożniki ×15 w 19 miesięcy (Figure) i ×15 w 6 miesięcy (Tomorrow Robotics) to cykl hossy; progów z § 32 nie kalibrować do tych liczb | § 32 ust. 1; D9 | DEC | punktem odniesienia dla progów są rundy A europejskich firm obronnych (Helsing, Milrem, Tekever), nie humanoidy z USA i Chin |
| Prawa do danych z pilotów (investors sekcja 8, phys_ai_startups sekcja 10 pkt 4) | fundusze sektorowe i chmurowe płacą za własność modelu i danych z wdrożeń; dostawca chmury jako inwestor wymaga udokumentowanej wymienności dostawcy (dwa modele bazowe, tryb bez chmury) | § 26 (IP w Spółce), § 27 ust. 6 | CZ | prawa do danych treningowych i telemetrycznych w każdej umowie pilotażowej jako warunek z § 26; dostęp dostawcy chmury do danych spoza UE/NATO tylko za zgodą według § 27 ust. 6 |

### 7.4 Granty i programy publiczne

| Temat (źródło) | Co wynika z analizy | Gdzie u nas | Stan | Co zrobić |
|---|---|---|---|---|
| EDF, EDIP, STEP Obronność: kontrola spoza UE (grant sekcja 7 pkt 2) | „kontrola spoza UE" wyklucza z EDF; fundusz z USA jako inwestor kontrolujący zamyka EDF; precedens Milrem–EDGE kosztował pół roku gwarancji państwa | § 11, D1, D6 | OK | utrzymać § 11 wobec inwestora kontrolującego; przed każdym exitem poza Kryterium rozmowa z MON o gwarancjach z art. 9 ust. 4 EDF |
| SMART i „wyłącznie militarne" (grant sekcja 7 pkt 2) | SMART wyklucza projekty wyłącznie militarne; wariant cywilny musi być prawdziwym produktem | § 33 (spółka celowa) | DEC | rozstrzygnąć, czy wariant cywilny jest w Spółce, czy w spółce celowej z § 33, zanim złoży się wniosek |
| IP w konsorcjum (grant sekcja 7 pkt 8) | w EDF prawa do wyników należą do beneficjentów z ograniczeniami wobec państw trzecich; w SMART wdrożenie musi nastąpić w Polsce; partner-prime będzie chciał prawa pierwszeństwa do technologii | § 26 (IP w Spółce), § 33 ust. 3 (licencja niewyłączna); `plan_prac.md` etap C | OK | § 26 i § 33 ust. 3 są z tym zgodne; umowa konsorcjum według wzoru z `plan_prac.md` etap C, bez wyłączności (model ICEYE–Rheinmetall); nie oddawać IP partnerowi konsorcjum |
| Terminy naborów (grant sekcja 6) | EIC dual-use do 28 października 2026 r., nabór SMART 29 października – 29 grudnia 2026 r. **[M]** | `psa_todo.md` sekcja 6 | BRAK | przenieść terminy do `psa_todo.md` sekcja 6 i do planu finansowania w szczeblach (sekcja 6.1 powyżej) |

### 7.5 Dwie zmiany, które odblokowują wszystko

Zasada nadrzędna, powtarzająca się w każdej z pięciu analiz: dwie zmiany w umowie spółki — uszczelniony wyjątek funduszowy w § 11 ust. 14 i rozszerzony katalog przeniesień dozwolonych w § 12 ust. 7 — odblokowują rozmowę z każdym typem inwestora z `strategikon/vc/vc_types.md`, a decyzje D1 (holding w UE/EOG) i D6 (kontrola w UE pod art. 9 EDF) rozstrzygają, z którymi warto ją prowadzić. Reszta (progi § 32, serie uprzywilejowane w § 6–8, zakres zabezpieczeń dla długu w § 31 ust. 4) to parametry do ustalenia w umowie akcjonariuszy, nie konstrukcja umowy spółki.

---

## 8. Źródła
- Analizy, z których pochodzą sekcje 5–7 (repozytorium strategikon, gałąź `vc_case_studies`): `vc/case_studies/*.md` (źródła pierwotne w ostatniej sekcji każdego pliku), `vc/vc_types.md`, `vc/polish_vc.md`, `vc/investors.md`, `vc/grant.md`, `strategikon/strategy/biz/conclusions.md`, `strategy/biz/phys_ai_startups.md`.
