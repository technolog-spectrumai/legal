# Case study: Shield AI — autonomia jako osobna pozycja w kontrakcie (Hivemind, V-BAT, 12,7 mld USD)

Dokument wewnętrzny Basilisk Systems, informacyjny. Nie jest opinią prawną ani rekomendacją inwestycyjną i nie zmienia umowy spółki. Jedno ze studiów przypadku o rozwoju i finansowaniu firm obronnych, robotyki i fizycznego AI (przegląd i porównanie: `case_studies/README.md`). Shield AI jest najbliższym analogiem Basiliska: oprogramowanie autonomii (Hivemind) licencjonowane producentom płatowców i primom, plus własna linia dronów (V-BAT). Opisuje drogę od kontraktu DIU (2016 r.) przez SBIR, a16z i przejęcia do kupna autonomii przez USAF jako samodzielnej pozycji produkcyjnej na CCA (2026 r.). Odesłania do umowy według `psa.tex` w wersji 0.9.4-C (numery § według `spis_tresci.md`); uzupełnia `case_studies/anduril.md`, `case_studies/swarmer.md` (B2B2G), `jurisdictions/usa.md` i `regulations.md` sekcja 4.

Stan na 30 września 2026 r. Oznaczenia wiarygodności: **[Z]** — fakt z dokumentu pierwotnego (komunikat spółki, partnera, zamawiającego); **[M]** — doniesienie prasowe albo baza danych; **[W]** — wiedza ogólna o prawie albo praktyce rynkowej; **[?]** — szacunek albo teza niepotwierdzona. Uwaga metodyczna: strony źródłowe były w tej sesji niedostępne do pełnego odczytu (blokada sieciowa); fakty pochodzą ze streszczeń wyszukiwarki. Wyceny rund A-1 do E pochodzą z jednego agregatora (Forge); przychody to szacunki (Sacra); rok obrotowy kończy się prawdopodobnie w marcu.

---

## 1. Główny wniosek

Shield AI dostarcza **najważniejszy precedens dla pitchu Basiliska: 17 czerwca 2026 r. USAF kupiło autonomię misji Hivemind jako samodzielną pozycję produkcyjną na Collaborative Combat Aircraft, pod rządową architekturą referencyjną (A-GRA), niezależnie od płatowca**. Droga do tego: założenie w 2015 r. w San Diego przez byłego SEALa Brandona Tsenga, jego brata Ryana i Andrew Reitera; kontrakt DIU (2016 r.) przed serią A 10,5 mln USD od a16z (kwiecień 2017 r.); kwadrokopter Nova w walce z siłami specjalnymi (2018 r.); SBIR II AFWERX 7,2 mln USD (2020 r.); kupno płatowca (Martin UAV, V-BAT) i zespołu AI (Heron Systems, zwycięzca AlphaDogfight) w 2021 r.; jednorożec (seria D, 1,25 mld USD, sierpień 2021 r.); seria F 2,7 mld USD (2023 r.), F-1 5,3 mld USD z L3Harris i Hanwha (marzec 2025 r.), seria G 1,5 mld USD equity plus 500 mln USD uprzywilejowanych Blackstone przy 12,7 mld USD (26 marca 2026 r., Advent i JPMorgan), rozmowy o ≥20 mld USD (wrzesień 2026 r.); ok. 3,5 mld USD łącznie. Przychód ok. 300 mln USD (rok do marca 2025 r.), prognoza ≥540 mln USD (2026 r.), cel 1 mld USD (2028 r.). Licencje Hivemind Enterprise dla KAI, Northropa (Talon IQ), Kratosa, Airbusa (DT25 w Norwegii, integracja w 3 miesiące); biuro w Kijowie i integracja z dronami Brave1 (marzec 2026 r.). Cena: wady V-BAT i poważny wypadek marynarza (Forbes, maj 2025 r.), „epicka katastrofa" pierwszej wyprawy do Ukrainy (2022 r.), zewnętrzny prezes od maja 2025 r. i uprzywilejowany kapitał PE przed akcjami zwykłymi. Dla Basiliska: to dowód, że autonomia może być kupowana osobno i licencjonowana „suwerennym" OEM-om — model bez własnej fabryki.

---

## 2. Profil

| Element | Treść | Wiar. |
|---|---|---|
| Nazwa i forma | Shield AI Inc., San Diego; zakłady X-BAT we Frisco (Teksas); biura: Port Melbourne (Australia; Sentient, 95 osób), Kijów, Abu Zabi, Tokio, Oslo (wrzesień 2025 r.) | [Z]/[M] |
| Założenie | 2015 r.; Brandon Tseng (Akademia Marynarki, 7 lat SEAL, Harvard MBA; prezes/president), Ryan Tseng (brat; president, potem CSO), Andrew Reiter (CTO, obecnie Technical Fellow); prezes wykonawczy Gary Steele (ex-Splunk, założyciel Proofpoint) od 13 maja 2025 r. | [Z]/[M] |
| Produkty | Hivemind (pilot AI), Hivemind Enterprise (runtime, „Forge", API dla OEM, sił powietrznych i primów), Hivemind Vision; V-BAT (MQ-35, VTOL, 12 h, 180 km); X-BAT (myśliwiec VTOL, prezentacja 22 października 2025 r., loty 2026 r., zdolność 2028 r., 150 sztuk rocznie od ok. 2029 r.) | [Z]/[M] |
| Klienci i partnerzy | USAF (CCA), US Coast Guard, US Navy, JMSDF, MO Holandii, Siły Systemów Bezzałogowych Ukrainy, KAI, Boeing (MoU 2023 r.), General Atomics, L3Harris, Airbus DS, Kratos, Northrop Grumman, HII, Booz Allen | [Z]/[M] |
| Zatrudnienie | ok. 1 500 (marzec 2026 r., spółka); 1 300–1 800 wg agregatorów; 391 otwartych stanowisk (2026 r.) | [Z]/[M] |
| Przejęcia | Martin UAV (V-BAT) i Heron Systems (lipiec 2021 r.), Sentient Vision Systems (Australia, kwiecień 2024 r.), Aechelon Technology (symulacja, marzec 2026 r.) | [Z] |

---

## 3. Jak zaczęli: kapitał początkowy i pierwsze lata

- **Kontrakt rządowy przed VC.** Pierwszy duży kontrakt: program autonomii DIU w 2016 r.; wczesne granty SBIR i DIU „pomogły przejść dolinę śmierci" **[M]**. Kapitał założycieli i aniołów przed 2017 r. nieodnaleziony **[?]**.
- **Seria A 1 kwietnia 2017 r.:** 10,5 mln USD po 1,85 USD za akcję, 30,58 mln USD po pieniądzu, lead a16z (obecny w każdej rundzie od tamtej pory) **[M]**.
- **Pierwszy produkt w walce po trzech latach:** Nova, mały kwadrokopter mapujący i „czyszczący" budynki bez GPS i łączności, wdrożony z siłami specjalnymi na Bliskim Wschodzie w 2018 r. **[M]/[Z]**.
- **SBIR II AFWERX (wrzesień 2020 r.):** 7,2 mln USD z Biurem Zdolności Strategicznych OSD dla lotnictwa Armii w środowisku bez GPS **[Z]**.
- **Wniosek:** dwa lata od założenia do serii A; kontrakt DIU z 2016 r. był zdarzeniem wiarygodności, które odblokowało a16z — droga „nietradycyjnego wykonawcy" wprost istotna dla Basiliska **[?]**.

---

## 4. Oś czasu

| Data | Zdarzenie | Wiar. |
|---|---|---|
| 2015 | założenie w San Diego | [Z]/[M] |
| 2016 | kontrakt DIU (autonomia) | [M] |
| 1 kwietnia 2017 | seria A 10,5 mln USD (a16z) | [M] |
| 2018 | Nova w walce z SOF | [M] |
| styczeń i sierpień 2019 | seria A-1 10 mln USD (113 mln USD); seria B 25 mln USD (203 mln USD) | [M] |
| wrzesień 2020 | SBIR II AFWERX 7,2 mln USD | [Z] |
| luty 2021 | seria C 71 mln USD (295 mln USD) | [M] |
| lipiec 2021 | przejęcia Heron Systems (AlphaDogfight 5:0 z pilotem F-16) i Martin UAV (V-BAT) | [Z] |
| sierpień 2021 | seria D 223 mln USD, 1,25 mld USD (jednorożec) | [M] |
| 2022 | pierwsza wyprawa do Ukrainy — „epicka katastrofa" (Fortune) | [M] |
| grudzień 2022 | seria E 150 mln USD, 2,3 mld USD | [M] |
| marzec 2023 | MoU z Boeingiem | [M] |
| październik 2023 | seria F 200 mln USD, 2,7 mld USD (USIT lead, Riot co-lead; ARK, Disruptive, Snowpoint) | [Z] |
| kwiecień 2024 | przejęcie Sentient Vision (Australia) | [M] |
| 2024 | Hivemind na Kratos Firejet (<180 dni) i Airbus DT25 w Norwegii (3 miesiące); druga wyprawa do Ukrainy: V-BAT traci GPS na wysokości dwóch stóp, 8 miesięcy iteracji, potem zaliczone testy zakłócania | [Z]/[M] |
| lipiec 2024 | US Coast Guard: IDIQ 198 mln USD na usługi ISR (COCO) z V-BAT | [Z] |
| styczeń 2025 | JMSDF zamawia V-BAT (pierwszy japoński morski ISR UAS; produkcja w USA; partner lokalny nieujawniony) | [M] |
| 6 marca 2025 | seria F-1 240 mln USD (268 wg Contrary), 5,3 mld USD (L3Harris, Hanwha, Washington Harbour, USIT, Cacti, a16z) „na skalowanie Hivemind Enterprise"; KAI pierwszym klientem Hivemind Enterprise w Korei | [Z] |
| 12 marca – 13 maja 2025 | Gary Steele prezesem | [Z] |
| 13 maja 2025 | Forbes: poważny wypadek marynarza z V-BAT, byli pracownicy o pękających kadłubach i zapowietrzonym paliwie | [M] |
| lipiec 2025 | Holandia kupuje 8 V-BAT (marynarka i piechota morska) | [Z] |
| wrzesień–grudzień 2025 | biuro w Oslo; X-BAT (22 października); pierwszy V-BAT dla JMSDF (9 grudnia) | [Z]/[M] |
| 2025–2026 | szkolenie Sił Systemów Bezzałogowych Ukrainy, biuro w Kijowie, 130+ lotów V-BAT, 200+ celów; V-BAT z „umową uzbrojenia" | [Z]/[M] |
| 13 marca 2026 | partnerstwo z Brave1: Hivemind w dronach ukraińskiej produkcji | [M] |
| 26 marca 2026 | seria G: 1,5 mld USD equity + 500 mln USD uprzywilejowanych (Blackstone) = 2 mld USD przy 12,7 mld USD; lead Advent, co-lead JPMorganChase Security & Resiliency; linia 250 mln USD; przejęcie Aechelon | [Z] |
| kwiecień–maj 2026 | US Navy: prawo konkurowania o do 800 mln USD usług ISR; wybór do pilotażu roju dronów Pentagonu | [Z]/[M] |
| 17 czerwca 2026 | USAF: kontrakt produkcyjny na autonomię misji Hivemind dla CCA pod A-GRA | [Z] |
| 16 lipca 2026 | nagrania z testów X-BAT; samolot jeszcze nie latał | [M] |
| wrzesień 2026 | The Information: rozmowy o serii H przy ≥20 mld USD | [M] |

---

## 5. Finansowanie: 17 rund, ponad 35 inwestorów, ok. 3,5 mld USD

| Runda | Data | Kwota | Po pieniądzu | Lead / inwestorzy | Wiar. |
|---|---|---|---|---|---|
| A | kwiecień 2017 | 10,5 mln USD | 30,6 mln USD | a16z | [M] |
| A-1 | styczeń 2019 | 10 mln USD | 113 mln USD | — | [M] |
| B | sierpień 2019 | 25 mln USD | 203 mln USD | — | [M] |
| C | luty 2021 | 71 mln USD | 295 mln USD | — | [M] |
| D | sierpień 2021 | 223 mln USD | 1,25 mld USD | — | [M] |
| E | grudzień 2022 | 150 mln USD | 2,3 mld USD | — | [M] |
| F | październik 2023 | 200 mln USD | 2,7 mld USD | USIT, Riot; ARK, Disruptive, Snowpoint | [Z] |
| F-1 | marzec 2025 | 240 mln USD | 5,3 mld USD | L3Harris, Hanwha, Washington Harbour, USIT, Cacti, a16z | [Z] |
| G | marzec 2026 | 1,5 mld USD + 0,5 mld USD pref. | 12,7 mld USD | Advent (lead), JPMorganChase (co-lead); Blackstone (uprzywilejowane o stałym zwrocie, przed akcjami zwykłymi) + 250 mln USD delayed draw; Snowpoint, InnovationX, Riot, Disruptive, Apandion | [Z]/[M] |
| H (rozmowy) | wrzesień 2026 | — | ≥20 mld USD | — | [M] |

- Inwestorzy strategiczni: L3Harris i Hanwha Aerospace (2025 r.) **[Z]**; secondaries i tender offers nieodnalezione **[?]**.
- Struktura z 2026 r. (lead growth-PE, fundusz banku, uprzywilejowane strukturyzowane) to przejście od VC do kapitału późnego etapu i sygnał, że inwestorzy chcieli ochrony przy 12,7 mld USD; szablon, który europejscy inwestorzy wzrostowi mogą skopiować w defence tech **[?]**.
- Mnożniki: 12,7 mld USD to ok. 40× przychód bieżący; 20 mld USD to ok. 37× prognozy 2026 r. — wyżej niż Anduril, bo narracja licencyjna **[?]**.

---

## 6. Giełda

Nienotowana; brak harmonogramu IPO; prezes Steele wprowadził wcześniej Proofpoint „od 0 do IPO"; struktura serii G (PE, uprzywilejowane) jest profilem spółki przed-IPO **[M]/[?]**.

---

## 7. Wzrost w liczbach

| Miara | Wartość | Wiar. |
|---|---|---|
| Przychód | ok. 267 mln USD (2024 r.); ok. 300 mln USD (rok do marca 2025 r.); prognoza ≥540 mln USD (+80 %, 2026 r.); cel 1 mld USD (rok do marca 2028 r.) | [M]/[?] |
| Wycena | 30 mln USD (2017 r.) → 1,25 mld USD (2021 r.) → 2,7 mld USD (2023 r.) → 5,3 mld USD (2025 r.) → 12,7 mld USD (2026 r.) | [M]/[Z] |
| Zatrudnienie | ok. 1 500 (2026 r.) | [Z] |
| Kontrakty | USCG 198 mln USD (IDIQ); Navy do 800 mln USD (IDIQ); CCA (wartość nieujawniona); DIU/Navy ok. 50 mln USD na X-BAT (USAF wstrzymuje się) | [Z]/[M] |
| Integracje Hivemind | X-62A VISTA (F-16, ponad 3 lata), Kratos Firejet (<180 dni), BQM-177A (ósmy płatowiec), Airbus DT25 (3 miesiące), cel XQ-58 Valkyrie | [Z]/[M] |
| Ukraina | 130+ lotów V-BAT, 200+ celów | [M] |

---

## 8. Struktura właścicielska, kontrola i ład korporacyjny

- Udziały założycieli nieujawnione **[M]**; założyciele oddali fotel prezesa operatorowi z enterprise software (maj 2025 r.) **[Z]**.
- Rada: David Mussafer (przewodniczący Adventu, od marca 2026 r.), obserwator Todd Combs; agregator wymienia Beau Laskeya i Andrew Reitera **[M]**.
- Uprzywilejowane Blackstone o stałym zwrocie, bez nowych akcji zwykłych, przed każdym akcjonariuszem zwykłym **[M]**.
- Brak udziału państwa; strategiczni: L3Harris, Hanwha **[Z]**.
- Profil ładu bliższy spółce przed-IPO niż startupowi kontrolowanemu przez założycieli **[?]**.

---

## 9. Ocena: co zadziałało, co nie

**Zadziałało**
- Wczesny kontrakt DIU i SBIR jako kapitał wiarygodności przed VC.
- Obronne aktywo programowe (Hivemind) udowodnione na F-16 DARPA, potem zakup sprawdzonego płatowca (V-BAT), żeby je nosić; usługi COCO (załogi w polu) jako finansowanie uczenia się.
- Szybkość integracji jako fosa: z ponad 3 lat (F-16) do 3 miesięcy (DT25).
- Obecność w Ukrainie (Kijów, szkolenia, Brave1) przed największymi zwycięstwami programowymi.
- A-GRA: autonomia kupowana osobno i iterowana „niezależnie od samolotu".
- Licencje dla „suwerennych" OEM (KAI buduje własnego pilota AI na Hivemind Enterprise).

**Nie zadziałało albo kosztowało**
- Wady V-BAT i poważny wypadek marynarza: koszt posiadania sprzętu przez firmę programistyczną.
- Chaotyczne pierwsze wejście do Ukrainy (2022 r.); utrata GPS w 2024 r.
- Sprzeczność między publicznym sprzeciwem Tsenga wobec w pełni autonomicznej broni śmiercionośnej a umową uzbrojenia V-BAT.
- Sceptycyzm co do wyceny („czy Shield AI naprawdę jest warte 12,7 mld USD?"); USAF odmówiło finansowania X-BAT.
- Uprzywilejowany kapitał PE przed akcjami zwykłymi i utrata fotela prezesa przez założycieli.

---

## 10. Wnioski dla Basiliska: mapowanie na projekt umowy

Oznaczenia stanu jak w `vc.md` sekcja 8: **OK**, **CZ**, **BRAK**, **KOL**, **DEC**.

| Lekcja z Shield AI | Gdzie u nas | Stan | Co zrobić i kiedy |
|---|---|---|---|
| **Autonomia jako samodzielna pozycja w kontrakcie pod rządową architekturą referencyjną** (A-GRA, CCA, czerwiec 2026 r.) | `regulations.md` sekcja 4; § 33 ust. 3; `psa_todo.md` sekcja 6 | BRAK | Użyć precedensu w rozmowach z MON, PGZ, WB i w EDF: autonomia roju jako otwarta, konkurowana warstwa oprogramowania; projektować interfejsy pod architektury referencyjne (A-GRA, niemiecki CFSN, `case_studies/helsing.md`) |
| **Licencje dla suwerennych OEM (KAI, Northrop, Kratos, Airbus)** zamiast własnych płatowców | § 33 ust. 3 (licencja niewyłączna, ograniczona zakresem, wypowiadalna przy zmianie kontroli); `case_studies/swarmer.md` sekcja 10 (B2B2G) | OK | Produkt typu „Enterprise/Forge" (runtime, API, wsparcie) w mapie produktu etapu C; wzór licencji „na platformę" z audytem wolumenów |
| **Kontrakt prototypowy (DIU 2016) przed serią A** | `regulations.md` sekcja 4 (G1–G3); `psa_todo.md` sekcja 6 (DIANA, EIC) | CZ | Pierwszy kontrakt albo grant przed Kwalifikowaną Rundą (§ 32); DIANA Fort Kraków i Brave1 jako polskie DIU |
| **Szybkość integracji jako mierzalne KPI** (3 lata → 180 dni → 3 miesiące) | `emisja/inwestor.md` (data room) | BRAK | Mierzyć i publikować czas integracji z każdą nową platformą |
| **Obecność w Ukrainie przed dużymi kontraktami** (Kijów, Brave1) | `jurisdictions/ukraina.md` sekcja 6; § 28 | DEC | Polska bliskość Ukrainy jest tańsza niż dla firmy z San Diego; ukraińska TOV albo estońska spółka kontraktowa po pierwszym grancie Brave1 |
| **Posiadanie sprzętu = odpowiedzialność za wypadki** (V-BAT) | `regulations.md` sekcja 2.2; § 33 | OK | Zostać przy oprogramowaniu; w umowach rozdzielać odpowiedzialność za autonomię od płatowca i wyrzutni |
| **Kapitał uprzywilejowany PE przed akcjami zwykłymi na późnym etapie** | § 31 ust. 4 (instrumenty: WZ 75 %); art. 300²⁶ KSH (uprzywilejowanie akcji P.S.A.) [W] | CZ | Umowa spółki musi dopuszczać akcje uprzywilejowane o stałej stopie i liquidation preference; sprawdzić § 6–8 pod kątem serii uprzywilejowanych |
| **Założyciele oddają fotel prezesa operatorowi** przy 5 mld USD | § 10 (vesting), § 21 (Rada), `vc.md` sekcja 9 | DEC | Zdecydować z góry, kiedy Założyciele przechodzą na role strategiczne; zapisać w umowie akcjonariuszy |
| **Inwestorzy strategiczni z branży (L3Harris, Hanwha)** w rundzie | § 11 (NATO: USA, Korea spełniają), § 25 ust. 1 | OK | Dopuścić prima z UE/NATO w rundzie B z ograniczeniem informacji konkurencyjnych (§ 29–30) |

---

## 11. Luki i rzeczy do sprawdzenia

- Kapitał założycieli i aniołów; najwcześniejsze SBIR (przed 2020 r.); leady i wyceny rund A-1 do E (tylko Forge).
- Zbadane przychody, marże, backlog; konwencja roku obrotowego; wartość kontraktu CCA; data i wartość pilotażu roju.
- Cap table, prawa głosu, pula opcji, tender offers; wynik rozmów o ≥20 mld USD.
- Forma prawna biur w Kijowie, Abu Zabi, Tokio; ITAR/FOCI; udział w EDF (nie odnaleziono).
- Następstwa prawne wypadku z V-BAT.

---

## 12. Źródła sprawdzone 30 września 2026 r.

- Profil i początki — https://en.wikipedia.org/wiki/Shield_AI ; https://shield.ai/about/ ; https://research.contrary.com/company/shield-ai ; https://time.com/collections/time100-ai-2025/7305863/brandon-tseng/ ; https://shield.ai/enterprise/ ; https://shield.ai/locations/ ; https://shield.ai/shield-ai-appoints-gary-steele-as-ceo-ryan-tseng-named-president/ ; https://shield.ai/autonomy-for-the-world-indoor-exploration-with-nova-2/ ; https://shield.ai/shield-ai-awarded-defense-department-contract-ai-software/ ; https://aerospaceamerica.aiaa.org/institute/shield-ai-co-founder-shares-10-year-journey-reimagining-air-power/
- Rundy — https://forgeglobal.com/shield-ai_ipo/ ; https://www.clay.com/dossier/shield-ai-funding ; https://shield.ai/shield-ai-raises-200m-reaching-2-7b-valuation/ ; https://www.prnewswire.com/news-releases/shield-ai-raises-240m-at-5-3b-valuation-to-scale-hivemind-enterprise-an-ai-powered-autonomy-developer-platform-302393843.html ; https://shield.ai/shield-ai-to-acquire-software-simulation-company-aechelon-and-raise-2b-at-12-7b-valuation/ ; https://www.alternativeswatch.com/2026/03/26/shield-ai-funding-private-equity-defensetech-advent-sagewind/ ; https://angelinvestorsnetwork.com/market-analysis/shield-ai-series-g-defense-tech-analysis ; https://oodaloop.com/briefs/technology/shield-ai-in-talks-to-raise-at-20b-valuation-up-60-in-five-months/ ; https://sacra.com/c/shield-ai/
- Przejęcia i integracje — https://shield.ai/shield-ai-acquires-heron-systems/ ; https://www.prnewswire.com/news-releases/shield-ai-signs-definitive-agreement-to-acquire-martin-uav-301343441.html ; https://fortune.com/2024/04/04/shield-ai-ai-sentient-vision-systems-andreessen-horowitz-venture-mergers-military-drones-warfare ; https://www.kratosdefense.com/newsroom/kratos-and-shield-ai-conduct-ai-piloted-flights-on-the-kratos-tactical-firejet ; https://shield.ai/shield-ai-and-airbus-complete-successful-autonomous-flight-with-dt25-target-drone/ ; https://insideunmannedsystems.com/kratos-and-shield-ai-advance-ai-piloted-uas-technology-with-firejet-integration/ ; https://shield.ai/shield-ai-partners-with-korea-aerospace-industries-to-advance-ai-powered-autonomy-with-hivemind-enterprise/ ; https://www.flightglobal.com/defence/shield-ai-to-assist-kai-in-development-of-korean-ai-pilot/162283.article
- Kontrakty — https://www.prnewswire.com/news-releases/shield-ais-v-bat-selected-for-198-million-contract-to-provide-us-coast-guard-with-maritime-unmanned-aircraft-system-services-302187333.html ; https://shield.ai/shield-ai-selected-by-u-s-navy-to-compete-for-800m-in-isr-services-with-v-bat/ ; https://shield.ai/shield-ai-awarded-u-s-air-force-production-contract/ ; https://www.prnewswire.com/news-releases/shield-ai-awarded-us-air-force-production-contract-for-collaborative-combat-aircraft-mission-autonomy-302803710.html ; https://breakingdefense.com/2025/01/japan-inks-deal-with-shield-ai-for-sea-based-v-bat-drones/ ; https://shield.ai/shield-ai-v-bat-selected-by-netherlands-ministry-of-defence-to-equip-navy-and-marine-corps/ ; https://www.airandspaceforces.com/navy-x-bat-investment-air-force/ ; https://defensescoop.com/2025/10/22/shield-ai-vtol-autonomous-fighter-jet-x-bat/
- Ukraina — https://shield.ai/shield-ai-starts-training-with-ukraines-unmanned-systems-forces-establishes-local-presence-in-ukraine/ ; https://defence-industry.eu/shield-ai-completes-over-130-v-bat-sorties-in-ukraine-to-support-spring-campaign/ ; https://www.pravda.com.ua/eng/news/2026/03/13/8025307/ ; https://fortune.com/2025/12/21/shield-ai-ukraine-defense-tech-gary-steele
- Krytyka — https://www.forbes.com/sites/davidjeans/2025/05/13/shield-ai-navy-injury/ ; https://techcrunch.com/2024/10/09/shield-ais-founder-on-death-drones-in-ukraine-and-the-ai-weapon-no-one-wants ; https://dronexl.co/2026/02/27/shield-ais-v-bat-weapons-deal-drones/ ; https://newmarketpitch.com/blogs/news/defense-tech-shield-ai-overvalued ; https://www.revenuememo.com/p/who-owns-shield-ai
