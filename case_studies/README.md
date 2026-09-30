# Case studies: rozwój i finansowanie firm obronnych i dual-use

Dokumenty wewnętrzne Basilisk Systems, informacyjne. Nie są opinią prawną ani rekomendacją inwestycyjną i nie zmieniają umowy spółki. Katalog zawiera trzy studia przypadku firm, które sfinansowały rozwój trzema różnymi drogami, oraz notatkę o rynku obligacji Catalyst jako instrumencie długu. Cel: mieć konkretne, datowane punkty odniesienia dla planu finansowania Basiliska i dla decyzji odłożonych w `psa_todo.md` (sekcja 1: jurysdykcja i struktura; sekcja 6: terminy programów). Odesłania do umowy według `psa.tex` w wersji 0.9.4-C (numery § według `spis_tresci.md`); dokumenty uzupełniają `vc.md` (oczekiwania funduszy) i `regulations.md` (wymogi programów).

Stan na 30 września 2026 r.

---

## 1. Pliki

| Plik | Firma / temat | Droga finansowania | Co pokazuje |
|---|---|---|---|
| `swarmer.md` | Swarmer (Ukraina / USA, oprogramowanie rojów dronów, zał. 2023) | środki własne → akcelerator → SAFE → seria A z USA → mikro-IPO na Nasdaq po 34 miesiącach | najszybsza droga na giełdę, cena publicznej waluty, struktura holdingowa w USA, ład po IPO |
| `wb_electronics.md` | WB Electronics / Grupa WB (Polska, bezzałogowce i łączność, zał. 1997) | zamówienia MON → licencje i eksport → obligacje na przejęcia → jedna runda z PFR → IPO na GPW rozważane od 2015 r. i wciąż nieprzesądzone | wzrost bez giełdy i bez oddania kontroli, inwestor państwowy jako mniejszość, dług pod zastaw spółki zależnej |
| `iceye.md` | ICEYE (Finlandia / Polska, satelity SAR, zał. 2014) | granty uczelniane i unijne → VC z USA → państwo fińskie i koncerny → kontrakty rządowe → growth equity przy 10,5 mld EUR | drabina finansowania firmy kapitałochłonnej w UE, państwo jako inwestor i klient, JV z koncernem, płynność przez odsprzedaż zamiast IPO |
| `catalyst.md` | rynek obligacji GPW Catalyst | dług publiczny dla firm z przepływami | jak czytać notowania obligacji, wymogi ASO, koszty, marże, co może P.S.A. |
| `anduril.md` | Anduril (USA, neo-prime: Lattice i sprzęt, zał. 2017) | seed Founders Fund → klient cywilny (CBP) → OTA i prototypy → 9 rund do 61 mld USD → programy of record; IPO „za kilka lat" | sekwencja software → sprzęt przez przejęcia → produkcja lokalna u sojusznika; cena: 1 mld USD straty rocznie |
| `shield_ai.md` | Shield AI (USA, autonomia Hivemind i V-BAT, zał. 2015) | kontrakt DIU → a16z → SBIR → przejęcie płatowca → 17 rund do 12,7 mld USD z PE i kapitałem uprzywilejowanym | autonomia kupiona przez USAF jako osobna pozycja (A-GRA); licencje dla suwerennych OEM; koszt posiadania sprzętu |
| `helsing.md` | Helsing (Niemcy, AI obronne i drony, zał. 2021) | 100 mln EUR od jednego inwestora przed kontraktem → GC → 18 mld USD; zamówienia Bundeswehry i Ukrainy | AI wewnątrz platform primów (Saab, Airbus), „suwerenność europejska" jako produkt, spór o HX-2 |
| `destinus.md` | Destinus (Szwajcaria → Holandia, drony i pociski, zał. 2021) | seed → instrumenty zamienne i pożyczki wspólników → Commerzbank → pre-IPO przy 5 mld EUR | siedziba holdingu idzie za prawem eksportowym; JV 49/51 z Rheinmetallem; zakup AI (Daedalean) |
| `tekever.md` | Tekever (Portugalia / UK, drony AR3 i AR5, zał. 2001) | 23 lata bez rundy → 70 mln EUR (NIF, NSSIF) → jednorożec → 580 mln USD przy 6,4 mld USD | spółka w kraju klienta (UK 2013) ważniejsza niż runda; rynek macierzysty jako referencja |
| `milrem.md` | Milrem Robotics (Estonia, roboty lądowe, zał. 2013) | serwis dla MO → EDIDP i EDF (koordynator) → KMW 24,9 % → sprzedaż kontroli EDGE (ZEA) | inwestor strategiczny zamiast VC; art. 9 EDF po przejęciu spoza UE i gwarancje państwa; eksport finansowany przez darczyńców |
| `creotech.md` | Creotech Instruments (Polska, satelity, zał. 2012) | oszczędności → ARP → NCBR, ESA, PARP → NewConnect → GPW → 6 emisji do 2,8 mld zł; MON jako przegięcie | jedyna polska droga giełdowa deep techu; drabina grantów; rozwodnienie założycieli do 6–7 % |
| `aps.md` | Advanced Protection Systems (Polska, antydron, zał. 2015) | NCBR → eksport (Ukraina przez UK) → dwa nieudane IPO → PE mniejszość → 450–600 mln zł gwarancji pod SAN → proces sprzedaży | MON przychodzi po sojusznikach; prospekt to nie szybka droga; zegar funduszu PE |
| `figure_ai.md` | Figure AI (USA, humanoidy, zał. 2022) | 100 mln USD od założyciela → 39 mld USD w 3 lata; zero grantów i zamówień rządowych | koszt fizycznego AI pełnego stosu (1–2 mld USD); własność modelu i danych; pozew o bezpieczeństwo |
| `nomagic.md` | Nomagic (Polska / USA, roboty magazynowe z AI, zał. 2017) | Khosla → flip do USA po 20 miesiącach → EBI dług → EBOR seria B → klient-inwestor (Zalando) | polska substancja pod amerykańską matką; banki rozwoju jako pomost serii B; 8 lat do dwucyfrowej floty |
| `conclusions.md` | synteza trzynastu case studies | siedem archetypów finansowania i rekomendacje | co Basilisk kopiuje, czego unika, jakie decyzje podjąć przed rundą A |

Druga seria (gałąź `vc2`) dodaje dziesięć firm: defence tech z USA i Europy (Anduril, Shield AI, Helsing, Destinus, Tekever, Milrem), z Polski (Creotech, APS) oraz robotykę i fizyczne AI (Figure AI, Nomagic). Syntezę wszystkich trzynastu przypadków i rekomendacje dla Basiliska zawiera `conclusions.md`; profile jurysdykcji są w `jurisdictions/` (Portugalia dodana z powodu Tekevera).

Każdy case study ma tę samą strukturę: 1 główny wniosek, 2 profil, 3 jak zaczęli (kapitał początkowy i pierwsze lata), 4 oś czasu, 5 finansowanie runda po rundzie, 6 giełda, 7 wzrost w liczbach, 8 struktura właścicielska i ład, 9 ocena, 10 wnioski dla Basiliska z mapowaniem na § umowy, 11 luki, 12 źródła.

Oznaczenia wiarygodności we wszystkich plikach: **[Z]** — fakt z dokumentu pierwotnego (sprawozdanie SEC, raport EBI/ESPI, komunikat spółki, inwestora, uczelni albo zamawiającego); **[M]** — doniesienie prasowe albo baza danych; **[W]** — wiedza ogólna o prawie albo praktyce rynkowej, do potwierdzenia u kancelarii; **[?]** — szacunek, w tym własne obliczenie z cytowanych liczb, albo teza niepotwierdzona. Uwaga metodyczna: w sesji, w której powstały te pliki, strony źródłowe były niedostępne do pełnego odczytu (blokada sieciowa), więc fakty pochodzą ze streszczeń wyszukiwarki, a **[Z]** przyznano tylko tam, gdzie streszczenie dokumentu pierwotnego było jednoznaczne. Przed użyciem liczb poza firmą trzeba je sprawdzić w podlinkowanych dokumentach.

---

## 2. Porównanie

| Element | Swarmer | WB Electronics | ICEYE |
|---|---|---|---|
| Założenie | maj 2023 r.; Swarmer, Inc. (Delaware), centrala Austin; spółki w Ukrainie, Estonii, Polsce | 1997 r., Ożarów Mazowiecki; S.A. od 2010 r.; ponad 20 spółek, w tym w Ukrainie, USA, Indiach, Malezji | 2014 r. (projekt od 2012 r.), Espoo; spółki w Polsce, USA, Grecji, Holandii; JV w Niemczech |
| Produkt i model | oprogramowanie autonomii i dowodzenia rojem; licencje B2B2G dla producentów dronów | bezzałogowce, amunicja krążąca, łączność i dowodzenie; producent i integrator dla MON i na eksport | mikrosatelity SAR; dane i analityka; od 2020 r. sprzedaż całych systemów państwom |
| Kapitał początkowy | ok. 70 tys. USD założycieli; akcelerator D3 (SAFE, ok. 125 tys. USD); grant Brave1 ok. 50 tys. USD | środki założycieli (kwota nieznana); od 1998 r. zamówienie MON na TOPAZ; od 2001 r. eksport FONET; 2009 r. licencja dla Harrisa | grant uczelni 50 tys. EUR i budżet projektu 0,5 mln EUR; Tekes TUTLI; 2015 r.: 2,5 mln EUR VC + 1,7 mln EUR pożyczki Tekes + 2,4 mln EUR grantu H2020 |
| Kapitał własny od inwestorów | ok. 18,5 mln USD prywatnie; 17,25 mln USD z IPO; ok. 27 mln USD z linii kapitałowej po IPO | 128 mln zł (PFR, 2017 r.) — jedyna emisja | ok. 1,13–1,2 mld USD kapitału pierwotnego w ośmiu rundach; ok. 600 mln EUR odsprzedaży w 2025–2026 r. |
| Pieniądze bezzwrotne i pożyczki państwowe | ok. 50 tys. USD | nie znaleziono dotacji; prace rozwojowe zamawiane przez MON (Gladius 2: 49,9 mln zł) | ok. 83 mln EUR (Tekes, Business Finland, H2020), w tym ok. 36 mln EUR grantów |
| Dług | brak (linia kapitałowa to emisja akcji) | obligacje 80 (2014), 80 (2017), 60 (2020), 100 mln zł (2023), zabezpieczone na akcjach Radmoru; dziś dług minimalny | pożyczki Business Finland; część rozszerzenia z grudnia 2024 r. (65 mln USD dług i kapitał) |
| Inwestor państwowy | brak | PFR FIZAN: 24 % nowych akcji (2017 r.), dziś 26,44 %, „nie planuje pełnego wyjścia" | Tesi (od 2018 r.), Solidium (od 2024 r., miejsce w radzie), Vinci/BGK (od 2025 r.); państwo fińskie ok. 12 % po rundzie F |
| Pierwszy kontrakt publiczny | brak bezpośredniego; licencje przez producentów (SkyKnight 2,86 mln USD, 2026 r.; Czechy 1,41 mln USD) | 1998 r. (TOPAZ dla MON); największe: Gladius 2022 (ok. 2 mld zł), SAFE 2026 (11,66 mld zł netto) | Brazylia 2020 r.; Polska 2025 r. (860 mln zł), Finlandia (158 mln EUR), Niemcy (1,7 mld EUR w JV) |
| Przychody i wynik (ostatni pełny rok) | 2025: 0,31 mln USD; strata 8,5 mln USD | 2025: ok. 2,9 mld zł; zysk netto 679 mln zł | 2025: ponad 250 mln EUR; EBITDA ponad 100 mln EUR |
| Wycena | ok. 60 mln USD przy IPO; szczyt ponad 1 mld USD; ok. 255–325 mln USD 29 września 2026 r. | rozmowy o IPO: „powyżej 20 mld zł"; brak transakcji | 2,4 mld EUR (grudzień 2025 r.) → 10,5 mld EUR (czerwiec 2026 r.) |
| Kontrola założycieli | insiderzy ok. 58 % po IPO; przewodniczący rady Erik Prince; założyciel-CEO odszedł w lipcu 2026 r. | założyciele 73,56 %, zarząd i rada nadzorcza w ich rękach od 29 lat | udziały założycieli nieujawnione; ponad 50 inwestorów; prezes-założyciel nadal kieruje spółką |
| Giełda | Nasdaq Capital Market od 17 marca 2026 r. (SWMR) | akcje nienotowane; obligacje na Catalyst od 2015 r.; IPO na GPW rozważane, bez uchwały WZ | nienotowana; rozmowy o IPO w 2025 r., odłożone; Nasdaq niewykluczony |
| Czas | 34 miesiące od założenia do IPO | 29 lat i IPO wciąż opcją | 12 lat do dekakorna, 11 do rentowności, giełdy nie ma |

---

## 2a. Porównanie drugiej serii: defence tech, robotyka i fizyczne AI

| Element | Anduril | Shield AI | Helsing | Destinus | Tekever | Milrem | Creotech | APS | Figure AI | Nomagic |
|---|---|---|---|---|---|---|---|---|---|---|
| Kraj, forma | USA, Inc. (Kalifornia) | USA, Inc. (San Diego) | Niemcy, GmbH; spółki UK, FR, EE, UA | Szwajcaria → Holandia (B.V.) | Portugalia; Tekever Ltd (UK) od 2013 r. | Estonia, AS | Polska, S.A. (GPW) | Polska, S.A. (prywatna) | USA | Polska sp. z o.o. pod Nomagic Inc. (USA) |
| Kapitał początkowy | seed 17,5 mln USD (Founders Fund, 2017 r.) | kontrakt DIU (2016 r.), seria A 10,5 mln USD (a16z) | 102,5 mln EUR (Prima Materia, 2021 r.) | seed 29 mln USD (2022 r.) | własne środki od 2001 r.; pierwsza runda 2024 r. | serwis dla MO (2013 r.); ok. 6 mln USD do 2023 r. | oszczędności i „kilkaset tysięcy zł"; ARP 2014 r. | grant NCBR (2015 r.) | 100 mln USD od założyciela (2022 r.) | seed 8,6 mln USD (Khosla, 2020 r.) |
| Kapitał łącznie | ok. 11,3 mld USD | ok. 3,5 mld USD | ok. 3 mld EUR | ok. 400 mln EUR (głównie zamienne i dług) | ok. 1,2 mld USD | nieujawnione (EDGE) | ok. 668 mln zł (6 emisji) | nieujawnione (EI) + 450–600 mln zł gwarancji | ok. 1,9 mld USD | ok. 85 mln USD + dług EBI |
| Wycena (ostatnia) | 61 mld USD (maj 2026 r.); rozmowy 100 mld USD | 12,7 mld USD (marzec 2026 r.); rozmowy ≥20 mld USD | 18 mld USD (lipiec 2026 r.) | ponad 5 mld EUR (poszukiwana, maj 2026 r.) | 6,4 mld USD (wrzesień 2026 r.) | nieujawniona | ok. 2,8 mld zł (wrzesień 2026 r.) | nieujawniona (proces sprzedaży) | 39 mld USD (wrzesień 2025 r.) | nieujawniona |
| Przychód (ostatni) | 2,2 mld USD (2025 r.); prognoza 4,3 mld USD | ok. 300 mln USD; prognoza ≥540 mln USD | sprzeczne: 9,6 mln EUR (2023 r.) do 502 mln USD (2026 r.) | prognoza 500 mln EUR (zarząd) | ARR ok. 117 mln USD (agregator) | 46,1 mln EUR (2025 r.) | 167,5 mln zł (2025 r.), pierwszy zysk | 39,3 mln zł (2022 r.); sprzeczne | nieujawniony | nieujawniony (KRS 5,3 mln zł) |
| Pieniądze publiczne | CBP, SOCOM, CCA, Ghost Shark (AUD), IVAS, Armia 20 mld USD | DIU, SBIR, USCG 198 mln USD, Navy 800 mln USD, CCA | Bundeswehra (HX-2 1 mld EUR, EW 258 mln EUR, CFSN 580 mln EUR), Ukraina, UK 350 mln GBP | Holandia (marynarka, 700 Ruta), Hiszpania, Rheinmetall | UK MoD 270 mln GBP + CORVUS 400 mln GBP; Portugalia <10 mln EUR | EDIDP 30,6 mln EUR, EDF 50 mln EUR, Niemcy i Holandia dla Ukrainy, ZEA 100 mln EUR | ARP, NCBR, ESA, PARP SMART, MON 556,7 mln zł (KPO) | NCBR, Wojsko 2022 r., UK dla Ukrainy, SAN (podwykonawca) | brak | EBI, EBOR (brak polskich) |
| Inwestor państwowy / strategiczny | brak państwa; Rheinmetall (partner) | L3Harris, Hanwha (inwestorzy); Blackstone pref. | Saab (inwestor i partner) | Rheinmetall (JV 51/49) | NIF, NSSIF, UC Investments | KMW 24,9 %, EDGE (państwo ZEA) większość | ARP 17,1 % → 7,7 %; OFE, TFI | Enterprise Investors (PE) | brak | EBI, EBOR, Zalando (klient) |
| Kontrola założycieli | rada z założycieli; udział nieujawniony | oddali fotel prezesa (2025 r.) | rada Ek i Enders; ok. 24 % założyciele i pracownicy (model) | założyciel większość | Mendes 25–50 % Tekever Ltd | sprzedana | 15,2 % każdy → 6–7 % | większość (do 2026 r.) | pełna (własny kapitał) | nieujawniona |
| Giełda | IPO „za kilka lat" | brak planu; profil pre-IPO | „bez planów IPO" | IPO w Amsterdamie rozważane | brak | brak | NewConnect 2021 r., GPW 2022 r. | dwa nieudane podejścia | brak | brak |
| Główna lekcja | sekwencja, nie burn | autonomia kupowana osobno (A-GRA) | AI wewnątrz platformy prima | siedziba za prawem eksportowym | spółka w kraju klienta | art. 9 EDF przy exicie poza UE | drabina grantów i giełda w Polsce | MON po sojusznikach; dług pod prime'a | koszt pełnego stosu | flip po amerykańskim seedzie |

Szczegóły i wiarygodność każdej liczby w sekcjach 5–8 plików; przychody Helsinga, Tekevera, Destinusa, Figure i Nomagica są nieujawnione albo sprzeczne i oznaczone [?].

---

## 3. Trzy drogi i ich cena

- **Swarmer: kapitał zamiast klienta.** Inwestorzy i rynek wycenili dane z pola walki, nie sprzedaż; spółka weszła na giełdę z przychodami rzędu 0,3 mln USD i wykorzystała zawyżony kurs jako walutę (linia kapitałowa, przejęcie Ratel). Cena: struktura w USA (poza EDF), zmienność kursu, ład podporządkowany przewodniczącemu rady, odejście założyciela-CEO, rozwodnienie. Wniosek dla Basiliska: droga możliwa tylko po rezygnacji z programów UE i po przekształceniu P.S.A. w S.A.; w Polsce jej odpowiednikiem byłby NewConnect albo rynek główny GPW.
- **WB: klient zamiast kapitału.** Dwadzieścia lat wzrostu z zamówień MON, licencji i eksportu, potem dług na przejęcia i jedna runda z PFR jako mniejszością. Cena: 20 lat do 300 mln zł przychodów, zależność od kalendarza zamówień publicznych, inwestor państwowy z mniejszością blokującą, brak płynności dla właścicieli do dziś. Wniosek: model najbliższy polskim realiom Basiliska, ale wymaga pierwszego płacącego zamawiającego na etapie B+R (WB: przetarg z 1998 r., którego nikt inny nie chciał).
- **ICEYE: drabina, na której każdy szczebel ma innego inwestora.** Granty na prototyp, VC na starty, państwo i koncerny jako kapitał cierpliwy, kontrakty rządowe jako przegięcie, growth equity po rentowności; płynność przez odsprzedaż w rundach, nie przez giełdę. Cena: 11 lat do rentowności, ponad 50 inwestorów, inwestorzy spoza UE/NATO na etapie growth, mniejszość w JV jako bilet do zamówień niemieckich. Wniosek: wzorzec dla Basiliska w wariancie produkcyjnym; wymaga zaplanowania Kryterium § 11 tak, aby nie zablokowało szczebli 3 i 5.

---

## 3a. Siedem archetypów z drugiej serii

- **Neo-prime (Anduril):** oprogramowanie pierwsze, sprzęt kupowany przejęciami, klient cywilny przed Pentagonem, potem OTA i programy of record; 11 mld USD kapitału i 1 mld USD straty rocznie. Do skopiowania sekwencja, nie skala.
- **Warstwa autonomii (Shield AI):** kontrakt DIU przed VC, licencje Hivemind dla OEM i primów, USAF kupuje autonomię osobno pod A-GRA; posiadanie płatowca (V-BAT) przyniosło wypadki i pozwy. Najbliższy wzorzec produktowy Basiliska.
- **Kapitał kotwiczny (Helsing):** jeden inwestor finansuje lata oprogramowania przed przychodem; AI wewnątrz platform Saaba i Airbusa; zwrot ku dronom przyniósł spór o HX-2. W Polsce kotwicę zastępują EDF, EDIP, SAFE i Ukraina.
- **Jurysdykcja za klientem (Destinus, Tekever):** Destinus przeniósł holding ze Szwajcarii do Holandii, bo prawo eksportowe i budżety NATO tego wymagały; Tekever założył spółkę w UK dziewięć lat przed przełomem. Siedziba matki może zostać w Polsce, ale spółka operacyjna musi być tam, gdzie zamawiający.
- **Inwestor strategiczny i exit poza UE (Milrem):** KMW 24,9 %, potem EDGE z ZEA; kwalifikowalność do EDF uratowały gwarancje Estonii. Dla § 11 to precedens w obie strony.
- **Polska droga (Creotech, APS):** państwo jako pierwszy inwestor (ARP) i drabina grantów NCBR → ESA → SMART → MON zakończona giełdą (Creotech); albo eksport przed MON, PE mniejszość i gwarancje bankowe pod prime'a bez giełdy (APS). Obie wymagają S.A. do notowań i obie pokazują, że MON przychodzi późno, ale zmienia skalę.
- **Fizyczne AI (Figure AI, Nomagic):** pełny stos humanoidów kosztuje 1–2 mld USD przed przychodem i finansuje go wyłącznie kapitał prywatny; polski zespół z amerykańskim VC przechodzi pod matkę w USA w 20 miesięcy, a lukę serii B wypełniają EBI i EBOR. Basilisk powinien być warstwą oprogramowania na cudzym sprzęcie.

---

## 4. Wspólne lekcje dla Basiliska

Oznaczenia stanu jak w `vc.md` sekcja 8: **OK** — umowa to przewiduje; **CZ** — częściowo; **BRAK** — dodać; **KOL** — koliduje; **DEC** — wymaga decyzji Założycieli. Szczegółowe mapowania są w sekcji 10 każdego case study.

| Lekcja | Skąd | Gdzie u nas | Stan | Co zrobić |
|---|---|---|---|---|
| P.S.A. nie może być notowana (art. 300³⁶ § 2 KSH); droga na giełdę zaczyna się od przekształcenia w S.A. i zdjęcia ograniczeń obrotu | Swarmer, WB | § 25 ust. 1 lit. e; § 10–16; `vc.md` sekcja 8 („Exit": BRAK) | BRAK | ścieżka giełdowa w umowie akcjonariuszy: przekształcenie, zobowiązanie do głosowania, lock-up, co zastępuje Kryterium po debiucie |
| Kryterium § 11 zderza się z każdą z trzech dróg: matka w USA (Swarmer), JV z Koreą i produkcja w Ukrainie (WB), inwestorzy z Japonii i Kataru (ICEYE) | wszystkie | § 11 ust. 6 i 14, § 33 ust. 4, § 25 ust. 1 lit. n; `regulations.md` sekcja 3 (art. 9 EDF: kontrola, nie udział) | DEC | rozstrzygnąć przed rundą: limit kontroli spoza UE/EOG dla programów UE, ścieżka zgody 75 % dla mniejszościowych inwestorów i partnerów spoza Kryterium, przywrócenie ust. 14 dla funduszy |
| Kapitał państwowy wchodzi późno i jako mniejszość: PFR po 20 latach, Solidium po 10, Tesi po 4; dla startupu droga wiedzie przez fundusze PFR, EIF, EIC Fund i wehikuły BGK | WB, ICEYE | `regulations.md` sekcja 3; `psa_todo.md` sekcja 6 | CZ | plan finansowania w szczeblach z nazwanymi wehikułami państwowymi; wszystkie spełniają Kryterium (kontrola państwa UE) |
| Punktem przegięcia jest pierwszy kontrakt publiczny, nie runda: WB 1998, ICEYE 2020 i 2025; Swarmer bez niego ma 0,3 mln USD przychodów mimo 100 tys. misji | wszystkie | § 31 ust. 1 (zamówienia, zaliczki, programy B+R), § 33 | CZ | pierwszy płatny pilot z producentem albo praca rozwojowa dla Agencji Uzbrojenia przed rundą A |
| Granty obniżają rozwodnienie, ale nie zastępują klienta: ICEYE ok. 83 mln EUR (7 % kapitału) użyte jako dźwignia do VC; Swarmer 50 tys. USD; WB zero | ICEYE, Swarmer | `psa_todo.md` sekcja 6 (EIC, SMART, DIANA) | OK | wniosek do EIC przed rundą A; grant jako argument w wycenie |
| JV i konsorcja z koncernami: Rheinmetall 60/40 jako strona kontraktu 1,7 mld EUR, Hanwha 51/49, ICEYE Polska z WZŁ-1 | ICEYE, WB | § 33 ust. 1–5 (mniejszość dopuszczalna, IP w Spółce, licencja niewyłączna, prawa przy braku kontroli) | OK | wzór umowy JV (etap C pkt 25) według modelu ICEYE–Rheinmetall; PGZ jako partner konsorcjum |
| Próg 25 %: PFR z 26,44 % blokuje uchwały kwalifikowane; w umowie Basiliska 75 % wszystkich głosów oznacza, że każdy pakiet powyżej 25 % blokuje | WB | § 25 ust. 1; § 32 ust. 2; § 25 ust. 1 lit. j (umorzenie zmienia proporcje) | CZ | maksymalny udział inwestora w uchwale kierunkowej; skutki umorzeń w umowie akcjonariuszy |
| Ład przez wzrost: przewodniczący z własną spółką i odejście założyciela-CEO cztery miesiące po IPO (Swarmer) kontra kontrola założycieli przez 29 lat (WB) | Swarmer, WB | § 10 (vesting, Odejście Dobrowolne), § 21 ust. 3, § 23 ust. 2, § 25 ust. 1 lit. h, § 29–30 | OK | nie oddawać tych postanowień w rundzie; vesting przeżywa przekształcenie |
| Dług dopiero przy przepływach: WB pierwsze obligacje po 17 latach, przy 300 mln zł przychodów, WIBOR + 2–3,7 pp; obligacje nie wymagają S.A. | WB | `catalyst.md`; § 31 ust. 4–5; § 25 ust. 1 lit. k; § 34 ust. 3 | OK | Plan Finansowania z kategorią „dług publiczny"; klauzula o obligacjach w § 31 do rozważenia |
| Płynność bez IPO: odsprzedaż ok. 600 mln EUR w rundach ICEYE; u Swarmera lock-up i −41 % w tydzień; u WB brak płynności do dziś | ICEYE, Swarmer | § 12, § 14, § 11 (Kryterium przy każdym nabyciu); `vc.md` sekcja 8 („permitted transfers") | KOL | szybka ścieżka zgody Spółki i wyłączenia prawa pierwszeństwa dla nabywców zweryfikowanych w rundzie |
| Horyzont: 34 miesiące (Swarmer, software), 11 lat do rentowności (ICEYE, sprzęt), 29 lat (WB, produkcja) | wszystkie | § 34 ust. 2 (reinwestycja 36 miesięcy); `vc.md` sekcja 6 | CZ | horyzont w umowie akcjonariuszy zależnie od wariantu: softwarowy albo produkcyjny |
| Miejsce rejestracji a polski „nexus": ICEYE fińskie z centrum operacyjnym w Warszawie i kontraktem MON; Swarmer amerykańskie z zespołem w Kijowie i Warszawie; WB polskie z produkcją w Ukrainie | wszystkie | `psa_todo.md` sekcja 1 | DEC | zamówienia publiczne wymagają podmiotu i zdolności w kraju zamawiającego, nie siedziby matki; struktura holdingowa tylko przed pierwszą rundą |
| Autonomia może być kupowana jako osobna pozycja pod rządową architekturą referencyjną (USAF A-GRA, niemiecki CFSN) i licencjonowana suwerennym OEM | Shield AI, Helsing | § 33 ust. 3; `regulations.md` sekcja 4 | BRAK | interfejsy zgodne z A-GRA i CFSN; produkt typu „Enterprise" dla producentów; precedens A-GRA w rozmowach z MON i PGZ |
| Czyste oprogramowanie dochodzi do programów of record przez platformę prima albo własny nośnik; posiadanie sprzętu kosztuje (V-BAT, HX-2) | Anduril, Shield AI, Helsing | § 33; sekcja 3a tego pliku | DEC | pakiet autonomii w konsorcjum sprzętowym (PGZ, WB, Saab); rozdzielić w umowach metryki autonomii od płatowca i wyrzutni |
| Siedziba holdingu idzie za prawem eksportowym i budżetami klientów; spółka zależna w kraju zamawiającego założona wcześnie | Destinus, Tekever, Anduril | `jurisdictions/README.md` sekcje 1 i 4.2; § 33 | OK | matka w Polsce; pierwsza spółka zależna po pierwszym kontrakcie (kolejność w `jurisdictions/README.md` sekcja 4.2) |
| Exit albo inwestor większościowy spoza UE uruchamia art. 9 EDF; ratunkiem są gwarancje państwa członkowskiego | Milrem | § 11; `jurisdictions/kryteria.md` sekcja 3 | OK | w umowie inwestycyjnej: exit poza Kryterium tylko po uchwale 75 % i rozmowie z MON o gwarancjach |
| Inwestor kotwiczny z mandatem wielorundowym obniża ryzyko każdej kolejnej rundy (Founders Fund 5 z 9 rund, Prima Materia A i D, Khosla każda runda) | Anduril, Helsing, Nomagic | `vc.md` sekcje 3–4; § 32 | CZ | szukać inwestora rundy A z kapitałem na B i C (NIF, PFR, EIF); pro-rata w umowie inwestycyjnej |
| Kapitał uprzywilejowany PE i banków przed akcjami zwykłymi pojawia się przy 5–13 mld USD (Blackstone w Shield AI) | Shield AI | § 31 ust. 4; § 6–8 (rodzaje akcji) | CZ | sprawdzić, czy umowa dopuszcza serie uprzywilejowane o stałej stopie i liquidation preference |
| Polska giełda działa dla deep techu z kotwicą publiczną: NewConnect (11 mln zł) → GPW (40 mln zł) → emisje po kontraktach; wymaga S.A. i rozwadnia założycieli do 6–7 % | Creotech, APS | § 25 ust. 1 lit. e; art. 300³⁶ § 2 KSH | DEC | zdecydować, czy Założyciele akceptują rozwodnienie poniżej 25 % w zamian za giełdę; jeśli nie, droga WB i APS |
| MON przychodzi po sojusznikach (APS: UK dla Ukrainy 2022 r., SAN 2026 r.; Creotech: MikroGlob po 12 latach), ale wtedy mnoży przychód | APS, Creotech | `jurisdictions/polska.md` sekcja 7; `psa_todo.md` sekcja 6 | DEC | plan etapu C z pierwszym klientem sojuszniczym finansowanym przez darczyńcę i MON jako drugim |
| Banki rozwoju (EBI venture debt, EBOR) i gwarancje bankowe pod prime'a wypełniają lukę serii B bez rozwodnienia | Nomagic, APS | § 31; `vc.md` sekcja 6 | BRAK | EBI, EBOR, EIF Defence Equity Facility i gwarancje BGK w planie finansowania etapu C |
| Fizyczne AI pełnego stosu kosztuje 1–2 mld USD przed przychodem; własność modelu i danych z wdrożeń to aktywo, za które płacą inwestorzy | Figure AI, Nomagic | § 26; wzór umowy pilota (etap C pkt 25) | BRAK | prawa do danych treningowych w każdym pilocie; Basilisk jako warstwa oprogramowania |
| Dokumentacja bezpieczeństwa pokazana inwestorom musi przetrwać rundę; zamrożona specyfikacja u powolnego zamawiającego niszczy reputację | Figure AI, APS | § 23 ust. 2; § 29–30 | CZ | polityka bezpieczeństwa systemów autonomicznych w data room; klauzula spiralnej aktualizacji w umowach z MON |

---

## 5. Jurysdykcje w case studies i typowe jurysdykcje startupów

**Występujące w plikach** (państwa i miasta, w roli siedziby, spółki zależnej, inwestora, klienta, poligonu albo giełdy): Ukraina (Kijów), Stany Zjednoczone (Delaware, Austin, Teksas, Floryda, Los Angeles, Irvine, Tampa, Nasdaq), Estonia, Polska (Warszawa, Kraków, Ożarów Mazowiecki, Gliwice, GPW i Catalyst), Czechy, Wielka Brytania, Finlandia (Espoo, Helsinki), Niemcy (Neuss, Frankfurt), Holandia (Amsterdam), Francja (Bpifrance), Hiszpania, Portugalia, Grecja (Ateny), Szwecja, Dania, Luksemburg, Japonia, Korea Południowa, Katar, Brazylia, Indie, Malezja, Gruzja, Turcja, Bliski Wschód, Iran (jako czynnik kursowy); organizacje: UE, EOG, NATO, ESA. Ich rola w każdym przypadku jest opisana w sekcjach 2, 3 i 8 case studies.

**Występujące w drugiej serii** (dodatkowo): Portugalia (Lizbona), Wielka Brytania (Southampton, Bristol, Aberporth, Swindon, Plymouth, Londyn), Szwajcaria (Payerne, Zurych), Holandia (Hengelo, Valkenburg, Born), Hiszpania, Niemcy (Monachium, Unterlüß, Mattsies), Estonia (Tallinn), Zjednoczone Emiraty Arabskie (Abu Zabi), Ukraina (Kijów), USA (San Diego, Frisco, Austin, Ohio, Irvine, Spartanburg, San Jose), Australia (Sydney, Port Melbourne), Japonia (Tokio, Jokosuka), Korea Południowa, Tajwan, Norwegia (Oslo), Szwecja (Sztokholm), Francja (Paryż), Polska (Piaseczno, Gdynia, Warszawa). Profile jurysdykcji: `jurisdictions/README.md`; Portugalia: `jurisdictions/portugalia.md`.

**Typowe jurysdykcje rejestracji startupów, których nie ma w case studies, z uwagą dla firmy obronnej** **[W]**:

| Jurysdykcja | Dlaczego startupy ją wybierają | Uwaga dla Basiliska |
|---|---|---|
| Delaware (USA) jako matka | standard dla VC z USA, prawo korporacyjne, Nasdaq; wzór Swarmera | kontrola spoza UE wyklucza z EDF, AGILE i EUDIS; Kryterium § 11 dopuszcza (NATO), ale `regulations.md` sekcja 3 sugeruje limit dla kontroli; spółka zależna w USA (wzór ICEYE US) zamiast matki |
| Wielka Brytania (Ltd) | londyński kapitał, NSSIF jako inwestor obronny, prawo angielskie w umowach inwestycyjnych | NATO, ale poza UE i poza EDF; kontrola z UK to ten sam problem co USA (`regulations.md` sekcja 3a) |
| Estonia (OÜ) | e-rezydencja, szybka rejestracja, niskie koszty, spółki kontraktowe dla firm ukraińskich (Swarmer Estonia OÜ, Farsight Vision) | UE i NATO, więc bez kolizji z Kryterium; realna alternatywa z `psa_todo.md` sekcja 1 |
| Finlandia, Szwecja, Dania | granty (Business Finland, Vinnova, EIFO), inwestorzy państwowi (Tesi, Solidium), gęstość startupów; wzór ICEYE | UE i NATO; wsparcie „na zasadach grantowych" (Modrzewski) |
| Niemcy (GmbH) i Francja (SAS) | największe budżety obronne UE, Helsing i Quantum Systems, Bpifrance i KfW jako inwestorzy państwowi | UE i NATO; wysokie koszty i formalizm; JV z koncernem (Rheinmetall, KNDS) jako droga do zamówień |
| Holandia (BV) i Luksemburg (S.à r.l., SCSp) | holdingi i fundusze, Euronext Amsterdam (CSG, Destinus), umowy o unikaniu podwójnego opodatkowania | UE i NATO; holding bez działalności operacyjnej nie pomaga w zamówieniach publicznych |
| Irlandia | anglojęzyczna UE, podatek CIT 12,5 %, siedziby technologiczne | UE, ale poza NATO: inwestor irlandzki spełnia Kryterium (UE), lecz Irlandia nie jest w NATO |
| Szwajcaria | kapitał, neutralność, Destinus | poza UE i NATO: podmiot kontrolowany ze Szwajcarii nie spełnia Kryterium § 11 |
| Izrael | defense tech, kapitał, doświadczenie eksportowe | poza UE i NATO: nie spełnia Kryterium; kontrola eksportu obu stron |
| Singapur, Zjednoczone Emiraty Arabskie (ADGM, DIFC), Kajmany, Brytyjskie Wyspy Dziewicze | holdingi funduszy, kapitał z Azji i Zatoki (QIA w ICEYE), wehikuły offshore | spoza Kryterium; fundusze z takich siedzib wymagają uchwały WZ 75 % (§ 11 ust. 6), a ich beneficjenci rzeczywiści muszą być ustaleni (§ 11 ust. 4) |
| Cypr, Malta | holdingi dla Europy Środkowej, niskie podatki | UE, ale poza NATO; Cypr bywa problemem przy weryfikacji beneficjentów rzeczywistych i sankcjach |
| Litwa, Łotwa, Czechy | sąsiedzi z rosnącym defense tech (CSG, Frankenburg w Estonii), fundusze państwowe | UE i NATO; bez kolizji z Kryterium |

Szczegółowe profile tych jurysdykcji (założenie spółki, podatki 2026, licencje obronne, fundusze, DIANA, NIF, SAFE) i rekomendacja co do siedziby, spółek zależnych i holdingu: katalog `jurisdictions/` (`jurisdictions/README.md`).

---

## 6. Co dalej

1. Rozstrzygnąć pytanie o jurysdykcję i strukturę holdingową (`psa_todo.md` sekcja 1) z użyciem sekcji 3 i 10 każdego case study: droga Swarmera wyklucza programy UE, droga ICEYE pokazuje, że polski „nexus" można zbudować spółką zależną.
2. Dopisać do umowy akcjonariuszy (etap C pkt 26 w `plan_prac.md`) ścieżkę giełdową i klauzulę o obligacjach; szczegóły w `swarmer.md` sekcja 10 i `catalyst.md` sekcja 5.
3. Uzupełnić `psa_todo.md` sekcja 6 o plan finansowania w szczeblach (wzór ICEYE) z nazwanymi wehikułami państwowymi spełniającymi Kryterium.
4. Sprawdzić przed użyciem na zewnątrz liczby oznaczone [Z] w dokumentach pierwotnych (SEC, EBI, komunikaty spółek), bo w tej sesji pochodziły ze streszczeń.
5. Wdrożyć rekomendacje z `conclusions.md` (sekcja 4): decyzje do podjęcia przed rundą A i zmiany w umowie inwestycyjnej wynikające z drugiej serii (A-GRA, dane treningowe, exit poza Kryterium, kapitał uprzywilejowany).
