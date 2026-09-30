# Case study: Milrem Robotics — robotyka lądowa z Estonii, EDF i sprzedaż kontroli do ZEA

Dokument wewnętrzny Basilisk Systems, informacyjny. Nie jest opinią prawną ani rekomendacją inwestycyjną i nie zmienia umowy spółki. Jedno ze studiów przypadku o rozwoju i finansowaniu firm obronnych, robotyki i fizycznego AI (przegląd i porównanie: `case_studies/README.md`). Opisuje, jak estońska firma serwisująca pojazdy wojskowe stała się liderem europejskich programów robotów lądowych (iMUGS, iMUGS2), rosła z pieniędzy państwowych i strategicznych zamiast VC, i co się stało z jej kwalifikowalnością do EDF po sprzedaży kontroli koncernowi z Abu Zabi. Odesłania do umowy według `psa.tex` w wersji 0.9.4-C (numery § według `spis_tresci.md`); uzupełnia `jurisdictions/estonia.md`, `jurisdictions/poza_kryterium.md` (ZEA), `kryteria.md` (test kontroli EDF) i `regulations.md` sekcja 3.

Stan na 30 września 2026 r. Oznaczenia wiarygodności: **[Z]** — fakt z dokumentu pierwotnego (rejestr, komunikat spółki, inwestora, Komisji Europejskiej albo zamawiającego); **[M]** — doniesienie prasowe albo baza danych; **[W]** — wiedza ogólna o prawie albo praktyce rynkowej, do potwierdzenia u kancelarii; **[?]** — szacunek, w tym własne obliczenie z cytowanych liczb, albo teza niepotwierdzona. Uwaga metodyczna: strony źródłowe były w tej sesji niedostępne do pełnego odczytu (blokada sieciowa); fakty pochodzą ze streszczeń wyszukiwarki, a **[Z]** przyznano tylko tam, gdzie streszczenie dokumentu pierwotnego było jednoznaczne. Serię przychodów z rejestru (Inforegister) trzeba przed użyciem poza firmą sprawdzić na stronie rejestru.

---

## 1. Główny wniosek

Milrem pokazuje trzecią drogę obok VC i giełdy: **klient państwowy od pierwszego dnia, konsorcja EDF jako finansowanie B+R platformy, inwestor strategiczny zamiast funduszy, a na końcu sprzedaż kontroli**. W dziesięć lat od pierwszego prototypu THeMIS (2015 r.) firma doszła do 46,1 mln EUR przychodu (2025 r.), 305 pracowników i sprzedaży do 16 państw, mając przed 2023 r. tylko ok. 6,25 mln USD kapitału zewnętrznego. Cena: 2024 r. zamknięty stratą 14,1 mln EUR i ujemnym kapitałem własnym (−14,4 mln EUR) przy 68 mln EUR zobowiązań, a kontrola nad firmą trafiła do państwowego koncernu EDGE z Abu Zabi, co uruchomiło postępowanie Komisji Europejskiej z art. 9 EDF. Milrem zachował rolę koordynatora EDF tylko dzięki gwarancjom rządu Estonii (lipiec 2023 r.). Dla Basiliska to precedens w obie strony: jak być liderem pakietu „funkcje inteligentne" w konsorcjum sprzętowym, i czego kosztuje inwestor spoza UE/EOG/NATO w rozumieniu § 11.

---

## 2. Profil

| Element | Treść | Wiar. |
|---|---|---|
| Nazwa i forma | Milrem AS (kod rejestru 12494266), Tallinn; w profilach także „Milrem Robotics OÜ"; grupa używa nazwy Milrem Robotics | [Z]/[M] |
| Założenie | 2013 r., założyciel i prezes Kuldar Väärsi; początkowo serwis i naprawa pojazdów wojskowych; w 2013 r. wygrany przetarg MO Estonii na utrzymanie transporterów PASI XA; prototypowanie robotów od 2014 r. | [M] |
| Produkty | THeMIS (Tracked Hybrid Modular Infantry System) — modułowy bezzałogowy pojazd gąsienicowy (CASEVAC, logistyka, rozminowanie, nosiciel uzbrojenia); Type-X — robotyczny wóz bojowy projektowany pod wymagania US Army RCV-M | [M] |
| Klienci | sprzedaż do 16 państw, m.in. USA, Hiszpania, Holandia, Norwegia, Francja, Niemcy, UK, Estonia, ZEA, Ukraina | [M] |
| Zatrudnienie | 172 (IV kw. 2022 r.), 196 (IV kw. 2023 r.), 296 (2024 r.), 305 (IV kw. 2025 r.); agregatory: 316–334 (2025–2026 r.) | [Z]/[M] |
| Biura i produkcja | Tallinn; biura w Finlandii, Szwecji, Holandii i USA (stan na luty 2023 r.); montaż końcowy THeMIS dla Ukrainy w zakładzie VDL Defentec w Born (Holandia), 1 sztuka dziennie, możliwe 500 rocznie | [M]/[Z] |
| Właściciel | EDGE Group (Abu Zabi, państwowy) — większość od lutego 2023 r.; mniejszość: KMW (dziś KNDS), założyciel, estońscy inwestorzy prywatni, pracownicy | [Z] |

---

## 3. Jak zaczęli: kapitał początkowy i pierwsze lata

- **Usługi przed produktem.** Pierwszym przychodem był kontrakt serwisowy dla MO Estonii z 2013 r. (utrzymanie PASI XA), a nie sprzedaż robota; prace nad THeMIS ruszyły jesienią 2014 r., prototyp pokazano na DSEI w Londynie we wrześniu 2015 r. **[M]**
- **Państwo jako pierwszy sponsor B+R.** THeMIS powstał „przy wsparciu Ministerstwa Obrony Estonii" w ramach projektu badawczo-rozwojowego; kwoty nieodnalezione **[M]/[?]**. Dotacji Enterprise Estonia (EAS) nie udało się potwierdzić w żadnym źródle **[?]**.
- **Kapitał zewnętrzny minimalny.** Do przejęcia przez EDGE w 2023 r. firma pozyskała ok. 6,25 mln USD kapitału zewnętrznego (Preqin) **[M]**; założycielskiego kapitału zakładowego nie odnaleziono.
- **Pierwszy duży pieniądz z UE, nie od inwestora.** W czerwcu 2020 r. konsorcjum pod wodzą Milrem dostało 30,6 mln EUR z EDIDP (poprzednika EDF) na iMUGS — europejski standard bezzałogowego systemu lądowego; całkowita wartość projektu 32,6 mln EUR **[Z]**. Tego samego roku Estonia i Holandia wspólnie kupiły 7 THeMIS (4 dla armii holenderskiej, 3 dla estońskiej) **[M]**.
- **Skala po siedmiu latach.** Przychód z rejestru: 5,4 mln EUR (2021 r.), 9,25 mln EUR (2022 r.), 19,0 mln EUR (2023 r.) **[Z]**. Wniosek: firma doszła do ok. 19 mln EUR przychodu niemal bez kapitału VC, z kontraktów, grantów EDIDP i inwestycji strategicznej KMW z 2021 r. (kwota nieujawniona) **[?]**.

---

## 4. Oś czasu

| Data | Zdarzenie | Wiar. |
|---|---|---|
| 2013 | założenie w Tallinie; kontrakt MO Estonii na serwis PASI XA | [M] |
| jesień 2014 | start prac nad THeMIS | [Z] |
| wrzesień 2015 | prototyp THeMIS na DSEI w Londynie | [M] |
| czerwiec 2020 | 30,6 mln EUR z EDIDP na iMUGS; konsorcjum pod wodzą Milrem | [Z] |
| wrzesień 2020 | wspólne zamówienie Estonii i Holandii: 7 THeMIS | [M] |
| 31 maja 2021 | Krauss-Maffei Wegmann obejmuje 24,9 % (umowa o współpracy strategicznej; warunki nieujawnione; „Europejskie Centrum Doskonałości Robotyki Wojskowej" w Estonii) | [M]/[Z] |
| wrzesień 2022 | pierwszy THeMIS (CASEVAC, zaopatrzenie) w Ukrainie | [M] |
| 29 listopada 2022 | kontrakt z KMW na 14 THeMIS dla Ukrainy finansowanych przez MO Niemiec (7 CASEVAC do końca 2022 r., 7 do rozminowania z ładunkami CNIM w II kw. 2023 r.) | [Z] |
| styczeń 2023 | Estonia uchwala ustawę o ocenie wiarygodności inwestycji zagranicznych (w mocy od września 2023 r.) | [M] |
| 15 lutego 2023 | EDGE (Abu Zabi) kupuje pakiet większościowy na IDEX; „największa inwestycja zagraniczna w estońskim przemyśle obronnym"; cena nieujawniona | [Z] |
| marzec 2023 | MO Estonii: zmiana właściciela „jeszcze nie zatwierdzona"; Komisja Europejska wszczyna badanie przejęcia pod kątem kontroli z państwa trzeciego | [M] |
| lipiec 2023 | werdykt Komisji: gwarancje Estonii czynią Milrem zgodnym z regułami; firma pozostaje liderem kontynuacji iMUGS i może uczestniczyć w EDF i PESCO | [M] |
| styczeń 2024 | kontrakt z MO ZEA: 20 wozów RCV i 40 THeMIS, ponad 100 mln EUR, „największa umowa estońskiego przemysłu obronnego" | [M] |
| 2024 | przychód 20,4 mln EUR, strata netto 14,1 mln EUR, kapitał własny −14,4 mln EUR, zobowiązania 68,0 mln EUR (w tym długoterminowe 41,3 mln EUR) | [Z] |
| kwiecień–maj 2025 | EDF zatwierdza ok. 50 mln EUR na iMUGS2 (wartość ok. 55 mln EUR, 29 beneficjentów, 2025–2028, koordynator Milrem) | [Z] |
| 6 października 2025 | podpisanie w VDL Born z ministrem obrony Holandii dostawy ponad 150 THeMIS dla Ukrainy finansowanej przez Holandię; 100 sztuk montuje VDL Defentec | [Z] |
| listopad 2025 | kick-off iMUGS2 w DG DEFIS w Brukseli | [Z] |
| 2025 | przychód 46,1 mln EUR (+126 %); 305 pracowników; przychód na pracownika 73,3 tys. EUR | [Z] |
| 2026 | umowy teamingowe z EOS Defence Systems, Hanwha Aerospace (program UGV Rumunii) i CNIM (Eurosatory) | [M] |
| 14–15 sierpnia 2026 | pożar w zakładzie w Tallinie; 29 września 2026 r. MSZ Estonii: sabotaż na zlecenie wywiadu rosyjskiego; trzej podejrzani zatrzymani na Łotwie; produkcja i dostawy do Ukrainy niezakłócone | [M] |

---

## 5. Finansowanie: inwestorzy strategiczni zamiast rund

| Etap | Data | Kapitał | Warunki | Wiar. |
|---|---|---|---|---|
| Kapitał wczesny | 2013–2020 | ok. 6,25 mln USD łącznie (Preqin) | inwestorzy i wyceny nieujawnione | [M] |
| Grant EDIDP | czerwiec 2020 | 30,6 mln EUR dla konsorcjum (część Milrem nieujawniona) | bezzwrotny, na iMUGS | [Z] |
| Inwestor strategiczny | 31 maja 2021 | KMW 24,9 % | kwota nieujawniona; Milrem „pozostaje niezależny"; centrum doskonałości w Estonii | [M] |
| Sprzedaż kontroli | 15 lutego 2023 | EDGE — pakiet większościowy | cena i dokładny udział nieujawnione; Milrem w klastrze Platforms & Systems EDGE; mniejszość: KMW, założyciel, inwestorzy estońscy, pracownicy | [Z] |
| Finansowanie po przejęciu | 2023–2024 | zobowiązania długoterminowe 41,3 mln EUR przy ujemnym kapitale własnym | struktura nieujawniona; najpewniej pożyczki wspólników (EDGE, KMW), nie dług bankowy ani obligacje | [Z]/[?] |
| Grant EDF | 2025 | ok. 50 mln EUR na iMUGS2 dla konsorcjum | bezzwrotny; Milrem koordynatorem | [Z] |

Wnioski z tabeli: (1) żadnej klasycznej rundy VC nie było; (2) strata 14 mln EUR przy 20 mln EUR sprzedaży w 2024 r. to tempo inwestowania, które toleruje tylko właściciel strategiczny; (3) po przejęciu wycena nigdy nie została ujawniona, a liczby z agregatorów są szacunkami **[?]**.

---

## 6. Giełda

Milrem nie jest notowany i nie ogłaszał planów IPO. Właściciel większościowy (EDGE) jest państwowym konglomeratem, a mniejszościowy (KNDS) sam przygotowuje własne wejście na giełdę **[W]**. Płynność dla wczesnych inwestorów i pracowników dała sprzedaż kontroli w 2023 r., nie rynek publiczny.

---

## 7. Wzrost w liczbach

| Rok | Przychód (mln EUR) | Wynik netto (mln EUR) | Pracownicy | Wiar. |
|---|---|---|---|---|
| 2021 | 5,4 | — | — | [Z] |
| 2022 | 9,25 | — | 172 | [Z] |
| 2023 | 19,0 | — | 196 | [Z] |
| 2024 | 20,4 | −14,1; kapitał własny −14,4 | 296 | [Z] |
| 2025 | 46,1 | nieodnaleziony | 305 | [Z] |

- I–III kw. 2025 r.: ponad 29 mln EUR, +155 % r/r, najwięcej wśród estońskich firm obronnych **[M]**.
- 2026 r.: „największy kontrakt w historii" (Ukraina, program europejskiej pomocy); ponad 200 systemów w Ukrainie do końca 2026 r. **[M]**.
- Sprzedaż do 16 państw; ZEA ponad 100 mln EUR (2024 r.); Holandia ponad 150 sztuk (wartość nieujawniona) **[M]**.
- Wycena: nigdy nieujawniona **[?]**.

---

## 8. Struktura właścicielska, kontrola i ład korporacyjny

- **Przed 2021 r.:** założyciel, estońscy inwestorzy prywatni, pracownicy **[M]**.
- **2021 r.:** KMW 24,9 % — próg tuż poniżej mniejszości blokującej w niemieckiej praktyce (25 %), typowy dla inwestora strategicznego, który chce wpływu bez konsolidacji **[W]**.
- **2023 r.:** EDGE — większość; pozostali: KMW, założyciel-prezes, inwestorzy estońscy, pracownicy **[Z]**.
- **Kontrola inwestycji:** transakcja zamknięta „na chwilę przed" wejściem w życie estońskiej ustawy o ocenie inwestycji zagranicznych (uchwalona w styczniu, w mocy od września 2023 r.), więc krajowego screeningu nie było **[M]**.
- **Test kontroli EDF (art. 9):** Komisja Europejska badała, czy przejęcie przez podmiot kontrolowany z państwa trzeciego nie narusza interesów bezpieczeństwa UE; w lipcu 2023 r. uznała, że gwarancje złożone przez Estonię czynią Milrem zgodnym; firma pozostała liderem kontynuacji iMUGS i może brać udział w EDF i PESCO **[M]**. Treść gwarancji nie została opublikowana **[?]**.
- **Krytyka:** kampania bojkotu za własność z ZEA (blog aktywistyczny) **[M]**; brak niezależnej analizy ekonomiki jednostkowej.
- **Bezpieczeństwo fizyczne:** sabotaż na zlecenie Rosji w sierpniu 2026 r. jako koszt bycia dostawcą dla Ukrainy **[M]**.

---

## 9. Ocena: co zadziałało, co nie

**Zadziałało**
- Klient państwowy od dnia zero (serwis dla MO), a potem państwo jako sponsor B+R produktu.
- Rola koordynatora EDIDP i EDF: 30,6 mln EUR (2020 r.) i ok. 50 mln EUR (2025 r.) na platformę, której firma nie sfinansowałaby z kapitału własnego.
- Eksport finansowany przez darczyńców: Niemcy (14 sztuk, 2022 r.) i Holandia (ponad 150 sztuk, 2025–2026 r.) płacą za dostawy do Ukrainy; Milrem sprzedaje do państwa trzeciego bez ryzyka kredytowego Ukrainy.
- Skalowanie produkcji u wykonawcy kontraktowego w kraju klienta (VDL Born) zamiast budowy własnej fabryki.
- Umowa z ZEA (ponad 100 mln EUR) jako nagroda za wejście EDGE.

**Nie zadziałało albo kosztowało**
- Ujemny kapitał własny i strata 14 mln EUR w 2024 r.; firma żyje z pożyczek właścicieli **[?]**.
- Sprzedaż kontroli poza UE/NATO: sześć miesięcy niepewności co do EDF, gwarancje rządowe jako warunek, reputacyjny koszt własności z ZEA.
- Brak ujawnionej wyceny i brak płynności dla mniejszości poza transakcją z 2023 r.
- Ekspozycja na sabotaż.

---

## 10. Wnioski dla Basiliska: mapowanie na projekt umowy

Oznaczenia stanu jak w `vc.md` sekcja 8: **OK** — umowa to przewiduje; **CZ** — częściowo; **BRAK** — dodać; **KOL** — koliduje; **DEC** — wymaga decyzji Założycieli.

| Lekcja z Milrem | Gdzie u nas | Stan | Co zrobić i kiedy |
|---|---|---|---|
| **Inwestor spoza UE/EOG/NATO z pakietem kontrolnym uruchamia art. 9 EDF; ratunkiem są gwarancje państwa członkowskiego** (Estonia, lipiec 2023 r.) | § 11 (Kryterium UE/EOG/NATO, bez wyjątku funduszowego); `kryteria.md` sekcja 3; `jurisdictions/poza_kryterium.md` sekcja 5 | OK | zachować § 11; w umowie inwestycyjnej dopisać, że exit do nabywcy spoza Kryterium wymaga (a) uchwały 75 %, (b) wcześniejszej rozmowy z MON o gwarancjach z art. 9 ust. 4 EDF **[W]** |
| **Inwestor strategiczny na 24,9 % zamiast VC** (KMW 2021 r.): kapitał, kanał sprzedaży, centrum kompetencji, bez konsolidacji | § 25 ust. 1 (Sprawy Zastrzeżone 75 %), § 32 (Kwalifikowana Runda), `vc.md` sekcje 3–4 | CZ | Rozważyć koncern z UE/NATO (WB, PGZ, KNDS, Rheinmetall, Saab) jako inwestora rundy A obok funduszu; określić w umowie inwestycyjnej, że strategiczny inwestor nie dostaje wyłączności ani prawa pierwokupu technologii (§ 33 ust. 3 licencja niewyłączna) |
| **EDF i EDIDP jako główne źródło B+R platformy**; Milrem był liderem sprzętowym, a partnerzy dostarczali „funkcje inteligentne" | `psa_todo.md` sekcja 6; `regulations.md` sekcja 4 (bramka G4); `plan_prac.md` etap C | BRAK | Zgłosić się do konsorcjów EDF 2027 jako dostawca pakietu autonomii roju (odpowiednik „intelligent functions" w iMUGS2); wymaga podmiotu z UE bez kontroli z państwa trzeciego, czyli P.S.A. w Polsce (`jurisdictions/README.md` sekcja 6) |
| **Eksport finansowany przez darczyńcę** (Niemcy, Holandia płacą za Ukrainę) | § 28 (eksport), `regulations.md` sekcja 3, `jurisdictions/ukraina.md` sekcja 6 | CZ | Celować w pakiety pomocowe finansowane przez państwa NATO i SAFE, a nie w bezpośrednią sprzedaż Ukrainie; licencja eksportowa i tak jest potrzebna (ZG-PL-U-1 nie obejmuje Ukrainy) |
| **Produkcja u wykonawcy w kraju klienta** (VDL Born) zamiast własnej fabryki | § 33 (spółki celowe), `jurisdictions/README.md` sekcja 4.2 | OK | Dla oprogramowania odpowiednikiem jest integracja u producenta platformy w kraju klienta; wzór umowy licencyjnej „na platformę" (`case_studies/swarmer.md` sekcja 10) |
| **Ujemny kapitał własny finansowany pożyczkami wspólników** | § 31 (finansowanie dłużne i instrumenty zamienne: WZ 75 %) | OK | Pożyczki od akcjonariuszy dopuszczalne tylko uchwałą; w umowie inwestycyjnej limit zadłużenia wobec akcjonariuszy i zakaz zabezpieczeń na IP (§ 31 ust. 4) |
| **Zamknięcie transakcji przed wejściem w życie ustawy o kontroli inwestycji** | `jurisdictions/polska.md` sekcja 4 (polski screening stały od 24 lipca 2025 r., próg 20 %) | OK | W Polsce nie ma „okna": każde nabycie ≥20 % przez podmiot spoza UE/EOG/OECD przez inwestora w spółce obronnej podlega UOKiK **[W]**; wpisać do harmonogramu rund |
| **Bezpieczeństwo fizyczne i cybernetyczne jako koszt dostaw do Ukrainy** | `regulations.md` sekcja 2.2; ŚBP (`jurisdictions/polska.md` sekcja 5) | BRAK | Budżet ochrony w planie etapu C; polityka bezpieczeństwa przed pierwszą dostawą do Ukrainy |

---

## 11. Luki i rzeczy do sprawdzenia

- Mapa podmiotów (Milrem AS, Milrem Robotics OÜ, spółki w Finlandii, Szwecji, Holandii, USA); dokładny udział EDGE i cena transakcji; czy po 2023 r. były podwyższenia kapitału rozwadniające mniejszość.
- Struktura 41,3 mln EUR zobowiązań długoterminowych (pożyczki wspólników czy bank); wynik za 2025 r.
- Dotacje EAS; udział w FAMOUS/FAMOUS II; zamówienia Sił Obronnych Estonii po 2020 r.; łączna liczba wyprodukowanych THeMIS i Type-X.
- Treść gwarancji Estonii wobec Komisji z 2023 r. — kluczowa dla oceny, czy polski MON mógłby złożyć podobne.
- Wartość holenderskiego pakietu dla Ukrainy; udział Milrem w kwotach iMUGS i iMUGS2.
- Seria przychodów z Inforegister — do potwierdzenia na stronie rejestru.

---

## 12. Źródła sprawdzone 30 września 2026 r.

- Rejestr i liczby — https://www.inforegister.ee/en/12494266-MILREM-AS/ ; profil — https://en.wikipedia.org/wiki/Milrem_Robotics ; https://robotics.press/news/milrem-robotics-company-profile ; https://investinestonia.com/how-estonian-defence-company-milrem-became-the-leading-robotics-developer-in-europe/ ; https://www.army-technology.com/projects/themis-hybrid-unmanned-ground-vehicle/ ; https://www.preqin.com/data/profile/asset/milrem-robotics/531038 ; https://pitchbook.com/profiles/company/268732-36
- iMUGS i iMUGS2 — https://www.businesswire.com/news/home/20200616005680/en/Milrem-Robotics-Led-Consortium-Awarded-306-MEUR-by-the-European-Commission-to-Develop-a-European-Standardized-Unmanned-Ground-System ; https://www.janes.com/osint-insights/defence-news/milrem-led-consortium-receives-eu-grant-to-develop-european-standard-unmanned-ground-system ; https://investinestonia.com/estonian-milrem-robotics-leads-e50m-european-defence-initiative/ ; https://defence-industry-space.ec.europa.eu/dg-defis-hosts-kick-meeting-imugs2-advancing-interoperable-unmanned-ground-systems-europe-2025-11-21_en ; https://defence-industry.eu/imugs-2-european-industry-consortium-secures-edf-funding-for-next-generation-unmanned-ground-systems/
- KMW i EDGE — https://www.army-technology.com/news/krauss-maffei-wegmann-to-acquire-24-9-stake-in-milrem-robotics/ ; https://www.sorainen.com/deals/milrem-robotics-secures-an-investment-from-krauss-maffei-wegmann/ ; https://edgegroup.ae/news/edge-acquires-majority-stake-milrem-robotics-europes-leading-developer-robotics-and-autonomous ; https://milremrobotics.com/edge-acquires-majority-stake-in-milrem-robotics-europes-leading-developer-of-robotics-and-autonomous-systems/ ; https://breakingdefense.com/2023/02/emirati-conglomerate-edge-grabs-majority-stake-in-estonian-robotics-firm/ ; https://investinestonia.com/milrem-robotics-raises-the-largest-foreign-investment-in-estonias-defence-sector/
- Kontrola inwestycji i EDF art. 9 — https://www.defensenews.com/global/europe/2023/03/25/estonian-firms-takeover-by-emirati-group-tests-joint-eu-defense-rules/ ; https://www.defensenews.com/global/europe/2023/03/31/eu-scrutinizes-emirati-takeover-of-estonian-robotics-firm/ ; https://www.defensenews.com/global/europe/2023/07/25/eu-issues-verdict-over-edge-groups-takeover-of-milrem-robotics/
- Kontrakty — https://www.edrmagazine.eu/netherlands-and-estonia-to-acquire-seven-milrem-robotics-themis-ugvs ; https://knds.com/en/press-releases/milrem-robotics-to-deliver-14-t-he-mis-ug-vs-to-ukraine-in-cooperation-with-kmw ; https://news.err.ee/1609235739/milrem-robotics-signs-estonian-defense-industry-s-biggest-deal-yet-with-uae ; https://www.defensenews.com/global/europe/2024/01/24/milrem-to-deliver-dozens-of-military-robots-to-uae-forces/ ; https://milremrobotics.com/milrem-robotics-to-deliver-over-150-themis-ugvs-to-ukraine-in-a-dutch-led-defence-initiative/ ; https://www.janes.com/defence-intelligence-insights/defence-news/industry/ukraine-conflict-milrem-expects-to-deliver-over-150-themis-ugvs-for-ukrainian-army-by-end-of-2026 ; https://www.upi.com/Top_News/World-News/2026/05/15/Hanwha-Aerospace-underground-vehicle-contract/6521778857223/
- Sabotaż 2026 — https://www.defensenews.com/global/europe/2026/09/29/estonia-blames-russia-in-arson-attack-on-military-robotics-firm-milrem/ ; https://eng.lsm.lv/article/society/crime/20.08.2026-three-suspects-detained-in-latvia-for-tallinn-military-factory-arson.a659564/ ; ekosystem — https://www.baltictimes.com/from_fintech_to_defence__war_in_ukraine_reshapes_estonia_s_startup_focus/ ; https://news.err.ee/1609351302/estonia-s-defense-sector-aiming-for-1-billion-annual-revenues-by-2030
