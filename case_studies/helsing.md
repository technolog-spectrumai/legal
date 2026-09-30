# Case study: Helsing — 100 mln EUR od jednego inwestora przed pierwszym kontraktem i spór o HX-2

Dokument wewnętrzny Basilisk Systems, informacyjny. Nie jest opinią prawną ani rekomendacją inwestycyjną i nie zmienia umowy spółki. Jedno ze studiów przypadku o rozwoju i finansowaniu firm obronnych, robotyki i fizycznego AI (przegląd i porównanie: `case_studies/README.md`). Helsing to europejski punkt odniesienia: start od oprogramowania, jeden inwestor kotwiczny (Prima Materia Daniela Eka), szybki zwrot ku sprzętowi (HF-1, HX-2, SG-1 Fathom, CA-1 Europa), AI wewnątrz platform primów (Saab, Airbus), „suwerenność europejska" jako produkt i kontestowany wynik w Ukrainie. Odesłania do umowy według `psa.tex` w wersji 0.9.4-C (numery § według `spis_tresci.md`); uzupełnia `jurisdictions/niemcy_francja.md`, `jurisdictions/estonia.md`, `case_studies/shield_ai.md` i `vc.md` sekcje 4 i 11.

Stan na 30 września 2026 r. Oznaczenia wiarygodności: **[Z]** — fakt z dokumentu pierwotnego (komunikat spółki, partnera, zamawiającego, rejestr); **[M]** — doniesienie prasowe albo baza danych; **[W]** — wiedza ogólna o prawie albo praktyce rynkowej; **[?]** — szacunek albo teza niepotwierdzona. Uwaga metodyczna: strony źródłowe były w tej sesji niedostępne do pełnego odczytu (blokada sieciowa); fakty pochodzą ze streszczeń wyszukiwarki. Przychody Helsinga są nieprzejrzyste: od 9,6 mln EUR (2023 r., Sacra) przez „502 mln USD" (Multiples, 2026 r.) po „ok. 1 mld USD" (2024 r., Sacra PDF) — liczby wzajemnie sprzeczne, żadna pierwotna.

---

## 1. Główny wniosek

Helsing to **dowód, że w Europie kapitał cierpliwy zastąpił amerykańską drabinę SBIR i OTA**: założony w 2021 r. w Monachium przez Torstena Reila, Gundberta Scherfa i Niklasa Köhlera, po jedenastu miesiącach zamknął serię A 102,5 mln EUR, z czego 100 mln EUR od Prima Materia (Daniel Ek), przy przychodzie rzędu 1 mln EUR (2022 r.) i bez ujawnionego kontraktu. Potem: seria B 209 mln EUR (General Catalyst, wrzesień 2023 r.), C 450 mln EUR (lipiec 2024 r.), D 600 mln EUR przy 12 mld EUR (Prima Materia, 17 czerwca 2025 r.) i E 1,8 mld USD przy 18 mld USD (13 lipca 2026 r.; Dragoneer, Goldman, JPMorgan, CPP, ICONIQ) — razem ok. 3 mld EUR; rada pod współprzewodnictwem Eka i byłego prezesa Airbusa Toma Endersa; „bez planów IPO", ok. 80 % kapitału w rękach europejskich przed serią E. Zamówienia: 4 000 HF-1 i 6 000 HX-2 dla Ukrainy, Bundeswehra 269 mln EUR na 4 300 HX-2 z ramą do 1 mld EUR (25 lutego 2026 r.), Eurofighter EW 258 mln EUR przez Saab (Cirra w Arexis), chmura bojowa CFSN 580 mln EUR (pierwsze 220 mln EUR, 8 lipca 2026 r.), Uranos KI z Airbusem, UK 350 mln GBP (Trinity House, fabryka w Plymouth), Helsing Estonia OÜ, Grob Aircraft kupiony (czerwiec 2025 r.), CA-1 Europa (lot 2027 r.). Cena: Bloomberg (styczeń 2026 r.): tylko 25 % HX-2 wystartowało w testach 14. pułku, brak obiecanych funkcji AI, podatność na WRE, Ukraina wstrzymała zamówienia; Welt: 5 trafień na 14; zarzuty zawyżonych cen i lobbingu (kwiecień 2025 r.); porażka we Francji (Dassault stawia na Harmattan AI). Dla Basiliska: najszybsza droga do pieniędzy programu of record to być certyfikowaną warstwą AI w kontrakcie prima; 100 % europejska własność to aktywo sprzedażowe, które Helsing reklamuje, a P.S.A. ma z definicji; a Helsing nie ma śladu w Polsce mimo 43,7 mld EUR SAFE.

---

## 2. Profil

| Element | Treść | Wiar. |
|---|---|---|
| Nazwa i forma | Helsing GmbH, Monachium; Helsing Limited (UK); Helsing Estonia OÜ (rej. 17024826, Tallinn); spółka we Francji (od marca 2022 r.); dyrektor zarządzający w Ukrainie (Andrij Szewczenko, działalność od 2022 r.); obecność w Sztokholmie; Grob Aircraft SE (Tussenhausen, ok. 275 osób) przejęty | [Z]/[M] |
| Założenie | 2021 r.; Torsten Reil, Gundbert Scherf, Niklas Köhler, „by dać sztuczną inteligencję dla ochrony naszych demokracji"; tła zawodowe (Reil ex-NaturalMotion, Scherf ex-McKinsey i BMVg, Köhler badacz AI) niepotwierdzone w tej sesji | [M]/[?] |
| Produkty | drony uderzeniowe HF-1 i HX-2 (elektryczny X-wing, do 100 km); UCAV CA-1 Europa z pilotem AI Centaur (ok. 11 m, 4 t, lot 2027 r., służba 2029 r.); Cirra (EW AI dla Eurofightera); Lura (akustyczne AI) i szybowiec podwodny SG-1 Fathom (60 kg, 3 miesiące patrolu); Uranos KI (stanowisko dowodzenia ISR); chmura bojowa CFSN; współpraca z Mistral (VLA) | [Z]/[M] |
| Rada | współprzewodniczący Daniel Ek i Tom Enders; Jeannette zu Fürstenberg, Denis Mercier; założyciele | [Z] |
| Zatrudnienie | 218 (2023 r.) → 700–900 (2026 r.; 884 na 31 sierpnia 2026 r.) plus ok. 275 w Grob; 147 otwartych stanowisk | [M] |
| Fabryki | Resilience Factory RF-1 (południowe Niemcy, ponad 1 000 HX-2 miesięcznie), RF-2 (razem ok. 2 500 miesięcznie); Plymouth (SG-1, listopad 2025 r.); Grob w Mattsies (18 mln EUR) | [Z]/[M] |

---

## 3. Jak zaczęli: kapitał początkowy i pierwsze lata

- **Bez seedu.** Jedenaście miesięcy po założeniu: seria A 102,5 mln EUR (listopad 2021 r.), w tym 100 mln EUR od Prima Materia; zapowiedź ekspansji do Francji **[M]**. Kapitału założycieli, aniołów ani pierwszego płatnego kontraktu nie odnaleziono **[?]**.
- **Oprogramowanie na cudzych platformach.** Platforma z pierwszych lat: AI integrujące dane z podczerwieni, wideo, sonaru i RF z sensorów na pojazdach wojskowych w obraz pola walki w czasie rzeczywistym **[M]**.
- **Francja (marzec 2022 r.) i Ukraina (od 2022 r.)** — obecność bezpośrednio przy wojsku i przemyśle **[M]**.
- **Przychód:** 1,2 mln EUR (2022 r.), 9,6 mln EUR (2023 r., +721 %) wg Sacra; GetLatka podaje 36,7 mln USD za 2023 r. (sprzeczność) **[?]**.
- **Jednorożec po dwóch latach:** seria B 209 mln EUR (General Catalyst, wrzesień 2023 r.) **[Z]/[M]**.
- **Wniosek:** ok. 100 mln EUR kapitału przy ok. 1 mln EUR przychodu to finansowanie laboratorium deep tech, nie startupu; warunkiem był jeden inwestor gotowy finansować lata oprogramowania przed przychodem — polska P.S.A. musi to zastąpić EDF, EDIP, zamówieniami z SAFE i współpracą z Ukrainą **[?]**.

---

## 4. Oś czasu

| Data | Zdarzenie | Wiar. |
|---|---|---|
| 2021 | założenie w Monachium | [M] |
| listopad 2021 | seria A 102,5 mln EUR (Prima Materia 100 mln EUR) | [M] |
| marzec 2022 | spółka we Francji; start działalności w Ukrainie | [M] |
| wrzesień 2023 | seria B 209 mln EUR (General Catalyst); jednorożec; doradca YPOG | [Z]/[M] |
| 5 czerwca 2024 | umowa ramowa z Airbus Defence and Space o AI dla Wingmana (ILA) | [Z] |
| lipiec 2024 | seria C 450 mln EUR (General Catalyst; Elad Gil, Accel, Saab, Lightspeed, Plural, Greenoaks), ok. 4,5 mld USD; łącznie 762 mln EUR; plan ekspansji bałtyckiej | [M] |
| listopad 2024 | zgoda rządu Niemiec na 4 000 HF-1 dla Ukrainy (produkowane z przemysłem ukraińskim, finansowane przez Niemcy) | [Z]/[M] |
| koniec 2024 | HX-2; Helsing Estonia OÜ; 70 mln EUR inwestycji w Bałtach w 3 lata | [M] |
| 13 lutego 2025 | 6 000 HX-2 dla Ukrainy; Resilience Factory RF-1 (>1 000 miesięcznie) | [Z] |
| kwiecień 2025 | Bloomberg: zarzuty zawyżonych cen i „usterkowego oprogramowania" od byłych pracowników, inwestorów i ekspertów | [M] |
| maj–czerwiec 2025 | Lura i SG-1 Fathom; Centaur lata na Gripenie E (3 loty nad Bałtykiem, od koncepcji do lotu w niecałe 6 miesięcy) | [Z]/[M] |
| 16–17 czerwca 2025 | przejęcie Grob Aircraft; seria D 600 mln EUR przy 12 mld EUR (Prima Materia; Accel, Lightspeed, Plural, GC, Saab, BDT & MSD) „na europejską suwerenność technologiczną" | [Z]/[M] |
| lipiec 2025 | UK: fabryka w Plymouth pod zobowiązaniem 350 mln GBP (Trinity House) | [M] |
| 25 września 2025 | CA-1 Europa w pełnej skali (Grob) | [M] |
| listopad 2025 | Uranos KI: kontrakty testowe dla Airbusa i Helsinga (ok. 136–170 mln EUR; Rheinmetall i Hensoldt odpadli); 19 listopada: 258 mln EUR z Saab Germany na EW Eurofightera (Cirra w Arexis, 3 lata); otwarcie Plymouth | [Z]/[M] |
| styczeń 2026 | Bloomberg: w testach 14. pułku wystartowało 25 % HX-2 (katapulty), brak trzech obiecanych komponentów AI, WRE zakłóca łącze, Ukraina wstrzymuje nowe zakupy; Welt: 5 trafień na 14; Helsing „odrzuca wiele ustaleń" | [M] |
| 25 lutego 2026 | Bundestag: 269 mln EUR na 4 300 HX-2 z ramą do 1 mld EUR (obok Stark Virtus 269 mln EUR) „pod ścisłymi warunkami" | [M] |
| luty 2026 | L'Express: „porażki we Francji", Dassault z 200 mln USD dla Harmattan AI | [M] |
| maj 2026 | doniesienia o rundzie Dragoneer ok. 1,2 mld USD przy 18 mld USD | [M] |
| 8 lipca 2026 | Bundestag: pierwsze ok. 220 mln EUR z 580 mln EUR na CFSN (chmura bojowa z upadłego FCAS; Helsing pokonał Airbus DS, MBDA Germany, Diehl) | [M] |
| 13 lipca 2026 | seria E 1,8 mld USD przy 18 mld USD (Dragoneer, Lightspeed, Disruptive, ICONIQ, Goldman Sachs Growth, JPMorganChase, CPP Investments, GC, Plural, StepStone); „największa runda startupu obronnego w Europie" | [Z]/[M] |
| 2026 | druga niemiecka Resilience Factory działa (ok. 1 000 miesięcznie, zapas 400–600) | [M] |

---

## 5. Finansowanie: pięć rund w pięć lat, ok. 3 mld EUR

| Runda | Data | Kwota | Po pieniądzu | Lead / inwestorzy | Wiar. |
|---|---|---|---|---|---|
| A | listopad 2021 | 102,5 mln EUR | — | Prima Materia (100 mln EUR) | [M] |
| B | wrzesień 2023 | 209 mln EUR | >1 mld USD | General Catalyst | [M] |
| C | lipiec 2024 | 450 mln EUR | ok. 4,5 mld USD | General Catalyst; Elad Gil, Accel, Saab, Lightspeed, Plural, Greenoaks | [M] |
| D | 17 czerwca 2025 | 600 mln EUR | 12 mld EUR | Prima Materia; Accel, Lightspeed, Plural, GC, Saab, BDT & MSD | [Z]/[M] |
| E | 13 lipca 2026 | 1,8 mld USD | 18 mld USD | Dragoneer, Lightspeed, Disruptive, ICONIQ, Goldman Sachs, JPMorganChase, CPP, GC, Plural, StepStone | [Z] |

- Reil przed D i E: 1,3 mld EUR zebrane, inwestorzy europejscy mają 80 % **[M]**; po serii E (Goldman, JPMorgan, CPP, ICONIQ) udział europejski najpewniej spadł **[?]**.
- Saab jest partnerem i akcjonariuszem (C i D) **[M]**.
- Secondaries: nieodnalezione; w serii E wymienieni „założyciele, pracownicy i kilka funduszy VC" **[Z]/[?]**.
- Mnożnik: przy 502 mln USD przychodu bieżącego 18 mld USD to ok. 36× (jak Shield AI); jeśli przychód 2025 r. był bliżej 100–200 mln EUR, mnożnik jest znacznie wyższy; przedstawiać przedział, nie punkt **[?]**.

---

## 6. Giełda

Nienotowana. Reil odrzuca pogłoski o IPO; Helsing „chce pozostać niezależny"; mimo to lista inwestorów serii E to kapitał crossover i pre-IPO **[M]/[?]**. Państwo niemieckie nie ma udziałów; pieniądz publiczny przychodzi kontraktami **[?]**.

---

## 7. Wzrost w liczbach

| Miara | Wartość | Wiar. |
|---|---|---|
| Przychód | 1,2 mln EUR (2022 r.), 9,6 mln EUR (2023 r.) wg Sacra; 36,7 mln USD (2023 r.) wg GetLatka; „502 mln USD" (2026 r.) wg Multiples; „ok. 1 mld USD" (2024 r.) wg Sacra PDF — sprzeczne | [?] |
| Wycena | >1 mld USD (2023 r.) → ok. 4,5 mld USD (2024 r.) → 12 mld EUR (2025 r.) → 18 mld USD (2026 r.) | [M]/[Z] |
| Zatrudnienie | 218 (2023 r.) → 700–900 (2026 r.) + 275 Grob | [M] |
| Moce | RF-1 >1 000 HX-2 miesięcznie; RF-1 + RF-2 ok. 2 500 miesięcznie; Plymouth „tysiące" szybowców | [Z]/[M] |
| Backlog (proxy) | HX-2 Bundeswehra 269 mln EUR (rama 1 mld EUR); Eurofighter EW 258 mln EUR; CFSN 580 mln EUR (220 mln EUR zatwierdzone); Uranos KI ok. 136–170 mln EUR z Airbusem; Ukraina 6 000 HX-2 + 4 000 HF-1 (wartości nieujawnione) | [M] |

---

## 8. Struktura właścicielska, kontrola i ład korporacyjny

- GmbH prowadzona przez założycieli; współprzewodniczący rady Ek (Prima Materia) i Enders (ex-Airbus) **[Z]**.
- Modelowany cap table (niska wiarygodność): Prima Materia ok. 14 %, General Catalyst ok. 16 %, Dragoneer ok. 11 %, założyciele i pracownicy ok. 24 %; „skoncentrowane prawa głosu założycieli" **[?]**.
- Klasy udziałów, prawa głosu, ESOP/VSOP, ewentualne przekształcenie w SE — nieodnalezione **[?]**.
- Legitymizacja przez radę (Enders, Mercier — były szef sztabu sił powietrznych Francji) i akcjonariusza-prima (Saab) **[M]**.

---

## 9. Ocena: co zadziałało, co nie

**Zadziałało**
- Inwestor kotwiczny finansujący lata oprogramowania przed przychodem.
- Wczesna obecność w Ukrainie: HF-1 z komponentami „praktycznie w całości" z Ukrainy, „dziesiątki milionów euro" zainwestowane lokalnie.
- AI wewnątrz platform primów: Cirra w Arexis Saaba (258 mln EUR), AI w Wingmanie Airbusa, Centaur na Gripenie w niecałe 6 miesięcy.
- Szybka konwersja niemieckiego dozbrojenia w zamówienia z ograniczoną konkurencją (HX-2, CFSN, Uranos KI); wygrane z Airbusem, Rheinmetallem, MBDA, Diehlem.
- „Suwerenność europejska" i Resilience Factories jako produkt; 80 % europejskiej własności jako argument.

**Nie zadziałało albo kosztowało**
- HX-2 w Ukrainie: 25 % startów, brak funkcji AI, podatność na WRE, wstrzymane zamówienia, 5 z 14 trafień; Bundestag kupił mimo to, ale z limitem 1 mld EUR i „ścisłymi warunkami".
- Zarzuty zawyżonych cen, lobbingu i „usterkowego oprogramowania" (Bloomberg, kwiecień 2025 r.); zarzut korupcji nieudowodniony.
- Porażka we Francji: Dassault wybiera Harmattan AI.
- Nieprzejrzyste finanse wobec 18 mld USD wyceny.
- Zwrot ku sprzętowi wystawia oprogramowanie na awarie wyrzutni i płatowców, które nie mają nic wspólnego z AI, a niszczą jego wiarygodność **[?]**.
- Brak jakiegokolwiek projektu EDF, zamówienia z SAFE i obecności w Polsce w odnalezionych źródłach **[?]**.

---

## 10. Wnioski dla Basiliska: mapowanie na projekt umowy

Oznaczenia stanu jak w `vc.md` sekcja 8: **OK**, **CZ**, **BRAK**, **KOL**, **DEC**.

| Lekcja z Helsinga | Gdzie u nas | Stan | Co zrobić i kiedy |
|---|---|---|---|
| **Kapitał kotwiczny zamiast drabiny SBIR/OTA**: 100 mln EUR przed kontraktem | `vc.md` sekcje 4 i 11; `psa_todo.md` sekcja 6; `jurisdictions/README.md` sekcja 3 | DEC | Bez Daniela Eka: EDF, EDIP, zamówienia MON z SAFE i współpraca z Ukrainą jako substytut cierpliwego kapitału; szukać inwestora kotwicznego z mandatem wielorundowym (NIF, Prima Materia-podobne family office z UE) |
| **Certyfikowana warstwa AI wewnątrz programu prima** (Cirra w Arexis, AI w Wingmanie) | § 33 ust. 3; `case_studies/shield_ai.md` sekcja 10; `case_studies/iceye.md` (JV) | BRAK | Cel etapu C: umowa podwykonawcza z PGZ, WB albo Saabem, w której autonomia roju jest wyodrębnionym pakietem z własnym IP (§ 26) |
| **Rządowe architektury referencyjne** (CFSN „dla przyszłych dostawców", A-GRA) | `regulations.md` sekcja 4; `psa_todo.md` sekcja 6 | BRAK | Zgodność interfejsów z niemieckim CFSN i amerykańskim A-GRA jako wymaganie produktowe |
| **Ukraina jako poligon i baza dostawców** (HF-1 z Ukrainy) | `jurisdictions/ukraina.md` sekcja 6; § 28 | DEC | Polska bliskość i Brave1 są tańsze niż dla Monachium; TOV albo spółka estońska po pierwszym grancie |
| **Suwerenność jako cecha produktu**: 80 % europejskiej własności, Resilience Factories | § 11; `kryteria.md` K1–K2; `jurisdictions/README.md` sekcja 1 | OK | P.S.A. w 100 % polska jest kwalifikowalna do EDF z definicji; dokumentować łańcuch własności (§ 11 ust. 4) jako aktywo sprzedażowe w każdym wniosku |
| **Zwrot ku sprzętowi = odpowiedzialność za wyrzutnie i płatowce** (HX-2) | § 33; `regulations.md` sekcja 2.2 | OK | Zostać przy oprogramowaniu; w umowach rozdzielić metryki autonomii od metryk platformy i wyrzutni |
| **Luka: brak Helsinga w Polsce mimo 43,7 mld EUR SAFE** | `jurisdictions/polska.md` sekcja 6; `case_studies/aps.md` sekcja 10 | DEC | Narracja „polskiego czempiona autonomii" jest wolna; MON i PGZ nie mają krajowego dostawcy warstwy AI roju |
| **Rada z byłym prezesem Airbusa i byłym szefem sztabu** | § 21 (Rada Dyrektorów), § 21 ust. 3 (Kryterium) | CZ | Dyrektor niewykonawczy z MON/NATO od etapu C (jak `destinus.md` sekcja 10) |
| **Krytyka cen i lobbingu przy zamówieniach z ograniczoną konkurencją** | § 29–30 (transakcje z podmiotami powiązanymi), § 23 ust. 2 (zgodność) | OK | Polityka antykorupcyjna i rejestr kontaktów z zamawiającym od pierwszej umowy z MON |

---

## 11. Luki i rzeczy do sprawdzenia

- Tła założycieli; kapitał przed serią A; pierwszy płatny kontrakt.
- Wyceny po pieniądzu serii A–C; czy seria E zawierała secondaries; klasy udziałów GmbH; ESOP; ewentualne przekształcenie w SE.
- Wiarygodny przychód (9,6 mln EUR → 502 mln USD → 1 mld USD); skonsolidowane zatrudnienie; nazwy spółek we Francji i Ukrainie; daty biur w Estonii i Sztokholmie; lokalizacja RF-2; zamknięcie przejęcia Grob.
- Wartość kontraktów ukraińskich i czy Niemcy sfinansowały partię HX-2; zamówienia MoD UK na SG-1 (poza zobowiązaniem 350 mln GBP).
- Udział w EDF, zamówienia z SAFE, obecność w Polsce — nic nie odnaleziono; dokumentacja pierwotna ustaleń Bloomberga i Welt.

---

## 12. Źródła sprawdzone 30 września 2026 r.

- Profil — https://en.wikipedia.org/wiki/Helsing_(company) ; https://www.caproasia.com/2025/06/18/germany-ai-defence-startup-helsing-raised-690-million-e600-million-in-series-d-funding-at-13-8-billion-e12-billion-valuation-founded-in-2021-by-torsten-reil-gundbert-scherf-niklas-kohler-in/ ; https://www.zoominfo.com/c/helsing-gmbh/563637804 ; https://www.baltictimes.com/helsing_establishes_helsing_estonia_to_bolster_baltic_defence_operations/ ; https://www.inforegister.ee/en/17024826-HELSING-OU/ ; https://www.lexpress.eu/intelligence/helsings-setbacks-in-france-the-rising-star-of-germanys-defence-sector-02-19-2026-IDHN6GMH4NBW5CHU44Y5ZMHXH4/ ; https://en.ain.ua/2026/08/05/tens-of-millions-of-euros-stayed-in-ukraine-and-gave-local-manufacturers-the-opportunity-to-grow-blitz-interview-with-helsings-managing-director-in-ukraine-andrii-shevchenko/ ; https://aviationweek.com/defense/aircraft-propulsion/helsing-buy-grob-aircraft ; https://www.nzz.ch/english/german-defense-startup-helsing-is-bringing-artificial-intelligence-to-the-battlefield-ld.1893755 ; https://www.trueup.io/co/helsing
- Rundy — https://siliconcanals.com/helsing-raises-102-5m/ ; https://tech.eu/2023/09/14/helsing-raises-eur209m-in-series-b-funding-for-ai-defence-tech/ ; https://helsing.ai/newsroom/helsing-raises-euro209m-series-b-to-bolster-defence-ai-capabilities-for-democracies ; https://www.munich-startup.de/en/103104/helsing-series-c/ ; https://techcrunch.com/2024/07/11/defence-ai-startup-helsing-raises-487m-series-c-plans-baltic-expansion-to-combat-russian-threat ; https://sifted.eu/articles/helsing-fundraise-600m-daniel-ek ; https://www.cnbc.com/2025/06/17/spotifys-daniel-ek-leads-investment-in-defense-startup-helsing.html ; https://helsing.ai/newsroom/helsing-raises-eur600m-to-invest-in-european-technological-sovereignty ; https://helsing.ai/newsroom/helsing-raises-1-8bn-in-series-e ; https://www.bloomberg.com/news/articles/2026-07-13/drone-startup-helsing-raises-at-18-billion-with-goldman-backing ; https://www.defensenews.com/global/europe/2026/07/13/helsing-raises-18-billion-in-europes-biggest-defense-startup-round/ ; https://sacra.com/c/helsing/ ; https://multiples.vc/private-comps/helsing ; https://businessmodelcanvastemplate.com/blogs/owners/helsing-who-owns
- Kontrakty — https://helsing.ai/newsroom/helsing-to-produce-6000-additional-strike-drones-for-ukraine ; https://breakingdefense.com/2025/02/ukraine-orders-6000-loitering-munitions-from-germanys-helsing/ ; https://dronexl.co/2026/02/25/germany-helsing-stark-kamikaze-drone-deal/ ; https://www.defensenews.com/global/europe/2026/02/26/once-reluctant-germany-goes-big-on-one-way-attack-drones/ ; https://www.handelsblatt.com/unternehmen/industrie/ruestung-airbus-und-helsing-konkurrieren-um-ki-projekt-der-bundeswehr/100174744.html ; https://www.airforce-technology.com/news/helsing-saab-germany-ew-systems/ ; https://helsing.ai/newsroom/helsing-upgrades-eurofighter-with-artificial-intelligence ; https://thenextweb.com/news/helsing-germany-cfsn-combat-cloud-contract ; https://www.airbus.com/en/newsroom/press-releases/2024-06-airbus-and-helsing-to-collaborate-on-artificial-intelligence-for ; https://helsing.ai/newsroom/helsing-opens-its-first-uk-resilience-factory-in-plymouth-to-build-ai-enabled-submarine-hunters ; https://breakingdefense.com/2025/09/germanys-helsing-unveils-ai-enabled-ca-1-europa-ucav-targets-2029-entry-to-service/ ; https://helsing.ai/resilience-factories ; https://resiliencemedia.co/helsings-second-german-resilience-factory-is-live/
- Krytyka — https://www.kyivpost.com/post/68341 ; https://militarnyi.com/en/news/welt-german-hx-2-drones-in-ukraine-prove-only-35-accurate/ ; https://united24media.com/latest-news/ukraine-halts-german-hx-2-drone-orders-after-battlefield-failures-bloomberg-reveals-15137 ; https://table.media/en/security/news-en/helsing-drones-start-up-rejects-criticism-as-german-ministry-of-defense-continues-with-procurement-plans ; https://en.defence-ua.com/weapon_and_tech/the_controversy_surrounding_the_supply_of_german_hx_2_loitering_munitions_to_ukraine_stakeholder_positions-17224.html ; https://techfundingnews.com/frances-answer-to-helsing-harmattan-ai-secures-200m-from-dassault-aviation/ ; SAFE Polska — https://notesfrompoland.com/2026/05/08/poland-signs-agreement-with-eu-for-e44-billion-in-safe-defence-loans/
