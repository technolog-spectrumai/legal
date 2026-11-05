# Audyt prawny (stan końcowy po trzech rundach): Basilisk Systems P.S.A. 2.3-S i Appolonia P.S.A. 1.3-S

| | |
|----|----------------|
| **Przedmiot** | 1. Umowa Basilisk Systems P.S.A. — `psa.tex`, wersja 2.3-S. 2. Umowa Appolonia P.S.A. — `appolonia.tex`, wersja 1.3-S. Obie na gałęzi `psa_simple2`, po 18 §, z Załącznikiem nr 1, lustrzane poza firmą, siedzibą, przedmiotem działalności i wariantem cywilnym Appolonii. 3. Konstrukcja spółek siostrzanych (§ 15), konsorcjum, przenoszenie IP. |
| **Przebieg** | Audyt v0 (commit `99b14ac`) → trzy rundy „poprawka → audyt” (U1/A1, U2/A2, U3/A3). Szczegóły każdej rundy: `audyt_rundy.md`. |
| **Data** | listopad 2026 r. |
| **Stan prawny** | Według `memorandum.md` (KSH t.j. Dz.U. 2024 poz. 18 z późn. zm., w tym zmiany od 18.02.2027 r. z Dz.U. 2026 poz. 176) oraz źródeł wskazanych w raporcie. |
| **Ocena końcowa** | **W treści obu umów nie zostało ryzyko krytyczne ani wysokie.** Wszystkie 8 ryzyk K i W z audytu v0 oraz 3 ryzyka W wykryte w rundach usunięto w tekście. Zostają ryzyka rezydualne: czynności i dokumenty przy akcie (najważniejsze — uchwała o pełnomocniku i umowy przenoszące IP), podatki, decyzje biznesowe i tezy do potwierdzenia przez prawnika (punkt 1.3). |

**Weryfikacja źródeł.** W tym środowisku nie było dostępu do ISAP, portalu orzeczeń SN, SAOS, CBOSA ani systemów Legalis/LEX.

| Znak | Znaczenie |
|--|------------------|
| **[Z]** | Zweryfikowane na tekście przepisu albo orzeczenia — w `memorandum.md` lub `psa_feedback.tex` (z linkami do sn.pl i eli.gov.pl) |
| **[S]** | Potwierdzone wyszukiwaniem w toku audytu: istnienie, sygnatura, data i teza według baz orzeczeń lub komentarzy. Pełnego tekstu uzasadnienia nie czytano. |
| **[W]** | Wiedza ogólna albo wniosek audytora — do potwierdzenia przez prawnika |

Raport nie zastępuje opinii adwokata, radcy prawnego ani doradcy podatkowego.

---

## 1. Wnioski

### 1.1. Bilans rund

| Runda | Wersje | Co załatwiła | Co wykrył audyt po niej |
|---|---|---------|----------|
| v0 | 2.0-S / 1.0-S | — | 3 ryzyka K, 5 W, 11 Ś, 7 N |
| **U1 → A1** | 2.1-S / 1.1-S | Wszystkie K i W z v0 w treści umów; Ś1–Ś6, Ś11; N1–N6; Appolonia dostała poprawki IP | 2 W: brak terminu w vestingu, wąska definicja spółki siostrzanej; 4 Ś: licencja 5-letnia, lista umów pełnomocnika, adres doręczenia, błędne odesłania w dokumentacji |
| **U2 → A2** | 2.2-S / 1.2-S | Wszystkie ustalenia A1 | 1 W: pętla w vestingu po zbyciu w wykonaniu obowiązku; 1 Ś: podatek przy cenie emisyjnej; 1 N: sztywny zakaz głosu zastawnika |
| **U3 → A3** | 2.3-S / 1.3-S | Wszystkie ustalenia A2 | Brak nowych ryzyk K i W w treści; ryzyka rezydualne (punkt 1.3) |

### 1.2. Co jest dobrze

- **Ustrój i forma.** Rada Dyrektorów, reprezentacja łączna, uchwały poza WZ i udział zdalny są zgodne z KSH (art. 300⁷³–300⁷⁹, 300⁸⁰, 300⁹² **[Z]**). Forma aktu notarialnego jest konieczna, bo aport niepieniężny wyklucza S24 (art. 300⁶ § 1 **[Z]**).
- **Reprezentacja w umowach z dyrektorami.** Umowy założycieli-dyrektorów ze Spółką podpisuje pełnomocnik z uchwały akcjonariuszy (art. 300⁷⁹ § 1 **[Z]**): aport IP, umowy IP, kwartalne potwierdzenia, umowy wykonawcze vestingu, wykup akcji od dyrektora (§ 11 ust. 3, § 14 ust. 1, § 18 ust. 6, Załącznik nr 1).
- **Tytuł do IP.** Aport IP przenoszony w dniu aktu, z licencją tymczasową i egzekucją w naturze (art. 64 KC; SN II CSKP 593/22 **[Z]**). Ustawowe elementy umowy przeniesienia (art. 41, 46, 50, 53, 74 pr. aut. **[Z]**) są wpisane wprost. Kwartalne potwierdzenia dotyczą utworów już istniejących, co omija art. 41 ust. 3.
- **Vesting** bez udziału Spółki jako nabywcy, więc bez ryzyka obejścia art. 300⁴⁵ § 2 KSH (memorandum 1.5.2 **[Z]**):
  - terminy: 3 miesiące, potem 30 dni dla pozostałych założycieli, łącznie najwyżej 6 miesięcy;
  - jasny koniec obowiązku i wykreślenie wzmianki z rejestru;
  - skuteczność wobec nabywców wtórnych (memorandum 1.5.1 **[Z]**).
- **Ograniczenia zbywania:**
  - zamknięty katalog przyczyn odmowy;
  - wyłączenie art. 300³⁹ § 3–5 (memorandum 1.2.1: „zgodne warunkowo” **[Z]**);
  - lock-up 12 miesięcy;
  - fikcja zgody z mechanizmem dla podmiotu prowadzącego rejestr.
- **Spółki siostrzane.** § 15 wyłącza zakaz konkurencji, poufność i konflikt interesów w granicach prawa. Wymaga Umowy o Współpracy zatwierdzonej przez WZ, cen rynkowych z niezależnym biegłym, zgody WZ na udziały w siostrze (dominacja, art. 6 KSH). Działa także przy częściowo różnym składzie założycieli.
- **Parytet z S24:** rok obrotowy, zaliczki, głos zastawnika są uregulowane.

### 1.3. Rejestr ryzyk — stan końcowy

| ID | Ryzyko | Status | Ryzyko rezydualne |
|--|---------|---------|--------|
| **K1** | Umowy z założycielami-dyrektorami bez pełnomocnika — nieważność | Usunięte w treści (U1, U2). **Do wykonania:** uchwała o pełnomocniku w akcie i podpisy pełnomocnika. | **Ś** — dopuszczalność pełnomocnika „rodzajowego” (doktryna); przy wątpliwości wskazywać konkretne umowy |
| **K2** | Aport IP niewniesiony | Usunięte w treści (U1). **Do wykonania:** komplet umów przeniesienia z wykazami w dniu aktu. | **Ś** — zależy od wykonania (punkt 5) |
| **K3** | Wycena wkładów | Poza treścią — Załącznik nr 1 do wypełnienia | **Ś** — art. 300¹⁰ KSH, spójność z PIT |
| W1 | Odkup przez Spółkę po cenie emisyjnej | Usunięte (U1) | N |
| W2 | Nabywca wtórny w vestingu | Usunięte (U1, U3) | N |
| W3 | Wczesne zamykanie uchwał obiegowych | Usunięte (U1) | N |
| W4 | Konflikt interesów z Appolonią | Ograniczone (U1): WZ, formuły, biegły | **Ś** — ustawowy obowiązek wstrzymania się (art. 300⁵⁵ § 1) zostaje; realny po rozejściu się akcjonariatu |
| W5 | Dominacja przez unię personalną | Ograniczone (U1): akcje siostry tylko za zgodą WZ, zawiadomienie z art. 6 | N — dopóki nie ma wzajemnych udziałów |
| A1-1 | Vesting bez terminu | Usunięte (U2) | N |
| A1-2 | Definicja spółki siostrzanej | Usunięte (U2) | N |
| A2-1 | Pętla w vestingu | Usunięte (U3) | N |
| Ś1 | Fikcja zgody a rejestr | Ograniczone (U1, U2): obowiązek w umowie z podmiotem prowadzącym rejestr | N — do uzgodnienia z podmiotem przed aktem |
| Ś6 | Art. 41 ust. 3 pr. aut. | Ograniczone (U1): utwory „w ramach zadań”, kwartalne potwierdzenia | N |
| Ś7–Ś9, A2-2 | Podatki: aport IP, licencje nieodpłatne, cena emisyjna w vestingu, seria F za pracę, ceny transferowe | Ograniczone (U1, U3: dokumentacja ceny) | **Ś** — interpretacje indywidualne |
| Ś10 | Umowa o Współpracy nie istnieje | Poza treścią | **Ś** — bez niej § 15 nie daje licencji ani rozliczeń |
| Ś11 | Appolonia | Poprawki przeniesione (U1–U3) | **Ś** — firma („Appolonia”/„Apollonia”), siedziba, skład założycieli, PKD |
| N7 | Kody PKD 2025 | Poza treścią | N — sprawdzić przed wnioskiem do KRS |
| — | Decyzje Założycieli: próg odwołania dyrektora (§ 10 ust. 2), czas poufności (§ 14 ust. 3), vesting dla akcji nabytych od odchodzącego (A2-4) | Do decyzji | — |
| — | Dokumenty zależne `extra.tex`, `psa_feedback.tex`, `shareholder_agreement.tex`, `uchwaly.tex` z odwołaniami „??” | Poza zakresem (zgodnie z poleceniem, dokumentacji nie zmieniano) | — |

---

## 2. Umowy — analiza postanowień (stan 2.3-S / 1.3-S)

Poniżej tylko to, co istotne dla oceny prawnej. Numeracja jest taka sama w obu umowach.

### § 1–2. Firma, siedziba, przedmiot działalności

- **Ocena:** zgodne.
- **Podstawa:** art. 300⁵ § 1 KSH **[Z]**.
- **Uwagi:**
  - zakres Basilisk („na lądzie i w powietrzu”) i Appolonii („morze i wody śródlądowe”) się nie pokrywa, co jest podstawą § 15 i zakazu konkurencji;
  - kody PKD 2025 do weryfikacji (N7);
  - firma i siedziba Appolonii do uzupełnienia.

### § 3. Akcje, rejestr, akcje własne, zastaw

- **Ocena:** zgodne.
- **Podstawa:** art. 300³¹, 300³³–300³⁴, 300⁴⁷ § 1 pkt 2, § 2–3 i § 9, art. 300¹⁵ § 2 i 4–6 KSH **[Z]**.
- **Uwagi:**
  - wykup akcji własnych tylko w celu umorzenia albo dla programu P i serii F, upoważnienie najwyżej na 5 lat (ustawa takiego limitu w P.S.A. nie przewiduje — memorandum 1.3.5 **[Z]**);
  - Spółka nie nabywa akcji w vestingu;
  - zastawnik i użytkownik nie głosują; wyjątek za zgodą WZ (75%) dla zastawu zabezpieczającego finansowanie Spółki, przy spełnieniu warunków ustawowych.

### § 4. Objęcie akcji i wkłady

- **Ocena:** zgodne, pod warunkiem wykonania czynności przy akcie (K1, K2) i wyceny (K3).
- **Podstawa:**
  - KSH: art. 300² § 1–2, art. 300³, art. 300⁵ § 1 pkt 4, art. 300⁹, art. 300¹⁰, art. 300¹¹, art. 300¹² § 3, art. 300¹²³, art. 300¹²⁴, art. 587 § 1, art. 14 **[Z]**;
  - prawo autorskie: art. 41 ust. 2–4, art. 46, art. 53, art. 74 ust. 4 **[Z]**;
  - art. 64 KC **[Z]**.
- **Orzecznictwo:**
  - SN II CSKP 593/22 **[Z]** — wyrok zastępuje oświadczenie potrzebne do wykonania istniejącego obowiązku;
  - SN I CK 381/05, III CK 124/05 **[S]** — pola eksploatacji muszą być wymienione wyraźnie i znane w chwili umowy.
- **Uwagi:**
  - ust. 6 jest kompletny: forma, pola eksploatacji, prawa zależne, współtwórcy, wynagrodzenie = akcje, licencja tymczasowa, wykonanie w naturze;
  - ust. 5 rozstrzyga kolejność: IP w dniu aktu, pozostałe wkłady niepieniężne do 14 dni po wpisie.

### § 5–7. Emisje, seria F, seria P

- **Ocena:** zgodne.
- **Podstawa:** art. 300¹⁰³–300¹⁰⁷, 300¹¹⁴–300¹¹⁸ **[W]**; art. 300² § 2, art. 300¹⁰⁴ § 1 pkt 7 **[Z]**.
- **Uwagi:**
  - regulamin programu P zatwierdza WZ (§ 7 ust. 5), co wspiera preferencję z art. 24 ust. 11 PIT (memorandum T9 pkt 1);
  - podatek przy serii F za pracę — interpretacja (T9 pkt 2).

### § 8. Zbywanie

- **Ocena:** zgodne warunkowo.
- **Podstawa:** art. 300³⁹ § 1–6, art. 300³⁴ § 6 KSH **[Z]**.
- **Orzecznictwo:**
  - SN II CRN 60/93 **[S]** — bezskuteczność zawieszona przy braku zgody; zgoda działa wstecz;
  - SN V CSK 274/21 **[S]** i SA w Gdańsku V AGa 158/20 **[S]** — tak samo;
  - SN I CSK 132/11 **[S]** — skutki zależą od rodzaju ograniczenia.

  Orzeczenia dotyczą sp. z o.o. (art. 182 KSH, ta sama klauzula dyspozytywna co art. 300³⁹ § 2 — memorandum 1.2.1 **[Z]**); stosowanie do P.S.A. przez analogię **[W]**.

- **Uwagi:**
  - fikcja zgody po 14 dniach jest wsparta zaświadczeniem i obowiązkiem w umowie z podmiotem prowadzącym rejestr (adres doręczenia: siedziba albo adres do doręczeń elektronicznych);
  - wyłączenie art. 300³⁹ § 3–5 jest do obrony, bo każda przyczyna odmowy jest przejściowa albo usuwalna (art. 58 § 2, art. 353¹ KC **[Z]**).

### § 9. Obowiązek zbycia (vesting)

- **Ocena:** zgodne.
- **Podstawa:**
  - KSH: art. 300¹ § 3, art. 300³³ § 1 pkt 10–11, art. 300³⁹ § 1, art. 300⁴⁵ § 1–2, art. 300⁴⁷ § 9 **[Z]**;
  - art. 64 i 101 § 1 KC **[Z]**;
  - PIT: art. 17 ust. 2, art. 19, art. 11 ust. 2b **[Z]**.
- **Orzecznictwo:** SN V CSK 522/18 **[Z]**, SN II CSKP 593/22 **[Z]**.
- **Uwagi:**
  - nabywca to osoba wskazana przez Radę (nie Spółka); w braku wskazania — pozostali założyciele; po 6 miesiącach obowiązek wygasa;
  - akcje zbyte, zwolnione albo z wygasłym obowiązkiem przestają być nim objęte, a Spółka zgłasza to do rejestru;
  - umowa wykonawcza dokumentuje źródło ceny (art. 19 PIT — „uzasadniona przyczyna”);
  - umowę wykonawczą z założycielem-dyrektorem podpisuje pełnomocnik.

### § 10–11. Rada Dyrektorów i reprezentacja

- **Ocena:** zgodne.
- **Podstawa:** art. 300⁵⁵ § 1, 300⁵⁸ § 2, 300⁷³, 300⁷⁵–300⁷⁶, 300⁷⁹ § 1–4, art. 15 § 1 KSH **[Z]**; art. 300¹²⁵ § 2 (BJR) **[S]**.
- **Orzecznictwo:** SN II CSKP 1733/22 **[S]** — umowa z członkiem zarządu bez właściwej reprezentacji; przeważający pogląd o nieważności (glosy).
- **Uwagi:**
  - pełnomocnik do rodzajów umów, wskazywany w uchwale (może zapaść poza WZ — art. 300⁸⁰ **[Z]**), nie może być stroną umowy;
  - **ryzyko rezydualne:** dopuszczalność pełnomocnika „rodzajowego” nie jest przesądzona w orzecznictwie. Bezpieczniej wskazywać konkretne umowy albo pakiety.

### § 12. Uchwały akcjonariuszy

- **Ocena:** zgodne.
- **Podstawa:** art. 300⁸⁰ § 1–3, art. 300⁹² KSH **[Z]**.
- **Uwagi:**
  - uchwała obiegowa zapada przed terminem tylko przy wymaganej większości **wszystkich** głosów, więc późniejsze głosy nie mogą zmienić wyniku;
  - regulamin WZ przyjmowany przy zawiązaniu.

### § 13. Sprawy zastrzeżone

- **Ocena:** zgodne.
- **Uwagi:** 11 pozycji (75% wszystkich głosów), w tym Umowa o Współpracy (lit. j) i umowy finansowe z dyrektorami (lit. k — art. 15 § 1 KSH nie obejmuje dyrektora P.S.A. **[Z]**).

### § 14. Własność intelektualna, poufność, eksport, konkurencja

- **Ocena:** zgodne.
- **Podstawa:**
  - prawo autorskie: art. 9, 12, 16, 41, 46, 50, 53, 74 **[Z]**; art. 43 ust. 1 **[S/W]**; art. 67 ust. 5, art. 68 **[S]**;
  - PWP: art. 11 ust. 3 **[Z]**;
  - KSH: art. 300¹ § 3 **[Z]**.
- **Orzecznictwo:** SN I CSKP 62/21, SA w Warszawie VI ACa 1735/14 (licencja dorozumiana), SN II CK 51/04 (art. 68) **[S]**.
- **Uwagi:**
  - obowiązek umów IP ciąży na Spółce wobec pracowników i współpracowników oraz na Założycielach;
  - licencja na technologię sprzed założenia przedłuża się automatycznie; przy odmowie przedłużenia Rada żąda przeniesienia;
  - zakaz konkurencji obejmuje założycieli, Akcjonariuszy Funkcjonalnych (dopóki są akcjonariuszami) i dyrektorów;
  - licencja nieodpłatna — ryzyko podatkowe (Ś7).

### § 15. Współpraca ze Spółką Siostrzaną — punkt 3.

### § 16–18. Zysk, likwidacja, postanowienia końcowe

- **Ocena:** zgodne.
- **Uwagi:**
  - zaliczki na dywidendę (ust. 4) z testem wypłacalności;
  - rok obrotowy (ust. 5) z odesłaniem do art. 3 ust. 1 pkt 9 ustawy o rachunkowości **[W]** — do potwierdzenia z księgowym;
  - mediacja nie wpływa na terminy zaskarżenia uchwał;
  - uchwały założycielskie obejmują pełnomocnika do umów z dyrektorami.

---

## 3. Struktura Basilisk–Appolonia

- **Konstrukcja § 15.** Dopuszczalna jako postanowienia umów spółek (art. 300¹ § 3 KSH, art. 353¹ KC **[Z]**).
  - Status trwa, dopóki założyciele obu spółek łącznie mają ponad 50% głosów w każdej z nich.
  - Wyłączenia zakazu konkurencji i poufności są skuteczne, bo te obowiązki wynikają z samej umowy.
- **Konflikt interesów (Ś rezydualne).**
  - Ustawowego obowiązku ujawnienia i wstrzymania się (art. 300⁵⁵ § 1 **[Z]**) umowa nie uchyli. Ochrona BJR (art. 300¹²⁵ § 2 **[S]**) zakłada lojalność.
  - Zabezpieczenia: Umowa o Współpracy zatwierdzona jednomyślnie przez WZ obu spółek, póki akcjonariat jest identyczny; metody cen; niezależny biegły.
  - Przy wejściu inwestora do jednej spółki potrzebny jest przegląd tych zabezpieczeń.
- **Dominacja.** Unia personalna Rad może tworzyć dominację (art. 4 § 1 pkt 4 lit. d KSH **[S]**). Obowiązek zawiadomienia (art. 6 KSH **[S]**) ma znaczenie dopiero przy wzajemnych udziałach. Te są możliwe tylko za zgodą WZ (75%), z zawiadomieniem (§ 15 ust. 9).
- **Grupa spółek** (art. 21¹–21¹⁶ KSH, Dz.U. 2022 poz. 807 **[S]**) wymaga spółki dominującej — opcja na etap holdingu.
- **IP między spółkami:**
  - forma pisemna dla przeniesień i licencji wyłącznych **[S]**;
  - współtwórcy (art. 9 **[Z]**);
  - prawa do utworu osoby pracującej dla obu spółek — dla spółki, do której obszaru utwór należy (§ 15 ust. 5).
- **Konsorcjum, przetargi, granty:**
  - umowa konsorcjum co do zasady nie jest spółką cywilną (SA w Warszawie VI ACa 357/16 **[S]**), ale zależy to od treści;
  - wspólne oferty zamiast osobnych (art. 108 ust. 1 pkt 5 Pzp **[S]**), solidarna odpowiedzialność wykonawców wspólnych (art. 445 Pzp **[W]**);
  - EDF: co najmniej 3 podmioty z 3 państw **[S]**.
- **Podatki:** nieodpłatne świadczenia (NSA II FPS 1/06 **[S]**), ceny transferowe (art. 11a CIT **[W]**).
- **Appolonia:**
  - umowa jest lustrzana i ma wszystkie poprawki rund 1–3;
  - otwarte: pisownia firmy, siedziba, skład założycieli, weryfikacja kodów PKD (w tym morskich kodów usługowych).

---

## 4. Orzecznictwo — zestawienie

| Sygnatura | Sąd, data | Teza (w zakresie istotnym dla audytu) | Zastosowanie | Weryf. |
|-----|-----|---------------|-----|--|
| II CSKP 593/22 | SN, 9.12.2022 | Art. 64 KC nie tworzy obowiązku, ale wyrok zastępuje oświadczenie potrzebne do wykonania istniejącego obowiązku | § 4 ust. 6, § 9 | [Z] |
| V CSK 522/18 | SN, 23.06.2020 | Stosunek podstawowy wyznacza dopuszczalność zrzeczenia się odwołania pełnomocnictwa | § 9 ust. 6 | [Z] |
| III CZP 109/22 | SN | Rozdzielność majątkowa nie daje drugiemu małżonkowi praw korporacyjnych | akcje w majątku wspólnym | [Z] |
| III CSKP 65/21 | SN | Akcjonariuszem jest małżonek, który objął akcje i jest wpisany do rejestru | jw. | [Z] |
| III CZP 32/16 | SN | Udziały mogą należeć do majątku wspólnego (analogicznie akcje) | jw. | [Z] |
| III CZP 13/13 | SN (7), 18.09.2013 | Zaskarżanie uchwał organów zarządzających — powództwo o ustalenie | uchwały Rady | [W] |
| II CRN 60/93 | SN, 7.09.1993 | Zbycie bez zgody spółki — bezskuteczność zawieszona; zgoda działa wstecz | § 8 | [S] |
| V CSK 274/21 | SN | Brak zgody — bezskuteczność zawieszona, nie nieważność | § 8 | [S] |
| I CSK 132/11 | SN, 1.12.2011 | Skutki naruszenia ograniczeń zbywalności zależą od rodzaju ograniczenia | § 8 | [S] |
| V AGa 158/20 | SA w Gdańsku, 9.02.2021 | Umowa bez zgody organu — bezskuteczność zawieszona | § 8 | [S] |
| II CSKP 1733/22 | SN, 8.11.2024 | Umowa z członkiem zarządu a art. 210 KSH (glosy: nieważność bezwzględna jako pogląd przeważający) | § 11 ust. 3 | [S] |
| I CK 381/05 | SN, 8.03.2006 | Pola eksploatacji muszą być wyraźnie wymienione; pola nieznane wyłączone | § 14 ust. 1 lit. b | [S] |
| III CK 124/05 | SN, 14.09.2005 | Licencja obejmuje wyraźnie wymienione pola znane w chwili zawarcia | jw. | [S] |
| I CSKP 62/21 | SN, 13.05.2021 | Licencja niewyłączna bez formy pisemnej, możliwa konkludentnie (poza zamówieniami publicznymi) | § 4, § 14, § 15 | [S] |
| VI ACa 1735/14 | SA w Warszawie | Kontynuowanie współpracy jako licencja niewyłączna per facta concludentia | § 14 | [S] |
| II CK 51/04 | SN, 15.10.2004 | Zakres art. 68 ust. 2 pr. aut. | § 14 ust. 2 | [S] |
| SK 32/14 | TK, 23.06.2015 (Dz.U. 2015 poz. 932) | Ryczałt trzykrotności wynagrodzenia za naruszenie — niekonstytucyjny | ryzyko naruszeń IP | [S] |
| C-367/15 | TSUE, 25.01.2017 | Dwukrotność opłaty licencyjnej zgodna z dyrektywą 2004/48/WE | jw. | [S] |
| VI ACa 357/16 | SA w Warszawie | Konsorcjum: podtyp spółki cywilnej, spółka cywilna albo umowa samodzielna | konsorcjum | [S] |
| II FPS 1/06 | NSA (uchwała), 16.10.2006 | Szerokie pojęcie nieodpłatnego świadczenia | licencje nieodpłatne | [S] |
| KIO (wybór) | KIO | Odrębne oferty z jednej grupy kapitałowej — wykluczenie bez wykazania niezależności | przetargi | [S] |

**Luki w orzecznictwie** (wynik negatywny wyszukiwania): brak orzeczenia SN wprost o art. 41 ust. 3 pr. aut., o art. 300⁷⁹ KSH i o fikcji zgody na zbycie akcji P.S.A.

---

## 5. Lista kontrolna poza umową

**Przed aktem**

1. Uzgodnić z podmiotem prowadzącym rejestr akcjonariuszy:
   - mechanizm fikcji zgody (§ 8 ust. 1);
   - wzmianki o vestingu i lock-upie;
   - wykreślanie wzmianek po zakończeniu obowiązku (§ 9 ust. 7).
2. Wycena wkładów niepieniężnych z uzasadnieniem, spójna z PIT (K3).
3. Wykazy do aportu: repozytoria z commitami i sumami kontrolnymi, współtwórcy, open source z licencjami, oświadczenia o braku praw byłych pracodawców i uczelni.
4. Weryfikacja kodów PKD 2025. Dla Appolonii: firma, siedziba, skład założycieli.

**Przy akcie**

1. Uchwała założycielska o **pełnomocniku Spółki** z nazwiskiem i listą umów (§ 18 ust. 6, § 11 ust. 3).
2. Umowy przeniesienia aportu IP, podpisane po stronie Spółki przez pełnomocnika (§ 4 ust. 6).
3. Umowy wykonawcze vestingu z pełnomocnictwami (§ 9 ust. 6), z zapisem o źródle ceny.
4. Regulamin WZ, wybór podmiotu prowadzącego rejestr, pierwsi dyrektorzy.

**Po wpisie**

1. Wzmianki w rejestrze akcjonariuszy (od 18.02.2027 r. obowiązek zgłoszenia w 7 dni **[Z]**).
2. CRBR, NIP, VAT-R **[W]**.
3. Umowy o pracę albo B2B założycieli z klauzulami IP; kwartalne potwierdzenia utworów przez pełnomocnika.
4. Umowa o Współpracy z drugą spółką, zatwierdzona uchwałami WZ obu spółek (§ 13 lit. j).
5. Regulamin programu P zatwierdzony przez WZ (§ 7 ust. 5).
6. Wnioski o interpretacje podatkowe: aport IP, licencje nieodpłatne, cena emisyjna w vestingu, seria F, seria P.

---

## 6. Pytania do prawnika i doradcy podatkowego

1. Art. 300⁷⁹ § 1 KSH: czy pełnomocnik może być powołany do **rodzaju** umów (kwartalne potwierdzenia) czy wyłącznie do konkretnych umów?
2. Fikcja zgody na zbycie (§ 8 ust. 1): czy podmioty prowadzące rejestr akceptują taki mechanizm? Czy bezpieczniejszy jest sprzeciw (art. 300³⁹ § 1 „w inny sposób”)?
3. Art. 41 ust. 3 pr. aut.: czy przejście praw „z chwilą przekazania” w ramach zadań i kwartalne potwierdzenia wystarczą bez umowy o pracę albo B2B?
4. Art. 4 § 1 pkt 4 lit. d i art. 6 KSH w relacji sióstr z tymi samymi dyrektorami; stosowanie progu „kapitału zakładowego” do kapitału akcyjnego P.S.A.
5. Art. 3 ust. 1 pkt 9 ustawy o rachunkowości — łączenie pierwszego roku obrotowego (§ 16 ust. 5).
6. Pzp i EDF: czy Basilisk i Appolonia tworzą grupę kapitałową w rozumieniu u.o.k.k.? Jakie jest ostateczne brzmienie wymogu niezależności członków konsorcjum EDF?
7. Podatki:
   - PIT od aportu IP;
   - przychód Spółki z licencji nieodpłatnych;
   - cena emisyjna w vestingu (art. 19 PIT, art. 11 ust. 2b PIT);
   - seria F za pracę;
   - preferencja z art. 24 ust. 11 PIT dla serii P;
   - ceny transferowe między siostrami;
   - wymiana akcji przy ewentualnym holdingu.

---

## Źródła

**Repozytorium:** `memorandum.md` (1.1.4, 1.2.1, 1.3.5, 1.5.1, 1.5.2, 2.2.4, 2.3.3, 3.1.1–3.1.3, T4, T9), `psa_feedback.tex`, `prosta.md`, `analiza_ip_aport.md`, `audyt_rundy.md`, rozporządzenie MS w sprawie wzorca S24 (Dz.U. 2021 poz. 1191).

**Wyszukiwanie (poziom [S]):**

Prawo spółek

- art. 300⁷⁹ KSH: [lexlege.pl](https://lexlege.pl/ksh/art-300-79/)
- art. 300³⁹ KSH: [lexlege.pl](https://lexlege.pl/ksh/art-300-39/)
- art. 4 KSH: [lexlege.pl](https://lexlege.pl/ksh/art-4/); unia personalna: [rp.pl](https://pro.rp.pl/prawo-w-firmie/art13279531-powolywanie-tych-samych-osob-do-zarzadow-spolek-zaleznych-moze-byc-ryzykowne)
- art. 6 KSH: [lexlege.pl](https://lexlege.pl/ksh/art-6/)
- Grupa spółek: [Dz.U. 2022 poz. 807](https://api.sejm.gov.pl/eli/acts/DU/2022/807/text/T/D20220807L.pdf), [lexlege.pl](https://lexlege.pl/ksh/dzial-iv-grupa-spolek/15384/)
- BJR: [codozasady.pl](https://codozasady.pl/en/p/the-business-judgment-rule), [apcz.umk.pl](https://apcz.umk.pl/SIT/article/view/36110)
- II CSKP 1733/22 — glosa: [journals.umcs.pl](https://ns2.journals.umcs.pl/glosa/article/download/19897/pdf)
- V CSK 274/21: [sn.pl](https://www.sn.pl/sites/orzecznictwo/Orzeczenia3/V%20CSK%20274-21.pdf); I CSK 132/11: [standardyprawa.pl](https://standardyprawa.pl/orzeczenie/38302); V AGa 158/20: [dlajurysty.pl](https://dlajurysty.pl/orzeczenia/pokaz/54999/V-AGa-158-20)

Prawo autorskie

- I CK 381/05: [dlajurysty.pl](https://dlajurysty.pl/orzeczenia/pokaz/34704/I-CK-381-05); III CK 124/05: [dlajurysty.pl](https://dlajurysty.pl/orzeczenia/pokaz/35399/III-CK-124-05)
- Licencja dorozumiana (I CSKP 62/21, VI ACa 1735/14): [legeartis 2022/01](https://czasopismo.legeartis.org/2022/01/udzielenie-licencji-korzystanie-oprogramowania-per-facta-concludentia-zamowienie-publiczne/), [legeartis 2022/07](https://czasopismo.legeartis.org/2022/07/dorozumiane-przedluzenie-licencji-korzystanie-utworu-oprogramowania-per-facta-concludentia/)
- art. 41 ust. 3: [e-prawnik.pl](https://e-prawnik.pl/artykuly/czy-mozna-zawrzec-umowe-przeniesienia-autorskich-praw-majatkowych-do-wszystkich-utworow.html)
- art. 43: [lexlege.pl](https://lexlege.pl/ustawa-o-prawie-autorskim-i-prawach-pokrewnych/art-43/)
- art. 67: [lexlege.pl](https://lexlege.pl/ustawa-o-prawie-autorskim-i-prawach-pokrewnych/art-67/); projekt formy dokumentowej: [legeartis 2025/05](https://czasopismo.legeartis.org/2025/05/forma-dokumentowa-umowy-przeniesienie-praw-autorskich-licencji-wylacznej-rygore-niewaznosci-projekt/)
- art. 68: [lexlege.pl](https://lexlege.pl/ustawa-o-prawie-autorskim-i-prawach-pokrewnych/art-68/); II CK 51/04 w literaturze: [PPUW 2/2015](https://lawreview.wpia.uw.edu.pl/wp-content/uploads/2017/07/99_PDFsam_PPUW-2-2015-www.pdf)
- art. 74: [lexlege.pl](https://lexlege.pl/ustawa-o-prawie-autorskim-i-prawach-pokrewnych/art-74/)
- TK SK 32/14: [Dz.U. 2015 poz. 932](https://eli.gov.pl/api/acts/DU/2015/932/text/T/D20150932TK.pdf), [legeartis](https://czasopismo.legeartis.org/2015/06/wyrok-prawo-autorskie-sk-32-14/)
- TSUE C-367/15: [legeartis](https://czasopismo.legeartis.org/2017/01/odszkodowanie-dwukrotnosc-wynagrodzenia/)

Konsorcjum, przetargi, granty

- Konsorcjum a spółka cywilna: [standardyprawa.pl](https://standardyprawa.pl/standardy/3081), [podatki.biz](https://www.podatki.biz/artykuly/kwestie-zwiazane-z-konsorcjami-i-ksztaltowaniem-ich-relacji-wewnetrznych-i-zewnetrznych_34_45295.htm)
- Pzp, grupa kapitałowa: [rp.pl](https://pro.rp.pl/biznes/art42532791-jedna-grupa-kapitalowa-kilka-odrebnych-ofert-w-przetargu)
- EDF: [EUR-Lex 2021/697](https://eur-lex.europa.eu/eli/reg/2021/697), [streszczenie PE](https://oeil.europarl.europa.eu/oeil/en/document-summary?id=1655439)

Podatki

- NSA II FPS 1/06: [KIDP](https://archiwumdebata.kidp.pl/materialy/nieodplatne_swiadczenie.pdf)
- Wymiana udziałów: [poradnikprzedsiebiorcy.pl](https://poradnikprzedsiebiorcy.pl/-zamiana-udzialow-w-spolce-kiedy-jest-neutralna-podatkowo)
