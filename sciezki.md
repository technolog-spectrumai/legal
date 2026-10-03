# Ścieżki zmiany umowy P.S.A. — osiem profili kapitałowych

Dokument wewnętrzny Basilisk Systems, informacyjny. Nie jest opinią prawną i nie zmienia umowy spółki. Odpowiada na pytanie: w którą stronę można przebudować projekt umowy (`psa.tex`, wersja 1.0-RC, wariant A), jeżeli Spółka ma być bardziej (1) pod VC, (2) odporna na VC, (3) przemysłowa, (4) bootstrapowa, (5) inkubatorowa, (6) akceleratorowa, (7) pod granty, (8) pod kapitał instytucjonalny — co każda ścieżka zmienia w konkretnych paragrafach, co daje, co kosztuje i które ścieżki się wykluczają.

Uzupełnia `vc.md` (oczekiwania funduszy — uwaga: `vc.md` opisuje wersję 0.9.4-C, część jego zaleceń jest już wdrożona w 1.0-RC, zob. sekcja 3.1), `regulations.md` sekcja 3–3a (wymogi właścicielskie programów), `emisja/*.md` i decyzje D1–D16 memorandum. Numery § według `spis_tresci.md`.

Stan na 3 października 2026 r. Oznaczenia jak w `regulations.md`: **[Z]** sprawdzone w źródle w `src/legal/`, **[W]** wiedza ogólna o praktyce, do potwierdzenia, **[?]** hipoteza.

---

## 1. Główny wniosek

1. **Nie trzeba wybierać jednej ścieżki.** Projekt już jest hybrydą: rdzeń przemysłowo-grantowy (Kryterium § 11, bezpieczeństwo i eksport § 27–28, spółki celowe § 33, reinwestycja zysku § 34 ust. 2) z modułem VC, który w wersji 1.0-RC jest w większości gotowy (§ 11 ust. 14 Kwalifikowany Inwestor Finansowy, Przeniesienia Dozwolone w § 12, dyrektor inwestora w § 21 ust. 3, katalog warunków rundy z ochroną serii w § 32 ust. 4 lit. f).
2. **Właściwa architektura to „rdzeń stały + moduły uśpione”.** Rdzeń nie zmienia się w żadnej ścieżce (sekcja 2). Moduły ścieżek są albo już w umowie i włączają się uchwałą (runda, instrumenty zamienne, spółki celowe), albo czekają jako gotowe brzmienia do wpisania przy konkretnym zdarzeniu.
3. **Prawdziwie sprzeczne są trzy pary:** VC/instytucje ↔ odporność na VC (kontrola głosów), granty EDF/AGILE ↔ kontrolujący inwestor spoza UE/EOG, inwestor przemysłowy ↔ VC (prawo pierwszeństwa strategicznego i wycena wyjścia). Reszta to sekwencja, nie konflikt (sekcja 5).
4. **Największa luka obecnego projektu to ochrona kontroli Założycieli po pierwszej rundzie.** Każda akcja serii A ma jeden głos (§ 5 ust. 3), a Sprawy Zastrzeżone liczą 75 % wszystkich głosów (§ 25). Inwestor z ponad 25 % głosów blokuje wszystko, a Założyciele po rozwodnieniu ESOP-em (15 %) i serią F (do 20 %) mogą stracić własne 75 % jeszcze przed rundą. Ścieżka 2 pokazuje ustawowe narzędzia P.S.A., które to naprawiają (art. 300²⁶ KSH — akcje założycielskie).

---

## 2. Rdzeń stały — wspólny dla wszystkich ścieżek

| Element | § | Dlaczego nie ruszać |
|---|---|---|
| Kryterium Bezpieczeństwa EU/NATO co do **kontroli** | § 11 ust. 5–6, 15 | warunek EDF/AGILE/EUDIS (brak kontroli przez niestowarzyszone państwo trzecie, art. 9 rozporządzenia 2021/697 i motyw 95 **[Z]** `eu_32021R0697_edf_PL.txt`), koncesji MSWiA i DIANA; fundusze obronne traktują jako atut (`vc.md` sekcja 6) |
| Bezpieczeństwo informacji, dostęp spoza UE/NATO, kontrola eksportu | § 27 ust. 6, § 28 | bez nich bramki G2–G5 z `regulations.md` są nie do przejścia |
| Kluczowa Własność Intelektualna w Spółce | § 7, § 26, § 33 ust. 3 | każdy inwestor i każdy grant bada tytuł do IP; licencja do spółek celowych tylko niewyłączna |
| Vesting i zwrotne zbycie jako obowiązek związany z akcją | § 10 | standard rynkowy niezależnie od źródła kapitału |
| Wartość Godziwa i Niezależny Ekspert | § 19 | jeden standard ceny dla wszystkich mechanizmów wyjścia |
| Zgoda Spółki na zbycie z zamkniętym katalogiem odmowy | § 12 ust. 1–2 | odmowa wyłącznie z przyczyn bezpieczeństwa i prawa, co jest do obrony wobec każdego inwestora |

Ścieżki różnią się wszystkim innym: progami głosów, rodzajami akcji, prawami inwestora, mechaniką wyjścia, dywidendą, ładem Rady.

---

## 3. Osiem ścieżek

Każda ścieżka: **kto daje kapitał → czego wymaga → co zmienić w umowie → zysk / koszt**.

### 3.1. Bardziej pod VC

**Kapitał.** Fundusze seed i serii A (polskie ASI z kapitałem PFR/FENG, fundusze deep tech i obronne z UE, NIF). Ticket 2–15 mln zł, 15–25 % na rundę **[W]**.

**Wymagania.** Akcje uprzywilejowane odrębnej serii, preferencja 1× non-participating, antyrozwodnienie BBWA, protective provisions serii, miejsce w Radzie, swoboda przeniesień w grupie funduszu, drag z ochroną inwestora, brak badania każdego LP (`vc.md` sekcje 2–4).

**Stan w 1.0-RC.** Zrobione: § 11 ust. 14 (Kwalifikowany Inwestor Finansowy: test zarządzającego, siedziby i kontroli zamiast look-through LP, limity 25 %/50 % dla inwestorów spoza Kryterium), § 11 ust. 15 (zmiana składu LP nie jest utratą Kryterium), § 12 (Przeniesienia Dozwolone do funduszu równoległego, kontynuacyjnego, następcy, SPV), § 21 ust. 3 (jeden dyrektor niewykonawczy inwestora spoza Kryterium za zgodą 75 %), § 32 ust. 4 lit. a–f (1× NP, BBWA, dyrektor/obserwator, informacje, pro-rata, zgoda serii na zmiany naruszające jej prawa).

**Co jeszcze zmienić.**

| § | Zmiana | Priorytet |
|---|---|---|
| § 16 | po Kwalifikowanej Rundzie drag wymaga zgody większości akcji serii inwestorskiej albo upływu okresu ochronnego (np. 4–5 lat) i ceny minimalnej (np. 2–3× ceny emisyjnej serii); podział ceny według uprzywilejowania (waterfall) zamiast „taka sama cena za akcję tego samego rodzaju” (ust. 2 lit. b nie przeszkadza, ale nie przewiduje preferencji) | zalecane |
| § 5, nowy ust. | z góry zdefiniowana „seria I” z maksymalną liczbą akcji i terminem emisji — wtedy emisja nie wymaga trybu zmiany umowy (art. 300¹⁰³ KSH **[Z]**); uprzywilejowanie co do podziału majątku i głosu dopuszcza art. 300²⁵ § 2 **[Z]**, a uchwała o emisji określa uprzywilejowanie akcji nowej emisji (art. 300¹⁰⁴ § 1 pkt 2 **[Z]**); czy uprzywilejowanie można zapisać w umowie z góry dla akcji jeszcze nieistniejących — **[?]**, pytanie do kancelarii | opcjonalne, skraca rundę |
| § 38 | zgoda indywidualna serii na zmianę umowy uszczuplającą jej prawa (dziś tylko jako warunek rundy z § 32 ust. 4 lit. f — przenieść do postanowień końcowych, żeby działał niezależnie od uchwały kierunkowej) | zalecane |
| § 13 | lock-up Założycieli do 3–5 lat albo do wyjścia — **nie w umowie spółki**, tylko w umowie akcjonariuszy rundy | w rundzie |
| § 29 | zakaz konkurencji po odejściu 18–24 miesiące — w umowie akcjonariuszy, z odszkodowaniem | w rundzie |

**Zysk.** Krótsze due diligence, wyższa wycena, dostęp do follow-on. **Koszt.** Po rundzie Założycielom zostaje zwykle 50–65 % (po ESOP); inwestor z ponad 25 % blokuje każdą Sprawę Zastrzeżoną, drag przestaje być w rękach Założycieli.

### 3.2. Bardziej odporna na VC (kontrola Założycieli)

**Kapitał.** Ten sam co w 3.1, ale na warunkach Założycieli: inwestorzy finansowi przyjmują ograniczoną rolę w zamian za udział w wyniku. Akceptują to głównie fundusze obronne i rodzinne, aniołowie, część CVC **[W]**; generalistyczne VC traktują dual-class na seed jako sygnał ostrzegawczy **[W]**.

**Narzędzia ustawowe P.S.A. (wszystkie [Z], `pl_2000_1037_ksh_ujednolicony.txt`, art. 300²⁵–300²⁸):**

- **akcje założycielskie (art. 300²⁶)** — „każda kolejna emisja nowych akcji nie może naruszać określonego minimalnego stosunku liczby głosów” tych akcji do wszystkich głosów; przy emisji, która by go naruszyła, liczba głosów z akcji założycielskich zwiększa się automatycznie, a uchwała o emisji wskazuje nową liczbę głosów. To jedyny mechanizm, który chroni udział w głosach **bez zgody inwestora przy każdej rundzie**;
- **uprzywilejowanie co do głosu (art. 300²⁵)** — katalog otwarty („w szczególności”), w P.S.A. bez limitu liczby głosów na akcję znanego z S.A. **[W]** co do braku limitu — do potwierdzenia;
- **akcje nieme (art. 300²⁷)** — dla inwestora: preferencja dywidendowa w zamian za brak głosu, z okolicznościami, w których głos odżywa;
- **uprawnienia indywidualne (art. 300²⁸)** — np. prawo Założycieli (oznaczonych imiennie) do powoływania większości Rady Dyrektorów; wygasają z utratą statusu akcjonariusza, chyba że umowa stanowi inaczej.

**Co zmienić.**

| § | Zmiana |
|---|---|
| § 5–6 | część serii A (np. akcje Założycieli Pierwotnych) jako akcje założycielskie z minimalnym stosunkiem głosów (np. 51 % albo 75 %), z **sunsetem**: wygasa przy IPO, po N latach albo co do akcji Założyciela, który odszedł (powiązanie z § 10 — akcje odkupione wracają jako zwykłe) |
| § 21 ust. 2 | uprawnienie indywidualne Założycieli do powołania większości Rady, dopóki łącznie mają co najmniej X % akcji |
| § 16 | drag tylko za zgodą większości akcji założycielskich |
| § 32 ust. 4 | zamknąć katalog: wykluczyć participating, full ratchet, weto operacyjne; seria inwestorska może być niema albo z ograniczonym głosem |
| § 25 | próg Spraw Zastrzeżonych liczyć z akcji założycielskich (wtedy 75 % = większość, którą Założyciele mają zawsze) albo dwa progi: strukturalne (75 %) i operacyjne (zwykła większość) |

**Zysk.** Kontrola przetrwa 2–3 rundy; ochrona przed wymuszonym exitem do podmiotu, którego Założyciele nie akceptują (istotne przy technologii obronnej). **Koszt.** Mniejszy krąg funduszy, niższa wycena; ryzyko, że Kryterium kontroli i akcje założycielskie razem dadzą obraz „spółki nieinwestowalnej” **[W]**; konflikt z ścieżkami 1 i 8 (sekcja 5).

### 3.3. Bardziej przemysłowa

**Kapitał.** Koncern obronny, integrator, producent UAV/USV, CVC, partner produkcyjny; kapitał często w formie kontraktu, zaliczki, wspólnej spółki, a nie akcji **[W]**.

**Wymagania.** Prawo pierwszeństwa nabycia Spółki albo wyłączność na pole, licencja na IP, udział w spółce produkcyjnej, miejsce w Radzie, zgoda na zmianę kontroli (klauzule change-of-control w kontraktach obronnych).

**Co zmienić.** Główny kanał to **§ 33 (Przedsięwzięcia Produkcyjne), nie equity w Spółce-matce** — umowa ma już licencję niewyłączną z polem, terytorium i czasem, weryfikację partnera, prawa minimalne Spółki i finansowanie bez regresu.

| § | Zmiana |
|---|---|
| § 33 | dopisać: zakaz wyłączności dostaw lub zakupu dłuższej niż 3–5 lat bez uchwały 75 % (anty-lock-in); prawo Spółki do odkupu udziału partnera po Wartości Godziwej przy zmianie kontroli nad partnerem (już jest prawo wyjścia — rozważyć opcję kupna) |
| § 14 | jeżeli strategiczny wchodzi do Spółki: najwyżej ROFO (prawo pierwszej oferty) ograniczone w czasie, **nie** ROFR na sprzedaż całej Spółki i nie opcja kupna |
| § 16 ust. 2 | warunek: transakcja nie narusza change-of-control w kontraktach obronnych albo uzyskano zgody zamawiających |
| § 29–30 | akcjonariusz-klient: wyłączenie głosu przy umowach z nim, dostęp do informacji handlowych o konkurentach tylko przez „clean team” |
| § 23 | dyrektor wskazany przez strategicznego nie głosuje w sprawach dotyczących jego konkurentów i cen |

**Zysk.** Przychód i skala produkcji bez rozwodnienia, ścieżka do certyfikacji i zamówień. **Koszt.** Strategiczny w kapitale odstrasza VC i innych klientów (konkurentów strategicznego); ryzyko „pełzającego przejęcia” przez licencję i wyłączność; obniżona wycena przy wyjściu do innego nabywcy.

### 3.4. Bardziej bootstrapowa

**Kapitał.** Przychody, zaliczki od klientów, kontrakty B+R, pożyczki Założycieli (§ 7 ust. 7), leasing (§ 31 ust. 5); bez rund.

**Co zmienić (uprościć, nie usuwać rdzenia).**

| § | Zmiana |
|---|---|
| § 21 | Rada 1–3 osób (dziś 3–7) i dyrektor niewykonawczy nieobowiązkowy do czasu rundy |
| § 22 | reprezentacja jednoosobowa do progu (np. 100 000 zł) |
| § 25 | mniej Spraw Zastrzeżonych; podnieść próg lit. k z 500 000 zł albo wiązać z budżetem |
| § 34 ust. 2 | dywidenda dopuszczalna wcześniej niż po 36 miesiącach, gdy gotówka przekracza N miesięcy kosztów; dla bootstrapu dywidenda to główna forma wynagrodzenia Założycieli |
| § 8 | pula 10 % zamiast 15 %, albo program phantom/gotówkowy zamiast akcji serii P (mniej kosztów notarialnych i KRS) |
| § 32 | zostawić bez zmian (uśpiony), żeby nie zamykać drogi |

**Zysk.** Kontrola i niskie koszty ładu. **Koszt.** Wolniejszy wzrost; przy późniejszej rundzie trzeba przywrócić Radę i katalog spraw (zmiana umowy u notariusza, ale bez przeszkody prawnej).

### 3.5. Bardziej inkubatorowa

**Kapitał.** Inkubator, park technologiczny, uczelnia, hub obronny; zwykle 5–10 % akcji za infrastrukturę, laboratorium, poligon, mentoring, usługi prawne, czasem z małą gotówką **[W]**.

**Kluczowy fakt prawny.** W P.S.A. „wkładem niepieniężnym na pokrycie akcji może być wszelki wkład mający wartość majątkową, w szczególności świadczenie pracy lub usług” (art. 300² § 2 KSH **[Z]**). Obecny § 7 ust. 2 wyłącza pracę i usługi tylko u Założycieli serii A; § 9 korzysta z wkładu w postaci pracy dla serii F. Inkubator może więc objąć akcje za usługi bez zmiany ustawowych zasad, ale wkład usługowy nie idzie na kapitał akcyjny (art. 300³ § 1 w zw. z art. 14 § 1 KSH **[Z]**).

| § | Zmiana |
|---|---|
| § 25 / nowa uchwała | emisja dla inwestora usługowego: opis świadczeń, harmonogram, wycena, data rozpoczęcia |
| § 10 (odpowiednio) | mechanizm zwrotny przy niewykonaniu usług — jak vesting serii F (§ 9 ust. 9), po cenie emisyjnej |
| § 12 | Przeniesienia Dozwolone także do funduszu lub spółki zależnej inkubatora (dziś tylko Kwalifikowany Inwestor Finansowy) |
| § 32 ust. 4 | bez weta; prawa informacyjne i pro-rata najwyżej do pierwszej rundy |
| § 11 | inkubator zwykle polski — bez kolizji z Kryterium; uczelnia jako podmiot publiczny: sprawdzić, czy jej udział nie jest „kontrolą państwową” w rozumieniu § 11 ust. 14 lit. b (nie jest, jeżeli państwo z UE/NATO **[W]**) |

**Zysk.** Infrastruktura i wiarygodność bez gotówki. **Koszt.** Rozwodnienie na najniższej wycenie; „martwy” akcjonariusz w cap table, jeżeli usług nie wykonano, a nie ma mechanizmu zwrotnego.

### 3.6. Bardziej akceleratorowa

**Kapitał.** Akceleratory z equity (5–10 % za 100–500 tys. zł), programy publiczne bez equity: NATO DIANA (100 tys. EUR faza 1, do 300 tys. EUR faza 2 **[Z]** `regulations.md` 3), EUDIS Business Accelerator (voucher 65 tys. EUR **[Z]**), EIC Accelerator (grant do 2,5 mln EUR + inwestycja do 30 mln EUR **[Z]**).

**Instrument.** SAFE / pożyczka konwertowalna z cap i dyskontem. § 31 ust. 4 już wymaga dla instrumentów zamiennych uchwały 75 % — mechanika jest, brakuje parametrów konwersji.

| § | Zmiana |
|---|---|
| § 32, nowy ust. | „Instrument Zamienny”: konwersja przy Kwalifikowanej Rundzie po niższej z ceny cap i ceny rundy minus dyskonto; MFN; konwersja przy sprzedaży Spółki (1× zwrot albo konwersja); termin długi bez rundy (konwersja po cap albo zwrot) |
| § 25 ust. 2 / § 32 | prawo poboru może być wyłączone przez samą umowę spółki — art. 300¹⁰⁶ § 1 KSH: prawo poboru przysługuje, „jeżeli umowa spółki lub uchwała akcjonariuszy nie stanowią inaczej” **[Z]**; wyłączyć je z góry dla emisji konwersyjnej, żeby nie potrzebować 4/5 |
| § 11 | akcelerator z USA (np. YC) to podmiot z NATO — Kryterium spełnione; ale to „kontrola” tylko przy większości, więc bez kolizji z EDF; sprawdzić OISP (oświadczenia z wzorów NVCA, `vc.md` sekcja 2) |
| § 10 | akcelerator często wymaga vestingu Założycieli z datą sprzed programu — Załącznik nr 2 |

**Zysk.** Szybki kapitał bez wyceny, sieć. **Koszt.** Konwersja przy niskim cap rozwadnia bardziej niż runda; kilka SAFE z różnymi cap komplikuje cap table przed serią A.

### 3.7. Bardziej pod granty

**Kapitał.** EDF, AGILE (od 2027, 1–5 mln EUR), EUDIS, EIC Accelerator, ścieżka SMART (PARP/NCBR), granty krajowe MON/NCBR.

**Wymagania.** EDF: siedziba i struktury zarządcze w UE, brak kontroli przez niestowarzyszone państwo trzecie lub podmiot z takiego państwa, derogacja tylko za gwarancjami państwa członkowskiego **[Z]** (art. 9, motyw 95, definicja „podmiotu z niestowarzyszonego państwa trzeciego”); AGILE i EUDIS jak EDF **[?]**; trwałość projektu, zakaz podwójnego finansowania, IP z projektu w UE, rachunkowość projektowa **[W]**.

| § | Zmiana |
|---|---|
| § 11, nowy ust. | **warunkowe zawężenie Kryterium kontroli do UE/EOG**: „dopóki Spółka jest beneficjentem albo wnioskodawcą EDF, AGILE lub EUDIS, żaden podmiot spoza UE/EOG (w tym z NATO) ani ich grupa nie uzyskuje kontroli ani prawa weta” — to otwarte pytanie z `psa_todo.md` sekcja 1 i decyzja D6; Kryterium dla samego udziału zostaje EU/NATO |
| § 21 ust. 3 | co najmniej dwóch dyrektorów z obywatelstwem UE/EOG (EDF: zarząd w UE; koncesja: `regulations.md` 3a) |
| § 25 | nowa Sprawa Zastrzeżona: czynność naruszająca warunki trwałości lub umowy o dofinansowanie (zbycie IP z projektu, zmiana kontroli, przeniesienie działalności poza UE) |
| § 16 ust. 2 | warunek: zgoda instytucji finansującej, jeżeli umowa o dofinansowanie jej wymaga |
| § 26 / § 33 ust. 3 | IP powstałe w projekcie nie opuszcza UE (licencja do SPV spoza UE wymaga uchwały 75 %) |
| § 31 ust. 4 | już zwalnia „standardowe postanowienia umów o dofinansowanie” z uchwały WZ — zostawić |
| § 34 | dywidenda nie z dotacji; rezerwa na wkład własny do projektów |

**Zysk.** Kapitał nierozwadniający, wiarygodność wobec MON/NATO; granty dla DSR rosną i mogą dorównać VC **[Z]** (`nif_report_2026.txt` przez `vc.md` sekcja 6). **Koszt.** Kontrolujący inwestor z USA/UK wyłącza EDF; trwałość projektu spowalnia exit; obciążenie administracyjne.

### 3.8. Bardziej pod kapitał instytucjonalny

**Kapitał.** PFR (przez fundusze), EIF/Defence Equity Facility, NIF (do 15 mln EUR initial ticket, board involvement, siedziba w państwie-LP **[Z]** `web_nif_about.txt`), fundusze emerytalne i ubezpieczeniowe przez fundusze funduszy, family offices, późniejsze growth i IPO.

**Wymagania.** Wszystko z 3.1 plus: instytucjonalny ład korporacyjny, przewidywalność, ESG i polityki wykluczeń (broń autonomiczna), raportowanie do LP, badanie sprawozdań, zdolność do IPO **[W]**.

| § | Zmiana |
|---|---|
| § 21 ust. 6–7 | co najmniej jeden dyrektor niezależny (niepowiązany z Założycielami ani inwestorem) po serii A; komitet audytu i komitet wynagrodzeń w regulaminie Rady |
| § 30 | polityka transakcji z podmiotami powiązanymi z progami i zgodą dyrektorów niezależnych (dziś „[WYMAGA OPINII PRAWNIKA]”) |
| § 3 ust. 3 / § 28 | polityka „human-in/on-the-loop” przyjęta przez Radę — dokument pokazywany LP z wykluczeniem LAWS (`vc.md` sekcja 7) |
| § 32 ust. 4 lit. d | prawa informacyjne kwartalne i roczne „w granicach przepisów o informacjach niejawnych i kontroli eksportu” |
| § 34 | badanie sprawozdania finansowego niezależnie od progów ustawowych |
| nowy § / umowa akcjonariuszy | przygotowanie do przekształcenia w S.A. przy IPO: akcje założycielskie i uprawnienia indywidualne wygasają (sunset z 3.2), Kryterium zostaje w formie dopuszczalnej na rynku regulowanym **[?]** |

**Zysk.** Największe i najdłuższe pieniądze (NIF: „long term approach”, follow-on). **Koszt.** Najdroższa zgodność; najmniej autonomii; konflikt z 3.2 bez sunsetu.

---

## 4. Zestawienie

| Ścieżka | Kto | Główny § do zmiany | Głosy Założycieli po 1. zdarzeniu | Gotowość dziś |
|---|---|---|---|---|
| 1. VC | ASI, deep tech, NIF | § 16, § 38, seria I | 50–65 % **[W]** | wysoka (1.0-RC) |
| 2. Odporna na VC | aniołowie, rodzinne, obronne | § 5–6 (art. 300²⁶), § 21, § 25 | ≥ ustalony minimalny stosunek | brak |
| 3. Przemysłowa | koncern, integrator, CVC | § 33, § 14, § 16 | bez zmian (kapitał w SPV) | średnia (§ 33) |
| 4. Bootstrap | klienci, przychody | § 21–22, § 25, § 34 | 85–100 % | nadmiar ładu |
| 5. Inkubator | inkubator, uczelnia | emisja za usługi, § 10, § 12 | 90–95 % | średnia (art. 300² § 2) |
| 6. Akcelerator | akcelerator, DIANA, EIC | § 32 (Instrument Zamienny) | 90–95 % po konwersji | średnia (§ 31 ust. 4) |
| 7. Granty | EDF, AGILE, EIC, SMART | § 11 (kontrola UE/EOG), § 21, § 25 | bez zmian | średnia |
| 8. Instytucje | PFR, EIF, NIF, growth | § 21, § 30, polityki | 30–50 % **[W]** | niska |

---

## 5. Matryca zgodności ścieżek

Oznaczenia: **+** zgodne / sekwencja naturalna, **~** zgodne warunkowo, **−** sprzeczne bez kompromisu.

|   | 1 VC | 2 Odp. | 3 Przem. | 4 Boot. | 5 Ink. | 6 Akc. | 7 Granty | 8 Inst. |
|---|---|---|---|---|---|---|---|---|
| **1 VC** | · | − | ~ | ~ | + | + | ~ | + |
| **2 Odporna** | − | · | ~ | + | + | ~ | + | − |
| **3 Przemysłowa** | ~ | ~ | · | + | + | + | + | ~ |
| **4 Bootstrap** | ~ | + | + | · | + | + | + | − |
| **5 Inkubator** | + | + | + | + | · | + | + | + |
| **6 Akcelerator** | + | ~ | + | + | + | · | + | + |
| **7 Granty** | ~ | + | + | + | + | + | · | ~ |
| **8 Instytucje** | + | − | ~ | − | + | + | ~ | · |

**Sprzeczności i kompromisy:**

| Para | Konflikt | Kompromis |
|---|---|---|
| 1/8 ↔ 2 | protective provisions i board seat inwestora vs akcje założycielskie i większość Rady Założycieli | akcje założycielskie z sunsetem (IPO, N lat, odejście Założyciela); inwestor dostaje zgodę serii w sprawach strukturalnych (§ 32 ust. 4 lit. f), Założyciele kontrolę operacyjną |
| 1/8 ↔ 7 | kontrolujący fundusz z USA/UK wyłącza EDF/AGILE | inwestor spoza UE/EOG tylko mniejszościowy, bez weta, dopóki Spółka korzysta z EDF (`regulations.md` 3a, `vc.md` sekcja 7); wybór świadomy przed rundą (D6) |
| 1 ↔ 3 | ROFR strategicznego na Spółkę obniża wycenę wyjścia i odstrasza VC | ROFO zamiast ROFR, wygasa przy serii A; strategiczny w SPV (§ 33), nie w Spółce |
| 4 ↔ 8 | minimalny ład vs instytucjonalny ład | sekwencja: bootstrap teraz, ład instytucjonalny wpisywany przy serii A |
| 2 ↔ 6 | SAFE z MFN i konwersją do serii z protective provisions | konwersja do serii bez prawa weta albo do akcji niemych (art. 300²⁷) |
| 7 ↔ 8 | trwałość projektu i zgody instytucji vs swoboda exitu | zgoda instytucji jako warunek § 16 ust. 2, ograniczona do okresu trwałości |

---

## 6. Rekomendowana architektura i sekwencja

**Sekwencja: 4 → 5/6 + 7 → 3 (przez SPV) → 1 → 8, z modułem 2 jako bezpiecznikiem kontroli.**

1. **Przed zawiązaniem (zmiany w `psa.tex`).**
   - Rdzeń bez zmian (sekcja 2).
   - Moduł grantowy: warunkowe Kryterium kontroli UE/EOG „dopóki beneficjent EDF/AGILE/EUDIS” (3.7) — rozstrzyga D6.
   - Moduł akceleratorowy: definicja Instrumentu Zamiennego w § 32 i wyłączenie prawa poboru dla konwersji w samej umowie (3.6).
   - Decyzja o module odporności: akcje założycielskie z art. 300²⁶ z sunsetem (3.2). To jedyna zmiana, której **nie da się tanio dodać później** — po rundzie wymaga zgody inwestora. Jeżeli Założyciele jej chcą, musi być w umowie od zawiązania.
2. **Pierwsze 12–24 miesiące.** Bootstrap-light w praktyce (Plan Finansowania § 31 ust. 5, pożyczki § 7 ust. 7), DIANA/EIC/SMART, inkubator za usługi (3.5), współpraca przemysłowa wyłącznie przez § 33.
3. **Seria A.** Moduł VC: dopisanie § 16 (drag z ochroną serii, waterfall), § 38 (zgoda serii), ewentualnie seria I z art. 300¹⁰³; reszta w umowie akcjonariuszy (lock-up, non-compete, exit) — zgodnie z `vc.md` sekcja 9.
4. **Seria B i dalej.** Ład instytucjonalny (3.8), sunset akcji założycielskich przy IPO.

**Trzy decyzje dla Założycieli (do dopisania jako D17–D19 w memorandum):**

- **D17.** Czy chcemy akcje założycielskie (art. 300²⁶) z sunsetem — teraz albo nigdy w praktyce.
- **D18.** Czy Kryterium kontroli ma być warunkowo zawężone do UE/EOG (EDF/AGILE) — rozwinięcie D6.
- **D19.** Czy inwestor przemysłowy może wejść do kapitału Spółki-matki, czy wyłącznie do Przedsięwzięć Produkcyjnych (§ 33).

---

## 7. Pytania do kancelarii (nowe, poza `law.md`)

1. Czy akcje założycielskie z art. 300²⁶ KSH można połączyć z mechanizmem zwrotnego zbycia (§ 10) tak, aby akcje odkupione od odchodzącego Założyciela traciły charakter założycielski; czy sunset (termin, IPO) jest dopuszczalny jako postanowienie umowy spółki.
2. Czy w P.S.A. istnieje limit liczby głosów na akcję uprzywilejowaną co do głosu (art. 300²⁵) — odpowiednik art. 352 KSH dla S.A.
3. Czy umowa spółki może z góry określić uprzywilejowanie akcji serii, która zostanie wyemitowana dopiero uchwałą z art. 300¹⁰³ (seria I).
4. Czy wyłączenie prawa poboru w umowie spółki (art. 300¹⁰⁶ § 1) można ograniczyć do emisji konwersyjnych i antyrozwodnieniowych.
5. Czy warunkowe Kryterium („dopóki Spółka jest beneficjentem EDF/AGILE/EUDIS”) jest wystarczająco określone dla rejestru akcjonariuszy i sądu rejestrowego.
6. Czy emisja dla inkubatora za usługi (art. 300² § 2) wymaga wyceny biegłego i jak ująć zwrotne zbycie przy niewykonaniu usług.

---

## 8. Źródła

- KSH, art. 300², 300³, 300²⁵–300²⁸, 300¹⁰³, 300¹⁰⁴, 300¹⁰⁶ — `src/legal/pl_2000_1037_ksh_ujednolicony.txt` (sprawdzone 3 października 2026 r.).
- Rozporządzenie (UE) 2021/697 (EDF), motyw 95 i definicja podmiotu z niestowarzyszonego państwa trzeciego — `src/legal/eu/eu_32021R0697_edf_PL.txt`; art. 9 według `vc.md` sekcja 4 i `regulations.md` sekcja 3.
- NIF — `src/legal/web/web_nif_about.txt`; wymogi programów — `regulations.md` sekcja 3; praktyka VC — `vc.md` sekcje 2–9 i źródła tam wskazane.
- Projekt umowy: `psa.tex` wersja 1.0-RC — § 5, 7, 11 ust. 14–15, 12, 13, 16, 21, 25, 31–34 odczytane bezpośrednio.
