# Case study: Figure AI — 100 mln USD od założyciela, 39 mld USD wyceny i jeden pilot w BMW

Dokument wewnętrzny Basilisk Systems, informacyjny. Nie jest opinią prawną ani rekomendacją inwestycyjną i nie zmienia umowy spółki. Jedno ze studiów przypadku o rozwoju i finansowaniu firm obronnych, robotyki i fizycznego AI (przegląd i porównanie: `case_studies/README.md`). Opisuje skrajny przypadek fizycznego AI: humanoidy finansowane wyłącznie kapitałem prywatnym, bez grantów i bez klienta rządowego, z wyceną 39 mld USD przy nieujawnionych przychodach. Odesłania do umowy według `psa.tex` w wersji 0.9.4-C (numery § według `spis_tresci.md`); uzupełnia `case_studies/nomagic.md` (kontrast skali), `jurisdictions/usa.md` i `vc.md` sekcja 11.

Stan na 30 września 2026 r. Oznaczenia wiarygodności: **[Z]** — fakt z dokumentu pierwotnego (komunikat spółki, pozew w relacji agencyjnej); **[M]** — doniesienie prasowe albo baza danych; **[W]** — wiedza ogólna o prawie albo praktyce rynkowej; **[?]** — szacunek albo teza niepotwierdzona. Uwaga metodyczna: strony źródłowe były w tej sesji niedostępne do pełnego odczytu (blokada sieciowa); fakty pochodzą ze streszczeń wyszukiwarki. Metryki wdrożenia w BMW, tempo produkcji BotQ i wycena serii A pochodzą z agregatorów i blogów powtarzających komunikaty spółki, nie z dokumentów pierwotnych.

---

## 1. Główny wniosek

Figure AI pokazuje, **ile kosztuje fizyczne AI na granicy technologii i kto może to sfinansować: nie Polska P.S.A.** Brett Adcock założył firmę w 2022 r. i wyłożył ok. 100 mln USD z własnych pieniędzy (z Vettery i Archer Aviation), pomijając fazę grantów i aniołów; potem: seria A 70 mln USD (Parkway, maj 2023 r., ok. 500 mln USD wyceny wg agregatorów), seria B 675 mln USD przy 2,6 mld USD (29 lutego 2024 r.; Microsoft, OpenAI Startup Fund, NVIDIA, Amazon, Bezos, Intel) i seria C ponad 1 mld USD przy 39 mld USD po pieniądzu (wrzesień 2025 r.; Parkway, Brookfield, NVIDIA, Intel) — razem ok. 1,9 mld USD. Jedyne publiczne wdrożenie: Figure 02 przez ok. 11 miesięcy w fabryce BMW w Spartanburgu (ponad 30 000 X3, ponad 90 000 części), wycofane ok. listopada 2025 r.; partnerstwo z OpenAI zerwane w lutym 2025 r. na rzecz własnego modelu Helix; Figure 03 i fabryka BotQ (cel 12 000 sztuk rocznie) w październiku 2025 r.; w listopadzie 2025 r. pozew byłego głównego inżyniera bezpieczeństwa, że mapa bezpieczeństwa pokazana inwestorom serii C została „wypatroszona" w miesiącu zamknięcia rundy; secondaries blokowane przez spółkę (cease-and-desist), a mimo to 174 USD za akcję na Forge (sierpień 2026 r.). Dla Basiliska: fizyczne AI pełnego stosu wymaga 1–2 mld USD przed przychodem, więc Basilisk musi być warstwą autonomii na cudzym sprzęcie; własność modelu i danych z wdrożeń jest tym, za co inwestorzy płacą; a dokumentacja bezpieczeństwa pokazana inwestorom musi przetrwać rundę.

---

## 2. Profil

| Element | Treść | Wiar. |
|---|---|---|
| Założenie i forma | 2022 r.; Brett Adcock (założyciel, prezes; wcześniej Vettery sprzedane Adecco i Archer Aviation); forma i siedziba (zakładane Delaware C-corp, San Jose/Sunnyvale) niepotwierdzone | [M]/[?] |
| Produkty | humanoidy Figure 01 → 02 → 03 (październik 2025 r., zaprojektowany do masowej produkcji i domu); model VLA Helix rozwijany w całości wewnętrznie; fabryka BotQ (cel 12 000 sztuk rocznie, „jeden robot na 90 minut" w kwietniu 2026 r. wg bloga) | [M]/[?] |
| Klienci | BMW Manufacturing (Spartanburg); drugi duży klient „podobno UPS" (niepotwierdzone) | [M]/[?] |
| Zatrudnienie | ok. 400 | [M] |
| Kapitał | ok. 1,9 mld USD w pięciu rundach | [M] |

---

## 3. Jak zaczęli: kapitał początkowy i pierwsze lata

- **Pieniądze założyciela zamiast seedu.** Ok. 100 mln USD od Adcocka w 2022 r.; natychmiastowa rekrutacja dużego zespołu **[M]**.
- **Seria A przed chodzącym robotem.** 70 mln USD od Parkway Venture Capital (maj 2023 r.) przy ok. 500 mln USD wyceny (tylko agregatory) **[M]/[?]**.
- **Pierwsze 24 miesiące:** budowa Figure 01 i podpisanie BMW (ogłoszone z serią B, luty 2024 r.); środki serii B na trening AI, produkcję robotów i inżynierów, „by dostarczyć jednostki produkcyjne w latach 2024–2025" **[M]**.
- **Wniosek:** czek założyciela usunął fazę 2–3 lat grantów i aniołów, przez którą przeszły Creotech i APS; ceną jest założyciel z nietypową kontrolą **[?]**.

---

## 4. Oś czasu

| Data | Zdarzenie | Wiar. |
|---|---|---|
| 2022 | założenie; 100 mln USD od założyciela | [M] |
| maj 2023 | seria A 70 mln USD (Parkway) | [M] |
| 29 lutego 2024 | seria B 675 mln USD przy 2,6 mld USD; współpraca z OpenAI i Microsoft Azure | [M] |
| luty 2025 | koniec partnerstwa z OpenAI; własny model Helix | [M] |
| 29 kwietnia 2025 | listy cease-and-desist do brokerów rynku wtórnego | [M] |
| wrzesień 2025 | seria C ponad 1 mld USD przy 39 mld USD po pieniądzu (Parkway lead; Brookfield, NVIDIA, Intel Capital, Microsoft; udział OpenAI Startup Fund po rozstaniu wątpliwy) | [Z]/[?] |
| wrzesień 2025 | zwolnienie inżyniera bezpieczeństwa Roberta Gruendela (wg pozwu) | [M] |
| październik 2025 | premiera Figure 03 | [M] |
| ok. listopada 2025 | Figure 02 wycofany z BMW po ok. 11 miesiącach | [M]/[?] |
| 21 listopada 2025 | pozew sygnalisty Gruendela (N.D. California): bezprawne zwolnienie dni po udokumentowanych skargach; robot mógł wywierać siłę ponad dwukrotnie większą niż potrzebna do złamania czaszki i rozciął stalowe drzwi lodówki; mapa bezpieczeństwa pokazana dwóm inwestorom „wypatroszona" w miesiącu zamknięcia rundy; spółka: zwolnienie „za słabe wyniki", zarzuty to „fałsze" | [Z]/[M] |
| kwiecień 2026 | BotQ: jeden robot na 90 minut (blog, niezweryfikowane) | [?] |
| 13 sierpnia 2026 | transakcja na Forge po 174 USD za akcję | [M] |

---

## 5. Finansowanie: runda po rundzie

| Runda | Data | Kwota | Wycena | Inwestorzy | Wiar. |
|---|---|---|---|---|---|
| Seed | 2022 | 100 mln USD | — | założyciel | [M] |
| Seria A | maj 2023 | 70 mln USD | ok. 500 mln USD (agregator) | Parkway Venture Capital | [M]/[?] |
| Seria B | luty 2024 | 675 mln USD | 2,6 mld USD | Microsoft, OpenAI Startup Fund, NVIDIA, Amazon Industrial Innovation Fund, Bezos Expeditions, Parkway, Intel Capital, Align Ventures, ARK Invest | [M] |
| Seria C | wrzesień 2025 | ponad 1 mld USD | 39 mld USD po pieniądzu | Parkway (lead), Brookfield, NVIDIA, Intel Capital, Microsoft i inni | [Z]/[M] |
| Secondaries | 2025–2026 | — | 174 USD/akcja (Forge, sierpień 2026 r.); bez liczby akcji nie da się policzyć dyskonta | spółka blokuje nieautoryzowany obrót | [M]/[?] |

- Ok. 95 % kapitału weszło w dwóch rundach „strategicznych" (2024–2025 r.) od hiperskalerów, producentów chipów i jednego funduszu (Parkway), który zakotwiczył już serię A; koncentracja typowa dla cyklu humanoidów 2024–2025 r., nie dla klasycznej syndykacji VC **[?]**.
- Skok wyceny 15× w 19 miesięcy (2,6 → 39 mld USD) **[M]**.

---

## 6. Giełda

Nienotowana; strony „pre-IPO" i spekulacje o debiucie (2026 r.) bez potwierdzenia; spółka ogranicza obrót wtórny **[M]/[?]**.

---

## 7. Wzrost w liczbach

| Miara | Wartość | Wiar. |
|---|---|---|
| Wycena | ok. 500 mln USD (2023 r.) → 2,6 mld USD (2024 r.) → 39 mld USD (2025 r.) | [M]/[Z] |
| BMW | ok. 11 miesięcy, ponad 30 000 X3, ponad 90 000 części, ponad 1 250 godzin; zakończone ok. listopada 2025 r. | [?] |
| BotQ | cel 12 000 sztuk rocznie | [M] |
| Przychód | nieujawniony; „ok. 60 mln USD ARR 2024" (agregator, szacunek); „największy zakład pre-revenue w robotyce" (blog) | [?] |
| Zatrudnienie | ok. 400 | [M] |

Wniosek: bez ujawnionego przychodu i po zakończeniu jedynego publicznego wdrożenia wycena 39 mld USD to zakład o Helix i skalę BotQ; stosunek wyceny do ujawnionych sztuk (dziesiątki robotów) jest najbardziej skrajny w całym zestawie case studies **[?]**.

---

## 8. Struktura właścicielska, kontrola i ład korporacyjny

- Adcock założył, sfinansował i prowadzi spółkę; pierwsze 100 mln USD i każda narracja (OpenAI in, OpenAI out, Helix, Figure 03, BotQ) dają mu faktyczną kontrolę niezależnie od klas akcji **[?]**; klasy akcji, rada, odejścia współzałożycieli (w tym szeroko opisywane odejście CTO Jerry'ego Pratta w 2024 r.) nieodnalezione w tej sesji **[?]**.
- Pozew sygnalisty: zarzut, że dokumentacja bezpieczeństwa pokazana inwestorom nie przetrwała rundy — ryzyko ładu, które reguły rynku publicznego (jak u Creotechu) mają ujawniać **[Z]/[?]**.
- Ograniczanie secondaries: brak wyceny rynkowej poza rundami **[M]**.

---

## 9. Ocena: co zadziałało, co nie

**Zadziałało**
- Kapitał założyciela kupił szybkość; inwestorzy strategiczni (Microsoft, NVIDIA, Bezos, Brookfield) kupili wiarygodność i moc obliczeniową.
- Jeden pilot flagowy (BMW) dostarczył materiału demonstracyjnego pod wycenę 39 mld USD.
- Własny model (Helix) po rozstaniu z OpenAI: inwestorzy traktują własność modelu i danych z wdrożeń jako kluczowe aktywo.

**Nie zadziałało albo kosztowało**
- Zależność od cudzego modelu porzucona w 12 miesięcy; potrzeba własnego labu AI.
- Jedyne publiczne wdrożenie zakończone po 11 miesiącach bez ujawnionej kontynuacji.
- Przychód nieujawniony; wycena oderwana od zamówień.
- Pozew o odwet za sygnalizowanie ryzyka bezpieczeństwa powiązany wprost z narracją fundraisingową.
- Blokada secondaries ogranicza odkrywanie ceny.
- Brak jakiegokolwiek zamówienia rządowego: humanoidy w obronności (Foundation Robotics, xTechHumanoid US Army) to inne firmy **[M]**.

---

## 10. Wnioski dla Basiliska: mapowanie na projekt umowy

Oznaczenia stanu jak w `vc.md` sekcja 8: **OK**, **CZ**, **BRAK**, **KOL**, **DEC**.

| Lekcja z Figure AI | Gdzie u nas | Stan | Co zrobić i kiedy |
|---|---|---|---|
| **Pełny stos fizycznego AI kosztuje 1–2 mld USD przed przychodem** | `plan_prac.md` etap C; § 32; `vc.md` sekcja 11 | DEC | Basilisk jako warstwa autonomii na sprzęcie primów (jak APS na PGZ–Kongsberg, Nomagic na standardowych ramionach); nie budować własnych platform |
| **Własność modelu i danych z wdrożeń to aktywo, za które płacą inwestorzy** (Helix zamiast OpenAI) | § 26 (IP w Spółce), § 33 ust. 3 (licencja), wzór umowy pilota (etap C pkt 25) | BRAK | Prawa do danych treningowych i telemetrycznych w każdej umowie pilotażowej z MON i producentem; zakaz wyłączności modelu dla jednego klienta |
| **Jeden pilot flagowy niesie wycenę przez 18 miesięcy, ale jego koniec musi mieć następcę** | `psa_todo.md` sekcja 6; `regulations.md` sekcja 4 (G5) | DEC | Jedno widoczne ćwiczenie z Siłami Zbrojnymi RP jako odpowiednik BMW; równolegle drugi pilot u sojusznika |
| **Kontrola założyciela kupiona własnym kapitałem** jest niedostępna; polscy założyciele utrzymują kontrolę przez syndykaty instytucji (Creotech), PE mniejszość (APS) albo VC pod matką w USA (Nomagic) | § 10, § 25, `vc.md` sekcja 9 | OK | Wybrać świadomie jedną z trzech dróg przed rundą A; umowa daje Założycielom Sprawy Zastrzeżone 75 % |
| **Dokumentacja bezpieczeństwa pokazana inwestorom musi przetrwać rundę** (pozew Gruendela) | § 23 ust. 2 (głos dyrektora ds. zgodności), § 29–30, `regulations.md` sekcja 2.2 | CZ | Polityka bezpieczeństwa systemów autonomicznych jako załącznik do data room i do umowy inwestycyjnej (oświadczenia i zapewnienia) **[W]** |
| **Blokowanie secondaries** chroni narrację, ale odbiera płynność pracownikom | § 12–14 (ograniczenia obrotu), § 27 (ESOP) | OK | Zaplanować okna odsprzedaży dla pracowników w rundach (wzór ICEYE), zamiast zakazu |
| **Brak zamówień rządowych w fizycznym AI USA**: finansowanie w 100 % prywatne | `jurisdictions/usa.md` sekcja 5 | OK | Dla Basiliska odwrotnie: klient rządowy jest źródłem przychodu i wiarygodności; nie kopiować modelu Figure |

---

## 11. Luki i rzeczy do sprawdzenia

- Lista inwestorów serii C i ceny za akcję z komunikatu spółki; liczba akcji i dyskonto secondaries; ewentualna runda 2026 r. albo prospekt.
- Przychód, sztuki wyprodukowane i wysłane; klienci Figure 03 po BMW (UPS niepotwierdzone).
- Oświadczenie Adcocka o zerwaniu umowy z OpenAI; odejścia Pratta i innych; klasy akcji i rada; stan sprawy Gruendela w 2026 r.
- Udział w xTech lub DARPA; lokalizacja i zachęty dla BotQ.

---

## 12. Źródła sprawdzone 30 września 2026 r.

- Profil i rundy — https://en.wikipedia.org/wiki/Figure_AI ; https://en.wikipedia.org/wiki/Brett_Adcock ; https://sacra.com/c/figure-ai/ ; https://forgeglobal.com/figure-ai_ipo/ ; https://time.com/collections/time100-ai-2024/7012726/brett-adcock/ ; https://www.therobotreport.com/figure-ai-raises-675m-to-commercialize-humanoids/ ; https://techcrunch.com/2024/02/29/figure-rides-the-humanoid-robot-hype-wave-to-2-6b-valuation-and-openai-collab/ ; https://www.cnbc.com/2024/02/29/robot-startup-figure-valued-at-2point6-billion-by-bezos-amazon-nvidia.html ; https://www.figure.ai/news/series-c ; https://www.therobotreport.com/figure-ai-raises-1b-in-series-c-funding-toward-humanoid-robot-development/ ; https://www.inc.com/chloe-aiello/humanoid-robot-company-figure-is-valued-at-39-billion-its-goal-is-human-level-intelligence/91240631 ; https://tracxn.com/d/companies/figure/__mGB8ifRJofxLs0K1QhT-K0x9b67g4bQIEIT7bBN3B7c ; https://tsginvest.com/figure-ai/ ; https://humanoidindex.org/companies/figure-ai
- Secondaries — https://techcrunch.com/2025/04/29/figure-ai-sent-cease-and-desist-letters-to-secondary-markets-brokers/ ; https://valueaddvc.com/blog/figure-ai-valuation-2026-39b-humanoid-robotics-investors ; https://www.upmarket.co/private-markets/pre-ipo/figure-ai/
- BMW, Figure 03, BotQ — https://blog.robozaps.com/b/figure-02-review ; https://blog.robozaps.com/b/figure-03-review ; https://axis-intelligence.com/figure-ai-statistics/ ; https://getlatka.com/companies/figure-ai
- Pozew — https://www.cnbc.com/2025/11/21/figure-ai-sued.html ; https://interestingengineering.com/innovation/figure-ai-faces-whistleblower-lawsuit ; https://www.benzinga.com/markets/tech/25/11/49020142/nvidia-backed-figure-ai-sued-by-former-safety-engineer-claiming-dangerous-robots-and-fraudulent-cuts-to-safety-plan
- Humanoidy w obronności (kontekst) — https://www.cnbc.com/2026/05/30/humanoid-robots-ukraine-war-foundation-military-ai.html ; https://time.com/article/2026/03/09/ai-robots-soldiers-war/ ; https://xtech.army.mil/competition/xtechhumanoid/
