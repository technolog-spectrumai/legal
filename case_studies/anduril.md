# Case study: Anduril — od wieży na granicy do 61 mld USD, czyli neo-prime z Doliny Krzemowej

Dokument wewnętrzny Basilisk Systems, informacyjny. Nie jest opinią prawną ani rekomendacją inwestycyjną i nie zmienia umowy spółki. Jedno ze studiów przypadku o rozwoju i finansowaniu firm obronnych, robotyki i fizycznego AI (przegląd i porównanie: `case_studies/README.md`). Opisuje wzorzec „neo-prime": oprogramowanie jako pierwszy produkt, cywilny szybki klient jako pierwszy przychód, sprzęt kupowany przejęciami, kontrakty prototypowe przekształcone w programy of record, i cenę tego modelu (ok. 1 mld USD straty rocznie). Odesłania do umowy według `psa.tex` w wersji 0.9.4-C (numery § według `spis_tresci.md`); uzupełnia `jurisdictions/usa.md`, `case_studies/shield_ai.md` (model licencyjny) i `vc.md` sekcja 11.

Stan na 30 września 2026 r. Oznaczenia wiarygodności: **[Z]** — fakt z dokumentu pierwotnego (komunikat spółki, partnera, zamawiającego, dokument urzędowy); **[M]** — doniesienie prasowe albo baza danych; **[W]** — wiedza ogólna o prawie albo praktyce rynkowej; **[?]** — szacunek, w tym własne obliczenie z cytowanych liczb, albo teza niepotwierdzona. Uwaga metodyczna: strony źródłowe były w tej sesji niedostępne do pełnego odczytu (blokada sieciowa); fakty pochodzą ze streszczeń wyszukiwarki. Anduril nie publikuje zbadanych wyników; przychody to szacunki agregatorów i deklaracje spółki w prasie; kwoty i wyceny rund do serii D pochodzą wyłącznie z agregatorów.

---

## 1. Główny wniosek

Anduril to wzorzec, którego Basilisk **nie może skopiować w skali, ale może w sekwencji**. Założony 20 kwietnia 2017 r. przez Palmera Luckeya (Oculus) i czterech wspólników, w tym Trae'a Stephensa z Founders Fund, dostał seed 17,5 mln USD od Founders Fund w sierpniu 2017 r., pokazał wieżę Sentry z oprogramowaniem Lattice Departamentowi Bezpieczeństwa Wewnętrznego we wrześniu 2017 r. i sprzedał pierwsze wieże straży granicznej (CBP, 4,8 mln USD, 2018 r.) — cywilny, szybki klient przed Pentagonem. Potem dziewięć rund do serii H 5 mld USD przy 61 mld USD (13 maja 2026 r., Thrive i a16z; ok. 11,3 mld USD łącznie), przejęcie rocznie od 2021 r. (Area-I, Dive, Adranos, Blue Force, Numerica, Klas), skoki z kontraktów prototypowych (SOCOM 967,6 mln USD, CCA) do programów of record (produkcja Fury od czerwca 2026 r., Ghost Shark 1,7 mld AUD, IVAS 22 mld USD przejęty od Microsoftu, umowa ramowa Armii do 20 mld USD, Barracuda ≥3 000 sztuk), fabryka Arsenal-1 w Ohio za 910 mln USD i spółki zależne w Australii, UK, Tajwanie i Japonii. Przychód ok. 150 mln USD (2021 r.) → 2,2 mld USD (2025 r.) → prognoza 4,3 mld USD (2026 r.) przy ok. 1 mld USD straty i 800–900 mln USD spalania gotówki; IPO „za kilka lat, najpierw rentowność". Dla Basiliska: Lattice było pierwszym produktem, ale każdy duży kontrakt od 2021 r. jest zakotwiczony w sprzęcie; w Europie nawet Anduril wchodzi przez Rheinmetall z hasłem „europejskiej suwerenności" — czyli przez to, co polska P.S.A. ma z definicji.

---

## 2. Profil

| Element | Treść | Wiar. |
|---|---|---|
| Nazwa i forma | Anduril Industries Inc.; „kalifornijska firma technologii obronnych" (Costa Mesa); stan rejestracji niepotwierdzony | [M]/[?] |
| Założenie | 20 kwietnia 2017 r.; Palmer Luckey (założyciel Oculusa, twarz firmy), Trae Stephens (ex-Palantir, partner Founders Fund; przewodniczący wykonawczy), Brian Schimpf (prezes), Matt Grimm, Joe Chen | [M]/[Z] |
| Produkty | Lattice (platforma oprogramowania: fuzja sensorów, model 3D otoczenia); wieże Sentry; drony Ghost/Ghost-X; amunicja krążąca Altius (z Area-I); Roadrunner; pociski Barracuda; myśliwiec bezzałogowy Fury/YFQ-44A (z Blue Force); pojazdy podwodne Dive i Ghost Shark; gogle IVAS/SBMC; silniki rakietowe (Adranos); radary i C2 (Numerica); komputery (Klas) | [M] |
| Klienci | CBP, USMC, SOCOM, US Army, USAF, US Navy, Australia, Tajwan, UK (dla Ukrainy), Japonia | [M]/[Z] |
| Zatrudnienie | 2 801 (2023 r.) → 9 308 (marzec 2026 r.) → 9 670 (31 lipca 2026 r.); agregatory | [M] |
| Spółki zagraniczne | Australia (Sydney: inżynieria, produkcja Ghost Shark od maja 2022 r.); UK (dostawca Altius dla Ukrainy); Tajwan (luty 2025 r., z MND i NCSIST); Anduril Industries Japan G.K. (3 grudnia 2025 r., Tokio) | [Z]/[M] |

---

## 3. Jak zaczęli: kapitał początkowy i pierwsze lata

- **Urodzony w funduszu.** Pomysł powstał na wyjeździe Founders Fund, gdy Luckey poznał Stephensa „szukającego kolejnego dużego startupu obronnego"; seed 17,5 mln USD od Founders Fund w sierpniu 2017 r. (wycena ok. 88 mln USD wg wpisu w mediach społecznościowych, niska wiarygodność) **[M]/[?]**. Kapitału własnego założycieli żadne źródło nie kwantyfikuje **[?]**.
- **Produkt w pięć miesięcy.** Wieża Sentry na energię słoneczną z Lattice zademonstrowana DHS we wrześniu 2017 r. **[M]**.
- **Klient cywilny przed Pentagonem.** Pilot czterech wież w sektorze San Diego (początek 2018 r.) w nowym Biurze Innowacji CBP; kontrakt 4 833 000 USD na „sprzęt nadzoru granicznego" (ok. 10 wież); potem 56 wież i plan 140 kolejnych; późniejsza umowa 363 mln USD na wieże XR Sentry **[Z]/[M]**.
- **Seria A po 14 miesiącach:** 41 mln USD (czerwiec 2018 r., Founders Fund, SV Angel, Human Capital); seria B 127 mln USD (wrzesień 2019 r., Founders Fund i General Catalyst; a16z, 8VC, Lux) przy ok. 1,04 mld USD **[M]**.
- **Przychód ok. 150 mln USD w pierwszych pięciu latach** (2021 r.) **[M]**; wczesny kontrakt USMC na nadzór antywtargnięciowy (data nieustalona).
- **Wniosek:** szybki, niskoprogowy nabywca cywilny (CBP) pozwolił sprawdzić Lattice w terenie przed programami DoD **[?]**.

---

## 4. Oś czasu

| Data | Zdarzenie | Wiar. |
|---|---|---|
| 20 kwietnia 2017 | założenie | [M] |
| sierpień 2017 | seed 17,5 mln USD (Founders Fund) | [M] |
| wrzesień 2017 | demo Sentry dla DHS | [M] |
| 2018 | pilot i kontrakt CBP 4,8 mln USD; czerwiec: seria A 41 mln USD | [Z]/[M] |
| wrzesień 2019 | seria B 127 mln USD, ok. 1,04 mld USD | [M] |
| lipiec 2020 | seria C 200 mln USD, 1,92 mld USD | [M] |
| kwiecień 2021 | przejęcie Area-I (Altius); czerwiec: seria D 450 mln USD, ok. 4,7 mld USD (Elad Gil) | [M] |
| 19 stycznia 2022 | SOCOM: partner integracji C-UAS, IDIQ do 967,6 mln USD (OTA, 12 oferentów, do 2032 r.) | [M] |
| luty–maj 2022 | przejęcie Dive Technologies; start Ghost Shark w Australii (140 mln AUD współfinansowane z rządem) | [M] |
| grudzień 2022 | seria E 1,48 mld USD, 8,5 mld USD (Valor) | [M] |
| czerwiec i wrzesień 2023 | przejęcia Adranos (silniki rakietowe) i Blue Force Technologies (Fury) | [M] |
| 24 kwietnia 2024 | USAF wybiera Anduril i General Atomics do CCA Increment 1 (pokonani Lockheed, Northrop, Boeing) | [M] |
| czerwiec 2024 | zgoda Departamentu Stanu na sprzedaż 291 Altius-600M-V Tajwanowi (300 mln USD) | [Z]/[M] |
| sierpień 2024 | seria F 1,5 mld USD, ok. 14 mld USD (Sands, Founders Fund) | [M] |
| wrzesień–listopad 2024 | Ghost-X wybrany przez Armię; Ghost-X i Altius w Replicator 1.2; CDR CCA | [Z]/[M] |
| styczeń 2025 | Arsenal-1 (Ohio): 910,5 mln USD capex, 4 008 miejsc pracy do 2035 r.; przychód 2024 r. ok. 1 mld USD; plan tender offer dla pracowników 100 mln USD | [M] |
| 11 lutego – 10 kwietnia 2025 | nowacja kontraktu IVAS (22 mld USD) z Microsoftu na Anduril; Armia nie planuje masowego zakupu IVAS 1.2, rusza recompete SBMC (Anduril 159 mln USD prototyp, z Metą) | [M] |
| 6 marca 2025 | UK zamawia ok. 30 mln GBP Altius dla Ukrainy (International Fund for Ukraine) | [M] |
| 5 czerwca 2025 | seria G 2,5 mld USD, 30,5 mld USD (Founders Fund 1 mld USD, ponad 8× nadsubskrypcja); 10 czerwca Luckey: „na pewno będziemy spółką publiczną" | [M] |
| 18 czerwca 2025 | partnerstwo strategiczne z Rheinmetallem: europejskie warianty Barracuda i Fury, silniki rakietowe, integracja z Battlesuite; „suwerenność europejska", produkcja lokalna „na stole" | [Z] |
| 10 września 2025 | Australia: 1,7 mld AUD na produkcję Ghost Shark (5 lat); fabryka w Sydney i pierwszy pojazd w listopadzie | [Z]/[M] |
| 3 grudnia 2025 | spółka w Japonii | [Z] |
| 13 marca 2026 | umowa ramowa Armii do 20 mld USD (5+5 lat), konsoliduje ponad 120 działań zakupowych (Lattice, sprzęt, dane, compute), bez narzutów pass-through | [Z]/[M] |
| 24 marca 2026 | produkcja seryjna YFQ-44A Fury w Arsenal-1, 3 miesiące przed terminem | [M] |
| 13 maja 2026 | seria H 5 mld USD, 61 mld USD (Thrive, a16z); umowa ramowa Departamentu Wojny na Barracuda-500M: ≥3 000 sztuk w 3 lata, ≥1 000 rocznie, dostawy od I poł. 2027 r.; zakład w Kalifornii za ponad 40 mln USD | [Z]/[M] |
| 17 czerwca 2026 | decyzja produkcyjna USAF dla FQ-44A (Anduril) i FQ-42A (GA) | [M] |
| 9 lipca 2026 | Luckey: IPO nie „w środku cyklu hossy", „w ciągu kilku lat", najpierw rentowność | [M] |
| 24–27 lipca 2026 | doniesienia o rundzie przy ok. 100 mld USD (bez potwierdzenia zamknięcia); pierwszy Fury z Ohio, 557 dni od ogłoszenia projektu | [M]/[Z] |

---

## 5. Finansowanie: dziewięć rund i jeden sponsor

| Runda | Data | Kwota | Wycena po pieniądzu | Lead / inwestorzy | Wiar. |
|---|---|---|---|---|---|
| Seed | sierpień 2017 | 17,5 mln USD | ok. 88 mln USD (wpis społecznościowy) | Founders Fund | [M]/[?] |
| A | czerwiec 2018 | 41 mln USD | — | Founders Fund; SV Angel, Human Capital | [M] |
| B | wrzesień 2019 | 127 mln USD | ok. 1,04 mld USD | Founders Fund, General Catalyst; a16z, 8VC, Lux | [M] |
| C | lipiec 2020 | 200 mln USD | 1,92 mld USD | — | [M] |
| D | czerwiec 2021 | 450 mln USD | ok. 4,7 mld USD | Elad Gil | [M] |
| E | grudzień 2022 | 1,48 mld USD | 8,5 mld USD | Valor Equity Partners | [M] |
| F | sierpień 2024 | 1,5 mld USD | ok. 14 mld USD | Sands Capital, Founders Fund | [M] |
| G | 5 czerwca 2025 | 2,5 mld USD | 30,5 mld USD | Founders Fund (1 mld USD) | [M] |
| H | 13 maja 2026 | 5 mld USD | 61 mld USD | Thrive Capital, a16z | [M] |
| (rozmowy) | lipiec 2026 | — | ok. 100 mld USD | — | [M] |

- Suma rund ok. 11,3 mld USD według własnego rachunku (agregator Clay podaje „ponad 6,9 mld USD w dziewięciu rundach" — rozbieżność) **[?]**.
- Founders Fund prowadził seed, A, B, F i G: jeden sponsor przez dziewięć lat obniżał ryzyko sygnału w każdej rundzie **[?]**.
- Płynność: tender offer 100 mln USD dla pracowników (plan ze stycznia 2025 r.); RSU; Forge dla inwestorów akredytowanych; implikowana wycena wtórna ok. 100 mld USD po serii H **[M]**.
- Instrumenty: wyłącznie wycenione akcje uprzywilejowane; brak konwertowalnych i venture debt w źródłach **[?]**.
- Mnożniki: 61 mld USD to ok. 28× przychód 2025 r. i ok. 14× prognozy 2026 r.; 100 mld USD to ok. 23× prognozy **[?]**.

---

## 6. Giełda

Nienotowana. Czerwiec 2025 r.: „na pewno" publiczna, bo „nie ma drogi" do programów za bilion dolarów (F-35) bez giełdy; lipiec 2026 r.: nie w hossie, „w ciągu kilku lat", po rentowności; brak S-1 **[M]**. Jedna analiza twierdzi, że rentowność dopiero w 2030 r. (atrybucja niezweryfikowana) **[?]**.

---

## 7. Wzrost w liczbach

| Rok | Przychód (szacunki) | Wynik | Pracownicy | Wycena | Wiar. |
|---|---|---|---|---|---|
| 2021 | ok. 150 mln USD | — | — | 4,7 mld USD | [M] |
| 2022 | ok. 236 mln USD | — | — | 8,5 mld USD | [M] |
| 2023 | ok. 342 mln USD (alt. 420) | — | 2 801 | — | [M] |
| 2024 | ok. 1 mld USD (podwojenie) | — | — | 14 mld USD | [M] |
| 2025 | 2,2 mld USD (+120 %) | — | — | 30,5 mld USD | [M] |
| 2026 (prognoza) | ok. 4,3 mld USD | ok. −1 mld USD; spalanie 800–900 mln USD | 9 670 (lipiec) | 61 mld USD | [M] |

- Moce: Arsenal-1 5 mln stóp kw. na 500 akrach; Fury 150 rocznie; Fury, Roadrunner, Barracuda i platforma niejawna w produkcji do końca 2026 r.; Barracuda ≥1 000 rocznie od 2027 r. **[M]/[Z]**.
- Backlog i marże: nieujawnione; kontrakt Armii to pułap, nie zaksięgowany przychód **[?]**.

---

## 8. Struktura właścicielska, kontrola i ład korporacyjny

- Rada: pięciu założycieli (Schimpf, Luckey, Chen, Stephens, Grimm) według agregatorów; miejsca inwestorów nieujawnione **[M]**.
- Brak ujawnionej struktury dwuklasowej ani klauzul ochronnych założycieli; udział Luckeya szacowany na 5–15 % (niepotwierdzony) **[M]/[?]**; kontrola wykonywana najpewniej przez skład rady i sojusz z Founders Fund, nie przez akcje uprzywilejowane głosowo **[?]**.
- Brak udziału państwa **[?]**; pracownicy z RSU i tender offers **[M]**.
- Lobbing: największy klient obronny lobbujący w sprawach AI w 2025 r. (35 lobbystów); własny PAC **[M]/[Z]**.

---

## 9. Ocena: co zadziałało, co nie

**Zadziałało**
- Wejście przez oprogramowanie i szybkiego klienta cywilnego (CBP), potem OTA i prototypy (SOCOM, CCA) zamiast FAR Part 15.
- Własny sprzęt kupowany przejęciami, żeby Lattice zawsze miało „ciało" do sprzedania.
- „Buduj przed kontraktem": własne finansowanie oprzyrządowania (zakład Barracuda, partia Altius dla Tajwanu, współfinansowanie Ghost Shark) i szybkość dostaw jako argument sprzedażowy; Fury 3 miesiące przed terminem, Ghost Shark przed czasem, Tajwan 6 miesięcy od podpisu.
- Przejmowanie kłopotliwych albo skonsolidowanych programów (IVAS od Microsoftu, umowa ramowa Armii) jako droga do programu of record z pominięciem klasycznego konkursu.
- Ekspansja zagraniczna prowadzona kontraktem: każda spółka zależna po konkretnym programie (Australia 2022, Tajwan 2025, Japonia 2025, UK).

**Nie zadziałało albo kosztowało**
- Ok. 1 mld USD straty i 800–900 mln USD spalania w 2026 r., finansowane megarundami.
- „Najbardziej kontrowersyjny startup technologiczny" (Bloomberg Businessweek): autonomia śmiercionośna, nadzór graniczny, protesty (Seattle, lipiec 2026 r.).
- Spory: pozew założyciela Area-I o ≥15 mln USD (zaniżony earn-out); pozew przeciw startupowi absolwentów (Salient Motion) i memo Luckeya „bez litości"; kultura „wyczerpujących godzin".
- Ryzyko programów: IVAS z „latami problemów projektowych"; raport o katastrofach dronów w Ukrainie (listopad 2025 r., szczegóły nieodczytane).
- Brak zbadanych finansów: inwestorzy nie znają marż, backlogu ani koncentracji do czasu S-1.

---

## 10. Wnioski dla Basiliska: mapowanie na projekt umowy

Oznaczenia stanu jak w `vc.md` sekcja 8: **OK**, **CZ**, **BRAK**, **KOL**, **DEC**.

| Lekcja z Andurila | Gdzie u nas | Stan | Co zrobić i kiedy |
|---|---|---|---|
| **Sekwencja: szybki klient cywilny → OTA i prototypy → własny nośnik dla oprogramowania → produkcja lokalna u sojusznika** | `regulations.md` sekcja 4 (bramki G1–G6); `psa_todo.md` sekcja 6; `plan_prac.md` etap C | CZ | Odpowiedniki: klient cywilny (infrastruktura krytyczna, straż graniczna) przed MON; EDF, EDIP, DIANA i Brave1 jako „OTA"; integracja z platformą polskiego producenta przed przetargiem |
| **Czyste oprogramowanie nie dochodzi do budżetów programów of record bez platformy albo prima** (umowa Armii wiąże Lattice ze sprzętem) | § 33; `case_studies/shield_ai.md` sekcja 10 (A-GRA jako wyjątek) | DEC | Zdecydować: dron referencyjny (JV z producentem) albo firma integracja OEM; nie własna produkcja |
| **Nawet archetypowy disruptor wchodzi do Europy przez prime'a i hasło suwerenności** (Rheinmetall, czerwiec 2025 r.) | § 11; `kryteria.md` K1–K2; `jurisdictions/README.md` sekcja 1 | OK | Polska własność w 100 % to kwalifikowalność do EDF i SAFE, którą Anduril musi kupić partnerem; napisać to wprost w każdym wniosku konsorcjalnym |
| **Jeden sponsor przez dziewięć lat** (Founders Fund w 5 z 9 rund) | `vc.md` sekcje 3–4; § 32 (Kwalifikowana Runda) | CZ | Szukać inwestora z mandatem na kolejne rundy (NIF, PFR, EIF); w umowie inwestycyjnej pro-rata dla lead inwestora |
| **„Buduj przed kontraktem" w skali, którą można sfinansować samemu** | § 31 ust. 1; `case_studies/tekever.md` sekcja 10 | DEC | Zamiast fabryki: zintegrować autonomię z dwiema platformami przed pierwszym przetargiem MON |
| **Earn-out i spory z przejętymi założycielami** (Area-I) | § 25 ust. 1 lit. e (zbycie 75 %), `vc.md` sekcja 8 wiersz „Exit" | BRAK | Przy exicie do nabywcy typu Anduril: earn-out z obiektywnymi kamieniami i arbitrażem; klauzula w umowie akcjonariuszy |
| **Płynność pracowników przez tender offers** (100 mln USD, 2025 r.) | § 27 (ESOP), § 12–14 | CZ | Zaplanować okna odsprzedaży w rundach od serii B (wzór ICEYE) |
| **Spalanie 800–900 mln USD finansowane rundami**: model nie do skopiowania | `plan_prac.md`; `vc.md` sekcja 11 | OK | Kopiować sekwencję, nie burn |

---

## 11. Luki i rzeczy do sprawdzenia

- Kapitał założycieli i wycena seedu (tylko wpis społecznościowy); siedziba prawna; nazwa spółki brytyjskiej; zatrudnienie w UK i Japonii.
- Zbadane finanse (przychód, marża, backlog, gotówka); rok rentowności; czy runda przy 100 mld USD została zamknięta.
- Cap table, prawa głosu, miejsca inwestorów w radzie, pula opcji; warunki tender offer 2025 r. i ewentualnego w 2026 r.
- Forma prawna partnerstwa z Rheinmetallem (JV czy teaming) i Anduril Australia (FOCI); daty i ceny przejęć Numerica i Klas; data nagrody SBMC.
- Treść raportu Bloomberga o katastrofach dronów w Ukrainie; roczne wydatki lobbingowe.

---

## 12. Źródła sprawdzone 30 września 2026 r.

- Profil i początki — https://en.wikipedia.org/wiki/Anduril_Industries ; https://en.wikipedia.org/wiki/Trae_Stephens ; https://thedynamics.ai/articles/anduril-history ; https://www.anduril.com/anduril-leadership ; https://www.revenuememo.com/p/who-owns-anduril ; https://privacyinternational.org/report/5704/dual-use-tech-anduril-example ; https://www.ohchr.org/sites/default/files/Documents/Issues/Racism/SR/RaceBordersDigitalTechnologies/Andurils_New_Border_Surveillance_Contract_With_the_US_Marine_Corps_and_CBP.pdf ; https://fedscoop.com/anduril-sentry-towers-cbp/ ; https://acquisitiontalk.com/2022/08/anduril-grows-revenue-to-150m-in-its-first-five-years/ ; https://builtin.com/articles/what-is-anduril ; https://www.reveliolabs.com/companies/anduril-industries/employees
- Rundy — https://www.clay.com/dossier/anduril-industries-funding ; https://techcrunch.com/2025/06/05/anduril-raises-2-5b-at-30-5b-valuation-led-by-founders-fund/ ; https://aviationweek.com/defense/supply-chain/anduril-valued-305-billion-after-series-g-funding-round ; https://techcrunch.com/2026/05/13/anduril-raises-5b-doubles-valuation-to-61b/ ; https://www.cnbc.com/2026/05/13/anduril-valuation-defense-tech-funding-boom.html ; https://www.bloomberg.com/news/articles/2026-05-13/anduril-valued-at-61-billion-in-round-led-by-thrive-andreessen ; https://www.defensenews.com/industry/techwatch/2026/07/24/anduril-in-talks-to-raise-funding-at-about-100-billion-valuation/ ; https://x.com/theinformation/status/1879660513220833292 ; https://forgeglobal.com/insights/how-to-invest-in-anduril-pre-ipo/
- Kontrakty — https://www.govconwire.com/articles/anduril-wins-968m-socom-counter-uas-tech-integration-contract ; https://breakingdefense.com/2022/01/anduril-nets-biggest-dod-contract-to-date-signifier-or-outlier-for-defense-start-ups/ ; https://defensescoop.com/2024/04/24/anduril-general-atomics-air-force-cca-program/ ; https://www.defensenews.com/unmanned/2024/11/13/pentagon-announces-new-batch-of-drones-for-replicator-program/ ; https://breakingdefense.com/2025/02/microsoft-announces-plan-to-slide-22-billion-ivas-contract-over-to-anduril/ ; https://breakingdefense.com/2025/03/army-continues-iterating-on-ivas-not-currently-planning-mass-buy-of-1-2-version/ ; https://war.gov/News/Contracts/Contract/Article/4434754/contracts-for-march-13-2026 ; https://www.nextgov.com/defense/2026/03/army-anduril-enter-new-20b-enterprise-agreement/412153/ ; https://www.anduril.com/news/anduril-department-of-war-sign-production-agreement-for-surface-launched-barracuda-500m ; https://www.twz.com/air/usaf-orders-both-general-atomics-fq-42-and-andurils-fq-44-into-production ; https://theaviationist.com/2026/03/24/yfq-44a-fury-cca-is-now-in-production/ ; https://www.jobsohio.com/newsroom/news-press/first-ohio-built-fury-rolls-off-andurils-arsenal-1-production-line ; https://www.manufacturingdive.com/news/anduril-industries-columbus-ohio-1-billion-arsenal-1-hyperscale-facility/737780/
- Zagranica — https://www.minister.defence.gov.au/media-releases/2025-09-10/equipping-royal-australian-navy-next-generation-autonomous-undersea-vehicles ; https://www.innovationaus.com/1-7bn-defence-deal-propels-ghost-shark-robo-subs-into-production/ ; https://www.anduril.com/news/ghost-shark-factory-opens-in-sydney-first-vehicle-off-the-line-ahead-of-schedule-ready-for ; https://www.c4isrnet.com/battlefield-tech/2024/06/20/us-approves-loitering-munitions-sale-for-taiwans-porcupine-strategy/ ; https://www.flightglobal.com/military-uavs/taiwan-receives-first-anduril-altius-600m-loitering-munitions/164081.article ; https://www.flightglobal.com/defence/uk-orders-andurils-altius-loitering-munitions-for-donation-to-ukraine/162099.article ; https://www.anduril.com/news/anduril-expands-to-japan-advancing-its-mission-to-transform-allied-defense ; https://www.tectonicdefense.com/anduril-expands-to-taiwan/ ; https://www.rheinmetall.com/en/media/news-watch/news/2025/06/2025-06-18-strategic-partnership ; https://www.shephardmedia.com/news/air-warfare/domestic-production-on-the-table-as-anduril-poised-to-bring-capabilities-to-european-defence-market/
- Wyniki i IPO — https://sacra.com/research/anduril-the-nintendo-of-american-dynamism/ ; https://sacra.com/c/anduril/ ; https://finance.yahoo.com/news/anduril-expects-double-sales-lose-211557605.html ; https://www.theinformation.com/articles/anduril-hot-ticket-despite-burning-800-million-cash ; https://www.cnbc.com/2025/06/10/anduril-palmer-luckey-ipo.html ; https://www.cnbc.com/2026/07/09/anduril-ceo-ipo-defense.html ; https://www.forex.com/en-us/news-and-analysis/anduril-ipo-everything-you-need-to-know-about-anduril/
- Krytyka — https://www.britannica.com/money/Anduril-Industries ; https://news.bloomberglaw.com/esg/anduril-industries-hit-with-15-million-lawsuit-over-drone-deal ; https://www.courtlistener.com/docket/67766126/anduril-industries-inc-v-salient-motion-inc/ ; https://www.theinformation.com/articles/andurils-luckey-warns-of-no-mercy-after-suing-startup-launched-by-alums ; https://www.geekwire.com/2026/defense-tech-giant-anduril-eyes-new-funding-at-100b-valuation-as-seattle-expansion-draws-protests/ ; https://www.bnnbloomberg.ca/business/2025/11/27/us-defense-firm-anduril-faces-setbacks-from-drone-crashes/ ; https://www.citizen.org/article/generative-influence/ ; https://projects.propublica.org/itemizer/committee/C00763623/2026
