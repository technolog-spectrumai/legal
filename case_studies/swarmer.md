# Case study: Swarmer — wzrost, historia VC i IPO na Nasdaq

Dokument wewnętrzny Basilisk Systems, informacyjny. Nie jest opinią prawną ani rekomendacją inwestycyjną i nie zmienia umowy spółki. Jedno ze studiów przypadku o rozwoju i finansowaniu firm obronnych, robotyki i fizycznego AI (przegląd i porównanie: `case_studies/README.md`). Opisuje, jak ukraiński startup oprogramowania do rojów dronów przeszedł w niecałe trzy lata od założenia do notowania na Nasdaq, jak wyglądała jego droga przez VC i co z tego wynika dla Basiliska. Odesłania do umowy według `psa.tex` w wersji 0.9.4-C (numery § według `spis_tresci.md`); uzupełnia `vc.md` (oczekiwania funduszy), `regulations.md` sekcja 3 (wymogi właścicielskie programów), `emisja/inwestor.md` (seria inwestorska) i pytanie o jurysdykcję z `psa_todo.md` sekcja 1.

Stan na 30 września 2026 r. Oznaczenia wiarygodności: **[Z]** — fakt z dokumentu pierwotnego (sprawozdanie SEC, komunikat spółki albo inwestora w serwisie agencyjnym, transkrypcja wyników); **[M]** — doniesienie prasowe albo baza danych; **[W]** — wiedza ogólna o prawie albo praktyce rynkowej, do potwierdzenia u kancelarii; **[?]** — szacunek, w tym własne obliczenie z cytowanych liczb, albo teza niepotwierdzona. Uwaga metodyczna: w tej sesji strony źródłowe (sec.gov, businesswire.com, forbes.ua, ain.ua, dou.ua i inne) były niedostępne do pełnego odczytu z powodu blokady sieciowej; fakty pochodzą ze streszczeń wyszukiwarki, a **[Z]** przyznano tylko tam, gdzie streszczenie dokumentu pierwotnego było jednoznaczne. Przed użyciem liczb poza firmą trzeba je sprawdzić w podlinkowanym dokumencie (numery akcesji SEC w sekcji 12).

---

## 1. Główny wniosek

1. **Swarmer to najkrótsza znana droga od założenia do giełdy w defense tech:** spółka zawiązana w maju 2023 r., seed 2,7 mln USD we wrześniu 2024 r., seria A 15 mln USD we wrześniu 2025 r., IPO na Nasdaq Capital Market 17 marca 2026 r. za 17,25 mln USD brutto **[Z]**. Łącznie ok. 18,5 mln USD kapitału prywatnego, 17,25 mln USD z IPO i ok. 27 mln USD z linii kapitałowej po IPO **[?]** (własne sumowanie, sekcje 5 i 6).
2. **Giełda była substytutem serii B, nie wyjściem.** IPO o wartości 15–17 mln USD z jednym butikowym gwarantem, przy przychodach 0,31 mln USD za 2025 r. i stracie 8,5 mln USD **[Z]**, dało spółce walutę akcyjną, którą w czerwcu 2026 r. spieniężono przez linię kapitałową (27,2 mln USD), a we wrześniu 2026 r. użyto do przejęcia Ratel Robotics za do 224 mln USD, głównie w akcjach **[Z]**.
3. **Kurs: 5 USD → 31 USD pierwszego dnia (+520 %) → maksimum 83,30 USD → 16,37 USD 29 września 2026 r.** Dwa największe spadki (czerwiec: −28,9 %; wrzesień: ponad −41 % w tygodniu) zbiegły się z podażą akcji (linia kapitałowa, koniec lock-upu), nie z wynikami **[M]**.
4. **Struktura od pierwszego dnia była amerykańska:** Swarmer, Inc. w Delaware (15 maja 2023 r.), spółki operacyjne w Ukrainie, Estonii i Polsce; główny kontrakt ukraiński zawarła spółka estońska **[Z]**. Kapitał pochodził wyłącznie od inwestorów z USA i Wielkiej Brytanii; pieniądze bezzwrotne to jeden grant Brave1 (2 mln UAH, ok. 50 tys. USD) **[M]**.
5. **Ład korporacyjny zmienił się szybciej niż produkt:** przewodniczącym rady został w grudniu 2025 r. Erik Prince (założyciel Blackwater), założyciel-CEO odszedł ze stanowiska cztery miesiące po IPO, a strategia z „oprogramowania autonomii" przeszła w „platformę przejęć" **[Z]**.
6. **Dla Basiliska:** droga Swarmera (spółka-matka w USA, kapitał z USA, mikro-IPO na Nasdaq) wyklucza się z drogą programów UE (EDF, AGILE, EUDIS: art. 9 rozporządzenia 2021/697) i wymagałaby zmian w Kryterium § 11. P.S.A. nie może być notowana (art. 300³⁶ § 2 KSH), więc każda ścieżka giełdowa Basiliska zaczyna się od przekształcenia w S.A. (§ 25 ust. 1 lit. e) i od zdjęcia ograniczeń obrotu z § 10–16. Szczegóły w sekcji 10.

---

## 2. Profil

| Element | Swarmer | Wiar. |
|---|---|---|
| Założenie | maj 2023 r.; Swarmer, Inc. zarejestrowana w Delaware 15 maja 2023 r. | [Z] |
| Założyciele | Serhii Kupriienko (wcześniej szef zespołu AI w Amazon Ring w Ukrainie; Politechnika Czernihowska, Stanford GSB) i Alex Fink (wcześniej CEO Otherweb; Technion) | [M] |
| Siedziba i struktura | centrala Austin (Teksas); spółki zależne: Autonomous Robotics Systems LLC (Kijów), Swarmer Estonia OÜ, biuro w Warszawie; zespoły inżynierskie w Kijowie i Warszawie | [Z]/[M] |
| Produkt | STYX (dowodzenie i planowanie misji: jeden operator dla wielu platform), MINAS (autonomia współdziałania heterogenicznych zespołów), TRIDENT (wbudowany system operacyjny drona: sieć mesh, szyfrowanie, abstrakcja sprzętu); niezależny od producenta | [Z] |
| Model biznesowy | B2B2G: licencje dla producentów dronów i integratorów, bez bezpośredniej sprzedaży państwu; w 2024–2025 r. jeden klient (Smart Machinery Solutions), który już nie kontraktuje | [Z] |
| Skala użycia | ponad 100 tys. misji bojowych w Ukrainie od kwietnia 2024 r. (własny licznik telemetryczny spółki) | [Z] |
| Zespół | 62 osoby w chwili IPO, 74 osoby 26 lipca 2026 r., ok. 500 pro forma po przejęciu Ratel | [Z] |
| Notowanie | Nasdaq Capital Market, ticker SWMR, od 17 marca 2026 r.; SEC CIK 2092574 | [Z] |

---

## 3. Jak zaczęli: kapitał początkowy i pierwsze lata

**Skąd wzięły się pierwsze pieniądze (maj 2023 – wrzesień 2024)**

- **Założyciele i ich wkład.** Serhii Kupriienko kierował przed inwazją zespołem AI w ukraińskim oddziale Amazon Ring; Alex Fink był seryjnym założycielem w USA (Otherweb). Spółkę-matkę zarejestrowali w Delaware 15 maja 2023 r. i włożyli ok. 70 tys. USD własnych pieniędzy **[Z]/[M]**. Pierwszy produkt opisano jako „AI Flight Control Center", które ma odciążyć operatorów od rutynowych zadań przy misjach wielu dronów **[M]**.
- **Akcelerator jako pierwszy inwestor (listopad 2023 r.).** D3 (Dare to Defend Democracy), pierwszy fundusz i akcelerator defense tech w Kijowie (fundusz 10 → 30 mln USD, wśród LP Eric Schmidt), objął SAFE; kwoty nie ujawniono, standardowy czek programu to 125 tys. USD **[M]**. D3 dało też dostęp do amerykańskich inwestorów, którzy potem poprowadzili seed i serię A.
- **Front jako pierwszy klient (kwiecień 2024 r.).** Oprogramowanie trafiło do jednostek przez ukraińskiego producenta dronów (Smart Machinery Solutions), jedynego klienta w 2024–2025 r.; przychody 2024 r. wyniosły 329 tys. USD, ale każda misja zasilała licznik telemetryczny, który stał się głównym argumentem inwestycyjnym **[Z]**.
- **Państwo bez pieniędzy, ale z poligonem (sierpień 2024 r.).** Brave1, ukraiński klaster defense tech, dał grant 2 mln UAH (ok. 50 tys. USD) oraz poligony, testy na froncie i kontakty z inwestorami i wystawami (Warszawa, Kraków, seminarium duńsko-ukraińskie) **[M]**.
- **Seed po 16 miesiącach (wrzesień 2024 r.).** 2,7 mln USD na SAFE od R-G.AI (lider), Radius Capital Ventures, Green Flag Ventures i D3; Green Flag inwestuje tylko w ukraińskie firmy dual-use od TRL 6, więc warunkiem był działający produkt w polu **[M]**.

**Jak z tego wyrosła firma (2024–2026)**

- Zespół pozostał mały (62 osoby przy IPO), a produkt stał się platformą trzech warstw (STYX, MINAS, TRIDENT) integrowaną z dronami różnych producentów; licznik misji rósł z zera (kwiecień 2024 r.) do 70 tys. (wrzesień 2025 r.) i ponad 100 tys. (2026 r.) **[Z]/[M]**.
- Kapitał początkowy przed seedem to łącznie ok. 245 tys. USD (założyciele, D3, Brave1) **[?]**; przez pierwsze 28 miesięcy do serii A spółka zebrała ok. 3 mln USD, a mimo to zamknęła serię A na 15 mln USD i weszła na giełdę bez znaczących przychodów, bo inwestorzy wyceniali dane z pola walki, nie sprzedaż.
- Dwa elementy tej ścieżki nie dadzą się przenieść do Polski: popyt wojenny, który dał realnego użytkownika w 11 miesięcy od założenia, oraz akcelerator z amerykańskimi LP, który otworzył drogę do kapitału z USA. Odpowiednikiem dla Basiliska są NATO DIANA (100 tys. EUR w fazie 1), voucher EUDIS (65 tys. EUR) i fundusze pre-seed z udziałem PFR (`regulations.md` sekcja 3), a zamiast frontu płatny pilot z producentem dronów w modelu § 33 **[?]**.

---

## 4. Oś czasu

| Data | Zdarzenie | Kwota / szczegół | Wiar. |
|---|---|---|---|
| 15 maja 2023 | zawiązanie Swarmer, Inc. (Delaware); środki własne założycieli | ok. 70 tys. USD | [Z]/[M] |
| 16 listopada 2023 | inwestycja akceleratora D3 (Dare to Defend Democracy; wśród LP Eric Schmidt), instrument SAFE | kwota nieujawniona; standardowy czek D3 to 125 tys. USD | [M] |
| kwiecień 2024 | pierwsze użycie na froncie (start licznika misji) | — | [Z] |
| 27 sierpnia 2024 | grant Brave1 | 2 mln UAH (ok. 50 tys. USD) | [M] |
| 16 września 2024 | seed na SAFE, lider R-G.AI; Radius Capital Ventures, Green Flag Ventures, D3 | 2,7 mln USD (Forbes.ua: 2,6 mln) | [M] |
| 2024 | przychody roczne (jeden klient) | 329 410 USD | [Z] |
| 16 września 2025 | seria A, lider Broadband Capital Investments (Michael Rapp); R-G.AI, D3, Green Flag, Radius, Network VC | 15 mln USD w komunikacie; w prospekcie 2 491 721 akcji uprzywilejowanych A-1 po 6,2711 USD ≈ 15,6 mln USD, zamknięcia od września 2025 do stycznia 2026 | [Z] |
| 17 września 2025 | Forbes Ukraine szacuje wycenę | 35–70 mln USD | [?] |
| 5 listopada 2025 | Oppenheimer Syndicate (Network VC), bilety od 5 tys. USD | 500 tys. USD (najpewniej w ramach zamknięć A-1) | [M]/[?] |
| grudzień 2025 | Erik Prince przewodniczącym rady dyrektorów (bez funkcji wykonawczych) | — | [Z] |
| 31 grudnia 2025 | wyniki 2025: przychody 309 920 USD, strata netto 8,5 mln USD, gotówka 9,3 mln USD | — | [Z] |
| 2 lutego 2026 | publiczne złożenie S-1 (wcześniej poufny DRS) | — | [Z] |
| 16 marca 2026 | S-1 skuteczny; cena IPO | 5,00 USD za akcję, 3 000 000 akcji | [Z] |
| 17 marca 2026 | pierwszy dzień notowań | otwarcie 12,50 USD, zamknięcie 31,00 USD | [M] |
| 18 marca 2026 | zamknięcie IPO z pełną opcją dodatkowego przydziału | 3 450 000 akcji, 17,25 mln USD brutto, ok. 14,7 mln USD netto; maksimum dnia 65,04 USD | [Z] |
| 13 maja 2026 | wyniki I kw. 2026 (przychody 20 325 USD, strata 4,46 mln USD, gotówka 23,5 mln USD); kontrakt Meta Bureau (drony SkyKnight) zawarty ze Swarmer Estonia OÜ | 2,86 mln USD za ponad 16 tys. licencji | [Z] |
| 10–11 czerwca 2026 | linia kapitałowa z Lucid (24 mies.) i rejestracja odsprzedaży 3 mln akcji; list Prince'a o strategii przejęć; kurs −28,9 % | do ok. 181 mln USD przy kursie 60,32 USD; sprzedano 654 734 akcje za 27,2 mln USD | [Z]/[M] |
| 29 czerwca 2026 | rozszerzenie kontraktu SkyKnight o czeskiego Progress TRW (pierwszy klient z NATO) | +1,41 mln USD → 3,87 mln USD; do 14,2 mln USD z opcjami | [Z] |
| 26 lipca 2026 | Kupriienko rezygnuje z funkcji Global CEO (zostaje w radzie do 2029 r., kieruje „Swarmer Labs"); Fink jedynym CEO | — | [Z] |
| 9 sierpnia 2026 | Kupriienko wykonuje opcje | 3 997 762 nowe akcje | [Z] |
| 13 sierpnia 2026 | wyniki II kw. 2026: przychody 216 413 USD, koszty operacyjne 7,5 mln USD, strata 7,3 mln USD, gotówka 25,3 mln USD | backlog: 16,3 mln USD umów + 16,8 mln USD MoU | [Z] |
| 21 sierpnia 2026 | Vectus Air Defense Systems („obrona powietrzna jako usługa"): Swarmer 20 %, Prince 80 % | — | [Z] |
| 10 września 2026 | umowa przejęcia Ratel Robotics (ukraiński producent UGV, ponad 300 osób, 86 mln USD kontraktów w 2026 r.) | do 224 mln USD: ok. 7,2 mln USD gotówki + 1 064 942 akcje przy zamknięciu; earn-out 7,2 mln USD + do 4 422 125 akcji do 2028 r. | [Z]/[M] |
| 14–15 września 2026 | koniec 180-dniowego lock-upu (ok. 9,35 mln akcji, ok. 59 % kapitału); kurs −26,6 % jednego dnia, ponad −41 % w tygodniu | — | [M] |
| 29 września 2026 | kurs zamknięcia | 16,37 USD; ok. 15,6 mln akcji → ok. 255 mln USD kapitalizacji | [M]/[?] |

---

## 5. Finansowanie prywatne: runda po rundzie

| Runda | Data | Kwota | Instrument | Lider i uczestnicy | Wycena | Wiar. |
|---|---|---|---|---|---|---|
| Środki założycieli | 2023 | ok. 70 tys. USD | kapitał własny | Kupriienko, Fink | — | [M] |
| Pre-seed / akcelerator | listopad 2023 | nieujawniona (standard 125 tys. USD) | SAFE | D3 (fundusz i akcelerator) | — | [M] |
| Grant | sierpień 2024 | 2 mln UAH (ok. 50 tys. USD) | bezzwrotny | Brave1 (ukraiński klaster defense tech) | — | [M] |
| Seed | 16 września 2024 | 2,7 mln USD | SAFE (kilka transz z różnymi capami) | R-G.AI (lider); Radius Capital Ventures, Green Flag Ventures, D3 | nieujawniona | [M]; instrument [Z] |
| Seria A | 16 września 2025 – styczeń 2026 | 15 mln USD (komunikat); ok. 15,6 mln USD (prospekt) | akcje uprzywilejowane A-1 po 6,2711 USD | Broadband Capital Investments (lider); R-G.AI, D3, Green Flag, Radius, Network VC; syndykat Oppenheimer 0,5 mln USD | nieujawniona; Forbes.ua 35–70 mln USD; z liczby akcji w prospekcie ≈ 66 mln USD post-money **[?]** | [Z] |
| **Razem prywatnie** | | **≈ 18,5 mln USD** (media: 17,9 mln w październiku 2025, „prawie 20 mln" w marcu 2026) | | | | [?] |

Co pokazuje prospekt o mechanice **[Z]**, z zastrzeżeniem, że liczby trzeba potwierdzić w 424B4 (akcesja 0001104659-26-029590):

- **SAFE zamieniono przy serii A na kilka podserii akcji uprzywilejowanych** (A-2 po 0,2975 USD, A-3 po 0,5000 USD, A-4 po 1,1667 USD, A-5 po 1,2499 USD, A-6 po 2,6663 USD; łącznie ok. 1,73 mln akcji). Posiadacze SAFE: D3 Fund LP, RG.AI Technologies Inc., Green Flag Fund I LP, Radius Fund I LP. Suma kapitału z konwersji (ok. 1,7 mln USD) jest niższa od ogłoszonych 2,7 mln USD seedu; różnica nierozstrzygnięta **[?]**.
- **Seria A-1**: 2 491 721 akcji po 6,2711 USD w kilku zamknięciach (wrzesień 2025 – styczeń 2026); cena A-1 była ponad dwukrotnie wyższa od najwyższego capu SAFE i dwudziestokrotnie wyższa od najniższego.
- **Cap table przed IPO**: Theseus Capital Partners LLC 22,0 % (2 324 961 akcji; według Venture Capital Journal „brytyjski family office", nigdy nienazwany w komunikatach), D3 Fund LP 10,1 %; powyżej 5 % także RG.AI Technologies, Green Flag Fund, Radius Fund I; Michael Rapp (Broadband) 475 000 akcji, 4,37 % **[M]**. Z 22 % Theseusa wynika ok. 10,6 mln akcji przed IPO; pomnożone przez cenę A-1 daje ≈ 66 mln USD post-money serii A, a przy cenie IPO 5 USD ≈ 53 mln USD, czyli **IPO było wycenione poniżej rundy A**, co odwrócił dopiero pierwszy dzień notowań **[?]**.
- **Inwestorzy**: Green Flag Ventures (Los Angeles, od 2023 r., bilety 150 tys. – 1 mln USD przy wycenach 1–25 mln USD pre-money, tylko ukraińskie dual-use od TRL 6) **[M]**; R-G.AI (amerykańska firma obronna z ramieniem inwestycyjnym) **[M]**; D3 (fundusz 10 → 30 mln USD, akcelerator w Kijowie) **[M]**; Broadband Capital Investments (Floryda, Michael Rapp) **[M]**. Uzasadnienie lidera serii A: „tempo innowacji napędzane doświadczeniem z pola walki pozwala iterować szybciej niż tradycyjnym firmom obronnym" **[Z]**.
- **Cel serii A** (Kupriienko): interoperacyjność „klasy sojuszniczej", certyfikacje platform, testy odporności, szkolenia i wsparcie w polu; ekspansja do Japonii, UK, UE i USA **[M]**.

Kontekst: ukraiński defense tech pozyskał ok. 5 mln USD VC w 2023 r., ok. 59 mln USD w 2024 r. i 105–129 mln USD w 2025 r. (źródła się różnią); seria A Swarmera była wtedy największą rundą w sektorze i odpowiadała ok. 14 % rocznej sumy **[M]/[?]**. Porównywalne rundy: Buntar Aerospace 10,4 mln USD (2026, Axon), Farsight Vision 7,2 mln EUR (2026, Axon), Trypillian 5 mln USD (2025), HIMERA 1,2 mln USD; TAF Industries bez VC, z przychodów **[M]**.

---

## 6. IPO: przebieg, wycena, kurs i następstwa

### 6.1 Parametry oferty **[Z]**

| Parametr | Wartość |
|---|---|
| Emitent | Swarmer, Inc. (Delaware), Austin; CIK 2092574 |
| Droga | klasyczne IPO z gwarancją (firm commitment); nie SPAC, nie direct listing |
| Rynek | Nasdaq Capital Market (segment małych spółek), ticker SWMR |
| Harmonogram | poufny DRS (ok. stycznia 2026) → publiczny S-1 2 lutego 2026 → skuteczność i cena 16 marca → pierwszy dzień 17 marca → zamknięcie 18 marca 2026 |
| Cena i wolumen | 5,00 USD; 3 000 000 akcji + 450 000 z opcji dodatkowego przydziału (wykonana w całości) = 3 450 000 akcji |
| Wpływy | 17,25 mln USD brutto; ok. 14,7 mln USD netto; dyskonto gwaranta 0,30 USD na akcję |
| Gwarant i doradcy | Lucid Capital Markets LLC (jedyny bookrunner); IR: ICR; w spółce Chief Legal Officer Jennifer DeTrani |
| Wycena przy cenie oferty | ok. 60 mln USD kapitalizacji (Breakingviews) |
| Cel wpływów | bieżąca działalność, rozwój produktu, zatrudnienie, integracje ze sprzętem producentów, cele ogólne |
| Lock-up | 180 dni, do 14 września 2026 r.; objął ok. 9,35 mln akcji (ok. 59 % kapitału) **[M]** |
| Cap table po IPO | insiderzy ok. 58 %; największy pojedynczy akcjonariusz 33,5 %, drugi 17,3 % (bez nazwisk w streszczeniu) **[M]** |

### 6.2 Dlaczego giełda po sześciu miesiącach od serii A

- Fink: notowanie „aby pozyskać więcej środków i szybciej budować produkt, integrować więcej sprzętu i mieć jak największy wpływ na polu walki" **[M]**. Kupriienko: „albo my zautomatyzujemy pole walki, albo zrobią to nasi wrogowie" **[M]**.
- Resilience Media: spółka chciała pozyskać drugie 15 mln USD; apetyt inwestorów publicznych na ukraiński defense tech był łatwiejszy do wykorzystania niż VC obawiające się strefy wojny i ryzyka korupcyjnego **[M]**. Zamiar IPO sygnalizowano w prasie już w październiku 2025 r., miesiąc po serii A **[M]**.
- Deborah Fairlamb (Green Flag): „wybiera się USA, bo mają zdecydowanie największy rynek kapitałowy"; IPO „przełamało barierę dla amerykańskiego inwestora" **[M]**.
- Nie znaleziono śladu rozważania SPAC ani giełdy europejskiej **[?]**.

### 6.3 Notowania i ocena rynku **[M]**

| Moment | Kurs / zdarzenie |
|---|---|
| 17 marca 2026 | otwarcie 12,50 USD; zamknięcie 31,00 USD (+520 %); kapitalizacja ok. 382 mln USD |
| 18 marca 2026 | maksimum dnia 65,04 USD (ok. +950 % od ceny IPO w dwa dni) |
| marzec–kwiecień 2026 | maksimum 52-tygodniowe 83,30 USD; 2 kwietnia +42 % na nagłówkach o Iranie |
| 10–11 czerwca 2026 | −28,9 % po ogłoszeniu linii kapitałowej Lucid i listu Prince'a |
| 15 września 2026 | −26,6 % po wygaśnięciu lock-upu i przy ryzyku rozwodnienia z Ratel; ponad −41 % w tygodniu |
| 29 września 2026 | 16,37 USD; kapitalizacja ok. 255–325 mln USD zależnie od liczby akcji (15,6–15,9 mln) |

Krytyka: Breakingviews (19 marca): „wycena 2000-krotności przychodów i historia małych, zmiennych, politycznie powiązanych debiutów"; Bloomberg (20 marca): „najnowsza moda Wall Street"; Seeking Alpha: przed IPO „mało przychodów, wysokie ryzyko", we wrześniu „możliwy krach wyceny"; Benzinga o Ratel: „emisja akcji jako główna waluta transakcji tworzy nawis wyceny". Jedyna rekomendacja „kupuj" pochodzi od gwaranta IPO (Lucid) **[M]**.

### 6.4 Co spółka zrobiła z publiczną walutą

1. **Linia kapitałowa Lucid (czerwiec 2026)**: 24-miesięczna umowa zakupu akcji; rejestracja odsprzedaży 3 mln akcji; przy założonym kursie 60,32 USD do ok. 181 mln USD; do daty aktualizacji prospektu sprzedano 654 734 akcje za 27,2 mln USD brutto **[Z]**. To tłumaczy, dlaczego gotówka wzrosła z 9,3 do 25,3 mln USD mimo strat ok. 11,8 mln USD w I półroczu i wpływów netto z IPO 14,7 mln USD **[?]**.
2. **Strategia platformy (list Prince'a, 11 czerwca 2026)**: spółka ma „identyfikować, przejmować i skalować firmy obronne o produktach sprawdzonych na polu walki", którym „brakuje kapitału, infrastruktury komercyjnej i zasięgu międzynarodowego" **[Z]**.
3. **Ratel Robotics (10 września 2026)**: do 224 mln USD, z czego gotówka przy zamknięciu tylko ok. 7,2 mln USD; reszta w akcjach i earn-outach do 2028 r. **[Z]/[M]**. Przy przychodach 216 tys. USD za kwartał akcje są jedyną realną walutą.
4. **Vectus (sierpień 2026)**: 20 % udziału w spółce Prince'a; transakcja z podmiotem powiązanym przewodniczącego rady **[Z]**.

---

## 7. Wzrost w liczbach

| Miara | 2024 | 2025 | I kw. 2026 | II kw. 2026 | Wiar. |
|---|---|---|---|---|---|
| Przychody | 329 410 USD | 309 920 USD (−5,9 %) | 20 325 USD | 216 413 USD | [Z] |
| Strata netto | b.d. | 8,5 mln USD | 4,46 mln USD | 7,3 mln USD | [Z] |
| Koszty operacyjne | b.d. | b.d. | 4,5 mln USD (w tym koszty IPO) | 7,5 mln USD (rok wcześniej 0,85 mln) | [Z] |
| Gotówka na koniec okresu | b.d. | 9,3 mln USD | 23,5 mln USD | 25,3 mln USD | [Z] |
| Misje bojowe (narastająco) | start w kwietniu | 70 tys. (wrzesień) → 82 tys. (październik) | ponad 100 tys. | ponad 100 tys. | [M]/[Z] |
| Zespół | b.d. | b.d. | 62 (IPO) | 74 (26 lipca) | [Z] |
| Backlog | — | — | — | 16,3 mln USD umów + 16,8 mln USD MoU = 33,1 mln USD | [Z] |
| Klienci | 1 (Smart Machinery Solutions) | 1 | wygaszanie | Meta Bureau (SkyKnight), Progress TRW (Czechy) | [Z] |

Trzy obserwacje **[?]**:

- Przychód na misję był pomijalny: ok. 0,3 mln USD rocznie przy dziesiątkach tysięcy misji oznacza, że wdrożenie w Ukrainie było de facto pilotażem u jednego producenta; monetyzacja przesunęła się na kontrakty po IPO i na klientów z NATO.
- Kontrakt SkyKnight daje punkt odniesienia dla cennika: 2,86 mln USD za ponad 16 tys. licencji to ok. 180 USD na dron jednorazowego użytku; z opcjami do 14,2 mln USD. Fink na wynikach za II kw.: ponad 20 producentów w Ukrainie wysyła większe wolumeny niż SkyKnight **[Z]**.
- Zespół 62–74 osoby przy kosztach operacyjnych 7,5 mln USD kwartalnie oznacza, że po IPO koszty rosną szybciej niż przychody; przejęcie Ratel zmienia spółkę z softwarowej (74 osoby) w produkcyjną (ok. 500 osób).

---

## 8. Struktura właścicielska, kontrola i ład korporacyjny

- **Holding**: Swarmer, Inc. (Delaware) jako emitent, licencjodawca i najpewniej właściciel IP (nie znaleziono zapisu wprost) **[?]**; Autonomous Robotics Systems LLC w Kijowie (B+R), Swarmer Estonia OÜ (strona kontraktu SkyKnight, umowy z HIMERA), biuro w Warszawie **[Z]/[M]**. Wniosek: działalność kontraktowa dla klientów z NATO jest prowadzona przez spółkę w UE, co omija ukraińskie ograniczenia eksportowe i walutowe, o których pisze Kyiv Independent **[?]**.
- **Rada**: Erik Prince (przewodniczący bez funkcji wykonawczych od grudnia 2025 r.), Kupriienko (dyrektor do 2029 r.), Fink (CEO i prezes), Philip Wagenheim (4,99 %); CFO Brooks Ensign **[Z]/[M]**. Prasa opisuje kontrowersje wokół powiązań politycznych Prince'a **[M]**.
- **Zmiana CEO**: Kupriienko ustąpił 26 lipca 2026 r. (bez podania przyczyny w komunikacie), a dwa tygodnie później wykonał opcje na 3 997 762 akcje **[Z]**. Założyciel miał więc opcje, nie tylko akcje objęte vestingiem, a jego odejście nie uruchomiło żadnego mechanizmu odkupu; przeciwnie, zwiększyło jego pakiet.
- **Ryzyka ujawnione w S-1**: pracownicy i kontraktorzy w Ukrainie podlegają poborowi; wojna może zakłócić telekomunikację i banki; spółka podlega amerykańskim i zagranicznym kontrolom eksportu i sankcjom; klauzule prawa Delaware utrudniają przejęcie **[Z]**. W streszczeniach nie ma zapisów o ukraińskich ograniczeniach walutowych, CFIUS ani ITAR **[?]**.
- **Ograniczenia eksportowe po stronie USA**: na SCSP AI+ Expo (maj 2026) ukraińscy menedżerowie, w tym ze Swarmera, mówili, że licencje na wysyłkę technologii opracowanej w USA do Ukrainy trwają do czterech miesięcy **[M]**.

---

## 9. Ocena: co zadziałało, co nie

**Zadziałało**

1. Produkt sprawdzony w boju jako jedyny argument sprzedażowy i inwestycyjny: 100 tys. misji przekonało VC i rynek mimo braku przychodów.
2. Struktura Delaware plus spółki w UE od pierwszego dnia: inwestorzy z USA, kontrakty z NATO przez Estonię, bez późniejszego „flipu".
3. Szybkość: 16 miesięcy od założenia do seedu, 12 do serii A, 6 do IPO.
4. Wykorzystanie „popu": linia kapitałowa spieniężyła zawyżony kurs (27 mln USD), a akcje stały się walutą przejęć.

**Nie zadziałało albo kosztowało**

1. Koncentracja: jeden klient przez dwa lata, potem jego wygaszenie; pierwszy realny kontrakt dopiero po IPO.
2. Mikro-IPO z jednym butikowym gwarantem: cienki free float, zmienność rzędu 30 % dziennie, wycena oderwana od przychodów, krytyka o „politycznie powiązanym debiucie".
3. Ład: przewodniczący z 80 % udziałem w spółce, w której emitent ma 20 % (Vectus); zmiana strategii cztery miesiące po debiucie; odejście założyciela-CEO bez ujawnionej przyczyny.
4. Rozwodnienie: linia kapitałowa, wykonanie opcji założyciela (ok. 4 mln akcji przy ok. 12 mln po IPO), Ratel w akcjach; lock-up zakończony spadkiem o ponad 40 % w tydzień.
5. Pieniądze bezzwrotne praktycznie nieobecne (50 tys. USD); ukraiński ekosystem nie oferował odpowiednika EIC, DIANA ani Ścieżki SMART.

---

## 10. Wnioski dla Basiliska: mapowanie na projekt umowy

Oznaczenia stanu jak w `vc.md` sekcja 8: **OK** — umowa to przewiduje; **CZ** — częściowo, do doprecyzowania; **BRAK** — nie ma, dodać; **KOL** — koliduje, do negocjacji albo decyzji; dodatkowo **DEC** — wymaga decyzji Założycieli.

| Lekcja ze Swarmera | Gdzie u nas | Stan | Co zrobić i kiedy |
|---|---|---|---|
| **Spółka-matka w USA daje dostęp do kapitału i Nasdaq, ale oddaje kontrolę poza UE.** Kryterium § 11 dopuszcza kontrolę z USA (NATO), lecz art. 9 EDF wyklucza firmę kontrolowaną przez podmiot z państwa niestowarzyszonego; to samo AGILE i EUDIS | § 11 ust. 6; `regulations.md` sekcje 3 i 3a; `psa_todo.md` sekcja 1 (pytanie o jurysdykcję) | DEC | Traktować „drogę Swarmera" (matka w USA) i „drogę EDF" jako wykluczające się. Jeżeli kapitał z USA, to przez spółkę zależną w USA dla kontraktów amerykańskich (wzór: ICEYE US), nie przez matkę. Rozstrzygnąć przed uchwałą kierunkową z § 32 ust. 2 **[W]** |
| **P.S.A. nie może być notowana**: art. 300³⁶ § 2 KSH zakazuje dopuszczenia i wprowadzenia jej akcji do obrotu zorganizowanego, czyli także na NewConnect **[Z]/[W]** | § 25 ust. 1 lit. e (przekształcenie: 75 % wszystkich głosów); `vc.md` sekcja 8, wiersz „Exit" (BRAK) | BRAK | W umowie akcjonariuszy zapisać ścieżkę giełdową: przekształcenie w S.A. (art. 551 KSH **[W]**), zobowiązanie do głosowania, harmonogram 12–18 miesięcy, które ograniczenia (§ 10–16, Kryterium) wygasają, a które przechodzą do umowy akcjonariuszy. Do rozmowy z kancelarią na etapie C |
| **Ograniczenia obrotu nie przeżyją giełdy**: zgoda Spółki na zbycie, prawo pierwszeństwa, Kryterium przy każdym nabyciu, obowiązki związane z akcją w rejestrze | § 10 ust. 14, § 11, § 12, § 14 | KOL | Świadomie: te mechanizmy są na fazę prywatną; po debiucie zdematerializowane akcje w KDPW nie niosą obowiązków z rejestru P.S.A. Zapisać w umowie akcjonariuszy, co zastępuje Kryterium po debiucie (lock-up, zobowiązania wobec MON, statut S.A.) **[W]** |
| **SAFE z kilkoma capami zamieniają się na kilka podserii uprzywilejowanych po różnych cenach** | § 31 ust. 4 (instrument zamienny jako Sprawa Zastrzeżona 75 %); konwersja jako emisja z pozbawieniem prawa poboru 4/5 (§ 25 ust. 2); `emisja/inwestor.md` sekcja 4 | CZ | Jeżeli pre-seed na SAFE: jedna uchwała 75 % dla wszystkich SAFE, jednolity cap albo z góry policzone ceny konwersji, oświadczenia z § 11 ust. 8 w treści SAFE; konwersję zaplanować jako jedną emisję z kilkoma cenami emisyjnymi **[W]** |
| **Nieprzejrzysty wehikuł jako największy akcjonariusz** (Theseus Capital Partners LLC, 22 %, nigdy nienazwany) | § 11 ust. 4 i ust. 6 lit. b (beneficjenci rzeczywiści), ust. 8–10 (dokumenty, wstrzymanie transakcji), przekreślony ust. 14 | KOL | Utrzymać wymóg ujawnienia beneficjentów rzeczywistych przed emisją; przywrócić ust. 14 w brzmieniu z `vc.md` sekcja 9 pkt 1; wehikuł jednego inwestora bez ujawnienia beneficjentów nie przechodzi weryfikacji |
| **Odejście założyciela-CEO po 38 miesiącach i wykonanie opcji na 4 mln akcji** | § 10 ust. 2 (48 miesięcy, klif 12), ust. 5 i 8 (Odejście Dobrowolne: akcje nienabyte po cenie emisyjnej), ust. 10 (double trigger) | OK | Umowa jest surowsza niż praktyka Swarmera. W umowie akcjonariuszy dopisać, że vesting przeżywa przekształcenie i IPO, z zamianą obowiązku związanego z akcją na zobowiązanie umowne **[W]** |
| **Przewodniczący rady z własną spółką, w której emitent bierze 20 %** (Vectus), i zmiana strategii cztery miesiące po IPO | § 21 ust. 3 (Kryterium wobec dyrektora), § 23 ust. 2 (głos dyrektora ds. zgodności), § 25 ust. 1 lit. h (zmiana strategii: 75 %), § 29 ust. 4–13 i § 30 (transakcje z podmiotami powiązanymi) | OK | Bez zmian; przy rundzie nie oddawać § 25 lit. h ani § 29–30 (`vc.md` sekcja 9, „czego nie oddawać") |
| **Lock-up 180 dni na 59 % kapitału i −41 % po jego wygaśnięciu** | § 13 (12 miesięcy od wpisu; inny cel); `vc.md` sekcja 8, wiersz „Lock-up" (CZ) | CZ | Lock-up giełdowy negocjuje się z gwarantem; w umowie akcjonariuszy zobowiązanie Założycieli do zwyczajowego lock-upu (180–360 dni) i do skoordynowanej sprzedaży po nim **[W]** |
| **Model B2B2G: licencje dla producentów, przychód dopiero z kontraktów wolumenowych** (16 tys. licencji za 2,86 mln USD) | § 33 ust. 3 (licencja niewyłączna, ograniczona zakresem, wypowiadalna przy zmianie kontroli), § 28 (eksport), § 23 ust. 1 lit. h | OK | We wzorze umowy spółki celowej (etap C pkt 25 w `plan_prac.md`) dodać licencję liczoną „na platformę" z raportowaniem wolumenów i audytem; w data room pokazać koncentrację klientów jako ryzyko znane i zarządzane |
| **Kontraktowanie z klientami z NATO przez spółkę w UE** (Swarmer Estonia OÜ) | `regulations.md` sekcje 2.2 i 4 (bramki G2, G5), § 28 | OK | Basilisk jest w UE od początku; odpowiednikiem problemu Swarmera jest eksport do UK i USA (EU001, rejestracja w MRiT przed pierwszym transferem) |
| **Pieniądze bezzwrotne nie zastąpiły klienta**: 50 tys. USD grantu, 0,3 mln USD przychodu, potem giełda | § 31 ust. 1 (katalog: zaliczki, zamówienia, programy B+R); `psa_todo.md` sekcja 6 (EIC, SMART, DIANA) | CZ | Granty planować jako obniżenie rozwodnienia w fazie TRL 4–6, nie jako model przychodowy; pierwszy płatny pilot z producentem (odpowiednik SkyKnight) przed rundą A |
| **Próg Kwalifikowanej Rundy 2 mln zł jest na poziomie seedu Swarmera**; wycena serii A ≈ 66 mln USD przy 0,3 mln USD przychodów | § 32 ust. 1 (pola do uzupełnienia) | CZ | Uzupełnić próg kwotowy i próg wyceny (D9 w `plan_prac.md`); nie kopiować wycen z 2026 r., bo rynek defense tech jest w „hype cycle" (określenie CEO Andurila) |
| **Spółka-matka zarejestrowana od pierwszego dnia, bez późniejszego flipu** | § 1–2; `psa_todo.md` sekcja 1 | DEC | Jeżeli struktura holdingowa ma powstać, to przed pierwszą rundą; przekształcenie transgraniczne po rundzie kosztuje (podatek od niezrealizowanych zysków, ciągłość programu motywacyjnego, ponowna weryfikacja Kryterium) |

Czego Swarmer nie rozstrzyga, a co Basilisk musi wiedzieć przed rundą: polskie odpowiedniki mikro-IPO to NewConnect i rynek główny GPW, oba dostępne dopiero po przekształceniu w S.A.; w 2022–2023 r. tą drogą poszły polskie spółki kosmiczne Creotech Instruments (rynek główny) i Scanway (NewConnect) **[W]**, a w 2026 r. IPO na GPW przygotowuje WB Electronics (`case_studies/wb_electronics.md`). Fundusze obronne (NIF, Expeditions, Balnord) i EIC Fund są w 2026–2027 r. realniejszymi partnerami niż rynek publiczny (`vc.md` sekcje 6 i 11).

---

## 11. Luki i rzeczy do sprawdzenia

- Tożsamość i beneficjenci rzeczywiści Theseus Capital Partners LLC; czy Broadband Capital inwestował przez ten wehikuł.
- Gdzie formalnie jest IP (Delaware czy Kijów) i jak wniesiono udziały ukraińskie do spółki-matki (data, wycena).
- Dokładne udziały Kupriienki, Finka i Prince'a z tabeli własności w 424B4; liczba akcji po IPO; treść lock-upu; tabela wykorzystania wpływów.
- Przyczyna rezygnacji Kupriienki; kim są sprzedający w rejestracji odsprzedaży 3 mln akcji.
- Rozbieżność między sumą konwersji SAFE (ok. 1,7 mln USD) a ogłoszonym seedem 2,7 mln USD; czy „UA1 VC" naprawdę uczestniczył w serii A (podaje tylko DroneXL).
- Nagłówek Yahoo o „wsparciu Rakutena w Japonii" i wzmianka o Rakutenie jako dystrybutorze: niepotwierdzone.
- Karta projektu EDF „SWARMER" (EDF-2024, nr 101224078) to niezwiązany akronim projektu, nie spółka; nie mylić.
- Ukraińskie ograniczenia eksportowe i walutowe dla spółki kijowskiej, status ITAR, CFIUS: brak w dostępnych streszczeniach S-1; przeczytać pełny tekst czynników ryzyka (akcesje 0001104659-26-009198 i 0001104659-26-072392).

---

## 12. Źródła sprawdzone 30 września 2026 r.

**Dokumenty SEC (CIK 2092574)**
- Prospekt 424B4, 17 marca 2026 — https://www.sec.gov/Archives/edgar/data/2092574/000110465926029590/tm2529424-12_424b4.htm
- S-1, 2 lutego 2026 — https://www.sec.gov/Archives/edgar/data/2092574/000110465926009198/tm2529424-6_s1.htm
- S-1 odsprzedaży (linia Lucid), czerwiec 2026 — https://www.sec.gov/Archives/edgar/data/2092574/000110465926072392/tmb-20260331xs1.htm ; 424B3 — https://www.sec.gov/Archives/edgar/data/0002092574/000110465926073813/tm2613900-5_424b3.htm
- 10-Q za I kw. 2026 — https://www.sec.gov/Archives/edgar/data/0002092574/000119312526222174/swmr-20260331.htm ; 10-Q za II kw. 2026 — https://www.sec.gov/Archives/edgar/data/0002092574/000119312526352312/swmr-20260630.htm
- 8-K z 19 sierpnia 2026 (wykonanie opcji) — https://www.sec.gov/Archives/edgar/data/2092574/000119312526356907/swmr-20260819.htm ; załączniki 8-K o zamknięciu IPO — https://www.sec.gov/Archives/edgar/data/2092574/000110465926031244/tm2529424d17_ex99-1.htm
- DRS/A — https://www.sec.gov/Archives/edgar/data/2092574/000110465926003363/filename1.htm

**Komunikaty spółki i inwestorów**
- Seria A, Business Wire, 16 września 2025 — https://www.businesswire.com/news/home/20250916602085/en/Swarmer-Ukraines-Leading-Drone-Autonomy-and-Swarming-Company-Announces-$15m-Series-A-Led-By-US-Investors
- Publiczne złożenie S-1, 2 lutego 2026 — https://www.businesswire.com/news/home/20260202054211/en/Swarmer-Announces-Public-Filing-of-Registration-Statement-for-Initial-Public-Offering
- Cena IPO, 16 marca 2026 — https://www.morningstar.com/news/business-wire/20260316719643/swarmer-announces-pricing-of-initial-public-offering
- Zamknięcie IPO, 18 marca 2026 — https://www.businesswire.com/news/home/20260318195296/en/Swarmer-Announces-Closing-of-Initial-Public-Offering-of-Common-Stock-and-Full-Exercise-of-Underwriters-Option-to-Purchase-Additional-Shares
- Kontrakt SkyKnight, 13 maja 2026 — https://www.globenewswire.com/news-release/2026/05/13/3293908/0/en/Swarmer-Awarded-2-86M-Contract-to-Outfit-SkyKnight-Drones-With-Swarming-Software.html ; rozszerzenie, 29 czerwca 2026 — https://www.nasdaq.com/press-release/swarmer-adds-additional-1m-revenue-skyknight-contract-update-expands-swarming
- List przewodniczącego, 11 czerwca 2026 — https://www.globenewswire.com/news-release/2026/06/11/3310349/0/en/Swarmer-Publishes-Letter-From-Its-Chairman-Erik-Prince-Outlining-Strategy.html
- Wyniki I kw. 2026, 13 maja 2026 — https://www.nasdaq.com/press-release/swarmer-reports-first-quarter-financial-results-2026-05-13 ; wyniki II kw. 2026, 13 sierpnia 2026 — https://www.globenewswire.com/news-release/2026/08/13/3344900/0/en/swarmer-reports-second-quarter-2026-financial-results-and-provides-business-update.html
- Transkrypcja konferencji wynikowej za II kw. 2026 — https://www.fool.com/earnings/call-transcripts/2026/08/20/swarmer-swmr-q2-2026-earnings-call-transcript/
- HIMERA, 29 kwietnia 2026 — https://www.globenewswire.com/news-release/2026/04/29/3284231/0/en/Swarmer-and-HIMERA-Partner-to-Integrate-Resilient-Communications-into-Advanced-Autonomous-Systems.html ; konsorcjum interceptorów, 12 maja 2026 — https://www.globenewswire.com/news-release/2026/05/12/3292799/0/en/Swarmer-to-Lead-Development-of-a-Deployable-Drone-Interceptor-System.html ; Brightline, 27 lipca 2026 — https://www.globenewswire.com/news-release/2026/07/27/3333479/0/en/Swarmer-and-Brightline-Partner-on-AI-Data-Collection-and-Drone-Interoperability-for-U-S-Department-of-War.html ; Lantronix, 30 lipca 2026 — https://www.lantronix.com/newsroom/press-releases/lantronix-and-swarmer-collaborate-to-create-custom-compute-module-for-group-1-unmanned-aerial-systems/
- Vectus, 21 sierpnia 2026 — https://www.globenewswire.com/news-release/2026/08/21/3348957/0/en/erik-prince-and-swarmer-announce-formation-of-vectus-air-defense-systems.html
- Ratel Robotics, 10 września 2026 — https://www.globenewswire.com/news-release/2026/09/10/3359272/0/en/swarmer-enters-into-definitive-agreement-to-acquire-ratel-robotics-a-leading-ukrainian-unmanned-ground-vehicle-manufacturer-for-up-to-224-million.html
- Zmiana CEO (8-K w streszczeniu) — https://www.tradingview.com/news/tradingview:9ef73fd513caa:0-serhii-kupriienko-resigns-as-global-ceo-of-swarmer-alexander-fink-remains-principal-executive-officer/

**Prasa i bazy**
- AIN.ua: D3, 16 listopada 2023 — https://en.ain.ua/2023/11/16/ukrainian-swarmer-secures-funding-from-d3/ ; Brave1, 27 sierpnia 2024 — https://en.ain.ua/2024/08/27/ukrainian-drone-startup-swarmer-secures-nearly-50k-grant-from-brave1/ ; seed, 16 września 2024 — https://en.ain.ua/2024/09/16/ukrainian-startup-swarmer-closes-27m-seed-round-to-develop-coordinated-swarm-drones/ ; seria A, 16 września 2025 — https://en.ain.ua/2025/09/16/swarmer-raised-15m/ ; syndykat Oppenheimer, 5 listopada 2025 — https://en.ain.ua/2025/11/05/swarmer-raises-investment-from-the-new-oppenheimer-fund-syndicate/ ; S-1, 2 lutego 2026 — https://en.ain.ua/2026/02/02/swarmer-and-ipo/ ; sektor 2025 — https://en.ain.ua/2025/12/24/major-investments-in-ukrainian-companies-in-2025/
- Forbes Ukraine: blitz-wywiad z szacunkiem wyceny, 17 września 2025 — https://forbes.ua/innovations/piloti-boyatsya-stati-ne-potribnimi-rozrobnik-roiv-droniv-swarmer-zaluchiv-rekordni-15-mln-kudi-spryamuyut-investitsii-i-yak-zminyuetsya-vikoristannya-bpla-na-fronti-blitsintervyu-17092025-32661 ; IPO, 17 marca 2026 — https://forbes.ua/news/ukrainskiy-defense-tech-startap-swarmer-proviv-ipo-tsina-za-aktsiyu-na-starti-torgiv-zrosla-na-175-17032026-37198
- Kyiv Independent, „Broke a barrier" — https://kyivindependent.com/ukrainian-defense-tech-finally-makes-its-way-to-u-s-markets/ ; seria A — https://kyivindependent.com/ukrainian-swarm-drone-ai-startup-secures-15-million-investment/
- Reuters Breakingviews, 19 marca 2026 — https://www.breakingviews.com/columns/considered-view/soaring-drone-ipo-is-likely-fly-off-course-2026-03-19/ ; Bloomberg, 20 marca 2026 — https://www.bloomberg.com/news/articles/2026-03-20/drone-tech-maker-s-1-000-surge-shows-latest-wall-street-fad
- Venture Capital Journal, 18 marca 2026 — https://www.venturecapitaljournal.com/uk-family-office-vcs-cash-in-on-swarmers-moonshot-ipo/
- DroneXL, 13 października 2025 — https://dronexl.co/2025/10/13/ukrainian-drone-swarm-startup-swarmer/ ; 20 marca 2026 — https://dronexl.co/2026/03/20/swarmers-ipo-ukraine-drone-swarm-software/ ; 10 września 2026 — https://dronexl.co/2026/09/10/erik-prince-swarmer-buys-ratel-robotics-224m/
- Resilience Media, „The Perfect Swarm" — https://resiliencemedia.co/the-perfect-swarm-how-swarmer-got-its-timing-just-right-by-accident-and-saw-its-us-ipo-pop/
- Defense One, wrzesień 2025 — https://www.defenseone.com/business/2025/09/ukrainian-startup-has-re-invented-drone-swarming/408099/ ; maj 2026 (licencje eksportowe) — https://www.defenseone.com/technology/2026/05/us-investors-warm-ukrainian-defense-startups-export-laws-slow-cooperation/413446/
- Axios, 16 września 2026 — https://www.axios.com/2026/09/16/swarmer-ratel-drones-erik-prince ; Benzinga, 15 września 2026 — https://www.benzinga.com/trading-ideas/movers/26/09/61797326/swarmer-stock-plunges-tuesday-whats-driving-the-action ; MarketBeat (lock-up) — https://www.marketbeat.com/instant-alerts/lockup-swarmer-incs-lock-up-period-to-expire-on-september-14th-nasdaq-swmr-2026-09-07/ ; Simply Wall St (linia kapitałowa) — https://simplywall.st/stocks/us/capital-goods/nasdaq-swmr/swarmer/news/swarmer-swmr-is-down-289-after-new-lucid-equity-line-and-def
- Notowania: Investing.com — https://www.investing.com/equities/swarmer-inc ; StockAnalysis — https://stockanalysis.com/stocks/swmr/ ; TipRanks (struktura własności) — https://www.tipranks.com/stocks/swmr/ownership
- The Robot Report (struktura spółek) — https://www.therobotreport.com/swarmer-to-acquire-ukrainian-ugv-maker-ratel-robotics-for-up-to-224m/ ; The Air Current (profil) — https://theaircurrent.com/ukraine-special-report/company-profile-swarmer/
- Kontekst sektorowy: TechCrunch, 8 lipca 2025 — https://techcrunch.com/2025/07/08/european-vc-breaks-taboo-by-investing-in-pure-defense-tech-from-ukraines-war-zones/ ; Crunchbase News (kandydaci do IPO) — https://news.crunchbase.com/public/potential-defense-tech-ipo-candidates-swmr/ ; CNBC o Andurilu, 9 lipca 2026 — https://www.cnbc.com/2026/07/09/anduril-ceo-ipo-defense.html
- Art. 300³⁶ KSH — https://lexlege.pl/ksh/art-300-36/ ; https://arslege.pl/rozporzadzanie-akcjami-prostej-spolki-akcyjnej/k8/a124131/
- Strony sec.gov, businesswire.com, globenewswire.com, forbes.ua, ain.ua, dou.ua, kyivindependent.com i dronexl.co były w tej sesji niedostępne do pełnego odczytu (blokada sieciowa); tezy oparte na ich streszczeniach z wyszukiwarki oznaczono [Z] tylko tam, gdzie streszczenie dokumentu pierwotnego było jednoznaczne.
