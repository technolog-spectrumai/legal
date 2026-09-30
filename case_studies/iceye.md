# Case study: ICEYE — od projektu studenckiego do dekakorna z kontraktami rządowymi

Dokument wewnętrzny Basilisk Systems, informacyjny. Nie jest opinią prawną ani rekomendacją inwestycyjną i nie zmienia umowy spółki. Jedno ze studiów przypadku o rozwoju i finansowaniu firm obronnych, robotyki i fizycznego AI (przegląd i porównanie: `case_studies/README.md`). Opisuje, jak fińsko-polska firma satelitarna przeszła w dwanaście lat od projektu na Uniwersytecie Aalto do wyceny 10,5 mld EUR, jakie kolejne źródła kapitału finansowały ją na każdym etapie i jaką rolę odegrały państwo, koncerny i kontrakty rządowe. Odesłania do umowy według `psa.tex` w wersji 0.9.4-C (numery § według `spis_tresci.md`); uzupełnia `vc.md` (oczekiwania funduszy), `regulations.md` sekcje 3 i 3b oraz `psa_todo.md` sekcje 1 i 6.

Stan na 30 września 2026 r. Oznaczenia wiarygodności: **[Z]** — fakt z dokumentu pierwotnego (komunikat spółki, inwestora, uczelni, agencji państwowej albo zamawiającego); **[M]** — doniesienie prasowe albo baza danych; **[W]** — wiedza ogólna o prawie albo praktyce rynkowej, do potwierdzenia u kancelarii; **[?]** — szacunek, w tym własne obliczenie z cytowanych liczb, albo teza niepotwierdzona. Uwaga metodyczna: w tej sesji strony źródłowe (iceye.com, spacenews.com, bloomberg.com, rp.pl, space24.pl i inne) były niedostępne do pełnego odczytu z powodu blokady sieciowej; fakty pochodzą ze streszczeń wyszukiwarki, a **[Z]** przyznano tylko tam, gdzie streszczenie dokumentu pierwotnego było jednoznaczne. Wyceny sprzed grudnia 2025 r. nie były publikowane.

---

## 1. Główny wniosek

1. **Dwanaście lat, osiem rund, ok. 1,2 mld USD kapitału pierwotnego.** ICEYE zaczęło się jako projekt studencki na Aalto (2012), zawiązano je w 2014 r., pierwszego satelitę wystrzeliło w styczniu 2018 r., a w czerwcu 2026 r. pozyskało 450 mln EUR od General Atlantic przy wycenie 10,5 mld EUR (ponad 1 mld EUR z odsprzedażą akcji przez dotychczasowych akcjonariuszy) **[Z]**. Granty i pożyczki państwowe to ok. 83 mln EUR, czyli ok. 7 % kapitału, ale decydujące w latach 2013–2018 **[?]**.
2. **Drabina finansowania miała pięć szczebli**, każdy z innym rodzajem inwestora: (1) uczelnia, Tekes i Horyzont 2020 na prototyp; (2) amerykańskie VC (True Ventures, Draper) na pierwsze starty; (3) fińskie państwo (Tesi od 2018 r., Solidium od 2024 r.) i koncerny-klienci (BAE Systems, Kajima, Tokio Marine, Nokia, Rheinmetall) jako kapitał cierpliwy; (4) kontrakty rządowe na całe satelity (Brazylia 2020, Polska, Finlandia, Holandia, Portugalia, Grecja, Niemcy, Szwecja, Japonia 2025–2026), które dały rentowność; (5) globalny growth equity (General Catalyst, General Atlantic, TCV, QIA) i unijny Scaleup Europe Fund, gdy firma była już rentowna **[Z]/[?]**.
3. **Punktem przegięcia była sprzedaż satelitów państwom, nie danych:** przychody ICEYE Oy stały na ok. 120 mln EUR w 2023–2024 r. ze stratą operacyjną 35 mln EUR w 2024 r.; w 2025 r. grupa miała ponad 250 mln EUR przychodów, ponad 100 mln EUR EBITDA, ponad 130 mln EUR przepływów operacyjnych i portfel 1,5 mld EUR; cel na 2027 r. to ponad 1 mld EUR **[Z]/[M]**.
4. **IPO rozważano i odłożono:** rozmowy z bankami w czerwcu 2025 r., w grudniu 2025 r. prezes: „nie ma takiego planu", Nasdaq niewykluczony; runda F została opisana jako budowa mocy, nie przygotowanie do giełdy; ponad 550 mln EUR odsprzedaży w rundzie F zdjęło presję na płynność **[M]**. O Warszawie nikt nie mówi.
5. **Wątek polski jest realny, nie tylko wizerunkowy:** współzałożyciel z Politechniki Warszawskiej, polskie VC (OTB Ventures) od serii B, ICEYE Polska od 2017 r. (dziś ponad 150 osób, centrum operacyjne sterujące całą konstelacją w Warszawie od 25 września 2026 r.), państwo polskie jako akcjonariusz (Vinci z grupy BGK, sierpień 2025 r.) i klient (MikroSAR, 860 mln zł brutto) **[Z]/[M]**. Odpowiedź założyciela na pytanie „dlaczego Finlandia": przypadek (Erasmus), lepiej finansowany projekt uczelniany i wsparcie „na zasadach grantowych" **[M]**.
6. **Dla Basiliska:** ICEYE to wzorzec firmy kapitałochłonnej zbudowanej w UE z inwestorami państwowymi (spełniają Kryterium § 11) i z partnerami przemysłowymi w JV (Rheinmetall 60/40: § 33). Pokazuje jednak także, że na etapie growth pojawiają się inwestorzy spoza UE/NATO (Kajima, IHI, QIA), których Kryterium bez uchwały WZ nie przepuści, i że horyzont do rentowności w sprzęcie to 10 lat. Mapowanie w sekcji 10.

---

## 2. Profil

| Element | ICEYE | Wiar. |
|---|---|---|
| Założenie | projekt na Uniwersytecie Aalto od 2012 r.; ICEYE Oy zawiązana w 2014 r. (Y-tunnus 2639822-1), działalność od 2015 r.; Espoo | [Z] |
| Założyciele | Rafał Modrzewski (Politechnika Warszawska, na Aalto od 2010 r. przez Erasmus; CEO) i Pekka Laurila | [Z]/[M] |
| Produkt | mikrosatelity radarowe SAR (poniżej 100 kg; rozdzielczość do 25 cm w najnowszych); zobrazowania i subskrypcje danych; analityka dla ubezpieczycieli (Flood, Wildfire, Hurricane Insights); od 2020 r. sprzedaż całych systemów satelitarnych państwom | [Z] |
| Konstelacja | ICEYE-X1 w styczniu 2018 r.; 16 na orbicie w lutym 2022 r.; 38 wystrzelonych do końca 2024 r.; 22 starty w 2025 r. (62 łącznie); 76 do lipca 2026 r.; produkcja ok. 50 rocznie w 2026 r., cel 100 rocznie do 2027–2028 r. | [Z]/[M] |
| Zespół | 296 osób w ICEYE Oy (2023), 359 (2024); grupa: ponad 900 (2025), ponad 1000 z 45 krajów (2026), w tym ponad 150 w Polsce | [M] |
| Biura i produkcja | Espoo; Warszawa (od 2017 r.; od 2026 r. Centrum Technologii Satelitarnych z czystym pomieszczeniem 500 m²); Irvine (USA, satelity na licencji amerykańskiej); Ateny (linia produkcyjna od 2025 r.); Neuss (JV z Rheinmetall, produkcja od III kw. 2026 r.); Japonia (montaż u IHI od 2026 r.); biura w UK, Hiszpanii, Holandii i innych | [Z]/[M] |
| Właściciele | ponad 50 inwestorów; po rundzie F: Solidium ok. 6 %, Tesi ok. 7 % (państwo fińskie łącznie ok. 12 %), fińscy inwestorzy instytucjonalni ok. 17 %; udziały założycieli nieujawnione | [Z]/[?] |
| Wycena | 2,4 mld EUR (grudzień 2025 r.) → 10,5 mld EUR (czerwiec 2026 r.); trzeci fiński dekakorn po Supercell i Oura | [Z] |

---

## 3. Jak zaczęli: kapitał początkowy i pierwsze lata

**Skąd wziął się pomysł i pierwsze pieniądze (2010–2015)**

- 2010 r.: Modrzewski przyjeżdża na Aalto z Politechniki Warszawskiej na wymianę Erasmus i trafia do uczelnianego programu satelitarnego (nanosatelita Aalto-1) **[M]**. Jego relacja: wybór Finlandii był „nieco losowy", ale „dziesięć lat temu fiński uniwersytet miał po prostu więcej pieniędzy": projekt studencki miał budżet ok. 0,5 mln EUR, a pierwszy grant, 50 tys. EUR, dała uczelnia **[M]**.
- 2012 r.: ICEYE rusza jako projekt zaliczeniowy w Katedrze Radionauki i Inżynierii Aalto; założyciele: Modrzewski i Pekka Laurila **[Z]**.
- 2013–2014 r.: prototyp technologii sfinansowany z programu TUTLI fińskiej agencji Tekes (dziś Business Finland), który wspiera komercjalizację badań uczelnianych; spółka zawiązana w 2014 r., działalność operacyjna od 2015 r. **[Z]**.
- 2015 r.: trzy źródła naraz, zanim spółka miała cokolwiek na orbicie: (1) 2,5 mln EUR (2,8 mln USD) od True Ventures i Founder.org (USA) oraz Lifeline Ventures (Finlandia), listopad 2015 r.; (2) pożyczka rozwojowa Tekes 1,7 mln EUR z programu Arctic Seas; (3) grant 2,4 mln EUR z instrumentu MŚP Horyzontu 2020 od 1 września 2015 r., z celem wprost zapisanym w komunikacie: „zintegrować, przetestować i zademonstrować system SAR w formie mikrosatelity, aby przyciągnąć prywatne inwestycje na start" **[Z]**. Pierwszy start planowano na 2017 r.

**Jak doszli do pierwszego satelity i pierwszych klientów (2017–2020)**

- Sierpień 2017 r.: 13 mln USD, w tym 8,5 mln USD kapitału od Draper Nexus, True Ventures, Lifeline, Space Angels i Draper Associates (reszta najpewniej pożyczki i granty) **[Z]/[?]**. Październik 2017 r.: rejestracja ICEYE Polska Sp. z o.o. w Warszawie **[Z]**.
- Styczeń 2018 r.: ICEYE-X1, pierwszy na świecie mikrosatelita SAR poniżej 100 kg i pierwszy fiński satelita komercyjny; grudzień 2018 r.: X2 **[Z]**. Maj 2018 r.: seria B 34 mln USD (True Ventures; wchodzą Seraphim, Promus, OTB Ventures z Warszawy i państwowe Tesi) z zapowiedzią dziewięciu startów do końca 2019 r.; grudzień 2018 r.: pożyczka kapitałowa Business Finland 10 mln EUR na produkcję satelitów **[Z]**.
- 2020 r.: seria C 87 mln USD (True Ventures, duży udział OTB) i pierwszy klient na cały system: Siły Powietrzne Brazylii, dwa satelity (grudzień 2020 r.); 2021 r.: partnerstwo ze Swiss Re i status misji wspierającej Copernicus (dane bezpłatne dla instytucji publicznych UE) **[Z]/[M]**.

**Co z tego wynika**

- Kapitał początkowy był publiczny i uczelniany: 50 tys. EUR grantu uczelni, budżet projektu 0,5 mln EUR, TUTLI, potem 1,7 mln EUR pożyczki i 2,4 mln EUR grantu UE. Prywatne VC weszło dopiero, gdy istniał prototyp i grant unijny, i to na kwotę mniejszą niż suma grantów **[?]**.
- Pierwsze trzy lata po zawiązaniu (2015–2017) to ok. 16 mln USD kapitału łącznie przy zerowych przychodach; sześć lat od zawiązania do pierwszej sprzedaży całego systemu (2020) i jedenaście do rentowności (2025).
- Założyciel podkreśla, że fińskie wsparcie „działa na zasadach grantowych" i że do rozwoju startupów „potrzebne jest zaufanie społeczne"; to bezpośredni argument w pytaniu o jurysdykcję z `psa_todo.md` sekcja 1 **[M]**.

---

## 4. Oś czasu

| Data | Zdarzenie | Kwota / szczegół | Wiar. |
|---|---|---|---|
| 2012 | projekt na Aalto (Modrzewski, Laurila) | budżet projektu ok. 0,5 mln EUR; grant uczelni 50 tys. EUR | [Z]/[M] |
| 2013–2014 | prototyp z Tekes TUTLI; zawiązanie ICEYE Oy | — | [Z] |
| 1 września 2015 | grant Horyzont 2020 (instrument MŚP) | 2,4 mln EUR | [Z] |
| listopad 2015 | pierwsza runda (True Ventures, Founder.org, Lifeline) i pożyczka Tekes | 2,5 mln EUR + 1,7 mln EUR | [Z] |
| 23 sierpnia 2017 | finansowanie 13 mln USD, w tym 8,5 mln USD kapitału (lider Draper Nexus) | — | [Z] |
| 19 października 2017 | rejestracja ICEYE Polska Sp. z o.o. (KRS 700126) | — | [Z] |
| styczeń 2018 | start ICEYE-X1 | — | [Z] |
| maj 2018 | seria B (True Ventures; Seraphim, Draper, Promus, OTB, Tesi) | 34 mln USD; łącznie 53 mln USD | [Z] |
| 14 grudnia 2018 | pożyczka kapitałowa Business Finland | 10 mln EUR | [Z] |
| 22 września 2020 | seria C (True Ventures; OTB „znaczący"; Tesi, DNX, Seraphim, Promus, Luxembourg Future Fund i inni) | 87 mln USD; łącznie 152 mln USD | [Z] |
| grudzień 2020 | Brazylia (FAB): dwa satelity, pierwszy klient na cały system | — | [M] |
| 12 października 2021 | misja wspierająca Copernicus (ESA) | — | [Z] |
| 3 lutego 2022 | seria D (Seraphim; BAE Systems, Kajima, Molten, OTB, True, UK NSSIF i inni) | 136 mln USD; łącznie 304 mln USD | [Z] |
| 18 sierpnia 2022 | Fundacja Serhija Prytuły kupuje dla Ukrainy dostęp do satelity i konstelacji („satelita ludowy") | ok. 16 mln USD | [M] |
| wrzesień 2023 | MSPO: porozumienie PGZ, WZŁ-1 i ICEYE Polska o polskiej konstelacji radarowej | — | [M] |
| 17–24 kwietnia 2024 | runda wzrostowa, lider Solidium (miejsce w radzie) | 93 mln USD; łącznie 438 mln USD | [Z]/[M] |
| 11–12 listopada 2024 | umowa strategiczna z MO Ukrainy (bezpośrednie tasking-i); Rheinmetall i ICEYE dostarczają zobrazowania | — | [Z] |
| 18 grudnia 2024 | rozszerzenie rundy (dług i kapitał; Solidium, fundusze BlackRock, Seraphim) | 65 mln USD; 158 mln USD w 2024 r.; ponad 500 mln USD od założenia | [Z] |
| 28 marca 2025 | umowa na dane SAR dla Centrum Sytuacyjnego NATO; potem APSS | — | [Z] |
| 8 maja 2025 | początek współpracy z Rheinmetall | — | [Z] |
| 14 maja 2025 | Polska: MikroSAR, konsorcjum ICEYE Polska (lider) i WZŁ-1: 3 satelity + segment naziemny, opcja na 3 kolejne | 860 mln zł brutto | [Z] |
| maj 2025 | biuro i linia produkcyjna w Atenach (dwa satelity dla Grecji); MoU z IHI (Japonia) | — | [Z] |
| czerwiec 2025 | program inwestycyjny ponad 250 mln EUR; Business Finland: 5,7 mln EUR grantów + 35,4 mln EUR pożyczek (później grant 28,3 mln EUR); Portugalia: pierwszy satelita; Holandia: 4 satelity; Bloomberg: rozmowy z bankami o IPO | 41,1 mln EUR | [Z]/[M] |
| 25 sierpnia 2025 | Vinci SA (grupa BGK) obejmuje udziały | ponad 40 mln zł | [M]/[Z] |
| 8 września 2025 | Finlandia: Siły Obronne kupują 3 satelity | ok. 158 mln EUR netto | [Z] |
| październik 2025 | IHI: 4 satelity + opcja na 20; montaż w Japonii | — | [Z] |
| 7 listopada 2025 | JV Rheinmetall ICEYE Space Solutions GmbH (60/40), Neuss | — | [Z] |
| 28 listopada 2025 | start pierwszego polskiego satelity wojskowego i obu greckich | — | [M] |
| 5–8 grudnia 2025 | seria E (General Catalyst; A.P. Moller, Bpifrance, Vinci/BGK, Solidium, Tesi, fińskie fundusze emerytalne i inni) | 150 mln EUR + 50 mln EUR odsprzedaży; wycena 2,4 mld EUR | [Z]/[M] |
| 18 grudnia 2025 | Niemcy: SPOCK 1 dla JV z Rheinmetall (dostęp do konstelacji do końca 2030 r.) | 1,7 mld EUR | [Z] |
| koniec 2025 | wyniki 2025: przychody ponad 250 mln EUR, EBITDA ponad 100 mln EUR, gotówka ponad 350 mln EUR, portfel 1,5 mld EUR | — | [Z] |
| 12 stycznia 2026 | Szwecja (FMV): satelity i systemy naziemne | część pakietu 1,3 mld SEK (z Planet) | [Z] |
| marzec 2026 | 6 startów (X-71 do X-76), w tym dwa polskie; Bloomberg: cel 1 mld EUR przychodów w 2027 r. | — | [M] |
| 5 maja 2026 | Bloomberg: rozmowy o ok. 250 mln EUR przy ok. 5 mld EUR | — | [M] |
| 9 czerwca 2026 | seria F (General Atlantic; Nokia, QIA, TCV, Solidium, Tesi, Varma, Ilmarinen, Lifeline) | 450 mln EUR + ponad 550 mln EUR odsprzedaży; wycena 10,5 mld EUR | [Z] |
| czerwiec 2026 | Portugalia zamawia 2 kolejne satelity (łącznie 4) | — | [M] |
| 5 sierpnia 2026 | Scaleup Europe Fund (EQT; Komisja Europejska inwestorem założycielskim) współliderem serii F, pierwsza inwestycja funduszu | — | [Z] |
| sierpień 2026 | ICEYE US: kontrakt NRO w programie Radar Commercial Augmentation | — | [Z] |
| wrzesień 2026 | MSPO: list intencyjny ICEYE–PGZ o wojskowym systemie łączności satelitarnej | — | [M] |
| 25 września 2026 | Centrum Technologii Satelitarnych w Warszawie: 3200 m², centrum operacyjne całej konstelacji, czyste pomieszczenie 500 m²; inwestycje 2026–2028 | ponad 120 mln zł | [M] |

---

## 5. Finansowanie: runda po rundzie

| Data | Runda | Kwota | Lider | Wybrani uczestnicy | Wycena | Wiar. |
|---|---|---|---|---|---|---|
| 2012–2014 | uczelnia, Tekes TUTLI | 50 tys. EUR grantu; budżet projektu 0,5 mln EUR; TUTLI b.d. | Aalto, Tekes | — | — | [M]/[Z] |
| 2015 | grant H2020 + pożyczka Tekes | 2,4 mln EUR + 1,7 mln EUR | UE, Tekes | — | — | [Z] |
| listopad 2015 | seed / „seria A" | 2,5 mln EUR (2,8 mln USD) | True Ventures | Founder.org, Lifeline Ventures | b.d. | [Z] |
| sierpień 2017 | rozszerzenie A | 13 mln USD (8,5 mln USD kapitału) | Draper Nexus | True, Lifeline, Space Angels, Draper Associates | b.d. | [Z] |
| maj 2018 | seria B | 34 mln USD | True Ventures | Seraphim, Draper Esprit, Promus, OTB Ventures, Tesi | b.d. (łącznie 53 mln USD) | [Z] |
| grudzień 2018 | pożyczka kapitałowa | 10 mln EUR | Business Finland | — | — | [Z] |
| wrzesień 2020 | seria C | 87 mln USD | True Ventures | OTB (duży udział), Tesi, DNX, Seraphim, Promus, Space Angels, New Space Capital, Luxembourg Future Fund | b.d. (łącznie 152 mln USD) | [Z] |
| luty 2022 | seria D | 136 mln USD | Seraphim Space | BAE Systems, Kajima Ventures, Molten, OTB, True, UK NSSIF, Space Capital, Promus i inni | b.d. (łącznie 304 mln USD; „jednorożec" w polskiej prasie) | [Z]/[M] |
| kwiecień 2024 | runda wzrostowa | 93 mln USD | Solidium Oy (państwo fińskie; miejsce w radzie) | Move Capital, Blackwells Capital, Christo Georgiev, dotychczasowi | b.d. (łącznie 438 mln USD) | [Z]/[M] |
| grudzień 2024 | rozszerzenie (dług i kapitał) | 65 mln USD | — | Solidium, fundusze BlackRock, Seraphim, Plio, Georgiev | b.d. (ponad 500 mln USD od założenia) | [Z] |
| czerwiec 2025 | granty i pożyczki | 41,1 mln EUR (5,7 grant + 35,4 pożyczki); potem grant 28,3 mln EUR | Business Finland | — | — | [Z] |
| sierpień 2025 | udziały dla państwa polskiego | ponad 40 mln zł | Vinci SA (BGK) | — | b.d. | [M] |
| grudzień 2025 | seria E | 150 mln EUR + 50 mln EUR odsprzedaży | General Catalyst | A.P. Moller Holding, Bpifrance, Vinci/BGK, RiO Family Office, Solidium, Tesi, Ilmarinen, Keva, Varma, Lifeline, Peter Sarlin | 2,4 mld EUR | [Z]/[M] |
| czerwiec–sierpień 2026 | seria F | 450 mln EUR + ponad 550 mln EUR odsprzedaży | General Atlantic; współlider Scaleup Europe Fund (EQT) | Nokia, QIA, TCV, Solidium (ok. 77 mln EUR w rundzie), Tesi, Varma, Ilmarinen, Lifeline | 10,5 mld EUR | [Z] |
| **Razem** | | **ok. 1,13–1,2 mld USD kapitału pierwotnego** (bazy: 1,1–1,25 mld USD); **ok. 83 mln EUR grantów i pożyczek państwowych**; **ok. 600 mln EUR odsprzedaży** w 2025–2026 r. | | | | [?] |

Cztery obserwacje **[?]**:

- Wycen nie ujawniano przez dziesięć lat; skok z 2,4 mld EUR (grudzień 2025 r.) do 10,5 mld EUR (czerwiec 2026 r.) w sześć miesięcy nastąpił po ogłoszeniu wyników za 2025 r. i kontraktu niemieckiego.
- Inwestorzy strategiczni byli zarazem klientami: BAE Systems i Kajima (seria D), Tokio Marine (użytkownik Flood Insights), Nokia (seria F), Rheinmetall (JV). Państwo fińskie weszło przez Tesi (2018) i Solidium (2024) i zwiększało udział w każdej kolejnej rundzie; państwo polskie przez Vinci (2025).
- Prezes o serii E: rentowność w 2025 r. sprawiła, że runda „nie była ściśle konieczna", ale pozwala szybciej wystrzeliwać satelity dla europejskich zdolności wojskowych **[M]**. Odsprzedaż ponad 550 mln EUR w serii F dała płynność wczesnym inwestorom i pracownikom bez giełdy.
- Dług ograniczał się do pożyczek Business Finland i części rozszerzenia z grudnia 2024 r.; nie znaleziono pożyczki EBI ani kredytów bankowych.

---

## 6. Rynek publiczny: rozważane i odłożone IPO

| Data | Kto | Co | Wiar. |
|---|---|---|---|
| 23 czerwca 2025 | Bloomberg | ICEYE „rozmawiało z bankami o potencjalnym IPO, które mogłoby nastąpić już w przyszłym roku"; sprzedaż 2025 r. ma się podwoić do ponad 200 mln EUR | [M] |
| grudzień 2025 | Modrzewski (Space Intel Report) | „w tej chwili nie ma takiego planu"; nie wyklucza notowania na Nasdaq; nie zdecydował, kiedy ani gdzie; spółka „nie ma pilnej potrzeby gotówki"; apel do Komisji Europejskiej o szybsze zamówienia | [M] |
| marzec 2026 | Mainsights | ICEYE „kandydat do IPO", otwarty na notowanie, ale priorytetem wykonanie portfela 1,5 mld EUR | [M] |
| czerwiec 2026 | Modrzewski (prasa fińska) | runda F „przede wszystkim o przyspieszeniu mocy produkcyjnych, a nie o szykowaniu się do giełdy" | [M] |
| listopad 2025 | inwestorzy detaliczni w Finlandii | ICEYE na liście spółek, których debiutu w Helsinkach oczekują | [M] |

Synteza **[?]**: sekwencja to rozmowy o IPO (czerwiec 2025) → prywatna seria E z odsprzedażą (grudzień 2025) → seria F z odsprzedażą ponad 550 mln EUR (czerwiec 2026). Przy gotówce ponad 350 mln EUR i dodatnich przepływach giełda jest wyborem, nie koniecznością; inwestorzy typu General Atlantic, TCV i QIA zwykle oczekują płynności w 3–5 lat, więc okno 2027–2029 jest prawdopodobne, ale nieogłoszone. Jedyne wymienione miejsce to Nasdaq; Helsinki to nadzieja fińskich komentatorów; o GPW nie ma wzmianki w żadnym źródle.

---

## 7. Wzrost w liczbach

| Miara | 2023 | 2024 | 2025 | 2026 (plan) | Wiar. |
|---|---|---|---|---|---|
| Przychody | 123,4 mln EUR (ICEYE Oy); spółka: „ponad 100 mln USD" | 121,2 mln EUR (ICEYE Oy) | ponad 250 mln EUR (grupa); baza Asiakastieto dla ICEYE Oy: 312,3 mln EUR (rozbieżność, patrz niżej) | „podobne tempo" (podwojenie); 2027: ponad 1 mld EUR | [M]/[Z] |
| Wynik operacyjny / EBITDA | zysk 4,1 mln EUR (marża 3,6 %) | strata operacyjna 35,3 mln EUR | EBITDA ponad 100 mln EUR; przepływy operacyjne ponad 130 mln EUR | — | [M]/[Z] |
| Gotówka | b.d. | b.d. | ponad 350 mln EUR | — | [Z] |
| Portfel zamówień | b.d. | b.d. | 1,5 mld EUR | — | [Z] |
| Satelity wystrzelone (narastająco) | 27 (czerwiec 2023) | 38 | 62 (22 w roku) | 76 do lipca; ok. 50 rocznie | [Z]/[M] |
| Zatrudnienie | 296 (Oy) | 359 (Oy) | ponad 900 (grupa) | ponad 1000; ponad 150 w Polsce | [M] |

Rozbieżność przychodów 2025 r. (312,3 mln EUR w bazie fińskiej wobec „ponad 250 mln EUR" w komunikacie) tłumaczy najpewniej różnica między spółką-matką sprzedającą satelity spółkom zależnym i JV a wynikiem skonsolidowanym; wiążąca jest liczba spółki **[?]**. Strata operacyjna w 2024 r. i zysk w 2025 r. pokazują, że przegięcie przyniosły dostawy systemów dla państw, nie sprzedaż danych.

**Kontrakty rządowe (kotwice przychodów)**

| Klient | Data | Przedmiot | Wartość | Wiar. |
|---|---|---|---|---|
| Brazylia (FAB) | grudzień 2020 | 2 satelity (Carcará 1 i 2) z własnym segmentem naziemnym; start maj 2022 | b.d. | [M] |
| Ukraina | sierpień 2022; listopad 2024; styczeń 2026 | dostęp do satelity i konstelacji kupiony przez Fundację Prytuły (środki zbiórki na Bayraktary); potem umowy z MO Ukrainy z bezpośrednim taskingiem i dużym wolumenem zobrazowań | ok. 16 mln USD (2022); dalsze b.d. | [M]/[Z] |
| Polska (Agencja Uzbrojenia) | 14 maja 2025 | MikroSAR: 3 satelity SAR (ICEYE) + stacjonarny i mobilny segment naziemny (WZŁ-1); opcja na 3 kolejne; cztery satelity na orbicie do maja 2026 r.; prasa mówi o sześciu (wykonanie opcji niepotwierdzone) | 860 mln zł brutto | [Z] |
| Finlandia (Siły Obronne) | 8 września 2025 | 3 satelity z opcjami; drugi wystrzelony 11 stycznia 2026 r. | ok. 158 mln EUR netto | [Z] |
| Holandia (RNLAF) | 23 czerwca 2025 | 4 satelity klasy 25 cm, segment naziemny, mobilny hub analityczny | b.d. (jedno streszczenie: 158 mln EUR, niezweryfikowane) | [Z]/[?] |
| Portugalia (Siły Powietrzne) | 13 czerwca 2025; czerwiec 2026 | 1 satelita + segment naziemny; potem 2 kolejne (łącznie 4 systemy) | b.d. | [Z]/[M] |
| Grecja (program narodowy przez ESA) | 2025 | 2 satelity; produkcja w Atenach; start 28 listopada 2025 r. | b.d. | [Z] |
| Niemcy (Bundeswehra) | 18 grudnia 2025 | SPOCK 1: wyłączny dostęp do konstelacji SAR do końca 2030 r., dla JV Rheinmetall ICEYE Space Solutions (60/40) | 1,7 mld EUR | [Z] |
| Szwecja (FMV) | 12 stycznia 2026 | satelity, dane, oprogramowanie i systemy naziemne na własność Sił Zbrojnych | część pakietu 1,3 mld SEK (z Planet) | [Z] |
| Japonia (IHI) | październik 2025 | 4 satelity + opcja na 20; montaż i testy w Japonii | b.d. | [Z] |
| NATO | marzec 2025; 2025 | dane SAR dla SITCEN; APSS (zobrazowania w ciągu godziny) | b.d. | [Z] |
| USA (NRO) | styczeń 2022; sierpień 2026 | ocena w BAA; kontrakt w Radar Commercial Augmentation (ICEYE US, Irvine) | b.d. | [Z] |
| UE (Copernicus) | październik 2021 | misja wspierająca; dane bezpłatne dla instytucji publicznych UE | b.d. | [Z] |

Wniosek **[?]**: ujawnione wartości (Polska ok. 200 mln EUR, Finlandia 158 mln EUR, Niemcy 1,7 mld EUR w JV, część Szwecji) są spójne z portfelem 1,5 mld EUR na koniec 2025 r. Ceną za zamówienia suwerenne jest lokalizacja produkcji: Ateny, Neuss, Irvine, Warszawa, Japonia.

---

## 8. Struktura właścicielska, kontrola i ład korporacyjny

- **Cap table**: ponad 50 inwestorów z ośmiu rund; po serii F Solidium ok. 6 %, Tesi ok. 7 %, państwo fińskie łącznie ok. 12 %, fińscy inwestorzy instytucjonalni (Varma, Ilmarinen, Keva, Nokia, Lifeline) ok. 17 %; ministrowie fińscy publicznie cieszyli się ze „zwiększonego udziału Finlandii w ICEYE" **[Z]**. Udziały założycieli i pozostałych funduszy nieujawnione **[?]**.
- **Rada**: Solidium ma miejsce od 2024 r.; skład rady nieustalony **[M]/[?]**.
- **Państwo jako inwestor i klient jednocześnie**: Finlandia (Tesi i Solidium jako akcjonariusze, Siły Obronne jako klient, Business Finland jako grantodawca), Polska (Vinci/BGK jako akcjonariusz, MON jako klient, PGZ i WZŁ-1 jako partnerzy przemysłowi; prezes w Radzie Biznesu przy Prezydencie RP) **[Z]/[M]**.
- **JV z koncernem**: Rheinmetall ICEYE Space Solutions GmbH (Rheinmetall 60 %, ICEYE 40 %) jest stroną kontraktu 1,7 mld EUR; ICEYE dostarcza satelity i technologię, produkcja w Neuss **[Z]**. ICEYE zaakceptowało mniejszość w JV jako cenę wejścia do niemieckich zamówień.
- **Struktura spółek**: ICEYE Oy (Finlandia) jako matka; ICEYE Polska Sp. z o.o. (lider konsorcjum MikroSAR); ICEYE US (satelity na licencji USA, kontrakty NRO); spółki w Holandii, Grecji i innych **[Z]/[M]**.
- **Płynność bez giełdy**: ok. 50 mln EUR (seria E) i ponad 550 mln EUR (seria F) odsprzedaży akcji przez dotychczasowych akcjonariuszy **[Z]/[M]**.

---

## 9. Ocena: co zadziałało, co nie

**Zadziałało**

1. Publiczne pieniądze na najbardziej ryzykowny etap (prototyp i pierwszy satelita), prywatne na skalowanie; grant UE użyty wprost jako dźwignia do przyciągnięcia VC.
2. Inwestorzy, którzy są klientami (BAE, Kajima, Tokio Marine, Rheinmetall, Nokia): kapitał z kanałem sprzedaży.
3. Państwo jako cierpliwy akcjonariusz (Tesi, Solidium) legitymizujące firmę u zamawiających wojskowych w całej Europie.
4. Zmiana modelu w 2020 r.: sprzedaż całych systemów państwom zamiast tylko danych; to ona dała rentowność w 2025 r.
5. Lokalizacja produkcji jako narzędzie sprzedaży (Ateny, Neuss, Irvine, Warszawa, Japonia) przy zachowaniu projektu satelity i IP w spółce-matce.
6. Odsprzedaże w rundach E i F zamiast IPO w „hype cycle": płynność dla inwestorów bez ryzyka kursowego, jakie poniósł Swarmer.

**Nie zadziałało albo kosztowało**

1. Jedenaście lat do rentowności i strata operacyjna 35 mln EUR jeszcze w 2024 r.; cierpliwość inwestorów była warunkiem przetrwania.
2. Ponad 50 inwestorów i osiem rund: koszt ładu, negocjacji i rozwodnienia; udziały założycieli nieznane, ale po ok. 1,2 mld USD kapitału pierwotnego z pewnością mniejszościowe **[?]**.
3. Wejście inwestorów spoza UE/NATO (Kajima i IHI z Japonii, QIA z Kataru) jako cena globalnego skalowania; w Finlandii nie było przeszkód, ale w firmie z Kryterium jak w § 11 każdy z nich wymagałby uchwały WZ.
4. Zależność od kalendarza zamówień publicznych: prezes publicznie apeluje do Komisji Europejskiej o szybsze zakupy; „bez europejskich agencji kupujących od lokalnych startupów trudno rosnąć" **[M]**.
5. Polska nie była miejscem założenia mimo polskiego założyciela; kraj „odzyskał" spółkę dopiero po dekadzie, kupując udziały i satelity **[?]**.

---

## 10. Wnioski dla Basiliska: mapowanie na projekt umowy

Oznaczenia stanu jak w `vc.md` sekcja 8: **OK** — umowa to przewiduje; **CZ** — częściowo, do doprecyzowania; **BRAK** — nie ma, dodać; **KOL** — koliduje, do negocjacji albo decyzji; **DEC** — wymaga decyzji Założycieli.

| Lekcja z ICEYE | Gdzie u nas | Stan | Co zrobić i kiedy |
|---|---|---|---|
| **Drabina finansowania**: granty na prototyp, VC na pierwsze wdrożenia, państwo i koncerny jako kapitał cierpliwy, kontrakty rządowe jako przegięcie, growth equity po rentowności | § 31 ust. 1 (katalog źródeł), § 32 (runda), § 33 (partnerzy); `regulations.md` sekcja 3; `psa_todo.md` sekcja 6 | CZ | Spisać plan finansowania w pięciu szczeblach z warunkami przejścia (TRL, pierwszy płatny pilot, pierwszy kontrakt wieloletni); EIC, Ścieżka SMART i DIANA to odpowiedniki Tekes i H2020 dla szczebla 1 |
| **Grant UE jako dźwignia do VC**: 2,4 mln EUR z H2020 „aby przyciągnąć prywatne inwestycje" | `psa_todo.md` sekcja 6 (EIC Accelerator: grant do 2,5 mln EUR i inwestycja do 30 mln EUR) | OK | Wniosek do EIC planować przed rundą A, nie po; grant zmniejsza rozwodnienie i podnosi wycenę |
| **Inwestorzy państwowi spełniają Kryterium**: Tesi, Solidium, Vinci/BGK to podmioty kontrolowane przez państwa UE | § 11 ust. 6 lit. b; `vc.md` sekcja 3 | OK | Uwzględnić PFR (przez fundusze), BGK (Vinci) i EIF jako inwestorów zgodnych z Kryterium bez uchwały WZ; sprawdzić wymogi ich programów (`regulations.md` sekcja 3) |
| **Inwestorzy strategiczni spoza UE/NATO na etapie growth** (Kajima, IHI: Japonia; QIA: Katar) | § 11 ust. 6 (zgoda WZ 75 %), ust. 14 (przekreślony wyjątek dla funduszy), § 12 ust. 2 lit. b; `regulations.md` sekcja 3 (art. 9 EDF: liczy się kontrola, nie udział) | KOL | Przewidzieć ścieżkę: mniejszościowy inwestor spoza Kryterium dopuszczony uchwałą 75 % z ograniczeniem dostępu do IP (§ 27 ust. 6) i bez praw kontrolnych; to zachowuje kwalifikowalność do EDF, bo art. 9 zakazuje kontroli, nie udziału **[W]** |
| **Koncern-klient jako akcjonariusz** (BAE, Kajima, Tokio Marine, Nokia) | § 29–30 (transakcje z Akcjonariuszami na warunkach rynkowych, ujawnienie konfliktu) | OK | Bez zmian; w umowie inwestycyjnej z koncernem dopisać brak wyłączności sprzedażowej i brak prawa pierwszeństwa do IP |
| **Mniejszość w JV z koncernem jako cena wejścia do zamówień** (Rheinmetall 60/40 jako strona kontraktu 1,7 mld EUR) | § 33 ust. 1–2 (udział mniejszościowy dopuszczalny), ust. 3 (IP zostaje w Spółce, licencja niewyłączna, ulepszenia dla Spółki), ust. 5 (prawa informacyjne, weto w sprawach IP i bezpieczeństwa przy braku kontroli) | OK | We wzorze umowy JV (etap C pkt 25 w `plan_prac.md`) użyć modelu ICEYE–Rheinmetall: JV jest stroną kontraktu, Basilisk dostawcą technologii; Rheinmetall (UE) spełnia Kryterium, Hanwha (Korea, zob. `wb_electronics.md`) nie |
| **Konsorcjum z polskim przemysłem państwowym** (ICEYE Polska + WZŁ-1 z PGZ w MikroSAR; porozumienie z PGZ) | § 33 (konsorcjum), § 23 ust. 1 lit. h | OK | Szablon dla programów MON: Basilisk liderem w warstwie autonomii, spółka PGZ w segmencie sprzętowym albo odwrotnie |
| **Państwo jako inwestor i klient jednocześnie** (Finlandia, Polska) | § 30 (transakcje z Akcjonariuszami), § 11 | OK | Jeżeli wehikuł Skarbu Państwa zostanie akcjonariuszem, kontrakty z MON podlegają § 30 (warunki rynkowe, ujawnienie); nie jest to przeszkoda, ale wymaga procedury |
| **Lokalizacja produkcji jako narzędzie sprzedaży**, IP w spółce-matce | § 33 ust. 3, § 26 (Kluczowa Własność Intelektualna), § 28 | OK | Przy pierwszym kontrakcie zagranicznym zakładać, że zamawiający zażąda montażu u siebie; § 33 to przewiduje |
| **Horyzont 10 lat do rentowności**; strata operacyjna w roku poprzedzającym przegięcie | § 34 ust. 2 (rekomendowana reinwestycja 36 miesięcy), `vc.md` sekcja 6 (fundusze obronne: 10–15 lat) | CZ | 36 miesięcy to horyzont softwarowy; przy modelu produkcyjnym zapisać w umowie akcjonariuszy politykę reinwestycji do pierwszego roku dodatnich przepływów |
| **Płynność przez odsprzedaż w rundach zamiast IPO** (ok. 600 mln EUR w 2025–2026 r.) | § 12 (zgoda Spółki na zbycie), § 14 (prawo pierwszeństwa), § 11 (Kryterium przy każdym nabyciu); `vc.md` sekcja 8 (permitted transfers) | KOL | Odsprzedaż w rundzie musi mieć szybką ścieżkę: zgoda Spółki i wyłączenie prawa pierwszeństwa dla nabywców zweryfikowanych w rundzie, w jednej uchwale z emisją; dopisać do § 12 ust. 7 albo do umowy akcjonariuszy **[W]** |
| **Miejsce w radzie dla inwestora państwowego** (Solidium 2024) przy ośmiu rundach | § 21 ust. 1 (Rada 3–7 osób), § 32 ust. 4 lit. c (jeden dyrektor albo obserwator na rundę) | CZ | Po trzeciej rundzie liczba miejsc się kończy; w umowie akcjonariuszy ustalić, że lider każdej rundy wskazuje dyrektora, pozostali obserwatora, z rotacją |
| **Pierwszy klient wojskowy przez fundację charytatywną** (Prytuła, 16 mln USD dla Ukrainy) | `regulations.md` sekcja 2.2b (klient spoza NATO), § 23 ust. 1 lit. h, § 28 (użytkownik końcowy) | OK | Procedura z `regulations.md` obejmuje taki przypadek: nabywcą jest fundacja, użytkownikiem końcowym armia państwa spoza NATO; certyfikat użytkownika końcowego i zezwolenie MRiT przed dostawą **[W]** |
| **„Dlaczego Finlandia": grant uczelniany 50 tys. EUR, budżet projektu 0,5 mln EUR, wsparcie grantowe** | `psa_todo.md` sekcja 1 (pytanie o jurysdykcję) | DEC | Argument za pozostaniem w Polsce, o ile Basilisk realnie sięgnie po granty (EIC, SMART, DIANA); argument za Estonią albo Finlandią, jeżeli o decyzji ma przesądzać dostęp do wsparcia na wczesnym etapie. Rozstrzygnąć razem z pytaniem o strukturę holdingową |

---

## 11. Luki i rzeczy do sprawdzenia

- Wyceny post-money rund 2015–2024; udziały założycieli; skład rady dyrektorów.
- Podział rozszerzenia z grudnia 2024 r. na dług i kapitał; warunki pożyczek Business Finland; czy istnieją kredyty bankowe.
- Data zawiązania ICEYE Oy (2014 według Wikipedii, działalność od 2015 według Aalto); skład pozostałych 4,5 mln USD z finansowania z 2017 r.
- Czy MON wykonał opcję na 3 kolejne satelity MikroSAR (data, wartość); wartość kontraktu holenderskiego (158 mln EUR pojawia się w jednym streszczeniu i może być pomyleniem z Finlandią).
- Wartości kontraktów: Grecja, Portugalia, Japonia (IHI), Brazylia, NATO, Ukraina 2024–2026, NRO.
- Czy „RiO Family Office" w serii E to wehikuł Rafała Brzoski (polska prasa pisze o jego inwestycji przy wycenie 2,4 mld EUR).
- Wielkość pakietu Vinci/BGK i czy został zwiększony w seriach E i F.
- Liczba satelitów operacyjnych (nie tylko wystrzelonych) we wrześniu 2026 r.; starty po lipcu 2026 r.
- Przychody i zatrudnienie ICEYE Polska przed 2026 r.

---

## 12. Źródła sprawdzone 30 września 2026 r.

**Początki i wsparcie publiczne**
- Aalto University, listopad 2015 — https://www.aalto.fi/en/news/aalto-born-iceye-receives-seven-figure-sum-in-funding-for-its-first-satellite ; sierpień 2017 — https://www.aalto.fi/en/news/aalto-born-iceye-receives-usd-13-million-for-its-radar-based-microsatellite-imaging-service
- Grant H2020 — https://www.iceye.com/newsroom/press-releases/iceye-secures-eur-2-4m-in-grant-from-eu-horizon-2020-sme-instrument ; runda 2015 — https://www.iceye.com/newsroom/press-releases/space-technology-startup-iceye-raises-2-8-million-series-a
- Pożyczka Business Finland 2018 — https://www.iceye.com/newsroom/press-releases/iceye-receives-10-million-euro-capital-loan-business-finland-to-initiate-internet-of-locations ; Business Finland 2025 — https://www.businessfinland.fi/en/whats-new/news/press-releases/2025/business-finland-grants-funding-to-iceye ; rząd Finlandii — https://valtioneuvosto.fi/en/-/60305973/business-finland-grants-exceptionally-large-funding-iceye-scales-operations-and-investments-in-r-d-with-eur-250-million
- ESA, Copernicus — https://www.esa.int/Applications/Observing_the_Earth/Copernicus/ICEYE_commercial_satellites_join_the_EU_Copernicus_programme ; EIF (InnovFin z OTB) — https://www.eif.org/what_we_do/equity/news/2021/eif-eur-300-million-new-investments-space-sector-orbital-ventures-primo-space.htm
- Modrzewski o Finlandii: rp.pl Radar — https://radar.rp.pl/innowacje-w-armiach/art43393481-rafal-modrzewski-iceye-do-rozwoju-startupow-potrzebne-jest-zaufanie-spoleczne ; Forbes.pl — https://www.forbes.pl/pierwszy-milion/iceye-rafal-modrzewski-i-pekka-laurilla-stworzyli-goracy-start-up-kosmiczny/5q2bjs6 ; Sifted — https://sifted.eu/articles/musk-spacex-rivals-europe

**Rundy finansowania**
- 2017 — https://www.iceye.com/newsroom/press-releases/iceye-raises-usd-13m-additional-financing-to-develop-sar-microsatellite-constellation ; seria B 2018 — https://www.iceye.com/newsroom/press-releases/iceye-raises-34-million-dollars-series-b-financing-confirms-nine-sar-satellite-launches-by-end-of-2019 ; seria C 2020 — https://www.iceye.com/newsroom/press-releases/usd-87m-in-series-c-for-iceye-to-continue-conquering-boundaries-in-radar-satellite-imaging ; seria D 2022 — https://www.iceye.com/newsroom/press-releases/iceye-raises-usd-136m-in-series-d-funding-round ; rozszerzenie 2024 — https://www.iceye.com/newsroom/press-releases/iceye-closes-65m-extension-to-existing-growth-funding-round-for-a-total-of-158m-raised-in-2024 ; seria F 2026 — https://www.iceye.com/newsroom/press-releases/iceye-leads-a-new-era-of-sovereign-intelligence-from-space-with-1b-funding-round
- Runda Solidium 2024: Via Satellite — https://www.satellitetoday.com/finance/2024/04/17/iceye-raises-93m-led-by-finnish-sovereign-wealth-fund-solidium/ ; SpaceNews — https://spacenews.com/satellite-imaging-company-iceye-raises-93-million-in-latest-funding-round/
- Seria E: Bloomberg, 5 grudnia 2025 — https://www.bloomberg.com/news/articles/2025-12-05/general-catalyst-bakcs-sattelite-startup-iceye-at-2-8-billion-valuation ; Via Satellite — https://www.satellitetoday.com/finance/2025/12/08/iceyes-latest-raise-values-company-at-2-8-billion/ ; Space Intel Report („no IPO for now") — https://www.spaceintelreport.com/iceye-no-ipo-for-now-300m-rev-in-2025-a-3b-valuation-with-expanding-production-co-asks-eu-commission-to-move-faster/ ; money.pl (Brzoska) — https://www.money.pl/gospodarka/tworca-inpostu-rusza-w-kosmos-rafal-brzoska-inwestuje-w-polskiego-jednorozca-wycenianego-na-2-4-mld-euro-7229272437373856a.html
- Seria F: General Atlantic — https://www.generalatlantic.com/media-article/iceye-leads-a-new-era-of-sovereign-intelligence-from-space-with-e1bn-fundraising-round/ ; Bloomberg, 9 czerwca 2026 — https://www.bloomberg.com/news/articles/2026-06-09/iceye-valuation-jumps-to-10-billion-in-funding-round-led-by-general-atlantic ; komunikat fiński (10,5 mld EUR) — https://www.sttinfo.fi/tiedote/72117779/iceyelle-miljardin-rahoituskierros-105-miljardin-euron-arvostustasolla-suomen-kolmas-decacorn-on-syntynyt?publisherId=69819051&lang=fi ; Solidium — https://www.solidium.fi/tiedotteet/solidium-osallistuu-iceyen-rahoituskierrokseen/ ; rząd Finlandii — https://valtioneuvosto.fi/en/-/1410877/ministers-strand-and-puisto-are-pleased-with-finland-s-increased-ownership-of-iceye ; EQT Scaleup Europe Fund — https://eqtgroup.com/news/eqts-scaleup-europe-fund-makes-first-investment-co-leads-1-billion-funding-round-in-iceye-europes-leader-in-sovereign-intelligence-from-space-2026-08-05 ; Interia (odsprzedaż) — https://biznes.interia.pl/gospodarka/news-iceye-z-wycena-ponad-10-mld-euro-wchodzimy-w-nowa-ere,nId,23493597
- Vinci/BGK: Bloomberg, 25 sierpnia 2025 — https://www.bloomberg.com/news/articles/2025-08-25/poland-buys-stake-in-finnish-surveillance-satellite-maker-iceye ; Defence24 — https://defence24.com/technology/poland-invests-in-iceye-bgk-group-signed-the-agreement
- Bazy: Tracxn — https://tracxn.com/d/companies/iceye/__LYPRQx3i9d8_A05BEgw8V1KyFzEeFfqq2LqwT9QBKB8/funding-and-investors ; Multiples.vc — https://multiples.vc/private-comps/iceye ; Asiakastieto (ICEYE Oy) — https://www.asiakastieto.fi/yritykset/fi/iceye-oy/26398221/taloustiedot

**Wyniki i IPO**
- Wyniki 2025 — https://www.iceye.com/newsroom/press-releases/iceye-announces-2025-financials ; Space Intel Report — https://www.spaceintelreport.com/iceyes-2025-financials-revenue-294m-will-double-this-year-153m-in-operating-cash-flow-1-76b-in-backlog/ ; Bloomberg, 12 marca 2026 — https://www.bloomberg.com/news/articles/2026-03-12/satellite-firm-iceye-targets-1-billion-revenue-next-year ; Bloomberg, 23 czerwca 2025 (IPO) — https://www.bloomberg.com/news/articles/2025-06-23/military-satellite-maker-iceye-explores-ipo-as-sales-on-track-to-double ; Defense News, 25 czerwca 2026 — https://www.defensenews.com/global/europe/2026/06/25/iceye-to-double-radar-satellite-capacity-by-late-2027-as-demand-surges/ ; Mainsights — https://www.mainsights.io/ma-news/finnish-satellite-intelligence-firm-iceye-on-track-for-eur-1bn-revenue-next-year-with-potential-ipo-plans

**Kontrakty rządowe**
- Polska, MikroSAR: ICEYE Polska — https://www.iceye.com/pl-pl/press/press-releases/iceye-dostarczy-satelity-sar-si%C5%82om-zbrojnym-rp-w-ramach-programu-mikrosar ; Space24 — https://space24.pl/satelity/obserwacja-ziemi/iceye-dostarczy-satelity-dla-wojska-polskiego-znamy-szczegoly-umowy ; rp.pl — https://www.rp.pl/biznes/art42279131-polska-armia-zyska-oczy-mon-kupuje-satelity-za-setki-milionow-zlotych ; czwarty satelita — https://evertiq.pl/news/2026-05-04-czwarty-satelita-iceye-dla-polskiego-wojska-na-orbicie ; PGZ–WZŁ-1–ICEYE 2023 — https://milmag.pl/mspo-2023-porozumienie-pgz-wzl-1-i-iceye-ws-konstelacji-satelitow-radarowych/ ; list intencyjny PGZ 2026 — https://space24.pl/bezpieczenstwo/technologie-wojskowe/iceye-i-pgz-chca-zbudowac-system-lacznosci-satelitarnej-dla-wojska-polskiego
- Finlandia — https://puolustusvoimat.fi/en/-/finnish-defence-forces-to-procure-satellites-from-iceye ; https://www.iceye.com/newsroom/press-releases/iceye-signs-satellite-acquisition-agreement-with-the-finnish-defence-forces
- Niemcy, SPOCK 1 — https://www.rheinmetall.com/en/media/news-watch/news/2025/12/2025-12-18-rheinmetall-and-iceye-win-billion-euro-contract-for-space-reconnaissance ; JV w Neuss — https://www.iceye.com/newsroom/press-releases/rheinmetall-and-iceye-establish-joint-venture-in-neuss ; SpaceNews — https://spacenews.com/germany-awards-1-9-billion-sar-satellite-deal-to-rheinmetall-iceye-venture/
- Holandia — https://www.satellitetoday.com/government-military/2025/06/23/iceye-to-supply-4-sar-satellites-to-royal-netherlands-air-force/ ; Portugalia — https://www.iceye.com/newsroom/press-releases/iceye-and-portuguese-air-force-announce-first-direct-satellite-procurement ; https://thedefensepost.com/2026/06/18/portugal-sar-satellite-iceye/ ; Grecja — https://www.iceye.com/newsroom/press-releases/iceye-strengthens-presence-in-greece-with-new-office-and-satellite-production-line ; Szwecja — https://valtioneuvosto.fi/en/-/236553176/minister-of-defence-antti-hakkanen-iceye-s-contract-with-sweden-will-strengthen-security-across-the-nordic-region ; Japonia (IHI) — https://www.ihi.co.jp/en/all_news/2025/aeroengine_space_defense/1201692_13743.html ; NATO — https://www.iceye.com/newsroom/press-releases/iceye-to-provide-sar-satellite-data-to-the-situation-center-at-nato ; USA (NRO RCA) — https://iceye.us/news/iceye-us-awarded-contract-under-nros-radar-commercial-augmentation-rca-program ; Ukraina 2022 — https://english.nv.ua/nation/prytula-foundation-purchases-full-satellite-access-for-16-million-for-ukraine-military-news-50264148.html ; Ukraina 2026 — https://www.iceye.com/newsroom/press-releases/ukraine-expands-partnership-with-iceye ; Brazylia — https://milmag.pl/en/iceye-radar-satellites/

**Polska: biuro, inwestorzy, komentarze**
- ICEYE Polska w KRS — https://rejestr.io/krs/700126/iceye-polska ; Centrum Technologii Satelitarnych: rp.pl — https://rp.pl/biznes/art45187501-iceye-zainwestuje-w-polsce-120-mln-zl-satelitami-pokieruje-z-warszawy ; Space24 — https://space24.pl/przemysl/sektor-krajowy/iceye-otwiera-nowa-siedzibe-w-warszawie-firma-zwieksza-inwestycje-w-polsce ; PAP Biznes — https://biznes.pap.pl/wiadomosci/firmy/iceye-otworzyl-centrum-technologii-satelitarnych-planuje-przeznaczyc-na-rozwoj
- OTB Ventures: Global Venturing — https://globalventuring.com/university/investors-put-34m-on-iceyes-radar/ ; Space24 — https://space24.pl/satelity/iceye-wiecej-kapitalu-satelitow-i-zadan-polskiego-oddzialu
- Rada Biznesu przy Prezydencie — https://www.money.pl/gospodarka/prezydent-powolal-rade-biznesu-oto-jej-sklad-7268066704521312a.html ; Parkiet (wycena 10 mld EUR) — https://www.parkiet.com/technologie/art44587371-spolka-z-polskim-ceo-wyceniana-na-10-mld-euro ; The Recursive — https://www.therecursive.com/polish-finnish-iceye-reaches-decacorn-status/
- Strony iceye.com, bloomberg.com, spacenews.com, satellitetoday.com, rp.pl, space24.pl i solidium.fi były w tej sesji niedostępne do pełnego odczytu (blokada sieciowa); tezy oparte na ich streszczeniach z wyszukiwarki oznaczono [Z] tylko tam, gdzie streszczenie dokumentu pierwotnego było jednoznaczne.
