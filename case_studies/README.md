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

## 3. Trzy drogi i ich cena

- **Swarmer: kapitał zamiast klienta.** Inwestorzy i rynek wycenili dane z pola walki, nie sprzedaż; spółka weszła na giełdę z przychodami rzędu 0,3 mln USD i wykorzystała zawyżony kurs jako walutę (linia kapitałowa, przejęcie Ratel). Cena: struktura w USA (poza EDF), zmienność kursu, ład podporządkowany przewodniczącemu rady, odejście założyciela-CEO, rozwodnienie. Wniosek dla Basiliska: droga możliwa tylko po rezygnacji z programów UE i po przekształceniu P.S.A. w S.A.; w Polsce jej odpowiednikiem byłby NewConnect albo rynek główny GPW.
- **WB: klient zamiast kapitału.** Dwadzieścia lat wzrostu z zamówień MON, licencji i eksportu, potem dług na przejęcia i jedna runda z PFR jako mniejszością. Cena: 20 lat do 300 mln zł przychodów, zależność od kalendarza zamówień publicznych, inwestor państwowy z mniejszością blokującą, brak płynności dla właścicieli do dziś. Wniosek: model najbliższy polskim realiom Basiliska, ale wymaga pierwszego płacącego zamawiającego na etapie B+R (WB: przetarg z 1998 r., którego nikt inny nie chciał).
- **ICEYE: drabina, na której każdy szczebel ma innego inwestora.** Granty na prototyp, VC na starty, państwo i koncerny jako kapitał cierpliwy, kontrakty rządowe jako przegięcie, growth equity po rentowności; płynność przez odsprzedaż w rundach, nie przez giełdę. Cena: 11 lat do rentowności, ponad 50 inwestorów, inwestorzy spoza UE/NATO na etapie growth, mniejszość w JV jako bilet do zamówień niemieckich. Wniosek: wzorzec dla Basiliska w wariancie produkcyjnym; wymaga zaplanowania Kryterium § 11 tak, aby nie zablokowało szczebli 3 i 5.

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

---

## 5. Jurysdykcje w case studies i typowe jurysdykcje startupów

**Występujące w plikach** (państwa i miasta, w roli siedziby, spółki zależnej, inwestora, klienta, poligonu albo giełdy): Ukraina (Kijów), Stany Zjednoczone (Delaware, Austin, Teksas, Floryda, Los Angeles, Irvine, Tampa, Nasdaq), Estonia, Polska (Warszawa, Kraków, Ożarów Mazowiecki, Gliwice, GPW i Catalyst), Czechy, Wielka Brytania, Finlandia (Espoo, Helsinki), Niemcy (Neuss, Frankfurt), Holandia (Amsterdam), Francja (Bpifrance), Hiszpania, Portugalia, Grecja (Ateny), Szwecja, Dania, Luksemburg, Japonia, Korea Południowa, Katar, Brazylia, Indie, Malezja, Gruzja, Turcja, Bliski Wschód, Iran (jako czynnik kursowy); organizacje: UE, EOG, NATO, ESA. Ich rola w każdym przypadku jest opisana w sekcjach 2, 3 i 8 case studies.

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

---

## 6. Co dalej

1. Rozstrzygnąć pytanie o jurysdykcję i strukturę holdingową (`psa_todo.md` sekcja 1) z użyciem sekcji 3 i 10 każdego case study: droga Swarmera wyklucza programy UE, droga ICEYE pokazuje, że polski „nexus" można zbudować spółką zależną.
2. Dopisać do umowy akcjonariuszy (etap C pkt 26 w `plan_prac.md`) ścieżkę giełdową i klauzulę o obligacjach; szczegóły w `swarmer.md` sekcja 10 i `catalyst.md` sekcja 5.
3. Uzupełnić `psa_todo.md` sekcja 6 o plan finansowania w szczeblach (wzór ICEYE) z nazwanymi wehikułami państwowymi spełniającymi Kryterium.
4. Sprawdzić przed użyciem na zewnątrz liczby oznaczone [Z] w dokumentach pierwotnych (SEC, EBI, komunikaty spółek), bo w tej sesji pochodziły ze streszczeń.
