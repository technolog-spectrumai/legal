# Weryfikacja audytów zewnętrznych (ChatGPT): umowa spółki 3.1-S, umowa akcjonariuszy 1.5, umowy IP 1.4

| | |
|----|----------------|
| **Przedmiot** | Trzy audyty: `audyt_psa_v3_1_s.md` (PSA-01–20), `audyt_basilisk_sha_v1_5.md` (SHA-01–17), `audyt_basilisk_ip_v1_4.md` (IP-01–20). |
| **Metoda** | Przepisy, na których opierają się ustalenia, sprawdzono na tekstach ujednoliconych w `src/legal/` (KSH, KC, KRO, Kodeks pracy, PIT, prawo autorskie, PWP, PKD 2025). Ustalenia porównano z treścią dokumentów na gałęzi `dev_1211`. |
| **Data** | 12 listopada 2026 r. |
| **Wynik** | **Audyty są rzetelne.** Każdy sprawdzony przepis ma treść podaną w audycie. Pięć ustaleń wskazuje rzeczywiste błędy w tekście umowy spółki, które przeoczyły nasze audyty (PSA-01, 02, 04, 05, 06). Część pozostałych to trafne ryzyka albo decyzje biznesowe; kilka sygnatur Dziennika Ustaw z 2026 r. nie da się sprawdzić w repozytorium. |

**Oznaczenia werdyktu.** **Trafne** — przepis i wniosek potwierdzone; **Częściowo** — przepis potwierdzony, wniosek przesadzony albo wymaga doprecyzowania; **Decyzja** — trafna uwaga, ale rozwiązanie zależy od wyboru Założycieli; **Niesprawdzalne** — brak tekstu źródła w repozytorium.

---

## 1. Przepisy sprawdzone na tekście

| Przepis | Treść (skrót) | Audyt |
|----|------------|----|
| art. 300⁸⁰ § 2 KSH | Głosowanie elektroniczne — gdy przewiduje je umowa spółki albo wszyscy zgodzą się w formie dokumentowej; **głosowanie na piśmie — tylko za zgodą wszystkich** | PSA-01 trafne |
| art. 300⁹⁰ KSH | Uchwały bez formalnego zwołania, jeżeli **wszystkie akcje są reprezentowane** | PSA-02 trafne |
| art. 300¹⁰⁰ § 4 KSH | Uchwały na piśmie — do księgi protokołów; elektroniczne — wydruki poświadczone podpisem członka zarządu | PSA-03 trafne |
| art. 300¹⁰³ KSH | Emisja bez zmiany umowy, jeżeli umowa przewiduje maksymalną liczbę akcji i **termin ich emisji** | PSA-04 trafne |
| art. 300¹⁰⁶ § 2, 300¹¹⁶ § 2 KSH | Wyłączenie poboru 4/5 głosów; prawa z warunkowej emisji — **dopiero po wpisie** zmiany umowy | PSA-05 trafne |
| art. 300⁴⁰ KSH | Zbycie akcji niepokrytej wymaga zgody spółki do pełnego pokrycia; informacja dla nabywcy; solidarność nabywcy ze zbywcą | PSA-06 trafne |
| art. 300⁹ § 1 KSH | Wkłady wnosi się w ciągu 3 lat od wpisu | PSA-11 trafne |
| art. 300¹²⁵, 300¹³⁴ KSH | Odpowiedzialność wobec spółki; roszczenia akcjonariuszy na zasadach ogólnych | PSA-20 trafne |
| PKD 2025, 30.32.Z | „Produkcja wojskowych statków powietrznych…” — odrębna od 30.31.Z | PSA-19 trafne |
| art. 84 KP | Pracownik nie może zrzec się wynagrodzenia | SHA-01 trafne |
| art. 467 KC | Depozyt sądowy tylko w wypadkach ustawowych | SHA-08 trafne (brak rachunku może mieścić się w pkt 4, ale nie automatycznie) |
| art. 33 pkt 9–10, art. 37 § 1 KRO | Prawa twórcy i przedmioty nabyte w zamian za nie należą do majątku osobistego; art. 37 nie wymienia akcji | SHA-16 trafne — **akcje objęte za aport IP twórcy są co do zasady majątkiem osobistym** |
| art. 22 ust. 1 PWP | Wynagrodzenie twórcy wynalazku, gdy prawo przysługuje zamawiającemu (art. 11 ust. 3), chyba że strony umówiły się inaczej | IP-08 trafne |
| art. 47¹ ust. 1, art. 77 ust. 1, art. 74 ust. 3 pr. aut. | Prawo do **regularnego** otrzymywania informacji; art. 43–44, 47¹ nie dla programów; nabycie programu pracownika — gdy stworzony w wyniku obowiązków ze stosunku pracy | IP-09, IP-15, IP-19 trafne |
| art. 5a pkt 34, art. 17 ust. 1e, art. 24 ust. 12b PIT | Zamknięty katalog komercjalizowanej IP; preferencja programu motywacyjnego w P.S.A. | PSA-16, PSA-17, IP-05 trafne |

Drobna nieścisłość audytu: przy księdze protokołów powołano art. 300⁵² KSH, który dotyczy ustanowienia zarządu albo rady dyrektorów — właściwy jest art. 300¹⁰⁰ § 2–5.

---

## 2. Werdykty — umowa spółki (PSA)

| ID | Werdykt | Komentarz | Priorytet naprawy |
|--|--|------------|--|
| PSA-01 | Trafne | § 12 ust. 1 pozwala zwołującemu wybrać głosowanie „na piśmie”, a ustawa wymaga na to zgody wszystkich akcjonariuszy. Głosowanie e-mailowe przewidziane w umowie jest w porządku | **1** |
| PSA-02 | Trafne | § 12 ust. 4: „cały kapitał akcyjny” → „wszystkie akcje” (PL i EN) | **1** |
| PSA-03 | Trafne | § 12 ust. 8: dodać księgę protokołów i wydruki uchwał elektronicznych | **1** |
| PSA-04 | Trafne | § 5 ust. 3: „uchwał podjętych do 31.12.2036” → termin emisji akcji | **1** |
| PSA-05 | Trafne | § 7 ust. 2: przy warunkowej emisji prawa można przyznać dopiero po wpisie do KRS; rozdzielić tryby | **1** |
| PSA-06 | Trafne | § 8 ust. 5 zwalnia ze zgody zbycia w vestingu; dla akcji niepokrytych (seria F za pracę) zgoda z art. 300⁴⁰ jest ustawowa | **1** |
| PSA-07 | Decyzja | Utrata akcji za aport IP przy złym odejściu przed cliffem — realny problem biznesowy; rozwiązanie: aport poza vestingiem albo automatyczne zwolnienie przy odejściu uzasadnionym w umowie spółki | 2 |
| PSA-08 | Trafne | Brak zaokrągleń i przypisania numerów zwalnianych akcji | 2 |
| PSA-09 | Częściowo | Skuteczność wobec nabywców opiera się na art. 300³⁴ KSH (obowiązki związane z akcją), co audyt pomija; zalecenie pakietu przystąpienia — słuszne | 3 |
| PSA-10 | Decyzja | Brak odmowy zgody wobec konkurenta — świadomy wybór (zamknięta lista przyczyn odmowy) | 3 |
| PSA-11 | Trafne | Wkład pracy serii F musi być wniesiony w 3 lata; vesting 4-letni trzeba od tego oddzielić | 2 |
| PSA-12 | Trafne | Kolejność: umowa spółki, potem cesja aportu (tego samego dnia); faktyczne minimum 1 zł | 2 |
| PSA-13 | Trafne | Osobna umowa background IP; art. 67 ust. 3, art. 68 pr. aut. | 2 |
| PSA-14 | Częściowo | Kworum przy konflikcie i sumowanie progów — usprawnienia, nie błędy | 3 |
| PSA-15 | Trafne | Nabyte akcje A nie stają się seriami F/P | 3 |
| PSA-16, 17 | Trafne | Zgodne z naszymi ustaleniami (art. 17 ust. 1e, art. 24 ust. 12b PIT); wymagają interpretacji | 2 |
| PSA-18 | Częściowo | Do potwierdzenia z księgowym; zapis jest zgodny z art. 3 ust. 1 pkt 9 UoR | 3 |
| PSA-19 | Trafne | Przy produkcji wojskowej potrzebny kod 30.32.Z i koncesja | 3 |
| PSA-20 | Trafne | Po usunięciu fikcji zgody milczenie Rady blokuje sprzedaż bez końca; obietnica odpowiedzialności dyrektorów wobec akcjonariusza jest zbyt mocna (art. 300¹²⁵, 300¹³⁴). Potrzebna ścieżka zastępcza, np. zgoda Walnego Zgromadzenia po bezskutecznym terminie | **1** |

## 3. Werdykty — umowa akcjonariuszy (SHA)

| ID | Werdykt | Komentarz | Priorytet |
|--|--|------------|--|
| SHA-01 | Trafne | § 3 ust. 2 pozwala pracować bez wynagrodzenia także na umowie o pracę — sprzeczne z art. 84 KP. Ograniczyć do nieodpłatnej funkcji dyrektora | **1** |
| SHA-02 | Trafne | § 1 ust. 5: umowa akcjonariuszy nie zastępuje cesji IP — usunąć to odesłanie do § 14 ust. 1 | **1** |
| SHA-03 | Trafne | Ochrona odejścia uzasadnionego to tylko obietnica głosowania; lepiej wpisać automatyczne zwolnienie do § 9 umowy spółki (wiąże się z PSA-07) | **1** |
| SHA-04 | Trafne | Wyjątek „mniej niż 30 dni do terminu” pozwala przenieść akcje w trakcie sporu; zakazać wszystkich czynności wykonawczych w spornym zakresie | **1** |
| SHA-05 | Trafne | Przystąpienie „w zakresie…” bez akceptacji pozostałych stron; kolizja z wyłączeniem uczestników programu P | **1** |
| SHA-06 | Częściowo | Art. 108 KC jest spełniony; zalecenia (ograniczenie substytucji, wygaśnięcie przy utracie funkcji) — rozsądne | 2 |
| SHA-07 | Trafne | Oferta: tabela cen i numerów, przyjęcia częściowe, art. 300⁴⁰ | 2 |
| SHA-08 | Trafne | Zapłata przed wpisem albo depozyt notarialny zamiast depozytu sądowego | 2 |
| SHA-09 | Trafne | Zamknięty katalog zdarzeń, przerwy, urlopy; dane o zdrowiu | 2 |
| SHA-10 | Trafne | Zakaz zatrudniania — ograniczyć do aktywnego nakłaniania; harmonizacja z § 14 ust. 5 umowy spółki | 2 |
| SHA-11 | Trafne | Wyjątek dla sygnalistów i informacji niezależnie wytworzonych | 2 |
| SHA-12 | Częściowo | Czy art. 15 KSH obejmuje pożyczkę **od** dyrektora — sporne; ale § 13 ust. 1 lit. j umowy spółki obejmuje każdą pożyczkę z dyrektorem, więc zgoda WZ i tak jest potrzebna. Dopisać | **1** |
| SHA-13 | Trafne | Katalog postanowień, które przetrwają wygaśnięcie | 2 |
| SHA-14 | Trafne | Uchwała o pełnomocniku musi obejmować całą umowę akcjonariuszy z załącznikami A–D | 2 |
| SHA-15 | Trafne | Drobne: wersja umowy spółki, termin mediacji, aktualizacja adresów, RODO | 3 |
| SHA-16 | Trafne | Nasza zgoda małżonka jest za szeroka: akcje za aport IP są majątkiem osobistym (art. 33 pkt 9–10 KRO); zgoda ma sens tylko przy akcjach z majątku wspólnego. Dodać oświadczenie o przynależności akcji | **1** |
| SHA-17 | Trafne | Zapowiedź przystąpienia małżonka nie jest przystąpieniem | 2 |

## 4. Werdykty — umowy IP

| ID | Werdykt | Komentarz | Priorytet |
|--|--|------------|--|
| IP-01 | Trafne | Umowa nr 1 przenosi prawa autorskie; patenty, know-how, sprzęt i bazy danych potrzebują osobnych modułów | **1** (jeśli takie aporty będą) |
| IP-02 | Trafne | Część B2 dopuszcza prawa nabyte, a Umowa nr 1 każe oświadczyć autorstwo — dodać wariant „nabywca praw” | **1** |
| IP-03 | Trafne | Współtwórcy: odrębne cesje albo umowa wielostronna z udziałami | **1** |
| IP-04 | Częściowo | Warunek z art. 169 KSH jest dopuszczalny; ryzyko dotyczy licencji udzielonych przez spółkę w organizacji — doprecyzować | 3 |
| IP-05 | Trafne | Oświadczenie twórcy tylko dla programu; potrzebne warianty dla patentu i know-how | 2 |
| IP-06 | Trafne | „Twórca” może być spółką — rozdzielić osobę fizyczną i wykonawcę-firmę | **1** |
| IP-07 | Trafne | Zakres zadań musi być konkretny (art. 41 ust. 3) | 2 |
| IP-08 | Trafne | Wynagrodzenie za wynalazki (art. 22 PWP) — wyłączyć albo ustalić | 2 |
| IP-09 | Trafne | Art. 47¹ — informacja regularna, nie tylko na żądanie (utwory inne niż programy) | 2 |
| IP-10 | Trafne | Wydanie prac w toku po zakończeniu współpracy | 2 |
| IP-11 | Trafne | Dane i modele nie zawsze są utworami; baza danych — prawo producenta | 2 |
| IP-12 | Trafne | Komponenty cudze wyłączyć z cesji; licencje open source | 2 |
| IP-13 | Trafne | Umowa background IP (to samo co PSA-13) | 2 |
| IP-14 | Częściowo | Prawa osobiste — doprecyzowanie, nie błąd | 3 |
| IP-15 | Trafne | Zdanie o pracownikach we wprowadzeniu jest zbyt kategoryczne | 3 |
| IP-16 | Trafne | Forma pisemna także dla kwartalnych potwierdzeń; kolejność podpisów tego samego dnia | 2 |
| IP-17, 18 | Trafne | Konta, sekrety, RODO; poufność i sygnaliści | 3 |
| IP-19 | Trafne | Powołanie art. 43 ust. 1 jako podstawy nieodpłatności programu jest nieprecyzyjne (art. 77 ust. 1); trzeba wybrać jeden wariant i poprawić ust. 2 | 2 |
| IP-20 | Trafne | Nieodpłatna cesja może dać spółce przychód z art. 12 ust. 1 pkt 2 CIT — zgodne z naszym wcześniejszym ustaleniem dla licencji | 2 |

---

## 5. Czego nie dało się sprawdzić

Sygnatury aktów z 2026 r. spoza repozytorium: KSH Dz.U. 2026 poz. 1440 (pełnomocnictwo na WZ od 3.12.2026), prawo autorskie poz. 1296 i 1477, Kodeks pracy poz. 1245, CIT poz. 554, VAT poz. 1263, ustawa o zwalczaniu nieuczciwej konkurencji poz. 85, ustawa o bazach danych 2024 poz. 1769. Wnioski audytów nie zależą od nich w istotny sposób, ale przed powołaniem się na te sygnatury trzeba je sprawdzić w Dzienniku Ustaw.

## 6. Rekomendacja

1. **Runda poprawek priorytetu 1** (w obu językach): PSA-01–06, PSA-20, SHA-01–05, SHA-12, SHA-16, IP-02, IP-03, IP-06 (oraz IP-01, jeżeli aportem mają być patenty, know-how lub sprzęt).
2. **Decyzje Założycieli przed rundą:** PSA-07 / SHA-03 (czy akcje za aport IP podlegają vestingowi i co dzieje się przy odejściu uzasadnionym), PSA-20 (kto rozstrzyga, gdy Rada milczy), SHA-10 (zakres zakazu zatrudniania).
3. **Priorytet 2 i 3** — w kolejnej rundzie albo z prawnikiem przed aktem.

---

## 7. Wprowadzone poprawki (gałąź `dev_audit_gpt`, bez decyzji biznesowych)

Wersje: umowa spółki **3.2-S**, umowa akcjonariuszy **1.6**, umowy IP **1.5**; każda poprawka w wersji polskiej i angielskiej.

| Ustalenie | Zmiana | Miejsce |
|--|------|--|
| PSA-01 | Głosowanie elektroniczne według umowy; na piśmie tylko za zgodą wszystkich (art. 300⁸⁰ § 2) | umowa spółki § 12 ust. 1 |
| PSA-02 | „Wszystkie akcje są reprezentowane” (art. 300⁹⁰) | § 12 ust. 4 |
| PSA-03 | Księga protokołów i wydruki uchwał elektronicznych (art. 300¹⁰⁰) | § 12 ust. 8 |
| PSA-04 | 31.12.2036 jako termin emisji; akcje objęte i emisja zgłoszona do tego dnia | § 5 ust. 3 |
| PSA-05 | Prawa z warunkowej emisji dopiero po wpisie; 4/5 przy wyłączeniu poboru | § 7 ust. 2 |
| PSA-06 | Zastrzeżenie art. 300⁴⁰ przy akcjach niepokrytych | § 8 ust. 5 |
| PSA-08 | Wzór liczenia zwolnionych akcji, zaokrąglenie w dół, kolejność numerów | § 9 ust. 2 |
| PSA-11 | Wkład pracą w 3 lata od wpisu emisji, niezależnie od vestingu | § 6 ust. 4 |
| PSA-20 (część prawna) | Odpowiedzialność dyrektorów według przepisów ogólnych zamiast obietnicy wobec akcjonariusza | § 8 ust. 1 |
| SHA-01 | Bez wynagrodzenia tylko funkcja dyrektora; wynagrodzenie ze stosunku pracy nienaruszone | SHA § 3 ust. 2 |
| SHA-02 | SHA nie jest umową przeniesienia IP | § 1 ust. 5 |
| SHA-04 | Wstrzymanie w sporze obejmuje wszystkich pełnomocników i przyjęcie oferty | § 4 ust. 5 |
| SHA-05 | Przystąpienie w całości, przyjmowane przez Spółkę; uczestnicy programu P nabywający Akcje Objęte przystępują | § 2, Załącznik C |
| SHA-08 | Wpis nabywcy po zapłacie; depozyt sądowy tylko z art. 467 KC | § 5 ust. 4 |
| SHA-11 | Wyjątki: sygnaliści, informacje znane wcześniej lub wytworzone niezależnie | § 7 ust. 2 |
| SHA-12 | Pożyczka od dyrektora — także zgoda WZ (§ 13 ust. 1 lit. j umowy spółki) | § 10 ust. 2 |
| SHA-13 | Postanowienia obowiązujące po wygaśnięciu | § 12 ust. 4 (nowy) |
| SHA-14 | Pełnomocnik umocowany do całej umowy z Załącznikami A–D | komparycja |
| SHA-15 | Zmiana adresu nie jest zmianą umowy | § 13 ust. 1–2 |
| SHA-16/17 | Oświadczenie o przynależności akcji (aport IP — majątek osobisty); zgoda tylko dla akcji z majątku wspólnego; zgoda nie jest przystąpieniem | § 13 ust. 7, Załącznik D |
| IP-02 | Wariant „nabywca praw”; prawa od pracodawcy, jeżeli skutecznie nabyte | Umowa nr 1 § 5, Załącznik 1.1 |
| IP-03 | Odrębna umowa każdego współtwórcy; współtwórca spoza Założycieli — osobna umowa z wynagrodzeniem | wstęp, Umowa nr 1 § 1 ust. 4 |
| IP-06 | Twórca = osoba fizyczna (także JDG); wykonawca-firma — odrębna umowa | Umowa nr 2 komparycja, § 1 ust. 3 |
| IP-09 | Informacja z art. 47¹ przekazywana regularnie (utwory niebędące programami) | Umowa nr 2 § 4 ust. 2 |
| IP-10 | Wydanie wszystkich prac i końcowe potwierdzenie w 14 dni | Umowa nr 2 § 7 ust. 3 |
| IP-11 | Dane i modele niebędące utworami; prawo producenta bazy danych | Umowa nr 2 § 1 ust. 1 |
| IP-12 | Komponenty osób trzecich wyłączone z cesji | Umowa nr 1 § 5, Umowa nr 2 § 6 |
| IP-15 | Precyzyjne zdanie o pracownikach (art. 12, 74 ust. 3) | wstęp |
| IP-16 | Forma pisemna albo podpis kwalifikowany dla potwierdzeń kwartalnych | Umowa nr 2 § 5 ust. 1 |
| IP-19 | Podstawa nieodpłatności: art. 43 ust. 1 tylko dla utworów niebędących programami; „godziwe” tylko przy wynagrodzeniu | Umowa nr 2 § 4 ust. 2–3 |

**Pozostające decyzje** zostały rozstrzygnięte w sekcji 8.

**Kontrola techniczna:** umowa spółki (51 stron), umowa akcjonariuszy (30), umowy IP (25) — kompilacja bez błędów, nierozwiązanych odwołań i przepełnionych wierszy: 0.

## 8. Decyzje biznesowe (gałąź `dev_decyzje_1211`)

Wersje: umowa spółki 3.3-S, umowa akcjonariuszy 1.7, umowy IP 1.6. Każda decyzja jest osobnym commitem.

| Nr | Decyzja | Gdzie |
|---|---|---|
| 1 | Vesting Założycieli: 25% w dniu startu, 75% co miesiąc przez 36 mies., cliff 6 mies.; seria F bez zmian (48 mies., cliff 12). Śmierć lub trwała niezdolność — zwolnienie wszystkich akcji; rozwiązanie bez przyczyny lub odejście uzgodnione — akcje z kolejnych 12 mies.; z mocy umowy spółki (PSA-07 / SHA-03) | umowa spółki § 9 ust. 2 i 5; SHA § 1 ust. 2, § 4 ust. 4 |
| 2 | Spółka musi udzielić zgody, jeśli nie ma przyczyny odmowy; gdy Rada milczy (po 14 + 7 dniach) — uchwała akcjonariuszy poza zgromadzeniem w 14 dni; potem powództwo o złożenie oświadczenia (art. 64 KC) (PSA-20) | umowa spółki § 8 ust. 1 |
| 3 | Odmowa dla konkurenta (z wyjątkiem inwestycji portfelowych ≤ 5%); Spółka w 30 dni wskazuje innego nabywcę na tych samych warunkach, inaczej musi udzielić zgody (PSA-10) | umowa spółki § 8 ust. 2 lit. e, ust. 3 |
| 4 | Zakaz konkurencji po wyjściu (12 mies.) tylko przy Odejściu Zwykłym; zakaz nakłaniania przez 12 mies. przy każdym odejściu, tylko aktywne nakłanianie; zakaz konkurencji z umowy spółki ograniczony do okresu zaangażowania lub pełnienia funkcji (SHA-10) | SHA § 8; umowa spółki § 14 ust. 5 |
| 5 | Know-how w Umowie nr 1; sprzęt nie jest aportem (sprzedaż albo użyczenie); wzór dla patentów — gdy będzie potrzebny (IP-01) | umowy IP: wstęp, Umowa nr 1 § 1 ust. 5 |
| 6 | Wynalazki: Założyciele i dyrektorzy — wynagrodzenie zawarte w stosunku podstawowym i udziale (art. 22 ust. 1 PWP); pozostali — 2 000 zł po zgłoszeniu i 5 000 zł po udzieleniu prawa (IP-08) | Umowa nr 2 § 6 ust. 1 |
| 7 | Kary: 25 000 zł (poufność), 50 000 zł (zakaz konkurencji lub nakłaniania), 25 000 zł (§ 5 ust. 6); dodatkowo 5 000 zł za miesiąc naruszenia ciągłego; limit 150 000 zł na Stronę | SHA § 9 ust. 1 |
| 8 | Umowa nr 2: wynagrodzenie w ramach stosunku podstawowego albo nieodpłatnie (dyrektor bez wynagrodzenia, a po przyznaniu wynagrodzenia — zawarte w nim); bez wariantu kwartalnego | Umowa nr 2 § 4 ust. 1 i 3 |

**Kontrola techniczna:** umowa spółki (51 stron), umowa akcjonariuszy (30), umowy IP (25) — 0 błędów, nierozwiązanych odwołań i przepełnionych wierszy.
