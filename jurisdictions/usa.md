# Stany Zjednoczone: spółka zależna z FOCI zamiast flipu do Delaware

Dokument wewnętrzny Basilisk Systems, informacyjny. Nie jest opinią prawną ani podatkową i nie zmienia umowy spółki. Część katalogu `jurisdictions/` (przegląd: `README.md`; kryteria: `kryteria.md`; podatki przeniesienia: `przeniesienie_i_podatki.md`). Odesłania do umowy według `psa.tex` w wersji 0.9.4-C.

Stan na 30 września 2026 r. Oznaczenia wiarygodności: **[Z]** — akt prawny, portal urzędowy albo publikacja kancelarii lub doradcy podatkowego; **[M]** — prasa, portal informacyjny albo doradca komercyjny; **[W]** — wiedza ogólna, do potwierdzenia; **[?]** — szacunek albo teza niepotwierdzona. Uwaga metodyczna: strony źródłowe były w tej sesji niedostępne do pełnego odczytu (blokada sieciowa); fakty pochodzą ze streszczeń wyszukiwarki; kategoria USML dla oprogramowania autonomii BSP wojskowych nie została ustalona.

---

## 1. Werdykt

| Rola | Ocena | Uzasadnienie |
|---|---|---|
| Siedziba główna (flip do Delaware) | nie w fazie A–C; tylko jako świadoma rezygnacja z Europy | USA są w NATO, ale nie w UE/EOG: amerykańska spółka-matka narusza Kryterium § 11 (bez wyjątku funduszowego po skreśleniu ust. 14) i test kontroli EDF art. 9; zamyka SAFE, EDIP, EIC i PFR; USA nie są LP NIF. Flip jest w Polsce opodatkowany 19 % (wymiana udziałów neutralna tylko do nabywcy z UE/EOG), a przeprowadzka założycieli uruchamia exit tax. Zysk: prawo Delaware, dokumenty NVCA, QSBS (15 mln USD / 75 mln USD po 4 lipca 2025 r.), § 174A (natychmiastowe odliczenie krajowego B+R), największy rynek: Anduril 61 mld USD, Shield AI 12,7 mld USD, Saronic 9,25 mld USD, sektor >33 mld USD w 2026 r. |
| Spółka zależna | tak, gdy klientem jest Department of War: Delaware C-corp albo LLC pod polską P.S.A. | wystarcza na DIU (CSO/OTA, 60–90 dni, budżet 979 mln USD FY2026), kontrakty FAR i DIANA (miejsca w Seattle i Bostonie); nie wystarcza na SBIR (>50 % własności obywateli albo rezydentów USA; spółki zależne zagranicznych matek wykluczone) ani na prace niejawne bez umowy FOCI (SCA, SSA albo Proxy z DCSA). Precedensy: ICEYE US („independent FOCI-mitigated", kontrakty NRO 2022 i sierpień 2026 r.) i WB America LLC (Alexandria, Wirginia, od 21 maja 2018 r.) |
| Spółka bazowa | nie | to samo co flip: kontrola spoza UE/EOG |
| Kryterium § 11, EDF, SAFE, DIANA, NIF | NATO tak; UE i EOG nie; EDF nie; SAFE nie; Horizon Europe nie; DIANA tak; NIF nie (USA, Kanada i Francja nie są LP) | amerykański fundusz w cap table jest dozwolony po § 11 (NATO), ale kontrola amerykańska zamyka EDF i SAFE |

---

## 2. Założenie spółki

| Element | Treść | Wiar. |
|---|---|---|
| Delaware C-corp | opłata za certificate of incorporation od 109 USD (≤1 500 akcji bez wartości nominalnej); registered agent 50–300 USD rocznie; raport roczny 50 USD do 1 marca; podatek franczyzowy min. 175 USD (metoda akcji autoryzowanych) albo 400 USD (metoda kapitału założonego: 400 USD na 1 mln USD), do 1 marca | [M] |
| Teksas | SB 29 z 14 maja 2025 r.: kodyfikacja business judgment rule, próg 3 % do pozwów pochodnych, zrzeczenie ławy przysięgłych; Texas Business Court od 1 września 2024 r. (HB 19); Dell ogłosił przeniesienie z Delaware do Teksasu („Dexit"); Swarmer ma siedzibę w Austin | [Z]/[M] |
| „Department of War" | EO 14347 z 5 września 2025 r.: nazwa wtórna; ustawowa nazwa Department of Defense (1949) tylko przez Kongres; strona war.gov | [Z] |
| Bank i EIN | praktyka dla założycieli nierezydentów nieodnaleziona | [?] |

## 3. Podatki 2026

| Element | Treść | Wiar. |
|---|---|---|
| CIT | federalny 21 %; stanowy: Delaware 8,7 % tylko od dochodu z Delaware, Teksas margin tax 0,75 %, Kalifornia 8,84 % | [W] |
| § 174A | OBBBA z 4 lipca 2025 r.: krajowe wydatki B+R odliczane w roku poniesienia (albo amortyzacja ≥60 miesięcy) od lat od 1 stycznia 2025 r.; zagraniczne B+R nadal amortyzowane 15 lat; małe firmy (≤31 mln USD przychodów) mogą wybrać zastosowanie wsteczne do lat 2022–2024, okno do 6 lipca 2026 r. | [Z] |
| QSBS § 1202 | akcje nabyte po 4 lipca 2025 r.: wyłączenie 50 % po 3 latach, 75 % po 4, 100 % po ≥5; limit 15 mln USD na emitenta (z 10 mln USD; indeksowany od 2026 r.) albo 10× koszt; pułap aktywów brutto 75 mln USD (z 50 mln USD) | [Z] |
| Umowa z Polską | obowiązuje konwencja z 1974 r.; konwencja z 2013 r. (5 % dywidendy przy ≥10 %, 15 % inaczej) nie weszła w życie | [Z] |
| Opcje | ISO (limit 100 tys. USD rocznie), NSO, wybór 83(b) w 30 dni, wycena 409A | [W] |
| Strona polska | flip: wymiana udziałów neutralna tylko, gdy nabywca podlega opodatkowaniu od całości dochodów w UE/EOG; do Delaware opodatkowana 19 % od wartości otrzymanych akcji; przeprowadzka założycieli: exit tax 19 %/3 %; przeniesienie IP: exit tax CIT i utrata IP Box; szczegóły w `przeniesienie_i_podatki.md` | [Z] |

## 4. Reżim obronny i eksportowy

| Element | Treść | Wiar. |
|---|---|---|
| ITAR | rejestracja w DDTC (DECCS): Tier 1 3 000 USD rocznie (2 500 USD dla małych firm), Tier 2 4 000 USD, Tier 3 4 000 USD + 1 100 USD za każdą decyzję powyżej pięciu; reguła z 10 grudnia 2024 r., w mocy od 9 stycznia 2025 r.; obowiązek rejestracji producentów bez eksportu (§ 122.1) — niezweryfikowany | [Z]/[?] |
| EAR 9A012 | cywilne BSP z autonomicznym sterowaniem albo lotem poza zasięgiem wzroku: licencja na eksport do każdego państwa poza Kanadą; oprogramowanie „specially designed" dla 9A012 kontrolowane; wojskowe BSP w USML kategoria VIII; kategoria dla oprogramowania autonomii (VIII(h)/(i), XI albo 9D610) nieustalona | [Z]/[?] |
| Deemed export | EAR § 734.13(b): udostępnienie kontrolowanej technologii cudzoziemcowi (oglądanie, rozmowa, praca pod jego kierunkiem) to eksport do jego państwa; „deemed re-export" do obywateli państw trzecich za granicą; polski zespół w Warszawie nie może swobodnie otrzymywać danych ITAR i oprogramowania 9A012 od spółki amerykańskiej | [Z] |
| AUKUS | § 126.7 ITAR: bezlicencyjnie tylko UK, USA, Australia; Polska poza | [Z] |
| CFIUS | obowiązkowe zgłoszenia tylko dla „TID US business" (technologie krytyczne, infrastruktura, dane wrażliwe); „excepted foreign states": Australia, Kanada, UK, Nowa Zelandia — Polska nie; 2026 r.: projekt Known Investor Program; greenfield co do zasady nie jest „covered transaction" (wnioskowanie); opłaty i terminy (30 dni deklaracja; 45+45 dni) niezweryfikowane | [Z]/[?] |
| FOCI | spółka pod „foreign ownership, control or influence" nie dostanie FCL bez mitygacji: SCA (minimalna, gdy właściciel zagraniczny da się odizolować), SSA (gdy cudzoziemiec faktycznie kontroluje; zarząd z poświadczeniami), Proxy Agreement (właściciel zachowuje własność, ale oddaje wszystkie głosy zatwierdzonym przez DCSA amerykańskim pełnomocnikom); dyrektorzy zewnętrzni to niezależni obywatele USA wskazani przez matkę i zatwierdzeni przez DCSA; „proscribed information" (TS, SCI, COMSEC, SAP) pod SSA wymaga National Interest Determination; czas 6–12+ miesięcy (niezweryfikowany) | [Z]/[?] |
| Blue UAS | lista DIU z 2020 r. po § 848 NDAA FY2020; zgodność z § 817 NDAA FY2023 i American Security Drone Act 2024; Framework (komponenty i oprogramowanie) i Cleared List (systemy); od końca 2025 r. zarządza DCMA (US-X); styczeń 2026 r.: FCC wyłączyło niektóre drony z Covered List | [M] |
| SBIR/STTR | >50 % własności bezpośredniej obywateli albo rezydentów USA; spółki zależne zagranicznych matek niekwalifikowalne; JV <50 % udziału zagranicznego; wygaśnięcie 30 września 2025 r., reautoryzacja (S. 3971, ok. 13 kwietnia 2026 r.) do 30 września 2031 r. — numer i data z blogów, sprawdzić na sbir.gov | [Z]/[?] |

## 5. Pieniądze publiczne i ekosystem

| Instrument | Treść | Wiar. |
|---|---|---|
| DIU | Commercial Solutions Openings i OTA z 10 USC 4022 w 60–90 dni; wymóg istotnego udziału nietradycyjnego wykonawcy albo ≥1/3 kosztów spoza budżetu federalnego; budżet 979 mln USD FY2026; >450 prototypów za 1,7 mld USD od 2016 r.; CSO Guide 2026; Replicator 2 (wrzesień 2024 r.) przeciw małym BSP | [Z]/[M] |
| AFWERX, AAL | szczegóły 2026 r. nieodnalezione | [?] |
| DIANA | Pacific Northwest Mission Acceleration Center (Seattle), MassChallenge (Boston) | [Z] |
| Wizy | H-1B: opłata 100 000 USD za nowe petycje od 21 września 2025 r. (proklamacja z 19 września 2025 r.), utrzymana przez sąd federalny w grudniu 2025 r.; E-2 dla Polaków (traktat od 6 sierpnia 1994 r.): ≥50 % własności obywateli państwa traktatowego, inwestycja od ok. 50 tys. USD, opłata 315 USD; realne drogi: O-1, E-2, L-1 | [Z] |
| Rundy | Anduril 5 mld USD serii H przy 61 mld USD (13 maja 2026 r., Thrive, a16z); Shield AI 1,5 mld USD serii G przy 12,7 mld USD (marzec 2026 r.); Saronic 1,75 mld USD przy 9,25 mld USD; sektor >33 mld USD w 2026 r.; Swarmer IPO Nasdaq 17 marca 2026 r. (`case_studies/swarmer.md`) | [M] |
| Precedensy | ICEYE US (Irvine, Kalifornia): „independent FOCI-mitigated U.S. company affiliated with ICEYE", Government Advisory Board z byłym dyrektorem NGA, kontrakt NRO BAA styczeń 2022 r., NRO Radar Commercial Augmentation sierpień 2026 r.; WB Group America (Alexandria, Wirginia, „WB America LLC", start 21 maja 2018 r. na SOFIC w Tampie): FONET w służbie US Armed Forces, FlyEye i Warmate pozycjonowane pod programy amerykańskie; instrument FOCI obu spółek nieustalony | [Z]/[M] |

## 6. Skutki dla Basiliska

| Wniosek | Gdzie u nas | Stan | Co zrobić |
|---|---|---|---|
| Flip do Delaware to decyzja o wyjściu z EDF, SAFE, EIC i PFR; po skreśleniu ust. 14 nawet amerykański fundusz w większości narusza § 11 | § 11; `regulations.md` sekcja 3b; `vc.md` sekcja 3 | OK | zachować; flip tylko uchwałą WZ ze zmianą umowy, po utracie albo świadomej rezygnacji z programów UE |
| Model ICEYE i WB: polska matka, amerykańska spółka zależna z FOCI, IP i zespół B+R w Polsce; § 174A karze amerykańską matkę za zagraniczne B+R (15 lat) | `case_studies/iceye.md`, `case_studies/wb_electronics.md`; § 33 | DEC | jeśli klient amerykański, spółka zależna z amerykańskim CEO i FSO, technologia amerykańska odgrodzona w USA |
| Deemed export: dane ITAR nie mogą trafiać do Warszawy bez licencji; roje sterowane naszym oprogramowaniem muszą być klasyfikowane po stronie amerykańskiej osobno | `regulations.md` sekcja 3 | BRAK | przed pierwszą umową amerykańską zamówić klasyfikację (commodity jurisdiction) i politykę ring-fencingu |
| SBIR zamknięty dla spółki zależnej; DIU i OTA otwarte | `kryteria.md` K4 | OK | celować w DIU CSO, nie w SBIR |
| Runda z amerykańskim inwestorem w P.S.A.: CFIUS nie dotyczy (inwestycja w spółkę polską), ale inwestycja tego samego funduszu w spółkę zależną amerykańską może być „covered transaction", bo Polska nie jest „excepted state" | § 25; `przeniesienie_i_podatki.md` sekcja 3.6 | DEC | rundy tylko na poziomie P.S.A. |
| Opłata H-1B 100 tys. USD: polskich inżynierów wysyłać do USA na O-1 albo E-2 (E-2 wymaga ≥50 % polskiej własności spółki amerykańskiej — zgodne z modelem spółki zależnej) | `plan_prac.md` etap C | OK | nic teraz |

## 7. Luki do sprawdzenia

- Kategoria USML/ECCN dla oprogramowania autonomii roju wojskowego (VIII(h), XI, 9D610); rejestracja producenta § 122.1.
- Typowy koszt flipu (25–100 tys. USD plus polska kancelaria i wycena); § 351, § 367(a), CFC/GILTI, Form 5471; stawki konwencji z 1974 r.
- Opłaty i terminy CFIUS; liczby z raportów 2024–2025; czy greenfield jest poza jurysdykcją.
- Limity SSA i Proxy; czas procedury FOCI; instrument ICEYE US i WB America; czy WB America ma FCL.
- Pułapy SBIR faza I/II i próg 500 pracowników; numer ustawy reautoryzacyjnej; Buy American i Berry Amendment (65 % → 75 % w 2029 r.).
- AFWERX, Army Applications Lab, status Replicator w 2026 r.; stawki stanowe CIT; płace inżynierów autonomii; rozmiary funduszy a16z American Dynamism, Founders Fund, 8VC, Lux.

---

## 8. Źródła sprawdzone 30 września 2026 r.

- Delaware i Teksas — https://www.rho.co/blog/delaware-c-corp ; https://www.rho.co/blog/delaware-franchise-tax ; https://clemta.com/blog/annual-costs-associated-with-a-delaware-c-corp ; https://www.seyfarth.com/news-insights/texas-adopts-business-friendly-amendments-to-its-corporate-codea-response-to-delaware.html ; https://www.jonesday.com/en/insights/2025/07/texas-enacts-businessfriendly-reforms-in-bid-to-dethrone-delaware-corporate-dominance ; https://www.dallasnews.com/business/article/dexit-delaware-texas-nevada-corporate-governance-22372009.php ; EO 14347 — https://www.whitehouse.gov/fact-sheets/2025/09/fact-sheet-president-donald-j-trump-restores-the-united-states-department-of-war/ ; https://en.wikipedia.org/wiki/Executive_Order_14347
- ITAR i EAR — https://www.federalregister.gov/documents/2024/04/24/2024-08627/international-traffic-in-arms-regulations-registration-fees ; https://public-inspection.federalregister.gov/2024-29032.pdf ; https://www.pilieromazza.com/itar-registration-fees-increase-preparing-government-contractors-for-financial-impact-and-registration-requirements/ ; https://jrupprechtlaw.com/drone-export-control-laws-ear-itar/ ; https://exportcontrol.fiu.edu/export/topics/unmanned-and-autonomous-vehicles/ ; https://exportcontrol.lbl.gov/glossary/ ; https://fdassociates.net/new-us-drone-export-policy-strengthens-control-on-military-drones/ ; AUKUS — https://www.federalregister.gov/documents/2025/12/30/2025-23998/international-traffic-in-arms-regulations-exemption-for-defense-trade-and-cooperation-among
- CFIUS — https://www.whitecase.com/insight-our-thinking/foreign-direct-investment-reviews-2026-united-states ; https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius/cfius-frequently-asked-questions ; https://www.congress.gov/crs-product/IF10177
- FOCI — https://www.hklaw.com/en/insights/media-entities/2024/10/podcast-foci-mitigation-ssas-scas-and-proxy-agreements ; https://www.cdse.edu/Portals/124/Documents/student-guides/IS065-guide.pdf ; https://www.whitecase.com/insight-alert/foci-update-evolving-us-department-defense-foci-environment-process-timing ; https://isidefense.com/understanding-foci-a-comprehensive-guide
- SBIR — https://www.nia.nih.gov/research/sbir/small-business-eligibility-requirements ; https://armysbir.army.mil/eligibility/ ; https://casrai.org/guides/sbir-reauthorization ; https://www.iedconline.org/news/2026/04/01/federal-policy-updates/congress-reauthorizes-the-small-business-innovation-research-sbir-and-small-business-technology-transfer-sttr-programs/ ; https://www.csis.org/analysis/sbir-and-sttr-reauthorization-and-future-small-business-innovation
- DIU, Blue UAS — https://s3.us-gov-west-1.amazonaws.com/publicdocs.diu.mil/CSO-Guide-2026.pdf ; https://www.diu.mil/work-with-us/open-solicitations ; https://www.gao.gov/assets/gao-25-106856.pdf ; https://www.spencerfane.com/insight/defense-innovation-unit-the-pentagons-front-door-for-unmanned-systems-technology-companies/ ; https://mobilicom.com/insight/blue_uas_framework/ ; https://fedlaws.org/blue-uas-drones-the-cleared-list-green-uas-and-asda-rules/ ; https://www.morganlewis.com/pubs/2026/01/fcc-exempts-certain-drones-and-components-from-covered-list-to-address-national-security-risks
- Podatki — https://www.morganlewis.com/pubs/2025/07/new-section-174a-restores-domestic-r-and-e-deductibility-but-other-changes-bring-mixed-results ; https://www.cohnreznick.com/insights/r-d-under-obbb-deduction-timelines-transition-rules ; https://www.hansonbridgett.com/publication/250709-7000-qsbs-after-obbba ; https://www.bakertilly.com/insights/changes-to-section-1202-qualified-small-business ; umowa z Polską — https://www.jct.gov/getattachment/190daa9f-e4f9-441d-928e-3dc7dd1a4ece/x-68-14-4619.pdf ; https://www.tohme-accounting.com/post/us-poland-tax-treaty-ratification/ ; flip — https://spzlegal.com/blog/the-delaware-flip ; https://www.clg-kuznicki.com/flip-do-usa-jak-przeniesc-strukture-startupu-do-delaware-krok-po-kroku/ ; https://www.podatki.biz/artykuly/neutralna-podatkowo-wymiana-udzialow-miedzy-wspolnikami-polskiej-i-zagranicznej-spolki_49_42115.htm
- Wizy — https://www.uscis.gov/newsroom/alerts/presidential-proclamation-on-restriction-on-entry-of-certain-nonimmigrant-workers ; https://www.globalimmigrationblog.com/2025/12/federal-court-upholds-trump-administration-100000-fee-for-certain-h-1b-petitions/ ; https://travel.state.gov/content/travel/en/us-visas/employment/treaty-trader-investor-visa-e.html ; https://poland.us/en/e-2-visa-for-poles-own-business-in-the-usa-without-a-green-card/
- Ekosystem i precedensy — https://www.cnbc.com/2026/05/13/anduril-valuation-defense-tech-funding-boom.html ; https://tech-insider.org/shield-ai-1-5-billion-series-g-12-7-billion-valuation-cca-aechelon-2026/ ; https://www.techbuzz.ai/articles/defense-tech-startup-saronic-raises-1-75b-for-autonomous-warships ; https://valueaddvc.com/pulse/defense-tech-funding-record-2026-analysis ; https://www.prnewswire.com/news-releases/iceye-us-establishes-government-advisory-board-to-accelerate-capability-development-for-national-security-302730924.html ; https://iceye.us/news/iceye-us-awarded-contract-under-nros-radar-commercial-augmentation-rca-program ; https://www.wbgroup.pl/en/wb-america/ ; https://wbgroupamerica.com/ ; https://milmag.pl/en/wb-group-expands-towards-america/ ; DIANA — https://dronehub.ai/blog/nato-diana-dual-use-accelerator ; NIF — https://www.nif.fund/about/
