# Oczekiwania prawne funduszy VC a projekt umowy P.S.A.

Dokument wewnętrzny Basilisk Systems, informacyjny. Nie jest opinią prawną i nie zmienia umowy spółki. Porządkuje, czego fundusze venture capital zwykle wymagają w dokumentacji prawnej: (1) na świecie, (2) w Polsce, (3) gdy fundusz zagraniczny inwestuje w polską spółkę, oraz (4) jak każde z tych oczekiwań ma się do projektu umowy (`psa.tex`, wersja 0.9.4-C; numery § według `spis_tresci.md`). Uzupełnia pytania 4.4.1–4.4.2 z `law.md`, Dokument dodatkowy nr 5 w `extra.tex` i `emisja/inwestor.md`.

Stan na 30 września 2026 r. Oznaczenia wiarygodności jak w `regulations.md`: **[Z]** sprawdzone w źródle (lista na końcu), **[W]** wiedza ogólna o praktyce rynkowej, do potwierdzenia u kancelarii albo w rozmowie z funduszem, **[?]** hipoteza.

---

## 1. Główny wniosek

Projekt umowy jest bliżej standardu VC niż typowa polska umowa założycielska: ma vesting założycieli, pulę ESOP, tag i drag, prawo pierwszeństwa, standard wyceny, katalog spraw zastrzeżonych i tryb rundy z listą dopuszczalnych warunków inwestorskich (§ 32 ust. 4). Cztery elementy będą przedmiotem negocjacji z każdym funduszem i warto je rozstrzygnąć przed rundą, nie w jej trakcie:

1. **Kryterium Bezpieczeństwa EU/NATO wobec funduszu i jego inwestorów** (§ 11 ust. 6 lit. b: beneficjenci rzeczywiści) — fundusz z inwestorami (LP) spoza UE/EOG/NATO nie spełni Kryterium bez zgody Walnego Zgromadzenia, a przekreślony wyjątek dla funduszy (§ 11 ust. 14) to jedyna furtka. Fundusze obronne i deep tech akceptują ograniczenia właścicielskie, ale nie akceptują badania każdego LP **[W]**.
2. **Swoboda obrotu wtórnego funduszu**: zgoda Spółki na każde rozporządzenie akcją (§ 12), prawo pierwszeństwa (§ 14) i Kryterium przy każdym nabyciu oznaczają, że fundusz nie może bez procedury przenieść akcji do funduszu następcy, spółki celowej albo wydać ich swoim LP przy likwidacji funduszu. Standard rynkowy to „permitted transfers” do podmiotów powiązanych **[W]**.
3. **Prawo weta inwestora**: umowa zna tylko progi 75 % wszystkich głosów (§ 25). Fundusz wymaga listy spraw wymagających jego zgody jako klasy akcji (protective provisions), niezależnie od tego, ile ma głosów **[W]**.
4. **Drag-along 75 % bez ochrony inwestora** (§ 16): fundusz zażąda, aby przymusowe współzbycie wymagało jego zgody, minimalnej ceny albo upływu okresu, oraz aby wypłata szła według waterfall z preferencją likwidacyjną **[W]**.

Reszta różnic to kwestia parametrów (wysokość puli, próg rundy, długość lock-upu), nie konstrukcji.

---

## 2. Standard światowy

Punkt odniesienia to wzorce NVCA (USA) i BVCA (Wielka Brytania), które wyznaczają słownik używany także przez fundusze europejskie. NVCA opublikowała 2 października 2025 r. aktualizację dokumentów wzorcowych, m.in. o mechanikę finansowania w transzach, zapisy dotyczące amerykańskiego programu bezpieczeństwa inwestycji wychodzących i regulacji o danych masowych oraz opcjonalną konwersję akcji uprzywilejowanych inwestora na zwykłe, jeżeli nie sfinansuje kolejnej transzy **[Z]**.

| Klauzula | Typowy standard (seed / seria A) | Uwagi |
|---|---|---|
| Rodzaj akcji | akcje uprzywilejowane (preferred) osobnej serii dla każdej rundy | w USA i UK spółka emituje nową klasę; prawa klasy są w statucie, nie tylko w umowie **[W]** |
| Preferencja likwidacyjna | 1× cena emisyjna, bez udziału (non-participating); przy sprzedaży spółki inwestor wybiera: zwrot 1× albo udział proporcjonalny | wariant founder-friendly to 1× non-participating, wariant inwestorski to participating **[Z]**; „liquidation event” obejmuje sprzedaż spółki i większości aktywów, nie tylko likwidację **[W]** |
| Antyrozwodnienie | broad-based weighted average przy rundzie po niższej wycenie (down round) | full ratchet spotykany w trudnym rynku, uważany za agresywny **[W]** |
| Pro-rata | prawo objęcia proporcjonalnej części kolejnych emisji, często „super pro-rata” dla lidera rundy | wygasa zwykle przy IPO **[W]** |
| ROFR i co-sale | prawo pierwszeństwa spółki, potem inwestorów, przy sprzedaży akcji przez założycieli; prawo przyłączenia inwestorów | dotyczy zbycia przez założycieli, nie przez inwestora **[W]** |
| Drag-along | uruchamiany przez większość akcji uprzywilejowanych (lub inwestorów i zarząd), zwykle z progiem cenowym albo okresem ochronnym; założyciele objęci dragiem | odpowiedzialność mniejszości ograniczona do otrzymanej ceny **[W]** |
| Protective provisions | katalog spraw wymagających zgody większości akcji uprzywilejowanych: zmiana statutu naruszająca prawa serii, nowa seria równa lub wyższa, dług powyżej progu, sprzedaż spółki, zmiana wielkości rady, dywidenda, wykup akcji, transakcje z podmiotami powiązanymi, zmiana ESOP | to kompetencja klasy akcji, nie procent głosów w spółce **[W]** |
| Rada | miejsce w radzie dla lidera rundy (albo obserwator), zwykle rada 3–5 osób: założyciele, inwestor, niezależny | obserwator ma prawa informacyjne bez głosu **[W]** |
| Prawa informacyjne | sprawozdania kwartalne i roczne, budżet, prawo inspekcji, próg „major investor” | **[W]** |
| Vesting założycieli | 4 lata, 1 rok cliff, potem miesięcznie; przyspieszenie „double trigger” (zmiana kontroli + zwolnienie bez przyczyny); część często uznana za nabytą na dzień rundy | reverse vesting: akcje istnieją, ale spółka ma prawo odkupu nienabytych **[W]** |
| Leaver | good leaver: zachowuje nabyte, nienabyte po cenie objęcia; bad leaver: traci nienabyte, nabyte często po niższej z ceny objęcia i wartości rynkowej | definicja „cause” wąska (przestępstwo, umyślne naruszenie) **[W]** |
| ESOP | pula 10–15 % post-money, tworzona przed rundą i wliczona do wyceny pre-money („option pool shuffle”) | fundusz chce, żeby rozwodnienie puli obciążało założycieli **[W]** |
| Własność intelektualna | wszystkie prawa przeniesione na spółkę przed zamknięciem; umowy z pracownikami i kontraktorami; brak „skażonego” kodu | warunek zawieszający closing **[W]** |
| Oświadczenia i zapewnienia | spółki i założycieli (tytuł do IP, brak sporów, cap table, podatki), z limitami odpowiedzialności | **[W]** |
| Zakaz konkurencji i non-solicit | w USA ograniczone prawem stanowym, w Europie standardowe 12–24 miesiące | **[W]** |
| Instrumenty pre-seed | SAFE (YC post-money), pożyczka konwertowalna z cap i dyskontem, MFN | konwersja w kolejnej rundzie kwalifikowanej **[W]** |
| Exit | prawo żądania wyjścia po 5–7 latach (w Europie), redemption rzadko wykonywane, registration rights (tylko USA) | **[W]** |
| Warunki zamknięcia | due diligence prawne, techniczne i finansowe; no-shop 30–60 dni; koszty prawne inwestora do limitu pokrywa spółka | **[W]** |
| Zgodność | KYC/AML inwestora i spółki, sankcje, od 2025 r. w USA także program bezpieczeństwa inwestycji wychodzących (OISP) **[Z]** | dla polskiej spółki dual-use istotne przy inwestorze z USA |

---

## 3. Polska: praktyka rynkowa i wymogi programowe

Polski rynek używa tego samego słownika, ale osadza go w KSH: umowa inwestycyjna (zobowiązaniowa) plus zmiana umowy spółki w formie aktu notarialnego, w której zapisuje się to, co ma działać wobec spółki i osób trzecich (uprzywilejowanie, ograniczenia zbywania, prawa osobiste inwestora, sprawy zastrzeżone). Nie ma jednego standardowego wzoru umowy inwestycyjnej; PFR Ventures publikuje wstępne wzory term sheet dla swoich programów (Starter, Biznest, Otwarte Innowacje, KOFFI, CVC), a Startup Poland prowadzi zbiór standardów rynkowych **[Z]**. Dominującą formą pozostaje sp. z o.o.; P.S.A. jest wybierana coraz częściej przez startupy technologiczne, ale fundusze mają z nią mniej doświadczeń, co przekłada się na dłuższe due diligence i pytania o rejestr akcjonariuszy oraz podatki ESOP **[W]**.

| Obszar | Praktyka w Polsce | Różnica wobec standardu światowego |
|---|---|---|
| Struktura funduszy | większość funduszy działa jako alternatywne spółki inwestycyjne (ASI) z kapitałem PFR, BGK/FENG, EIF; fundusz jest zwykle spółką komandytową albo sp. z o.o. z zarządzającym ASI | inwestor często ma własne wymogi programowe (poniżej) **[W]** |
| Wymogi PFR / FENG | spółka polska („Polish nexus”: siedziba, zespół, działalność w Polsce), status MŚP, brak powiązań kapitałowych fundusz–spółka przed inwestycją, KYC/AML, brak sankcji, ograniczenia dla sektorów wykluczonych, raportowanie do PFR; przy spółce zagranicznej polscy założyciele i limit portfela (`regulations.md` sekcja 3) | warunki w umowie inwestycyjnej jako zobowiązania spółki **[W]** |
| Preferencja likwidacyjna | 1× non-participating jako norma na seed; participating zdarza się przy słabszej pozycji założycieli; w sp. z o.o. realizowana przez uprzywilejowanie udziałów i umowny waterfall przy sprzedaży spółki | w P.S.A. uprzywilejowanie akcji jest elastyczne (prawo głosu, dywidenda, podział majątku) i musi być w umowie spółki **[Z]** |
| Antyrozwodnienie | broad-based weighted average; wykonywane przez emisję dodatkowych akcji dla inwestora po cenie nominalnej / emisyjnej minimalnej | w P.S.A. wymaga uchwały o emisji i 4/5 o prawie poboru, stąd zobowiązania do głosowania **[W]** |
| Vesting | reverse vesting 3–4 lata z cliff 12 miesięcy; wykonanie przez opcję call, ofertę nieodwołalną i pełnomocnictwo; bad leaver z ceną nominalną albo dyskontem 20–50 % | konstrukcja podobna do § 10; wątpliwości co do pełnomocnictw i kar umownych **[W]** |
| Lock-up założycieli | 3–5 lat albo do wyjścia inwestora, z wyjątkami dla przeniesień do spółek osobistych | dłuższy niż 12 miesięcy z § 13 **[W]** |
| Drag-along | próg 50–75 % z udziałem inwestora, często po 3–5 latach i z minimalną wyceną | **[W]** |
| Tag-along | pełny przy zmianie kontroli, proporcjonalny przy mniejszych zbyciach | **[W]** |
| Sprawy zastrzeżone | katalog spraw wymagających zgody inwestora (rada nadzorcza albo zgromadzenie z jego głosem): budżet, zatrudnienie powyżej progu, dług, IP, podmioty powiązane, emisje, zmiana umowy, wypłaty | zwykle w umowie spółki jako uprawnienie osobiste albo wymóg zgody klasy **[W]** |
| Organ nadzoru | rada nadzorcza z członkiem inwestora (sp. z o.o.) albo miejsce w Radzie Dyrektorów (P.S.A.); obserwator | **[W]** |
| ESOP | 5–15 %, częściej 10 %; w sp. z o.o. przez warunkowe podwyższenie kapitału albo opcje rozliczane gotówkowo; w P.S.A. przez upoważnienie do emisji z art. 300¹⁰³ KSH | pytanie o preferencję z art. 24 ust. 11 PIT dla P.S.A. (`extra.tex` Dokument nr 6) **[W]** |
| Zakaz konkurencji | 12–24 miesiące po odejściu, kary umowne; przy umowie o pracę odszkodowanie | **[W]** |
| Kary umowne | częste w polskich umowach inwestycyjnych (naruszenie IP, konkurencji, poufności, obowiązku współdziałania); rzadkie na Zachodzie | **[W]** |
| Exit | zobowiązanie do współdziałania przy wyjściu po 5–7 latach, opcja put wobec założycieli rzadko, prawo do doradcy przy sprzedaży | **[W]** |
| Forma | zmiana umowy spółki u notariusza, wpis w KRS warunkuje powstanie akcji (art. 300¹⁰⁷ § 3 KSH); rachunek escrow do dnia wpisu | closing dwuetapowy **[W]** |
| Podatki | PCC od zmiany umowy w części kapitału akcyjnego, agio; ulga na ASI dla inwestorów indywidualnych | **[W]** |

---

## 4. Fundusze zagraniczne inwestujące w Polsce, w tym fundusze obronne i dual-use

| Oczekiwanie | Treść | Skutek dla Basiliska |
|---|---|---|
| Struktura holdingowa (flip) | fundusze amerykańskie i część brytyjskich wolą spółkę-matkę w Delaware, UK albo Holandii z polską spółką operacyjną; fundusze europejskie i DIANA/NIF akceptują spółkę w państwie NATO/UE | decyzja D1 z `plan_prac.md`; flip po wniesieniu IP ma skutki podatkowe i eksportowe (`psa_todo.md` sekcja 1) **[W]** |
| Dokumentacja po angielsku, wzorce NVCA/BVCA | umowa inwestycyjna po angielsku pod prawem polskim albo pod prawem obcym z polską umową spółki | `psa.tex` po polsku; potrzebne tłumaczenie robocze i „term sheet crosswalk” (Dokument nr 5 w `extra.tex`) **[W]** |
| Akcje uprzywilejowane | odrębna seria z preferencją likwidacyjną i antyrozwodnieniem zapisana w statucie | P.S.A. dopuszcza; wymaga zmiany umowy spółki w akcie notarialnym (`emisja/inwestor.md` sekcja 5) **[Z]** |
| Kontrola inwestycji (FDI) | inwestor spoza UE w spółce z technologią dual-use sprawdza ustawę o kontroli niektórych inwestycji i oczekuje warunku zawieszającego | § 12 ust. 2 lit. e przewiduje wstrzymanie terminu; w rundzie potrzebny warunek zawieszający w umowie inwestycyjnej **[W]** |
| Sankcje, KYC, kontrola eksportu | fundusz z USA wymaga zgodności z EAR/ITAR i OISP; fundusze europejskie z 2021/821 | § 28 i program zgodności; klasyfikacja produktów przed data room (bramka G2 w `regulations.md`) **[Z/W]** |
| Fundusze obronne (NIF, Expeditions, Balnord, fundusze EDF/EUDIS) | NATO Innovation Fund: fundusz wspierany przez 24 państwa NATO, bilety do 15 mln EUR, inwestuje w AI, autonomię i inne technologie; oczekuje siedziby i własności w państwach NATO **[Z]**; fundusze z kapitałem EDF/EUDIS wymagają braku kontroli przez państwo niestowarzyszone (art. 9 rozporządzenia 2021/697, `regulations.md` sekcja 3) | Kryterium § 11 jest zgodne z tymi wymogami co do kierunku; kolizja tylko przy kontroli przez podmiot z NATO spoza UE (D6) **[W]** |
| Inwestorzy funduszu (LP) spoza Kryterium | fundusz ma LP z Szwajcarii, Izraela, Singapuru, Japonii, Korei, Australii, Zatoki; żaden z tych krajów nie jest w UE/EOG/NATO; fundusz nie ujawni pełnej listy LP i nie zgodzi się na ich indywidualną weryfikację | bez § 11 ust. 14 każdy taki fundusz potrzebuje zgody WZ 75 %; standard obronny to test na poziomie zarządzającego i kontroli, nie każdego LP **[W]** |
| Swoboda przeniesień w grupie funduszu | przeniesienie akcji do funduszu kontynuacyjnego, spółki celowej, następcy zarządzającego, wydanie akcji LP przy likwidacji funduszu bez zgody spółki i bez prawa pierwszeństwa | § 12–14 nie znają „permitted transferee” dla inwestora **[W]** |
| Rada i obserwator | członek rady wskazany przez fundusz może być obywatelem państwa spoza UE/NATO (np. partner ze Szwajcarii) | § 21 ust. 3 wyklucza taką osobę; obserwator dopuszczalny **[W]** |
| Prawo właściwe i spory | fundusze zagraniczne wolą arbitraż (np. SCC, LCIA) dla umowy inwestycyjnej; umowa spółki zawsze pod prawem polskim | § 38 ust. 4: sąd siedziby Spółki; arbitraż możliwy w umowie inwestycyjnej i akcjonariuszy **[W]** |
| Wycena i waluta | inwestycja w EUR/USD, cena emisyjna w PLN; ryzyko kursowe do zamknięcia | rachunek escrow, klauzula przeliczenia **[W]** |

---

## 5. Mapowanie oczekiwań na projekt umowy

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
| Antyrozwodnienie BBWA | § 32 ust. 4 lit. b | OK | mechanika emisji dodatkowych akcji wymaga uchwał 75 % i 4/5; zobowiązanie do głosowania z § 32 ust. 3 (pytanie 3.3.1) |
| Zobowiązanie do głosowania za rundą | § 32 ust. 3 | CZ | skuteczność wobec akcjonariuszy do potwierdzenia; fundusz zażąda tego samego w umowie akcjonariuszy z karą umowną **[W]** |
| Instrumenty zamienne (SAFE, pożyczka) | § 31 ust. 4 | OK | uchwała 75 % jako Sprawa Zastrzeżona; konwersja to emisja z prawem poboru do wyłączenia (`emisja/inwestor.md` sekcja 4) |
| Zakaz finansowania przez podmioty spoza Kryterium | § 31 ust. 3 | CZ | fundusze akceptują; banki i leasingodawcy spoza UE/NATO są rzadkością; venture debt z USA wymaga wyjątku **[W]** |
| Zakaz konkurencji założycieli | § 29 ust. 1–3 | CZ | po odejściu tylko na podstawie odrębnej umowy (umowa akcjonariuszy § Zakaz konkurencji); fundusz oczekuje 12–24 miesięcy i kar umownych |
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

## 6. Zalecenia: przed rundą i w rundzie

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

## 7. Co fundusz sprawdzi w due diligence i gdzie to jest w repozytorium

| Pytanie inwestora | Dokument |
|---|---|
| Kto ma jakie akcje, po jakiej cenie, za jaki wkład | `psa.tex` § 5–7, Załącznik nr 1 |
| Czy IP należy do spółki | § 26, umowy przeniesienia praw (do przygotowania), Załącznik nr 3 (licencje OSS, prawa osób trzecich) |
| Czy założyciele mają vesting i jak jest wykonywany | § 10, Załącznik nr 2, umowa wykonawcza (`shareholder_agreement.tex`) |
| Kto może kupić akcje i jak wychodzi inwestor | § 11–16, `vc.md` sekcja 5 |
| Jak spółka podejmuje decyzje | § 21–25, `extra.tex` Dokument nr 3, regulamin Rady (do przygotowania) |
| Zgodność eksportowa i sankcyjna, klasyfikacja produktów | § 27–28, `regulations.md`, program zgodności (do przygotowania) |
| Podatki ESOP i aportu | `extra.tex` Dokument nr 6, interpretacja indywidualna (pkt 27) |
| Zakaz konkurencji i inne aktywności założycieli | § 29, Załącznik nr 3, umowa akcjonariuszy |
| Umowy z pracownikami i B2B | do przygotowania (`psa_todo.md` sekcja 4) |

---

## 8. Źródła sprawdzone 30 września 2026 r.

- NVCA, aktualizacja dokumentów wzorcowych z 2 października 2025 r.: https://nvca.org/press_releases/nvca-releases-2025-updates-to-model-legal-documents/ ; omówienia: https://natlawreview.com/article/breaking-down-october-2-2025-nvca-updates-model-legal-documents-what-founders-and ; https://www.foley.com/insights/publications/2025/10/breaking-down-the-nvca-what-founders-and-vcs-need-to-know/
- Preferencja likwidacyjna, standard 1× non-participating: https://www.hustlefund.vc/post/angel-squad-liquidation-preference-the-term-sheet-clause-that-actually-matters ; https://www.morse.law/news/liquidation-preference/
- PFR Ventures o umowie inwestycyjnej i term sheet: https://startup.pfr.pl/artykul/prawo-w-umowie-z-vc-umowa-inwestycyjna ; https://startup.pfr.pl/artykul/jak-wyglada-umowa-inwestycyjna-z-vc ; wzory term sheet dla programów PFR: https://pfrventures.pl/dokumentacja-programow-opartych-o-feng
- Standardy Startup Poland, term sheet: https://standardy.startuppoland.org/wiedza/przed-inwestycja/term-sheet/
- Uprzywilejowanie akcji w P.S.A.: https://www.biznes.gov.pl/pl/portal/00168 ; https://prosta-spolka.pl/uprzywilejowanie-akcji-w-prostej-spolce-akcyjnej/ ; https://emiteo.pl/blog/post/akcje-uprzywilejowane-psa/
- NATO Innovation Fund: https://www.nif.fund/about/ ; raport NIF o stanie startupów obronnych w Europie (2026): https://www.nif.fund/wp-content/uploads/2026/02/NIF-report-Defence-Security-and-Resilience-2026-A4-size-25mm-margin-V2.pdf ; przegląd europejskich inwestorów obronnych: https://www.eu-startups.com/2026/09/the-21-european-investors-funding-natos-defence/
- Strony startup.pfr.pl, standardy.startuppoland.org i foley.com były w tej sesji niedostępne do pełnego odczytu (blokada sieciowa); tezy oparte na ich streszczeniach z wyszukiwarki oznaczono [Z] tylko tam, gdzie streszczenie było jednoznaczne.
