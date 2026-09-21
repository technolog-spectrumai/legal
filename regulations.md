# Mapa reżimów regulacyjnych Basilisk Systems

Dokument wewnętrzny, informacyjny. Nie jest opinią prawną i nie zmienia umowy spółki. Porządkuje, które reżimy prawne dotyczą Basiliska, co je uruchamia, a co nie, oraz kiedy w cyklu rozwoju firmy trzeba zrobić formalny checkpoint. Zawiera także ocenę tez z rozmowy z ChatGPT z 21 września 2026 r. o starcie firmy jako dual-use R&D.

Stan na 21 września 2026 r. Oznaczenia wiarygodności:

- **[Z]** — sprawdzone w źródłach urzędowych lub branżowych (lista na końcu),
- **[W]** — wiedza ogólna, brzmienie przepisu do potwierdzenia u kancelarii,
- **[?]** — teza niezweryfikowana; traktować jako hipotezę.

Pytania do kancelarii dotyczące tych reżimów są w `law.md`, pkt 4.1 i 4.2. Powiązane postanowienia projektu umowy: § 3 ust. 4, § 4 ust. 4 i 7–8, § 11 (Kryterium), § 27 ust. 6, § 28, § 31 ust. 3, § 33 ust. 3–4.

---

## 1. Główny wniosek

Prace badawczo-rozwojowe nad autonomią, percepcją, planowaniem, fuzją sensorów, komunikacją między robotami i edge AI można prowadzić w Polsce bez koncesji, bez świadectwa bezpieczeństwa przemysłowego i bez zezwoleń eksportowych, dopóki:

1. nie wytwarzamy ani nie modyfikujemy wyrobu **specjalnie zaprojektowanego do celów wojskowych lub policyjnych** z wykazu koncesyjnego,
2. nie prowadzimy **obrotu** takim wyrobem ani **technologią** o takim przeznaczeniu, w tym nie udostępniamy jej partnerom,
3. nie przekazujemy kontrolowanej technologii, oprogramowania ani sprzętu **poza obszar celny UE** (także elektronicznie),
4. nie przetwarzamy informacji niejawnych,
5. testy w terenie wykonujemy zgodnie z prawem lotniczym, morskim i radiowym.

Każdy z tych progów jest osobnym checkpointem (sekcja 4). Ta konstrukcja jest zgodna z tym, co przewiduje projekt umowy: § 4 ust. 4 mówi o wariantach obronnych „wyłącznie po spełnieniu właściwych wymogów prawa", a § 4 ust. 7–8 rozdzielają katalog PKD w umowie od rozpoczęcia działalności regulowanej.

---

## 2. Reżimy — kto, co uruchamia, co nie uruchamia

### 2.1 Koncesja MSWiA — wyroby i technologia o przeznaczeniu wojskowym lub policyjnym

- **Podstawa:** ustawa z 13 czerwca 2019 r. o wykonywaniu działalności gospodarczej w zakresie wytwarzania i obrotu materiałami wybuchowymi, bronią, amunicją oraz wyrobami i technologią o przeznaczeniu wojskowym lub policyjnym (Dz.U. 2019 poz. 1214, z późn. zm.) **[Z]**; wykaz: rozporządzenie **Rady Ministrów** (nie MSWiA) z 17 września 2019 r., Dz.U. 2019 poz. 1888 **[Z]**. Ustawę zmieniono ustawą z 13 marca 2026 r. (Dz.U. 2026 poz. 471), zakres zmian w ustawie koncesyjnej do sprawdzenia **[Z/?]**.
- **Organ:** Minister Spraw Wewnętrznych i Administracji **[Z]**.
- **Co uruchamia:** wytwarzanie wyrobów z wykazu (w tym naprawa, przeróbka, modyfikacja — do potwierdzenia zakresu definicji „wytwarzanie" **[W]**) oraz obrót wyrobami i technologią z wykazu. Wykaz WT V obejmuje „załogowe i bezzałogowe statki powietrzne [...] specjalnie zaprojektowane lub zmodyfikowane do celów wojskowych lub policyjnych", w tym „bezzałogowe statki powietrzne oraz ich systemy i urządzenia, takie jak: startu, lądowania, kierowania i kontroli lotu" **[Z]**. Drony przeznaczone do rażenia celów wchodzą dodatkowo w kategorie broni i amunicji **[W]**.
- **Czego nie uruchamia:** cywilny dron, USV lub UGV kupiony na rynku i użyty jako platforma testowa; własne B+R nad algorytmami na podstawie informacji jawnych; symulacje; publikacje i zgłoszenia patentowe. Ustawa nie zna osobnej koncesji na „tworzenie technologii" — koncesji wymaga wytwarzanie wyrobów oraz obrót wyrobami i technologią **[W]**.
- **Pułapki:** (a) napis „prototyp / research only" nie wyłącza koncesji, jeżeli fizycznie powstaje wyrób z wykazu; (b) **obrót technologią** obejmuje udostępnianie i licencjonowanie — licencja na oprogramowanie autonomii dla spółki celowej lub partnera produkującego wojskowe UAV (§ 33 ust. 3 umowy) może wymagać koncesji po stronie Basiliska, nie tylko producenta **[W]**; (c) prowadzenie działalności bez koncesji jest przestępstwem zagrożonym karą do 10 lat pozbawienia wolności **[Z]**; (d) czy ustawa przewiduje wyłączenie dla prac B+R i prototypów — nie potwierdzono, pytanie do kancelarii **[?]**.
- **Sankcja i praktyka:** koncesję uzyskuje się przed rozpoczęciem działalności; wymaga m.in. opinii, warunków lokalowych, osoby z uprawnieniami; realny czas kilka miesięcy **[W]**.

### 2.2 Kontrola obrotu strategicznego — dual-use i uzbrojenie

- **Podstawa:** rozporządzenie (UE) 2021/821 (dual-use, załącznik I i IV) **[W]**; ustawa z 29 listopada 2000 r. o obrocie z zagranicą towarami, technologiami i usługami o znaczeniu strategicznym, znowelizowana ustawą z 13 marca 2026 r. (Dz.U. 2026 poz. 471), w mocy od 22 kwietnia 2026 r., z planowanym systemem Tracker 2.0 do wniosków elektronicznych **[Z]**.
- **Organ:** minister właściwy ds. gospodarki (MRiT) **[Z]**; przy uzbrojeniu wymagany Wewnętrzny System Kontroli (WSK) **[Z]**.
- **Co uruchamia:** eksport, transfer, pośrednictwo i pomoc techniczna dotyczące pozycji z wykazów. „Eksport" obejmuje elektroniczne przekazanie oprogramowania lub technologii poza obszar celny UE oraz udostępnienie ich osobom spoza UE **[W]** — w praktyce: repozytorium lub chmura na serwerze poza UE, e-mail do partnera w USA, dostęp zdalny pracownika spoza UE, prezentacja dokumentacji technicznej na targach poza UE. Dla części pozycji (załącznik IV) zezwolenia wymaga także transfer wewnątrz UE **[W]**.
- **Kandydaci do klasyfikacji w produktach Basiliska** (do sprawdzenia przez specjalistę, § 28 ust. 2 umowy nakazuje klasyfikację przed udostępnieniem) **[W]**: 9A012 (UAV o określonej wytrzymałości i sterowaniu poza zasięgiem wzroku), 9A120 (UAV o zasięgu ≥ 300 km), kategoria 7 (nawigacja inercyjna, działanie bez GNSS), kategoria 6 (sensory, radary, lidary), 5A002 (kryptografia w łączności między robotami), 9D/9E, 7D/7E, 6D/6E (oprogramowanie i technologia do powyższych); dla jednostek nawodnych i podwodnych kategoria 8. Produkt wojskowy trafia zamiast tego na wykaz uzbrojenia (ML10 dla UAV, ML9 dla jednostek pływających) **[W]**.
- **Czego nie uruchamia:** rozwój i testy w Polsce oraz w UE bez przekazania kontrolowanej technologii poza UE; sprzedaż na rynek polski i unijny pozycji spoza załącznika IV.
- **Pułapki:** klasyfikacja jest obowiązkiem firmy; nieświadomy „eksport" przez chmurę albo współpracownika spoza UE; komponenty z USA objęte ITAR/EAR mają własne ograniczenia reeksportu i dostępu osób, niezależne od prawa UE **[W]**.

### 2.2a Cywilne technologie strategiczne: budowanie a obrót

Pytanie Założycieli: autonomiczny lot jest technologią o znaczeniu strategicznym, choć cywilną. Co wolno, a co wymaga zezwolenia?

**Budowanie jest wolne, obrót z zagranicą jest kontrolowany.** Ustawa o obrocie z zagranicą towarami, technologiami i usługami o znaczeniu strategicznym reguluje wyłącznie obrót z zagranicą: eksport, transfer wewnątrzunijny wybranych pozycji, import części pozycji, tranzyt, pośrednictwo i pomoc techniczną. Nie reguluje prac rozwojowych, produkcji na własne potrzeby ani sprzedaży w Polsce. Rozwijanie autonomii lotu w Polsce nie wymaga zezwolenia, koncesji ani zgłoszenia **[W]**.

**Czy autonomia lotu jest pozycją kontrolowaną?** Prawdopodobnie tak, w zależności od parametrów platformy **[W]**:

- 9A012.a obejmuje UAV sterowane poza zasięgiem wzroku operatora o określonej wytrzymałości (co najmniej 30 minut przy odporności na podmuchy albo co najmniej 1 godzina);
- 9A012.b.2 obejmuje systemy nawigacji, orientacji, naprowadzania lub sterowania **specjalnie zaprojektowane, aby zapewnić UAV zdolność autonomicznego sterowania lotem lub nawigacji** — to jest dokładnie warstwa Basiliska;
- 9D (oprogramowanie) i 9E (technologia) obejmują oprogramowanie i technologię do rozwoju, produkcji lub użytkowania powyższych; kategoria 7 obejmuje nawigację inercyjną i nawigację bez GNSS o określonej dokładności; 5A002 kryptografię w łączności między platformami;
- małe platformy o krótkim czasie lotu mogą wypadać poza 9A012.a, ale oprogramowanie i technologia mogą pozostać kontrolowane przez kategorie 7 albo przez klauzulę catch-all (końcowe zastosowanie wojskowe w państwie objętym embargiem albo broń masowego rażenia);
- koordynacja roju nie ma, według naszej wiedzy, osobnej pozycji w wykazie, ale jako oprogramowanie „do użytkowania" kontrolowanego UAV może być kontrolowana pośrednio **[?]**;
- wykaz w załączniku I jest aktualizowany co roku rozporządzeniem delegowanym; klasyfikację robi się na aktualnej wersji.

**Co dokładnie jest „obrotem" technologią i oprogramowaniem** (rozporządzenie 2021/821, art. 2) **[W]**:

- eksport to także transmisja elektroniczna poza obszar celny UE oraz **udostępnienie** oprogramowania lub technologii osobie spoza UE, w tym przez chmurę i zdalny dostęp;
- w praktyce: repozytorium kodu na serwerach poza UE, kopie zapasowe w chmurze poza UE, dostęp zdalny współpracownika przebywającego poza UE, przesłanie dokumentacji do partnera w USA, prezentacja szczegółów technicznych na targach poza UE, testy w ośrodku poza UE (np. centra testowe DIANA poza UE);
- pomoc techniczna (szkolenie, doradztwo, przekazanie umiejętności) dotycząca pozycji kontrolowanych na rzecz osób spoza UE podlega osobnej kontroli;
- transfer wewnątrz UE jest wolny poza pozycjami z załącznika IV; czy któraś pozycja Basiliska tam trafia (np. 9A120 przy zasięgu co najmniej 300 km) — do sprawdzenia;
- zatrudnienie obywatela państwa spoza UE pracującego w Polsce nie jest eksportem w rozumieniu prawa UE (brak konstrukcji „deemed export"), ale § 27 ust. 6 umowy i Kryterium nakładają własny, surowszy wymóg zgody na dostęp spoza UE/NATO **[W]**.

**Wyłączenia, z których korzysta B+R** (uwagi ogólne do załącznika I) **[W]**:

- technologia i oprogramowanie **powszechnie dostępne** (public domain) nie są kontrolowane; publikacja wyników i kod otwarty wychodzą spod kontroli, ale samo opublikowanie technologii kontrolowanej może być traktowane jak jej udostępnienie — decyzję o publikacji poprzedza klasyfikacja;
- **podstawowe badania naukowe** (basic scientific research) są wyłączone; prace nad produktem już nie;
- oprogramowanie masowego rynku (mass market) — wyłączenie nie obejmuje typowo oprogramowania autonomii.

**Import i rynek krajowy** **[W]**: sprzedaż w Polsce i w UE nie wymaga zezwolenia (poza załącznikiem IV); przy imporcie niektórych pozycji polska ustawa przewiduje obowiązki ewidencyjne i oświadczenia użytkownika końcowego; komponenty z USA objęte ITAR/EAR niosą własne ograniczenia reeksportu i dostępu osób.

**Zezwolenia, gdy obrót już jest potrzebny** **[W]**: indywidualne, globalne albo generalne. Unijne generalne zezwolenie EU001 obejmuje eksport większości pozycji z załącznika I do USA, Kanady, Wielkiej Brytanii, Norwegii, Szwajcarii, Japonii, Australii i Nowej Zelandii, z wyłączeniami; czy obejmuje pozycje Basiliska — do sprawdzenia przy pierwszym eksporcie. Organ: MRiT; po nowelizacji z 2026 r. wnioski elektroniczne przez Tracker 2.0 **[Z]**.

**Konsekwencje praktyczne od dnia 1:**

1. Klasyfikacja produktu, kodu i dokumentacji przed pierwszym udostępnieniem poza firmę (§ 28 ust. 2 umowy), z zapisem wyniku i wersji wykazu; przy wątpliwości wniosek do MRiT o ustalenie, czy pozycja podlega kontroli.
2. Kod i dokumentacja techniczna na serwerach w UE albo we własnej infrastrukturze; chmura i repozytoria z regionem UE i kontrolą dostępu według obywatelstwa i miejsca pobytu.
3. Rejestr dostępu do Kluczowej Własności Intelektualnej (§ 26 ust. 6 umowy) rozszerzony o miejsce pobytu i obywatelstwo osób z dostępem.
4. Program zgodności eksportowej (§ 28 ust. 4) prowadzony od początku, choć WSK jest obowiązkowy dopiero przy uzbrojeniu; ułatwia późniejsze zezwolenia i due diligence inwestorów.
5. Przy DIANA, EIC i partnerach spoza UE: przed przekazaniem czegokolwiek poza UE checkpoint G2/G5.

Wniosek: to, że technologia jest cywilna, nie ma znaczenia dla kontroli obrotu; liczy się pozycja wykazu, kraj i użytkownik końcowy. Budować można swobodnie, ale granica UE jest dla oprogramowania autonomii granicą prawną, także w chmurze.

### 2.3 Prawo lotnicze — bezzałogowe systemy powietrzne

- **Podstawa:** rozporządzenia (UE) 2019/945 (projektowanie, produkcja, klasy UAS, wprowadzanie do obrotu) i 2019/947 (operacje: kategorie „otwarta", „szczególna", „certyfikowana"), ustawa Prawo lotnicze znowelizowana ustawą z 24 stycznia 2025 r., w mocy od 27 lutego 2025 r. **[Z]**.
- **Organ:** Urząd Lotnictwa Cywilnego; strefy geograficzne — PAŻP **[W]**.
- **Co uruchamia:** każdy lot testowy. Rejestracja operatora; loty poza kategorią otwartą (BVLOS, roje, masa, wysokość, nad ludźmi) wymagają zezwolenia na operację w kategorii szczególnej po analizie ryzyka SORA albo scenariusza standardowego **[W]**; produkcja własnych płatowców do sprzedaży — wymogi 2019/945 i oznakowanie klasy.
- **Czego nie uruchamia:** symulacja, testy stanowiskowe, testy na UGV i USV.
- **Pułapki:** rój i BVLOS to niemal zawsze kategoria szczególna; testy w pobliżu lotnisk i w strefach ograniczonych; częstotliwości (2.4).

### 2.4 Prawo morskie i żegluga śródlądowa — jednostki nawodne

Reżim pominięty w rozmowie z ChatGPT, mimo że proponuje on morze jako pierwsze laboratorium.

- **Podstawa:** ustawa o bezpieczeństwie morskim, ustawa z 12 kwietnia 2018 r. o rejestracji jachtów i innych jednostek pływających o długości do 24 m (rejestr REJA24), ustawa o żegludze śródlądowej, COLREG **[Z/W]**.
- **Organ:** dyrektor właściwego urzędu morskiego (morze), urząd żeglugi śródlądowej (wody śródlądowe) **[W]**.
- **Co uruchamia:** rejestracja jednostki o długości powyżej 7,5 m albo z napędem powyżej 15 kW **[Z]**; testy jednostki bez załogi na wodach morskich — w praktyce zgoda urzędu morskiego, który może czasowo zamknąć akwen dla żeglugi i rybołówstwa na czas testów jednostek autonomicznych **[Z]**; radiostacja statkowa VHF/AIS — pozwolenie UKE (2.5); ubezpieczenie OC.
- **Pułapki:** brak w Polsce kompletnego reżimu dla statków autonomicznych (MASS), decyzje są indywidualne; na jeziorach i rzekach obowiązują odrębne przepisy; procedura uzyskania zgody na testy — do ustalenia z urzędem morskim przed pierwszym wyjściem w morze **[?]**.

### 2.5 Częstotliwości radiowe

- **Podstawa:** Prawo komunikacji elektronicznej; organ: UKE **[W]**.
- **Co uruchamia:** łączność poza pasmami ogólnodostępnymi (ISM, 2,4/5,8 GHz z limitami mocy), własne radia mesh o większej mocy, radiostacje statkowe. Pozwolenie radiowe albo rezerwacja częstotliwości; urządzenia radiowe — dyrektywa RED i oznakowanie CE **[W]**.

### 2.6 Informacje niejawne

- **Podstawa:** ustawa z 5 sierpnia 2010 r. o ochronie informacji niejawnych **[W]**.
- **Organ:** ABW (cywilne), SKW (wojskowe).
- **Co uruchamia:** dostęp firmy do informacji o klauzuli „poufne" lub wyższej wymaga świadectwa bezpieczeństwa przemysłowego; osoby — poświadczeń bezpieczeństwa; przy klauzuli „zastrzeżone" wystarczają upoważnienia i pion ochrony **[W]**.
- **Czego nie uruchamia:** własne, jawne B+R. Świadectwo staje się potrzebne dopiero przy kontraktach z MON, NATO lub integratorami przekazującymi dokumentację niejawną. Uzyskanie trwa zwykle ponad rok — planować z wyprzedzeniem, nie na dzień 1 **[W]**.

### 2.7 Broń, amunicja, materiały wybuchowe

Osobny reżim (ta sama ustawa z 2019 r. oraz ustawa o broni i amunicji). Uruchamia go integracja efektorów, ładunków lub amunicji, także testowa. Poza zakresem obecnych planów; każde wejście w ten obszar to osobny checkpoint **[W]**.

### 2.8 Produkty cywilne — zgodność produktowa UE

Reżim pominięty w rozmowie z ChatGPT; dotyczy właśnie cywilnej ścieżki dual-use.

- **AI Act** (rozporządzenie 2024/1689): wyłącza systemy AI wyłącznie do celów wojskowych i obronnych, ale obejmuje produkty cywilne; autonomia jako element bezpieczeństwa produktu może być systemem wysokiego ryzyka; obowiązki wchodzą etapami do 2027 r. **[W]**.
- **Rozporządzenie maszynowe** 2023/1230 (stosowane od 2027 r.): autonomiczne maszyny mobilne, roboty lądowe, maszyny rolnicze i leśne **[W]**.
- **Cyber Resilience Act** 2024/2847: produkty z elementami cyfrowymi, obowiązki raportowania od 2026 r., pełne od 2027 r. **[W]**.
- **RED, EMC, LVD, oznakowanie CE** dla sprzętu **[W]**.
- **RODO** przy danych z kamer i sensorów.

### 2.9 Zamówienia obronne, offset, kontrola inwestycji

Później: ustawa Prawo zamówień publicznych (dział obronność), ustawa offsetowa, ustawa o kontroli niektórych inwestycji (przy wejściu inwestora spoza UE do spółki o znaczeniu dla bezpieczeństwa). Ten ostatni reżim jest powodem lit. e w § 12 ust. 2 umowy **[W]**.

### 2.10 Sankcje

Objęte § 11 i § 28 umowy; test sankcyjny nabywców, partnerów i kontrahentów obowiązuje od dnia 1.

---

## 3. Wymogi właścicielskie programów finansowania a Kryterium EU/NATO

To jest miejsce, gdzie regulacje spotykają się z umową spółki.

| Program | Wymóg dotyczący firmy | Relacja do Kryterium z § 11 |
|---|---|---|
| **EDF** (rozporządzenie 2021/697, art. 9) | siedziba i zarząd w UE lub państwie stowarzyszonym; **brak kontroli przez państwo trzecie niestowarzyszone** lub podmiot z takiego państwa; derogacja tylko z gwarancjami państwa członkowskiego; konsorcjum ≥ 3 podmiotów z ≥ 3 państw (dla technologii przełomowych ≥ 2 z 2) **[Z]** | Kryterium dopuszcza właścicieli z NATO spoza UE (USA, UK, Turcja, Kanada). Inwestor z takiego państwa uzyskujący **kontrolę** nad Basiliskiem może wyłączyć firmę z EDF bez derogacji. Do rozważenia przy rundzie: limit kontroli spoza UE/EOG, nie tylko spoza NATO. **[W]** |
| **EIC Accelerator** (dual-use od 17 czerwca 2026 r.) | MŚP z UE lub państwa stowarzyszonego z Horyzontem Europa; grant do 2,5 mln EUR, inwestycja do 30 mln EUR **[Z]** | bez kolizji |
| **NATO DIANA** | siedziba w jednym z 32 państw NATO; TRL co najmniej 4 (3–4 preferowane, 5–6 akceptowane); 100 tys. EUR w fazie 1, do 300 tys. EUR w fazie 2 **[Z]** | zgodne z Kryterium |
| **PFR Deep Tech / Otwarte Innowacje** | inwestycje przez fundusze VC, nie bezpośrednio; PFR 300 mln zł plus co najmniej 300 mln zł inwestorów prywatnych; ok. 195 mln zł już przydzielone (Expeditions II, Balnord) **[Z]** | wymogi funduszu, zwykle spółka polska |
| **Ścieżka SMART** (FENG) | MŚP; realne prace B+R; nabór PARP dla pojedynczych MŚP **29 października – 29 grudnia 2026 r.**, NCBR dla konsorcjów 7 sierpnia – 16 października 2026 r. **[Z]** | bez kolizji |
| **AGILE** (od początku 2027 r.) | MŚP i startupy obronne, granty 1–5 mln EUR, 100 % kosztów, decyzja w ok. 4 miesiące, 20–30 projektów **[Z]** | jak EDF (kontrola) **[?]** |
| **EUDIS** | Business Accelerator: voucher 65 tys. EUR; cascade funding przez konsorcja EDF **[Z]** | jak EDF |

---

## 3a. Wspólnik z Wielkiej Brytanii (albo innego państwa NATO spoza UE)

Pytanie Założycieli przy tabeli z sekcji 3. Odpowiedź zależy od trzech rzeczy: czy wspólnik ma **kontrolę**, gdzie **fizycznie pracuje** i jaki ma **dostęp do technologii**.

| Reżim | Wspólnik mniejszościowy z UK | Wspólnik z UK z kontrolą (większość, weto, decydujący wpływ) |
|---|---|---|
| Umowa spółki, Kryterium § 11 ust. 6 | dopuszczalny bez zgody WZ (UK jest w NATO) **[Z]** | dopuszczalny, ale zob. skutki niżej |
| PFR Deep Tech / Otwarte Innowacje | brak zakazu w publicznych warunkach programów; warunkiem jest polska spółka („Polish nexus"), a przy spółce zagranicznej polscy założyciele i kapitał na działalność w Polsce; ostateczne warunki ustala konkretny fundusz VC **[Z/W]** | jak obok, ale fundusze z komponentem obronnym mogą badać strukturę właścicielską ostrzej **[?]** |
| EDF, AGILE, EUDIS | dopuszczalny: art. 9 EDF zakazuje **kontroli** przez państwo trzecie niestowarzyszone, nie udziału; UK nie jest stowarzyszone z EDF i nie przystąpiło do SAFE (grudzień 2025 r.) **[Z]** | firma traci kwalifikowalność, chyba że uzyska gwarancje państwa członkowskiego (art. 9 ust. 4); zarząd wykonawczy i infrastruktura użyta w projekcie muszą być w UE **[Z/W]** |
| NATO DIANA | bez przeszkód **[Z]** | bez przeszkód |
| EIC Accelerator | bez przeszkód, UK jest stowarzyszone z Horyzontem Europa **[W]** | do sprawdzenia przy naborze dual-use **[?]** |
| Koncesja MSWiA (bramka G3) | może być akcjonariuszem; przy udziale co najmniej 20 % musi wykazać niekaralność (zaświadczenie z UK, tłumaczenie); we wniosku podaje się udział kapitału zagranicznego i adresy wspólników **[Z]** | jak obok; ale co najmniej dwóch członków Rady (albo członek i prokurent) musi mieć obywatelstwo Polski, UE, Szwajcarii albo EFTA-EOG, albo polskie zezwolenie na pobyt stały — obywatel UK bez takiego zezwolenia nie liczy się do tej dwójki **[Z]** |
| Kontrola obrotu strategicznego (dual-use) | jeżeli pracuje **w Polsce**: brak eksportu, obowiązuje tylko § 27 ust. 6 (UK w NATO, więc bez dodatkowej zgody). Jeżeli pracuje **z UK**: każde udostępnienie kontrolowanego kodu lub dokumentacji jest eksportem; UK jest na liście unijnego zezwolenia generalnego EU001, co upraszcza sprawę, ale wymaga rejestracji w MRiT przed pierwszym użyciem i ewidencji **[W]** | jak obok |
| Informacje niejawne (bramka G4) | dostęp cudzoziemca do informacji niejawnych wymaga poświadczenia w trybie umowy dwustronnej o ochronie informacji; na starcie bez znaczenia **[W]** | jak obok |
| Kontrola inwestycji | przy zawiązaniu bez znaczenia; przy późniejszym nabyciu znaczącego pakietu w spółce z sektora chronionego stosuje się § 12 ust. 2 lit. e **[W]** | jak obok |
| Podatki, CRBR | podatek u źródła według umowy Polska–UK, wpis do CRBR jako beneficjent rzeczywisty przy ponad 25 % **[W]** | jak obok |

**Wniosek.** Wspólnik z UK jako współzałożyciel mniejszościowy jest bezpieczny dla wszystkich programów i dla umowy. Trzy warunki, które warto zapisać w umowie wspólników: (1) wspólnicy spoza UE/EOG łącznie nie uzyskują kontroli ani weta nad zarządem, dopóki firma korzysta z EDF, AGILE lub EUDIS; (2) co najmniej dwóch członków Rady ma obywatelstwo UE/EOG, z myślą o koncesji; (3) jeżeli wspólnik pracuje spoza UE, przed pierwszym udostępnieniem kodu robimy checkpoint G2 (rejestracja EU001 albo zezwolenie). Do potwierdzenia przez kancelarię: dokładne brzmienie wymogów koncesyjnych po nowelizacji z 2026 r. i zakres EU001 dla pozycji Basiliska.

## 4. Checkpointy prawne w cyklu rozwoju

| Bramka | Zdarzenie | Co sprawdzić przed | Kto |
|---|---|---|---|
| **G0** | zawiązanie spółki | PKD do KRS (10 pozycji, § 4 ust. 5); wojskowe kody zostają w umowie (§ 4 ust. 6) do ujawnienia później bez aktu notarialnego | kancelaria |
| **G1** | pierwszy test w terenie | ULC (kategoria, SORA), urząd morski / żeglugi śródlądowej, UKE, ubezpieczenie, RODO przy nagraniach | Rada |
| **G2** | pierwsze udostępnienie technologii poza firmę: partner, spółka celowa, inwestor w due diligence, chmura, współpracownik spoza UE | klasyfikacja dual-use (§ 28 ust. 2); zgoda z § 27 ust. 6 na dostęp spoza UE/NATO; czy licencja jest „obrotem technologią" z wykazu koncesyjnego (§ 33 ust. 3); NDA; ITAR/EAR komponentów | dyrektor ds. zgodności |
| **G3** | pierwszy wariant „specjalnie zaprojektowany lub zmodyfikowany do celów wojskowych" | kwalifikacja wyrobu do wykazu WT przed rozpoczęciem prac fizycznych; koncesja MSWiA przed wytwarzaniem; ujawnienie 30.32.Z w KRS; WSK | Rada + kancelaria |
| **G4** | pierwszy kontrakt z MON, NATO, integratorem | klauzule niejawności → świadectwo bezpieczeństwa przemysłowego (start procedury ≥ 12 miesięcy wcześniej); zamówienia obronne; offset | Rada + kancelaria |
| **G5** | pierwszy eksport lub transfer poza UE | zezwolenie MRiT albo potwierdzenie braku kontroli; kraj i użytkownik końcowy; sankcje | dyrektor ds. zgodności |
| **G6** | runda z inwestorem spoza UE/EOG | Kryterium § 11, kontrola inwestycji (§ 12 ust. 2 lit. e), skutki dla EDF/AGILE (sekcja 3) | WZ + kancelaria |

Zasada: **B+R można zacząć bez koncesji; przed pierwszym prototypem wojskowym i przed pierwszym przekazaniem technologii za granicę robimy formalny checkpoint prawny i klasyfikacyjny.** Ta zasada z rozmowy z ChatGPT jest trafna i warto ją wpisać do regulaminu Rady.

---

## 5. Ocena tez z rozmowy z ChatGPT

| Teza | Ocena | Komentarz |
|---|---|---|
| Nie ma w Polsce ogólnej licencji na R&D dual-use | trafna | brak takiego reżimu; ograniczenia pojawiają się przy wyrobie wojskowym, obrocie, eksporcie i informacjach niejawnych |
| Dual-use (UE) i „wyrób o przeznaczeniu wojskowym" (ustawa koncesyjna) to różne pojęcia | trafna | kluczowe rozróżnienie; dual-use to kontrola obrotu z zagranicą, koncesja to reżim wytwarzania i obrotu w kraju |
| Koncesji wymaga wytwarzanie wyrobów i obrót wyrobami oraz technologią; nie ma koncesji na „tworzenie technologii" | trafna z zastrzeżeniem **[W]** | zgodne z konstrukcją ustawy; brzmienie definicji „wytwarzanie" (czy obejmuje modyfikację) i „obrót" (czy obejmuje licencję) do potwierdzenia u kancelarii |
| Cywilny quadcopter + własne badania to inny reżim niż wojskowy BSP | trafna | zgodne z WT V („specjalnie zaprojektowane lub zmodyfikowane") |
| Napis „prototyp" nie wyłącza koncesji | trafna | istotna przestroga |
| Elektroniczne przekazanie oprogramowania poza UE jest eksportem | trafna **[W]** | definicja eksportu w 2021/821 obejmuje transmisję i udostępnienie elektroniczne |
| Autonomiczny lot jako technologia strategiczna cywilna | ChatGPT nie odpowiedział wprost | prawdopodobnie pozycja 9A012.b.2 z oprogramowaniem 9D i technologią 9E; budowanie wolne, obrót z zagranicą kontrolowany; szczegóły w sekcji 2.2a |
| Nowelizacja kontroli obrotu od 22 kwietnia 2026 r. | trafna **[Z]** | ustawa z 13 marca 2026 r., Dz.U. 2026 poz. 471; zmienia także ustawę koncesyjną |
| Testy UAV: kategoria szczególna, SORA, ULC; radio; broń osobno | trafna | pominął prawo morskie przy USV i zgodność produktową (AI Act, maszynowe, CRA) |
| Świadectwo ABW dopiero przy informacjach „poufne" i wyżej | trafna **[W]** | dodać: procedura trwa długo, start z wyprzedzeniem |
| Prawo lotnicze dostosowane w 2025 r. | trafna **[Z]** | ustawa z 24 stycznia 2025 r., w mocy od 27 lutego 2025 r. |
| EIC dopuszcza dual-use od 17 czerwca 2026 r.; grant do 2,5 mln EUR | trafna **[Z]** | inwestycja EIC Fund: **do 30 mln EUR**, nie 1–10 mln; wnioski dual-use od 9 lipca 2026 r.; sesje pełnych wniosków 2 września i 4 listopada 2026 r.; osobny STEP Defence Scale-Up zamyka się 28 października 2026 r. |
| PFR Deep Tech: 300 mln zł | częściowo **[Z]** | 300 mln zł od PFR plus co najmniej 300 mln zł od inwestorów prywatnych, łącznie 600 mln zł; przez 3–5 funduszy VC; ok. 65 % już przydzielone |
| Ścieżka SMART: tegoroczny nabór zakończony | nietrafna **[Z]** | nabór 26 lutego – 31 marca 2026 r. się zakończył, ale PARP otwiera kolejny dla MŚP **29 października – 29 grudnia 2026 r.**; NCBR dla konsorcjów do 16 października 2026 r. |
| EDF: konsorcjum 3 podmiotów z 3 państw, lżejsze wyjątki dla technologii przełomowych | trafna **[Z]** | pominął warunek braku kontroli przez państwo trzecie niestowarzyszone, który wchodzi w kolizję z częścią NATO w Kryterium (sekcja 3) |
| EUDIS: do 60 tys. EUR | w przybliżeniu **[Z]** | voucher Business Accelerator wynosi 65 tys. EUR |
| AGILE: 115 mln EUR od 2027 r. | trafna **[Z]** | granty 1–5 mln EUR, 100 % kosztów |
| DIANA: TRL 4–7, dla startupów bez doświadczenia obronnego | trafna **[Z]** | TRL co najmniej 4, niżej przy silnym potencjale dual-use |
| Strategia: warstwa autonomii zamiast „produkcji dronów", COTS hardware, jawne B+R, checkpoint przed wariantem wojskowym | trafna jako strategia | zgodna z § 4 ust. 1–4 umowy (podstawowa działalność to oprogramowanie autonomii, platformy cywilne) i z konstrukcją Kryterium; zmniejsza koszt zgodności na starcie |
| Morze jako pierwsze laboratorium | trafna technicznie, niekompletna prawnie | wymaga zgody urzędu morskiego, rejestracji jednostki powyżej 7,5 m lub 15 kW, radiostacji; brak kompletnego reżimu MASS w Polsce |

---

## 6. Co z tego wynika dla dokumentów spółki

1. **Umowa (psa.tex):** bez zmian koniecznych. Opcjonalnie w § 4 ust. 7 zdanie, że samo wskazanie kodu PKD nie jest podstawą do rozpoczęcia działalności regulowanej.
2. **law.md:** dopisać do 4.1.1 pytanie o koncesję przy licencjonowaniu technologii spółce celowej (§ 33 ust. 3) i o wyłączenia B+R w ustawie z 2019 r.; do 4.2.2 pytanie o klasyfikację dual-use produktów cywilnych, ITAR/EAR i transfer wewnątrzunijny; nowe pytanie o kolizję Kryterium (NATO spoza UE) z art. 9 EDF.
3. **Regulamin Rady:** wpisać bramki G1–G6 jako obowiązkowe checkpointy dyrektora ds. zgodności (§ 21 ust. 7, § 28 ust. 4 umowy).
4. **Plan B+R:** pierwszy program (USV albo UAV) zaplanować tak, aby do TRL 4–5 pozostawał w pełni jawny i cywilny; to warunek wejścia do DIANA i EIC bez koncesji.

---

## 7. Źródła sprawdzone 21 września 2026 r.

- Ustawa z 13 czerwca 2019 r. — https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20190001214
- Rozporządzenie Rady Ministrów z 17 września 2019 r. (Dz.U. 2019 poz. 1888) — https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20190001888
- Ustawa z 13 marca 2026 r. (Dz.U. 2026 poz. 471) — https://eli.gov.pl/eli/DU/2026/471/ogl ; omówienie: https://olesinski.com/aktualnosci/nowe-zasady-obrotu-towarami-strategicznymi-8-kluczowych-zmian-dla-sektora-dual-use-i-zbrojeniowego/
- Ustawa z 24 stycznia 2025 r. o zmianie ustawy Prawo lotnicze — https://www.prawo.pl/akty/dz-u-2025-179,22110121.html
- Ustawa z 12 kwietnia 2018 r. o rejestracji jachtów i innych jednostek pływających do 24 m — https://orka.sejm.gov.pl/proc8.nsf/ustawy/2261_u.htm ; REJA24 — https://portal.reja24.gov.pl/
- EIC otwiera się na dual-use (17 czerwca 2026) — https://eic.ec.europa.eu/news/european-innovation-council-opens-defence-and-dual-use-technologies-2026-06-17_en ; terminy 2026 — https://www.zabala.eu/news/eic-accelerator-2026-updates/ ; https://www.onesynergy.eu/2026/06/29/eic-accelerator-2026-july-cutoff/
- PFR Deep Tech — https://pfrventures.pl/en/artykul/pfr-deep-tech-pln-600-million-investments-advanced-technologies ; https://radar.rp.pl/mspo/art45102551-kapital-dla-bezpieczenstwa-pfr-wzmacnia-polski-przemysl-obronny-i-technologie-dual-use
- Ścieżka SMART 2026 — https://www.parp.gov.pl/component/grants/grants/sciezka-smart ; https://mdotacje.pl/sciezka-smart-parp-2026/
- AGILE — https://defence-industry-space.ec.europa.eu/eu115-million-programme-agile-and-rapid-defence-innovation-agile-2026-03-26_en
- NATO DIANA 2026 — https://www.nato.int/cps/en/natohq/news_235771.htm ; https://www.techuk.org/resource/nato-s-2026-diana-innovation-challenges-announced.html
- EDF, art. 9 — https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32021R0697 ; https://gowlingwlg.com/en/insights-resources/articles/2026/the-european-defence-fund
- EUDIS — https://eudis.europa.eu/eudis-tracks/business-accelerator_en ; https://eudis.europa.eu/eudis-tracks/cascade-funding_en
