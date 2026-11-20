---
title: "Basilisk Systems P.S.A. — audyt całościowy nr 4"
subtitle: "Umowa spółki 3.3-S, umowa akcjonariuszy 1.7, umowy IP 1.6, Cennik, NDA, polityka, licencje 1.0, podręczniki, komentarz"
date: "20 listopada 2026 r."
---

# 1. Zakres, metoda i wynik w skrócie

**Zakres.** Wszystkie dokumenty Basilisk w stanie z gałęzi `dev_licencje`:

- umowa spółki (`psa.tex`, `psa_en.tex`);
- umowa akcjonariuszy, czyli UA (`basilisk_sha*.tex`);
- umowy IP (`basilisk_ip*.tex`);
- Cennik, NDA, polityka bezpieczeństwa;
- wzory licencji (`basilisk_licencje.md`);
- 4 podręczniki decyzji, komentarz do umowy, bibliografia.

**Metoda.** Audyt objął 3 niezależne przeglądy:

1. zgodność z prawem — treść postanowień porównana z tekstami ustaw z gałęzi `dev_codex` (KSH z nowelizacją 2026, KC, KPC, KP, KRO, PrAut, PWP, UZNK, PIT, ustawa koncesyjna, UONI, akty UE);
2. spójność — odesłania, liczby, terminy, PL/EN, diagramy, kompilacja;
3. ryzyka biznesowe — perspektywa założycieli, inwestorów i klientów obronnych.

Najważniejsze ustalenia sprawdziłem osobiście w tekstach ustaw; są oznaczone **[sprawdzone w ustawie]**. Ustalenia oparte na ocenie lub aktach, których tekstu nie ma w `dev_codex`, oznaczono **[do weryfikacji]**.

**Wynik w skrócie.**

- **Kompilacja:** 18 dokumentów kompiluje się bez nierozwiązanych odwołań i przepełnień.
- **Spójność PL/EN:** liczba paragrafów, ustępów i punktów, kwoty, terminy i odesłania zgadzają się w 6 parach umów, w podręcznikach i w komentarzu.
- **Większość przepisów jest poprawnie zastosowana.** Dotyczy to m.in.:
  - ograniczeń zbywania akcji;
  - emisji i limitów;
  - reprezentacji wobec dyrektorów;
  - większości głosów;
  - kar z waloryzacją;
  - pól eksploatacji;
  - uprawnień z art. 75–76 PrAut w licencjach.
- **3 problemy blokują albo poważnie utrudniają działalność** i powinny zostać usunięte przed aktem notarialnym:
  - licencja założycieli bez prawa do sublicencji (K1);
  - impas przy podziale 50/50 (K2);
  - brak pakietu dokumentów zawiązania (K4).
- **Kolejne 5 problemów krytycznych** dotyczy rund inwestorskich, koncesji i vestingu.
- **Kilkanaście błędów redakcyjnych i odesłań** da się poprawić od razu, bez decyzji biznesowych (rozdział 5).

**Priorytety:**

| Poziom | Liczba | Kiedy |
|------------------|------|------------------------------------|
| Krytyczne (K) | 8 | przed aktem notarialnym, póki łatwo o jednomyślność |
| Ważne (W) | 22 | przed pierwszą rundą / pierwszym kontraktem obronnym |
| Spójność (S) | 14 | od razu — poprawki techniczne |
| Niskie (N) | 15 | przy najbliższej wersji dokumentów |

# 2. Krytyczne

| ID | Problem | Podstawa | Rekomendacja | Gdzie |
|------|------------------------------------|------------------|------------------------------------|------------|
| **K1** | **Licencja założycieli nie pozwala na sublicencje.** Licencja na technologię niewniesioną aportem (§ 14 ust. 2) i licencja tymczasowa do czasu aportu (§ 4 ust. 6) nie dają Spółce prawa udzielania sublicencji. Spółka nie może więc licencjonować klientom produktów zawierających ten kod — wzory licencji nie mają w tym zakresie podstawy. | art. 67 ust. 3 PrAut: licencjobiorca bez postanowienia umowy „nie może upoważnić innej osoby” **[sprawdzone w ustawie]** | Dopisać w obu miejscach: „…z prawem udzielania sublicencji klientom, integratorom i podmiotom zależnym w zakresie niezbędnym do komercjalizacji produktów Spółki; sublicencje udzielone w okresie licencji pozostają w mocy po jej wygaśnięciu.” Dodać pozycję do listy kontrolnej w licencjach (Załącznik D). | US § 4 ust. 6, § 14 ust. 2; licencje Zał. D |
| **K2** | **Impas 50/50.** Sprawy wymagające bezwzględnej większości głosów oddanych to powołanie i odwołanie dyrektorów, sprawozdanie finansowe, zysk i wynagrodzenia. Przy głosowaniu A (50%) przeciw B+C+D+E (50%) uchwała nie zapada. Mechanizm impasu w UA obejmuje tylko emisje i transakcje ponad 500 tys. zł i kończy się na mediacji. Po upływie kadencji Spółka może zostać bez Rady. | art. 300⁹⁸ § 1 KSH (bezwzględna większość) **[sprawdzone w ustawie]**; US § 13 ust. 3 | Jedna z opcji: (a) zmienić podział na 500 001 / 499 999 akcji; (b) uprawnienia indywidualne z art. 300²⁸ KSH **[sprawdzone w ustawie]** — A powołuje 2 dyrektorów, B jednego, C–E wspólnie jednego, dyrektora niezależnego wybiera WZ 75%; (c) rozszerzyć mechanizm impasu na sprawy z § 13 ust. 3 i dodać rozstrzygnięcie przez niezależnego eksperta po bezskutecznej mediacji. | US § 10, § 13 ust. 3; UA § 11 |
| **K3** | **Brak ścieżki rundy inwestorskiej.** Drag-along, tag-along i ROFR są wyłączone. Lock-up trwa 12 miesięcy. Wprowadzenie ich później wymaga zgody każdego akcjonariusza, którego dotyczy, a pozbawienie prawa poboru — 4/5 głosów. Każdy Założyciel z 10% może zablokować albo renegocjować rundę. Sprzedaż 100% akcji inwestorowi strategicznemu wymaga zgody wszystkich, a A może sprzedać 50% bez prawa przyłączenia mniejszości. | art. 300⁹⁸ § 3, 300¹⁰⁶ § 2 KSH **[sprawdzone w ustawie]**; US § 8 ust. 6, § 17 ust. 1 | Dodać do UA paragraf „Kwalifikowana Runda”: próg (kwota albo wycena) i katalog dopuszczalnych warunków (1× non-participating, broad-based weighted average, 1 miejsce w Radzie albo obserwator, doładowanie ESOP, drag na określonych warunkach). Założyciele zobowiązują się głosować „za” i nie wykonywać prawa poboru, z pełnomocnictwem i karą. Do US i UA dodać tag-along przy zmianie kontroli i ROFR pro rata. To wcześniejsza świadoma decyzja (wariant prosty) — do ponownego rozważenia. | UA § 10; US § 8 |
| **K4** | **Brak pakietu dokumentów zawiązania.** Umowa wymaga uchwał przy akcie notarialnym: pierwsi dyrektorzy, podmiot prowadzący rejestr akcjonariuszy, pierwszy regulamin WZ, pełnomocnik do umów z Założycielami-dyrektorami. Brak pełnomocnika grozi nieważnością umów IP i UA. `uchwaly.tex` jest nieaktualny i odsyła do starej numeracji. | art. 300⁷⁹ § 1 KSH **[sprawdzone w ustawie]**; US § 3 ust. 5, § 12 ust. 5, § 17 ust. 6 | Przygotować pakiet: uchwały 1–5 i regulamin WZ. Pełnomocnik spoza Stron, umocowany do UA z załącznikami, Umów nr 1 i 2 i potwierdzeń kwartalnych w zakresie z § 11 ust. 3. Zaktualizować `uchwaly.tex` do wersji 3.3-S. | pakiet aktu |
| **K5** | **Koncesja i PKD.** W § 2 brak kodów działalności wojskowej. Koncesja jest wymagana na wytwarzanie i obrót technologią wojskową, także na licencjonowanie. Bada się m.in. akcjonariuszy z co najmniej 20% (dziś A i B). | PKD 2025: 30.32.Z, 30.40.Z, 33.18.Z **[sprawdzone w rozporządzeniu]**; art. 7 i 10 ustawy koncesyjnej **[sprawdzone w ustawie]** | Dopisać 30.32.Z, 30.40.Z i 33.18.Z do kodów nieujawnianych przy pierwszym wpisie. Wskazać 2 Założycieli-dyrektorów do przygotowania zawodowego i badań. W UA: obowiązek akcjonariuszy z co najmniej 20% dostarczania dokumentów i informowania o zmianach. | US § 2 ust. 2; UA |
| **K6** | **Seria F za pracę a obowiązek zbycia.** Odchodzący z serii F za pracę nie wniósł jeszcze całego wkładu, a musi zbyć akcje. Nabywca odpowiadałby solidarnie za cudzą, niewykonaną pracę. | art. 300⁴⁰ § 3 KSH **[sprawdzone w ustawie]** | W § 6 ust. 4: „Z Dniem Ustania Zaangażowania niewniesiona część wkładu w postaci pracy lub usług przekształca się w obowiązek zapłaty jej wartości określonej w uchwale emisyjnej.” Alternatywa: seria F tylko za wkład pieniężny. | US § 6 ust. 4, § 9 ust. 4 |
| **K7** | **Vesting i leaver — ryzyka sporu.** Do rozstrzygnięcia razem: (a) akcje objęte za wartościowy aport IP wracają po 0,01 zł, a Spółka zatrzymuje IP — ryzyko zarzutu z art. 58 KC; (b) „istotna przyczyna” nie jest zdefiniowana, a ustanie zaangażowania stwierdza Rada, w której A ma głos rozstrzygający; (c) niepowołanie na kolejną kadencję liczy się jako Odejście Zwykłe; (d) nabywcę akcji niezwolnionych wybiera Rada — po odejściu B wskazanie A daje mu ok. 65%; (e) pole „data rozpoczęcia” w Załączniku nr 1 jest fakultatywne, więc vesting A nie jest zagwarantowany; (f) brak zawieszenia przy urlopie rodzicielskim lub chorobie. | art. 58 § 2 KC **[sprawdzone w ustawie]**; US § 9 ust. 2–5; UA § 3–4 | (a) cena = wyższa z: ceny emisyjnej i wartości wkładu na akcję, nie wyższa niż wartość godziwa, albo wyłączenie akcji za aport z obowiązku zbycia; (b) zamknięta lista istotnych przyczyn; (c) niepowołanie albo odwołanie bez istotnej przyczyny = Odejście Uzasadnione; (d) domyślnie pro rata dla pozostałych Założycieli, a inny nabywca tylko za zgodą WZ 75%; (e) w UA: wszyscy Założyciele Pierwotni podlegają vestingowi; (f) urlopy i choroba do 12 miesięcy zawieszają vesting. | US § 9; UA § 3–4 |
| **K8** | **Licencje nie pasują do zamówień obronnych.** OWL mają pierwszeństwo przed warunkami nabywcy (w zamówieniach publicznych wiąże wzór zamawiającego). Terytorium wyklucza misje NATO. Licencji nie można przenieść w ramach Skarbu Państwa. Sublicencja dla integratorów jest zakazana. Działania wojenne są siłą wyższą. Przy licencji wieczystej opłaconej z góry limit odpowiedzialności spada prawie do zera. | ocena praktyki zamówień **[do weryfikacji]** | Dodać Moduł M4 „sektor publiczny i obronny”: OWL jako załącznik do umowy zamawiającego; terytorium obejmujące miejsca rozmieszczenia Sił Zbrojnych RP i misje NATO/UE; przeniesienie w ramach Skarbu Państwa; sublicencja dla integratorów i serwisu; wsparcie 10–20 lat; działania wojenne nie są siłą wyższą; limit odpowiedzialności jako % wartości umowy. | licencje |

# 3. Ważne

## 3.1. Prawne

| ID | Problem | Podstawa | Rekomendacja | Gdzie |
|------|------------------------------------|------------------|------------------------------------|------------|
| W1 | **Kworum Rady.** Dyrektor w konflikcie interesów „nie jest uwzględniany przy ustalaniu wymaganego udziału”, co obniża ustawowe kworum (połowa członków); umowa może je tylko zaostrzać. | art. 300⁵⁸ § 2 KSH **[sprawdzone w ustawie]** | Dyrektor w konflikcie nie głosuje, ale liczy się do kworum. Jeśli kworum nie da się osiągnąć, zgody udziela WZ. | US § 10 ust. 6, § 3 ust. 8 lit. c |
| W2 | **Termin wskazania nabywcy przy odmowie wobec konkurenta.** 30 dni od odmowy może przekroczyć ustawowy miesiąc od zgłoszenia. | art. 300³⁹ § 3 zd. 4 KSH **[sprawdzone w ustawie]** | „…w terminie miesiąca od dnia zgłoszenia zamiaru zbycia wskazuje innego nabywcę”; odmowę z lit. e składać w 14 dni. | US § 8 ust. 3 |
| W3 | **Kary i zakaz konkurencji wobec Założyciela-pracownika.** Kary z UA obejmują też naruszenia w czasie stosunku pracy. Zakaz po odejściu bez umowy z art. 101² KP grozi zarzutem obejścia przepisów. | art. 101¹ § 2, 101² § 3 KP; SN II PK 120/07 **[sprawdzone w orzeczeniu]** | „Kar z ust. 1 lit. a–b nie stosuje się do naruszeń w czasie stosunku pracy.” „Wobec pracownika zakaz po ustaniu stosunku pracy obowiązuje wyłącznie na podstawie umowy z art. 101² KP.” | UA § 8 ust. 4, § 9 ust. 1 |
| W4 | **Forma zgody na wpis od 18.02.2027.** Pełnomocnictwo z Załącznika B UA nie ma określonej formy, więc pełnomocnik może nie złożyć skutecznej zgody na wpis nabywcy (vesting). | art. 300³⁴ § 3 KSH (od 18.02.2027) **[sprawdzone w ustawie]**; art. 99 § 1 KC | W UA § 5 ust. 3 i Załączniku B: pełnomocnictwo z podpisem notarialnie poświadczonym albo kwalifikowanym i obejmujące zgodę na wpis. | UA § 5, Zał. B |
| W5 | **Moment cesji aportu.** „Najpóźniej w dniu zawarcia umowy spółki” dopuszcza cesję przed aktem, gdy spółka w organizacji jeszcze nie istnieje. | art. 300¹¹ § 1 KSH | „w dniu zawarcia niniejszej umowy, niezwłocznie po jej zawarciu”. | US § 4 ust. 6; UA § 6 ust. 1; IP wstęp |
| W6 | **Spór o ustanie zaangażowania.** Termin 6 miesięcy biegnie mimo sporu. Wyjątek „mniej niż 30 dni” w UA § 4 ust. 5 pozwala przenieść akcje w trakcie sporu. Leaver głosuje akcjami niezwolnionymi i może zablokować rundę. | logika mechanizmu; art. 64 KC | Zawieszenie biegu terminów w sporze; usunąć wyjątek 30 dni; porozumienie głosowe dla Akcji Niezwolnionych od Dnia Ustania Zaangażowania. | US § 9 ust. 4; UA § 4 ust. 5 |
| W7 | **Właściwość sądu i arbitraż w licencjach.** Umowa „w formie dokumentowej” nie daje skutecznej klauzuli sądu ani zapisu na arbitraż przez odesłanie do OWL. | art. 46 § 1, 1162 § 2 KPC **[sprawdzone w ustawie]** | Zamówienie podpisuje się własnoręcznie albo kwalifikowanym podpisem elektronicznym. | OWL § 21–22 |
| W8 | **Dane Operacyjne a RODO.** Logi mogą zawierać dane osobowe. Trenowanie na nich modeli to cel własny Spółki, czyli Spółka staje się administratorem. | art. 28 ust. 10 RODO **[sprawdzone w akcie]** | „Dane Operacyjne wykorzystuje się do rozwoju po anonimizacji.” | OWL § 10 ust. 2 |
| W9 | **Monitoring pracowników.** Przegląd dzienników dostępu to monitoring w rozumieniu KP i wymaga regulaminu oraz uprzedzenia z 2-tygodniowym wyprzedzeniem. | art. 22² § 6, 22³ § 4 KP | Dodać ustęp o monitoringu i wprowadzić go regulaminem pracy albo obwieszczeniem. | Polityka § 4, § 7 |
| W10 | **Ścieżka przy milczeniu Rady** nie działa dla akcjonariusza poniżej 5%, bo nie może on sam rozesłać projektu uchwały. | US § 12 ust. 3 | W § 8 ust. 1: projekt może rozesłać także akcjonariusz, którego zgłoszenie dotyczy. | US § 8 ust. 1 |
| W11 | **Akcje własne odsprzedane** uczestnikom programu albo serii F nie są objęte obowiązkiem zbycia. | art. 300³³ § 1 pkt 11 KSH | Rozszerzyć § 9 ust. 1 na akcje własne zbyte na podstawie § 3 ust. 7 lit. b, jeżeli uchwała tak stanowi. | US § 9 ust. 1 |

## 3.2. Inwestorzy i finansowanie

| ID | Problem | Rekomendacja | Gdzie |
|------|------------------------------------|------------------------------------|------------|
| W12 | **ESOP:** każda emisja serii P wymaga WZ 75% i 4/5 przy pozbawieniu prawa poboru; brak regulaminu programu; uczestnicy nie są stronami UA. | Umowa spółki może sama wyłączyć prawo poboru do akcji serii P (art. 300¹⁰⁶ § 1 KSH **[sprawdzone w ustawie]**). Do tego jedna emisja warunkowa z warrantami i regulamin (4 lata, roczny cliff, good/bad leaver, art. 24 ust. 11–12b PIT). | US § 5 ust. 6, § 7 |
| W13 | **Instrumenty seed:** konwersja pożyczki albo SAFE wymaga nowej serii, zmiany umowy u notariusza i 4/5. | Upoważnienie dla „serii S” z art. 300¹⁰³ KSH z wyłączeniem prawa poboru dla konwersji; wzór pożyczki konwertowalnej. | US § 5 |
| W14 | **Prawa inwestora:** brak praw osobistych, praw informacyjnych i zgód serii. Zakaz konkurencji dyrektora (§ 14 ust. 5) obejmie dyrektora z funduszu, a odmowa wobec konkurenta — inwestora strategicznego. | Wzór uprawnienia z art. 300²⁸ KSH (dyrektor albo obserwator), wyjątek portfelowy w § 14 ust. 5, prawa informacyjne w UA w granicach UONI. | US § 8 ust. 2 lit. e, § 13, § 14 ust. 5 |
| W15 | **UA i NDA zbyt ostre dla inwestorów finansowych:** nabywca musi przyjąć zakaz konkurencji i kary, a NDA z karą przed pierwszą rozmową. | Podział UA na część Założycieli i część wszystkich akcjonariuszy; wariant NDA dla inwestora bez kary, z wyjątkiem portfelowym. | UA § 2, § 7; NDA |
| W16 | **Technologia sprzed zawiązania** (licencja 5 lat z możliwością nieprzedłużenia, wykup po cenie biegłego wybranego przez Radę) to czerwona flaga w due diligence. | Wnieść ją albo sprzedać przed rundą. Na resztę: licencja nieodwołalna w polu działalności Spółki, cena wykupu z góry według formuły, biegły wybierany wspólnie. | US § 14 ust. 2; UA § 6 ust. 4 |
| W17 | **Podatki:** Część B2 opodatkowana od razu; cena 0,01 zł może dać przychód nabywcy i rodzić pytania z art. 19 PIT u zbywcy; wkład pracą w serii F. | Interpretacje indywidualne przed aktem i przed pierwszym przymusowym zbyciem; minimalizacja Części B2. **[do weryfikacji]** | US Zał. nr 1; UA § 6 ust. 5 |
| W18 | **Tytuł do IP:** oświadczenia „według najlepszej wiedzy”, brak obowiązku uzyskania zwolnień od uczelni i byłych pracodawców. | Kwestionariusz IP każdego Założyciela, pisemne zwolnienia albo cesje; bez nich wkład trafia do Części B2 albo poza aport. | UA § 6; Umowa nr 1 § 5 |
| W19 | **Ochrona mniejszości w budżecie:** wydatki wpisane do budżetu omijają WZ; transakcje z podmiotami powiązanymi zatwierdza sama Rada; brak praw informacyjnych dla Założyciela spoza Rady. | Budżet także za zgodą WZ albo dyrektora mniejszości; transakcje z podmiotami powiązanymi powyżej 100 tys. zł — WZ 75%; miesięczny raport dla akcjonariuszy. | US § 10 ust. 7, § 13 |

## 3.3. Obronność i regulacje

| ID | Problem | Rekomendacja | Gdzie |
|------|------------------------------------|------------------------------------|------------|
| W20 | **Świadectwo bezpieczeństwa przemysłowego:** wniosek dopiero przed umową; brak kierownika przedsiębiorcy; ABW bada strukturę kapitału. | Wyznaczyć kierownika uchwałą Rady; złożyć wniosek przy pierwszych rozmowach z Agencją Uzbrojenia; w UA obowiązek ujawniania beneficjentów rzeczywistych. | Polityka § 3 ust. 3; UA |
| W21 | **Program zgodności eksportowej:** brak dokumentu, na który powołują się umowa spółki i OWL; brak klasyfikacji produktów; SBOM bez pochodzenia z USA (ITAR/EAR) i bez ograniczeń „no military use” w licencjach modeli i danych. Udostępnienie data roomu zagranicznym analitykom to przekazanie technologii. | Program zgodności przyjęty uchwałą Rady; klasyfikacja każdego produktu; SBOM z ECCN i krajem pochodzenia; warstwowy data room. | US § 10 ust. 7, § 14 ust. 4; OWL § 12, Zał. A |
| W22 | **CRA, RED, AI Act, rozporządzenie maszynowe, nowa dyrektywa o odpowiedzialności za produkty:** OWL dają poprawki bezpieczeństwa przez 24 miesiące i tylko w płatnym wsparciu, a dla produktów cywilnych mogą obowiązywać dłuższe okresy i bezpłatne łatki. Kontrola składu akcjonariatu dla EDF, koncesji i statusu MŚP. | Rozdzielić produkty cywilne i wojskowe; procedura obsługi podatności; analiza zgodności przed wprowadzeniem do obrotu; w UA ograniczenie przeniesienia kontroli poza UE/EOG w czasie projektów EDF i koncesji. **[do weryfikacji — tekstów CRA, RED, 2023/1230 i 2024/2853 brak w dev_codex]** | OWL § 7; Zał. D; UA |

# 4. Uwagi do licencji i dokumentów pomocniczych (niskie)

| ID | Problem | Rekomendacja |
|------|------------------------------------------|------------------------------|
| N1 | NDA § 3 ust. 3: zakaz dekompilacji bez zastrzeżenia uprawnień ustawowych (art. 75–76 PrAut **[sprawdzone w ustawie]**). | Dopisać „z zastrzeżeniem art. 75 ust. 2 i 3 PrAut”. |
| N2 | OWL § 19 ust. 1: wyłączenie wypowiedzenia dotyczy tylko licencji „wieczystej”, a licencja ponad 5 lat też staje się bezterminowa (art. 68 ust. 2 PrAut **[sprawdzone w ustawie]**). | Rozszerzyć na licencje ponad 5 lat. |
| N3 | Moduł M2.6: ograniczenie odpowiedzialności przy licencji ewaluacyjnej bez zastrzeżenia produktu niebezpiecznego i szkody na osobie (art. 449⁹ KC **[sprawdzone w ustawie]**). | „z zastrzeżeniem § 15 ust. 2 pkt 2–3 OWL”. |
| N4 | Moduł M1.2: sprzedaż urządzenia z programem wyczerpuje prawo do dalszego obrotu tym egzemplarzem (art. 51 ust. 3 PrAut). | Oprzeć ograniczenie przeniesienia na kontroli eksportu i zobowiązaniu umownym. |
| N5 | OWL § 17 ust. 2: wydanie kodu z depozytu „w razie upadłości” może kolidować z prawem upadłościowym. **[do weryfikacji]** | Wyzwalać zaprzestaniem wsparcia albo likwidacją. |
| N6 | OWL § 1 ust. 2: przedsiębiorca na prawach konsumenta (art. 385⁵ KC). | Oświadczenie o zawodowym charakterze umowy. |
| N7 | Cennik zmieniany jednostronnie w trakcie umowy wiąże tylko, gdy twórca nie wypowie umowy (art. 384¹ KC). | Prawo wypowiedzenia Umowy nr 2 przy zmianie Cennika. |
| N8 | Umowa nr 2 § 7 i umowa spółki § 14 ust. 3: brak wprost wyjątku dla sygnalistów (postanowienie i tak nieważne w tym zakresie). | Dopisać wyjątek. |
| N9 | Polityka: „księga akcyjna” zamiast rejestru akcjonariuszy; brak zawiadamiania osób (art. 34 RODO) i ewidencji naruszeń (art. 33 ust. 5); sprzeczność punktów (3) i (4) wzoru oświadczenia. | Poprawki redakcyjne. |
| N10 | Umowa spółki § 3 ust. 6: obowiązek zgody na e-mail jest niewymuszalny (art. 300³³ § 1 pkt 5 KSH). | „…albo wskazuje adres do doręczeń elektronicznych”. |
| N11 | Umowa spółki § 3 ust. 7: zamknięty katalog celów nabycia akcji własnych koliduje z nabyciem z mocy ustawy. | „z zastrzeżeniem art. 300⁴⁷ § 1 pkt 3–5 KSH”. |
| N12 | UA § 4 ust. 1 i Załącznik B: otwarty katalog przesłanek, dane o zdrowiu bez ograniczeń, szeroka substytucja pełnomocnictwa (art. 9 RODO, art. 106 i 108 KC). | Zamknięty katalog; tylko orzeczenie; pełnomocnik nie może być nabywcą. |
| N13 | Umowa nr 1 § 2 ust. 4: automatyczny zwrot praw nie chroni licencji udzielonych przez spółkę w organizacji. | Zobowiązanie do zwrotnej cesji z zachowaniem licencji. |
| N14 | Umowa spółki § 14 ust. 1: „przysługują Spółce” samo nie przenosi praw; § 15 ust. 4 — pierwszy rok obrotowy niejednoznaczny. | „Spółka nabywa te prawa na podstawie umów…”; jedna konkretna data. |
| N15 | Spółka wpisana przed 18.02.2027 musi w 3 miesiące zgłosić do KRS dane podmiotu prowadzącego rejestr (nowelizacja KSH 2026). | Do harmonogramu zgodności. |

# 5. Spójność — poprawki techniczne (od razu)

| ID | Problem | Poprawka |
|------|------------------------------------------|------------------------------|
| S1 | **Kalendarz terminów w obu pełnych podręcznikach** odsyła do „Umowa nr 2 § 8” przy wydaniu utworów w 14 dni; właściwy jest **§ 7 ust. 4** (zweryfikowane). Ten sam błędny numer „§ 8” podawałem wcześniej w podsumowaniach i w opisie PR D (#11) przy karze dla współpracowników B2B — sama umowa jest poprawna. | Zmienić na § 7 ust. 4, najlepiej przez `\ref{u2:oswiadczenia}`. |
| S2 | Diagram progów: pas „finansowanie, zabezpieczenie, zbycie aktywów” pokazuje WZ 75% powyżej 500 tys. zł bez względu na budżet; umowa wymaga WZ tylko poza budżetem. | Opisać pas „poza budżetem”. |
| S3 | Licencje (wprowadzenie, Zał. D poz. 7): brak progu WZ 75% dla transakcji poza budżetem ponad 500 tys. zł. | Dopisać. |
| S4 | Umowa spółki § 17 ust. 6 nie nadąża za nowym § 11 ust. 3 (tylko „zawarcie”, bez Umowy nr 2). | Odesłać do zakresu z § 11 ust. 3 i dodać § 14 ust. 1. |
| S5 | Forma zgody na wpis z § 8 ust. 1 nie trafiła do komentarza ani do UA (zob. W4). | Dodać art. 300³⁴ § 3 KSH w komentarzu. |
| S6 | Polityka twierdzi, że powołuje się na nią UA — UA o niej nie wspomina. | Usunąć odwołanie albo dodać je w UA § 7. |
| S7 | Diagram „Umowy z dyrektorami”: „ani inny dyrektor” przedstawione jako wymóg, a to rekomendacja. | „Nie strona umowy; zalecenie: nie dyrektor”. |
| S8 | Diagram zgody na zbycie: gałąź lock-up kończy się na WZ, bez przejścia do Rady (zgoda Rady jest zawsze potrzebna). | Dodać strzałkę WZ → Rada. |
| S9 | Diagram odejścia: „Rozwiązanie bez przyczyny” zniekształca przesłankę i nie używa nazwy „Odejście Uzasadnione”; komentarz w skrócie nieprecyzyjny. | Ujednolicić z UA § 4 ust. 3 i US § 9 ust. 5. |
| S10 | Podpis diagramu progów w wersjach PL ma zakodowany numer paragrafu. | Użyć `\ref`. |
| S11 | Komentarz do § 9 ust. 6: art. 101 § 1 KC — UA powołuje już § 1 i 2. | „art. 101 § 1–2 KC”. |
| S12 | Wzór vestingu w § 9 ust. 2: brak zakresów „dla m < 6” (Założyciel) i „0 dla m < 12” (seria F). | Dopisać zakresy. |
| S13 | `build.sh`: 2 przebiegi nie wystarczają dla podręcznika (zmieniają się numery stron w spisie treści). | Trzeci przebieg albo pętla do ustalenia etykiet. |
| S14 | `build.sh`: przy budowaniu wybranych plików nie dobudowuje zależności (`psa_en`, `basilisk_sha*`). | Automatyczne zależności. |

# 6. Co jest dobrze

- **Zbywanie akcji:** zamknięta lista przyczyn odmowy, ścieżka przy milczeniu Rady (uchwała, potem sąd, art. 64 KC), forma zgody od 2027 r.
- **Emisje i większości:** limity i termin emisji (art. 300¹⁰³); 4/5 przy wyłączeniu prawa poboru; 75% wszystkich głosów surowsze od ustawy; zgoda akcjonariusza przy zwiększeniu jego obowiązków (art. 300⁹⁸ § 3).
- **Vesting:** jako obowiązek związany z akcją, ujawniany w rejestrze; Spółka nie jest nabywcą; automatyczne zwolnienie przy dobrym odejściu.
- **Reprezentacja wobec dyrektorów:** zgodna z art. 300⁷⁹ KSH, z zakresem z uchwały III CZP 42/18.
- **Kary umowne:** tylko za zobowiązania niepieniężne, z limitem i waloryzacją (art. 483–484, 358¹ § 2 KC); wyłączenia dla sygnalistów w UA i NDA.
- **Umowy IP:** pola eksploatacji (także trening modeli), forma pisemna, art. 77 PrAut, rozdzielenie Części B1 i B2.
- **Licencje:**
  - uprawnienia z art. 75–76 PrAut zachowane;
  - okres i terytorium wpisywane wprost;
  - odpowiedzialność za szkodę umyślną i produkt niebezpieczny nieograniczona;
  - licencja zwrotna tylko niewyłączna (TTBER);
  - brak zdalnego wyłączania w działaniu i aktywacja bez sieci, co jest silnym argumentem wobec wojska.
- **Polityka bezpieczeństwa:** kategoria „Kontrolowane”, rejestr dostępów i procedura przy odejściu stanowią dowód „niezbędnych działań” z art. 11 UZNK (I CKN 304/00).
- **Technika:** pełna kompilacja i parzystość PL/EN; odesłania pobierane automatycznie z umów.

# 7. Proponowana kolejność

1. **Od razu, bez decyzji biznesowych:** S1–S14 oraz W1, W2, W4, W5, W7, N1–N3.
2. **Przed aktem notarialnym — decyzje Założycieli:** K1, K2, K4, K5, K6, K7, W3, W6, W10, W11, W12 (wyłączenie prawa poboru dla serii P w umowie), W13.
3. **Przed pierwszą rozmową z funduszem:** K3, W14–W19.
4. **Przed pierwszym kontraktem obronnym:** K8, W20–W22.

Statusy wcześniejszych audytów: nadal otwarte pozostają PSA-07 (K7a), PSA-12 (W5), PSA-13 i IP-13 (K1, W16), PSA-14 (W1), PSA-15 (W11), PSA-16/17 i IP-20 (W17), PSA-18 (N14), PSA-19 (K5), SHA-04 częściowo (W6), SHA-06 i SHA-09 (N12), IP-04 (N13), IP-18 (N8). Pozostałe ustalenia z audytów 1–3 i z audytów ChatGPT są usunięte.
