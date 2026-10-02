# Komentarz do umowy spółki Basilisk Systems P.S.A. — co, dlaczego i na jakiej podstawie

Plik wyjaśnia każdą zmianę wprowadzoną do projektu umowy (`psa.tex`) po memorandum: co zmieniliśmy, dlaczego, na jakiej podstawie prawnej i w którym commicie. Jest przeznaczony dla prawnika weryfikującego umowę i dla Założycieli. Nie jest częścią umowy ani opinią prawną; pełne uzasadnienia są w `memorandum.md` (numeracja pytań jak w `law.md`).

Numery paragrafów odpowiadają aktualnej wersji `psa.tex` na gałęzi `psa_v3`. Odesłanie „memorandum 1.5.2” oznacza odpowiedź na pytanie 1.5.2; „K7” to siódma z 18 zmian koniecznych z podsumowania memorandum. Oznaczenia wiarygodności przy przepisach: **[Z]** sprawdzone w tekście aktu (`src/legal/`), **[W]** wiedza ogólna do potwierdzenia, **[?]** hipoteza.

Każdy commit można obejrzeć poleceniem `git show <hash>`; pełna lista: `git log --oneline cab9b54..psa_v3`.

## 1. Historia wersji

| Wersja | Gałąź | Co się stało | Gdzie opisane |
|---|---|---|---|
| 0.8 | `psa_correction` (commit `1264ca2`) | pierwszy pełny projekt, „tekst czysty” | `psa_feedback.tex` Część 2 (audyt § po §) |
| 0.9 – 0.9.3 | `psa_correction` | 28 commitów: Kryterium EU/NATO, zwrotne zbycie, Kwalifikowana Runda, wkłady, dziedziczenie, Załączniki | `zmiany.md` |
| 0.9.4-C | `psa_check` | wariant hybrydowy („bramka miękka”); wersja wysłana kancelarii razem z 79 pytaniami | `law.md`, `email.md` |
| memorandum 1.0 | `psa_check` | odpowiedzi na 79 pytań, sekcje T1–T9, 18 zmian koniecznych, 16 decyzji Założycieli | `memorandum.md` |
| memorandum 1.1 | `psa_check` | weryfikacja na tekstach ustaw polskich (`src/legal/`) | `memorandum.md`, Załącznik nr 5 |
| memorandum 1.2 | `psa_check` (`cab9b54`) | weryfikacja na tekstach prawa UE (EDF, 2021/821, 2026/1386, 2026/877) | `memorandum.md`, `memorandum.tex` (ramki) |
| 1.0-RC | `psa_v3` | wdrożenie uwag memorandum, jedna uwaga = jeden commit (85 commitów) | ten plik |

## 2. Przyjęte założenia wdrożenia

Wdrożenie przyjmuje rekomendacje memorandum tam, gdzie Założyciele jeszcze nie zdecydowali (Załącznik nr 2 memorandum). Każde z tych założeń prawnik i Założyciele mogą odwrócić.

- **D2** — odmowa zgody z powodu Kryterium: **wariant A** (ratalny, § 12 ust. 3); zmiany potrzebne tylko w wariancie B (m.in. K1) pominięto.
- **D3** — wyjątek dla funduszy w § 11 ust. 14: **przywrócony** w brzmieniu z odpowiedzi 1.4.3.
- **D4** — przekreślone zdania: **usunięte**, odesłania poprawione (3.4.4).
- **D5** — Kryterium wobec spadkobierców i małżonków: **utrzymane**.
- **D6** — warstwa „kontroli UE/EOG” pod art. 9 EDF: w **umowie akcjonariuszy**, nie w umowie spółki.
- **D7** — PKD przeważające **72.10.Z**; kody wojskowe nie w pierwszym wniosku.
- **D10** — rejestr akcjonariuszy prowadzi **dom maklerski**.
- **D11** — program motywacyjny: **warunkowa emisja akcji** (art. 300¹¹⁴–300¹¹⁸ KSH) jako tryb podstawowy (3.2.1).
- **Dane** — pola `[…]` z danymi (nazwiska, kwoty, daty) zostały polami — uzupełniają je Założyciele.

## 3. Zmiany paragraf po paragrafie

### § 4. Przedmiot działalności i PKD 2025

#### § 4 ust. 7: wskazanie kodu PKD nie jest podstawą do rozpoczęcia działalności regulowanej

Commit `5957c54` · memorandum 4.1.2 · klasa: opcjonalne

- **Pytanie:** Czy ujawnienie kodów wojskowych PKD przed uzyskaniem koncesji jest zasadne, czy lepiej dodać je przy zmianie umowy po koncesji?
- **Ocena brzmienia 0.9.4-C:** zgodne
- **Dlaczego zmieniono:** Projekt rozdziela dwie rzeczy, które często się myli: przedmiot działalności w umowie (§ 4 ust. 5–6, wszystkie 19 kodów) i pozycje ujawniane w KRS (tylko dziesięć z ust. 5, bez kodów wojskowych). Prawo nie zakazuje ujęcia w umowie działalności koncesjonowanej przed uzyskaniem koncesji; koncesja warunkuje jej wykonywanie (art. 5 i art. 7 ust. 1 ustawy z 2019 r.), a nie deklarację w umowie. Sąd rejestrowy nie żąda koncesji przy wpisie spółki (inaczej niż przy działalności bankowej czy ubezpieczeniowej, gdzie zezwolenie poprzedza rejestrację) [W]. § 4 ust. 7–8 dodatkowo wyjaśniają, że ujęcie kodu nie jest ani obowiązkiem, ani upoważnieniem do rozpoczęcia działalności regulowanej. […]
- **Rekomendacja memorandum:** Pozostawić kody wojskowe w § 4 ust. 6 i nie ujawniać ich w KRS przy pierwszym wpisie; ujawnić je wnioskiem o zmianę danych przy bramce G3, w kolejności ustalonej z organem koncesyjnym. Opcjonalnie wzmocnić § 4 ust. 7 zdaniem, że wskazanie kodu nie stanowi podstawy do rozpoczęcia działalności regulowanej (postulat z `psa_todo.md`); ma ono wartość wyłącznie komunikacyjną wobec banków i kontrahentów.
- **Podstawa prawna:** art. 300⁵ § 1 pkt 2 KSH (przedmiot działalności jako element umowy) [Z]; art. 300¹² § 2 pkt 2 KSH (przedmiot działalności w zgłoszeniu) [Z]; art. 40 pkt 1 ustawy o KRS („nie więcej niż dziesięć pozycji, w tym jeden przedmiot przeważającej działalności na poziomie podklasy”) [Z]; art. 5 i art. 7 ust. 1 ustawy z 13 czerwca 2019 r. (koncesja warunkuje *wykonywanie* działalności) [Z]; art. 17 ust. 1 pkt 2 tej ustawy (numer KRS we wniosku „o ile przedsiębiorca taki numer lub wpis posiada”) [Z]; art. 37 i n. ustawy Prawo przedsiębiorców [numery do sprawdzenia] [W]; art. 300⁹⁸ § 2 pkt 1, art. 300¹⁰⁰ § 2 i art. 300¹⁰² § 1–2 KSH (zmiana umowy: większość trzech czwartych, protokół notarialny, wpis do rejestru, zgłoszenie w 6 miesięcy) [Z]; § 25 ust. 1 lit. a; art. 55 ust. 1 ustawy o kosztach sądowych w sprawach cywilnych (250 zł od wniosku o zmianę wpisu) [Z].

#### § 4 ust. 8, § 3 ust. 4: klauzula koncesyjna obejmuje oprogramowanie i technologię, odesłanie dynamiczne; ocena zgodności i zezwolenia operacyjne BSP

Commit `118cdd5` · memorandum 4.1.1 · klasa: zalecane

- **Pytanie:** Czy powołana podstawa (ustawa z 13 czerwca 2019 r. o wykonywaniu działalności gospodarczej w zakresie wytwarzania i obrotu materiałami wybuchowymi, bronią, amunicją oraz wyrobami i technologią o przeznaczeniu wojskowym lub policyjnym) jest aktualna i obejmuje bezzałogowe statki powietrzne oraz ich oprogramowanie; jak ma się do prawa lotniczego i rozporządzeń UE o bezzałogowych systemach powietrznych?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo — podstawa aktualna i trafnie powołana; zmiany z 2026 r. sprawdzone w tekście i nieistotne dla Spółki; warunkiem jest kwalifikacja wyrobu do wykazu przed bramką G3
- **Dlaczego zmieniono:** **Aktualność.** Ustawa z 2019 r. obowiązuje i pozostaje właściwą podstawą reżimu koncesyjnego. Koncesji udziela, w drodze decyzji, minister właściwy do spraw wewnętrznych (art. 8 ust. 1), na czas oznaczony od 5 do 50 lat (art. 8 ust. 2), po zasięgnięciu opinii m.in. Szefa ABW i Szefa SKW (art. 9 ust. 1). […]
- **Rekomendacja memorandum:** Utrzymać obie klauzule. Doprecyzować § 4 ust. 8 tak, aby obejmował oprogramowanie i technologię (w tym licencjonowanie) oraz odsyłał do przepisów „w brzmieniu obowiązującym”; w § 3 ust. 4 zastąpić „certyfikacji lotniczej” zwrotem „oceny zgodności, certyfikacji i zezwoleń operacyjnych”. Przed bramką G3 z `regulations.md`: zakwalifikować konkretny wyrób do wykazu WT (kryterium „specjalnie zaprojektowany lub zmodyfikowany”), wyznaczyć dwóch dyrektorów (albo dyrektora i prokurenta) spełniających art. 10 ust. 1 pkt 1 (szkolenie z art. 11, badania z art. 12) oraz zaplanować pozyskanie zaświadczeń o niekaralności od akcjonariuszy z pakietem co najmniej 20%. Sygnał dla pakietu A1: rozważyć w § 11 ust. 15 obowiązek akcjonariusza dostarczenia dokumentów wymaganych w postępowaniu koncesyjnym.
- **Podstawa prawna:** ustawa z 13 czerwca 2019 r. (Dz.U. 2019 poz. 1214; t.j. Dz.U. 2023 poz. 1743), zmieniona art. 2 ustawy z 13 marca 2026 r. (Dz.U. 2026 poz. 471) [Z]; art. 3 ust. 1 pkt 12–13 (definicje technologii i wyrobów o przeznaczeniu wojskowym lub policyjnym), art. 4, art. 5, art. 7 ust. 1, art. 8 ust. 1–2, art. 9 ust. 1, art. 10 ust. 1 pkt 2–3, art. 11–12, art. 17 i art. 133 tej ustawy [Z]; brak w niej ustawowej definicji „wytwarzania” i „obrotu” [Z]; rozporządzenie Rady Ministrów z 17 września 2019 r. w sprawie klasyfikacji rodzajów materiałów wybuchowych, broni, amunicji oraz wyrobów i technologii o przeznaczeniu wojskowym lub policyjnym, na których wytwarzanie lub obrót jest wymagane uzyskanie koncesji (Dz.U. 2019 poz. 1888): część IV, kategoria WT V ust. 3, WT XI ust. 2, WT XIII ust. 3–4 oraz definicje pkt 12–15 załącznika [Z]; wykaz zawiera kategorie WT I–XIV, nie ma kategorii WT XXI/XXII [Z]; rozporządzenie (UE) 2018/1139, art. 2 ust. 3 lit. a [W]; rozporządzenie delegowane (UE) 2019/945 [W]; rozporządzenie wykonawcze (UE) 2019/947 (tekst pierwotny): art. 2 pkt 1 i 17, art. 3–6, art. 12, art. 14 ust. 5–6, art. 23 ust. 1–2, załącznik część A pkt UAS.OPEN.060 ust. 2 lit. d i część B pkt UAS.SPEC.050 ust. 1 lit. b [Z] (tekst EN); przesunięcie daty stosowania na 31 grudnia 2020 r. rozporządzeniem wykonawczym (UE) 2020/746 [W]; ustawa Prawo lotnicze (t.j. Dz.U. 2025 poz. 1431): art. 1 ust. 3–4, art. 2 pkt 1a, 1b, 2 i 24–26, dział VIa (art. 156a i n.), art. 156b ust. 3 [Z]; rozporządzenie (UE) 2021/821: art. 2 pkt 1 (produkty podwójnego zastosowania obejmują oprogramowanie i technologię) [Z] (tekst EN); ustawa z 29 listopada 2000 r. o obrocie z zagranicą towarami, technologiami i usługami o znaczeniu strategicznym: art. 3 pkt 10, art. 6, art. 33 ust. 1 [Z].

### § 5. Akcje i kapitał akcyjny

#### § 5 ust. 2, § 9 ust. 4 i 6: usunięcie zbędnego określenia akcji imiennych

Commit `6eb54df` · memorandum 4.3.3 · klasa: zalecane

- **Pytanie:** Czy nowelizacja KSH z 23 stycznia 2026 r. (wejście w życie 18 lutego 2027 r.) wpływa na którekolwiek z postanowień projektu i czy warto już dziś przygotować umowę pod nowe przepisy?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo — tekst ustawy sprawdzony w całości; żadne postanowienie projektu nie jest z nią sprzeczne, ale nowelizacja nakłada na Spółkę nowe obowiązki proceduralne i obowiązek dostosowania umowy w 2 lata
- **Dlaczego zmieniono:** **Co zmienia ustawa w odniesieniu do P.S.A. i rejestru akcjonariuszy** (pełny wykaz na podstawie tekstu): (1) art. 300³² § 1¹–1³: „zarząd zgłasza zawarcie umowy [o prowadzenie rejestru] do sądu rejestrowego”; zgłoszenie zawiera dla domu maklerskiego firmę, numer w rejestrze i NIP, a dla notariusza imię i nazwisko oraz siedzibę i adres kancelarii (także zastępcy notariusza); dołącza się oświadczenie zarządu potwierdzające zawarcie umowy; § 3: podmiot prowadzący rejestr zawiadamia sąd przez system teleinformatyczny o wygaśnięciu albo rozwiązaniu umowy w 7 dni. (2) art. 300³³ § 1 pkt 5 i 6: rozszerzenie danych akcjonariusza i nabywcy o numer PESEL albo datę urodzenia, numer i nazwę rejestru osoby niebędącej osobą fizyczną oraz dane o współwłasności akcji; § 3: „wszelkie zmiany danych, o których mowa w § 1 pkt 1–4 oraz 9–11, zarząd zgłasza podmiotowi prowadzącemu rejestr akcjonariuszy w terminie siedmiu dni od dnia wystąpienia zdarzenia” — obejmuje dane spółki, akcje, wzmiankę o pokryciu oraz *ograniczenia rozporządzania i obowiązki związane z akcją*; sankcja: grzywna do 20 000 zł dla członka zarządu (art. 594 § 1 pkt 2¹). (3) art. 300³⁴: w § 1 „siedmiu dni” zastąpiono „tygodniem”; § 3 zdanie drugie określa formę zgody na wpis (pisemna z podpisem notarialnie poświadczonym, pisemna w obecności osoby upoważnionej przez podmiot albo elektroniczna z podpisem kwalifikowanym, zaufanym lub osobistym); § 9 dopuszcza automatyczne powiadomienia elektroniczne. […]
- **Rekomendacja memorandum:** Dodać klauzulę dostosowawczą do § 38 i termin 7 dni do § 24 ust. 3. W umowie wykonawczej (pakiet 1.5) przewidzieć składanie przez Założycieli zgód na wpis w formie z art. 300³⁴ § 3 zdanie drugie. Zawiązać Spółkę bez oczekiwania na 2027 r.; w kalendarzu Rady zapisać: zgłoszenie podmiotu prowadzącego rejestr do KRS do 18 maja 2027 r., przegląd umowy pod kątem art. 34 do 18 lutego 2029 r.
- **Podstawa prawna:** ustawa z 23 stycznia 2026 r. o zmianie ustawy — Kodeks spółek handlowych oraz niektórych innych ustaw (Dz.U. 2026 poz. 176, ogłoszona 17 lutego 2026 r.) [Z]; art. 35 (wejście w życie po upływie 12 miesięcy od ogłoszenia, tj. 18 lutego 2027 r., z wyjątkiem art. 28 i 33 — 28 lutego 2026 r.) [Z]; art. 1 pkt 2–6 i 30 (art. 300³², 300³³, 300³⁴, 300³⁵, 300³⁷ § 2 i art. 594 § 1 KSH) [Z]; art. 1 pkt 16–27 (zmiany dotyczące wyłącznie spółki akcyjnej, m.in. uchylenie art. 334 i zmiany art. 337, 351, 352, 356, 361, 406¹, 432, 434, 453, 476) [Z]; art. 2 (art. 90a § 1 Prawa o notariacie) [Z]; art. 5 (art. 10 ust. 4a pkt 4, art. 25da i art. 38 pkt 8a lit. j ustawy o KRS) [Z]; art. 16 pkt 3 (art. 83a ust. 4ac ustawy o obrocie instrumentami finansowymi) [Z]; art. 28–34 (przepisy przejściowe) [Z]; art. 300²⁹ § 1 KSH („akcje nie mają formy dokumentu”) [Z]; art. 55 ust. 1 ustawy o kosztach sądowych w sprawach cywilnych [Z]; art. 111 § 2 i art. 112 KC (obliczanie terminów) [Z].

#### § 5 ust. 6: przywrócenie ustępu o rejestrze akcjonariuszy w brzmieniu merytorycznym (wybór podmiotu, zgłaszanie ograniczeń i obowiązków)

Commit `d0b769a` · memorandum 4.3.2 · klasa: opcjonalne — warunek spełnia się w umowie z podmiotem prowadzącym rejestr

- **Pytanie:** Które ograniczenia i obowiązki powinny zostać ujawnione w rejestrze akcjonariuszy i jak dobrać podmiot prowadzący rejestr pod kątem obsługi tych ograniczeń?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** **Co ujawniać.** Rejestr jest jedynym miejscem, w którym ograniczenia i obowiązki stają się widoczne dla nabywcy i dla podmiotu dokonującego wpisu, a wpis nabywcy jest konstytutywny dla nabycia akcji (art. 300³⁷ § 1); dlatego ujawnienie ma znaczenie praktyczne większe niż ujawnienie w KRS. Do wpisu jako *ograniczenia co do rozporządzania akcją* (pkt 10): zgoda Spółki (§ 12 ust. 1–3), Okres Ograniczenia Zbywania (§ 13), prawo pierwszeństwa (§ 14), prawo przyłączenia i przymusowego współzbycia (§ 15, § 16), Kryterium i weryfikacja nabywcy (§ 11 ust. 4–6, 13), ograniczenia dziedziczenia (§ 17). Jako *postanowienia umowy o związanych z akcją obowiązkach wobec spółki* (pkt 11): obowiązek zbycia z mechanizmu zwrotnego zbycia (§ 10 ust. 14, z oznaczeniem akcji objętych mechanizmem według Załącznika nr 2), obowiązek zbycia po utracie Kryterium (§ 11 ust. 15), obowiązki informacyjne (§ 18 ust. 1, § 11 ust. 15 zdanie pierwsze), poufność (§ 27) oraz — po zmianie z 4.2.1 — obowiązek z § 28 ust. 5. […]
- **Rekomendacja memorandum:** Sporządzić wykaz ograniczeń i obowiązków do ujawnienia (według listy powyżej) jako załącznik do umowy z podmiotem prowadzącym rejestr; wybrać podmiot po zapytaniu ofertowym z kryteriami (1)–(8); wybór ująć w uchwale założycielskiej objętej aktem (4.3.1). Opcjonalnie przywrócić § 5 ust. 6 w brzmieniu merytorycznym.
- **Podstawa prawna:** art. 300³⁰ § 1–2 KSH (obowiązek rejestracji akcji; wpis po wpisie spółki) [Z]; art. 300³¹ § 1–5 KSH (podmiot uprawniony do prowadzenia rachunków papierów wartościowych albo notariusz; postać elektroniczna, dopuszczalna baza rozproszona; wybór uchwałą akcjonariuszy, „przy zawiązaniu spółki wyboru dokonują akcjonariusze”) [Z]; art. 4 ust. 1 pkt 1 ustawy z 29 lipca 2005 r. o obrocie instrumentami finansowymi (domy maklerskie, banki prowadzące działalność maklerską, banki powiernicze, zagraniczne firmy inwestycyjne działające przez oddział, KDPW, NBP) [Z]; art. 300³² § 1–2 KSH (niezwłoczne zawarcie umowy; rozwiązanie przez spółkę tylko pod warunkiem zawarcia nowej; wypowiedzenie przez podmiot z ważnych powodów, nie krócej niż 3 miesiące) [Z]; art. 300³³ § 1 pkt 10–11 i § 2 KSH („umowa spółki może zawierać dodatkowe postanowienia dotyczące informacji ujawnianych w rejestrze akcjonariuszy”) [Z]; art. 300³⁴ § 1 i 3 KSH (wpis na żądanie spółki lub osoby mającej interes prawny w 7 dni; powiadomienie osoby, której prawa mają być wykreślone, zmienione lub obciążone) [Z]; art. 300³⁵ § 1–3 KSH (jawność dla spółki i akcjonariuszy) [Z]; art. 300³⁶ § 4 (forma dokumentowa zbycia), art. 300³⁷ § 1 (konstytutywny skutek wpisu) i art. 300³⁸ § 1 KSH [Z]; art. 300⁸⁷ § 1 KSH (zwołanie walnego zgromadzenia pocztą elektroniczną na adres wpisany do rejestru) [Z]; ustawa z 23 stycznia 2026 r. (Dz.U. 2026 poz. 176): od 18 lutego 2027 r. art. 300³² § 1¹–1³ i § 3, art. 300³³ § 3, art. 300³⁴ § 3 zdanie drugie i § 9, art. 300³⁵ § 1¹ KSH, art. 38 pkt 8a lit. j ustawy o KRS, art. 83a ust. 4ac ustawy o obrocie instrumentami finansowymi, art. 90a § 1 Prawa o notariacie [Z].

### § 7. Wkłady Założycieli

#### § 7 ust. 3: wskazanie podstawy wyceny wkładów niepieniężnych i oświadczenie Założycieli o ich wartości

Commit `2ba6155` · memorandum 3.1.1 · klasa: zalecane

- **Pytanie:** Jakie dokumenty i wyceny wkładów niepieniężnych są potrzebne do zawiązania i wpisu (art. 300² KSH), kto ponosi odpowiedzialność za zawyżenie wartości wkładu przeznaczonego na kapitał akcyjny i jak ją ograniczyć, skoro na kapitał idą tylko wkłady pieniężne?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** W P.S.A. nie ma sprawozdania założycieli ani badania wkładów przez biegłego rewidenta, jakie zna spółka akcyjna; wycena wkładów niepieniężnych jest własną odpowiedzialnością Założycieli i dyrektorów [W]. Umowa (akt notarialny) musi zawierać przedmiot każdego wkładu niepieniężnego, serie i numery akcji obejmowanych za ten wkład oraz osobę obejmującą (art. 300⁵ § 1 pkt 4); wartość nie jest ustawowym elementem umowy, ale jest potrzebna do oświadczenia Rady Dyrektorów składanego przy wpisie „o wysokości kapitału akcyjnego, ustalonej na podstawie sumy wartości wniesionych wkładów, przeznaczonych na kapitał akcyjny” (art. 300¹² § 3 pkt 2 [Z]), do rozliczenia podatkowego Założyciela (art. 17 ust. 1 pkt 9 PIT [Z]) i do § 7 ust. 3, który wprost odsyła do wartości „określonej w Załączniku nr 1” — Załącznik nr 1 nie ma jednak kolumny wartości (zob. 3.1.4). Do zgłoszenia dołącza się (art. 300¹² § 3–4 [Z]): umowę spółki z Załącznikiem nr 1, oświadczenie wszystkich dyrektorów o wysokości kapitału akcyjnego, oświadczenie wszystkich dyrektorów, „że wkłady na pokrycie akcji zostały wniesione w części przewidzianej w umowie spółki”, oraz listę akcjonariuszy z liczbą i serią akcji objętych przez każdego z nich; samo zgłoszenie zaznacza okoliczność wnoszenia wkładów niepieniężnych (§ 2 pkt 7). […]
- **Rekomendacja memorandum:** Dla każdego składnika przygotować przed dniem podpisania umowy: (a) kod, modele, dokumentacja — umowa przeniesienia autorskich praw majątkowych w formie pisemnej (3.1.3), wykaz repozytoriów z identyfikatorem wersji (commit, tag), sumy kontrolne, protokół wydania, wykaz twórców z podstawą nabycia praw od każdego z nich, wykaz komponentów otwartych z licencjami; (b) sprzęt — protokół wydania z numerami seryjnymi, dowody nabycia, oświadczenie o braku obciążeń i zastrzeżeń własności; (c) zgłoszenia patentowe i prawa do uzyskania patentu — cesja pisemna, wnioski o zmianę zgłaszającego do UPRP/EPO, wykaz twórców i oświadczenia o prawie do wynalazku; (d) wycena — raport rzeczoznawcy albo co najmniej notatka metodyczna (metoda kosztowa lub dochodowa, założenia, data), podpisana przez wszystkich Założycieli; (e) oświadczenia z § 26 ust. 5 w formie odrębnego dokumentu. W § 7 ust. 3 dodać wskazanie podstawy wyceny.
- **Podstawa prawna:** art. 300² § 1–2, art. 300³ § 1–2, art. 300⁵ § 1 pkt 3–5 i § 2 KSH [Z]; art. 300⁴ pkt 3, art. 300⁹ § 1–3, art. 300¹⁰ § 1–2, art. 300¹² § 2 pkt 6–7, § 3 pkt 2–3 i § 4, art. 300¹²³, art. 300¹²⁴, art. 587 § 1 KSH [Z]; art. 14 § 1–2 KSH [Z]; art. 300¹¹ § 1–2 KSH (spółka w organizacji) [Z]; art. 300⁷³ § 1 KSH (Rada Dyrektorów wykonuje kompetencje zarządu) [Z]; art. 17 ust. 1 pkt 9, art. 19 ust. 1 i 4, art. 22 ust. 1e pkt 3 ustawy o PIT [Z].

#### § 7 ust. 4: przeznaczenie na kapitał akcyjny także wkładów niepieniężnych, stwierdzenie wniesienia uchwałą Rady

Commit `9a6a433` · memorandum 3.1.2, K12 · klasa: konieczne

- **Pytanie:** Czy przeznaczenie na kapitał akcyjny wyłącznie wkładów pieniężnych (a wkładów niepieniężnych poza kapitał) jest dopuszczalne i jakie ma skutki podatkowe i bilansowe?
- **Ocena brzmienia 0.9.4-C:** ryzyko
- **Dlaczego zmieniono:** Art. 300³ § 1 KSH brzmi: „W spółce tworzy się wyrażony w złotych kapitał akcyjny, na który przeznacza się wniesione wkłady pieniężne oraz niepieniężne, z uwzględnieniem art. 14 § 1. Kapitał akcyjny powinien wynosić co najmniej 1 złoty” [Z]; art. 14 § 1 wyłącza z kapitału akcyjnego tylko prawa niezbywalne oraz świadczenie pracy bądź usług [Z]. Przepis jest sformułowany kategorycznie („przeznacza się”) i — według przeważającego, naszym zdaniem, odczytania — nie pozostawia Założycielom wyboru, które z wkładów zdatnych do zaliczenia trafią do kapitału; swoboda dotyczy wysokości wartości, nie jej alokacji [W]. […]
- **Rekomendacja memorandum:** Przeznaczyć na kapitał akcyjny wszystkie wkłady z § 7 ust. 1 lit. a–d w wartościach z Załącznika nr 1; kapitał na dzień wpisu obejmuje wkłady wniesione przed zgłoszeniem, a wkłady wnoszone w 14 dni po wpisie zwiększają kapitał na podstawie uchwały Rady bez zmiany umowy. Jeżeli Założyciele chcą utrzymać niski kapitał, drogą jest ostrożna (ale obronna podatkowo) wycena wkładów, nie ich wyłączenie z kapitału. Decyzję poprzedzić potwierdzeniem przez kancelarię wykładni art. 300³ § 1 KSH.
- **Podstawa prawna:** art. 300³ § 1–2 w zw. z art. 14 § 1 KSH [Z]; art. 300² § 2, art. 300¹⁰ § 1, art. 300¹² § 3 pkt 2, art. 300¹⁵ § 1–6, art. 300¹⁹ KSH [Z]; art. 17 ust. 1 pkt 9, art. 19 ust. 1 i 3–4, art. 21 ust. 1 pkt 109, art. 22 ust. 1e i 1f ustawy o PIT [Z]; art. 12 ust. 1 pkt 2 ustawy o CIT [W]; art. 1 ust. 1 pkt 1 lit. k i ust. 3 pkt 2, art. 1a pkt 2, art. 6 ust. 1 pkt 8 i art. 7 ust. 1 pkt 9 ustawy o PCC [Z]; art. 36 ust. 1 i 2aa ustawy o rachunkowości [Z].

### § 8. Program motywacyjny — pula 15% po pełnym rozwodnieniu

#### § 8 ust. 3 i 5: emisja serii P w trybie warunkowej emisji akcji (tryb podstawowy) albo zwykłym; wyłączenie prawa poboru serii P w umowie

Commit `e6b6941` · memorandum 3.2.1, K14 · klasa: konieczne

- **Pytanie:** Czy „uchwała ramowa” na wiele transz emisji serii P, wykonywana przez Radę, oraz jedna uchwała 4/5 o pozbawieniu prawa poboru dla wszystkich transz są dopuszczalne na tle art. 300¹⁰³–300¹⁰⁷ KSH, czy każda transza wymaga własnej uchwały o prawie poboru?
- **Ocena brzmienia 0.9.4-C:** ryzyko (konstrukcja hybrydowa nieznana ustawie; ustawa daje dwa gotowe instrumenty, z których umowa nie korzysta)
- **Dlaczego zmieniono:** Konstrukcję trzeba rozłożyć na trzy warstwy. *Pierwsza — podstawa w umowie.* Art. 300¹⁰³ KSH stanowi, że emisja akcji jest zmianą umowy spółki, ale „zachowanie przepisów o zmianie umowy spółki nie jest wymagane, jeżeli emisja akcji następuje uchwałą akcjonariuszy podejmowaną na podstawie dotychczasowych postanowień umowy spółki przewidujących maksymalną liczbę akcji i termin ich emisji” [Z]; § 8 ust. 1 i 3 spełniają ten wymóg (zob. 3.2.2). *Druga — uchwała o emisji.* Wbrew założeniu, na którym oparto § 8 ust. 3, P.S.A. zna delegację kompetencji emisyjnej: (a) *upoważnienie Rady Dyrektorów do emisji* (art. 300¹¹⁰–300¹¹³, stosowane do rady dyrektorów jak do zarządu) — umowa spółki może upoważnić organ zarządzający na okres nie dłuższy niż pięć lat, odnawialny zmianą umowy, do jednej albo kilku emisji łącznie nie większych niż jedna czwarta liczby akcji istniejących w dniu udzielenia upoważnienia, za wkłady pieniężne (chyba że upoważnienie dopuszcza niepieniężne), bez akcji uprzywilejowanych i uprawnień indywidualnych; uchwała o zmianie umowy w tym przedmiocie musi być umotywowana (art. 300¹¹¹), uchwała Rady zastępuje uchwałę Walnego Zgromadzenia o emisji (art. 300¹¹²), a pozbawienie prawa poboru wymaga przy każdej emisji uchwały akcjonariuszy 4/5 albo upoważnienia Rady zapisanego w umowie spółki i uchwalonego większością 4/5 (art. 300¹¹³) [Z]; (b) *warunkowa emisja akcji* (art. 300¹¹⁴–300¹¹⁸) — ustawowy instrument programów motywacyjnych: Walne Zgromadzenie uchwala emisję z zastrzeżeniem, że akcje obejmą osoby, „które uzyskały te prawa na podstawie umowy zawartej ze spółką” (art. 300¹¹⁴ § 2 pkt 2), przy czym zawarcie takiej umowy wymaga zgody Walnego Zgromadzenia 3/4 (§ 3), liczba akcji nie może przekroczyć dwukrotności akcji istniejących (§ 4); uchwała określa maksymalną liczbę akcji, cenę emisyjną, cel, termin wykonania prawa i krąg uprawnionych (art. 300¹¹⁵ § 1), sama „skutkuje wyłączeniem prawa poboru” i musi spełniać warunki art. 300¹⁰⁶ § 2, czyli większość 4/5 (art. 300¹¹⁵ § 2); po wpisie tej zmiany umowy do rejestru (art. 300¹¹⁶) uprawnieni obejmują akcje pisemnym oświadczeniem, Rada wydaje dyspozycję wpisu do rejestru akcjonariuszy i z tym wpisem następuje nabycie praw z akcji (art. 300¹¹⁷–300¹¹⁸ § 1), a do sądu rejestrowego trafia tylko roczny wykaz objętych akcji (art. 300¹¹⁸ § 2–3) [Z]; nowelizacja poz. 176 potwierdza ten model, wyłączając od 18 lutego 2027 r. akcje z art. 300¹¹⁸ spod ogólnej zasady, że objęcie akcji nie wymaga wpisu w rejestrze akcjonariuszy do nabycia praw (nowe brzmienie art. 300³⁷ § 2) [Z]. Uchwała ramowa z § 8 ust. 3 nie jest żadnym z tych instrumentów: jest zwykłą emisją z oddziału 1, w której Walne Zgromadzenie chce rozłożyć skutek na transze wykonywane przez Radę. […]
- **Rekomendacja memorandum:** Przebudować § 8 ust. 3 i 5: (1) przewidzieć jako tryb podstawowy warunkową emisję akcji serii P (jedna uchwała 4/5 na całą pulę albo jej część, zgoda na zawieranie umów uczestnictwa udzielona w tej samej uchwale dla kategorii osób i warunków z regulaminu, objęcie po nabyciu uprawnień pisemnym oświadczeniem, prawa z akcji z chwilą wpisu do rejestru akcjonariuszy); (2) zachować tryb zwykły z uchwałą obejmującą kilka transz jako alternatywę, z pełnym katalogiem art. 300¹⁰⁴ i upoważnieniami dla Rady; (3) wyłączyć w umowie prawo poboru akcji serii P na podstawie art. 300¹⁰⁶ § 1, co czyni ust. 5 zbędnym; (4) potwierdzić z kancelarią, czy termin z art. 300¹⁰² § 2 dotyczy emisji z art. 300¹⁰³, i do czasu potwierdzenia zgłaszać każdą emisję zwykłą w sześć miesięcy od uchwały. Upoważnienie Rady z art. 300¹¹⁰ (limit jednej czwartej akcji, pięć lat) rozważyć jako narzędzie dla drobnych emisji, nie dla puli P. Wybór trybu podstawowego jest decyzją Założycieli; rekomendujemy warunkową emisję.
- **Podstawa prawna:** art. 300¹⁰³, art. 300¹⁰⁴ § 1 pkt 1–7 i § 2, art. 300¹⁰⁵ § 1–3, art. 300¹⁰⁶ § 1–2 i 6, art. 300¹⁰⁷ § 1–3 KSH [Z]; art. 300¹⁰⁸–300¹¹³ KSH (upoważnienie zarządu albo rady dyrektorów do emisji akcji) [Z]; art. 300¹¹⁴–300¹¹⁸ KSH (warunkowa emisja akcji), art. 300¹¹⁹ KSH (warranty subskrypcyjne), art. 300⁸¹ pkt 4 KSH [Z]; art. 300¹⁰² § 2 KSH (termin sześciu miesięcy na zgłoszenie zmiany umowy) [Z]; art. 300³⁷ § 2 KSH w brzmieniu od 18 lutego 2027 r. (Dz.U. 2026 poz. 176, art. 1 pkt 6) [Z]; art. 444 § 1 KSH (porównawczo) [Z]; art. 300¹ § 3 KSH [Z].

### § 9. Założyciele Funkcjonalni Serii F — późniejsi współzałożyciele

#### § 9 ust. 3: uchwała kwalifikacyjna nie jest przyrzeczeniem oferty, roszczenie o akcje serii F wyłącznie z umowy objęcia

Commit `e9349ee` · memorandum 3.2.3 · klasa: opcjonalne

- **Pytanie:** Czy uchwała kwalifikacyjna serii F (bez oferty i bezwarunkowego prawa do akcji, § 9 ust. 3) nie rodzi po stronie kandydata roszczeń i czy status Założyciela Funkcjonalnego Serii F może być odebrany?
- **Ocena brzmienia 0.9.4-C:** zgodne
- **Dlaczego zmieniono:** Uchwała kwalifikacyjna jest aktem wewnętrznym Spółki adresowanym do organów, nie oświadczeniem woli wobec kandydata; § 9 ust. 3 wprost odmawia jej charakteru oferty i bezwarunkowego prawa do akcji, a § 8 ust. 7 (odpowiednio) i art. 300¹⁰⁷ § 3 KSH przesądzają, że akcje powstają z wpisem do rejestru (przy warunkowej emisji — prawa z akcji z wpisem do rejestru akcjonariuszy, art. 300¹¹⁸ § 1 [Z]). Nie jest ofertą, bo nie określa istotnych postanowień umowy objęcia (art. 66 § 1 KC), ani umową przedwstępną — kandydat nie jest jej stroną, a umowa spółki nie zawiera istotnych postanowień umowy przyrzeczonej (art. 389 § 1 KC [Z]). Roszczenia kandydata mogą więc powstać tylko poza uchwałą: (1) z umowy o pracę, umowy B2B albo „term-sheetu założycielskiego” (`emisja/founder.md`, krok 0), jeżeli zawierają przyrzeczenie akcji; […]
- **Rekomendacja memorandum:** Wymóg jasnego komunikatu przenieść do dokumentów z kandydatem: umowa o pracę albo B2B i term-sheet założycielski powinny stwierdzać, że do zawarcia umowy objęcia kandydatowi nie przysługuje roszczenie o akcje ani o złożenie oferty, że status może zostać cofnięty na warunkach § 9 ust. 3 oraz że wynagrodzenie jest niezależne od akcji. W umowie spółki dodać zdanie o braku roszczenia o złożenie oferty.
- **Podstawa prawna:** art. 66 § 1, art. 72 § 2, art. 389 § 1, art. 353¹ KC [Z]; art. 300¹⁰⁵ § 1–3, art. 300¹⁰⁷ § 3, art. 300¹¹⁸ § 1 KSH [Z]; art. 300¹⁰¹ KSH w zw. z art. 422 § 2 KSH (legitymacja do zaskarżenia uchwały) [Z].

#### § 9 ust. 4, § 8 ust. 9: termin 31.12.2036 odniesiony do dnia uchwały o emisji; zwiększenie puli serii P tylko zmianą umowy

Commit `9bfd334` · memorandum 3.2.2 · klasa: opcjonalne

- **Pytanie:** Czy określenie w umowie maksymalnej liczby akcji i terminu (2036 r.) dla serii P i F spełnia wymogi art. 300¹⁰³ KSH dotyczące upoważnienia do emisji?
- **Ocena brzmienia 0.9.4-C:** zgodne
- **Dlaczego zmieniono:** Art. 300¹⁰³ KSH wymaga, aby dotychczasowe postanowienia umowy spółki przewidywały „maksymalną liczbę akcji i termin ich emisji” [Z]; obie serie to spełniają: seria P — 176 471 akcji do 31 grudnia 2036 r. (§ 8 ust. 1 i 3), seria F — 250 000 akcji do 31 grudnia 2036 r. z dodatkowym ograniczeniem 20% (§ 9 ust. 4). Dodatkowy limit procentowy zawęża upoważnienie, a nie rozszerza, więc jest dopuszczalny. […]
- **Rekomendacja memorandum:** Odnieść termin do dnia uchwały o emisji w obu paragrafach i uprościć ust. 9. Rozważyć (decyzja Założycieli) skrócenie horyzontu serii F albo zastrzeżenie, że po Kwalifikowanej Rundzie emisje serii F wymagają zgody przewidzianej w dokumentach rundy.
- **Podstawa prawna:** art. 300¹⁰³ KSH [Z]; art. 300⁵ § 1 pkt 3, art. 300¹⁰⁰ § 2, art. 300¹⁰² § 1–2, art. 300¹⁰⁷ § 3 KSH [Z]; art. 300¹¹⁰ § 1–3 KSH (pięcioletnie upoważnienie Rady, porównawczo) [Z]; art. 444 § 1 KSH (porównawczo) [Z].

#### § 9 ust. 7, § 18 ust. 1, § 22 ust. 3, § 24 ust. 1, § 29 ust. 12, § 39 ust. 1: usunięcie przekreślonych zdań i ustępów, odesłania w § 24 (ust. 5, ust. 10) i w umowie wykonawczej (§ 39 ust. 3-4, § 24 ust. 2)

Commit `d7d6f77` · memorandum 3.4.4, decyzja D4 · klasa: zalecane

- **Pytanie:** Przekreślone zdania i ustęp: czy ich usunięcie jest bezpieczne, czy któreś powinny zostać; spójność definicji po usunięciu.
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Dziewięć fragmentów. (1) § 5 ust. 6 (rejestr akcjonariuszy) — powtórzenie ustawy: „wybór podmiotu prowadzącego rejestr akcjonariuszy wymaga uchwały akcjonariuszy. Przy zawiązaniu spółki wyboru dokonują akcjonariusze” (art. 300³¹ § 5 [Z]); usunięcie bezpieczne. […]
- **Rekomendacja memorandum:** Usunąć osiem fragmentów deklaratywnych i odesłanie; o ust. 14 zdecydować łącznie z pakietem 1.4 (rekomendacja: przywrócić uszczelniony). Po usunięciu poprawić odesłania w § 24 ust. 2 i 12 oraz w umowie akcjonariuszy; przed podpisaniem zweryfikować mechanicznie wszystkie odesłania „ust. N” do paragrafów, w których usunięto ustęp.
- **Podstawa prawna:** art. 2 KSH [Z]; art. 300³⁰ § 1–2, art. 300³¹ § 5 KSH (rejestr akcjonariuszy, wybór podmiotu przez akcjonariuszy) [Z]; art. 300⁷⁹ § 1 KSH [Z]; art. 300¹⁰⁴ § 1 KSH [Z]; art. 300³⁸ § 1 KSH [Z]; § 11 ust. 14, § 32 ust. 1.

### § 10. Akcjonariusze Funkcjonalni i mechanizm zwrotnego zbycia akcji

#### § 10 ust. 6a: przesłanka przestępstwa, 24-miesięczny limit przekwalifikowania Odejścia, dopłata po ustaleniu innego rodzaju Odejścia

Commit `9ef37ea` · memorandum 1.5.4 · klasa: zalecane

- **Pytanie:** Czy katalog Odejścia Zawinionego (§ 10 ust. 5) i tryb jego stwierdzania nie rodzą ryzyka sporu o kwalifikację zdarzenia, i kto powinien je stwierdzać?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Katalog jest zamknięty („wyłącznie”) i w większości opisuje zdarzenia obiektywne (lit. b, d, e), co ogranicza spór; nieostre pozostają „rażące niedbalstwo” (lit. a) i „działanie na szkodę Spółki” (lit. b), które są klasycznymi polami sporu. Trzy elementy podnoszą ryzyko: (1) „popełnienie przestępstwa” bez wskazania, czy wymagane jest prawomocne skazanie — Rada, stwierdzając przestępstwo na własną rękę, wystawia Spółkę na zarzut arbitralności (każdego „uważa się za niewinnego, dopóki jego wina nie zostanie stwierdzona prawomocnym wyrokiem sądu”, art. 42 ust. 3 Konstytucji; Kodeks pracy przyjmuje w art. 52 § 1 pkt 2 kompromis: przestępstwo „oczywiste lub stwierdzone prawomocnym wyrokiem”), a czekanie na wyrok trwa lata; […]
- **Rekomendacja memorandum:** Doprecyzować lit. b (przestępstwo: prawomocne skazanie albo — do czasu wyroku — zawieszenie wykonania prawa nabycia akcji zwolnionych, ze zbyciem akcji niezwolnionych po cenie emisyjnej bez zwłoki), ograniczyć przekwalifikowanie do 24 miesięcy od Dnia Odejścia i dodać regułę dopłaty. Stwierdzanie pozostawić Radzie Dyrektorów w trybie umowy wykonawczej.
- **Podstawa prawna:** art. 353¹, art. 58 § 2, art. 5 KC [Z]; art. 42 ust. 3 Konstytucji RP (domniemanie niewinności — pomocniczo) [Z]; art. 52 § 1 pkt 2 KP (pomocniczo) [Z]; art. 300⁵⁵ § 1 i art. 300⁵⁸ § 2 KSH [Z]; art. 1157 pkt 1 KPC [Z]

#### § 10 ust. 6b: kwalifikacja Odejścia niezależna od podstawy zaangażowania, skutek prawomocnego ustalenia bezzasadności rozwiązania; umowa wykonawcza: ograniczenie kar umownych wobec założycieli-pracowników

Commit `0102d0c` · memorandum 1.5.5 · klasa: zalecane

- **Pytanie:** Czy mechanizm jest neutralny wobec podstawy zaangażowania założyciela (umowa o pracę, B2B, powołanie) i czy zwolnienie akcji nie rodzi skutków w prawie pracy?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Mechanizm jest formalnie neutralny: uruchamia go „ustanie funkcjonalnego zaangażowania” (§ 10 ust. 4–6, § [umowa wspólników: odejscie] ust. 1), niezależnie od tego, czy podstawą jest stosunek pracy, umowa B2B czy powołanie do Rady Dyrektorów; akcje nie są wynagrodzeniem za pracę, lecz zostały objęte za wkłady (§ 7), więc ich zwalnianie nie jest przychodem ze stosunku pracy ani składnikiem wynagrodzenia (art. 12 PIT), a późniejsze zbycie jest przychodem z kapitałów pieniężnych (art. 17 PIT) — inaczej może być przy akcjach serii F obejmowanych za wkład w postaci pracy (§ 9 ust. 7), gdzie kwalifikacja podatkowa objęcia wymaga odrębnej opinii [?]. Nieneutralne są punkty styku: (1) przy umowie o pracę definicja lit. b ust. 4 („rozwiązanie przez Spółkę bez istotnej przyczyny”) i katalog ust. 5 nie pokrywają się z art. 52 KP i z pojęciem „uzasadnionego wypowiedzenia” (art. 45 KP); jeżeli sąd pracy przywróci pracownika albo zasądzi odszkodowanie za wadliwe rozwiązanie, kwalifikacja Odejścia staje się sporna — potrzebna jest reguła z 1.5.4 (dopłata) i wyraźne zastrzeżenie, że kwalifikacja Odejścia jest niezależna od trybu rozwiązania stosunku pracy, ale prawomocne ustalenie bezzasadności rozwiązania przez Spółkę oznacza Odejście Usprawiedliwione; (2) kary umowne wobec pracownika za naruszenie obowiązków pracowniczych są w orzecznictwie SN uznawane za niedopuszczalne (wyczerpujący reżim art. 114–122 KP, art. 300 KP) [W] — dyskonto 80% jako cena opcji się broni (1.5.2), ale kary umowne z umowy wykonawczej (§ [umowa wspólników: konkurencja] ust. 5, § [umowa wspólników: poufnosc] ust. 4) wobec założyciela-pracownika trzeba ograniczyć do okresu po ustaniu stosunku pracy albo do naruszeń poza sferą obowiązków pracowniczych; […]
- **Rekomendacja memorandum:** Dodać do § 10 zdanie o niezależności kwalifikacji od podstawy zaangażowania i o skutku prawomocnego ustalenia bezzasadności rozwiązania; w umowie wykonawczej ograniczyć kary umowne wobec pracowników zgodnie z pkt (2). Preferować dla założycieli powołanie plus umowa B2B albo kontrakt menedżerski, co Założyciele powinni rozstrzygnąć świadomie.
- **Podstawa prawna:** art. 18 § 1, art. 22 § 1, art. 30 § 4, art. 45 § 1, art. 52 § 1, art. 56 § 1, art. 87 § 1, art. 91 § 1, art. 101¹–101², art. 114–122, art. 300 KP [Z]; art. 300² § 2 KSH (wkład w postaci pracy lub usług) [Z]; art. 300⁷³ § 3 i art. 300⁷⁴ § 1 KSH (odwołanie dyrektora) [Z]; art. 12 ust. 1 i art. 17 ust. 1 pkt 6 lit. a ustawy o PIT [Z]

#### § 10 ust. 8 lit. b: 80% Wartości Godziwej jako cena umowna opcji, nie kara umowna, z zaliczeniem różnicy na odszkodowanie; umowa wykonawcza: wyłączenie nabywcy finansowanego przez Spółkę

Commit `9790623` · memorandum 1.5.2 · klasa: zalecane

- **Pytanie:** Czy zbycie za 80 % Wartości Godziwej przy Odejściu Zawinionym może zostać zakwestionowane (obejście przepisów o umorzeniu lub o nabyciu akcji własnych, kara umowna, nadmierność) i jakie są granice takiej redukcji ceny?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Zarzut obejścia przepisów o umorzeniu i akcjach własnych jest słaby: akcje nie są unicestwiane, nabywcą nie może być Spółka ani osoba działająca na jej rachunek (§ 10 ust. 11–12, wyraźnie nawiązujące do art. 300⁴⁷ § 9 KSH), a minimum z art. 300⁴⁵ § 2 KSH („spłata, która nie może być niższa od wartości godziwej akcji”) dotyczy wyłącznie umorzenia przymusowego, które jest zresztą dopuszczalne tylko wtedy, gdy „umowa spółki tak stanowi i określa przesłanki umorzenia przymusowego” (art. 300⁴⁵ § 1 KSH). Zarzut byłby realny tylko wtedy, gdyby Rada Dyrektorów wskazywała jako nabywcę podmiot finansowany przez Spółkę albo działający na jej zlecenie (np. spółkę zależną, fundację założycielską finansowaną przez Spółkę); tego umowa wykonawcza nie wyklucza dostatecznie wprost (§ [umowa wspólników: nabywca] ust. 1 wymienia „inwestora”), warto to dopisać. Kwalifikacja jako kara umowna również nie jest trafna: 80% Wartości Godziwej to cena w opcji kupna, a nie zastrzeżenie, że „naprawienie szkody wynikłej z niewykonania lub nienależytego wykonania zobowiązania niepieniężnego nastąpi przez zapłatę określonej sumy” (art. 483 § 1 KC); cena została oznaczona przez wskazanie podstaw jej ustalenia (art. 536 § 1 KC). […]
- **Rekomendacja memorandum:** Utrzymać 80%; w § 10 ust. 8 lit. b dodać zdanie, że cena jest ceną umowną opcji i nie stanowi kary umownej, a Spółka zalicza na ewentualne roszczenia odszkodowawcze różnicę między Wartością Godziwą a ceną zapłaconą; w umowie wykonawczej wykluczyć jako Nabywcę Wskazanego podmiot zależny od Spółki lub przez nią finansowany.
- **Podstawa prawna:** art. 300⁴⁵ § 1–2 KSH [Z]; art. 300⁴⁷ § 9 KSH [Z]; art. 353¹, art. 58 § 2–3, art. 483–484 KC [Z]; art. 536 § 1 KC [Z]; art. 19 ust. 1 w zw. z art. 17 ust. 2 oraz art. 11 ust. 2b ustawy o PIT [Z]

#### § 10 ust. 10: definicje Zmiany Kontroli i Istotnej Przyczyny, okno od umowy do 12 miesięcy po zamknięciu, konstruktywne odejście

Commit `9c212c7` · memorandum 1.5.6 · klasa: zalecane

- **Pytanie:** Przyspieszenie po zmianie kontroli (§ 10 ust. 10) — czy definicja „istotnej przyczyny” i 12-miesięczne okno są wystarczająco określone?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Ust. 10 nie definiuje ani „zmiany kontroli”, ani „istotnej przyczyny”; pierwsze pojęcie definiuje dopiero umowa wykonawcza (§ [umowa wspólników: smierc] ust. 3: ponad 50% głosów albo prawo powoływania większości dyrektorów), co jest odwróceniem hierarchii — przesłanka skutku korporacyjnego z umowy spółki nie powinna zależeć od umowy, której inwestor nie jest stroną (§ [umowa wspólników: strony] ust. 4). „Istotna przyczyna” pojawia się w ust. 4 lit. b i w ust. 10 bez definicji, mimo że umowa ma gotowy katalog zawinionych przyczyn w ust. 5; wykładnia z art. 65 KC prowadzi zapewne do utożsamienia „istotnej przyczyny” z ust. 5, ale nabywca kontroli będzie argumentował szerzej (np. „utrata zaufania”, „reorganizacja”). Dwunastomiesięczne okno jest standardem rynkowym i jest określone wystarczająco; brakuje natomiast (a) objęcia oknem rozwiązania współpracy w okresie od ogłoszenia transakcji do jej zamknięcia (typowa luka, w której nabywca „czyści” zespół przed closingiem), (b) przypadku konstruktywnego odejścia po zmianie kontroli (istotne pogorszenie roli lub wynagrodzenia — ust. 4 lit. c pokrywa to tylko częściowo), (c) wskazania, że zmiana kontroli obejmuje także zbycie całości lub zasadniczej części przedsiębiorstwa albo Kluczowej Własności Intelektualnej. Nieokreśloność nie czyni postanowienia nieważnym, ale przenosi spór na wykładnię, gdzie Spółka po zmianie kontroli jest stroną silniejszą.
- **Rekomendacja memorandum:** Zdefiniować w § 10 „Zmianę Kontroli” i „Istotną Przyczynę” (jako zdarzenia z ust. 5), rozszerzyć okno o okres od zawarcia umowy zmiany kontroli do jej wykonania i objąć nim rezygnację z powodu istotnego pogorszenia warunków.
- **Podstawa prawna:** art. 353¹, art. 65 KC [Z]; art. 4 § 1 pkt 4 KSH (definicja spółki dominującej — pomocniczo do pojęcia kontroli) [Z]

#### § 10 ust. 13: rozszerzenie obowiązkowej treści umowy wykonawczej (oferta lub umowa przedwstępna, oznaczony pełnomocnik z podpisem poświadczonym, wstrzymanie terminu, niezapłacenie ceny, zbieg z prawem pierwszeństwa)

Commit `b525dd9` · memorandum 1.5.3, K4 · klasa: konieczne

- **Pytanie:** Umowa wykonawcza: czy nieodwołalne oferty i pełnomocnictwa (art. 101 § 2 i art. 108 KC) mogą zostać skonstruowane tak, aby mechanizm zadziałał bez dalszego podpisu akcjonariusza, i czy orzeczenie zastępujące oświadczenie woli (art. 64 KC, art. 1047 KPC) jest realną drogą wykonania? Jak wygląda minimalna treść takiej umowy (zdarzenie, stwierdzenie Odejścia, nabywca, cena, terminy)?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo — konstrukcja poprawna co do zasady, projekt umowy wykonawczej ma braki, z których dwa są istotne
- **Dlaczego zmieniono:** **Oferta.** Oferta z oznaczonym terminem związania wiąże oferenta do upływu tego terminu (art. 66 § 2 KC a contrario — przepis reguluje wprost tylko ofertę bez terminu); po dojściu do adresata (art. 61 § 1 KC) prawo nie przewiduje jej jednostronnego odwołania, a nawet w obrocie między przedsiębiorcami — gdyby założyciel składał ofertę w ramach współpracy B2B — „oferty nie można odwołać, jeżeli wynika to z jej treści lub określono w niej termin przyjęcia” (art. 66² § 2 KC); zastrzeżenie „nieodwołalności” jest więc skuteczne i w istocie deklaratoryjne. Oferta pod warunkiem zawieszającym Odejścia (art. 89 KC) i z ceną oznaczalną „według Wartości Godziwej” (art. 536 § 1 KC) jest dopuszczalna; śmierć oferenta nie umarza oferty (art. 62 KC), co umowa wykonawcza prawidłowo wykorzystuje w § [umowa wspólników: smierc]. Forma: zbycie akcji P.S.A. wymaga formy dokumentowej pod rygorem nieważności (art. 300³⁶ § 4 KSH), więc oferta i przyjęcie w formie dokumentowej wystarczają materialnie; co więcej, „oświadczenie akcjonariusza o zobowiązaniu do przeniesienia akcji” jest samodzielną podstawą wpisu w rejestrze (art. 300³⁴ § 4 zdanie drugie KSH), więc ofertę albo umowę przedwstępną warto zredagować tak, aby mogła pełnić tę rolę. **Brak nr 1**: oferta z Załącznika A jest skierowana do osoby nieoznaczonej („Dopuszczalny Nabywca wskazany przez Spółkę”). […]
- **Rekomendacja memorandum:** Przebudować Załączniki A–B (oferta do Spółki z prawem wskazania nabywcy plus umowa przedwstępna; pełnomocnictwo dla Spółki z substytucją, z podpisem notarialnie poświadczonym), uzupełnić braki (a)–(g), a w § 10 ust. 13 rozszerzyć katalog obowiązkowej treści. Umowę wykonawczą podpisać tego samego dnia co umowę Spółki; wzory uzgodnić z podmiotem prowadzącym rejestr.
- **Podstawa prawna:** art. 61 § 1, art. 62, art. 66 § 1–2, art. 66² § 2, art. 89, art. 99 § 1, art. 101 § 1–2, art. 106, art. 108, art. 389–390, art. 393, art. 536 § 1 KC [Z]; art. 64 KC, art. 1047 § 1–2 i art. 786 § 1 KPC [Z]; art. 300³⁶ § 4, art. 300³⁴ § 3–5, art. 300³⁷ § 1 KSH [Z]; SN V CSK 522/18 i II CSKP 593/22 [Z] (tezy według `psa_feedback.tex`; teksty orzeczeń niedostępne); art. 730 i n. KPC [Z]; art. 4 pkt 1 i art. 7 ust. 1 pkt 1 lit. b ustawy o PCC [Z]
- **Orzecznictwo:** II CSKP 593/22, V CSK 522/18 (zob. sekcja 6)

#### § 10 ust. 14: obowiązek zbycia obciąża każdoczesnego posiadacza akcji, Spółka żąda wpisu wzmianek w rejestrze (art. 300^33 KSH)

Commit `1bb60c1` · memorandum 1.5.1, K3 · klasa: konieczne

- **Pytanie:** Czy obowiązek zbycia jako „obowiązek związany z akcją” jest skuteczny wobec nabywców wtórnych i wobec podmiotu prowadzącego rejestr akcjonariuszy; jak go ujawnić w rejestrze?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo — skuteczność wobec Spółki i rejestru tak, wobec nabywcy wtórnego z luką w § 12 ust. 2
- **Dlaczego zmieniono:** Obowiązek zbycia jest świadczeniem akcjonariusza wobec Spółki „określonym w umowie spółki” w rozumieniu art. 300¹ § 3 KSH, a więc obowiązkiem o charakterze korporacyjnym, który obciąża każdoczesnego posiadacza akcji, a nie tylko podpisującego umowę założyciela. Kwalifikacja w § 10 ust. 14 („obowiązek związany z akcją wobec Spółki”) jest prawidłowa i odpowiada kategoriom, które rejestr akcjonariuszy ujawnia z mocy ustawy: „ograniczenia co do rozporządzania akcją” (art. 300³³ § 1 pkt 10 KSH) oraz „postanowienia umowy spółki o związanych z akcją obowiązkach wobec spółki” (pkt 11); umowa spółki może ponadto przewidzieć dodatkowe informacje ujawniane w rejestrze (art. 300³³ § 2 KSH). Podmiot prowadzący rejestr wpisuje te wzmianki na żądanie Spółki, nie później niż w siedem dni, na podstawie przedłożonych dokumentów — tu samej umowy spółki (art. 300³⁴ § 1 i 4 KSH); nie potrzeba do tego zgody akcjonariusza. […]
- **Rekomendacja memorandum:** Zamknąć lukę w § 12 ust. 2: dodać podstawę odmowy zgody dla akcji objętych obowiązkiem zbycia, gdy nabywca nie przystąpił do umowy wykonawczej (oferta i pełnomocnictwo), oraz doprecyzować w § 10 ust. 14, że obowiązek obciąża każdoczesnego posiadacza akcji i że zdarzenia dotyczące Akcjonariusza Funkcjonalnego uruchamiają obowiązek także wobec nabywcy. Przed zawiązaniem uzgodnić z wybranym podmiotem prowadzącym rejestr (notariusz albo dom maklerski) brzmienie wzmianek do wpisu.
- **Podstawa prawna:** art. 300¹ § 3 KSH [Z]; art. 300³³ § 1 pkt 10–11 i § 2 KSH [Z]; art. 300³³ § 3 i art. 594 § 1 pkt 2¹ KSH w brzmieniu od 18.02.2027 r. (Dz.U. 2026 poz. 176) [Z]; art. 300³⁴ § 1 i 4–6 KSH [Z]; art. 300³⁷ § 1 i art. 300³⁸ § 1 KSH [Z]; art. 300³⁹ § 1–2 KSH [Z]; art. 300³⁶ § 4 KSH (forma dokumentowa zbycia) [Z]; art. 353¹ KC [Z]

### § 11. Dopuszczalny Nabywca, Niedopuszczalny Nabywca i zmiana stanu prawnego po nabyciu

#### § 11 ust. 6: definicja porozumienia i działania na cudzy rachunek, zawiadomienie o porozumieniu w 14 dni, okresowe ponowienie oświadczenia

Commit `f48967d` · memorandum 1.1.3 · klasa: zalecane

- **Pytanie:** Czy wyłączenie nabycia na cudzy rachunek (§ 11 ust. 6) jest wystarczająco określone i egzekwowalne — w szczególności wobec podmiotu prowadzącego rejestr akcjonariuszy — oraz czy oświadczenie nabywcy z § 11 ust. 8 wystarcza jako narzędzie weryfikacji? Jakie skutki naruszenia (§ 12 ust. 8, § 36) są realnie osiągalne?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Klauzula jest wystarczająco określona co do istoty (rachunek, interes, polecenie; powiernik, pełnomocnik, strona porozumienia), lecz „w interesie” jest zwrotem ocennym, a „porozumienie dotyczące wykonywania praw z akcji” nie zostało zdefiniowane. Wobec podmiotu prowadzącego rejestr klauzula nie jest egzekwowalna bezpośrednio: podmiot ten „bada treść i formę dokumentów uzasadniających dokonanie wpisu”, nie ma natomiast „obowiązku badania zgodności z prawem oraz prawdziwości dokumentów”, chyba że poweźmie uzasadnione wątpliwości (art. 300³⁴ § 5 KSH), a więc nie bada stosunków wewnętrznych między nabywcą a jego mocodawcą [Z]; wpisze osobę, która przedstawi umowę zbycia i zgodę Spółki. Bramką jest zatem wyłącznie Spółka na etapie zgody, a jej narzędziem oświadczenie z ust. 8, dokumenty struktury właścicielskiej i publiczne wykazy (ust. 9). […]
- **Rekomendacja memorandum:** Doprecyzować: zdefiniować „porozumienie” przez odesłanie do pisemnego albo ustnego porozumienia dotyczącego zgodnego głosowania, prowadzenia trwałej polityki wobec Spółki albo nabywania akcji; zastąpić „w interesie” zwrotem „na zlecenie albo na ryzyko ekonomiczne”; dodać obowiązek ponownego złożenia oświadczenia na żądanie Rady (nie częściej niż raz w roku) i obowiązek zawiadomienia o zawarciu porozumienia w 14 dni; rozważyć karę umowną w umowie akcjonariuszy (nie w umowie spółki).
- **Podstawa prawna:** art. 300³³ § 1 pkt 10–11, art. 300³⁴ § 4–6, art. 300³⁷ § 1 i art. 300³⁸ § 1 KSH [Z]; art. 83 i art. 58 KC [Z]; art. 87 ust. 1 pkt 5–6 ustawy o ofercie publicznej (definicja działania w porozumieniu, jako wzorzec redakcyjny) [W]; art. 471 i art. 483 KC [Z].

#### § 11 ust. 11a: tryb stwierdzenia statusu Prawnie Niedopuszczalnego Posiadacza, wstrzymanie świadczeń i praw, wyłączenie głosów zawieszonych z mianownika, prawa zarządcy przymusowego; § 24 ust. 12 odesłanie

Commit `0e85d47` · memorandum 1.7.3, K9 · klasa: konieczne

- **Pytanie:** Czy konstrukcja Prawnie Niedopuszczalnego Posiadacza (bez automatycznego przymusowego zbycia) jest spójna z sankcjami i kontrolą eksportu, i czy nie potrzebuje wyraźnego trybu zawieszenia wykonywania praw z akcji?
- **Ocena brzmienia 0.9.4-C:** ryzyko — konstrukcja spójna, ale brak trybu zawieszenia i korekty progów głosowania może sparaliżować Spółkę
- **Dlaczego zmieniono:** Konstrukcja jest trafna: zamrożenie środków i zasobów gospodarczych (art. 2 ust. 1 rozp. 269/2014: zamrożeniu podlegają wszystkie środki finansowe i zasoby gospodarcze „należące do, będące własnością, w posiadaniu lub pod kontrolą” osób z załącznika I, a „środki finansowe” obejmują wprost „akcje i udziały”, art. 1 lit. g pkt iii; „zamrożenie” to zapobieżenie każdemu przeniesieniu lub użyciu, „które skutkowałoby jakąkolwiek zmianą ich wielkości, kwoty, lokalizacji, własności, posiadania, charakteru, przeznaczenia”, art. 1 lit. f — tłum. robocze [Z] (tekst EN, pierwotny; załącznik I jako lista wymaga sprawdzenia w wersji skonsolidowanej); wobec osób z listy krajowej ustawa z 2022 r. nakazuje „odpowiednio” stosować art. 2 i 9 tego rozporządzenia — art. 1 pkt 2 ustawy — a niedopełnienie obowiązku zamrożenia albo zakazu udostępniania zagrożone jest karą pieniężną do 20 000 000 zł, art. 6 ust. 1–2 ustawy) obejmuje akcje, więc ich zbycie jest zakazane, a nabywca niczego by nie nabył — automatyczne przymusowe zbycie byłoby więc czynnością zakazaną (art. 58 § 1 KC), co § 11 ust. 11–12 słusznie wykluczają; zbycie jest możliwe dopiero wtedy, gdy dopuszczą je właściwe przepisy, i ust. 11 tę ścieżkę przewiduje. Tekst pierwotny rozporządzenia zna jednak tylko derogacje z art. 4–6 (podstawowe potrzeby, koszty usług prawnych i utrzymania zamrożonych zasobów, wydatki nadzwyczajne — art. 4; zaspokojenie roszczeń stwierdzonych orzeczeniem arbitrażowym sprzed wpisu albo orzeczeniem sądowym lub administracyjnym — art. 5; płatność należna od osoby z listy z umowy lub zobowiązania powstałego przed wpisem — art. 6) [Z] (tekst EN) i nie przewiduje wprost zezwolenia na zbycie zamrożonych akcji; czy taka derogacja istnieje w obecnym brzmieniu (późniejsze zmiany), trzeba sprawdzić w wersji skonsolidowanej [?]. Wobec osób z listy krajowej ustawa z 2022 r. przewiduje natomiast ścieżkę publicznoprawną: minister właściwy do spraw gospodarki może ustanowić tymczasowy zarząd przymusowy, gdy jest to niezbędne dla funkcjonowania przedsiębiorstwa prowadzonego w Polsce w celu utrzymania miejsc pracy, usług użyteczności publicznej albo ochrony interesu ekonomicznego państwa (art. 6a ust. 1), a zarządca „wykonuje prawa z akcji” osoby z listy (art. 6a ust. 11 pkt 3) i może je zbyć na podstawie pełnomocnictwa albo postanowienia sądu (art. 6a ust. 15–16); możliwy jest też zarząd w celu przejęcia własności za odszkodowaniem odpowiadającym wartości rynkowej (art. 6b ust. 1 i 4) [Z]. […]
- **Rekomendacja memorandum:** Dodać w § 11 tryb stwierdzenia statusu uchwałą Rady, wstrzymania świadczeń i niedopuszczenia do wykonywania praw w zakresie wynikającym z prawa, oraz regułę wyłączenia głosów zawieszonych z mianownika większości umownych, z zastrzeżeniem wykonywania praw przez zarządcę przymusowego.
- **Podstawa prawna:** art. 1 lit. e–g, art. 2 ust. 1–2, art. 4–7 i art. 9 rozporządzenia Rady (UE) nr 269/2014 [Z] (tekst EN, pierwotny, bez konsolidacji); art. 1 pkt 2, art. 2, art. 6 ust. 1–2, art. 6a ust. 1, 11, 15–16 i 27, art. 6b ust. 1 i 4 oraz art. 6da ustawy z 13 kwietnia 2022 r. o szczególnych rozwiązaniach w zakresie przeciwdziałania wspieraniu agresji na Ukrainę oraz służących ochronie bezpieczeństwa narodowego [Z]; art. 1 oraz art. 2 pkt 2 lit. d i pkt 10 lit. c rozporządzenia (UE) 2021/821 [Z] (tekst EN, wersja skonsolidowana na 26.05.2023); art. 300¹ § 3, art. 300³³, art. 300³⁹ § 6 KSH [Z]; art. 58 § 1 KC [Z]

#### § 11 ust. 14, § 32 ust. 1: przywrócenie wyjątku dla Kwalifikowanego Inwestora Finansowego w brzmieniu uszczelnionym (zarządzający regulowany, rozproszenie, progi 25%/50%/10%, ujawnienie beneficjentów, zawiadomienia) i odesłania

Commit `a839982` · memorandum 1.4.1, 1.4.3, decyzja D3 · klasa: zalecane

*Pytanie 1.4.1.*

- **Pytanie:** Czy zachowanie wyjątku uprościłoby obsługę zbyć wtórnych i wejścia funduszy (w tym funduszy z inwestorami spoza UE/NATO) bez naruszenia wymogów właścicielskich programów finansowania obronnego i przepisów o kontroli inwestycji?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Tak. Bez wyjątku każdy fundusz VC z choćby jednym inwestorem (LP) spoza UE/EOG/NATO — a to niemal każdy fundusz z kapitałem ze Szwajcarii, Izraela, Singapuru, Japonii, Korei, Australii czy Zatoki — nie spełnia lit. b Kryterium (beneficjenci rzeczywiści) i potrzebuje uchwały Walnego Zgromadzenia 75% do każdej transakcji: wejścia w rundzie, dokupienia, przeniesienia do funduszu następcy. Uchwała jest osiągalna, ale odbierana przez fundusze jako sygnał ryzyka i przedmiot negocjacji od pierwszego spotkania (`vc.md` sekcje 1 i 4 [W]). […]
- **Rekomendacja memorandum:** Przywrócić ust. 14 w brzmieniu uszczelnionym (1.4.3) wraz z odesłaniem w § 32 ust. 1 i wyłączeniem w § 11 ust. 15 zdarzeń po stronie pasywnych inwestorów funduszu. Decyzja należy do Założycieli; jeżeli zdecydują o usunięciu wyjątku, umowa pozostaje poprawna, a koszt przenosi się na każdą rundę (uchwała 75%).
- **Podstawa prawna:** art. 2 pkt 6 i 24, art. 5 oraz art. 9 ust. 3–4 i 7 rozporządzenia 2021/697 (EDF: kontrola przez państwo trzecie) [Z]; art. 2 pkt 1, 5, 7 i 8, art. 4 ust. 15, art. 5 ust. 1 lit. a, art. 15 ust. 1 lit. a–b i ust. 3, art. 19 ust. 2 lit. e oraz motyw 18 rozporządzenia (UE) 2026/1386 (od 17 stycznia 2028 r.) [Z] (tekst EN); warunki NATO DIANA (siedziba w państwie NATO) [W]; NATO Innovation Fund (wspierany przez 24 państwa NATO, inwestuje w spółki z siedzibą w jednym z tych państw — `web_nif_about.txt`) [Z]; art. 3 ust. 1 pkt 1, art. 12c ust. 6 i art. 12e ust. 4 ustawy o kontroli niektórych inwestycji (podmiot dominujący, nabycie pośrednie, spółki zależne podmiotów z państw trzecich) [Z]; ustawa z 27 maja 2004 r. o funduszach inwestycyjnych i zarządzaniu alternatywnymi funduszami inwestycyjnymi (ASI, ZASI) [W]; dyrektywa 2011/61/UE (AIFMD) [W].

*Pytanie 1.4.3.*

- **Pytanie:** Jeżeli wyjątek ma zostać, jak go sformułować, aby nie stał się furtką dla podmiotów spoza Kryterium (np. wehikuły jednego inwestora)?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Furtki w przekreślonym brzmieniu są trzy: (1) brak wymogu rozproszenia — fundusz z jednym LP spoza Kryterium, zarządzany formalnie z UE, spełniałby test; (2) brak wymogu statusu regulacyjnego zarządzającego — „spółka zarządzająca aktywami” może być dowolną spółką; (3) zbyt szerokie zwolnienie z lit. b („nie stosuje się wymogu dotyczącego beneficjentów rzeczywistych”), obejmujące także beneficjentów kontrolujących. […]
- **Rekomendacja memorandum:** Przywrócić ust. 14 w brzmieniu poniżej; przywrócić odesłanie w § 32 ust. 1; dodać w ust. 15 wyłączenie zdarzeń po stronie pasywnych inwestorów.
- **Podstawa prawna:** art. 300³⁹ § 1 KSH [Z]; ustawa o funduszach inwestycyjnych i zarządzaniu AFI (ZASI, rejestr KNF) [W]; dyrektywa 2011/61/UE [W]; art. 2 ust. 2 pkt 1 lit. a ustawy AML (beneficjent rzeczywisty) [Z]; art. 2 pkt 1, 7 i 8 oraz art. 19 ust. 2 lit. e rozporządzenia (UE) 2026/1386 [Z] (tekst EN); art. 9 ust. 7 rozporządzenia 2021/697 [Z]; strony programów PFR Ventures (`pfr_pfrv_starter.txt`, `pfr_pfrv_biznest.txt`, `pfr_pfrv_otwarte_innowacje.txt`, `pfr_pfrv_koffi.txt`) [Z]; `vc.md` sekcja 6 pkt 1 [W].

#### § 11 ust. 14: test kontroli także nad zarządzającym i przez inwestora spoza Kryterium, zachowanie weryfikacji i obowiązków AML, fundusze siostrzane bez odrębnej uchwały

Commit `802a590` · memorandum 4.4.2, brzmienie I · klasa: zalecane — odstępstwo od reguły „zgodne warunkowo → zalecane” nie jest potrzebne; brzmienia podajemy, bo zmiany są proste i jednoznaczne

- **Pytanie:** Jakie zmiany ułatwiłyby dostosowanie umowy do rundy bez naruszenia jej założeń (bezpieczeństwo właścicielskie, kontrola eksportu, mechanizm zwrotnego zbycia)?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo — założenia umowy da się utrzymać w całości; potrzebne są cztery zmiany w umowie spółki przed rundą i przeniesienie reszty do dokumentów rundy
- **Dlaczego zmieniono:** Kryterium zmian jest jedno: nic, co decyduje o dostępie do EDF, EUDIS, DIANA/NIF i koncesji, nie może zostać osłabione (warunki EDF: siedziba i „zarządcze struktury wykonawcze” w Unii lub w państwie stowarzyszonym oraz brak „kontroli niestowarzyszonego państwa trzeciego lub podmiotu z niestowarzyszonego państwa trzeciego”, art. 9 ust. 1–3 rozporządzenia 2021/697, z derogacją za gwarancjami zatwierdzonymi przez państwo członkowskie lub stowarzyszone siedziby z art. 9 ust. 4 [Z]; państwa stowarzyszone to według art. 5 członkowie EFTA należący do EOG, których rozporządzenie nie wymienia z nazwy [Z], w praktyce obecnie Norwegia, `web_edf_gowling.txt` [Z]; warunek NIF: siedziba w jednym z 24 państw NATO będących jego inwestorami, `web_nif_about.txt` [Z]). Te założenia to: (i) kontrola nad Spółką pozostaje w rękach osób i podmiotów z UE/EOG/NATO, a — jeżeli Założyciele przyjmą decyzję D6 — z UE/EOG; (ii) dostęp do Kluczowej Własności Intelektualnej spoza UE/NATO tylko za zgodą Rady po analizie eksportowej (§ 27 ust. 6, § 28); […]
- **Rekomendacja memorandum:** Wprowadzić zmiany A.1–A.4 przed pierwszym term sheetem (A.1 i A.3 warunkują w praktyce rozmowę z funduszami D i Z); A.5 i A.6 zależnie od decyzji Założycieli o kręgu inwestorów; A.7 po stanowisku kancelarii. Resztę zostawić dokumentom rundy. Brzmienia poniżej są sugestią do weryfikacji przez uprawnionego prawnika, w szczególności co do art. 300³⁹ § 2 KSH (wyłączenie zgody Spółki dla kategorii przeniesień) i ujawnienia w rejestrze akcjonariuszy.
- **Podstawa prawna:** art. 300³⁹ § 1–2 KSH („chyba że umowa spółki stanowi inaczej”) [Z]; art. 300²⁵ § 1–2 i art. 300²⁸ § 1–2 KSH [Z]; art. 300³³ § 1 pkt 4 i 10 KSH (rejestr akcjonariuszy zawiera „rodzaj danej akcji i uprawnienia szczególne z akcji” oraz „ograniczenia co do rozporządzania akcją”) [Z]; art. 300¹⁰³ KSH (emisja na podstawie postanowień umowy „przewidujących maksymalną liczbę akcji i termin ich emisji” bez trybu zmiany umowy) [Z]; art. 300¹⁰⁴ § 1 pkt 2 KSH [Z]; art. 300¹⁰⁶ § 1–2 KSH (prawo poboru, „jeżeli umowa spółki lub uchwała akcjonariuszy nie stanowią inaczej”; pozbawienie uchwałą większością 4/5) [Z]; art. 2 pkt 6 i 24, art. 5 i art. 9 ust. 1–4 i 7 rozporządzenia (UE) 2021/697 [Z]; art. 2 pkt 1, 5 i 7, art. 4 ust. 1, 2, 9 i 15 lit. a–c, art. 5 ust. 1–2, art. 6, art. 11 ust. 3 i 5, art. 20 ust. 4 lit. a, art. 30–31, motywy 14–15 i 20, zał. I pkt 1–3 i zał. II pkt 14 rozporządzenia (UE) 2026/1386 [Z] (tekst EN); rozporządzenie (UE) 2021/821 (unijny system kontroli wywozu, pośrednictwa, pomocy technicznej, tranzytu i transferu produktów podwójnego zastosowania; do jego zał. I odsyła art. 4 ust. 15 lit. a rozporządzenia 2026/1386) [Z] (tekst EN, konsolidacja na 26.05.2023 r.); art. 12a ust. 1 pkt 1, art. 12c ust. 1 pkt 1 i 5, ust. 4–5 oraz art. 12d ust. 3 pkt 7 i ust. 4 ustawy o kontroli niektórych inwestycji [Z]; art. 2 ust. 2 pkt 1 ustawy AML [Z].

#### § 11 ust. 15: 3-miesięczny termin na wskazanie nabywcy przez Spółkę, Wartość Godziwa na dzień zdarzenia, wyłączenie Spółki jako nabywcy poza art. 300^47 KSH, skutek braku wskazania

Commit `06a40d7` · memorandum 1.1.4 · klasa: zalecane

- **Pytanie:** Utrata Kryterium po nabyciu (§ 11 ust. 15): czy obowiązek zbycia akcji w 6 miesięcy i prawo Spółki do wskazania nabywcy są dopuszczalne i skuteczne wobec nabywców wtórnych jako obowiązek „związany z akcją”; czy nie grozi zakwalifikowanie tej konstrukcji jako przymusowego wykupu poza trybem ustawowym?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Obowiązek zbycia na rzecz osoby trzeciej za Wartość Godziwą nie jest ani umorzeniem (akcje nie są unicestwiane, brak obniżenia kapitału akcyjnego), ani nabyciem akcji własnych (nabywcą nie jest Spółka ani osoba działająca na jej rachunek — projekt powinien to powtórzyć wprost, jak w § 10 ust. 11–12), ani przymusowym wykupem: przepisy o P.S.A. nie zawierają odpowiednika art. 418 KSH, a jedynymi ustawowymi trybami przymusowej zmiany składu akcjonariatu są sądowe wyłączenie akcjonariusza (art. 300⁴⁹) i ustąpienie akcjonariusza z wykupem „po cenie odpowiadającej wartości godziwej” (art. 300⁵⁰ § 3) [Z]. Jest to umowny obowiązek związany z akcją, dopuszczalny na podstawie autonomii umowy spółki (art. 300¹ § 3 w zw. z art. 300³⁹ § 1 KSH) i podlegający ujawnieniu w rejestrze (art. 300³³ § 1 pkt 11). Wobec nabywcy wtórnego obowiązek jest skuteczny, ponieważ nabywca akcji wstępuje w stosunek spółki ukształtowany umową; ujawnienie w rejestrze wyłącza zarzut nieznajomości. […]
- **Rekomendacja memorandum:** Uzupełnić ust. 15 o: termin 3 miesięcy dla Spółki na wskazanie nabywcy, a po jego bezskutecznym upływie — utrzymanie obowiązku z zawieszeniem prawa do wskazania do czasu kolejnego wezwania; wyłączenie z „utraty Kryterium” zdarzeń po stronie inwestorów pasywnych funduszu, jeżeli Założyciele przywrócą ust. 14 (zob. 1.4.3); zdanie, że nabywcą nie może być Spółka ani osoba działająca na jej rachunek poza trybem art. 300⁴⁷ KSH; wymóg przystąpienia każdego inwestora do umowy wykonawczej w zakresie pełnomocnictwa (do umowy inwestycyjnej).
- **Podstawa prawna:** art. 300³³ § 1 pkt 11 KSH (obowiązki związane z akcją w rejestrze) [Z]; art. 300³⁹ § 1 KSH [Z]; art. 300⁴⁵ § 2, art. 300⁴⁷ § 9 oraz art. 300⁴⁹–300⁵⁰ KSH [Z]; art. 64 KC, art. 1047 KPC [Z]; SN II CSKP 593/22 [Z].
- **Orzecznictwo:** II CSKP 593/22 (zob. sekcja 6)

#### § 11 ust. 16: obowiązek akcjonariusza z pakietem co najmniej 20% dostarczenia zaświadczeń o niekaralności i danych do postępowania koncesyjnego

Commit `6255bdf` · memorandum 4.1.1 · klasa: zalecane

- **Pytanie:** Czy powołana podstawa (ustawa z 13 czerwca 2019 r. o wykonywaniu działalności gospodarczej w zakresie wytwarzania i obrotu materiałami wybuchowymi, bronią, amunicją oraz wyrobami i technologią o przeznaczeniu wojskowym lub policyjnym) jest aktualna i obejmuje bezzałogowe statki powietrzne oraz ich oprogramowanie; jak ma się do prawa lotniczego i rozporządzeń UE o bezzałogowych systemach powietrznych?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo — podstawa aktualna i trafnie powołana; zmiany z 2026 r. sprawdzone w tekście i nieistotne dla Spółki; warunkiem jest kwalifikacja wyrobu do wykazu przed bramką G3
- **Dlaczego zmieniono:** **Aktualność.** Ustawa z 2019 r. obowiązuje i pozostaje właściwą podstawą reżimu koncesyjnego. Koncesji udziela, w drodze decyzji, minister właściwy do spraw wewnętrznych (art. 8 ust. 1), na czas oznaczony od 5 do 50 lat (art. 8 ust. 2), po zasięgnięciu opinii m.in. Szefa ABW i Szefa SKW (art. 9 ust. 1). […]
- **Rekomendacja memorandum:** Utrzymać obie klauzule. Doprecyzować § 4 ust. 8 tak, aby obejmował oprogramowanie i technologię (w tym licencjonowanie) oraz odsyłał do przepisów „w brzmieniu obowiązującym”; w § 3 ust. 4 zastąpić „certyfikacji lotniczej” zwrotem „oceny zgodności, certyfikacji i zezwoleń operacyjnych”. Przed bramką G3 z `regulations.md`: zakwalifikować konkretny wyrób do wykazu WT (kryterium „specjalnie zaprojektowany lub zmodyfikowany”), wyznaczyć dwóch dyrektorów (albo dyrektora i prokurenta) spełniających art. 10 ust. 1 pkt 1 (szkolenie z art. 11, badania z art. 12) oraz zaplanować pozyskanie zaświadczeń o niekaralności od akcjonariuszy z pakietem co najmniej 20%. Sygnał dla pakietu A1: rozważyć w § 11 ust. 15 obowiązek akcjonariusza dostarczenia dokumentów wymaganych w postępowaniu koncesyjnym.
- **Podstawa prawna:** ustawa z 13 czerwca 2019 r. (Dz.U. 2019 poz. 1214; t.j. Dz.U. 2023 poz. 1743), zmieniona art. 2 ustawy z 13 marca 2026 r. (Dz.U. 2026 poz. 471) [Z]; art. 3 ust. 1 pkt 12–13 (definicje technologii i wyrobów o przeznaczeniu wojskowym lub policyjnym), art. 4, art. 5, art. 7 ust. 1, art. 8 ust. 1–2, art. 9 ust. 1, art. 10 ust. 1 pkt 2–3, art. 11–12, art. 17 i art. 133 tej ustawy [Z]; brak w niej ustawowej definicji „wytwarzania” i „obrotu” [Z]; rozporządzenie Rady Ministrów z 17 września 2019 r. w sprawie klasyfikacji rodzajów materiałów wybuchowych, broni, amunicji oraz wyrobów i technologii o przeznaczeniu wojskowym lub policyjnym, na których wytwarzanie lub obrót jest wymagane uzyskanie koncesji (Dz.U. 2019 poz. 1888): część IV, kategoria WT V ust. 3, WT XI ust. 2, WT XIII ust. 3–4 oraz definicje pkt 12–15 załącznika [Z]; wykaz zawiera kategorie WT I–XIV, nie ma kategorii WT XXI/XXII [Z]; rozporządzenie (UE) 2018/1139, art. 2 ust. 3 lit. a [W]; rozporządzenie delegowane (UE) 2019/945 [W]; rozporządzenie wykonawcze (UE) 2019/947 (tekst pierwotny): art. 2 pkt 1 i 17, art. 3–6, art. 12, art. 14 ust. 5–6, art. 23 ust. 1–2, załącznik część A pkt UAS.OPEN.060 ust. 2 lit. d i część B pkt UAS.SPEC.050 ust. 1 lit. b [Z] (tekst EN); przesunięcie daty stosowania na 31 grudnia 2020 r. rozporządzeniem wykonawczym (UE) 2020/746 [W]; ustawa Prawo lotnicze (t.j. Dz.U. 2025 poz. 1431): art. 1 ust. 3–4, art. 2 pkt 1a, 1b, 2 i 24–26, dział VIa (art. 156a i n.), art. 156b ust. 3 [Z]; rozporządzenie (UE) 2021/821: art. 2 pkt 1 (produkty podwójnego zastosowania obejmują oprogramowanie i technologię) [Z] (tekst EN); ustawa z 29 listopada 2000 r. o obrocie z zagranicą towarami, technologiami i usługami o znaczeniu strategicznym: art. 3 pkt 10, art. 6, art. 33 ust. 1 [Z].

#### § 11 ust. 15: utrata Kryterium przez Kwalifikowanego Inwestora Finansowego ograniczona do zmiany kontroli nad zarządzającym i uprawnień inwestora spoza Kryterium

Commit `d67d64e` · memorandum 4.4.2, brzmienie II · klasa: zalecane — odstępstwo od reguły „zgodne warunkowo → zalecane” nie jest potrzebne; brzmienia podajemy, bo zmiany są proste i jednoznaczne

- **Pytanie:** Jakie zmiany ułatwiłyby dostosowanie umowy do rundy bez naruszenia jej założeń (bezpieczeństwo właścicielskie, kontrola eksportu, mechanizm zwrotnego zbycia)?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo — założenia umowy da się utrzymać w całości; potrzebne są cztery zmiany w umowie spółki przed rundą i przeniesienie reszty do dokumentów rundy
- **Dlaczego zmieniono:** Kryterium zmian jest jedno: nic, co decyduje o dostępie do EDF, EUDIS, DIANA/NIF i koncesji, nie może zostać osłabione (warunki EDF: siedziba i „zarządcze struktury wykonawcze” w Unii lub w państwie stowarzyszonym oraz brak „kontroli niestowarzyszonego państwa trzeciego lub podmiotu z niestowarzyszonego państwa trzeciego”, art. 9 ust. 1–3 rozporządzenia 2021/697, z derogacją za gwarancjami zatwierdzonymi przez państwo członkowskie lub stowarzyszone siedziby z art. 9 ust. 4 [Z]; państwa stowarzyszone to według art. 5 członkowie EFTA należący do EOG, których rozporządzenie nie wymienia z nazwy [Z], w praktyce obecnie Norwegia, `web_edf_gowling.txt` [Z]; warunek NIF: siedziba w jednym z 24 państw NATO będących jego inwestorami, `web_nif_about.txt` [Z]). Te założenia to: (i) kontrola nad Spółką pozostaje w rękach osób i podmiotów z UE/EOG/NATO, a — jeżeli Założyciele przyjmą decyzję D6 — z UE/EOG; (ii) dostęp do Kluczowej Własności Intelektualnej spoza UE/NATO tylko za zgodą Rady po analizie eksportowej (§ 27 ust. 6, § 28); […]
- **Rekomendacja memorandum:** Wprowadzić zmiany A.1–A.4 przed pierwszym term sheetem (A.1 i A.3 warunkują w praktyce rozmowę z funduszami D i Z); A.5 i A.6 zależnie od decyzji Założycieli o kręgu inwestorów; A.7 po stanowisku kancelarii. Resztę zostawić dokumentom rundy. Brzmienia poniżej są sugestią do weryfikacji przez uprawnionego prawnika, w szczególności co do art. 300³⁹ § 2 KSH (wyłączenie zgody Spółki dla kategorii przeniesień) i ujawnienia w rejestrze akcjonariuszy.
- **Podstawa prawna:** art. 300³⁹ § 1–2 KSH („chyba że umowa spółki stanowi inaczej”) [Z]; art. 300²⁵ § 1–2 i art. 300²⁸ § 1–2 KSH [Z]; art. 300³³ § 1 pkt 4 i 10 KSH (rejestr akcjonariuszy zawiera „rodzaj danej akcji i uprawnienia szczególne z akcji” oraz „ograniczenia co do rozporządzania akcją”) [Z]; art. 300¹⁰³ KSH (emisja na podstawie postanowień umowy „przewidujących maksymalną liczbę akcji i termin ich emisji” bez trybu zmiany umowy) [Z]; art. 300¹⁰⁴ § 1 pkt 2 KSH [Z]; art. 300¹⁰⁶ § 1–2 KSH (prawo poboru, „jeżeli umowa spółki lub uchwała akcjonariuszy nie stanowią inaczej”; pozbawienie uchwałą większością 4/5) [Z]; art. 2 pkt 6 i 24, art. 5 i art. 9 ust. 1–4 i 7 rozporządzenia (UE) 2021/697 [Z]; art. 2 pkt 1, 5 i 7, art. 4 ust. 1, 2, 9 i 15 lit. a–c, art. 5 ust. 1–2, art. 6, art. 11 ust. 3 i 5, art. 20 ust. 4 lit. a, art. 30–31, motywy 14–15 i 20, zał. I pkt 1–3 i zał. II pkt 14 rozporządzenia (UE) 2026/1386 [Z] (tekst EN); rozporządzenie (UE) 2021/821 (unijny system kontroli wywozu, pośrednictwa, pomocy technicznej, tranzytu i transferu produktów podwójnego zastosowania; do jego zał. I odsyła art. 4 ust. 15 lit. a rozporządzenia 2026/1386) [Z] (tekst EN, konsolidacja na 26.05.2023 r.); art. 12a ust. 1 pkt 1, art. 12c ust. 1 pkt 1 i 5, ust. 4–5 oraz art. 12d ust. 3 pkt 7 i ust. 4 ustawy o kontroli niektórych inwestycji [Z]; art. 2 ust. 2 pkt 1 ustawy AML [Z].

### § 12. Zbywanie i obciążanie akcji

#### § 12 ust. 1: milczenie Rady Dyrektorów jako fikcja odmowy z przyczyny ust. 2 lit. b uruchamiająca ust. 3

Commit `06f6c30` · memorandum 1.3.1 · klasa: zalecane

- **Pytanie:** Czy 14-dniowy termin, forma dokumentowa i zamknięty katalog przyczyn odmowy są zgodne z art. 300³⁹ § 3 KSH i czy projekt powinien określać skutek milczenia Rady (zgoda dorozumiana albo bieg terminu na wskazanie nabywcy)?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Forma dokumentowa pod rygorem nieważności odpowiada art. 300³⁹ § 4 KSH, według którego czynności z § 3 (odmowę zgody i wskazanie nabywcy) „dokonuje zarząd w formie dokumentowej pod rygorem nieważności, chyba że umowa spółki stanowi inaczej”, a przepis stosuje się odpowiednio do akcji ograniczonych „w inny sposób”; w Spółce czynności te wykonuje Rada Dyrektorów (art. 4 § 2¹ KSH) [Z]; zachowanie tej formy w umowie jest wskazane niezależnie od derogacji. Termin 14 dni jest krótszy niż ustawowy miesiąc na wskazanie nabywcy i dotyczy innej czynności (stanowiska w sprawie zgody), więc nie koliduje z ustawą; ten sam termin 14 dni ustawa przyjmuje dla zgody na zbycie akcji nie w pełni pokrytej (art. 300⁴⁰ § 2 KSH); jest wykonalny, jeżeli Rada obraduje elektronicznie (§ 21 ust. 10). Zamknięty katalog przyczyn odmowy jest dopuszczalny i korzystny: ustawa nie wymaga uzasadnienia odmowy, ale umowa może związać Radę kryteriami obiektywnymi, co ogranicza spory i zarzut uznaniowości. […]
- **Rekomendacja memorandum:** Dodać skutek milczenia jako fikcję odmowy z przyczyny lit. b, z zastrzeżeniem wstrzymania terminu.
- **Podstawa prawna:** art. 300³⁹ § 3–5 i art. 4 § 2¹ KSH [Z]; art. 300⁴⁰ § 2 KSH (14-dniowy termin ustawowy dla zgody na zbycie akcji nie w pełni pokrytej) [Z]; art. 77² KC (forma dokumentowa) [Z]; art. 60 KC [Z]; art. 300⁵⁸ KSH (uchwały Rady) [Z].

#### § 12 ust. 8: Przeniesienia Dozwolone Kwalifikowanego Inwestora Finansowego (fundusz następca, równoległy, spółka celowa, wydanie inwestorom) bez zgody Spółki i prawa pierwszeństwa, z weryfikacją i Kryterium

Commit `69edc0b` · memorandum 4.4.1, 4.4.2 brzmienie III · klasa: zalecane, zalecane — odstępstwo od reguły „zgodne warunkowo → zalecane” nie jest potrzebne; brzmienia podajemy, bo zmiany są proste i jednoznaczne

*Pytanie 4.4.1.*

- **Pytanie:** Które postanowienia (Kryterium, mechanizm przy odmowie zgody, zwrotne zbycie, drag-along 75 %, Sprawy Zastrzeżone 75 %, ograniczenia finansowania) w Państwa doświadczeniu budzą zastrzeżenia funduszy na etapie seed/serii A i co zwykle jest przedmiotem negocjacji?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo — żadne z ocenianych postanowień nie jest prawnie wadliwe; sześć z nich odbiega od standardu rynkowego w sposób, który wydłuży negocjacje albo zawęzi krąg funduszy
- **Dlaczego zmieniono:** Zastrzeżenia omawiamy w kolejności, w jakiej zwykle pojawiają się w term sheecie, z rozróżnieniem trzech grup funduszy: (G) fundusze generalistyczne działające jako ASI z kapitałem PFR/BGK/EIF i przewagą polskich albo unijnych inwestorów — w programach PFR Ventures udział PFR w kapitalizacji funduszu wynosi maksymalnie 80% (PFR Starter: bilety do 5 mln PLN, przede wszystkim spółki przed pierwszą komercyjną sprzedażą, wkład prywatny min. 20%, `pfr_pfrv_starter.txt`) albo do 60% (PFR KOFFI: etap wzrostu, bilety od 4 mln PLN, min. 85% wartości portfela w spółkach z siedzibą w Polsce, wkład prywatny min. 40%, `pfr_pfrv_koffi.txt`; PFR Otwarte Innowacje w strukturze standardowej: bilety 5–70 mln PLN, program także „w obszarze zaawansowanych technologii obronnych i dual-use”, wkład prywatny min. 40%, `pfr_pfrv_otwarte_innowacje.txt`) [Z]; przy KOFFI PFR wymaga rejestracji ZASI najpóźniej przy podpisaniu umowy i oczekuje zdywersyfikowanej struktury LP (`pfr_pfrv_koffi.txt`), a przy Starterze due diligence obejmuje ryzyka ze struktury inwestorskiej, „m.in. stopnia dywersyfikacji inwestorskiej Funduszu” (`pfr_pfrv_starter.txt`) [Z], więc największym LP takiego funduszu jest polski podmiot publiczny, a pozostali LP są rozproszeni. Inaczej w modelach koinwestycyjnych: w PFR Biznest kapitalizację funduszu tworzą tylko PFR i zarządzający, a min. 40% wartości każdej inwestycji wnoszą inwestorzy prywatni, w tym aniołowie biznesu, poza funduszem (`pfr_pfrv_biznest.txt`); w modelu koinwestycyjnym PFR OI wkład PFR może sięgać 97% kapitalizacji funduszu, a prywatne min. 40% wnoszą koinwestorzy dobierani „deal by deal” bezpośrednio do spółki, każdy za akceptacją PFR OI (`pfr_pfrv_otwarte_innowacje.txt`) [Z] — tu aniołowie i koinwestorzy stają się akcjonariuszami Spółki obok funduszu, więc Kryterium i zgoda Rady dotyczą każdego z nich osobno; […]
- **Rekomendacja memorandum:** Rozstrzygnąć przed rundą, nie w jej trakcie, cztery punkty sporne z każdym funduszem: test Kryterium dla funduszy (§ 11 ust. 14 i 15), przeniesienia dozwolone (§ 12), ochrona serii inwestorskiej przy drag (§ 16) i katalog spraw wymagających zgody serii (§ 32 ust. 4). Pozostałe punkty zostawić do term sheetu. Brzmienia w odpowiedzi na pytanie 4.4.2. Wybór, czy szukać inwestora w grupie G/D (mniejsze zmiany), czy także Z (zmiany w § 21 ust. 3 i wariant A w § 12 ust. 3), należy do Założycieli.
- **Podstawa prawna:** art. 300³⁹ § 1–6 KSH [Z]; art. 300⁴⁷ KSH [Z]; art. 300¹⁰³–300¹⁰⁷ KSH [Z]; art. 300¹⁰⁶ § 2 KSH (pozbawienie prawa poboru) [Z]; art. 300²⁵ § 1–2 KSH (akcje uprzywilejowane; katalog otwarty: uprzywilejowanie „może dotyczyć w szczególności prawa głosu, prawa do dywidendy lub podziału majątku w przypadku likwidacji spółki”) [Z]; art. 300²⁸ § 1–2 KSH (uprawnienia indywidualne oznaczonego akcjonariusza, „w szczególności uprawnienie do powołania lub odwołania członków zarządu lub rady nadzorczej”, wygasające najpóźniej z utratą statusu akcjonariusza, „chyba że umowa spółki stanowi inaczej”) [Z]; art. 300¹⁰⁴ § 1 pkt 2 KSH (uprzywilejowanie akcji nowej emisji w uchwale o emisji) [Z]; art. 2 pkt 6 i 24, art. 5 i art. 9 ust. 1–4 i 7 rozporządzenia (UE) 2021/697 (EDF) [Z]; art. 2 pkt 1, 5 i 7, art. 4 ust. 2, 9 i 15, art. 5 ust. 1–2, art. 15 ust. 1 lit. b i ust. 3, art. 19 ust. 2 lit. e oraz motywy 14–15 rozporządzenia (UE) 2026/1386 (kontrola inwestycji zagranicznych, stosowane od 17 stycznia 2028 r., art. 31) [Z] (tekst EN); art. 2 ust. 2 pkt 1 ustawy z 2018 r. o przeciwdziałaniu praniu pieniędzy oraz finansowaniu terroryzmu (beneficjent rzeczywisty: osoba fizyczna sprawująca kontrolę, w tym mająca „więcej niż 25% ogólnej liczby udziałów lub akcji” albo głosów, a w braku takiej osoby — osoba na wyższym stanowisku kierowniczym) [Z]; ustawa o kontroli niektórych inwestycji [W]; praktyka rynkowa: wzorce NVCA po aktualizacji z 2 października 2025 r. (`web_nvca_2025_press.txt`, `web_nvca_2025_foley.txt`) [Z], omówienia PFR Startup (`web_pfr_umowa_inwestycyjna.txt`, `pfr_startup_umowa_inwestycyjna.txt`, pfr_startup_term_sheet.txt) [Z], strony programów PFR Ventures (`pfr_pfrv_starter.txt`, `pfr_pfrv_biznest.txt`, `pfr_pfrv_otwarte_innowacje.txt`, `pfr_pfrv_koffi.txt`) [Z], wzorce BVCA i treść wzorów term sheet PFR Ventures (same wzory nie zostały pobrane, `pfr_pfrv_feng_dokumentacja.txt`) [W].

*Pytanie 4.4.2.*

- **Pytanie:** Jakie zmiany ułatwiłyby dostosowanie umowy do rundy bez naruszenia jej założeń (bezpieczeństwo właścicielskie, kontrola eksportu, mechanizm zwrotnego zbycia)?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo — założenia umowy da się utrzymać w całości; potrzebne są cztery zmiany w umowie spółki przed rundą i przeniesienie reszty do dokumentów rundy
- **Dlaczego zmieniono:** Kryterium zmian jest jedno: nic, co decyduje o dostępie do EDF, EUDIS, DIANA/NIF i koncesji, nie może zostać osłabione (warunki EDF: siedziba i „zarządcze struktury wykonawcze” w Unii lub w państwie stowarzyszonym oraz brak „kontroli niestowarzyszonego państwa trzeciego lub podmiotu z niestowarzyszonego państwa trzeciego”, art. 9 ust. 1–3 rozporządzenia 2021/697, z derogacją za gwarancjami zatwierdzonymi przez państwo członkowskie lub stowarzyszone siedziby z art. 9 ust. 4 [Z]; państwa stowarzyszone to według art. 5 członkowie EFTA należący do EOG, których rozporządzenie nie wymienia z nazwy [Z], w praktyce obecnie Norwegia, `web_edf_gowling.txt` [Z]; warunek NIF: siedziba w jednym z 24 państw NATO będących jego inwestorami, `web_nif_about.txt` [Z]). Te założenia to: (i) kontrola nad Spółką pozostaje w rękach osób i podmiotów z UE/EOG/NATO, a — jeżeli Założyciele przyjmą decyzję D6 — z UE/EOG; (ii) dostęp do Kluczowej Własności Intelektualnej spoza UE/NATO tylko za zgodą Rady po analizie eksportowej (§ 27 ust. 6, § 28); […]
- **Rekomendacja memorandum:** Wprowadzić zmiany A.1–A.4 przed pierwszym term sheetem (A.1 i A.3 warunkują w praktyce rozmowę z funduszami D i Z); A.5 i A.6 zależnie od decyzji Założycieli o kręgu inwestorów; A.7 po stanowisku kancelarii. Resztę zostawić dokumentom rundy. Brzmienia poniżej są sugestią do weryfikacji przez uprawnionego prawnika, w szczególności co do art. 300³⁹ § 2 KSH (wyłączenie zgody Spółki dla kategorii przeniesień) i ujawnienia w rejestrze akcjonariuszy.
- **Podstawa prawna:** art. 300³⁹ § 1–2 KSH („chyba że umowa spółki stanowi inaczej”) [Z]; art. 300²⁵ § 1–2 i art. 300²⁸ § 1–2 KSH [Z]; art. 300³³ § 1 pkt 4 i 10 KSH (rejestr akcjonariuszy zawiera „rodzaj danej akcji i uprawnienia szczególne z akcji” oraz „ograniczenia co do rozporządzania akcją”) [Z]; art. 300¹⁰³ KSH (emisja na podstawie postanowień umowy „przewidujących maksymalną liczbę akcji i termin ich emisji” bez trybu zmiany umowy) [Z]; art. 300¹⁰⁴ § 1 pkt 2 KSH [Z]; art. 300¹⁰⁶ § 1–2 KSH (prawo poboru, „jeżeli umowa spółki lub uchwała akcjonariuszy nie stanowią inaczej”; pozbawienie uchwałą większością 4/5) [Z]; art. 2 pkt 6 i 24, art. 5 i art. 9 ust. 1–4 i 7 rozporządzenia (UE) 2021/697 [Z]; art. 2 pkt 1, 5 i 7, art. 4 ust. 1, 2, 9 i 15 lit. a–c, art. 5 ust. 1–2, art. 6, art. 11 ust. 3 i 5, art. 20 ust. 4 lit. a, art. 30–31, motywy 14–15 i 20, zał. I pkt 1–3 i zał. II pkt 14 rozporządzenia (UE) 2026/1386 [Z] (tekst EN); rozporządzenie (UE) 2021/821 (unijny system kontroli wywozu, pośrednictwa, pomocy technicznej, tranzytu i transferu produktów podwójnego zastosowania; do jego zał. I odsyła art. 4 ust. 15 lit. a rozporządzenia 2026/1386) [Z] (tekst EN, konsolidacja na 26.05.2023 r.); art. 12a ust. 1 pkt 1, art. 12c ust. 1 pkt 1 i 5, ust. 4–5 oraz art. 12d ust. 3 pkt 7 i ust. 4 ustawy o kontroli niektórych inwestycji [Z]; art. 2 ust. 2 pkt 1 ustawy AML [Z].

#### § 12 ust. 2 lit. e: zawiadomienie organu kontroli inwestycji składa nabywca przy współdziałaniu zbywcy i Spółki, termin złożenia i chwila ustania wstrzymania

Commit `5d857c8` · memorandum 1.1.2 · klasa: opcjonalne

- **Pytanie:** Jak Kryterium ma się do ustawy o kontroli niektórych inwestycji i innych przepisów o ochronie bezpieczeństwa i obronności — czy umowne Kryterium może współistnieć z kontrolą publiczną i czy powinno wprost do niej odsyłać?
- **Ocena brzmienia 0.9.4-C:** zgodne
- **Dlaczego zmieniono:** Kontrola publiczna i Kryterium działają na różnych płaszczyznach i nie kolidują. Ustawa o kontroli niektórych inwestycji zawiera dwa mechanizmy. Pierwszy (art. 4–12) dotyczy wyłącznie podmiotów umieszczonych w wykazie Rady Ministrów (art. 3 ust. 1 pkt 5, art. 4 ust. 2), a organem kontroli jest dla sektora zbrojeniowego Minister Obrony Narodowej (art. 3 ust. 1 pkt 6 lit. c); […]
- **Rekomendacja memorandum:** Bez zmian w definicji Kryterium. Opcjonalnie dopisać w § 12 ust. 2 lit. e, że obowiązek zawiadomienia organu (zgłoszenia wniosku o zezwolenie) obciąża nabywcę (zgodnie z art. 12f ust. 1 ustawy; w zakresie współdziałania — zbywcę i Spółkę), że zawiadomienie składa się niezwłocznie po zgłoszeniu Spółce zamiaru rozporządzenia, a w każdym razie przed zawarciem umowy zobowiązującej do nabycia (art. 12f ust. 5; od 17 stycznia 2028 r. — przed zamknięciem transakcji, art. 4 ust. 9 rozporządzenia 2026/1386), i że wstrzymanie terminu ustaje z dniem doręczenia decyzji albo upływu terminu na sprzeciw. W harmonogramach rund z inwestorem spoza Unii planowanych na 2028 r. i później uwzględnić 45-dniowe badanie wstępne i możliwe badanie pogłębione (art. 4 ust. 2) oraz — przy inwestorze kontrolowanym przez państwo trzecie albo gdy Spółka realizuje projekt EDF — terminy mechanizmu współpracy (art. 5–6, art. 9 i art. 11).
- **Podstawa prawna:** art. 12a–12k ustawy z 24 lipca 2015 r. o kontroli niektórych inwestycji, w szczególności art. 12a ust. 1 pkt 1, art. 12c ust. 1 pkt 1, 4 i 5, art. 12d ust. 3 pkt 7 i ust. 4, art. 12e ust. 4, art. 12f ust. 1 i 5, art. 12h ust. 5 i 8, art. 12k ust. 1 oraz art. 16a [Z]; art. 3 ust. 1 pkt 5–6 i art. 4 tej ustawy (wykaz podmiotów podlegających ochronie; Minister Obrony Narodowej jako organ dla sektora zbrojeniowego) [Z]; rozporządzenie (UE) 2019/452 (obowiązuje do 16 stycznia 2028 r.; tekst niedostępny) [W]; art. 1 ust. 4 i ust. 5 lit. b, art. 2 pkt 1, 5, 7 i 9, art. 3 ust. 1–2, art. 4 ust. 2, 4–5, 7, 9, 11 i 15–17, art. 5 ust. 1–2, art. 6, art. 9, art. 11 ust. 3–5, art. 12 ust. 1 i 3, art. 19 ust. 1 lit. a–b i ust. 2 lit. a–b, d–e, art. 20 ust. 1 i 4, art. 30 ust. 1–3, art. 31, motywy 14, 15 i 20 oraz załączniki I–III rozporządzenia (UE) 2026/1386 z 17 czerwca 2026 r. w sprawie kontroli inwestycji zagranicznych [Z] (tekst EN); art. 10 ust. 1 pkt 2 ustawy z 13 czerwca 2019 r. (koncesja) [Z]; art. 57 ust. 2 pkt 1 ustawy z 5 sierpnia 2010 r. o ochronie informacji niejawnych (bezpieczeństwo przemysłowe) [Z]; § 12 ust. 2 lit. e.

#### § 12 ust. 2 lit. d i e: jedno wezwanie i limit 60 dni wstrzymania, skutek braku informacji; zgoda warunkowa i 30-dniowy termin zawiadomienia organu

Commit `dfec229` · memorandum 1.3.2 · klasa: zalecane

- **Pytanie:** Czy wstrzymanie biegu terminu (lit. d i e) jest dopuszczalne, czy też grozi uznaniem za ukrytą odmowę uruchamiającą mechanizm z ust. 3?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Wstrzymanie biegu terminu jest modyfikacją trybu ustawowego dopuszczalną na podstawie § 2 i gospodarczo uzasadnioną: Rada nie może zająć stanowiska bez informacji, a zgoda na nabycie, które wymaga decyzji organu, byłaby zgodą warunkową. Ryzyko ukrytej odmowy powstaje wtedy, gdy wstrzymanie nie ma granicy: Rada mogłaby żądać coraz to nowych dokumentów i nigdy nie odmówić, blokując zarówno wpis, jak i bieg terminu na wskazanie nabywcy. Sąd oceniłby to jako nadużycie (art. 5 KC) i mógłby przyjąć, że odmowa nastąpiła z chwilą pierwszego kompletnego zgłoszenia — z nieprzewidywalnym skutkiem dla terminów. […]
- **Rekomendacja memorandum:** Ograniczyć wstrzymanie z lit. d do 60 dni i jednego wezwania; w lit. e przewidzieć zgodę warunkową, jeżeli pozostałe przesłanki są spełnione.
- **Podstawa prawna:** art. 300³⁹ § 2–5 KSH [Z]; art. 5 i art. 354 KC [Z]; art. 89 KC (warunek) [Z]; art. 12f ust. 1 i 5 oraz art. 12h ust. 5 i 8 ustawy o kontroli niektórych inwestycji (uprzednie zawiadomienie nabywcy; 30 dni roboczych i 120 dni) [Z].

#### § 12 ust. 2 lit. f: odmowa zgody na zbycie akcji objętych obowiązkiem zbycia nabywcy, który nie przystąpił do umowy wykonawczej

Commit `b99588c` · memorandum 1.5.1, K2 · klasa: konieczne

- **Pytanie:** Czy obowiązek zbycia jako „obowiązek związany z akcją” jest skuteczny wobec nabywców wtórnych i wobec podmiotu prowadzącego rejestr akcjonariuszy; jak go ujawnić w rejestrze?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo — skuteczność wobec Spółki i rejestru tak, wobec nabywcy wtórnego z luką w § 12 ust. 2
- **Dlaczego zmieniono:** Obowiązek zbycia jest świadczeniem akcjonariusza wobec Spółki „określonym w umowie spółki” w rozumieniu art. 300¹ § 3 KSH, a więc obowiązkiem o charakterze korporacyjnym, który obciąża każdoczesnego posiadacza akcji, a nie tylko podpisującego umowę założyciela. Kwalifikacja w § 10 ust. 14 („obowiązek związany z akcją wobec Spółki”) jest prawidłowa i odpowiada kategoriom, które rejestr akcjonariuszy ujawnia z mocy ustawy: „ograniczenia co do rozporządzania akcją” (art. 300³³ § 1 pkt 10 KSH) oraz „postanowienia umowy spółki o związanych z akcją obowiązkach wobec spółki” (pkt 11); umowa spółki może ponadto przewidzieć dodatkowe informacje ujawniane w rejestrze (art. 300³³ § 2 KSH). Podmiot prowadzący rejestr wpisuje te wzmianki na żądanie Spółki, nie później niż w siedem dni, na podstawie przedłożonych dokumentów — tu samej umowy spółki (art. 300³⁴ § 1 i 4 KSH); nie potrzeba do tego zgody akcjonariusza. […]
- **Rekomendacja memorandum:** Zamknąć lukę w § 12 ust. 2: dodać podstawę odmowy zgody dla akcji objętych obowiązkiem zbycia, gdy nabywca nie przystąpił do umowy wykonawczej (oferta i pełnomocnictwo), oraz doprecyzować w § 10 ust. 14, że obowiązek obciąża każdoczesnego posiadacza akcji i że zdarzenia dotyczące Akcjonariusza Funkcjonalnego uruchamiają obowiązek także wobec nabywcy. Przed zawiązaniem uzgodnić z wybranym podmiotem prowadzącym rejestr (notariusz albo dom maklerski) brzmienie wzmianek do wpisu.
- **Podstawa prawna:** art. 300¹ § 3 KSH [Z]; art. 300³³ § 1 pkt 10–11 i § 2 KSH [Z]; art. 300³³ § 3 i art. 594 § 1 pkt 2¹ KSH w brzmieniu od 18.02.2027 r. (Dz.U. 2026 poz. 176) [Z]; art. 300³⁴ § 1 i 4–6 KSH [Z]; art. 300³⁷ § 1 i art. 300³⁸ § 1 KSH [Z]; art. 300³⁹ § 1–2 KSH [Z]; art. 300³⁶ § 4 KSH (forma dokumentowa zbycia) [Z]; art. 353¹ KC [Z]

#### § 12 ust. 4: wyraźna derogacja art. 300^39 § 3-5 KSH (z odesłaniem do § 2) przy odmowie z przyczyny ust. 2 lit. f

Commit `775f392` · memorandum 1.2.1 · klasa: opcjonalne

- **Pytanie:** Czy art. 300³⁹ § 2 KSH („chyba że umowa spółki stanowi inaczej”) pozwala zarówno na modyfikację mechanizmu ustawowego (A: termin 3 miesięcy zamiast miesiąca, zapłata ratalna, Spółka jako możliwy nabywca), jak i na całkowite wyłączenie § 3–6 dla jednej przesłanki odmowy (B)? Gdzie leżą granice tej swobody?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo (A: zgodne; B: zgodne warunkowo)
- **Dlaczego zmieniono:** Konstrukcja art. 300³⁹ KSH jest dwustopniowa: § 1 daje umowie spółki swobodę ograniczenia rozporządzania „w inny sposób” (bez katalogu), a § 2 („jeżeli zbycie akcji jest uzależnione od zgody spółki, stosuje się przepisy § 3–6, chyba że umowa spółki stanowi inaczej”) czyni ustawowy tryb § 3–6 jedynie modelem domyślnym dla wariantu „zgoda spółki”. Skoro umowa mogłaby w ogóle nie sięgać po zgodę spółki i ograniczyć obrót „w inny sposób” (np. zamkniętym kręgiem nabywców), to tym bardziej może — w wariancie ze zgodą — zmodyfikować tryb ustawowy (A) albo wyłączyć go w części (B). Klauzula ta jest zresztą wspólna obu spółkom (art. 182 § 2 KSH zawiera identyczne zastrzeżenie); różnica polega na tym, że w sp. z o.o. model ustawowy angażuje sąd rejestrowy (zezwolenie na zbycie z ważnych powodów, termin i cena ustalane przez sąd — art. 182 § 3–4), a w P.S.A. ustawodawca oddał umowie spółki „termin do wskazania nabywcy, cenę nabycia albo sposób jej określenia oraz termin zapłaty” (art. 300³⁹ § 3 zd. 2), z jednym ograniczeniem modelu domyślnego: „termin do wskazania nabywcy nie może być dłuższy niż miesiąc od dnia zgłoszenia spółce zamiaru zbycia akcji” (§ 3 zd. 4) [Z]. […]
- **Rekomendacja memorandum:** Oba warianty są dopuszczalne; decyzja między nimi jest decyzją o rozkładzie ryzyka, nie o legalności (zob. 1.2.5). Niezależnie od wyboru: utrzymać wyraźne odesłanie do art. 300³⁹ § 2 KSH w każdym miejscu, w którym umowa odstępuje od trybu ustawowego (ust. 3, ust. 4 zd. 1, § 13 ust. 1), aby sąd rejestrowy i podmiot prowadzący rejestr widzieli świadomą derogację.
- **Podstawa prawna:** art. 300³⁹ § 1–6 KSH [Z]; art. 300¹ § 3 i art. 4 § 2¹ KSH [Z]; art. 182 § 2–5 KSH (dla porównania: model sp. z o.o. z udziałem sądu rejestrowego) [Z]; art. 57, art. 353¹ i art. 58 § 1–2 KC [Z]; art. 300⁴⁷ KSH [Z].

#### § 12 ust. 3: zaświadczenie Spółki w 7 dni o powstaniu swobody zbycia jako dokument dla rejestru akcjonariuszy

Commit `67a005d` · memorandum 1.2.2 · klasa: zalecane

- **Pytanie:** Jak każdy z wariantów zadziała wobec podmiotu prowadzącego rejestr akcjonariuszy (czy odmówi wpisu nabywcy spoza Kryterium, jeżeli akcjonariusz zbędzie akcje mimo odmowy) oraz wobec sądu rejestrowego przy rejestracji umowy?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Podmiot prowadzący rejestr działa w obu wariantach tak samo, bo nie bada Kryterium, lecz dokumenty: wpis następuje na żądanie Spółki albo osoby mającej interes prawny (art. 300³⁴ § 1) na podstawie „dokumentów uzasadniających dokonanie wpisu” (§ 4); podmiot „bada treść i formę dokumentów”, „nie ma jednak obowiązku badania zgodności z prawem oraz prawdziwości dokumentów [...], chyba że poweźmie w tym względzie uzasadnione wątpliwości” (§ 5), a „przy dokonywaniu wpisów [...] uwzględnia ograniczenia co do rozporządzania akcją” (§ 6) [Z]. Jeżeli w rejestrze ujawniono, że rozporządzenie wymaga zgody Spółki (art. 300³³ § 1 pkt 10), brak dokumentu zgody jest brakiem formalnym i podmiot odmówi wpisu; zbycie mimo odmowy nie wywoła skutku nabycia (art. 300³⁷ § 1 KSH: nabycie z chwilą wpisu; art. 300³⁸ § 1: wobec Spółki akcjonariuszem jest tylko osoba wpisana). Różnica między wariantami ujawnia się dopiero po odmowie: w wariancie A, po upływie terminu na wskazanie nabywcy albo braku zapłaty, akcjonariusz zbywa „swobodnie” — i wtedy podmiot prowadzący rejestr staje przed pytaniem, jak stwierdzić, że swoboda powstała; bez zaświadczenia Spółki zażąda go albo odmówi wpisu, a spór trafi do sądu. […]
- **Rekomendacja memorandum:** W obu wariantach: (a) ujawnić ograniczenia w rejestrze (1.1.6); (b) w wariancie A dodać obowiązek Spółki wydania w 7 dni zaświadczenia o powstaniu swobody zbycia (art. 300³⁹ § 5 KSH), które stanowi dokument dla rejestru; (c) w umowie o prowadzenie rejestru zastrzec, że wpis nabywcy następuje po przedstawieniu zgody Spółki, potwierdzenia z ust. 7 albo zaświadczenia z lit. b.
- **Podstawa prawna:** art. 300³³ § 1 pkt 10, art. 300³⁷ § 1 i art. 300³⁸ § 1 KSH [Z]; art. 300³⁴ § 1 i 4–6 KSH — dokumenty, zakres badania i uwzględnianie ograniczeń przez podmiot prowadzący rejestr [Z]; art. 300³⁴ § 3 zd. 2 KSH w brzmieniu od 18 lutego 2027 r. (forma zgody na wpis) [Z]; art. 23 ust. 1 ustawy o KRS (zakres kognicji sądu rejestrowego) [Z]; art. 300⁵ KSH (treść umowy) [Z].

#### § 12 ust. 3: 90-dniowy termin końcowy wyceny z płatnością według wartości wskazanej przez Radę, raty bez zgody zbywcy tylko przy 50% z góry, do 12 rat i zastawie albo gwarancji, dzień przeniesienia

Commit `13c7189` · memorandum 1.2.3 · klasa: zalecane

- **Pytanie:** Wariant A: czy zapłata ratalna i pierwsza rata w 30 dni odpowiadają wymogowi określenia w umowie ceny (sposobu jej ustalenia) i terminu zapłaty; czy niezapłacenie pierwszej raty prawidłowo uruchamia swobodę zbycia; jak zastrzeżenie „chyba że nie przyjął oferowanej zapłaty” (art. 300³⁹ § 5 KSH) działa przy zapłacie ratalnej; czy odesłanie do § 17 ust. 4 (raty przewidziane dla spłaty spadkobierców) jest wystarczająco precyzyjne?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Cena: odesłanie do Wartości Godziwej z § 19 (definicja, tryb uzgodnienia, Niezależny Ekspert, wiążący charakter) jest „sposobem określenia” ceny w rozumieniu art. 300³⁹ § 3 zd. 2 KSH („cenę nabycia albo sposób jej określenia oraz termin zapłaty określa umowa spółki”) i spełnia wymóg ustawowy. Termin zapłaty: „30 dni od ostatecznego ustalenia, nie później niż w dniu przeniesienia” jest terminem określonym, ale otwartym z drugiej strony — ustalenie wartości przez Niezależnego Eksperta nie ma w § 19 terminu końcowego, więc akcjonariusz może czekać miesiącami bez prawa swobodnego zbycia; sąd mógłby uznać, że umowa nie określa terminu zapłaty dostatecznie, a wówczas § 3 zd. 3 („w braku tych postanowień akcja może być zbyta bez ograniczenia”) otwiera swobodę zbycia od razu [Z] co do brzmienia; czy niedostatecznie określony termin jest „brakiem postanowień”, pozostaje kwestią wykładni [?]. Raty: KSH nie zabrania rozłożenia ceny na raty, ale § 5 mówi o nieuiszczeniu „ceny”; projekt słusznie precyzuje, że swobodę zbycia uruchamia brak zapłaty pierwszej raty w terminie — to postanowienie „stanowi inaczej” w rozumieniu § 2 i jest skuteczne. […]
- **Rekomendacja memorandum:** Przeredagować ust. 3: (a) termin końcowy: jeżeli Wartość Godziwa nie zostanie ostatecznie ustalona w 90 dni od wskazania nabywcy, nabywca płaci pierwszą ratę od wartości wskazanej przez Radę z wyrównaniem po ustaleniu, a w braku zapłaty powstaje swoboda zbycia; (b) raty tylko za zgodą zbywcy albo, bez jego zgody, wyłącznie gdy pierwsza rata wynosi co najmniej 50% ceny, liczba rat nie przekracza 12, a zabezpieczeniem jest zastaw rejestrowy na nabywanych akcjach albo gwarancja bankowa; (c) wyraźne określenie dnia przeniesienia (wpis w rejestrze po zapłacie pierwszej raty).
- **Podstawa prawna:** art. 300³⁹ § 2, 3 i 5 KSH [Z]; art. 300⁴⁷ KSH [Z]; art. 327–329 KC (zastaw na prawach) [Z] oraz ustawa o zastawie rejestrowym [W]; art. 300³³ § 1 pkt 6 i art. 300³⁷ § 1–2 KSH (ujawnienie zastawu w rejestrze; od 18 lutego 2027 r. zastaw rejestrowy powstaje z wpisem do rejestru zastawów bez wpisu w rejestrze akcjonariuszy) [Z]; art. 455 i art. 476 KC [Z].

#### § 12 ust. 4: wyraźna derogacja art. 300^39 § 3-5 KSH przy odmowie z powodu Niedopuszczalnego Nabywcy, wstrzymanie terminu nie jest odmową

Commit `ed56b6f` · memorandum 1.2.7 · klasa: zalecane

- **Pytanie:** § 12 ust. 4 zdanie pierwsze: przy odmowie z powodu Niedopuszczalnego Nabywcy obowiązek wskazania innego nabywcy nie powstaje, bo przeszkoda wynika z prawa. Czy to ujęcie jest spójne z art. 300³⁹ KSH, czy wymaga wyraźnej derogacji jak w ust. 3?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Merytorycznie ujęcie jest trafne: jeżeli nabycie przez planowanego nabywcę jest zakazane przez prawo, umowa zbycia byłaby nieważna (art. 58 § 1 KC), a odmowa zgody Spółki ma charakter deklaratoryjny; nie ma powodu, by Spółka szukała nabywcy zastępczego, skoro zbywca może po prostu wskazać innego (ust. 6). Technicznie jednak art. 300³⁹ § 3 zd. 1 KSH („jeżeli spółka odmawia zgody na zbycie akcji, powinna wskazać innego nabywcę”) nie różnicuje przyczyn odmowy: każda odmowa uruchamia obowiązek wskazania nabywcy, „chyba że umowa spółki stanowi inaczej” (§ 2). Zdanie „obowiązek nie powstaje, ponieważ przeszkoda wynika z prawa” jest uzasadnieniem, nie postanowieniem umownym „stanowiącym inaczej”; ostrożny sąd albo podmiot prowadzący rejestr może uznać, że brak wyraźnej derogacji oznacza stosowanie modelu ustawowego, a wtedy brak wskazania nabywcy w miesiąc dawałby — paradoksalnie — swobodę zbycia (choć nadal ograniczoną przepisami sankcyjnymi). […]
- **Rekomendacja memorandum:** Dodać wyraźną derogację w ust. 4 zd. 1.
- **Podstawa prawna:** art. 300³⁹ § 2–5 KSH [Z]; art. 58 § 1 KC [Z]; art. 1 lit. f–g i art. 2 ust. 1–2 rozporządzenia (UE) nr 269/2014 (zamrożenie środków obejmujące „stocks and shares”; zakaz udostępniania) [Z] (tekst EN, pierwotny, bez konsolidacji); rozporządzenie 833/2014 [W]; art. 1 pkt 1–2 w zw. z art. 2 ust. 1 ustawy z 13 kwietnia 2022 r. o szczególnych rozwiązaniach w zakresie przeciwdziałania wspieraniu agresji na Ukrainę (lista krajowa prowadzona przez ministra właściwego do spraw wewnętrznych; odpowiednie stosowanie środków z art. 2 rozporządzenia 269/2014 — zamrożenie i zakaz udostępniania środków — oraz z art. 9 — zakaz udziału w obchodzeniu tych środków) [Z].

#### § 12 ust. 7: potwierdzenie wyniku weryfikacji przez Radę Dyrektorów (niebędące zgodą) jako dokument dla rejestru przy nabyciach zwolnionych ze zgody Spółki

Commit `7c2d9db` · memorandum 1.2.8 · klasa: zalecane

- **Pytanie:** § 12 ust. 7: zgody Spółki nie wymaga zbycie w postępowaniu egzekucyjnym ani nabycie w wykonaniu prawa pierwszeństwa, przyłączenia, przymusowego współzbycia, zwrotnego zbycia i w Kwalifikowanej Rundzie — przy zachowaniu wymogu Kryterium (poza egzekucją). Czy wymóg Kryterium przy tych nabyciach jest skuteczny, skoro nie ma tam zgody Spółki, a przy drag-along weryfikuje się go przed zawiadomieniem?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Wymóg Kryterium bez zgody Spółki jest skuteczny jako ograniczenie „w inny sposób” (art. 300³⁹ § 1 KSH): zamknięty krąg nabywców jest samodzielnym ograniczeniem rozporządzania, niezależnym od mechanizmu zgody, i wiąże strony transakcji oraz — po ujawnieniu (pkt 10) — podmiot prowadzący rejestr. Słabością jest brak dokumentu: skoro nie ma zgody Spółki, podmiot prowadzący rejestr nie ma czego żądać i nie jest w stanie sam ocenić Kryterium; w praktyce wpisze nabywcę na podstawie umowy, a naruszenie ujawni się później. Przy Kwalifikowanej Rundzie problem nie występuje (nabycie następuje przez objęcie akcji nowej emisji na podstawie uchwały Walnego Zgromadzenia — emisja stanowi zmianę umowy spółki, art. 300¹⁰³ KSH — i wpisu do KRS; objęcie jest wyłączone spod zasady wpisu konstytutywnego w rejestrze akcjonariuszy, art. 300³⁷ § 2 KSH; […]
- **Rekomendacja memorandum:** Dodać w ust. 7 potwierdzenie Rady jako dokument dla rejestru; nie wprowadzać mechanizmu wskazania nabywcy w egzekucji na wzór art. 185 KSH (brak podstawy ustawowej w P.S.A.); ryzyko egzekucyjne ograniczać przez wymóg zgody Spółki na obciążenie akcji.
- **Podstawa prawna:** art. 300³⁹ § 1 KSH („w inny sposób je ograniczyć”) i § 6 [Z]; art. 300³³ § 1 pkt 10, art. 300³⁴ § 6 i art. 300³⁷ § 1–2 KSH [Z]; art. 300¹⁰³–300¹⁰⁵ KSH (emisja i objęcie akcji nowej emisji) [Z]; art. 910 i art. 911³ KPC (egzekucja z praw majątkowych; zajęcie ujawniane w rejestrze akcjonariuszy) [Z].

#### § 12 ust. 10: obowiązek Rady Dyrektorów ujawnienia ograniczeń i obowiązków w rejestrze akcjonariuszy w 7 dni, wpis nabywcy po przedstawieniu zgody albo potwierdzenia z ust. 7

Commit `5593c71` · memorandum 1.1.6 · klasa: zalecane

- **Pytanie:** Czy dla skuteczności Kryterium wobec osób trzecich potrzebne jest ujawnienie ograniczenia w rejestrze akcjonariuszy, a jeżeli tak — w jakiej formie i na czyj wniosek?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Kryterium wiąże każdego akcjonariusza z mocy umowy spółki niezależnie od wpisu; wpis nie jest przesłanką ważności ograniczenia. Ujawnienie jest jednak potrzebne dla skuteczności praktycznej: podmiot prowadzący rejestr „przy dokonywaniu wpisów [...] uwzględnia ograniczenia co do rozporządzania akcją” (art. 300³⁴ § 6 KSH), więc znając ograniczenie z pkt 10 zażąda przy wpisie nabywcy dokumentu zgody Spółki i odmówi wpisu bez niego, a nabycie następuje dopiero z chwilą wpisu (art. 300³⁷ § 1 KSH) [Z]. Bez adnotacji podmiot ten może wpisać nabywcę na podstawie samej umowy zbycia. […]
- **Rekomendacja memorandum:** Dodać w § 12 ustęp nakładający na Radę Dyrektorów obowiązek zgłoszenia do rejestru ograniczeń i obowiązków z § 11, § 12, § 13, § 10 i § 17 w terminie 7 dni od zawarcia umowy o prowadzenie rejestru i od każdego zdarzenia uzasadniającego wpis (zgodnie z art. 300³³ § 3 KSH w brzmieniu od 18 lutego 2027 r.); zawrzeć w tej umowie zobowiązanie podmiotu prowadzącego rejestr do żądania zgody Spółki albo potwierdzenia z § 12 ust. 7 (zob. 1.2.8) przed każdym wpisem nabywcy.
- **Podstawa prawna:** art. 300³¹–300³⁴ KSH, w szczególności art. 300³³ § 1 pkt 10 („ograniczenia co do rozporządzania akcją”) i pkt 11 („postanowienia umowy spółki o związanych z akcją obowiązkach wobec spółki”), § 2 (dodatkowe informacje ujawniane na podstawie umowy spółki) oraz art. 300³⁴ § 1 i 4–6 (wpis na żądanie spółki albo osoby mającej interes prawny; dokumenty; uwzględnianie ograniczeń) [Z]; art. 300³⁷ § 1 i art. 300³⁸ § 1 KSH (skutek wpisu) [Z]; art. 300³² § 1 KSH (umowa o prowadzenie rejestru) [Z]; art. 300³³ § 3 i art. 594 § 1 pkt 2¹ KSH w brzmieniu obowiązującym od 18 lutego 2027 r. (Dz.U. 2026 poz. 176) [Z].

### § 13. Okres Ograniczenia Zbywania Akcji Założycieli

#### § 13 ust. 1: derogacja ograniczona do art. 300^39 § 3-5 KSH, ujawnienie Okresu Ograniczenia z datą końcową; § 12 ust. 7, § 14 ust. 6: przeniesienie do podmiotu kontrolowanego bez zgody Spółki i prawa pierwszeństwa

Commit `171d699` · memorandum 1.2.6 · klasa: zalecane

- **Pytanie:** Lock-up (§ 13 ust. 1): Założyciel Pierwotny przez 12 miesięcy od wpisu Spółki (Założyciel Serii F — od Dnia Przyznania) nie może zbyć ani obciążyć akcji bez zgody Walnego Zgromadzenia (75% Głosów Uprawnionych w Sprawie); na podstawie art. 300³⁹ § 2 KSH w tym okresie wyłączono § 3–6 i mechanizm z § 12 ust. 3. Czy taka derogacja na czas określony jest dopuszczalna i jak ją ujawnić w rejestrze? Czy wyjątki z § 13 ust. 2 (runda, tag-along i drag-along, zwrotne zbycie, przeniesienie do podmiotu w całości kontrolowanego) wymagają jeszcze zgody Spółki z § 12?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Derogacja czasowa jest najbezpieczniejszym zastosowaniem § 2: ograniczenie ma termin końcowy, dotyczy tylko Założycieli (którzy sami je przyjmują przy zawiązaniu), a wyjątki z ust. 2 zachowują drogi wyjścia. Osadzenie lock-upu w art. 300³⁹ § 1 (a nie w zobowiązaniu obligacyjnym z art. 57 § 2 KC) czyni go skutecznym wobec Spółki i rejestru, nie tylko między stronami. Ujawnienie: adnotacja przy akcjach każdego Założyciela Pierwotnego „ograniczenie rozporządzania: zgoda Walnego Zgromadzenia do dnia [data = wpis + 12 miesięcy], § 13 umowy”; dla akcji serii F adnotacja przy wpisie emisji z datą liczoną od Dnia Przyznania (Spółka musi ją podać podmiotowi prowadzącemu rejestr). […]
- **Rekomendacja memorandum:** Zmienić „§ 3–6” na „§ 3–5” w § 13 ust. 1 (§ 12 ust. 4 odsyła tylko do mechanizmu z ust. 3 i nie wymaga zmiany); dopisać przeniesienie do podmiotu w całości kontrolowanego do wyłączeń zgody i prawa pierwszeństwa; ujawnić lock-up w rejestrze z datą końcową.
- **Podstawa prawna:** art. 300³⁹ § 1–2 i § 6 KSH [Z]; art. 57 § 2 KC [Z]; art. 300³³ § 1 pkt 10 i § 2 KSH [Z]; art. 300⁵ KSH [Z]; art. 910 i art. 911³ KPC [Z].

#### § 13 ust. 2 lit. a, § 33 ust. 2: wyjątek dla zbycia wtórnego na rzecz inwestora Rundy zatwierdzonego w uchwale kierunkowej, bez prawa pierwszeństwa, z zachowaniem zwrotnego zbycia; zgoda z § 11 ust. 6 w uchwale kierunkowej

Commit `6870417` · memorandum 3.3.3 · klasa: zalecane

- **Pytanie:** Jak pogodzić Kwalifikowaną Rundę z prawem poboru (§ 32 ust. 5, § 25 ust. 2) i z wymogiem Kryterium wobec inwestorów, a także z lock-upem założycieli (§ 13 ust. 2 lit. a)?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** *Prawo poboru.* Każda emisja, także w Rundzie, rodzi prawo poboru wszystkich dotychczasowych akcjonariuszy proporcjonalnie do posiadanych akcji, ustalane na dzień uchwały o emisji; skierowanie akcji do inwestora wymaga pozbawienia go w całości albo w części uchwałą 4/5 w interesie Spółki (art. 300¹⁰⁶ § 1–2 [Z]), a akcje nieobjęte w wykonaniu prawa poboru Rada oferuje według uznania po cenie nie niższej niż emisyjna (§ 6). § 32 ust. 5 poprawnie to zastrzega, a przy strukturze 50/20/10/10/10 koalicje 4/5 (A+B+jeden z C/D/E albo A+C+D+E) pokrywają się z koalicjami 75%, więc runda nie tworzy dodatkowej blokady; po emisjach serii F i P układ się zmieni. Pro-rata z ust. 4 lit. e jest podzbiorem ustawowego prawa poboru: ustawowe prawo jest szersze (obejmuje także uczestników programu i Założycieli Serii F), więc przy kolejnej rundzie trzeba pozbawić prawa poboru „w części” — wszystkich poza inwestorem korzystającym z pro-rata — każdorazowo większością 4/5; stąd znaczenie rozszerzenia ust. 3 (3.3.1). Prawo poboru w P.S.A. jest jednak dyspozytywne: art. 300¹⁰⁶ § 1 przyznaje je, „jeżeli umowa spółki lub uchwała akcjonariuszy nie stanowią inaczej” [Z]. […]
- **Rekomendacja memorandum:** Doprecyzować § 13 ust. 2 lit. a i dodać w § 32 ust. 2, że uchwała kierunkowa może zawierać zgodę z § 11 ust. 6 oraz zatwierdzenie transakcji wtórnych z inwestorami Rundy. Rozważyć (decyzja Założycieli) wykorzystanie art. 300¹⁰⁶ § 1 KSH: zapisanie w umowie, że prawo poboru nie przysługuje w zakresie akcji obejmowanych przez inwestorów wskazanych w uchwale kierunkowej, co usuwa odrębną uchwałę 4/5 z każdej rundy; w zamian uchwała kierunkowa (75%) staje się jedyną blokadą.
- **Podstawa prawna:** art. 300¹⁰⁶ § 1–3 i 6 KSH [Z] (§ 1: prawo poboru przysługuje, „jeżeli umowa spółki lub uchwała akcjonariuszy nie stanowią inaczej”); art. 300³⁹ § 1–2 KSH [Z]; § 11 ust. 5–6, § 12 ust. 7, § 14 ust. 1.

### § 14. Prawo pierwszeństwa nabycia akcji

#### § 14 ust. 1 i 4: wygaśnięcie oferty przy odmowie zgody, wskazanie nabywcy zastępuje prawo pierwszeństwa, 60 dni od upływu terminów z ust. 3, wymóg Kryterium wobec nabywcy

Commit `8dce83a` · memorandum 1.3.4 · klasa: zalecane

- **Pytanie:** Kolejność prawa pierwszeństwa (§ 14) i zgody Spółki (§ 12): czy dopuszczenie oferty równoczesnej ze zgłoszeniem nie koliduje z wymogiem, by oferta odzwierciedlała warunki uzgodnione z nabywcą, i czy 20-dniowe terminy przyjęcia oferty oraz 60-dniowe okno zbycia są wykonalne?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Oferta równoczesna nie koliduje z wymogiem odzwierciedlenia warunków, bo zgłoszenie z § 12 ust. 1 już zawiera cenę i istotne warunki uzgodnione z nabywcą; oferta jest tym samym zestawem warunków skierowanym do innych adresatów. Kolizja pojawia się w innym miejscu: jeżeli Spółka odmówi zgody z powodu Kryterium i uruchomi wskazanie nabywcy (ust. 3), równolegle złożona oferta pierwszeństwa wisi w próżni — projekt nie mówi, czy wygasa, czy wskazany nabywca ma pierwszeństwo przed akcjonariuszami. Trzeba to rozstrzygnąć: odmowa zgody powoduje wygaśnięcie oferty (terminy z ust. 3 nigdy nie zaczynają biec), a wskazanie nabywcy przez Spółkę zastępuje prawo pierwszeństwa. […]
- **Rekomendacja memorandum:** Doprecyzować: skutek odmowy zgody dla oferty, początek biegu 60 dni, wymóg Kryterium w ust. 4.
- **Podstawa prawna:** art. 300³⁹ § 1 KSH [Z]; art. 66 § 1–2 KC (oferta i termin związania) [Z]; art. 300⁴⁷ KSH [Z].

#### § 14 ust. 3: nabycie przez Spółkę w granicach upoważnienia WZ (art. 300^47 § 1 pkt 2 i § 2 KSH) albo wskazanie w 20 dni samodzielnego nabywcy spełniającego Kryterium

Commit `8fc2c03` · memorandum 1.3.5 · klasa: zalecane

- **Pytanie:** § 14 ust. 3: Spółka może przyjąć ofertę, „o ile nabycie akcji własnych jest prawnie dopuszczalne” — czy odesłanie to wystarcza w świetle art. 300⁴⁷ KSH?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Odesłanie jest prawnie wystarczające (nie tworzy pozoru uprawnienia sprzecznego z ustawą), ale praktycznie puste. Art. 300⁴⁷ § 1 KSH dopuszcza nabycie akcji własnych w zamkniętych przypadkach; dla prawa pierwszeństwa właściwy jest pkt 2: nabycie „na podstawie i w granicach upoważnienia udzielonego w uchwale akcjonariuszy” [Z]. Nabycie w tym trybie wymaga łącznie (§ 2): pełnego pokrycia nabywanych akcji, nieprzekroczenia 25% wszystkich akcji (łącznie z akcjami nabytymi z innych tytułów) oraz tego, by łączna cena nabycia z kosztami nie była wyższa od kwoty „kapitału rezerwowego, utworzonego w tym celu z kwoty, o której mowa w art. 300¹⁵ § 2” (zysk i kapitały rezerwowe z zysku dostępne do wypłaty); do zapłaty ceny stosuje się odpowiednio art. 300¹⁵ § 4–6, w tym test wypłacalności (§ 3). […]
- **Rekomendacja memorandum:** Uzupełnić ust. 3 o prawo Spółki do wskazania samodzielnego nabywcy w terminie 20 dni i o odesłanie do upoważnienia Walnego Zgromadzenia; po zawiązaniu podjąć uchwałę upoważniającą.
- **Podstawa prawna:** art. 300⁴⁷ § 1 pkt 2, § 2–3 i § 9 KSH (nabycie na podstawie i w granicach upoważnienia udzielonego w uchwale akcjonariuszy; warunki: pełne pokrycie, próg 25%, celowy kapitał rezerwowy; osoba trzecia działająca na rachunek spółki) [Z]; art. 300¹⁵ § 2 i § 4–6 KSH (kwota dostępna do wypłaty i test wypłacalności) [Z]; art. 362 § 1 pkt 8 KSH (dla porównania: pięcioletni limit upoważnienia w spółce akcyjnej) [Z]; § 25 ust. 1 lit. j.

### § 16. Prawo przymusowego współzbycia

#### § 16 ust. 5: ochrona serii inwestorskiej przy przymusowym współzbyciu (zgoda większości serii albo okres ochronny z ceną minimalną), podział ceny według uprzywilejowania

Commit `b876db3` · memorandum 4.4.1, 4.4.2 brzmienie IV · klasa: zalecane, zalecane — odstępstwo od reguły „zgodne warunkowo → zalecane” nie jest potrzebne; brzmienia podajemy, bo zmiany są proste i jednoznaczne

*Pytanie 4.4.1.*

- **Pytanie:** Które postanowienia (Kryterium, mechanizm przy odmowie zgody, zwrotne zbycie, drag-along 75 %, Sprawy Zastrzeżone 75 %, ograniczenia finansowania) w Państwa doświadczeniu budzą zastrzeżenia funduszy na etapie seed/serii A i co zwykle jest przedmiotem negocjacji?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo — żadne z ocenianych postanowień nie jest prawnie wadliwe; sześć z nich odbiega od standardu rynkowego w sposób, który wydłuży negocjacje albo zawęzi krąg funduszy
- **Dlaczego zmieniono:** Zastrzeżenia omawiamy w kolejności, w jakiej zwykle pojawiają się w term sheecie, z rozróżnieniem trzech grup funduszy: (G) fundusze generalistyczne działające jako ASI z kapitałem PFR/BGK/EIF i przewagą polskich albo unijnych inwestorów — w programach PFR Ventures udział PFR w kapitalizacji funduszu wynosi maksymalnie 80% (PFR Starter: bilety do 5 mln PLN, przede wszystkim spółki przed pierwszą komercyjną sprzedażą, wkład prywatny min. 20%, `pfr_pfrv_starter.txt`) albo do 60% (PFR KOFFI: etap wzrostu, bilety od 4 mln PLN, min. 85% wartości portfela w spółkach z siedzibą w Polsce, wkład prywatny min. 40%, `pfr_pfrv_koffi.txt`; PFR Otwarte Innowacje w strukturze standardowej: bilety 5–70 mln PLN, program także „w obszarze zaawansowanych technologii obronnych i dual-use”, wkład prywatny min. 40%, `pfr_pfrv_otwarte_innowacje.txt`) [Z]; przy KOFFI PFR wymaga rejestracji ZASI najpóźniej przy podpisaniu umowy i oczekuje zdywersyfikowanej struktury LP (`pfr_pfrv_koffi.txt`), a przy Starterze due diligence obejmuje ryzyka ze struktury inwestorskiej, „m.in. stopnia dywersyfikacji inwestorskiej Funduszu” (`pfr_pfrv_starter.txt`) [Z], więc największym LP takiego funduszu jest polski podmiot publiczny, a pozostali LP są rozproszeni. Inaczej w modelach koinwestycyjnych: w PFR Biznest kapitalizację funduszu tworzą tylko PFR i zarządzający, a min. 40% wartości każdej inwestycji wnoszą inwestorzy prywatni, w tym aniołowie biznesu, poza funduszem (`pfr_pfrv_biznest.txt`); w modelu koinwestycyjnym PFR OI wkład PFR może sięgać 97% kapitalizacji funduszu, a prywatne min. 40% wnoszą koinwestorzy dobierani „deal by deal” bezpośrednio do spółki, każdy za akceptacją PFR OI (`pfr_pfrv_otwarte_innowacje.txt`) [Z] — tu aniołowie i koinwestorzy stają się akcjonariuszami Spółki obok funduszu, więc Kryterium i zgoda Rady dotyczą każdego z nich osobno; […]
- **Rekomendacja memorandum:** Rozstrzygnąć przed rundą, nie w jej trakcie, cztery punkty sporne z każdym funduszem: test Kryterium dla funduszy (§ 11 ust. 14 i 15), przeniesienia dozwolone (§ 12), ochrona serii inwestorskiej przy drag (§ 16) i katalog spraw wymagających zgody serii (§ 32 ust. 4). Pozostałe punkty zostawić do term sheetu. Brzmienia w odpowiedzi na pytanie 4.4.2. Wybór, czy szukać inwestora w grupie G/D (mniejsze zmiany), czy także Z (zmiany w § 21 ust. 3 i wariant A w § 12 ust. 3), należy do Założycieli.
- **Podstawa prawna:** art. 300³⁹ § 1–6 KSH [Z]; art. 300⁴⁷ KSH [Z]; art. 300¹⁰³–300¹⁰⁷ KSH [Z]; art. 300¹⁰⁶ § 2 KSH (pozbawienie prawa poboru) [Z]; art. 300²⁵ § 1–2 KSH (akcje uprzywilejowane; katalog otwarty: uprzywilejowanie „może dotyczyć w szczególności prawa głosu, prawa do dywidendy lub podziału majątku w przypadku likwidacji spółki”) [Z]; art. 300²⁸ § 1–2 KSH (uprawnienia indywidualne oznaczonego akcjonariusza, „w szczególności uprawnienie do powołania lub odwołania członków zarządu lub rady nadzorczej”, wygasające najpóźniej z utratą statusu akcjonariusza, „chyba że umowa spółki stanowi inaczej”) [Z]; art. 300¹⁰⁴ § 1 pkt 2 KSH (uprzywilejowanie akcji nowej emisji w uchwale o emisji) [Z]; art. 2 pkt 6 i 24, art. 5 i art. 9 ust. 1–4 i 7 rozporządzenia (UE) 2021/697 (EDF) [Z]; art. 2 pkt 1, 5 i 7, art. 4 ust. 2, 9 i 15, art. 5 ust. 1–2, art. 15 ust. 1 lit. b i ust. 3, art. 19 ust. 2 lit. e oraz motywy 14–15 rozporządzenia (UE) 2026/1386 (kontrola inwestycji zagranicznych, stosowane od 17 stycznia 2028 r., art. 31) [Z] (tekst EN); art. 2 ust. 2 pkt 1 ustawy z 2018 r. o przeciwdziałaniu praniu pieniędzy oraz finansowaniu terroryzmu (beneficjent rzeczywisty: osoba fizyczna sprawująca kontrolę, w tym mająca „więcej niż 25% ogólnej liczby udziałów lub akcji” albo głosów, a w braku takiej osoby — osoba na wyższym stanowisku kierowniczym) [Z]; ustawa o kontroli niektórych inwestycji [W]; praktyka rynkowa: wzorce NVCA po aktualizacji z 2 października 2025 r. (`web_nvca_2025_press.txt`, `web_nvca_2025_foley.txt`) [Z], omówienia PFR Startup (`web_pfr_umowa_inwestycyjna.txt`, `pfr_startup_umowa_inwestycyjna.txt`, pfr_startup_term_sheet.txt) [Z], strony programów PFR Ventures (`pfr_pfrv_starter.txt`, `pfr_pfrv_biznest.txt`, `pfr_pfrv_otwarte_innowacje.txt`, `pfr_pfrv_koffi.txt`) [Z], wzorce BVCA i treść wzorów term sheet PFR Ventures (same wzory nie zostały pobrane, `pfr_pfrv_feng_dokumentacja.txt`) [W].

*Pytanie 4.4.2.*

- **Pytanie:** Jakie zmiany ułatwiłyby dostosowanie umowy do rundy bez naruszenia jej założeń (bezpieczeństwo właścicielskie, kontrola eksportu, mechanizm zwrotnego zbycia)?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo — założenia umowy da się utrzymać w całości; potrzebne są cztery zmiany w umowie spółki przed rundą i przeniesienie reszty do dokumentów rundy
- **Dlaczego zmieniono:** Kryterium zmian jest jedno: nic, co decyduje o dostępie do EDF, EUDIS, DIANA/NIF i koncesji, nie może zostać osłabione (warunki EDF: siedziba i „zarządcze struktury wykonawcze” w Unii lub w państwie stowarzyszonym oraz brak „kontroli niestowarzyszonego państwa trzeciego lub podmiotu z niestowarzyszonego państwa trzeciego”, art. 9 ust. 1–3 rozporządzenia 2021/697, z derogacją za gwarancjami zatwierdzonymi przez państwo członkowskie lub stowarzyszone siedziby z art. 9 ust. 4 [Z]; państwa stowarzyszone to według art. 5 członkowie EFTA należący do EOG, których rozporządzenie nie wymienia z nazwy [Z], w praktyce obecnie Norwegia, `web_edf_gowling.txt` [Z]; warunek NIF: siedziba w jednym z 24 państw NATO będących jego inwestorami, `web_nif_about.txt` [Z]). Te założenia to: (i) kontrola nad Spółką pozostaje w rękach osób i podmiotów z UE/EOG/NATO, a — jeżeli Założyciele przyjmą decyzję D6 — z UE/EOG; (ii) dostęp do Kluczowej Własności Intelektualnej spoza UE/NATO tylko za zgodą Rady po analizie eksportowej (§ 27 ust. 6, § 28); […]
- **Rekomendacja memorandum:** Wprowadzić zmiany A.1–A.4 przed pierwszym term sheetem (A.1 i A.3 warunkują w praktyce rozmowę z funduszami D i Z); A.5 i A.6 zależnie od decyzji Założycieli o kręgu inwestorów; A.7 po stanowisku kancelarii. Resztę zostawić dokumentom rundy. Brzmienia poniżej są sugestią do weryfikacji przez uprawnionego prawnika, w szczególności co do art. 300³⁹ § 2 KSH (wyłączenie zgody Spółki dla kategorii przeniesień) i ujawnienia w rejestrze akcjonariuszy.
- **Podstawa prawna:** art. 300³⁹ § 1–2 KSH („chyba że umowa spółki stanowi inaczej”) [Z]; art. 300²⁵ § 1–2 i art. 300²⁸ § 1–2 KSH [Z]; art. 300³³ § 1 pkt 4 i 10 KSH (rejestr akcjonariuszy zawiera „rodzaj danej akcji i uprawnienia szczególne z akcji” oraz „ograniczenia co do rozporządzania akcją”) [Z]; art. 300¹⁰³ KSH (emisja na podstawie postanowień umowy „przewidujących maksymalną liczbę akcji i termin ich emisji” bez trybu zmiany umowy) [Z]; art. 300¹⁰⁴ § 1 pkt 2 KSH [Z]; art. 300¹⁰⁶ § 1–2 KSH (prawo poboru, „jeżeli umowa spółki lub uchwała akcjonariuszy nie stanowią inaczej”; pozbawienie uchwałą większością 4/5) [Z]; art. 2 pkt 6 i 24, art. 5 i art. 9 ust. 1–4 i 7 rozporządzenia (UE) 2021/697 [Z]; art. 2 pkt 1, 5 i 7, art. 4 ust. 1, 2, 9 i 15 lit. a–c, art. 5 ust. 1–2, art. 6, art. 11 ust. 3 i 5, art. 20 ust. 4 lit. a, art. 30–31, motywy 14–15 i 20, zał. I pkt 1–3 i zał. II pkt 14 rozporządzenia (UE) 2026/1386 [Z] (tekst EN); rozporządzenie (UE) 2021/821 (unijny system kontroli wywozu, pośrednictwa, pomocy technicznej, tranzytu i transferu produktów podwójnego zastosowania; do jego zał. I odsyła art. 4 ust. 15 lit. a rozporządzenia 2026/1386) [Z] (tekst EN, konsolidacja na 26.05.2023 r.); art. 12a ust. 1 pkt 1, art. 12c ust. 1 pkt 1 i 5, ust. 4–5 oraz art. 12d ust. 3 pkt 7 i ust. 4 ustawy o kontroli niektórych inwestycji [Z]; art. 2 ust. 2 pkt 1 ustawy AML [Z].

### § 17. Dziedziczenie akcji

#### § 17 ust. 2: dłużnik spłaty (nabywca, solidarnie Spółka), 3-miesięczny termin wskazania nabywcy, ścieżka rezerwowa przez nabycie akcji własnych albo umorzenie przymusowe z przesłanką niewstąpienia

Commit `127376a` · memorandum 1.6.1, K5 · klasa: konieczne

- **Pytanie:** Czy § 17 prawidłowo wykorzystuje art. 300⁴¹ § 1 KSH (ograniczenie albo wyłączenie wstąpienia pod warunkiem określenia zasad spłaty), a warunki spłaty (100 % Wartości Godziwej, raty z § 17 ust. 4) są określone wystarczająco, aby ograniczenie było skuteczne?
- **Ocena brzmienia 0.9.4-C:** ryzyko — konstrukcja poprawna, ale warunki spłaty nie wskazują dłużnika ani ścieżki, gdy nabywcy nie ma
- **Dlaczego zmieniono:** Art. 300⁴¹ § 1 KSH pozwala umową ograniczyć lub wyłączyć wstąpienie spadkobierców, pod warunkiem określenia warunków spłaty spadkobierców niewstępujących „pod rygorem bezskuteczności ograniczenia lub wyłączenia”. Projekt (a) wyraźnie powołuje przepis i deklaruje ograniczenie (ust. 1 zdanie pierwsze — to poprawia wadę wskazaną w audycie do wersji 0.8), (b) określa przesłanki niewstąpienia, (c) określa wysokość spłaty (100% Wartości Godziwej na dzień otwarcia spadku), (d) odsyła do zasad ratalnych ust. 4 (dawne błędne odesłanie do ust. 5 zostało poprawione). Konstrukcja jest trafna także w tym, że nie próbuje wyłączyć samego dziedziczenia (akcje przechodzą na spadkobiercę ex lege, art. 922 KC), lecz tylko wstąpienie do Spółki — spadkobierca niewstępujący jest właścicielem akcji bez statusu członkowskiego i ma roszczenie o spłatę; to model ugruntowany na tle art. 183 § 1 KSH, którego brzmienie art. 300⁴¹ § 1 zdanie pierwsze i drugie powtarza dosłownie, więc dorobek orzeczniczy do sp. z o.o. jest przenoszalny; nabycie w drodze spadku nie wymaga wpisu konstytutywnego (art. 300³⁷ § 2 KSH), lecz „wobec spółki uważa się za akcjonariusza tylko tę osobę, która jest wpisana do rejestru akcjonariuszy” (art. 300³⁸ § 1 KSH), co daje Spółce narzędzie do niedopuszczenia spadkobiercy niewstępującego do wykonywania praw. […]
- **Rekomendacja memorandum:** Uzupełnić ust. 2 i ust. 4 o dłużnika spłaty (nabywca, a solidarnie Spółka), termin wskazania nabywcy, bezwarunkowy termin pierwszej raty i ścieżkę rezerwową przez nabycie akcji własnych albo umorzenie, z wyraźnym określeniem niewstąpienia jako przesłanki umorzenia (art. 300⁴⁵ § 1 KSH); dodać regułę dla akcji za wkład pracy (art. 300⁴¹ § 1 zdanie trzecie i § 2 KSH). Rozważyć automatyczne zwolnienie akcji niezwolnionych przy śmierci (decyzja Założycieli).
- **Podstawa prawna:** art. 300⁴¹ § 1–2 KSH [Z]; art. 300⁴⁴–300⁴⁶ KSH (umorzenie przymusowe i automatyczne, spłata nie niższa od wartości godziwej) [Z]; art. 300¹⁵ § 2 i 4–6 KSH [Z]; art. 300⁴⁷ § 1–2 KSH [Z]; art. 300³⁷ § 2 i art. 300³⁸ § 1 KSH [Z]; art. 922 § 1, art. 924–925, art. 1025 § 2, art. 1027 KC [Z]; art. 21 ust. 1 i art. 64 Konstytucji RP [Z]; art. 183 § 1 KSH (analogia; brzmienie identyczne) [Z] i orzecznictwo do sp. z o.o. [W]

#### § 17 ust. 2: wstąpienie spadkobierców z akcji za wkład pracy lub usług według § 17 zamiast zgody z art. 300^41 § 2 KSH, proporcjonalne pomniejszenie spłaty

Commit `6da7955` · memorandum 1.6.1, K6 · klasa: konieczne

- **Pytanie:** Czy § 17 prawidłowo wykorzystuje art. 300⁴¹ § 1 KSH (ograniczenie albo wyłączenie wstąpienia pod warunkiem określenia zasad spłaty), a warunki spłaty (100 % Wartości Godziwej, raty z § 17 ust. 4) są określone wystarczająco, aby ograniczenie było skuteczne?
- **Ocena brzmienia 0.9.4-C:** ryzyko — konstrukcja poprawna, ale warunki spłaty nie wskazują dłużnika ani ścieżki, gdy nabywcy nie ma
- **Dlaczego zmieniono:** Art. 300⁴¹ § 1 KSH pozwala umową ograniczyć lub wyłączyć wstąpienie spadkobierców, pod warunkiem określenia warunków spłaty spadkobierców niewstępujących „pod rygorem bezskuteczności ograniczenia lub wyłączenia”. Projekt (a) wyraźnie powołuje przepis i deklaruje ograniczenie (ust. 1 zdanie pierwsze — to poprawia wadę wskazaną w audycie do wersji 0.8), (b) określa przesłanki niewstąpienia, (c) określa wysokość spłaty (100% Wartości Godziwej na dzień otwarcia spadku), (d) odsyła do zasad ratalnych ust. 4 (dawne błędne odesłanie do ust. 5 zostało poprawione). Konstrukcja jest trafna także w tym, że nie próbuje wyłączyć samego dziedziczenia (akcje przechodzą na spadkobiercę ex lege, art. 922 KC), lecz tylko wstąpienie do Spółki — spadkobierca niewstępujący jest właścicielem akcji bez statusu członkowskiego i ma roszczenie o spłatę; to model ugruntowany na tle art. 183 § 1 KSH, którego brzmienie art. 300⁴¹ § 1 zdanie pierwsze i drugie powtarza dosłownie, więc dorobek orzeczniczy do sp. z o.o. jest przenoszalny; nabycie w drodze spadku nie wymaga wpisu konstytutywnego (art. 300³⁷ § 2 KSH), lecz „wobec spółki uważa się za akcjonariusza tylko tę osobę, która jest wpisana do rejestru akcjonariuszy” (art. 300³⁸ § 1 KSH), co daje Spółce narzędzie do niedopuszczenia spadkobiercy niewstępującego do wykonywania praw. […]
- **Rekomendacja memorandum:** Uzupełnić ust. 2 i ust. 4 o dłużnika spłaty (nabywca, a solidarnie Spółka), termin wskazania nabywcy, bezwarunkowy termin pierwszej raty i ścieżkę rezerwową przez nabycie akcji własnych albo umorzenie, z wyraźnym określeniem niewstąpienia jako przesłanki umorzenia (art. 300⁴⁵ § 1 KSH); dodać regułę dla akcji za wkład pracy (art. 300⁴¹ § 1 zdanie trzecie i § 2 KSH). Rozważyć automatyczne zwolnienie akcji niezwolnionych przy śmierci (decyzja Założycieli).
- **Podstawa prawna:** art. 300⁴¹ § 1–2 KSH [Z]; art. 300⁴⁴–300⁴⁶ KSH (umorzenie przymusowe i automatyczne, spłata nie niższa od wartości godziwej) [Z]; art. 300¹⁵ § 2 i 4–6 KSH [Z]; art. 300⁴⁷ § 1–2 KSH [Z]; art. 300³⁷ § 2 i art. 300³⁸ § 1 KSH [Z]; art. 922 § 1, art. 924–925, art. 1025 § 2, art. 1027 KC [Z]; art. 21 ust. 1 i art. 64 Konstytucji RP [Z]; art. 183 § 1 KSH (analogia; brzmienie identyczne) [Z] i orzecznictwo do sp. z o.o. [W]

#### § 17 ust. 2: większość dla zgody na wstąpienie spadkobiercy liczona bez głosów z akcji spadkowych, uzasadnienie odmowy

Commit `ed16fed` · memorandum 1.6.2 · klasa: zalecane

- **Pytanie:** Czy uzależnienie wstąpienia od Kryterium i zgody Walnego Zgromadzenia jest dopuszczalne wobec spadkobierców (w tym ustawowych), także z perspektywy konstytucyjnej ochrony dziedziczenia?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Art. 300⁴¹ § 1 KSH nie ogranicza przesłanek, od których umowa może uzależnić wstąpienie; dopuszczalne jest zarówno wyłączenie wszystkich spadkobierców, jak i ograniczenie do osób spełniających określone cechy, byle z określoną spłatą. Kryterium Bezpieczeństwa EU/NATO i zgoda Walnego Zgromadzenia mieszczą się w tej swobodzie; dotyczy to także spadkobierców ustawowych, bo ustawa nie różnicuje. Ochrona konstytucyjna dziedziczenia (art. 21 ust. 1, art. 64 Konstytucji) obejmuje wartość majątkową spadku, a nie przynależność do korporacji: spadkobierca otrzymuje 100% Wartości Godziwej bez dyskonta, więc ekwiwalent jest pełny, a ograniczenie ma podstawę ustawową (art. 300⁴¹ § 1 KSH, co odpowiada wymogowi ograniczania własności „tylko w drodze ustawy” z art. 64 ust. 3 Konstytucji) i cel (bezpieczeństwo struktury właścicielskiej spółki obronnej), co spełnia test proporcjonalności z art. 31 ust. 3 — tym bardziej, że ograniczenie ma źródło w umowie, którą spadkodawca sam zawarł. […]
- **Rekomendacja memorandum:** Utrzymać Kryterium wobec spadkobierców; w § 17 ust. 2 zastrzec, że próg zgody liczy się z wyłączeniem akcji objętych spadkiem, i dodać wymóg uzasadnienia odmowy.
- **Podstawa prawna:** art. 300⁴¹ § 1 KSH [Z]; art. 21 ust. 1, art. 31 ust. 3, art. 64 ust. 1–3 Konstytucji RP [Z]; art. 63 TFUE (dziedziczenie jako przepływ kapitału w orzecznictwie TSUE) [W]; art. 18 TFUE [W]; art. 58 § 2 KC [Z]

#### § 17 ust. 2a: tryb wezwania spadkobierców i bieg 90 dni, wszczęcie postępowania spadkowego przez Spółkę, stwierdzenie niewstąpienia uchwałą Rady, umorzenie automatyczne (art. 300^46 KSH) wobec spadkobiercy niewspółdziałającego

Commit `574cb13` · memorandum 1.6.3, K8 · klasa: konieczne

- **Pytanie:** Czy 90-dniowe terminy i mechanizm rezerwowy (obowiązkowe zbycie na rzecz wskazanego nabywcy) są wykonalne wobec spadkobiercy, który nie współdziała; kto i jak stwierdza „niewstąpienie”?
- **Ocena brzmienia 0.9.4-C:** ryzyko
- **Dlaczego zmieniono:** Wobec spadkobiercy niewspółdziałającego projekt ma dwie słabości. Pierwsza dotyczy biegu terminów: 90 dni liczy się „od wezwania”, ale Spółka często nie zna spadkobierców, a ci nie mają obowiązku ujawnić się przed uzyskaniem stwierdzenia nabycia spadku albo aktu poświadczenia dziedziczenia (art. 1025 § 2, art. 1027 KC), co trwa miesiącami (stwierdzenie nabycia spadku ani poświadczenie dziedziczenia „nie może nastąpić przed upływem sześciu miesięcy od otwarcia spadku, chyba że wszyscy znani spadkobiercy złożyli już oświadczenia o przyjęciu lub o odrzuceniu spadku”, art. 1026 KC); do tego czasu akcje figurują na zmarłym (nabycie w drodze spadku następuje bez wpisu, art. 300³⁷ § 2 KSH, ale wobec Spółki akcjonariuszem jest tylko osoba wpisana, art. 300³⁸ § 1 KSH), prawa z nich nie są wykonywane, a Spółka nie może ani wezwać, ani stwierdzić niewstąpienia. Umowa powinna przewidywać wezwanie skierowane do znanych spadkobierców i — rezerwowo — na ostatni adres zmarłego, oraz możliwość wystąpienia przez Spółkę jako zainteresowanego o stwierdzenie nabycia spadku (art. 1025 § 1 KC) albo o ustanowienie kuratora spadku (art. 666 § 1 KPC), który „powinien starać się o wyjaśnienie, kto jest spadkobiercą” (art. 667 § 1 KPC). […]
- **Rekomendacja memorandum:** Dodać do § 17: tryb wezwania i bieg terminu od wykazania następstwa lub od doręczenia na ostatni adres, uprawnienie Spółki do wszczęcia postępowania spadkowego lub o kuratora, stwierdzenie niewstąpienia uchwałą Rady z doręczeniem, oraz umorzenie jako ścieżkę ostateczną.
- **Podstawa prawna:** art. 300⁴¹ § 1, art. 300³⁴ § 1 i 4, art. 300³⁷ § 2, art. 300³⁸ § 1, art. 300⁴⁴–300⁴⁶, art. 300⁴⁷ KSH [Z]; art. 1025 § 2, art. 1026, art. 1027, art. 1035–1036 KC [Z]; art. 64 KC, art. 1047 KPC [Z]; art. 666–667 KPC (kurator spadku) [Z]

#### § 17 ust. 4: bezwarunkowy termin spłaty (30 dni od ostatecznego ustalenia Wartości Godziwej) i raty na żądanie nabywcy albo Spółki zamiast przesłanki zagrożenia płynności

Commit `f016ffa` · memorandum 1.6.1, K7 · klasa: konieczne

- **Pytanie:** Czy § 17 prawidłowo wykorzystuje art. 300⁴¹ § 1 KSH (ograniczenie albo wyłączenie wstąpienia pod warunkiem określenia zasad spłaty), a warunki spłaty (100 % Wartości Godziwej, raty z § 17 ust. 4) są określone wystarczająco, aby ograniczenie było skuteczne?
- **Ocena brzmienia 0.9.4-C:** ryzyko — konstrukcja poprawna, ale warunki spłaty nie wskazują dłużnika ani ścieżki, gdy nabywcy nie ma
- **Dlaczego zmieniono:** Art. 300⁴¹ § 1 KSH pozwala umową ograniczyć lub wyłączyć wstąpienie spadkobierców, pod warunkiem określenia warunków spłaty spadkobierców niewstępujących „pod rygorem bezskuteczności ograniczenia lub wyłączenia”. Projekt (a) wyraźnie powołuje przepis i deklaruje ograniczenie (ust. 1 zdanie pierwsze — to poprawia wadę wskazaną w audycie do wersji 0.8), (b) określa przesłanki niewstąpienia, (c) określa wysokość spłaty (100% Wartości Godziwej na dzień otwarcia spadku), (d) odsyła do zasad ratalnych ust. 4 (dawne błędne odesłanie do ust. 5 zostało poprawione). Konstrukcja jest trafna także w tym, że nie próbuje wyłączyć samego dziedziczenia (akcje przechodzą na spadkobiercę ex lege, art. 922 KC), lecz tylko wstąpienie do Spółki — spadkobierca niewstępujący jest właścicielem akcji bez statusu członkowskiego i ma roszczenie o spłatę; to model ugruntowany na tle art. 183 § 1 KSH, którego brzmienie art. 300⁴¹ § 1 zdanie pierwsze i drugie powtarza dosłownie, więc dorobek orzeczniczy do sp. z o.o. jest przenoszalny; nabycie w drodze spadku nie wymaga wpisu konstytutywnego (art. 300³⁷ § 2 KSH), lecz „wobec spółki uważa się za akcjonariusza tylko tę osobę, która jest wpisana do rejestru akcjonariuszy” (art. 300³⁸ § 1 KSH), co daje Spółce narzędzie do niedopuszczenia spadkobiercy niewstępującego do wykonywania praw. […]
- **Rekomendacja memorandum:** Uzupełnić ust. 2 i ust. 4 o dłużnika spłaty (nabywca, a solidarnie Spółka), termin wskazania nabywcy, bezwarunkowy termin pierwszej raty i ścieżkę rezerwową przez nabycie akcji własnych albo umorzenie, z wyraźnym określeniem niewstąpienia jako przesłanki umorzenia (art. 300⁴⁵ § 1 KSH); dodać regułę dla akcji za wkład pracy (art. 300⁴¹ § 1 zdanie trzecie i § 2 KSH). Rozważyć automatyczne zwolnienie akcji niezwolnionych przy śmierci (decyzja Założycieli).
- **Podstawa prawna:** art. 300⁴¹ § 1–2 KSH [Z]; art. 300⁴⁴–300⁴⁶ KSH (umorzenie przymusowe i automatyczne, spłata nie niższa od wartości godziwej) [Z]; art. 300¹⁵ § 2 i 4–6 KSH [Z]; art. 300⁴⁷ § 1–2 KSH [Z]; art. 300³⁷ § 2 i art. 300³⁸ § 1 KSH [Z]; art. 922 § 1, art. 924–925, art. 1025 § 2, art. 1027 KC [Z]; art. 21 ust. 1 i art. 64 Konstytucji RP [Z]; art. 183 § 1 KSH (analogia; brzmienie identyczne) [Z] i orzecznictwo do sp. z o.o. [W]

### § 18. Stosunki majątkowe małżeńskie i akcje

#### § 18 ust. 3: odpowiednie stosowanie § 11 ust. 15 do małżonka, który nabył akcje bez zgody Spółki i bez spełnienia Kryterium

Commit `dc33d4b` · memorandum 1.7.1 · klasa: zalecane

- **Pytanie:** Czy rozdzielenie sfery majątkowej (przynależność akcji do majątku wspólnego) od korporacyjnej (wykonywanie praw z akcji przez akcjonariusza wpisanego do rejestru) jest ujęte prawidłowo na tle KRO i KSH, i czy potrzebny jest osobny mechanizm wykupu udziału małżonka?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Ujęcie jest prawidłowe i odpowiada linii SN cytowanej w `psa_feedback.tex`: akcje nabyte ze środków wspólnych mogą należeć do majątku wspólnego (III CZP 32/16 — do udziałów, stosowane analogicznie), lecz akcjonariuszem jest małżonek, który je objął i jest wpisany do rejestru (III CSKP 65/21), a ustanowienie rozdzielności nie daje drugiemu małżonkowi praw korporacyjnych (III CZP 109/22). § 18 ust. 2 mówi dokładnie to, ust. 3 i 4 obsługują przejście akcji po podziale. Dwie uwagi praktyczne: (1) dla założycieli kwestia przynależności rozstrzyga się już przy objęciu — akcje objęte za wkład z majątku osobistego („prawa autorskie i prawa pokrewne, prawa własności przemysłowej oraz inne prawa twórcy” należą do majątku osobistego, art. 33 pkt 9 KRO; surogacja z pkt 10) wchodzą do majątku osobistego, a objęte za gotówkę wspólną — do wspólnego; ponieważ Załącznik nr 1 miesza wkłady, warto, aby każdy założyciel pozostający w ustroju wspólności złożył przy zawiązaniu oświadczenie o źródle wkładu albo rozważył umowę majątkową; (2) osobny mechanizm wykupu udziału małżonka nie jest potrzebny: przy podziale majątku sąd może przyznać akcje akcjonariuszowi ze spłatą na rzecz małżonka (art. 46 KRO w zw. z art. 1035 i 212 KC), a ust. 4 zobowiązuje akcjonariusza do dążenia do takiego rozwiązania. […]
- **Rekomendacja memorandum:** Dodać w § 18 ust. 3 odesłanie do § 11 ust. 15 stosowanego odpowiednio do małżonka, który nabył akcje z mocy orzeczenia lub podziału bez spełnienia Kryterium; przy zawiązaniu odebrać oświadczenia o źródle wkładów.
- **Podstawa prawna:** art. 31 § 1–2, art. 33 pkt 2, 9 i 10, art. 43, art. 46, art. 47¹ KRO [Z]; art. 300³⁷–300³⁸ KSH [Z]; SN III CZP 109/22, III CSKP 65/21, III CZP 32/16 [Z] (tezy według `psa_feedback.tex`; teksty orzeczeń niedostępne); art. 1035 KC w zw. z art. 212 KC [Z]
- **Orzecznictwo:** III CSKP 65/21, III CZP 109/22, III CZP 32/16 (zob. sekcja 6)

### § 19. Wartość Godziwa i Dzień Wyceny

#### § 19 ust. 2: Wartość Godziwa jako wynagrodzenie za umorzenie bez zgody akcjonariusza, nie niższe od minimum z art. 300^45 § 2 KSH

Commit `6bb1b2e` · memorandum 1.8.1 · klasa: opcjonalne

- **Pytanie:** Czy umowna definicja może być stosowana we wszystkich mechanizmach projektu (zwrotne zbycie, dziedziczenie, utrata Kryterium, wskazanie nabywcy), czy w niektórych ustawa narzuca własną metodę lub minimalny poziom spłaty?
- **Ocena brzmienia 0.9.4-C:** zgodne
- **Dlaczego zmieniono:** W żadnym z czterech mechanizmów ustawa nie narzuca własnej metody. Zwrotne zbycie i obowiązek zbycia po utracie Kryterium (§ 11 ust. 15) są umownymi obowiązkami sprzedaży na rzecz osoby trzeciej — cena jest przedmiotem swobody umów (art. 353¹ KC) i może być nawet niższa od wartości rynkowej (cena emisyjna, 80%). Przy odmowie zgody na zbycie „termin do wskazania nabywcy, cenę nabycia albo sposób jej określenia oraz termin zapłaty określa umowa spółki”, a „w braku tych postanowień akcja może być zbyta bez ograniczenia” (art. 300³⁹ § 3 KSH) — ustawa nie ma więc własnej reguły cenowej, lecz sankcję za jej brak, i § 12 ust. 3 słusznie z tego korzysta; ten sam skutek (swobodne zbycie) wywołuje niewskazanie nabywcy w terminie albo niezapłacenie ceny przez wskazanego nabywcę (art. 300³⁹ § 5 KSH). […]
- **Rekomendacja memorandum:** Bez zmian merytorycznych; opcjonalnie dopisać, że Wartość Godziwa stanowi także wynagrodzenie za umorzenie przymusowe, nie niższe niż wymagane ustawą.
- **Podstawa prawna:** art. 353¹ KC [Z]; art. 300³⁹ § 2–5 KSH [Z]; art. 300⁴¹ § 1 KSH [Z]; art. 300⁴⁵ § 2 KSH [Z]; art. 300⁴⁹ § 2 w zw. z art. 266 § 3 oraz art. 300⁵⁰ § 3 KSH (wyłączenie i ustąpienie akcjonariusza przez sąd) [Z]; art. 28 ust. 6 ustawy o rachunkowości (definicja wartości godziwej) [Z]

#### § 19 ust. 4: wspólny wybór Niezależnego Eksperta, rezerwowo przez instytucję neutralną, procedura kontradyktoryjna z terminem 60 dni

Commit `47f3d42` · memorandum 1.8.2, K10 · klasa: konieczne

- **Pytanie:** Czy wiążący charakter wyceny eksperta (§ 19 ust. 7) i tryb jego wyboru wytrzymają spór sądowy między wspólnikami?
- **Ocena brzmienia 0.9.4-C:** ryzyko — wiążący charakter tak, wybór eksperta przez Radę Dyrektorów nie
- **Dlaczego zmieniono:** Klauzula ekspercka („expert determination”) jest w prawie polskim umową o oznaczenie świadczenia przez osobę trzecią; jest dopuszczalna (art. 353¹, art. 536 § 1 KC), ale nie jest zapisem na sąd polubowny — ekspert nie rozstrzyga sporu, lecz ustala fakt, więc przepisy o zapisie na sąd polubowny (art. 1157, art. 1161 § 1 KPC) nie mają do niej zastosowania, a droga sądowa pozostaje otwarta (spór o cenę jako spór o prawa majątkowe byłby arbitrażowalny, art. 1157 pkt 1 KPC, ale § 38 ust. 4 wybiera sąd powszechny). Sąd nie zastąpi jednak wyceny własną tylko dlatego, że strona się z nią nie zgadza: bada, czy ustalenie mieści się w granicach umowy i nie jest rażąco niesłuszne, a strona kwestionująca musi wykazać wadę — i tu wyjątki z ust. 7 (błąd rachunkowy, brak niezależności, rażące pominięcie danych) są dobrze dobrane; warto dodać czwarty: oczywistą sprzeczność z zasadami wyceny określonymi w ust. 2 i 5 (np. zastosowanie dyskonta). Sąd, badając zarzuty, powoła biegłego („w wypadkach wymagających wiadomości specjalnych”, art. 278 § 1 KPC), więc wycena ekspercka musi być udokumentowana na poziomie opinii biegłego. […]
- **Rekomendacja memorandum:** Zmienić tryb wyboru na wspólny, z rezerwowym wskazaniem przez instytucję neutralną (do wyboru Założycieli: prezes właściwego sądu okręgowego, Krajowa Izba Biegłych Rewidentów, sąd arbitrażowy przy izbie gospodarczej); dodać procedurę kontradyktoryjną i czwarty wyjątek w ust. 7.
- **Podstawa prawna:** art. 353¹, art. 58 § 2, art. 536 § 1 KC [Z]; art. 1157 pkt 1, art. 1161 § 1–2 KPC [Z]; art. 278 § 1 KPC [Z]; art. 300⁵⁵ § 1 KSH [Z]

#### § 19 ust. 7: wyjątek oczywistej sprzeczności z zasadami wyceny i tryb ponownej wyceny przez innego Niezależnego Eksperta

Commit `83e8405` · memorandum 1.8.2, K11 · klasa: konieczne

- **Pytanie:** Czy wiążący charakter wyceny eksperta (§ 19 ust. 7) i tryb jego wyboru wytrzymają spór sądowy między wspólnikami?
- **Ocena brzmienia 0.9.4-C:** ryzyko — wiążący charakter tak, wybór eksperta przez Radę Dyrektorów nie
- **Dlaczego zmieniono:** Klauzula ekspercka („expert determination”) jest w prawie polskim umową o oznaczenie świadczenia przez osobę trzecią; jest dopuszczalna (art. 353¹, art. 536 § 1 KC), ale nie jest zapisem na sąd polubowny — ekspert nie rozstrzyga sporu, lecz ustala fakt, więc przepisy o zapisie na sąd polubowny (art. 1157, art. 1161 § 1 KPC) nie mają do niej zastosowania, a droga sądowa pozostaje otwarta (spór o cenę jako spór o prawa majątkowe byłby arbitrażowalny, art. 1157 pkt 1 KPC, ale § 38 ust. 4 wybiera sąd powszechny). Sąd nie zastąpi jednak wyceny własną tylko dlatego, że strona się z nią nie zgadza: bada, czy ustalenie mieści się w granicach umowy i nie jest rażąco niesłuszne, a strona kwestionująca musi wykazać wadę — i tu wyjątki z ust. 7 (błąd rachunkowy, brak niezależności, rażące pominięcie danych) są dobrze dobrane; warto dodać czwarty: oczywistą sprzeczność z zasadami wyceny określonymi w ust. 2 i 5 (np. zastosowanie dyskonta). Sąd, badając zarzuty, powoła biegłego („w wypadkach wymagających wiadomości specjalnych”, art. 278 § 1 KPC), więc wycena ekspercka musi być udokumentowana na poziomie opinii biegłego. […]
- **Rekomendacja memorandum:** Zmienić tryb wyboru na wspólny, z rezerwowym wskazaniem przez instytucję neutralną (do wyboru Założycieli: prezes właściwego sądu okręgowego, Krajowa Izba Biegłych Rewidentów, sąd arbitrażowy przy izbie gospodarczej); dodać procedurę kontradyktoryjną i czwarty wyjątek w ust. 7.
- **Podstawa prawna:** art. 353¹, art. 58 § 2, art. 536 § 1 KC [Z]; art. 1157 pkt 1, art. 1161 § 1–2 KPC [Z]; art. 278 § 1 KPC [Z]; art. 300⁵⁵ § 1 KSH [Z]

### § 21. Rada Dyrektorów

#### § 21 ust. 3: dyrektor niespełniający Kryterium za zgodą WZ 75%, przy większości Rady i Przewodniczącym spełniających Kryterium, dostęp do Kluczowej Własności Intelektualnej według § 27 ust. 6 i § 28

Commit `3d5f0d1` · memorandum 1.1.5 · klasa: zalecane

- **Pytanie:** Czy wymóg Kryterium wobec dyrektorów (§ 21 ust. 3) jest dopuszczalny?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** KSH określa jedynie minimalne wymogi wobec członków organów (pełna zdolność do czynności prawnych, brak prawomocnego skazania za przestępstwa wymienione w art. 18 § 2 KSH) i nie zakazuje umowie spółki ustanawiania wymogów dodatkowych (kwalifikacje, wiek, obywatelstwo, niekaralność szersza niż ustawowa); dla P.S.A. potwierdza to wprost art. 300⁵³ KSH: „wobec spółki członkowie zarządu i dyrektorzy podlegają ograniczeniom ustanowionym w umowie spółki” [Z]; praktyka zna takie klauzule w spółkach regulowanych [W]. Stosunek organizacyjny dyrektora nie jest stosunkiem pracy, więc zakaz dyskryminacji z Kodeksu pracy nie ma zastosowania; jeżeli dyrektor jest równocześnie zatrudniony, kryterium dotyczy powołania do organu, nie zatrudnienia. Wymóg jest spójny z reżimem koncesyjnym: koncesji udziela się przedsiębiorcy innemu niż osoba fizyczna, „jeżeli co najmniej dwie osoby będące członkami organu zarządzającego przedsiębiorstwa albo członek organu zarządzającego przedsiębiorstwa i ustanowiony przez ten organ do kierowania działalnością określoną w koncesji prokurent lub pełnomocnik” mają m.in. obywatelstwo polskie, innego państwa UE, Szwajcarii albo EFTA-EOG bądź zezwolenie na pobyt stały lub rezydenta długoterminowego UE (art. 10 ust. 1 pkt 2 w zw. z pkt 1 lit. a ustawy z 13 czerwca 2019 r.; ustawa z 13 marca 2026 r., Dz.U. poz. 471, nie zmienia tego przepisu [Z]) — Kryterium jest tu nawet szersze (NATO), więc nie zastępuje tego wymogu. […]
- **Rekomendacja memorandum:** Dodać wyjątek za zgodą Walnego Zgromadzenia (75% wszystkich głosów) z zastrzeżeniem § 27 ust. 6 i § 28, a także wymóg, aby w każdym czasie większość dyrektorów, w tym Przewodniczący, spełniała Kryterium.
- **Podstawa prawna:** art. 300⁵² § 1 i art. 300⁵³ KSH (dyrektorzy podlegają ograniczeniom ustanowionym w umowie spółki), art. 18 § 1–2 KSH (wymogi ustawowe dla członków organów) [Z]; art. 300¹ § 3 KSH [Z]; art. 10 ust. 1 pkt 2 w zw. z pkt 1 lit. a ustawy z 13 czerwca 2019 r. — wymogi obywatelstwa osób kierujących działalnością koncesjonowaną [Z]; art. 11³ Kodeksu pracy — dotyczy „dyskryminacji w zatrudnieniu”, nie stosunku organizacyjnego [Z].

#### § 21 ust. 3-4: wspólna kadencja w latach obrotowych, wygaśnięcie mandatu z powołaniem następcy nie później niż 6 miesięcy po kadencji (art. 300^56 KSH), obowiązek zwołania WZ 3 miesiące przed upływem kadencji

Commit `dcd601e` · memorandum 2.1.1 · klasa: zalecane

- **Pytanie:** Czy większości przy powołaniu i odwołaniu oraz przedłużenie mandatu do 6 miesięcy są zgodne z przepisami KSH o organach P.S.A. i czy przedłużenie mandatu nie koliduje z zasadą wygaśnięcia mandatu?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo (większości — zgodne; prorogacja mandatu — wymaga przebudowy redakcyjnej)
- **Dlaczego zmieniono:** Większości są poprawne. Art. 300⁷³ § 3 KSH przekazuje powoływanie i odwoływanie dyrektorów akcjonariuszom, a art. 300⁷⁴ § 2 pozwala umowie „ograniczać prawo odwołania do ważnych powodów”, więc tym bardziej dopuszcza większość kwalifikowaną dla odwołania bez ważnych powodów; bezwzględna większość głosów oddanych („więcej niż połowę głosów oddanych”, art. 4 § 1 pkt 10) jest ustawową regułą domyślną (art. 300⁹⁸ § 1), a wymóg 75% wszystkich głosów jest „innym postanowieniem umowy” na tym samym tle co art. 203 § 2 i 370 § 2 KSH. Na zgromadzeniu uchwały o powołaniu i odwołaniu wymagają głosowania tajnego (art. 300⁹⁹ § 2); przy uchwałach poza zgromadzeniem wymóg ten nie obowiązuje (art. 300⁸⁰ § 3). […]
- **Rekomendacja memorandum:** Zachować mechanizm ciągłości, ale zbudować go jako element definicji kadencji i mandatu, nie jako „przedłużenie” po wygaśnięciu: kadencja liczona w latach obrotowych, mandat wygasa z dniem powołania następcy, nie później niż 6 miesięcy po upływie kadencji; dodać regułę dla dyrektora dokooptowanego w trakcie kadencji wspólnej i obowiązek Rady zwołania WZ z porządkiem obrad obejmującym wybory nie później niż 3 miesiące przed upływem kadencji. Rozważyć przykładowy katalog ważnych powodów (regulamin Rady albo umowa akcjonariuszy). Decyzja Założycieli: czy bezwzględna większość oddanych ma pozostać przy odwołaniu z ważnych powodów, mimo że akcjonariusz z 50% może ją zablokować.
- **Podstawa prawna:** art. 300⁷³ § 3 KSH („Dyrektorów powołują i odwołują oraz zawieszają w czynnościach, z ważnych powodów, akcjonariusze uchwałą, chyba że umowa spółki stanowi inaczej”) [Z]; art. 300⁷⁴ § 1–2 KSH (odwołanie w każdym czasie uchwałą akcjonariuszy; umowa „może zawierać inne postanowienia, w szczególności ograniczać prawo odwołania do ważnych powodów”) [Z]; art. 300⁵⁶ § 1–4 KSH (mandat; kadencja liczona w latach obrotowych; wspólna kadencja; wygaśnięcie mandatu z dniem odbycia WZ zatwierdzającego sprawozdanie za ostatni rok kadencji — każdorazowo „chyba że umowa spółki stanowi inaczej”) [Z]; art. 300⁹⁸ § 1 KSH (bezwzględna większość głosów jako reguła domyślna, „jeżeli przepisy niniejszego działu lub umowa spółki nie stanowią inaczej”) [Z]; art. 4 § 1 pkt 10 KSH (bezwzględna większość: „więcej niż połowę głosów oddanych”) [Z]; art. 300⁹⁶ KSH (wyłączenie od głosowania — nie obejmuje głosowania nad własnym odwołaniem) [Z]; art. 300⁹⁹ § 2 i art. 300⁸⁰ § 3 KSH (tajne głosowanie przy powołaniu i odwołaniu; nie dotyczy uchwał podejmowanych poza zgromadzeniem) [Z]; art. 39 KC (czynność rzekomego organu, potwierdzenie) [Z]; analogicznie art. 202 § 2–3, art. 203 § 2, art. 369 § 3–4 i art. 370 § 2 KSH [Z] oraz uchwała SN III CZP 109/22 (kadencja a mandat) [W].

#### § 21 ust. 3: wyjątek od Kryterium ograniczony do jednego dyrektora niewykonawczego wskazanego przez Kwalifikowanego Inwestora Finansowego, test sankcyjny, Przewodniczący i dyrektorzy wykonawczy spełniający Kryterium, wyłączenia w regulaminie Rady

Commit `d72a71c` · memorandum 4.4.2, brzmienie V · klasa: zalecane — odstępstwo od reguły „zgodne warunkowo → zalecane” nie jest potrzebne; brzmienia podajemy, bo zmiany są proste i jednoznaczne

- **Pytanie:** Jakie zmiany ułatwiłyby dostosowanie umowy do rundy bez naruszenia jej założeń (bezpieczeństwo właścicielskie, kontrola eksportu, mechanizm zwrotnego zbycia)?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo — założenia umowy da się utrzymać w całości; potrzebne są cztery zmiany w umowie spółki przed rundą i przeniesienie reszty do dokumentów rundy
- **Dlaczego zmieniono:** Kryterium zmian jest jedno: nic, co decyduje o dostępie do EDF, EUDIS, DIANA/NIF i koncesji, nie może zostać osłabione (warunki EDF: siedziba i „zarządcze struktury wykonawcze” w Unii lub w państwie stowarzyszonym oraz brak „kontroli niestowarzyszonego państwa trzeciego lub podmiotu z niestowarzyszonego państwa trzeciego”, art. 9 ust. 1–3 rozporządzenia 2021/697, z derogacją za gwarancjami zatwierdzonymi przez państwo członkowskie lub stowarzyszone siedziby z art. 9 ust. 4 [Z]; państwa stowarzyszone to według art. 5 członkowie EFTA należący do EOG, których rozporządzenie nie wymienia z nazwy [Z], w praktyce obecnie Norwegia, `web_edf_gowling.txt` [Z]; warunek NIF: siedziba w jednym z 24 państw NATO będących jego inwestorami, `web_nif_about.txt` [Z]). Te założenia to: (i) kontrola nad Spółką pozostaje w rękach osób i podmiotów z UE/EOG/NATO, a — jeżeli Założyciele przyjmą decyzję D6 — z UE/EOG; (ii) dostęp do Kluczowej Własności Intelektualnej spoza UE/NATO tylko za zgodą Rady po analizie eksportowej (§ 27 ust. 6, § 28); […]
- **Rekomendacja memorandum:** Wprowadzić zmiany A.1–A.4 przed pierwszym term sheetem (A.1 i A.3 warunkują w praktyce rozmowę z funduszami D i Z); A.5 i A.6 zależnie od decyzji Założycieli o kręgu inwestorów; A.7 po stanowisku kancelarii. Resztę zostawić dokumentom rundy. Brzmienia poniżej są sugestią do weryfikacji przez uprawnionego prawnika, w szczególności co do art. 300³⁹ § 2 KSH (wyłączenie zgody Spółki dla kategorii przeniesień) i ujawnienia w rejestrze akcjonariuszy.
- **Podstawa prawna:** art. 300³⁹ § 1–2 KSH („chyba że umowa spółki stanowi inaczej”) [Z]; art. 300²⁵ § 1–2 i art. 300²⁸ § 1–2 KSH [Z]; art. 300³³ § 1 pkt 4 i 10 KSH (rejestr akcjonariuszy zawiera „rodzaj danej akcji i uprawnienia szczególne z akcji” oraz „ograniczenia co do rozporządzania akcją”) [Z]; art. 300¹⁰³ KSH (emisja na podstawie postanowień umowy „przewidujących maksymalną liczbę akcji i termin ich emisji” bez trybu zmiany umowy) [Z]; art. 300¹⁰⁴ § 1 pkt 2 KSH [Z]; art. 300¹⁰⁶ § 1–2 KSH (prawo poboru, „jeżeli umowa spółki lub uchwała akcjonariuszy nie stanowią inaczej”; pozbawienie uchwałą większością 4/5) [Z]; art. 2 pkt 6 i 24, art. 5 i art. 9 ust. 1–4 i 7 rozporządzenia (UE) 2021/697 [Z]; art. 2 pkt 1, 5 i 7, art. 4 ust. 1, 2, 9 i 15 lit. a–c, art. 5 ust. 1–2, art. 6, art. 11 ust. 3 i 5, art. 20 ust. 4 lit. a, art. 30–31, motywy 14–15 i 20, zał. I pkt 1–3 i zał. II pkt 14 rozporządzenia (UE) 2026/1386 [Z] (tekst EN); rozporządzenie (UE) 2021/821 (unijny system kontroli wywozu, pośrednictwa, pomocy technicznej, tranzytu i transferu produktów podwójnego zastosowania; do jego zał. I odsyła art. 4 ust. 15 lit. a rozporządzenia 2026/1386) [Z] (tekst EN, konsolidacja na 26.05.2023 r.); art. 12a ust. 1 pkt 1, art. 12c ust. 1 pkt 1 i 5, ust. 4–5 oraz art. 12d ust. 3 pkt 7 i ust. 4 ustawy o kontroli niektórych inwestycji [Z]; art. 2 ust. 2 pkt 1 ustawy AML [Z].

#### § 21 ust. 6: wyznaczenie dyrektora wykonawczego uchwałą (art. 300^76 KSH), obowiązek dyrektora niewykonawczego, delegacja bez spraw z art. 300^75 § 2-3 KSH i § 23, odwołalna

Commit `4f219d4` · memorandum 2.1.3 · klasa: opcjonalne

- **Pytanie:** Czy podział na dyrektorów wykonawczych i niewykonawczych oraz delegowanie prowadzenia spraw (§ 21 ust. 6–8) odpowiada art. 300⁷⁶ KSH i nie ogranicza odpowiedzialności dyrektorów?
- **Ocena brzmienia 0.9.4-C:** zgodne
- **Dlaczego zmieniono:** § 21 ust. 6 („Rada wyznacza co najmniej jednego dyrektora wykonawczego, któremu deleguje prowadzenie bieżącej działalności”) jest delegacją uchwałą Rady w rozumieniu art. 300⁷⁶ KSH, a ust. 7 powierza dyrektorom niewykonawczym nadzór w obszarach, które ustawa i tak przypisuje im jako „stały nadzór”. Ustawowy wyjątek — sprawy z art. 300⁷⁵ § 2 (decyzje strategiczne, plany, struktura) i § 3 (prokura) nie mogą być delegowane — projekt respektuje przez katalog § 23 ust. 1 lit. a)–b) i § 22 ust. 2. Ust. 8 („podział zadań nie ogranicza ustawowych praw i obowiązków Rady ani odpowiedzialności dyrektorów”) odpowiada stanowi prawnemu: odpowiedzialność każdego dyrektora jest indywidualna i zależna od winy, a delegacja zmienia treść obowiązków (dyrektor niewykonawczy odpowiada za nadzór, wykonawczy za prowadzenie), nie ich istnienie; nie da się jej umownie wyłączyć wobec Spółki ani wierzycieli (art. 300¹²⁵ § 1; co do art. 300¹³² ustawa mówi o „członkach zarządu”, a stosowanie go do dyrektorów przyjmuje się w drodze wykładni — bez wpływu na ocenę klauzuli). […]
- **Rekomendacja memorandum:** Bez zmian merytorycznych; opcjonalnie wzmocnić ust. 6 i 8 redakcyjnie.
- **Podstawa prawna:** art. 300⁷⁶ KSH (delegacja czynności prowadzenia przedsiębiorstwa umową, regulaminem albo uchwałą Rady, z wyjątkiem art. 300⁷⁵ § 2–3; stały nadzór dyrektorów niewykonawczych) [Z]; art. 300⁷⁵ § 2 KSH [Z]; art. 300⁵⁴ KSH („staranności wynikającej z zawodowego charakteru swojej działalności oraz dochować lojalności wobec spółki”) [Z]; art. 300¹²⁵ § 1–2 KSH (odpowiedzialność za szkodę, chyba że członek organu nie ponosi winy; działanie „w granicach uzasadnionego ryzyka gospodarczego”) [Z]; art. 300¹³² KSH (odpowiedzialność za zobowiązania spółki przy bezskutecznej egzekucji — przepis mówi literalnie o „członkach zarządu”, a art. 300¹³³ rozciąga go tylko na likwidatorów) [Z]; objęcie art. 300¹³² dyrektorów w drodze wykładni [?].

#### § 21 ust. 9, § 29 ust. 7: pełny skład Rady jako liczba dyrektorów aktualnie powołanych, dyrektor wyłączony nie liczy się do quorum w danej sprawie

Commit `c52757b` · memorandum 2.3.2 · klasa: zalecane

- **Pytanie:** Czy quorum liczone od pełnego składu (§ 21 ust. 9) i wyłączenie dyrektorów (§ 29 ust. 7) są spójne z przepisami KSH o konflikcie interesów (art. 300⁵⁵ KSH) i o uchwałach organów?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo (spójne co do zasady; niespójna redakcja „składu” i „pełnego składu”)
- **Dlaczego zmieniono:** Wyłączenie z § 29 ust. 7 odtwarza art. 300⁵⁵ § 1 (dyrektor „wstrzymuje się od udziału w rozstrzyganiu”) i dodaje, że głosu nie liczy się oraz że wyłączenie „nie zmniejsza pełnego składu” jako podstawy quorum — to rozwiązanie surowsze niż ustawa, wprost dopuszczone przez art. 300⁵⁸ § 2, i przyjęte przez audyt. Dwie nieścisłości. (1) § 21 ust. 9 mówi o „obecności co najmniej połowy jej składu”, a § 29 ust. 7 o „pełnym składzie”; ustawowe „połowa jego członków” jest w doktrynie rozumiane różnie (skład faktyczny albo umowny). […]
- **Rekomendacja memorandum:** Ujednolicić definicję „pełnego składu” w § 21 ust. 9 i § 29 ust. 7 oraz rozstrzygnąć, że dyrektor wyłączony nie liczy się do quorum w danej sprawie.
- **Podstawa prawna:** art. 300⁵⁸ § 1–5 KSH (§ 1 warunek prawidłowego zawiadomienia wszystkich członków o posiedzeniu albo głosowaniu na piśmie lub na odległość; § 2 kworum „co najmniej połowa jej członków”, umowa „może przewidywać surowsze wymagania dotyczące kworum”; § 3 głosujący na piśmie albo na odległość liczeni do kworum, „chyba że umowa spółki lub regulamin organu stanowią inaczej”; § 4 większość i głos rozstrzygający; § 5 protokół) [Z]; art. 300⁵⁵ § 1 KSH („powinien ujawnić sprzeczność interesów i wstrzymać się od udziału w rozstrzyganiu takich spraw oraz może żądać zaznaczenia tego w protokole”) [Z]; art. 300⁵⁷ § 1 KSH (regulamin organu) [Z].

### § 23. Sprawy wymagające uchwały Rady Dyrektorów

#### § 23 ust. 2: wyznaczenie uchwałą dyrektora ds. bezpieczeństwa lub zgodności, tryb do czasu wyznaczenia i przy wyłączeniu lub nieobecności, skutek braku głosu i przedłożenie sprawy WZ

Commit `ff191e0` · memorandum 2.1.2 · klasa: zalecane

- **Pytanie:** Czy wymóg pozytywnego głosu określonego dyrektora (§ 23 ust. 2) jest dopuszczalny (uprzywilejowanie głosu w Radzie) i jaki jest skutek jego braku dla ważności uchwały?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Dopuszczalność. Art. 300⁵⁸ § 4 KSH wprost dopuszcza, by umowa określiła inną niż bezwzględna większość, i przewiduje głos rozstrzygający prezesa, przewodniczącego „lub innego członka organu”, co pokazuje, że ustawodawca nie traktuje równości głosów w Radzie P.S.A. jako zasady bezwzględnej. Wymóg, aby w ściśle określonych kategoriach spraw (§ 23 ust. 1 lit. e)–i) oraz k)) w większości znalazł się głos dyrektora niewykonawczego odpowiedzialnego za bezpieczeństwo lub zgodność, jest większością kwalifikowaną o charakterze funkcyjnym, a nie personalnym uprzywilejowaniem konkretnej osoby; uzasadnia go art. 300⁷⁶ (nadzór dyrektorów niewykonawczych) i regulacyjny profil Spółki. […]
- **Rekomendacja memorandum:** Doprecyzować: Rada wyznacza uchwałą co najmniej jednego dyrektora niewykonawczego odpowiedzialnego za bezpieczeństwo i zgodność niezwłocznie po ukonstytuowaniu się (obowiązek, nie opcja); do czasu wyznaczenia sprawy z lit. e)–i) i k) wymagają głosów wszystkich dyrektorów niewykonawczych; przy wyłączeniu albo nieobecności wyznaczonego dyrektora — głosu innego dyrektora niewykonawczego, a w jego braku sprawa trafia do Walnego Zgromadzenia; dodać wprost skutek: „uchwała nie zostaje podjęta”, z prawem przedłożenia sprawy Walnemu Zgromadzeniu (większość 75% wszystkich głosów), co odbiera klauzuli charakter weta osobistego.
- **Podstawa prawna:** art. 300⁵⁸ § 4 KSH („Uchwały organu zapadają bezwzględną większością głosów, chyba że umowa spółki stanowi inaczej”; umowa może przewidzieć głos rozstrzygający „prezesa, przewodniczącego lub innego członka organu”), § 2 (umowa może przewidywać surowsze wymagania dotyczące kworum) i § 5 (protokół z imionami i nazwiskami głosujących oraz wynikiem) [Z]; art. 300⁷⁵ § 1–2 i art. 300⁷⁶ § 1 KSH [Z]; art. 17 § 1–3 KSH (skutek braku uchwały wymaganej ustawą — nieważność; wymaganej wyłącznie umową — ważność, odpowiedzialność wobec spółki) [Z]; art. 300⁷⁷ § 2 KSH („Prawa dyrektora do reprezentowania spółki nie można ograniczyć ze skutkiem prawnym wobec osób trzecich”) [Z]; art. 189 KPC w zw. z art. 58 KC [Z] oraz uchwała SN (7) z 18.09.2013 r., III CZP 13/13 (zaskarżanie uchwał organów menedżerskich powództwem o ustalenie) [W]; art. 300¹²⁵ § 1 KSH (odpowiedzialność członka organu wobec spółki za szkodę, chyba że nie ponosi winy) [Z].

### § 24. Walne Zgromadzenie i sposób obliczania głosów

#### § 24 ust. 2: kaskada doręczeń zawiadomień o WZ (e-mail z rejestru, w braku przesyłka polecona albo kurierska), obowiązek podania adresu i zgody przy wpisie, chwila doręczenia, uchwały bez formalnego zwołania

Commit `402e224` · memorandum 2.2.2 · klasa: zalecane

- **Pytanie:** Czy zawiadomienie e-mailem na adres z rejestru akcjonariuszy spełnia art. 300⁸⁷ KSH i co, gdy akcjonariusz nie wskaże adresu?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Kanał jest ustawowy: art. 300⁸⁷ § 1 wymienia wprost pocztę elektroniczną „na adres akcjonariusza wpisany do rejestru akcjonariuszy”, bez odrębnej zgody pisemnej, jaką zna art. 238 § 1 KSH dla sp. z o.o.; zgoda akcjonariusza jest jednak warunkiem samego wpisu adresu do rejestru (art. 300³³ § 1 pkt 5: „jeżeli akcjonariusz wyraził zgodę na komunikację ... przy wykorzystaniu poczty elektronicznej”), więc przesuwa się na etap rejestru. § 24 ust. 3 jest więc zgodny z ustawą, a odesłanie do „terminów ustawowych” (dwa tygodnie) poprawne. Ustawa mówi o „wysłaniu”, więc decyduje data nadania, nie odbioru; Spółka powinna zachować dowód wysyłki. […]
- **Rekomendacja memorandum:** Dodać w ust. 3 kaskadę: (1) e-mail na adres z rejestru; (2) w jego braku przesyłka polecona albo kurierska na adres z rejestru; (3) nakaz podania adresu e-mail przy pierwszym wpisie i zgoda na komunikację elektroniczną w umowie akcjonariuszy oraz w umowie objęcia akcji; (4) przypomnienie, że przy reprezentacji wszystkich akcji uchwały można podejmować bez formalnego zwołania (art. 300⁹⁰).
- **Podstawa prawna:** art. 300⁸⁷ § 1 KSH („Walne zgromadzenie zwołuje się pocztą elektroniczną na adres akcjonariusza wpisany do rejestru akcjonariuszy, na adres do doręczeń elektronicznych lub za pomocą listu poleconego lub przesyłki nadanej pocztą kurierską”; wysyłka co najmniej dwa tygodnie przed WZ) [Z]; art. 300³³ § 1 pkt 5 KSH (rejestr zawiera adres poczty elektronicznej, „jeżeli akcjonariusz wyraził zgodę na komunikację w stosunkach ze spółką i podmiotem prowadzącym rejestr akcjonariuszy przy wykorzystaniu poczty elektronicznej”; po nowelizacji Dz.U. 2026 poz. 176, od 18.02.2027 r., pkt 5 zachowuje wymóg zgody i dodaje PESEL albo datę urodzenia) [Z]; art. 300³⁴ § 1 KSH (wpis „na żądanie spółki lub innej osoby mającej interes prawny”, nie później niż w 7 dni) [Z]; art. 300⁹⁰ KSH (uchwały mimo braku formalnego zwołania, jeżeli reprezentowane są wszystkie akcje i nikt nie zgłosił sprzeciwu) [Z]; art. 300¹⁰¹ KSH w zw. z art. 422 § 2 pkt 4 KSH (legitymacja akcjonariusza nieobecnego „jedynie w przypadku wadliwego zwołania walnego zgromadzenia”) [Z]; art. 238 § 1 KSH (sp. z o.o.: e-mail za uprzednią pisemną zgodą wspólnika) [Z].

#### § 24 ust. 2: 7-dniowy termin zgłaszania zmian danych podlegających wpisowi do rejestru akcjonariuszy, w tym istotnych dla Kryterium; § 38 ust. 6: klauzula dostosowawcza do zmian przepisów

Commit `d900f94` · memorandum 4.3.3 · klasa: zalecane

- **Pytanie:** Czy nowelizacja KSH z 23 stycznia 2026 r. (wejście w życie 18 lutego 2027 r.) wpływa na którekolwiek z postanowień projektu i czy warto już dziś przygotować umowę pod nowe przepisy?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo — tekst ustawy sprawdzony w całości; żadne postanowienie projektu nie jest z nią sprzeczne, ale nowelizacja nakłada na Spółkę nowe obowiązki proceduralne i obowiązek dostosowania umowy w 2 lata
- **Dlaczego zmieniono:** **Co zmienia ustawa w odniesieniu do P.S.A. i rejestru akcjonariuszy** (pełny wykaz na podstawie tekstu): (1) art. 300³² § 1¹–1³: „zarząd zgłasza zawarcie umowy [o prowadzenie rejestru] do sądu rejestrowego”; zgłoszenie zawiera dla domu maklerskiego firmę, numer w rejestrze i NIP, a dla notariusza imię i nazwisko oraz siedzibę i adres kancelarii (także zastępcy notariusza); dołącza się oświadczenie zarządu potwierdzające zawarcie umowy; § 3: podmiot prowadzący rejestr zawiadamia sąd przez system teleinformatyczny o wygaśnięciu albo rozwiązaniu umowy w 7 dni. (2) art. 300³³ § 1 pkt 5 i 6: rozszerzenie danych akcjonariusza i nabywcy o numer PESEL albo datę urodzenia, numer i nazwę rejestru osoby niebędącej osobą fizyczną oraz dane o współwłasności akcji; § 3: „wszelkie zmiany danych, o których mowa w § 1 pkt 1–4 oraz 9–11, zarząd zgłasza podmiotowi prowadzącemu rejestr akcjonariuszy w terminie siedmiu dni od dnia wystąpienia zdarzenia” — obejmuje dane spółki, akcje, wzmiankę o pokryciu oraz *ograniczenia rozporządzania i obowiązki związane z akcją*; sankcja: grzywna do 20 000 zł dla członka zarządu (art. 594 § 1 pkt 2¹). (3) art. 300³⁴: w § 1 „siedmiu dni” zastąpiono „tygodniem”; § 3 zdanie drugie określa formę zgody na wpis (pisemna z podpisem notarialnie poświadczonym, pisemna w obecności osoby upoważnionej przez podmiot albo elektroniczna z podpisem kwalifikowanym, zaufanym lub osobistym); § 9 dopuszcza automatyczne powiadomienia elektroniczne. […]
- **Rekomendacja memorandum:** Dodać klauzulę dostosowawczą do § 38 i termin 7 dni do § 24 ust. 3. W umowie wykonawczej (pakiet 1.5) przewidzieć składanie przez Założycieli zgód na wpis w formie z art. 300³⁴ § 3 zdanie drugie. Zawiązać Spółkę bez oczekiwania na 2027 r.; w kalendarzu Rady zapisać: zgłoszenie podmiotu prowadzącego rejestr do KRS do 18 maja 2027 r., przegląd umowy pod kątem art. 34 do 18 lutego 2029 r.
- **Podstawa prawna:** ustawa z 23 stycznia 2026 r. o zmianie ustawy — Kodeks spółek handlowych oraz niektórych innych ustaw (Dz.U. 2026 poz. 176, ogłoszona 17 lutego 2026 r.) [Z]; art. 35 (wejście w życie po upływie 12 miesięcy od ogłoszenia, tj. 18 lutego 2027 r., z wyjątkiem art. 28 i 33 — 28 lutego 2026 r.) [Z]; art. 1 pkt 2–6 i 30 (art. 300³², 300³³, 300³⁴, 300³⁵, 300³⁷ § 2 i art. 594 § 1 KSH) [Z]; art. 1 pkt 16–27 (zmiany dotyczące wyłącznie spółki akcyjnej, m.in. uchylenie art. 334 i zmiany art. 337, 351, 352, 356, 361, 406¹, 432, 434, 453, 476) [Z]; art. 2 (art. 90a § 1 Prawa o notariacie) [Z]; art. 5 (art. 10 ust. 4a pkt 4, art. 25da i art. 38 pkt 8a lit. j ustawy o KRS) [Z]; art. 16 pkt 3 (art. 83a ust. 4ac ustawy o obrocie instrumentami finansowymi) [Z]; art. 28–34 (przepisy przejściowe) [Z]; art. 300²⁹ § 1 KSH („akcje nie mają formy dokumentu”) [Z]; art. 55 ust. 1 ustawy o kosztach sądowych w sprawach cywilnych [Z]; art. 111 § 2 i art. 112 KC (obliczanie terminów) [Z].

#### § 24 ust. 6-7: regulamin WZ jako podstawa zasad udziału elektronicznego (art. 300^92 § 2 KSH) z regułą przejściową dla zawiadomienia, zastrzeżenie zakresu dopuszczalnego przez prawo przy problemach technicznych

Commit `4b4b6f1` · memorandum 2.2.1 · klasa: zalecane

- **Pytanie:** Czy sformułowania o udziale elektronicznym są zgodne z art. 300⁸⁸ i 300⁹² KSH (miejsce zgromadzenia a uczestnictwo zdalne) i nie zostaną odczytane jako w pełni wirtualne zgromadzenie?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo (konstrukcja hybrydowa — zgodna; brak regulaminu WZ wymaganego przez art. 300⁹² § 2)
- **Dlaczego zmieniono:** Wersja 0.9.4 usunęła sformułowanie kwestionowane przez audyt („WZ może odbywać się z wykorzystaniem środków komunikacji elektronicznej”). Obecny § 24 ust. 2 wskazuje fizyczne miejsce (siedziba albo Warszawa — dopuszczalne na tle art. 300⁸⁸, oba miejsca w Polsce), a ust. 6 mówi wyłącznie o „uczestnictwie w Walnym Zgromadzeniu przy wykorzystaniu środków komunikacji elektronicznej zgodnie z art. 300⁹² KSH”, z wyliczeniem dwustronnej komunikacji w czasie rzeczywistym i głosowania na odległość, czyli dokładnie w ramach ustawowej konstrukcji zgromadzenia hybrydowego: przewodniczący, protokolant (przy zmianie umowy — notariusz) i miejsce obrad pozostają fizyczne, a akcjonariusze mogą być zdalni. Istotne, że art. 300⁹² jest opt-in („umowa spółki może dopuszczać”), więc wyraźne dopuszczenie w ust. 6 jest konieczne i jest. […]
- **Rekomendacja memorandum:** Konstrukcję hybrydową zachować. W ust. 7 przewidzieć regulamin Walnego Zgromadzenia przyjęty uchwałą akcjonariuszy jako podstawę szczegółowych zasad udziału elektronicznego (art. 300⁹² § 2), z regułą przejściową dla zawiadomienia; w ust. 8 dodać „w zakresie dopuszczalnym przez prawo”. Regulamin przyjąć na pierwszym Walnym Zgromadzeniu po rejestracji.
- **Podstawa prawna:** art. 300⁸⁸ § 1–2 KSH (WZ „odbywa się w siedzibie spółki, jeżeli umowa spółki nie wskazuje innego miejsca”; miejsce za granicą wymaga dodatkowo miejsca w Polsce; inne miejsce za zgodą wszystkich akcjonariuszy w formie dokumentowej) [Z]; art. 300⁹² § 1–2 KSH (umowa „może dopuszczać” udział elektroniczny; wymogi „jedynie” niezbędne do identyfikacji i bezpieczeństwa; „Szczegółowe zasady dotyczące sposobu uczestnictwa w walnym zgromadzeniu przy wykorzystaniu środków komunikacji elektronicznej określa regulamin walnego zgromadzenia”) [Z]; art. 300⁸⁷ § 4 KSH (zawiadomienie „powinno zawierać dokładny opis sposobu uczestnictwa w walnym zgromadzeniu i wykonywania prawa głosu”) [Z]; art. 300⁸⁰ § 1–2 KSH (uchwały poza WZ na piśmie albo elektronicznie; głosowanie elektroniczne, jeżeli środki wskazano w umowie) [Z]; art. 300¹⁰⁰ § 1 KSH (protokół z listą akcjonariuszy głosujących elektronicznie) i art. 300¹⁰¹ KSH (art. 422–427 stosowane odpowiednio do zaskarżania uchwał) [Z].

#### § 24 ust. 10-11: zobowiązanie akcjonariusza wyłączonego umownie do niewykonywania głosu, konwersja progu wszystkich głosów na Głosy Uprawnione w Sprawie przy wyłączeniu ustawowym

Commit `435511a` · memorandum 2.2.3 · klasa: zalecane

- **Pytanie:** Czy dwa sposoby liczenia większości (od głosów uprawnionych w sprawie i od wszystkich głosów) są jasne i zgodne z KSH, zwłaszcza przy wyłączeniu głosu akcjonariusza występującego o zgodę (§ 13 ust. 1, § 25 ust. 3)?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Konstrukcja jest jasna: § 24 ust. 11 definiuje „Głosy Uprawnione w Sprawie” i wyjaśnia, że głosy wyłączone nie liczą się ani w liczniku, ani w mianowniku; ust. 12 oddziela progi liczone od „wszystkich głosów w Spółce”. Oba sposoby są dopuszczalne: próg liczony od wszystkich głosów jest surowszy niż ustawowe większości głosów oddanych, a art. 300⁹⁸ pozwala umowie na zaostrzenie. Rachunek dla § 13 ust. 1 i § 25 ust. 3 działa: przy wniosku Założyciela z 50% pozostaje 50 głosów, próg 75% to 38 głosów (20+10+10 wystarcza); przy wniosku Założyciela z 10% — 68 z 90 (50+20). […]
- **Rekomendacja memorandum:** Dodać do § 24 ust. 12 regułę konwersji przy wyłączeniu ustawowym oraz do ust. 11 zobowiązanie akcjonariusza wyłączonego umownie do niewykonywania głosu. Decyzja Założycieli: czy reguła konwersji ma dotyczyć wszystkich Spraw Zastrzeżonych, czy tylko tych, w których wyłączenie ustawowe jest realne (lit. l, m).
- **Podstawa prawna:** art. 300⁹⁸ § 1–2 KSH (bezwzględna większość jako reguła; 3/4 głosów dla zmiany umowy, zbycia przedsiębiorstwa lub ZCP, obligacji zamiennych i rozwiązania, „chyba że umowa spółki przewiduje surowsze warunki”) [Z]; art. 300⁹⁸ § 3 KSH (zmiana umowy „uszczuplająca prawa indywidualne poszczególnych akcjonariuszy, wymaga zgody wszystkich akcjonariuszy, których dotyczy”) [Z]; art. 4 § 1 pkt 9–10 KSH (głosy „za”, „przeciw” lub „wstrzymujące się” oddane; bezwzględna większość) [Z]; art. 300⁹⁶ KSH (ustawowe wyłączenie od głosowania: odpowiedzialność, absolutorium, zwolnienie z zobowiązania, spór) [Z]; art. 244 i 413 § 1 KSH (identyczne katalogi w sp. z o.o. i S.A.) [Z]; art. 300¹ § 3 KSH (akcjonariusz zobowiązany tylko do świadczeń określonych w umowie) [Z]; art. 20 KSH (równe traktowanie „w takich samych okolicznościach”) [Z]; art. 300³⁹ § 1–2 KSH (ograniczenia rozporządzania akcją w umowie) [Z]; art. 353¹ KC [Z].

### § 25. Sprawy Zastrzeżone dla Walnego Zgromadzenia

#### § 25 ust. 5: uchwały WZ w sprawach Rady jako zgoda, zgody ustawowe (art. 300^81 KSH), umowna zgoda WZ na kredyt, pożyczkę i poręczenie z dyrektorem lub prokurentem, nieruchomości do progu z lit. k bez uchwały WZ; ust. 1 lit. f: wydzierżawienie i obciążenie przedsiębiorstwa

Commit `f1ded08` · memorandum 2.2.4 · klasa: zalecane

- **Pytanie:** Czy katalog Spraw Zastrzeżonych i próg 75% nie blokują czynności, dla których ustawa przewiduje inną większość albo kompetencję Rady?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Zaostrzenie jest dozwolone, więc żadna pozycja katalogu nie jest sprzeczna z ustawową większością: 75% wszystkich głosów jest surowsze niż 3/4 głosów oddanych dla zmiany umowy, zbycia przedsiębiorstwa lub ZCP i rozwiązania (art. 300⁹⁸ § 2), niż większości przy łączeniu, podziale i przekształceniu (art. 506 § 1, 541 § 1, 575, 577 § 1 pkt 1 — wszystkie z klauzulą „chyba że umowa ... przewiduje surowsze warunki”), a pozbawienie prawa poboru zachowuje 4/5 (§ 25 ust. 2; art. 300¹⁰⁶ § 2). Audyt to potwierdził. Trzy punkty wymagają jednak uwagi. […]
- **Rekomendacja memorandum:** Dodać do § 25 ustęp wyjaśniający charakter zgody WZ w sprawach należących do Rady, odesłanie do zgód ustawowych (art. 300⁸¹) oraz własny, umowny wymóg zgody WZ na kredyt, pożyczkę, poręczenie i podobną umowę z dyrektorem albo prokurentem (bo art. 15 KSH nie wymienia dyrektora); zdecydować o nieruchomościach (proponowane: opt-out do progu z lit. k); rozszerzyć lit. f) o wydzierżawienie i obciążenie przedsiębiorstwa lub ZCP; rozważyć obniżenie większości dla lit. i.
- **Podstawa prawna:** art. 300⁹⁸ § 1–2 KSH (większości kwalifikowane 3/4; „chyba że umowa spółki przewiduje surowsze warunki”) [Z]; art. 300⁸¹ KSH (katalog czynności wymagających uchwały akcjonariuszy: pkt 2 zbycie i wydzierżawienie przedsiębiorstwa albo ZCP oraz ustanowienie na nich ograniczonego prawa rzeczowego — bez opt-out; pkt 3 „nabycie i zbycie nieruchomości, użytkowania wieczystego lub udziału w nieruchomości, chyba że umowa spółki stanowi inaczej”; pkt 4 obligacje zamienne i warranty; pkt 5 umowa o zarządzanie spółką zależną) [Z]; art. 300⁷⁵ § 2 KSH (uchwały Rady wymaga podejmowanie decyzji o strategicznym znaczeniu, ustalanie planów biznesowych, ustalenie struktury organizacyjnej) [Z]; art. 300¹⁰³ i 300¹⁰⁶ § 2 KSH (emisja jako zmiana umowy; pozbawienie prawa poboru „większością czterech piątych głosów”) [Z]; art. 17 § 1–3 KSH [Z]; art. 15 § 1 KSH (zgoda WZ na kredyt, pożyczkę, poręczenie lub podobną umowę z członkiem zarządu, rady nadzorczej, komisji rewizyjnej, prokurentem, likwidatorem — przepis nie wymienia dyrektora P.S.A., a przepisy o P.S.A. nie zawierają odesłania) [Z]; stosowanie art. 15 do dyrektora w drodze wykładni [?]; art. 506 § 1, 541 § 1 (3/4 głosów przy reprezentacji co najmniej połowy kapitału), 575 (2/3 kapitału) i 577 § 1 pkt 1 KSH (3/4 głosów przy połowie kapitału), każdorazowo „chyba że umowa ... przewiduje surowsze warunki” [Z].

### § 26. Własność intelektualna i aktywa technologiczne

#### § 26 ust. 2: obowiązek Założyciela zawarcia pisemnych umów przeniesienia praw (pola eksploatacji, prawa zależne, prawa osobiste, prawa do uzyskania patentu) w dniu umowy i w 30 dni od wpisu Spółki

Commit `424d7cb` · memorandum 3.1.3 · klasa: zalecane

- **Pytanie:** Czy oświadczenia z § 26 ust. 5 i obowiązek współdziałania z § 26 ust. 7 wystarczą, aby przed rundą wykazać tytuł Spółki do kodu, modeli i zgłoszeń patentowych; jakie odrębne umowy przeniesienia (pola eksploatacji, forma pisemna, wpisy) są konieczne?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo (warunek spełnia się poza umową)
- **Dlaczego zmieniono:** Oświadczenia z § 26 ust. 5 są zapewnieniami (podstawą odpowiedzialności odszkodowawczej i Odejścia Zawinionego, § 10 ust. 5 lit. d), a ust. 7 jest zobowiązaniem do współdziałania; żadne z nich nie przenosi praw, co umowa sama przyznaje w ust. 4. Inwestor w due diligence bada łańcuch tytułu, a nie oświadczenia. Konieczne są: (1) *kod i dokumentacja* — umowa przeniesienia autorskich praw majątkowych w formie pisemnej pod rygorem nieważności (art. 53), z wyraźnym wymienieniem pól eksploatacji (art. 41 ust. 2; dla programów komputerowych pola z art. 74 ust. 4: trwałe lub czasowe zwielokrotnianie, tłumaczenie, przystosowywanie, zmiany, rozpowszechnianie), tylko pól znanych w chwili umowy (art. 41 ust. 4), z przeniesieniem prawa zezwalania na wykonywanie praw zależnych (art. 46), zobowiązaniem twórcy do niewykonywania autorskich praw osobistych i upoważnieniem Spółki (art. 16 — prawa osobiste są niezbywalne) oraz oznaczeniem utworów (repozytorium, wersja, sumy kontrolne); nieważna jest umowa „w części dotyczącej wszystkich utworów lub wszystkich utworów określonego rodzaju tego samego twórcy mających powstać w przyszłości” (art. 41 ust. 3 [Z]), dlatego § 26 ust. 2 („ma przysługiwać Spółce”) nie zastąpi umów o pracę i umów B2B, a klauzule w tych umowach muszą obejmować utwory powstałe w wykonaniu danej umowy (nabycie z chwilą przyjęcia utworu), nie zaś „wszystkie utwory danego rodzaju”. […]
- **Rekomendacja memorandum:** Zawrzeć w dniu podpisania umowy trzy rodzaje dokumentów przeniesienia (kod i dane; sprzęt; prawa do wynalazków) według powyższych wymogów, a w umowach o pracę i B2B każdego Założyciela i pracownika — klauzule przeniesienia praw do utworów powstałych w wykonaniu danej umowy, z chwilą ich przyjęcia i z okresowymi protokołami przekazania (granica z art. 41 ust. 3). W § 26 dodać obowiązek zawarcia takich umów, aby jego naruszenie było naruszeniem umowy spółki.
- **Podstawa prawna:** art. 9 ust. 1–3, art. 12 ust. 1, art. 14 ust. 1, art. 16, art. 41 ust. 2–4, art. 46, art. 50, art. 53, art. 74 ust. 1, 3 i 4 ustawy o prawie autorskim i prawach pokrewnych [Z]; art. 11 ust. 1–3, art. 12 ust. 1–2, art. 20, art. 67 ust. 2–3, art. 72 ust. 1 ustawy Prawo własności przemysłowej [Z]; art. 11 ust. 1–2 ustawy o zwalczaniu nieuczciwej konkurencji [Z]; ustawa o ochronie baz danych [W]; art. 300¹¹ § 1–2 KSH [Z].

### § 27. Poufność, bezpieczeństwo informacji i cyberbezpieczeństwo

#### § 27 ust. 3: przetrwanie obowiązku poufności po utracie statusu akcjonariusza, pisemne zobowiązania dyrektorów niebędących akcjonariuszami i nabywców akcji

Commit `db993d8` · memorandum 4.2.3 · klasa: zalecane

- **Pytanie:** Czy 10-letni okres poufności i ograniczenie dostępu spoza UE/NATO (§ 27 ust. 3 i 6) są egzekwowalne wobec akcjonariuszy i dyrektorów, w tym po ustaniu ich statusu?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** **Wobec akcjonariuszy w czasie posiadania akcji.** Obowiązek poufności jako świadczenie określone w umowie spółki (art. 300¹ § 3) jest dopuszczalny i wiąże każdego akcjonariusza, także nabywcę wtórnego, bo umowa spółki wiąże z mocy prawa każdego, kto obejmuje albo nabywa akcje [W]. Może być ujawniony w rejestrze jako obowiązek związany z akcją (art. 300³³ § 1 pkt 11). Egzekwowalność: powództwo o zaniechanie, o naprawienie szkody (§ 36), zabezpieczenie; w zakresie tajemnicy przedsiębiorstwa dodatkowo roszczenia z art. 18 ust. 1 uznk (zaniechanie, usunięcie skutków, odszkodowanie, wydanie korzyści). […]
- **Rekomendacja memorandum:** Dodać w § 27 ust. 3 klauzulę przetrwania i objąć nią dyrektorów przez obowiązek Spółki zawarcia z nimi umowy; w ust. 6 wskazać adresata i dodać EOG. Karę umowną umieścić w umowie wykonawczej i umowach objęcia akcji, nie w umowie spółki.
- **Podstawa prawna:** art. 300¹ § 3 KSH („akcjonariusze są zobowiązani jedynie do świadczeń określonych w umowie spółki”) [Z]; art. 300⁵⁴ KSH (staranność zawodowa i lojalność członka organu) [Z]; art. 300⁵⁵ § 2 KSH („członek organu nie może ujawniać tajemnic spółki, także po wygaśnięciu mandatu”) [Z]; art. 300⁵⁵ § 1 KSH (konflikt interesów) [Z]; art. 11 ust. 1–2 i 4 oraz art. 18 ust. 1 ustawy z 16 kwietnia 1993 r. o zwalczaniu nieuczciwej konkurencji [Z]; dyrektywa (UE) 2016/943 [W]; art. 353¹ KC [W]; art. 483–484 KC [Z]; art. 300³³ § 1 pkt 11 i § 2 KSH (obowiązki związane z akcją; dodatkowe informacje ujawniane w rejestrze na podstawie umowy) [Z]; art. 300³⁵ § 1 KSH (rejestr jawny dla spółki i każdego akcjonariusza) [Z]; art. 54 ust. 1–2 ustawy z 5 sierpnia 2010 r. o ochronie informacji niejawnych (świadectwo bezpieczeństwa przemysłowego) [Z]; art. 2 pkt 2 lit. d i pkt 3 lit. b, art. 3 ust. 1, art. 8 ust. 1–3, art. 12 ust. 1 oraz załącznik II sekcje A–F (EU001–EU006) rozporządzenia (UE) 2021/821 [Z] (tekst EN).

#### § 27 ust. 6: adresaci zakazu dostępu do Kluczowej Własności Intelektualnej (akcjonariusz, dyrektor, osoba działająca na rzecz Spółki), dodanie EOG, odesłanie do § 28

Commit `a072eb9` · memorandum 4.2.3 · klasa: zalecane

- **Pytanie:** Czy 10-letni okres poufności i ograniczenie dostępu spoza UE/NATO (§ 27 ust. 3 i 6) są egzekwowalne wobec akcjonariuszy i dyrektorów, w tym po ustaniu ich statusu?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** **Wobec akcjonariuszy w czasie posiadania akcji.** Obowiązek poufności jako świadczenie określone w umowie spółki (art. 300¹ § 3) jest dopuszczalny i wiąże każdego akcjonariusza, także nabywcę wtórnego, bo umowa spółki wiąże z mocy prawa każdego, kto obejmuje albo nabywa akcje [W]. Może być ujawniony w rejestrze jako obowiązek związany z akcją (art. 300³³ § 1 pkt 11). Egzekwowalność: powództwo o zaniechanie, o naprawienie szkody (§ 36), zabezpieczenie; w zakresie tajemnicy przedsiębiorstwa dodatkowo roszczenia z art. 18 ust. 1 uznk (zaniechanie, usunięcie skutków, odszkodowanie, wydanie korzyści). […]
- **Rekomendacja memorandum:** Dodać w § 27 ust. 3 klauzulę przetrwania i objąć nią dyrektorów przez obowiązek Spółki zawarcia z nimi umowy; w ust. 6 wskazać adresata i dodać EOG. Karę umowną umieścić w umowie wykonawczej i umowach objęcia akcji, nie w umowie spółki.
- **Podstawa prawna:** art. 300¹ § 3 KSH („akcjonariusze są zobowiązani jedynie do świadczeń określonych w umowie spółki”) [Z]; art. 300⁵⁴ KSH (staranność zawodowa i lojalność członka organu) [Z]; art. 300⁵⁵ § 2 KSH („członek organu nie może ujawniać tajemnic spółki, także po wygaśnięciu mandatu”) [Z]; art. 300⁵⁵ § 1 KSH (konflikt interesów) [Z]; art. 11 ust. 1–2 i 4 oraz art. 18 ust. 1 ustawy z 16 kwietnia 1993 r. o zwalczaniu nieuczciwej konkurencji [Z]; dyrektywa (UE) 2016/943 [W]; art. 353¹ KC [W]; art. 483–484 KC [Z]; art. 300³³ § 1 pkt 11 i § 2 KSH (obowiązki związane z akcją; dodatkowe informacje ujawniane w rejestrze na podstawie umowy) [Z]; art. 300³⁵ § 1 KSH (rejestr jawny dla spółki i każdego akcjonariusza) [Z]; art. 54 ust. 1–2 ustawy z 5 sierpnia 2010 r. o ochronie informacji niejawnych (świadectwo bezpieczeństwa przemysłowego) [Z]; art. 2 pkt 2 lit. d i pkt 3 lit. b, art. 3 ust. 1, art. 8 ust. 1–3, art. 12 ust. 1 oraz załącznik II sekcje A–F (EU001–EU006) rozporządzenia (UE) 2021/821 [Z] (tekst EN).

### § 28. Kontrola eksportu, sankcje i końcowe zastosowanie

#### § 28 ust. 1: przykładowe wyliczenie aktów (2021/821, ustawa o obrocie strategicznym, ustawa koncesyjna, środki ograniczające, AI Act w zakresie zastosowania) w brzmieniu obowiązującym

Commit `1b2b759` · memorandum 4.2.1 · klasa: zalecane — odstępstwo od reguły dla oceny „zgodne” uzasadnione tym, że ust. 5 w obecnym brzmieniu nie jest wykonalny

- **Pytanie:** Czy klauzule wewnętrznej zgodności wystarczają jako ramy, czy projekt powinien wprost odsyłać do konkretnych aktów (rozporządzenie UE o produktach podwójnego zastosowania, ustawa o obrocie z zagranicą towarami o znaczeniu strategicznym)?
- **Ocena brzmienia 0.9.4-C:** zgodne
- **Dlaczego zmieniono:** Klauzule ramowe są prawidłowym rozwiązaniem i w praktyce lepszym niż odesłania do konkretnych aktów. Załącznik I do rozporządzenia 2021/821 jest zmieniany aktami delegowanymi Komisji w ślad za ustaleniami reżimów międzynarodowych (art. 17 ust. 1 lit. a) [Z] (tekst EN) — w praktyce corocznie [W]; dostępna nam wersja skonsolidowana pochodzi z 26 maja 2023 r. i była później zmieniana (2023–2025). Ustawa krajowa została właśnie znowelizowana (od 22 kwietnia 2026 r. art. 2 odsyła wprost do rozporządzenia 2021/821, art. 6 porządkuje wymogi zezwoleń, art. 17a wylicza kompetencje organu kontroli obrotu, a rozdział 3a tworzy elektroniczny rejestr zezwoleń), a reżim sankcyjny zmienia się co kilka miesięcy; odesłanie sztywne w akcie notarialnym starzeje się i rodzi spory, czy obowiązek obejmuje akt następczy. § 28 ust. 1 mówi o „obowiązujących przepisach”, co jest odesłaniem dynamicznym; ust. 2–4 przenoszą materię wykonawczą tam, gdzie powinna być — do programu zgodności przyjmowanego przez Radę (§ 23 ust. 1 lit. h–i). […]
- **Rekomendacja memorandum:** Utrzymać klauzule ramowe. Uzupełnić ust. 1 o przykładowe wyliczenie aktów oraz przebudować ust. 5 tak, aby sankcja wobec akcjonariusza niefunkcjonalnego miała postać skonkretyzowanego obowiązku zbycia. W programie zgodności z ust. 4 wskazać osobę odpowiedzialną za koordynację kontroli obrotu (art. 9 ust. 2 pkt 11 ustawy), ująć obowiązek oznaczania dokumentów handlowych i umów licencyjnych (art. 11 ust. 9 rozporządzenia 2021/821), ewidencję (art. 27) oraz ocenę produktów pod kątem AI Act (wyłączenia z art. 2 ust. 3 i 8, reżim szczególny dla produktów z sekcji B załącznika I — art. 2 ust. 2). Decyzja Założycieli: czy sankcją ma być zbycie po Wartości Godziwej (neutralne dla inwestora), czy z dyskontem (co fundusze VC zakwestionują — zob. pakiet 4.4).
- **Podstawa prawna:** rozporządzenie (UE) 2021/821 (tekst skonsolidowany na 26 maja 2023 r., EN): art. 2 pkt 1–3, 9–10 i 21 (definicje produktów podwójnego zastosowania, wywozu — w tym transmisji elektronicznej i udostępnienia oprogramowania lub technologii osobom poza obszarem celnym Unii, eksportera, pomocy technicznej, wewnętrznego programu zgodności), art. 3 ust. 1, art. 4 ust. 1–2 (klauzula catch-all i obowiązek powiadomienia), art. 8 ust. 1–3 (pomoc techniczna), art. 11 ust. 1 i 9 (transfer wewnątrzunijny), art. 12 ust. 1 i 4 (rodzaje zezwoleń; ICP przy zezwoleniu globalnym), art. 17 ust. 1 (aktualizacja załączników I i IV aktami delegowanymi), art. 27 ust. 1, 3–4 (ewidencja), załącznik II sekcja A (EU001, część 2–3) i sekcja G (EU007) [Z] (tekst EN; załącznik I zmieniany po 2023 r.); rozporządzenie (UE) 2024/1689 (AI Act): art. 2 ust. 2, 3, 6 i 8, art. 3 pkt 1, art. 6 ust. 1, art. 108, art. 113, motyw 12, załącznik I sekcja B pkt 20 [Z] (tekst EN; daty stosowania do sprawdzenia pod kątem późniejszych zmian [?]); rozporządzenie (UE) 2021/697, art. 9 ust. 4 [Z]; ustawa z 29 listopada 2000 r. o obrocie z zagranicą towarami, technologiami i usługami o znaczeniu strategicznym dla bezpieczeństwa państwa, a także dla utrzymania międzynarodowego pokoju i bezpieczeństwa (t.j. Dz.U. 2023 poz. 1582, zm. Dz.U. 2026 poz. 471): art. 2, art. 3 pkt 10, art. 6, art. 9 ust. 2 pkt 11, art. 11, art. 17a, art. 24a, art. 33 ust. 1 i 2a [Z]; rozporządzenia sankcyjne UE (m.in. 833/2014, 269/2014) [W]; ustawa z 13 kwietnia 2022 r. o szczególnych rozwiązaniach w zakresie przeciwdziałania wspieraniu agresji na Ukrainę oraz służących ochronie bezpieczeństwa narodowego (t.j. Dz.U. 2025 poz. 514) [Z]; art. 300¹ § 3 KSH („akcjonariusze są zobowiązani jedynie do świadczeń określonych w umowie spółki”) [Z]; art. 300³³ § 1 pkt 11 KSH [Z]; art. 64 KC [Z].

#### § 28 ust. 5: obowiązek zbycia akcji przez akcjonariusza naruszającego kontrolę eksportu na rzecz wskazanego Dopuszczalnego Nabywcy za Wartość Godziwą jako obowiązek związany z akcją

Commit `6456051` · memorandum 4.2.1 · klasa: zalecane — odstępstwo od reguły dla oceny „zgodne” uzasadnione tym, że ust. 5 w obecnym brzmieniu nie jest wykonalny

- **Pytanie:** Czy klauzule wewnętrznej zgodności wystarczają jako ramy, czy projekt powinien wprost odsyłać do konkretnych aktów (rozporządzenie UE o produktach podwójnego zastosowania, ustawa o obrocie z zagranicą towarami o znaczeniu strategicznym)?
- **Ocena brzmienia 0.9.4-C:** zgodne
- **Dlaczego zmieniono:** Klauzule ramowe są prawidłowym rozwiązaniem i w praktyce lepszym niż odesłania do konkretnych aktów. Załącznik I do rozporządzenia 2021/821 jest zmieniany aktami delegowanymi Komisji w ślad za ustaleniami reżimów międzynarodowych (art. 17 ust. 1 lit. a) [Z] (tekst EN) — w praktyce corocznie [W]; dostępna nam wersja skonsolidowana pochodzi z 26 maja 2023 r. i była później zmieniana (2023–2025). Ustawa krajowa została właśnie znowelizowana (od 22 kwietnia 2026 r. art. 2 odsyła wprost do rozporządzenia 2021/821, art. 6 porządkuje wymogi zezwoleń, art. 17a wylicza kompetencje organu kontroli obrotu, a rozdział 3a tworzy elektroniczny rejestr zezwoleń), a reżim sankcyjny zmienia się co kilka miesięcy; odesłanie sztywne w akcie notarialnym starzeje się i rodzi spory, czy obowiązek obejmuje akt następczy. § 28 ust. 1 mówi o „obowiązujących przepisach”, co jest odesłaniem dynamicznym; ust. 2–4 przenoszą materię wykonawczą tam, gdzie powinna być — do programu zgodności przyjmowanego przez Radę (§ 23 ust. 1 lit. h–i). […]
- **Rekomendacja memorandum:** Utrzymać klauzule ramowe. Uzupełnić ust. 1 o przykładowe wyliczenie aktów oraz przebudować ust. 5 tak, aby sankcja wobec akcjonariusza niefunkcjonalnego miała postać skonkretyzowanego obowiązku zbycia. W programie zgodności z ust. 4 wskazać osobę odpowiedzialną za koordynację kontroli obrotu (art. 9 ust. 2 pkt 11 ustawy), ująć obowiązek oznaczania dokumentów handlowych i umów licencyjnych (art. 11 ust. 9 rozporządzenia 2021/821), ewidencję (art. 27) oraz ocenę produktów pod kątem AI Act (wyłączenia z art. 2 ust. 3 i 8, reżim szczególny dla produktów z sekcji B załącznika I — art. 2 ust. 2). Decyzja Założycieli: czy sankcją ma być zbycie po Wartości Godziwej (neutralne dla inwestora), czy z dyskontem (co fundusze VC zakwestionują — zob. pakiet 4.4).
- **Podstawa prawna:** rozporządzenie (UE) 2021/821 (tekst skonsolidowany na 26 maja 2023 r., EN): art. 2 pkt 1–3, 9–10 i 21 (definicje produktów podwójnego zastosowania, wywozu — w tym transmisji elektronicznej i udostępnienia oprogramowania lub technologii osobom poza obszarem celnym Unii, eksportera, pomocy technicznej, wewnętrznego programu zgodności), art. 3 ust. 1, art. 4 ust. 1–2 (klauzula catch-all i obowiązek powiadomienia), art. 8 ust. 1–3 (pomoc techniczna), art. 11 ust. 1 i 9 (transfer wewnątrzunijny), art. 12 ust. 1 i 4 (rodzaje zezwoleń; ICP przy zezwoleniu globalnym), art. 17 ust. 1 (aktualizacja załączników I i IV aktami delegowanymi), art. 27 ust. 1, 3–4 (ewidencja), załącznik II sekcja A (EU001, część 2–3) i sekcja G (EU007) [Z] (tekst EN; załącznik I zmieniany po 2023 r.); rozporządzenie (UE) 2024/1689 (AI Act): art. 2 ust. 2, 3, 6 i 8, art. 3 pkt 1, art. 6 ust. 1, art. 108, art. 113, motyw 12, załącznik I sekcja B pkt 20 [Z] (tekst EN; daty stosowania do sprawdzenia pod kątem późniejszych zmian [?]); rozporządzenie (UE) 2021/697, art. 9 ust. 4 [Z]; ustawa z 29 listopada 2000 r. o obrocie z zagranicą towarami, technologiami i usługami o znaczeniu strategicznym dla bezpieczeństwa państwa, a także dla utrzymania międzynarodowego pokoju i bezpieczeństwa (t.j. Dz.U. 2023 poz. 1582, zm. Dz.U. 2026 poz. 471): art. 2, art. 3 pkt 10, art. 6, art. 9 ust. 2 pkt 11, art. 11, art. 17a, art. 24a, art. 33 ust. 1 i 2a [Z]; rozporządzenia sankcyjne UE (m.in. 833/2014, 269/2014) [W]; ustawa z 13 kwietnia 2022 r. o szczególnych rozwiązaniach w zakresie przeciwdziałania wspieraniu agresji na Ukrainę oraz służących ochronie bezpieczeństwa narodowego (t.j. Dz.U. 2025 poz. 514) [Z]; art. 300¹ § 3 KSH („akcjonariusze są zobowiązani jedynie do świadczeń określonych w umowie spółki”) [Z]; art. 300³³ § 1 pkt 11 KSH [Z]; art. 64 KC [Z].

### § 29. Zakaz konkurencji, konflikt interesów i transakcje z podmiotami powiązanymi

#### § 29 ust. 8 lit. b: 14-dniowy termin zwołania WZ w celu powołania dodatkowego dyrektora po stwierdzeniu braku zdolności Rady do podjęcia uchwały

Commit `8ef66e0` · memorandum 2.3.1 · klasa: opcjonalne

- **Pytanie:** Czy uchwała Walnego Zgromadzenia może zastąpić uchwałę Rady w sprawach, dla których ustawa sama wymaga uchwały Rady (w szczególności art. 300⁷⁵ § 2 KSH), gdy wyłączenia dyrektorów uniemożliwiają jej podjęcie? Jeżeli nie — jaki tryb rezerwowy jest dopuszczalny?
- **Ocena brzmienia 0.9.4-C:** zgodne (w brzmieniu 0.9.4)
- **Dlaczego zmieniono:** Odpowiedź brzmi: nie, i projekt już to przyjmuje. Art. 300⁷⁵ § 2 przydziela decyzje strategiczne, plany i strukturę Radzie jako organowi, a Walne Zgromadzenie nie ma w P.S.A. kompetencji do prowadzenia spraw; uchwała akcjonariuszy może być zgodą właścicielską, ale nie decyzją organu prowadzącego sprawy. § 29 ust. 8 lit. b) wyraża to poprawnie: „uchwała Walnego Zgromadzenia nie zastępuje uchwały Rady; transakcja nie może zostać zawarta do czasu przywrócenia zdolności Rady”, a ust. 8 lit. a) słusznie ogranicza substytucję do wymogów czysto umownych (tam art. 17 § 3 i tak pozbawia brak uchwały skutku zewnętrznego). Wątpliwość audytu do wersji 0.8 jest zatem rozwiązana. […]
- **Rekomendacja memorandum:** Bez zmian normatywnych. Opcjonalnie: w § 21 ust. 2 dodać, że co najmniej jeden dyrektor niewykonawczy nie jest akcjonariuszem ani Osobą Bliską akcjonariusza (rezerwa na wypadek konfliktu), a w § 29 ust. 8 — termin, w którym Rada zwołuje WZ w celu powołania dodatkowego dyrektora (np. 14 dni).
- **Podstawa prawna:** art. 300⁷⁵ § 2 KSH [Z]; art. 300⁵⁵ § 1 KSH (obowiązek ujawnienia i wstrzymania się od udziału w rozstrzyganiu) [Z]; art. 300⁵⁸ § 2 KSH (quorum) [Z]; art. 300⁷³ § 3 KSH (powoływanie dyrektorów uchwałą akcjonariuszy) [Z]; art. 300⁷⁹ KSH [Z]; art. 17 § 1–3 KSH [Z]; art. 300⁸⁰ § 1–3 KSH (uchwała akcjonariuszy poza WZ; tajne głosowanie z art. 300⁹⁹ § 2 nie ma tu zastosowania) [Z].

### § 30. Transakcje z Akcjonariuszami i podmiotami powiązanymi

#### § 30: usunięcie oznaczenia roboczego [WYMAGA OPINII PRAWNIKA]

Commit `59fa2c7` · memorandum 4.3.1, K16 · klasa: konieczne — odstępstwo od reguły uzasadnione: bez czynności redakcyjnych tekst nie może stać się aktem notarialnym; zmiany merytoryczne nie są konieczne

- **Pytanie:** Jaka forma zawiązania i jakie dokumenty do KRS są wymagane (w tym dokumentacja wkładów niepieniężnych) i które postanowienia projektu mogą wywołać zastrzeżenia sądu rejestrowego (ograniczenia zbywalności, Kryterium, obowiązki związane z akcją, uchwały ramowe)?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo — co do treści; w obecnej postaci redakcyjnej (przekreślenia, oznaczenia robocze, puste pola) tekst nie nadaje się do aktu i wywołałby wezwanie sądu, co kwalifikujemy jako ryzyko formalne
- **Dlaczego zmieniono:** **Forma.** Umowa nie korzysta ze wzorca, więc „powinna być zawarta w formie aktu notarialnego” (art. 300⁶). Wszyscy Założyciele stawają osobiście albo przez pełnomocnika z pełnomocnictwem w formie aktu notarialnego (art. 99 § 1 KC). Załączniki nr 1–3 muszą być objęte aktem, bo Załącznik nr 1 zawiera elementy obowiązkowe umowy („liczbę, serie i numery akcji, związane z nimi uprzywilejowanie, akcjonariuszy obejmujących poszczególne akcje oraz cenę emisyjną akcji”, a przy wkładach niepieniężnych ich przedmiot i akcje za nie obejmowane — art. 300⁵ § 1 pkt 3–5), a Załącznik nr 2 uruchamia mechanizm z § 10. […]
- **Rekomendacja memorandum:** Sporządzić wersję „do aktu” bez przekreśleń, oznaczeń i pól; objąć aktem uchwały założycielskie (powołanie pierwszej Rady, wybór podmiotu prowadzącego rejestr, ewentualnie zatwierdzenie Załączników); przygotować pakiet dokumentów wkładowych na dzień aktu (§ 7 ust. 4 zdanie ostatnie); przygotować listę akcjonariuszy z art. 300¹² § 4 i — jeżeli którykolwiek dyrektor ma adres poza UE — pełnomocnika do doręczeń z art. 19a ust. 5a ustawy o KRS. Potwierdzić u doradcy podatkowego brak PCC od umowy P.S.A. Uprawniony prawnik powinien potwierdzić bieżącą praktykę PRS co do formy załączników.
- **Podstawa prawna:** art. 300⁵ § 1 KSH (elementy umowy) [Z]; art. 300⁶ KSH (forma aktu notarialnego) [Z]; art. 300⁷ § 1 i 4 KSH (wzorzec — niewykorzystany; przy wzorcu tylko wkłady pieniężne) [Z]; art. 300⁹ § 1 KSH (wniesienie wkładów w całości w 3 lata od wpisu) [Z]; art. 300¹⁰ § 1 KSH (wyrównanie znacznie zawyżonego wkładu na kapitał akcyjny) [Z]; art. 300¹¹ § 1–2 KSH (spółka w organizacji; reprezentacja) [Z]; art. 300¹² § 1–4 KSH (zgłoszenie, załączniki, lista akcjonariuszy) [Z]; art. 300¹³ § 1–2 w zw. z art. 164 § 3, art. 165, art. 169 § 1 i art. 172 KSH (drobne uchybienia, braki usuwalne, termin 6 miesięcy, braki po wpisie) [Z]; art. 7, art. 19 ust. 2 i 5–6, art. 19a ust. 5, 5a i 5d, art. 20a ust. 1 i 3, art. 23 ust. 1 ustawy o KRS [Z]; art. 130 § 1–3 KPC [Z]; art. 40 pkt 1 ustawy o KRS [Z]; art. 52 ust. 1 i art. 55 ust. 1 ustawy o kosztach sądowych w sprawach cywilnych (500 zł za wpis; 250 zł za zmianę) [Z]; opłata za ogłoszenie w MSiG 100 zł [W]; art. 99 § 1 KC [Z]; art. 53 ustawy o prawie autorskim, art. 12 ust. 1–2 i art. 67 ust. 2–3 PWP [Z]; ustawa o PCC: art. 1 ust. 1 pkt 1 lit. k, art. 1a pkt 1–2, art. 6 ust. 1 pkt 8 lit. a, art. 7 ust. 1 pkt 9 [Z]; art. 60 ust. 1 pkt 1 ustawy o przeciwdziałaniu praniu pieniędzy (CRBR: 14 dni od wpisu) [Z]; art. 300³¹ § 5 i art. 300³² § 1 KSH [Z]; art. 300³⁹ § 1–2 KSH [Z]; art. 300³³ § 1 pkt 10–11 KSH [Z]; art. 300⁹⁸ § 2 i art. 300¹⁰³ KSH [Z]; art. 300¹ § 3 KSH [Z].

#### § 30 ust. 2 i 5: granica wartości godziwej (art. 300^21 KSH) z sankcją zwrotu oraz katalog transakcji z akcjonariuszami wymagających uchwały WZ 75% Głosów Uprawnionych w Sprawie

Commit `8c30ca4` · memorandum 2.3.4 · klasa: zalecane

- **Pytanie:** § 30: jak pojęcie „godziwych warunków” ma się do ustawowych ograniczeń świadczeń na rzecz akcjonariuszy (art. 300¹⁵ i n. KSH); czy brak obowiązku przetargu i progi ustalane w regulaminie albo uchwale są bezpieczne; które większe transakcje powinny wymagać zgody Walnego Zgromadzenia?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** „Godziwe warunki” a ograniczenia wypłat. KSH pozwala wypłacać akcjonariuszom tylko z zysku i kapitału akcyjnego, w granicach testów z art. 300¹⁵ § 2 i 5, a każde świadczenie sprzeczne z prawem lub umową podlega zwrotowi (art. 300²²). W P.S.A. nie trzeba sięgać do doktrynalnej koncepcji „ukrytej wypłaty”: art. 300²¹ KSH stanowi wprost, że wartość świadczeń spółki na rzecz akcjonariuszy z innego tytułu niż prawa z akcji, a także na rzecz spółek lub spółdzielni z nimi powiązanych, dominujących lub zależnych, „nie może przekraczać wartości godziwej świadczenia wzajemnego otrzymanego przez spółkę”. […]
- **Rekomendacja memorandum:** Doprecyzować ust. 2 (odesłanie do art. 300²¹ KSH: wartość świadczenia Spółki nie wyższa niż wartość godziwa świadczenia wzajemnego, także wobec podmiotów powiązanych spoza literalnego zakresu przepisu; nadwyżka do zwrotu), przenieść progi z regulaminu do umowy jako nowy ust. 5 z listą transakcji wymagających uchwały WZ, objąć nim umowy kredytu, pożyczki i poręczenia z dyrektorem niezależnie od art. 15 KSH; usunąć oznaczenie „[WYMAGA OPINII PRAWNIKA]” po potwierdzeniu przez radcę prawnego. Decyzja Założycieli: wysokość progu rocznego (500 000 zł) i objęcie mienia nabywanego od Założycieli w okresie 2 lat.
- **Podstawa prawna:** art. 300²¹ KSH („Wartość świadczeń spełnianych przez spółkę na rzecz akcjonariuszy z innego tytułu niż prawa wynikające z akcji, a także na rzecz spółek lub spółdzielni z nimi powiązanych albo pozostających wobec nich w stosunku dominacji lub zależności, nie może przekraczać wartości godziwej świadczenia wzajemnego otrzymanego przez spółkę”) [Z]; art. 300¹⁵ § 2 i 5 KSH (test bilansowy; test wypłacalności na 6 miesięcy) [Z]; art. 300²² § 1–4 KSH (zwrot wypłaty „dokonanej wbrew przepisom prawa lub postanowieniom umowy spółki”; solidarna odpowiedzialność członków organów, „chyba że nie ponoszą winy”; zakaz zwolnienia; przedawnienie 3 lata, chyba że odbiorca wiedział o bezprawności) [Z]; art. 300¹²⁹ KSH (actio pro socio do roszczeń o zwrot wypłat) [Z]; art. 20 KSH [Z]; art. 17 KSH [Z]; art. 15 § 1 KSH (nie wymienia dyrektora P.S.A. — pkt 2.2.4) [Z]; art. 300⁵⁵ i 300⁷⁹ KSH [Z]; art. 394 § 1 KSH (S.A.: nabycie mienia od założyciela lub akcjonariusza za cenę ponad 1/10 wpłaconego kapitału zakładowego przed upływem dwóch lat od zarejestrowania — uchwała WZ większością 2/3; brak odpowiednika w P.S.A., wzorzec) [Z]; art. 23m–23zf ustawy o PIT (rozdział 4b: ceny transferowe; podmioty powiązane od 25% udziałów lub głosów, art. 23m ust. 1 pkt 4) [Z]; art. 11a–11t ustawy o CIT [W]; art. 61 rozporządzenia finansowego (UE) 2018/1046 i zasada konkurencyjności w programach dotacyjnych [W].

### § 31. Finansowanie Spółki

#### § 31 ust. 4: prawo weta zawężone do sprzeciwu wobec uchwał organów, wyłączenie zwyczajowych kowenantów i postanowień umów o dofinansowanie

Commit `977b236` · memorandum 3.3.4 · klasa: zalecane

- **Pytanie:** Czy ograniczenia z § 31 ust. 3–4 (instrumenty zamienne, zabezpieczenia na IP) nie utrudnią finansowania dłużnego i grantowego i czy są egzekwowalne wobec finansujących?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Dwie obserwacje redakcyjne poprzedzają ocenę. Po pierwsze, ust. 3 odwołuje się do „wymogów Dopuszczalnego Nabywcy”, a Dopuszczalny Nabywca to w § 11 ust. 1 wyłącznie test prawnej dopuszczalności (sankcje, zakazy) — nie Kryterium Bezpieczeństwa EU/NATO. Ust. 3 jest więc łagodniejszy, niż zakłada opis w pytaniu i w `vc.md`: bank czy leasingodawca spoza UE/NATO nie jest nim objęty, a zabroniony jest tylko skutek w postaci kontroli, praw do akcji albo do Kluczowej Własności Intelektualnej po stronie podmiotu objętego zakazem prawnym — czego prawo zabrania i bez umowy. […]
- **Rekomendacja memorandum:** Rozstrzygnąć (decyzja Założycieli), czy ust. 3 ma odsyłać do Kryterium; zawęzić „prawo weta” do prawa sprzeciwu wobec uchwał organów Spółki; dodać wyłączenie dla standardowych postanowień umów o dofinansowanie i kowenantów kredytowych.
- **Podstawa prawna:** art. 17 § 1–3 KSH [Z]; art. 300⁷⁷ § 2 KSH (nieograniczalność prawa reprezentacji dyrektora wobec osób trzecich), art. 300⁵³ KSH [Z]; art. 300⁸¹ pkt 2 i 4, art. 300¹¹⁴ § 3 KSH (uchwały akcjonariuszy wymagane ustawą) [Z]; art. 300¹ § 3 KSH [Z]; art. 7 ustawy o zastawie rejestrowym i rejestrze zastawów [W]; art. 9 ust. 3–4 rozporządzenia (UE) 2021/697 (EDF: odbiorcy i podwykonawcy uczestniczący w działaniu nie podlegają kontroli niestowarzyszonego państwa trzeciego ani podmiotu z takiego państwa; podmiot kontrolowany kwalifikuje się tylko na podstawie gwarancji zatwierdzonych przez państwo siedziby, które według ust. 4 lit. c muszą m.in. zapewniać, że odbiorca pozostanie właścicielem praw własności intelektualnej i rezultatów działania, a te nie będą podlegać kontroli ani ograniczeniu ze strony takiego państwa lub podmiotu ani nie zostaną wyeksportowane poza Unię i państwa stowarzyszone bez zgody państwa siedziby), art. 2 pkt 6 i 24, art. 5, art. 20 ust. 3–4 i 9, art. 23 ust. 2–4 rozporządzenia (UE) 2021/697 [Z]; art. 2 pkt 1 rozporządzenia (UE) 2026/1386 [Z] (tekst EN); § 11 ust. 1 i 6.

### § 32. Kwalifikowana Runda Finansowania

#### § 32 ust. 4 lit. f: katalog spraw wymagających zgody większości akcji serii wyemitowanej w Kwalifikowanej Rundzie bez odrębnej uchwały 75%, wygaśnięcie poniżej progu udziału

Commit `77da93d` · memorandum 4.4.1, 4.4.2 brzmienie VI · klasa: zalecane, zalecane — odstępstwo od reguły „zgodne warunkowo → zalecane” nie jest potrzebne; brzmienia podajemy, bo zmiany są proste i jednoznaczne

*Pytanie 4.4.1.*

- **Pytanie:** Które postanowienia (Kryterium, mechanizm przy odmowie zgody, zwrotne zbycie, drag-along 75 %, Sprawy Zastrzeżone 75 %, ograniczenia finansowania) w Państwa doświadczeniu budzą zastrzeżenia funduszy na etapie seed/serii A i co zwykle jest przedmiotem negocjacji?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo — żadne z ocenianych postanowień nie jest prawnie wadliwe; sześć z nich odbiega od standardu rynkowego w sposób, który wydłuży negocjacje albo zawęzi krąg funduszy
- **Dlaczego zmieniono:** Zastrzeżenia omawiamy w kolejności, w jakiej zwykle pojawiają się w term sheecie, z rozróżnieniem trzech grup funduszy: (G) fundusze generalistyczne działające jako ASI z kapitałem PFR/BGK/EIF i przewagą polskich albo unijnych inwestorów — w programach PFR Ventures udział PFR w kapitalizacji funduszu wynosi maksymalnie 80% (PFR Starter: bilety do 5 mln PLN, przede wszystkim spółki przed pierwszą komercyjną sprzedażą, wkład prywatny min. 20%, `pfr_pfrv_starter.txt`) albo do 60% (PFR KOFFI: etap wzrostu, bilety od 4 mln PLN, min. 85% wartości portfela w spółkach z siedzibą w Polsce, wkład prywatny min. 40%, `pfr_pfrv_koffi.txt`; PFR Otwarte Innowacje w strukturze standardowej: bilety 5–70 mln PLN, program także „w obszarze zaawansowanych technologii obronnych i dual-use”, wkład prywatny min. 40%, `pfr_pfrv_otwarte_innowacje.txt`) [Z]; przy KOFFI PFR wymaga rejestracji ZASI najpóźniej przy podpisaniu umowy i oczekuje zdywersyfikowanej struktury LP (`pfr_pfrv_koffi.txt`), a przy Starterze due diligence obejmuje ryzyka ze struktury inwestorskiej, „m.in. stopnia dywersyfikacji inwestorskiej Funduszu” (`pfr_pfrv_starter.txt`) [Z], więc największym LP takiego funduszu jest polski podmiot publiczny, a pozostali LP są rozproszeni. Inaczej w modelach koinwestycyjnych: w PFR Biznest kapitalizację funduszu tworzą tylko PFR i zarządzający, a min. 40% wartości każdej inwestycji wnoszą inwestorzy prywatni, w tym aniołowie biznesu, poza funduszem (`pfr_pfrv_biznest.txt`); w modelu koinwestycyjnym PFR OI wkład PFR może sięgać 97% kapitalizacji funduszu, a prywatne min. 40% wnoszą koinwestorzy dobierani „deal by deal” bezpośrednio do spółki, każdy za akceptacją PFR OI (`pfr_pfrv_otwarte_innowacje.txt`) [Z] — tu aniołowie i koinwestorzy stają się akcjonariuszami Spółki obok funduszu, więc Kryterium i zgoda Rady dotyczą każdego z nich osobno; […]
- **Rekomendacja memorandum:** Rozstrzygnąć przed rundą, nie w jej trakcie, cztery punkty sporne z każdym funduszem: test Kryterium dla funduszy (§ 11 ust. 14 i 15), przeniesienia dozwolone (§ 12), ochrona serii inwestorskiej przy drag (§ 16) i katalog spraw wymagających zgody serii (§ 32 ust. 4). Pozostałe punkty zostawić do term sheetu. Brzmienia w odpowiedzi na pytanie 4.4.2. Wybór, czy szukać inwestora w grupie G/D (mniejsze zmiany), czy także Z (zmiany w § 21 ust. 3 i wariant A w § 12 ust. 3), należy do Założycieli.
- **Podstawa prawna:** art. 300³⁹ § 1–6 KSH [Z]; art. 300⁴⁷ KSH [Z]; art. 300¹⁰³–300¹⁰⁷ KSH [Z]; art. 300¹⁰⁶ § 2 KSH (pozbawienie prawa poboru) [Z]; art. 300²⁵ § 1–2 KSH (akcje uprzywilejowane; katalog otwarty: uprzywilejowanie „może dotyczyć w szczególności prawa głosu, prawa do dywidendy lub podziału majątku w przypadku likwidacji spółki”) [Z]; art. 300²⁸ § 1–2 KSH (uprawnienia indywidualne oznaczonego akcjonariusza, „w szczególności uprawnienie do powołania lub odwołania członków zarządu lub rady nadzorczej”, wygasające najpóźniej z utratą statusu akcjonariusza, „chyba że umowa spółki stanowi inaczej”) [Z]; art. 300¹⁰⁴ § 1 pkt 2 KSH (uprzywilejowanie akcji nowej emisji w uchwale o emisji) [Z]; art. 2 pkt 6 i 24, art. 5 i art. 9 ust. 1–4 i 7 rozporządzenia (UE) 2021/697 (EDF) [Z]; art. 2 pkt 1, 5 i 7, art. 4 ust. 2, 9 i 15, art. 5 ust. 1–2, art. 15 ust. 1 lit. b i ust. 3, art. 19 ust. 2 lit. e oraz motywy 14–15 rozporządzenia (UE) 2026/1386 (kontrola inwestycji zagranicznych, stosowane od 17 stycznia 2028 r., art. 31) [Z] (tekst EN); art. 2 ust. 2 pkt 1 ustawy z 2018 r. o przeciwdziałaniu praniu pieniędzy oraz finansowaniu terroryzmu (beneficjent rzeczywisty: osoba fizyczna sprawująca kontrolę, w tym mająca „więcej niż 25% ogólnej liczby udziałów lub akcji” albo głosów, a w braku takiej osoby — osoba na wyższym stanowisku kierowniczym) [Z]; ustawa o kontroli niektórych inwestycji [W]; praktyka rynkowa: wzorce NVCA po aktualizacji z 2 października 2025 r. (`web_nvca_2025_press.txt`, `web_nvca_2025_foley.txt`) [Z], omówienia PFR Startup (`web_pfr_umowa_inwestycyjna.txt`, `pfr_startup_umowa_inwestycyjna.txt`, pfr_startup_term_sheet.txt) [Z], strony programów PFR Ventures (`pfr_pfrv_starter.txt`, `pfr_pfrv_biznest.txt`, `pfr_pfrv_otwarte_innowacje.txt`, `pfr_pfrv_koffi.txt`) [Z], wzorce BVCA i treść wzorów term sheet PFR Ventures (same wzory nie zostały pobrane, `pfr_pfrv_feng_dokumentacja.txt`) [W].

*Pytanie 4.4.2.*

- **Pytanie:** Jakie zmiany ułatwiłyby dostosowanie umowy do rundy bez naruszenia jej założeń (bezpieczeństwo właścicielskie, kontrola eksportu, mechanizm zwrotnego zbycia)?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo — założenia umowy da się utrzymać w całości; potrzebne są cztery zmiany w umowie spółki przed rundą i przeniesienie reszty do dokumentów rundy
- **Dlaczego zmieniono:** Kryterium zmian jest jedno: nic, co decyduje o dostępie do EDF, EUDIS, DIANA/NIF i koncesji, nie może zostać osłabione (warunki EDF: siedziba i „zarządcze struktury wykonawcze” w Unii lub w państwie stowarzyszonym oraz brak „kontroli niestowarzyszonego państwa trzeciego lub podmiotu z niestowarzyszonego państwa trzeciego”, art. 9 ust. 1–3 rozporządzenia 2021/697, z derogacją za gwarancjami zatwierdzonymi przez państwo członkowskie lub stowarzyszone siedziby z art. 9 ust. 4 [Z]; państwa stowarzyszone to według art. 5 członkowie EFTA należący do EOG, których rozporządzenie nie wymienia z nazwy [Z], w praktyce obecnie Norwegia, `web_edf_gowling.txt` [Z]; warunek NIF: siedziba w jednym z 24 państw NATO będących jego inwestorami, `web_nif_about.txt` [Z]). Te założenia to: (i) kontrola nad Spółką pozostaje w rękach osób i podmiotów z UE/EOG/NATO, a — jeżeli Założyciele przyjmą decyzję D6 — z UE/EOG; (ii) dostęp do Kluczowej Własności Intelektualnej spoza UE/NATO tylko za zgodą Rady po analizie eksportowej (§ 27 ust. 6, § 28); […]
- **Rekomendacja memorandum:** Wprowadzić zmiany A.1–A.4 przed pierwszym term sheetem (A.1 i A.3 warunkują w praktyce rozmowę z funduszami D i Z); A.5 i A.6 zależnie od decyzji Założycieli o kręgu inwestorów; A.7 po stanowisku kancelarii. Resztę zostawić dokumentom rundy. Brzmienia poniżej są sugestią do weryfikacji przez uprawnionego prawnika, w szczególności co do art. 300³⁹ § 2 KSH (wyłączenie zgody Spółki dla kategorii przeniesień) i ujawnienia w rejestrze akcjonariuszy.
- **Podstawa prawna:** art. 300³⁹ § 1–2 KSH („chyba że umowa spółki stanowi inaczej”) [Z]; art. 300²⁵ § 1–2 i art. 300²⁸ § 1–2 KSH [Z]; art. 300³³ § 1 pkt 4 i 10 KSH (rejestr akcjonariuszy zawiera „rodzaj danej akcji i uprawnienia szczególne z akcji” oraz „ograniczenia co do rozporządzania akcją”) [Z]; art. 300¹⁰³ KSH (emisja na podstawie postanowień umowy „przewidujących maksymalną liczbę akcji i termin ich emisji” bez trybu zmiany umowy) [Z]; art. 300¹⁰⁴ § 1 pkt 2 KSH [Z]; art. 300¹⁰⁶ § 1–2 KSH (prawo poboru, „jeżeli umowa spółki lub uchwała akcjonariuszy nie stanowią inaczej”; pozbawienie uchwałą większością 4/5) [Z]; art. 2 pkt 6 i 24, art. 5 i art. 9 ust. 1–4 i 7 rozporządzenia (UE) 2021/697 [Z]; art. 2 pkt 1, 5 i 7, art. 4 ust. 1, 2, 9 i 15 lit. a–c, art. 5 ust. 1–2, art. 6, art. 11 ust. 3 i 5, art. 20 ust. 4 lit. a, art. 30–31, motywy 14–15 i 20, zał. I pkt 1–3 i zał. II pkt 14 rozporządzenia (UE) 2026/1386 [Z] (tekst EN); rozporządzenie (UE) 2021/821 (unijny system kontroli wywozu, pośrednictwa, pomocy technicznej, tranzytu i transferu produktów podwójnego zastosowania; do jego zał. I odsyła art. 4 ust. 15 lit. a rozporządzenia 2026/1386) [Z] (tekst EN, konsolidacja na 26.05.2023 r.); art. 12a ust. 1 pkt 1, art. 12c ust. 1 pkt 1 i 5, ust. 4–5 oraz art. 12d ust. 3 pkt 7 i ust. 4 ustawy o kontroli niektórych inwestycji [Z]; art. 2 ust. 2 pkt 1 ustawy AML [Z].

#### § 32 ust. 3: zobowiązanie do głosowania obejmuje uchwałę o emisji, zmianie umowy, pozbawieniu prawa poboru i uchwały wykonawcze Rundy; umowa wykonawcza § 13 ust. 6-7: kara umowna i nieodwołalne pełnomocnictwo do głosowania

Commit `39cedfd` · memorandum 3.3.1 · klasa: zalecane

- **Pytanie:** Czy zobowiązanie do głosowania i współdziałania (§ 32 ust. 3) jest skuteczne wobec akcjonariuszy i egzekwowalne, czy pozostaje jedynie zobowiązaniem odszkodowawczym?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Umowy o sposób wykonywania prawa głosu są w orzecznictwie i doktrynie uznawane za dopuszczalne w granicach art. 353¹ KC: nie mogą naruszać bezwzględnie obowiązujących przepisów, interesu spółki ani prowadzić do „sprzedaży” głosu; zobowiązanie z § 32 ust. 3 mieści się w tych granicach, bo jest ograniczone do uchwał zgodnych z uchwałą kierunkową, wyłącza głosowanie sprzeczne z prawem i interesem Spółki i nie nakłada obowiązku wniesienia środków [W]. Umieszczenie go w umowie spółki ma dwie zalety wobec umowy akcjonariuszy: „akcjonariusze są zobowiązani jedynie do świadczeń określonych w umowie spółki” (art. 300¹ § 3 [Z]), więc obowiązek wiąże także każdego późniejszego nabywcę akcji, a jego naruszenie jest naruszeniem umowy spółki (§ 36). Skuteczność ma jednak trzy granice. […]
- **Rekomendacja memorandum:** Utrzymać ust. 3 i rozszerzyć go na uchwały wykonawcze przewidziane w dokumentach Rundy oraz na uchwałę o pozbawieniu prawa poboru; w umowie akcjonariuszy dodać karę umowną i nieodwołalne pełnomocnictwo do głosowania w sprawach objętych uchwałą kierunkową, z ograniczeniem do jej treści.
- **Podstawa prawna:** art. 300¹ § 3 KSH [Z]; art. 353¹, art. 64, art. 101 § 1, art. 471, art. 483 § 1 KC [Z]; art. 1047 § 1 KPC [Z]; art. 300¹⁰¹ KSH w zw. z art. 422 § 1 KSH [Z]; SN, wyrok z 9 grudnia 2022 r., II CSKP 593/22 [Z]; SN, wyrok z 23 czerwca 2020 r., V CSK 522/18 [Z].
- **Orzecznictwo:** II CSKP 593/22, V CSK 522/18 (zob. sekcja 6)

#### § 32 ust. 4: rozróżnienie warunków inwestorskich wprowadzanych zmianą umowy Spółki (uprzywilejowanie, prawo wskazania dyrektora, zgoda serii z lit. f) od kontraktowych; zgoda właścicielska w uchwale kierunkowej

Commit `44c7526` · memorandum 3.3.2, K15 · klasa: konieczne

- **Pytanie:** Czy warunki inwestorskie z § 32 ust. 4 mogą zostać przyznane bez zmiany umowy spółki (uprzywilejowanie akcji, prawa osobiste inwestora), czy ich część wymaga zmiany umowy w formie aktu notarialnego?
- **Ocena brzmienia 0.9.4-C:** ryzyko (sformułowanie „bez konieczności odrębnej zmiany pozostałych postanowień niniejszej umowy” jest mylące co do formy)
- **Dlaczego zmieniono:** Podział jest następujący. (a) *Uprzywilejowanie likwidacyjne* — „spółka może emitować akcje o szczególnych uprawnieniach, które powinny być określone w umowie spółki”, a uprzywilejowanie może dotyczyć w szczególności „podziału majątku w przypadku likwidacji spółki” (art. 300²⁵ § 1–2 [Z]; art. 300⁵ § 1 pkt 3). Uchwała o emisji określa uprzywilejowanie, „jeżeli uchwała przewiduje uprzywilejowanie akcji nowej emisji” (art. 300¹⁰⁴ § 1 pkt 2 [Z]) — ale ponieważ emisja jest zmianą umowy (art. 300¹⁰³), taka uchwała jest zarazem zmianą umowy w protokole notarialnym; że wymaga to poziomu umowy, potwierdza zakaz emitowania akcji uprzywilejowanych i przyznawania uprawnień indywidualnych przez Radę działającą na podstawie upoważnienia (art. 300¹¹⁰ § 5 [Z]). […]
- **Rekomendacja memorandum:** Przeredagować ust. 4 tak, aby rozróżniał warunki wprowadzane zmianą umowy Spółki (a, c, zgody serii) od kontraktowych (b, d, e) i utrzymywał zgodę właścicielską na poziomie uchwały kierunkowej. Rozważyć predefiniowaną serię I jako wariant.
- **Podstawa prawna:** art. 300⁵ § 1 pkt 3, art. 300²⁵ § 1–2, art. 300²⁶ KSH (akcje uprzywilejowane, akcje założycielskie) [Z]; art. 300²⁸ § 1–2 KSH (uprawnienia indywidualne akcjonariusza — odpowiednik art. 354 KSH) [Z]; art. 300¹² § 2 pkt 4–5, art. 300³³ § 1 pkt 4 KSH [Z]; art. 300⁷³ § 3 KSH (dyrektorów powołują akcjonariusze uchwałą, chyba że umowa stanowi inaczej) [Z]; art. 300⁹⁸ § 4–5, art. 300¹⁰⁰ § 2, art. 300¹⁰²–300¹⁰⁴, art. 300¹⁰⁶ § 1–2, art. 300¹¹⁰ § 5 KSH [Z]; art. 353¹ KC [Z]; art. 2 pkt 1, 5 i 7, art. 4 ust. 1, 2, 9 i 15, art. 5 ust. 2 lit. a, art. 11 ust. 3 i 5, art. 30 ust. 3, art. 31 oraz załącznik II pkt 14 rozporządzenia (UE) 2026/1386 [Z] (tekst EN).

### § 33. Spółki celowe i wspólne przedsięwzięcia produkcyjne

#### § 33 ust. 2a: sposób liczenia łącznego zaangażowania, Limit Zaangażowania zatwierdzany przez WZ, obowiązek informacyjny przed utratą kontroli, reguła kolizyjna z § 25 ust. 1 lit. k i § 31 ust. 5

Commit `8b341fa` · memorandum 2.4.4 · klasa: zalecane

- **Pytanie:** Czy progi kwotowe i podział kompetencji Rada / Walne Zgromadzenie są wykonalne przy zmianach zaangażowania w czasie (np. dokapitalizowanie spółki celowej)?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Podział jest wykonalny co do zasady, bo próg jest „łączny” (kumulatywny) i obejmuje wkłady, udziały, pożyczki i zabezpieczenia (ust. 2 zd. 2), a utrata kontroli i wniesienie Kluczowej Własności Intelektualnej są odrębnymi wyzwalaczami WZ (lit. n). Problemy ujawniają się w czasie. (1) Sposób liczenia: umowa nie mówi, czy zabezpieczenia liczy się według sumy gwarancyjnej, pożyczki według kapitału, wkłady rzeczowe według wartości godziwej, ani czy spłacona pożyczka albo wygasła gwarancja obniża „łączne zaangażowanie”; nie wiadomo też, czy licencja z ust. 3 (bez wynagrodzenia albo z royalties) ma wartość zaliczaną do progu. […]
- **Rekomendacja memorandum:** Dodać w § 33 ust. 2 zasady liczenia zaangażowania i instytucję Limitu Zaangażowania: WZ zatwierdza dla danego Przedsięwzięcia limit (kwotę i rodzaje instrumentów), w ramach którego Rada decyduje o kolejnych transzach bez odrębnej uchwały; obowiązek informacyjny Rady przed zaniechaniem prowadzącym do utraty kontroli; reguła kolizyjna z lit. k i § 31.
- **Podstawa prawna:** art. 300⁷⁵ § 2 KSH [Z]; art. 17 § 1 i 3 KSH [Z]; art. 300⁸¹ pkt 2 KSH („zbycie i wydzierżawienie przedsiębiorstwa albo jego zorganizowanej części oraz ustanowienie na nich ograniczonego prawa rzeczowego” — uchwała akcjonariuszy z mocy ustawy, bez klauzuli opt-out, gdy wkład do Przedsięwzięcia ma taki charakter) [Z]; art. 300⁹⁸ § 2 pkt 2 KSH (zbycie przedsiębiorstwa albo ZCP — 3/4 głosów) [Z]; § 23 ust. 1 lit. d), f), k), § 25 ust. 1 lit. f), n), § 31 ust. 4–5.

#### § 33 ust. 3: własność ulepszeń niewydzielnych, dla pozostałych licencja niewyłączna z sublicencją i prawo pierwszeństwa, wyłączność w granicach prawa konkurencji, dokumentowana ocena Rady

Commit `ebc4d12` · memorandum 2.4.1 · klasa: zalecane

- **Pytanie:** Czy licencja niewyłączna ograniczona do zakresu przedsięwzięcia z prawami do ulepszeń dla Spółki jest zgodna z prawem konkurencji (porozumienia o transferze technologii) i nie rodzi obowiązków z kontroli eksportu przy udostępnieniu partnerom?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Prawo konkurencji. Licencja niewyłączna, ograniczona do produktu, pola eksploatacji, terytorium i czasu, jest klasycznym porozumieniem o transferze technologii i — przy udziałach rynkowych nieprzekraczających 20% (konkurenci, łącznie) albo 30% (niekonkurenci, każda ze stron) — korzysta z wyłączenia grupowego (art. 3 ust. 1–2; po późniejszym przekroczeniu progu wyłączenie trwa jeszcze trzy lata kalendarzowe, art. 8 lit. e) [Z] (tekst EN); ograniczenia pola i terytorium są w umowach licencyjnych co do zasady dozwolone. Problemem jest ulepszeniowa część ust. 3: „prawa do ulepszeń […] przysługują Spółce, a jeżeli nie jest to prawnie możliwe — nieodpłatna, wyłączna i bezterminowa licencja z prawem sublicencji”. […]
- **Rekomendacja memorandum:** Zmienić ust. 3 tak, aby cel (Spółka kontroluje ulepszenia Kluczowej Własności Intelektualnej) był realizowany w wariantach o możliwie niskim ryzyku: własność ulepszeń niewydzielnych (także ona wypada spod wyłączenia grupowego — art. 5 ust. 1 lit. a rozporządzenia 2026/877 — i opiera się na ocenie indywidualnej, z reguły korzystnej); dla ulepszeń wydzielnych — licencja niewyłączna z prawem sublicencji plus prawo pierwszeństwa nabycia; wyłączność tylko w zakresie dozwolonym przez prawo konkurencji, z odpłatnością, gdy jest wymagana; obowiązek Rady dokumentowania oceny konkurencyjnej przy każdej licencji; utrzymać odesłania eksportowe.
- **Podstawa prawna:** art. 101 ust. 1 i 3 TFUE [W]; art. 6 ustawy o ochronie konkurencji i konsumentów [W]; rozporządzenie Komisji (UE) 2026/877 z 16.04.2026 r. w sprawie stosowania art. 101 ust. 3 TFUE do kategorii porozumień o transferze technologii (art. 1 ust. 1 lit. b pkt vii: prawa do technologii obejmują prawa autorskie do oprogramowania; art. 1 ust. 1 lit. c pkt i: umowa licencyjna zawarta „w celu wytwarzania produktów objętych umową przez licencjobiorcę lub jego podwykonawców” (tłum. robocze); art. 2 wyłączenie; art. 3: progi 20% łącznie dla konkurentów i 30% dla każdej ze stron wśród niekonkurentów; art. 5 ust. 1 lit. a: wyłączeniem nie jest objęte „bezpośrednie lub pośrednie zobowiązanie licencjobiorcy do udzielenia licencji wyłącznej albo przeniesienia praw, w całości lub w części, na licencjodawcę […] w odniesieniu do własnych ulepszeń albo własnych nowych zastosowań licencjonowanej technologii” (tłum. robocze); art. 10: okres przejściowy 1.05.2026–30.04.2027 r. tylko dla umów obowiązujących 30.04.2026 r. i spełniających warunki rozporządzenia 316/2014; art. 11: wejście w życie 1.05.2026 r., wygaśnięcie 30.04.2038 r.) [Z] (tekst EN); wytyczne Komisji w sprawie transferu technologii (2026) [W]; rozporządzenia (UE) 2023/1066 (B+R) i 2023/1067 (specjalizacja) oraz wytyczne horyzontalne 2023 (wspólna produkcja) [W] — art. 9 rozporządzenia 2026/877 wyłącza jego stosowanie do licencji w umowach B+R i specjalizacyjnych objętych tymi rozporządzeniami [Z] (tekst EN); rozporządzenie (UE) 2021/821, art. 2 pkt 2 lit. d (eksportem jest przekazanie oprogramowania lub technologii drogą elektroniczną do miejsca przeznaczenia poza obszarem celnym Unii, w tym udostępnienie ich w formie elektronicznej osobom spoza tego obszaru) i art. 4 ust. 1 (klauzula catch-all: zezwolenie na wywóz pozycji spoza załącznika I po poinformowaniu przez organ o przeznaczeniu) [Z] (tekst EN, wersja skonsolidowana 2023); art. 3 ust. 1 (zezwolenie na wywóz pozycji z załącznika I), art. 8 ust. 1 (zezwolenie na pomoc techniczną dotyczącą pozycji z załącznika I, gdy organ poinformował o przeznaczeniu z art. 4 ust. 1) i ust. 3 lit. a (wyłączenie dla pomocy w państwach z części 2 sekcji A załącznika II), art. 11 ust. 1 i załącznik IV (zezwolenie na transfer wewnątrzunijny pozycji z załącznika IV) [Z] (tekst EN), pozycje załącznika IV nieweryfikowane; unijne generalne zezwolenia na wywóz EU001 (załącznik II sekcja A, bez Turcji) i EU002–EU006 (sekcje B–F: Turcja objęta tylko dla wąskich kategorii pozycji albo operacji — np. EU002: 1A001, 1A003, 3C003–3C006) [Z] (tekst EN, wersja skonsolidowana 2023); ustawa z 29.11.2000 r. o obrocie z zagranicą towarami, technologiami i usługami o znaczeniu strategicznym (art. 2: obrót dozwolony na zasadach rozporządzenia 2021/821; art. 3 pkt 5b pomoc techniczna; art. 3 pkt 10 organ kontroli obrotu — minister właściwy do spraw gospodarki), znowelizowana ustawą z 13.03.2026 r. (Dz.U. 2026 poz. 471, ogłoszona 7.04.2026 r., wejście w życie po 14 dniach) [Z]; ustawa z 13.06.2019 r. o wykonywaniu działalności gospodarczej w zakresie wytwarzania i obrotu materiałami wybuchowymi, bronią, amunicją oraz wyrobami i technologią o przeznaczeniu wojskowym lub policyjnym (art. 7 ust. 1 pkt 2: „obrotu technologią o przeznaczeniu wojskowym lub policyjnym — wymaga uzyskania koncesji”; art. 3 ust. 1 pkt 12: technologia to „informacje niezbędne do rozwoju, produkcji lub używania danego wyrobu ... mające postać danych technologicznych lub pomocy technicznej”) [Z].

#### § 33 ust. 4: kompetencja Rady do dopuszczenia ograniczonego dostępu partnerów z państw EU001 albo związanych umową o bezpieczeństwie informacji z UE lub NATO; warstwa programowa EDF (art. 9) z uchwałą WZ dla kontroli z państwa niestowarzyszonego

Commit `2081146` · memorandum 2.4.2 · klasa: zalecane

- **Pytanie:** Czy uzależnienie udziału partnera od Kryterium jest dopuszczalne, w tym wobec partnerów z państw NATO spoza UE?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Dopuszczalność. Kryterium wobec partnera Przedsięwzięcia jest wewnętrznym warunkiem, jaki Spółka stawia własnym kontrahentom, a nie ograniczeniem obrotu akcjami; Spółka jako podmiot prywatny może dobierać partnerów według kryterium bezpieczeństwa, byle nie naruszała sankcji, przepisów o równym traktowaniu w obszarach objętych regulacją (np. zamówienia publiczne, dotacje) ani warunków programów. […]
- **Rekomendacja memorandum:** Uzupełnić ust. 4 o warstwę programową: gdy Przedsięwzięcie korzysta z finansowania UE na obronność albo ma być wykorzystane w takim projekcie, Rada zapewnia zgodność z warunkami programu (w szczególności art. 9 EDF), a kontrola partnera z państwa niestowarzyszonego nad Przedsięwzięciem wymaga uchwały WZ. Równolegle rozszerzyć kompetencję Rady (z głosem dyrektora ds. bezpieczeństwa) na partnerów z państw objętych unijnym zezwoleniem generalnym EU001 albo umową o bezpieczeństwie informacji z UE przy dostępie ograniczonym do zakresu Przedsięwzięcia; kontrola — nadal WZ. Decyzja Założycieli: lista państw zaufanych i czy Ukraina ma być objęta trybem Rady.
- **Podstawa prawna:** art. 353¹ KC (swoboda doboru kontrahenta) [Z]; art. 18, 49 i 63 TFUE (adresowane do państw; skutek horyzontalny ograniczony) [W]; art. 5 i art. 9 rozporządzenia (UE) 2021/697 (EDF): państwa stowarzyszone to członkowie EFTA należący do EOG (art. 5); odbiorcy i podwykonawcy „nie podlegają kontroli niestowarzyszonego państwa trzeciego lub podmiotu z niestowarzyszonego państwa trzeciego” (art. 9 ust. 3); odstępstwo dla podmiotu z siedzibą w UE lub państwie stowarzyszonym kontrolowanego z takiego państwa tylko przy gwarancjach zatwierdzonych przez państwo członkowskie lub stowarzyszone jego siedziby, m.in. że odbiorca pozostanie właścicielem praw własności intelektualnej wynikających z działania i rezultatów, a te nie będą podlegały kontroli ani ograniczeniu ze strony niestowarzyszonego państwa trzeciego ani podmiotu z takiego państwa (art. 9 ust. 4 lit. c); współpraca z podmiotami spoza UE i państw stowarzyszonych albo przez nie kontrolowanymi jest dopuszczalna, gdy nie jest sprzeczna z interesami bezpieczeństwa Unii, bez nieuprawnionego dostępu do informacji niejawnych i bez kwalifikowalności kosztów (art. 9 ust. 6); zmianę w toku działania zgłasza się Komisji (art. 9 ust. 7); przeniesienie własności wyników działań badawczych albo udzielenie licencji wyłącznej na rzecz niestowarzyszonego państwa trzeciego lub podmiotu z takiego państwa wymaga uprzedniego powiadomienia Komisji, a gdy jest sprzeczne z interesami bezpieczeństwa i obronności Unii — zwrotu wsparcia (art. 20 ust. 4) [Z]; to, które państwa EFTA/EOG faktycznie uczestniczą w Funduszu, nie wynika z tekstu rozporządzenia [W]; art. 2 pkt 1, 2, 5 i 7 oraz art. 4 ust. 9 i 15–17 rozporządzenia (UE) 2026/1386 (inwestor zagraniczny to osoba fizyczna bez obywatelstwa państwa członkowskiego albo podmiot utworzony według prawa państwa trzeciego, także działający przez spółkę zależną w UE; uprzednie zezwolenie przed zamknięciem transakcji; inwestycja greenfield poza obowiązkowym zakresem) i art. 30 ust. 1 i 3 oraz art. 31 (stosowanie od 17.01.2028 r., z tym dniem uchylenie rozporządzenia 2019/452; nowych przepisów nie stosuje się do inwestycji zakończonych albo kontrolowanych w tym dniu) [Z] (tekst EN); rozporządzenie (UE) 2021/821 i unijne generalne zezwolenie na wywóz EU001 (załącznik II sekcja A; część 1: wszystkie pozycje z załącznika I poza wymienionymi w sekcji I załącznika II; część 2: Australia, Kanada, Islandia, Japonia, Nowa Zelandia, Norwegia, Szwajcaria z Liechtensteinem, Zjednoczone Królestwo, USA; brak Turcji, którą obejmują tylko wąskie zezwolenia EU002–EU006) [Z] (tekst EN, wersja skonsolidowana 2023); art. 54 ust. 1–2 ustawy o ochronie informacji niejawnych (warunkiem dostępu przedsiębiorcy do informacji niejawnych „poufne” lub wyższych jest świadectwo bezpieczeństwa przemysłowego wydawane przez ABW albo SKW) [Z]; dostęp podmiotów zagranicznych na podstawie umów dwustronnych [W]; art. 4 ust. 1 pkt 7 ustawy o kontroli niektórych inwestycji (wytwarzanie i obrót wyrobami i technologią o przeznaczeniu wojskowym jako działalność, dla której podmiot „może być uznany za podmiot objęty ochroną” rozporządzeniem Rady Ministrów) [Z].

#### § 33 ust. 7: wyjątek od zakazu konkurencji ograniczony (próg 10% i równy udział Spółki, powyżej uchwała WZ z wyłączeniem zainteresowanego, ujawnienie wynagrodzeń, wygaśnięcie z Dniem Odejścia z ofertą udziału dla Spółki, szanse biznesowe); umowa wykonawcza § 10 ust. 4, § 12: dostosowanie

Commit `7588070` · memorandum 2.4.3 · klasa: zalecane

- **Pytanie:** Czy wyłączenie udziału założycieli w przedsięwzięciach spod zakazu konkurencji (§ 33 ust. 7) nie osłabia § 29 i jak zabezpieczyć Spółkę przed wyciekiem wartości?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Wyjątek jest uzasadniony celowościowo: Założyciel może być potrzebny w spółce celowej jako wspólnik-operator, a bez wyjątku każdy taki udział naruszałby § 29 ust. 1 („uczestniczyć w podmiocie konkurencyjnym”). Warunki — ujawnienie Radzie, zatwierdzenie „z zachowaniem ust. 6” (tryb konfliktu i § 30), wpis do Załącznika nr 3 — są jednak zbyt słabe w czterech miejscach. (1) Zatwierdza Rada bezwzględną większością dyrektorów niekonfliktowych; przy Radzie złożonej z Założycieli możliwe jest wzajemne zatwierdzanie udziałów („ja tobie, ty mnie”). […]
- **Rekomendacja memorandum:** Ograniczyć wyjątek: udział pośredni przez Spółkę jako reguła; udział bezpośredni do 10% w Przedsięwzięciu, w którym Spółka ma co najmniej równy udział, zatwierdzany przez Radę z głosem dyrektora ds. zgodności; powyżej tego — uchwała WZ 75% Głosów Uprawnionych w Sprawie z wyłączeniem zainteresowanego; wynagrodzenie od Przedsięwzięcia ujawnione i zatwierdzone; zatwierdzenie wygasa z Dniem Odejścia albo z wypowiedzeniem licencji, z obowiązkiem zaoferowania udziału Spółce po Wartości Godziwej; zachowanie obowiązku oferowania Spółce szans biznesowych.
- **Podstawa prawna:** art. 300⁵⁴ KSH (staranność i lojalność) i art. 300⁵⁵ § 1 KSH (konflikt interesów) [Z]; art. 300⁵⁵ § 3 KSH (dyrektor „nie może bez zgody spółki zajmować się interesami konkurencyjnymi ani uczestniczyć w spółce konkurencyjnej”, w tym przy co najmniej 10% głosów lub udziałów w konkurencyjnej spółce kapitałowej, „chyba że umowa spółki stanowi inaczej”; „Jeżeli umowa spółki nie stanowi inaczej, zgody udziela organ uprawniony do powoływania członka organu”) [Z]; art. 300¹ § 3 KSH (obowiązki akcjonariusza z umowy) [Z]; art. 300³³ § 1 pkt 11 KSH (rejestr ujawnia „postanowienia umowy spółki o związanych z akcją obowiązkach wobec spółki”) [Z]; art. 11 ust. 1–2 ustawy o zwalczaniu nieuczciwej konkurencji (tajemnica przedsiębiorstwa) [Z]; art. 101 ust. 1 TFUE (klauzule niekonkurowania w JV jako ograniczenia akcesoryjne) [W]; § 29 ust. 1–2, § 33 ust. 5–7, umowa wykonawcza (shareholder_agreement.tex — zakaz po odejściu z tym samym wyjątkiem).

### § 35. Rozwiązywanie Impasu Decyzyjnego

#### § 35 ust. 1 i 3: stwierdzenie Impasu Decyzyjnego przez Radę albo Przewodniczącego, wybór Niezależnego Eksperta przez niezależną instytucję przy wyłączeniu dyrektorów

Commit `6976954` · memorandum 3.4.3 · klasa: opcjonalne

- **Pytanie:** Czy tryb impasu (§ 35) jest wykonalny i czy rozstrzygnięcie Niezależnego Eksperta w sprawach obiektywnych nie wkracza w kompetencje organów?
- **Ocena brzmienia 0.9.4-C:** zgodne
- **Dlaczego zmieniono:** Mechanizm jest umową o postępowanie przedsądowe (negocjacje, mediacja) oraz o ekspertyzę arbitralną — ustalenie przez osobę trzecią elementu stanu faktycznego (wartość, dane księgowe, kwestia techniczna, zakres prawa IP), wiążące strony jak uzgodnienie umowne i podlegające kontroli sądu jedynie w granicach rażącej nieprawidłowości; to ta sama konstrukcja co § 19 ust. 7 i mieści się w art. 353¹ KC [W]. Nie jest to zapis na sąd polubowny (nie rozstrzyga „sporu o prawa majątkowe” w rozumieniu art. 1157 pkt 1 KPC [Z]), więc nie wchodzi w kolizję z przepisami o sądownictwie polubownym ani z wyłączną kompetencją sądu do uchylania uchwał. Ust. 4 poprawnie wyłącza zastępowanie uchwał organów; ekspert ustala przesłankę (np. […]
- **Rekomendacja memorandum:** Doprecyzować, że stan Impasu Decyzyjnego stwierdza Rada Dyrektorów uchwałą (a w razie jej niezdolności — Przewodniczący), oraz przewidzieć wybór eksperta przez instytucję niezależną (np. organizację rzeczoznawców albo ośrodek mediacyjny), gdy Rada nie może działać; utrzymać brak mechanizmu wyjścia jako świadomą decyzję.
- **Podstawa prawna:** art. 353¹ KC [Z]; art. 300⁷³–300⁷⁹ KSH (rada dyrektorów) i art. 300⁸⁰–300⁸¹ KSH (uchwały akcjonariuszy) [Z]; art. 17 § 3 KSH [Z]; art. 1157 KPC (zdatność arbitrażowa: spory o prawa majątkowe) [Z]; § 19 ust. 7.

### § 38. Postanowienia końcowe

#### § 38 ust. 2: zgoda większości akcji serii na uszczuplenie jej praw i zgoda akcjonariuszy dotkniętych zaostrzeniem obowiązków związanych z akcją

Commit `48f3c13` · memorandum 3.4.2 · klasa: zalecane

- **Pytanie:** Czy brak klauzul zgody indywidualnej (ochrony konkretnego akcjonariusza przed zmianą) jest bezpieczny dla założycieli mniejszościowych i czy inwestor VC będzie ich wymagał?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Ustawowe minimum ochrony to: (1) „uchwała dotycząca zmiany umowy spółki, zwiększająca świadczenia akcjonariuszy lub uszczuplająca prawa indywidualne poszczególnych akcjonariuszy, wymaga zgody wszystkich akcjonariuszy, których dotyczy” (art. 300⁹⁸ § 3 [Z]); (2) przy akcjach o różnych uprawnieniach — oddzielne głosowanie w grupie akcjonariuszy akcji jednorodzajowych, których prawa narusza zmiana umowy, z wyłączeniem emisji akcji nieuprzywilejowanych (art. 300⁹⁸ § 4–5 [Z] — odpowiednik art. 419 KSH istnieje); (3) zakaz nierównego traktowania w takich samych okolicznościach (art. 20 [Z]); […]
- **Rekomendacja memorandum:** Dodać w § 38 ust. 3 zasadę zgody serii i zgody akcjonariuszy dotkniętych zaostrzeniem obowiązków związanych z akcją; nie wprowadzać indywidualnych wet dla poszczególnych Założycieli (decyzja Założycieli, jeżeli mniejszość oczekuje innej równowagi).
- **Podstawa prawna:** art. 300⁹⁸ § 2–5 KSH (większość 3/4 dla zmiany umowy; zgoda wszystkich akcjonariuszy, których dotyczy uchwała zwiększająca świadczenia lub uszczuplająca prawa indywidualne; oddzielne głosowanie w grupie akcji jednorodzajowych) [Z]; art. 20 KSH (równe traktowanie) [Z]; art. 300¹⁰¹ w zw. z art. 422 § 1 KSH (uchylenie uchwały krzywdzącej akcjonariusza) [Z]; art. 300²⁵, art. 300²⁶ (akcje założycielskie), art. 300²⁸ KSH [Z]; art. 419 § 1 KSH (S.A., porównawczo) [Z].

#### § 38 ust. 5, § 29 ust. 2: dane historyczne Załącznika nr 1 bez aktualizacji, ujawnienia i zgody z Załącznika nr 3 uchwałą WZ bez zmiany umowy z ewidencją Rady

Commit `35faad6` · memorandum 3.4.1 · klasa: zalecane

- **Pytanie:** Czy aktualizacja Załączników nr 1–3 (np. zmiana danych, wpis nowego Założyciela Serii F, ujawnione aktywności) zawsze wymaga zmiany umowy w formie aktu notarialnego i wpisu do KRS, czy część danych można przenieść do uchwał albo rejestrów?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Skoro Załączniki są częścią umowy (§ 38 ust. 6), każda zmiana ich treści jest zmianą umowy: uchwała 75% w protokole notarialnym (art. 300¹⁰⁰ § 2 [Z]), zgłoszenie nie później niż sześć miesięcy od uchwały (art. 300¹⁰² § 2 [Z]), wpis konstytutywny (§ 1), tekst jednolity dołączany do wniosku (art. 9 ust. 4 ustawy o KRS [Z]). Nie każde zdarzenie wymaga jednak aktualizacji. *Załącznik nr 1* zawiera dane założycielskie (kto, za co i które akcje objął) — ustawowo obowiązkową treść umowy, która jest historyczna: późniejsze zbycie akcji, zmiana adresu albo nazwiska Założyciela nie zmieniają umowy, lecz są ujawniane w rejestrze akcjonariuszy (art. 300³³ § 1 pkt 5–6 [Z]), a wniesienie wkładu stwierdza uchwała Rady (art. 300⁹ § 2 [Z]), po czym rejestr ujawnia wzmiankę o pełnym pokryciu akcji (art. 300³³ § 1 pkt 9). Aktualizacji wymaga tylko błąd w danych założycielskich (np. omyłka w numerach akcji). *Załącznik nr 2* identyfikuje Założycieli Pierwotnych objętych mechanizmem zwrotnego zbycia i daty rozpoczęcia; ponieważ obowiązek zbycia jest „obowiązkiem związanym z akcją wobec Spółki” (§ 10 ust. 14), a takie obowiązki muszą wynikać z umowy spółki (art. 300¹ § 3), krąg osób i data muszą być z umowy ustalalne. […]
- **Rekomendacja memorandum:** Pozostawić Załączniki nr 1–2 w umowie (z zastrzeżeniem, że dane historyczne nie wymagają aktualizacji), a Załącznik nr 3 uczynić dokumentem aktualizowanym uchwałą Walnego Zgromadzenia bez zmiany umowy.
- **Podstawa prawna:** art. 300⁵ § 1 pkt 3–4, art. 300¹⁰⁰ § 2, art. 300¹⁰² § 1–2 KSH [Z]; art. 300¹ § 3, art. 300⁹ § 2 KSH [Z]; art. 300³⁰–300³³ KSH (rejestr akcjonariuszy; art. 300³³ § 1 pkt 10–11 i § 2) [Z]; art. 300³³ § 3 KSH w brzmieniu od 18 lutego 2027 r. (Dz.U. 2026 poz. 176) [Z]; art. 9 ust. 4 ustawy o KRS (tekst jednolity umowy) [Z].

#### § 38 ust. 7: uchwały założycielskie objęte aktem (pierwsza Rada, podmiot prowadzący rejestr) i reprezentacja Spółki w organizacji

Commit `4267f51` · memorandum 4.3.1, K18 · klasa: konieczne — odstępstwo od reguły uzasadnione: bez czynności redakcyjnych tekst nie może stać się aktem notarialnym; zmiany merytoryczne nie są konieczne

- **Pytanie:** Jaka forma zawiązania i jakie dokumenty do KRS są wymagane (w tym dokumentacja wkładów niepieniężnych) i które postanowienia projektu mogą wywołać zastrzeżenia sądu rejestrowego (ograniczenia zbywalności, Kryterium, obowiązki związane z akcją, uchwały ramowe)?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo — co do treści; w obecnej postaci redakcyjnej (przekreślenia, oznaczenia robocze, puste pola) tekst nie nadaje się do aktu i wywołałby wezwanie sądu, co kwalifikujemy jako ryzyko formalne
- **Dlaczego zmieniono:** **Forma.** Umowa nie korzysta ze wzorca, więc „powinna być zawarta w formie aktu notarialnego” (art. 300⁶). Wszyscy Założyciele stawają osobiście albo przez pełnomocnika z pełnomocnictwem w formie aktu notarialnego (art. 99 § 1 KC). Załączniki nr 1–3 muszą być objęte aktem, bo Załącznik nr 1 zawiera elementy obowiązkowe umowy („liczbę, serie i numery akcji, związane z nimi uprzywilejowanie, akcjonariuszy obejmujących poszczególne akcje oraz cenę emisyjną akcji”, a przy wkładach niepieniężnych ich przedmiot i akcje za nie obejmowane — art. 300⁵ § 1 pkt 3–5), a Załącznik nr 2 uruchamia mechanizm z § 10. […]
- **Rekomendacja memorandum:** Sporządzić wersję „do aktu” bez przekreśleń, oznaczeń i pól; objąć aktem uchwały założycielskie (powołanie pierwszej Rady, wybór podmiotu prowadzącego rejestr, ewentualnie zatwierdzenie Załączników); przygotować pakiet dokumentów wkładowych na dzień aktu (§ 7 ust. 4 zdanie ostatnie); przygotować listę akcjonariuszy z art. 300¹² § 4 i — jeżeli którykolwiek dyrektor ma adres poza UE — pełnomocnika do doręczeń z art. 19a ust. 5a ustawy o KRS. Potwierdzić u doradcy podatkowego brak PCC od umowy P.S.A. Uprawniony prawnik powinien potwierdzić bieżącą praktykę PRS co do formy załączników.
- **Podstawa prawna:** art. 300⁵ § 1 KSH (elementy umowy) [Z]; art. 300⁶ KSH (forma aktu notarialnego) [Z]; art. 300⁷ § 1 i 4 KSH (wzorzec — niewykorzystany; przy wzorcu tylko wkłady pieniężne) [Z]; art. 300⁹ § 1 KSH (wniesienie wkładów w całości w 3 lata od wpisu) [Z]; art. 300¹⁰ § 1 KSH (wyrównanie znacznie zawyżonego wkładu na kapitał akcyjny) [Z]; art. 300¹¹ § 1–2 KSH (spółka w organizacji; reprezentacja) [Z]; art. 300¹² § 1–4 KSH (zgłoszenie, załączniki, lista akcjonariuszy) [Z]; art. 300¹³ § 1–2 w zw. z art. 164 § 3, art. 165, art. 169 § 1 i art. 172 KSH (drobne uchybienia, braki usuwalne, termin 6 miesięcy, braki po wpisie) [Z]; art. 7, art. 19 ust. 2 i 5–6, art. 19a ust. 5, 5a i 5d, art. 20a ust. 1 i 3, art. 23 ust. 1 ustawy o KRS [Z]; art. 130 § 1–3 KPC [Z]; art. 40 pkt 1 ustawy o KRS [Z]; art. 52 ust. 1 i art. 55 ust. 1 ustawy o kosztach sądowych w sprawach cywilnych (500 zł za wpis; 250 zł za zmianę) [Z]; opłata za ogłoszenie w MSiG 100 zł [W]; art. 99 § 1 KC [Z]; art. 53 ustawy o prawie autorskim, art. 12 ust. 1–2 i art. 67 ust. 2–3 PWP [Z]; ustawa o PCC: art. 1 ust. 1 pkt 1 lit. k, art. 1a pkt 1–2, art. 6 ust. 1 pkt 8 lit. a, art. 7 ust. 1 pkt 9 [Z]; art. 60 ust. 1 pkt 1 ustawy o przeciwdziałaniu praniu pieniędzy (CRBR: 14 dni od wpisu) [Z]; art. 300³¹ § 5 i art. 300³² § 1 KSH [Z]; art. 300³⁹ § 1–2 KSH [Z]; art. 300³³ § 1 pkt 10–11 KSH [Z]; art. 300⁹⁸ § 2 i art. 300¹⁰³ KSH [Z]; art. 300¹ § 3 KSH [Z].

### Załącznik nr 1

#### Załącznik nr 1: rozdzielenie numerów akcji obejmowanych za wkłady niepieniężne (Część A, z wartością wkładu i podstawą wyceny) i pieniężne (Część B), zestawienie łączne

Commit `1eb1977` · memorandum 3.1.4, K13 · klasa: konieczne

- **Pytanie:** Załącznik nr 1 zawiera pola do uzupełnienia — jakie dane muszą być kompletne w chwili podpisania umowy założycielskiej?
- **Ocena brzmienia 0.9.4-C:** ryzyko (Załącznik nr 1 nie rozdziela akcji obejmowanych za wkłady niepieniężne od obejmowanych za wkłady pieniężne i nie zawiera wartości wkładów)
- **Dlaczego zmieniono:** Załączniki są integralną częścią umowy (§ 38 ust. 6), więc w akcie notarialnym nie może pozostać żadne pole otwarte. Ustawowo obowiązkowe w chwili zawarcia umowy są: (1) dane identyfikujące każdego Założyciela (imię i nazwisko, PESEL, adres — notariusz i tak ich wymaga); (2) liczba, seria i numery akcji obejmowanych przez każdego z nich oraz cena emisyjna (pkt 3) — tabela w § 6 i kolumna „Akcje” w Załączniku nr 1 to zapewniają; […]
- **Rekomendacja memorandum:** Przebudować Załącznik nr 1 na dwie tabele: (A) akcje za wkłady niepieniężne — numery akcji, przedmiot, wartość, podstawa wyceny, dokumenty przeniesienia; (B) akcje za wkłady pieniężne — numery akcji, kwota, termin. Suma numerów obu tabel dla każdego Założyciela musi odpowiadać tabeli z § 6 ust. 1. Uzupełnić wszystkie pola przed wizytą u notariusza; Załączniki nr 2 i 3 uzupełnić albo wpisać „brak”.
- **Podstawa prawna:** art. 300⁵ § 1 pkt 3–5 i § 2 KSH [Z]; art. 300⁶ KSH (forma aktu notarialnego) [Z]; art. 300⁹ § 3, art. 300¹² § 2 pkt 7, § 3 i § 4 KSH (zgłoszenie, oświadczenia, lista akcjonariuszy) [Z]; art. 92 § 1 ustawy Prawo o notariacie [W]; art. 19 ust. 1 ustawy o KRS [Z].

### Załącznik nr 3

#### Załącznik nr 3 pkt 4: zakres danych klasyfikacji eksportowej (pozycja wykazu, data, wersja wykazu, osoba odpowiedzialna, wiążące wyjaśnienie)

Commit `14e540a` · memorandum 4.2.2 · klasa: opcjonalne — warunek spełnia się poza umową

- **Pytanie:** Czy klasyfikacja produktów Firmy (oprogramowanie autonomii, roje dronów) wymaga odrębnej weryfikacji specjalistycznej i czy mogą Państwo ją wykonać albo wskazać specjalistę?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo — klauzula wystarcza; warunek (klasyfikacja) spełnia się poza umową
- **Dlaczego zmieniono:** Tak, wymaga. Klasyfikacja jest ustaleniem techniczno-prawnym: porównuje parametry konkretnego produktu (czas lotu, odporność na podmuchy, zasięg, dokładność nawigacji inercyjnej, długość klucza kryptograficznego, „specjalne zaprojektowanie” warstwy autonomii) z progami pozycji wykazu, a następnie ocenia wyłączenia (technologia powszechnie dostępna, podstawowe badania naukowe, oprogramowanie masowego rynku) i klauzulę catch-all. Kancelaria prawna może i powinna zaopiniować reżim (co jest eksportem, jakie zezwolenie, EU001, transfer wewnątrzunijny z załącznika IV, ITAR/EAR komponentów), ale samo przypisanie pozycji wymaga danych inżynierskich i jest obowiązkiem Spółki, nie doradcy. […]
- **Rekomendacja memorandum:** Zlecić klasyfikację specjaliście ds. kontroli eksportu przed bramką G2 (pierwsze udostępnienie technologii poza firmę, w tym due diligence inwestora i chmura poza UE); przy wątpliwościach wystąpić o wiążące wyjaśnienie z art. 10 ustawy; wynik wpisać do Załącznika nr 3 pkt 4. W umowie nie ma nic do zmiany.
- **Podstawa prawna:** rozporządzenie (UE) 2021/821, załącznik I (tekst skonsolidowany na 26 maja 2023 r., EN; załącznik zmieniany po tej dacie): uwaga ogólna do technologii (GTN), uwaga ogólna do oprogramowania (GSN), definicje „technologii”, „wymaganej”, „rozwoju”, „informacji powszechnie dostępnych” i „podstawowych badań naukowych”; pozycje 9A012.a (BSP), 9A112 (BSP o zasięgu 300 km albo z autonomicznym sterowaniem i rozpylaczem), 9D001–9D002, 9D004.e (oprogramowanie do działania BSP z 9A012), 9E001–9E002, 9E101–9E102; 7A003 (inercyjne urządzenia pomiarowe; uwaga 2 wyłącza urządzenia certyfikowane dla lotnictwa cywilnego), 7A103, 7D002–7D004, 7E001, 7E004.b; 6A008 (radary, w tym SAR), 6D001–6D002, 6E001; 5A002.a, 5D002, 5E002 (kryptografia) oraz załącznik IV (w tym 1C101 i 1D103 — redukcja wykrywalności, także BSP z 9A012) [Z] (tekst EN); art. 3 ust. 1, art. 4 ust. 1–2 i art. 11 ust. 1 rozporządzenia [Z] (tekst EN); Wspólny wykaz uzbrojenia UE, ML10 (BSP) i ML21/ML22 [W]; ustawa z 29 listopada 2000 r.: art. 3 pkt 10 (organem kontroli obrotu jest minister właściwy do spraw gospodarki), art. 10 ust. 1 (wiążące wyjaśnienie w sprawie konieczności uzyskania zezwolenia), art. 11 (wewnętrzny system kontroli przy uzbrojeniu), art. 17a ust. 1 pkt 2 (rozstrzyganie o konieczności zezwolenia w przypadkach catch-all) [Z]; § 28 ust. 2 i § 23 ust. 1 lit. h.

### Inne miejsca umowy i dokumenty towarzyszące

#### Umowa wykonawcza § 13 ust. 5: warstwa kontroli UE/EOG w okresie finansowania EDF/AGILE/EUDIS, ze zgodą WZ 75%

Commit `65fc8d4` · memorandum 1.1.1, decyzja D6 · klasa: zalecane

- **Pytanie:** Czy ograniczenie kręgu nabywców akcji, spadkobierców, małżonków i dyrektorów według obywatelstwa, siedziby i struktury kontroli jest dopuszczalne na tle KSH (art. 300³⁹ i 300⁴¹), swobód traktatowych UE (przepływ kapitału, swoboda przedsiębiorczości) i zakazu dyskryminacji? Czy odmienne traktowanie państw UE/EOG i pozostałych państw NATO wymaga innej konstrukcji?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo
- **Dlaczego zmieniono:** Na gruncie KSH ograniczenie jest dopuszczalne. Art. 300³⁹ § 1 KSH stanowi, że „umowa spółki może uzależnić rozporządzenie akcją od zgody spółki lub w inny sposób je ograniczyć”, a przepis nie zawęża katalogu kryteriów; ograniczenie kręgu nabywców do osób o określonych cechach (obywatelstwo, siedziba, struktura kontroli) jest klasycznym „innym sposobem” ograniczenia, znanym z praktyki spółek z sektora obronnego, mediów czy lotnictwa [W]. Wobec spadkobierców podstawę daje art. 300⁴¹ § 1 KSH, który pozwala „ograniczyć lub wyłączyć wstąpienie do spółki spadkobierców”, ale wymaga, aby umowa określała „warunki spłaty spadkobierców niewstępujących do spółki, pod rygorem bezskuteczności ograniczenia lub wyłączenia”, a spłata uwzględniała „stosunek wartości wkładu wniesionego do wartości wkładu niewniesionego” (§ 1 zd. 2–3) — projekt spełnia ten warunek w § 17 ust. 2 i 4. […]
- **Rekomendacja memorandum:** Zachować Kryterium w obecnym kształcie. Dodać w § 11 ust. 6 zdanie o dodatkowej przesłance dla nabycia *kontroli* (UE/EOG/państwa stowarzyszone z EDF) obowiązującej w okresie korzystania z programów, z możliwością zgody Walnego Zgromadzenia większością 75%; alternatywnie zapisać to w umowie akcjonariuszy jako zobowiązanie do niedopuszczenia do takiej kontroli. Wybór miejsca należy do Założycieli; miejsce w umowie spółki daje skuteczność wobec Spółki i rejestru, umowa akcjonariuszy — elastyczność.
- **Podstawa prawna:** art. 300³⁹ § 1–2 KSH [Z]; art. 300⁴¹ § 1 KSH [Z]; art. 300¹ § 3 i art. 2 KSH w zw. z art. 353¹, art. 57 i art. 58 KC [Z]; art. 18, 49, 63, 65 ust. 1 lit. b i art. 346 ust. 1 lit. b TFUE [W]; art. 2 pkt 6, 7 i 24, art. 5 oraz art. 9 ust. 1–4 i 7 rozporządzenia (UE) 2021/697 (EDF) [Z]; art. 2 pkt 1, 5 i 7, art. 4 ust. 15 lit. a–b i ust. 17, art. 30 ust. 1, art. 31 oraz motywy 14, 15 i 20 rozporządzenia (UE) 2026/1386 (kontrola inwestycji zagranicznych, stosowane od 17 stycznia 2028 r.) [Z] (tekst EN); art. 12a–12k ustawy z 24 lipca 2015 r. o kontroli niektórych inwestycji [Z].

#### Umowa wykonawcza, Załączniki A–B: oferta skierowana do Spółki z prawem wskazania Nabywcy Wskazanego i zobowiązaniem do zbycia (umowa przedwstępna, art. 300^34 § 4 KSH), warunki, wstrzymanie terminu 6 miesięcy, granica 24 miesięcy, niezapłacenie ceny, dopłata, zgoda na wpis, PCC, depozyt; pełnomocnictwo dla Spółki z substytucją, nieodwołalne (art. 101 § 1 KC), z podpisem notarialnie poświadczonym, dom maklerski

Commit `888e0b3` · memorandum 1.5.3 · klasa: konieczne

- **Pytanie:** Umowa wykonawcza: czy nieodwołalne oferty i pełnomocnictwa (art. 101 § 2 i art. 108 KC) mogą zostać skonstruowane tak, aby mechanizm zadziałał bez dalszego podpisu akcjonariusza, i czy orzeczenie zastępujące oświadczenie woli (art. 64 KC, art. 1047 KPC) jest realną drogą wykonania? Jak wygląda minimalna treść takiej umowy (zdarzenie, stwierdzenie Odejścia, nabywca, cena, terminy)?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo — konstrukcja poprawna co do zasady, projekt umowy wykonawczej ma braki, z których dwa są istotne
- **Dlaczego zmieniono:** **Oferta.** Oferta z oznaczonym terminem związania wiąże oferenta do upływu tego terminu (art. 66 § 2 KC a contrario — przepis reguluje wprost tylko ofertę bez terminu); po dojściu do adresata (art. 61 § 1 KC) prawo nie przewiduje jej jednostronnego odwołania, a nawet w obrocie między przedsiębiorcami — gdyby założyciel składał ofertę w ramach współpracy B2B — „oferty nie można odwołać, jeżeli wynika to z jej treści lub określono w niej termin przyjęcia” (art. 66² § 2 KC); zastrzeżenie „nieodwołalności” jest więc skuteczne i w istocie deklaratoryjne. Oferta pod warunkiem zawieszającym Odejścia (art. 89 KC) i z ceną oznaczalną „według Wartości Godziwej” (art. 536 § 1 KC) jest dopuszczalna; śmierć oferenta nie umarza oferty (art. 62 KC), co umowa wykonawcza prawidłowo wykorzystuje w § [umowa wspólników: smierc]. Forma: zbycie akcji P.S.A. wymaga formy dokumentowej pod rygorem nieważności (art. 300³⁶ § 4 KSH), więc oferta i przyjęcie w formie dokumentowej wystarczają materialnie; co więcej, „oświadczenie akcjonariusza o zobowiązaniu do przeniesienia akcji” jest samodzielną podstawą wpisu w rejestrze (art. 300³⁴ § 4 zdanie drugie KSH), więc ofertę albo umowę przedwstępną warto zredagować tak, aby mogła pełnić tę rolę. **Brak nr 1**: oferta z Załącznika A jest skierowana do osoby nieoznaczonej („Dopuszczalny Nabywca wskazany przez Spółkę”). […]
- **Rekomendacja memorandum:** Przebudować Załączniki A–B (oferta do Spółki z prawem wskazania nabywcy plus umowa przedwstępna; pełnomocnictwo dla Spółki z substytucją, z podpisem notarialnie poświadczonym), uzupełnić braki (a)–(g), a w § 10 ust. 13 rozszerzyć katalog obowiązkowej treści. Umowę wykonawczą podpisać tego samego dnia co umowę Spółki; wzory uzgodnić z podmiotem prowadzącym rejestr.
- **Podstawa prawna:** art. 61 § 1, art. 62, art. 66 § 1–2, art. 66² § 2, art. 89, art. 99 § 1, art. 101 § 1–2, art. 106, art. 108, art. 389–390, art. 393, art. 536 § 1 KC [Z]; art. 64 KC, art. 1047 § 1–2 i art. 786 § 1 KPC [Z]; art. 300³⁶ § 4, art. 300³⁴ § 3–5, art. 300³⁷ § 1 KSH [Z]; SN V CSK 522/18 i II CSKP 593/22 [Z] (tezy według `psa_feedback.tex`; teksty orzeczeń niedostępne); art. 730 i n. KPC [Z]; art. 4 pkt 1 i art. 7 ust. 1 pkt 1 lit. b ustawy o PCC [Z]
- **Orzecznictwo:** II CSKP 593/22, V CSK 522/18 (zob. sekcja 6)

#### extra.tex: opis emisji serii P zgodny z § 8 (warunkowa emisja)

Commit `ae4636c` · memorandum 3.2.1 · klasa: konieczne

- **Pytanie:** Czy „uchwała ramowa” na wiele transz emisji serii P, wykonywana przez Radę, oraz jedna uchwała 4/5 o pozbawieniu prawa poboru dla wszystkich transz są dopuszczalne na tle art. 300¹⁰³–300¹⁰⁷ KSH, czy każda transza wymaga własnej uchwały o prawie poboru?
- **Ocena brzmienia 0.9.4-C:** ryzyko (konstrukcja hybrydowa nieznana ustawie; ustawa daje dwa gotowe instrumenty, z których umowa nie korzysta)
- **Dlaczego zmieniono:** Konstrukcję trzeba rozłożyć na trzy warstwy. *Pierwsza — podstawa w umowie.* Art. 300¹⁰³ KSH stanowi, że emisja akcji jest zmianą umowy spółki, ale „zachowanie przepisów o zmianie umowy spółki nie jest wymagane, jeżeli emisja akcji następuje uchwałą akcjonariuszy podejmowaną na podstawie dotychczasowych postanowień umowy spółki przewidujących maksymalną liczbę akcji i termin ich emisji” [Z]; § 8 ust. 1 i 3 spełniają ten wymóg (zob. 3.2.2). *Druga — uchwała o emisji.* Wbrew założeniu, na którym oparto § 8 ust. 3, P.S.A. zna delegację kompetencji emisyjnej: (a) *upoważnienie Rady Dyrektorów do emisji* (art. 300¹¹⁰–300¹¹³, stosowane do rady dyrektorów jak do zarządu) — umowa spółki może upoważnić organ zarządzający na okres nie dłuższy niż pięć lat, odnawialny zmianą umowy, do jednej albo kilku emisji łącznie nie większych niż jedna czwarta liczby akcji istniejących w dniu udzielenia upoważnienia, za wkłady pieniężne (chyba że upoważnienie dopuszcza niepieniężne), bez akcji uprzywilejowanych i uprawnień indywidualnych; uchwała o zmianie umowy w tym przedmiocie musi być umotywowana (art. 300¹¹¹), uchwała Rady zastępuje uchwałę Walnego Zgromadzenia o emisji (art. 300¹¹²), a pozbawienie prawa poboru wymaga przy każdej emisji uchwały akcjonariuszy 4/5 albo upoważnienia Rady zapisanego w umowie spółki i uchwalonego większością 4/5 (art. 300¹¹³) [Z]; (b) *warunkowa emisja akcji* (art. 300¹¹⁴–300¹¹⁸) — ustawowy instrument programów motywacyjnych: Walne Zgromadzenie uchwala emisję z zastrzeżeniem, że akcje obejmą osoby, „które uzyskały te prawa na podstawie umowy zawartej ze spółką” (art. 300¹¹⁴ § 2 pkt 2), przy czym zawarcie takiej umowy wymaga zgody Walnego Zgromadzenia 3/4 (§ 3), liczba akcji nie może przekroczyć dwukrotności akcji istniejących (§ 4); uchwała określa maksymalną liczbę akcji, cenę emisyjną, cel, termin wykonania prawa i krąg uprawnionych (art. 300¹¹⁵ § 1), sama „skutkuje wyłączeniem prawa poboru” i musi spełniać warunki art. 300¹⁰⁶ § 2, czyli większość 4/5 (art. 300¹¹⁵ § 2); po wpisie tej zmiany umowy do rejestru (art. 300¹¹⁶) uprawnieni obejmują akcje pisemnym oświadczeniem, Rada wydaje dyspozycję wpisu do rejestru akcjonariuszy i z tym wpisem następuje nabycie praw z akcji (art. 300¹¹⁷–300¹¹⁸ § 1), a do sądu rejestrowego trafia tylko roczny wykaz objętych akcji (art. 300¹¹⁸ § 2–3) [Z]; nowelizacja poz. 176 potwierdza ten model, wyłączając od 18 lutego 2027 r. akcje z art. 300¹¹⁸ spod ogólnej zasady, że objęcie akcji nie wymaga wpisu w rejestrze akcjonariuszy do nabycia praw (nowe brzmienie art. 300³⁷ § 2) [Z]. Uchwała ramowa z § 8 ust. 3 nie jest żadnym z tych instrumentów: jest zwykłą emisją z oddziału 1, w której Walne Zgromadzenie chce rozłożyć skutek na transze wykonywane przez Radę. […]
- **Rekomendacja memorandum:** Przebudować § 8 ust. 3 i 5: (1) przewidzieć jako tryb podstawowy warunkową emisję akcji serii P (jedna uchwała 4/5 na całą pulę albo jej część, zgoda na zawieranie umów uczestnictwa udzielona w tej samej uchwale dla kategorii osób i warunków z regulaminu, objęcie po nabyciu uprawnień pisemnym oświadczeniem, prawa z akcji z chwilą wpisu do rejestru akcjonariuszy); (2) zachować tryb zwykły z uchwałą obejmującą kilka transz jako alternatywę, z pełnym katalogiem art. 300¹⁰⁴ i upoważnieniami dla Rady; (3) wyłączyć w umowie prawo poboru akcji serii P na podstawie art. 300¹⁰⁶ § 1, co czyni ust. 5 zbędnym; (4) potwierdzić z kancelarią, czy termin z art. 300¹⁰² § 2 dotyczy emisji z art. 300¹⁰³, i do czasu potwierdzenia zgłaszać każdą emisję zwykłą w sześć miesięcy od uchwały. Upoważnienie Rady z art. 300¹¹⁰ (limit jednej czwartej akcji, pięć lat) rozważyć jako narzędzie dla drobnych emisji, nie dla puli P. Wybór trybu podstawowego jest decyzją Założycieli; rekomendujemy warunkową emisję.
- **Podstawa prawna:** art. 300¹⁰³, art. 300¹⁰⁴ § 1 pkt 1–7 i § 2, art. 300¹⁰⁵ § 1–3, art. 300¹⁰⁶ § 1–2 i 6, art. 300¹⁰⁷ § 1–3 KSH [Z]; art. 300¹⁰⁸–300¹¹³ KSH (upoważnienie zarządu albo rady dyrektorów do emisji akcji) [Z]; art. 300¹¹⁴–300¹¹⁸ KSH (warunkowa emisja akcji), art. 300¹¹⁹ KSH (warranty subskrypcyjne), art. 300⁸¹ pkt 4 KSH [Z]; art. 300¹⁰² § 2 KSH (termin sześciu miesięcy na zgłoszenie zmiany umowy) [Z]; art. 300³⁷ § 2 KSH w brzmieniu od 18 lutego 2027 r. (Dz.U. 2026 poz. 176, art. 1 pkt 6) [Z]; art. 444 § 1 KSH (porównawczo) [Z]; art. 300¹ § 3 KSH [Z].

#### Umowa wykonawcza § 6–7: treść główna zgodna z Załącznikami A–B

Commit `a4b0b06` · memorandum 1.5.3 · klasa: konieczne

- **Pytanie:** Umowa wykonawcza: czy nieodwołalne oferty i pełnomocnictwa (art. 101 § 2 i art. 108 KC) mogą zostać skonstruowane tak, aby mechanizm zadziałał bez dalszego podpisu akcjonariusza, i czy orzeczenie zastępujące oświadczenie woli (art. 64 KC, art. 1047 KPC) jest realną drogą wykonania? Jak wygląda minimalna treść takiej umowy (zdarzenie, stwierdzenie Odejścia, nabywca, cena, terminy)?
- **Ocena brzmienia 0.9.4-C:** zgodne warunkowo — konstrukcja poprawna co do zasady, projekt umowy wykonawczej ma braki, z których dwa są istotne
- **Dlaczego zmieniono:** **Oferta.** Oferta z oznaczonym terminem związania wiąże oferenta do upływu tego terminu (art. 66 § 2 KC a contrario — przepis reguluje wprost tylko ofertę bez terminu); po dojściu do adresata (art. 61 § 1 KC) prawo nie przewiduje jej jednostronnego odwołania, a nawet w obrocie między przedsiębiorcami — gdyby założyciel składał ofertę w ramach współpracy B2B — „oferty nie można odwołać, jeżeli wynika to z jej treści lub określono w niej termin przyjęcia” (art. 66² § 2 KC); zastrzeżenie „nieodwołalności” jest więc skuteczne i w istocie deklaratoryjne. Oferta pod warunkiem zawieszającym Odejścia (art. 89 KC) i z ceną oznaczalną „według Wartości Godziwej” (art. 536 § 1 KC) jest dopuszczalna; śmierć oferenta nie umarza oferty (art. 62 KC), co umowa wykonawcza prawidłowo wykorzystuje w § [umowa wspólników: smierc]. Forma: zbycie akcji P.S.A. wymaga formy dokumentowej pod rygorem nieważności (art. 300³⁶ § 4 KSH), więc oferta i przyjęcie w formie dokumentowej wystarczają materialnie; co więcej, „oświadczenie akcjonariusza o zobowiązaniu do przeniesienia akcji” jest samodzielną podstawą wpisu w rejestrze (art. 300³⁴ § 4 zdanie drugie KSH), więc ofertę albo umowę przedwstępną warto zredagować tak, aby mogła pełnić tę rolę. **Brak nr 1**: oferta z Załącznika A jest skierowana do osoby nieoznaczonej („Dopuszczalny Nabywca wskazany przez Spółkę”). […]
- **Rekomendacja memorandum:** Przebudować Załączniki A–B (oferta do Spółki z prawem wskazania nabywcy plus umowa przedwstępna; pełnomocnictwo dla Spółki z substytucją, z podpisem notarialnie poświadczonym), uzupełnić braki (a)–(g), a w § 10 ust. 13 rozszerzyć katalog obowiązkowej treści. Umowę wykonawczą podpisać tego samego dnia co umowę Spółki; wzory uzgodnić z podmiotem prowadzącym rejestr.
- **Podstawa prawna:** art. 61 § 1, art. 62, art. 66 § 1–2, art. 66² § 2, art. 89, art. 99 § 1, art. 101 § 1–2, art. 106, art. 108, art. 389–390, art. 393, art. 536 § 1 KC [Z]; art. 64 KC, art. 1047 § 1–2 i art. 786 § 1 KPC [Z]; art. 300³⁶ § 4, art. 300³⁴ § 3–5, art. 300³⁷ § 1 KSH [Z]; SN V CSK 522/18 i II CSKP 593/22 [Z] (tezy według `psa_feedback.tex`; teksty orzeczeń niedostępne); art. 730 i n. KPC [Z]; art. 4 pkt 1 i art. 7 ust. 1 pkt 1 lit. b ustawy o PCC [Z]
- **Orzecznictwo:** II CSKP 593/22, V CSK 522/18 (zob. sekcja 6)

## 4. Uwagi memorandum niewdrożone osobnym commitem

| Nr | Pytanie | Klasa | Uwaga | Status |
|---:|---|---|---|---|
| 12 | 4.4.1 | opcjonalne | Fundusz zażąda wpływu na wybór Dopuszczalnego Nabywcy akcji leavera albo podziału proporcjonalnego; parametr do term sheetu, nie zmiana konstrukcji. | pominięta: memorandum traktuje to jako parametr term sheetu, bez zmiany umowy |
| 19 | 4.4.1 | zalecane | Kryterium wobec funduszu bez wyjątku dla funduszy i z utratą Kryterium przy zmianie po stronie LP będzie negocjowane z każdym funduszem; test należy przenieść na poziom zarządzającego i kontroli. | pominięta: brak brzmienia; odpowiedź odsyła do 4.4.2 (wdrożone jako uwagi 21–24 i 27) |
| 22 | 1.4.2 | zalecane | Zachować w wyjątku ujawnienie beneficjentów rzeczywistych w rozumieniu AML, test sankcyjny i współdziałanie z organami koncesyjnymi. | wdrożona razem z uwagą 21 (to samo brzmienie z 1.4.3) |
| 23 | 1.4.3 | zalecane | Uszczelnić wyjątek: regulowany zarządzający, min. 5 inwestorów, progi 25%/50%/10%, wyłączenie wehikułów jednego inwestora, oświadczenie i zawiadomienia. | wdrożona razem z uwagą 21 (to samo brzmienie z 1.4.3) |
| 36 | 1.2.4 | konieczne | W wariancie B dodać wentyl: po 12 miesiącach bezskutecznego poszukiwania nabywcy akcjonariusz może żądać wskazania nabywcy przez Spółkę. | pominięta: dotyczy wyłącznie wariantu B (K1), przyjęto wariant A (D2) |
| 37 | 1.2.5 | zalecane | Rekomendacja wariantu A z poprawkami z 1.2.3; wariant B tylko z wentylem z 1.2.4; dodać przeniesienia dozwolone dla inwestora finansowego. | wdrożona w uwagach 35 (wariant A z poprawkami 1.2.3) i 29 (Przeniesienia Dozwolone) |
| 38 | 4.4.1 | zalecane | Dla rundy wariant A (ratalny) jest łatwiejszy do obrony niż wariant B; fundusze zażądają płatności jednorazowej i krótszego terminu dla serii inwestorskiej. | bez zmian: wariant A (D2); płatność jednorazowa dla serii inwestorskiej to temat term sheetu |
| 41 | 4.4.2 | zalecane | Dodać Przeniesienia Dozwolone dla Kwalifikowanego Inwestora Finansowego bez zgody Spółki i prawa pierwszeństwa, z weryfikacją, przystąpieniem nabywcy i zawiadomieniem Rady (brzmienie III). | wdrożona w uwadze 29 (commit 69edc0b, brzmienie III; faktycznie § 12 ust. 9) |
| 47 | 4.4.1 | zalecane | Drag 75% bez zgody serii inwestorskiej, ceny minimalnej i waterfall pozwala zmusić inwestora z udziałem do ok. 25% do sprzedaży; standard rynkowy wymaga ochrony serii. | wdrożona razem z uwagą 48 (commit b876db3, brzmienie IV z 4.4.2) |
| 55 | 1.7.2 | opcjonalne | Dopisek o minimalizacji danych; istotna jest polityka RODO i klauzula informacyjna poza umową. | pominięta: memorandum rekomenduje „bez zmian w umowie” (polityka RODO poza umową) |
| 61 | 4.4.1 | opcjonalne | Kryterium wobec dyrektora wyklucza partnera funduszu spoza UE/NATO; istotne tylko dla funduszy zagranicznych i części deep tech. | wdrożona w commitach 3d5f0d1 i uwadze 62 (§ 21 ust. 3) |
| 82 | 4.4.1 | opcjonalne | Ust. 3 odwołuje się do testu sankcyjnego (Dopuszczalny Nabywca), nie do Kryterium; venture debt spoza UE/NATO nie jest zakazany, Kryterium działa dopiero przy prawach do akcji przez § 11 ust. 13. | pominięta: memorandum (4.4.1 pkt 9) uznaje, że § 31 ust. 3 nie wymaga zmian |
| 84 | 4.4.2 | zalecane | Przywrócić przekreślone odesłanie do Kwalifikowanego Inwestora Finansowego w definicji Kwalifikowanej Rundy, jeżeli ust. 14 zostaje przywrócony. | wdrożona w commicie a839982 (odesłanie do Kwalifikowanego Inwestora Finansowego w § 32 ust. 1, przy D3) |
| 87 | 4.4.2 | opcjonalne | Dodać do katalogu warunków inwestorskich zamknięty katalog spraw wymagających zgody serii inwestorskiej, aby weto nie było „warunkiem dalej idącym” (brzmienie VI). | wdrożona w commicie 77da93d (uwaga 71, § 32 ust. 4 lit. f) |
| 93 | 4.3.1 | konieczne | Usunąć wszystkie przekreślenia (po decyzjach Założycieli) i wypełnić wszystkie pola; akt notarialny nie może zawierać tekstu przekreślonego ani adnotacji roboczych. | wdrożona w commitach d7d6f77 (usunięcie przekreśleń, D4) i 59fa2c7; zdania „W sprawach nieuregulowanych…” nie przywrócono (kolizja z D4) — do decyzji prawnika |
| 97 | 4.3.3 | zalecane | Dodać klauzulę dostosowawczą (odesłania dynamiczne, terminy ustawowe wobec rejestru i KRS, obowiązek Rady przygotowania dostosowania w 6 miesięcy od zmiany prawa; realizuje art. 34 ustawy z 23.01.2026 r.). | wdrożona w commicie d900f94 (§ 38 ust. 6, klauzula dostosowawcza) |

## 5. Indeks przepisów, na których opierają się zmiany

Przepis → paragrafy umowy zmienione z jego powodu. Pełny kontekst w odpowiedziach memorandum wskazanych w sekcji 3.

**Kodeks cywilny**

- art. 1025 § 2, art. 1026, art. 1027, art. 1035–1036 KC [Z] — § 17
- art. 1035 KC w zw. z art. 212 KC [Z] — § 18
- art. 111 § 2 i art. 112 KC (obliczanie terminów) [Z] — § 5, § 24
- art. 189 KPC w zw. z art. 58 KC [Z] oraz uchwała SN (7) z 18.09.2013 r., III CZP 13/13 (zaskarżanie uchwał organów menedżerskich powództwem o ustalenie) [W] — § 23
- art. 327–329 KC (zastaw na prawach) [Z] oraz ustawa o zastawie rejestrowym [W] — § 12
- art. 353¹ KC (swoboda doboru kontrahenta) [Z] — § 33
- art. 353¹ KC [W] — § 27
- art. 353¹ KC [Z] — § 10, § 12, § 19, § 24, § 32, § 35
- art. 353¹, art. 58 § 2, art. 5 KC [Z] — § 10
- art. 353¹, art. 58 § 2, art. 536 § 1 KC [Z] — § 19
- art. 353¹, art. 58 § 2–3, art. 483–484 KC [Z] — § 10
- art. 353¹, art. 64, art. 101 § 1, art. 471, art. 483 § 1 KC [Z] — § 32
- art. 353¹, art. 65 KC [Z] — § 10
- art. 39 KC (czynność rzekomego organu, potwierdzenie) [Z] — § 21
- art. 455 i art. 476 KC [Z] — § 12
- art. 471 i art. 483 KC [Z] — § 11
- art. 483–484 KC [Z] — § 27
- art. 5 i art. 354 KC [Z] — § 12
- art. 536 § 1 KC [Z] — § 10
- art. 57 § 2 KC [Z] — § 13
- art. 57, art. 353¹ i art. 58 § 1–2 KC [Z] — § 12
- art. 58 § 1 KC [Z] — § 11, § 12
- art. 58 § 2 KC [Z] — § 17
- art. 60 KC [Z] — § 12
- art. 61 § 1, art. 62, art. 66 § 1–2, art. 66² § 2, art. 89, art. 99 § 1, art. 101 § 1–2, art. 106, art. 108, art. 389–390, art. 393, art. 536 § 1 KC [Z] — § 10, inne
- art. 64 KC [Z] — § 28
- art. 64 KC, art. 1047 KPC [Z] — § 11, § 17
- art. 64 KC, art. 1047 § 1–2 i art. 786 § 1 KPC [Z] — § 10, inne
- art. 66 § 1, art. 72 § 2, art. 389 § 1, art. 353¹ KC [Z] — § 9
- art. 66 § 1–2 KC (oferta i termin związania) [Z] — § 14
- art. 77² KC (forma dokumentowa) [Z] — § 12
- art. 83 i art. 58 KC [Z] — § 11
- art. 89 KC (warunek) [Z] — § 12
- art. 922 § 1, art. 924–925, art. 1025 § 2, art. 1027 KC [Z] — § 17
- art. 99 § 1 KC [Z] — § 30, § 38

**Kodeks postępowania cywilnego**

- art. 1047 § 1 KPC [Z] — § 32
- art. 1157 KPC (zdatność arbitrażowa: spory o prawa majątkowe) [Z] — § 35
- art. 1157 pkt 1 KPC [Z] — § 10
- art. 1157 pkt 1, art. 1161 § 1–2 KPC [Z] — § 19
- art. 130 § 1–3 KPC [Z] — § 30, § 38
- art. 278 § 1 KPC [Z] — § 19
- art. 666–667 KPC (kurator spadku) [Z] — § 17
- art. 730 i n. KPC [Z] — § 10, inne
- art. 910 i art. 911³ KPC (egzekucja z praw majątkowych — § 12
- art. 910 i art. 911³ KPC [Z] — § 13

**Kodeks pracy**

- SN II CSKP 593/22 [Z] — § 11
- SN III CZP 109/22, III CSKP 65/21, III CZP 32/16 [Z] (tezy według `psa_feedback.tex` — § 18
- SN V CSK 522/18 i II CSKP 593/22 [Z] (tezy według `psa_feedback.tex` — § 10, inne
- SN, wyrok z 9 grudnia 2022 r., II CSKP 593/22 [Z] — § 32
- art. 18 § 1, art. 22 § 1, art. 30 § 4, art. 45 § 1, art. 52 § 1, art. 56 § 1, art. 87 § 1, art. 91 § 1, art. 101¹–101², art. 114–122, art. 300 KP [Z] — § 10
- art. 52 § 1 pkt 2 KP (pomocniczo) [Z] — § 10

**Kodeks rodzinny i opiekuńczy**

- art. 31 § 1–2, art. 33 pkt 2, 9 i 10, art. 43, art. 46, art. 47¹ KRO [Z] — § 18

**Kodeks spółek handlowych**

- analogicznie art. 202 § 2–3, art. 203 § 2, art. 369 § 3–4 i art. 370 § 2 KSH [Z] oraz uchwała SN III CZP 109/22 (kadencja a mandat) [W] — § 21
- art. 1 pkt 2–6 i 30 (art. 300³², 300³³, 300³⁴, 300³⁵, 300³⁷ § 2 i art. 594 § 1 KSH) [Z] — § 5, § 24
- art. 14 § 1–2 KSH [Z] — § 7
- art. 15 § 1 KSH (nie wymienia dyrektora P.S.A. — pkt 2.2.4) [Z] — § 30
- art. 15 § 1 KSH (zgoda WZ na kredyt, pożyczkę, poręczenie lub podobną umowę z członkiem zarządu, rady nadzorczej, komisji rewizyjnej, prokurentem, likwidatorem — przepis nie wymienia dyrektora P.S.A., a przepisy o P.S.A. nie zawierają odesłania) [Z] — § 25
- art. 17 KSH [Z] — § 30
- art. 17 § 1 i 3 KSH [Z] — § 33
- art. 17 § 1–3 KSH (skutek braku uchwały wymaganej ustawą — nieważność — § 23
- art. 17 § 1–3 KSH [Z] — § 25, § 29, § 31
- art. 17 § 3 KSH [Z] — § 35
- art. 182 § 2–5 KSH (dla porównania: model sp. z o.o. z udziałem sądu rejestrowego) [Z] — § 12
- art. 183 § 1 KSH (analogia — § 17
- art. 2 KSH [Z] — § 9
- art. 20 KSH (równe traktowanie „w takich samych okolicznościach”) [Z] — § 24
- art. 20 KSH (równe traktowanie) [Z] — § 38
- art. 20 KSH [Z] — § 30
- art. 238 § 1 KSH (sp. z o.o.: e-mail za uprzednią pisemną zgodą wspólnika) [Z] — § 24
- art. 244 i 413 § 1 KSH (identyczne katalogi w sp. z o.o. i S.A.) [Z] — § 24
- art. 300² § 1–2, art. 300³ § 1–2, art. 300⁵ § 1 pkt 3–5 i § 2 KSH [Z] — § 7
- art. 300² § 2 KSH (wkład w postaci pracy lub usług) [Z] — § 10
- art. 300² § 2, art. 300¹⁰ § 1, art. 300¹² § 3 pkt 2, art. 300¹⁵ § 1–6, art. 300¹⁹ KSH [Z] — § 7
- art. 300²² § 1–4 KSH (zwrot wypłaty „dokonanej wbrew przepisom prawa lub postanowieniom umowy spółki” — § 30
- art. 300²¹ KSH („Wartość świadczeń spełnianych przez spółkę na rzecz akcjonariuszy z innego tytułu niż prawa wynikające z akcji, a także na rzecz spółek lub spółdzielni z nimi powiązanych albo pozostających wobec nich w stosunku dominacji lub zależności, nie może przekraczać wartości godziwej świadczenia wzajemnego otrzymanego przez spółkę”) [Z] — § 30
- art. 300²⁵ § 1–2 KSH (akcje uprzywilejowane — § 12, § 16, § 32
- art. 300²⁵ § 1–2 i art. 300²⁸ § 1–2 KSH [Z] — § 11, § 12, § 16, § 21, § 32
- art. 300²⁵, art. 300²⁶ (akcje założycielskie), art. 300²⁸ KSH [Z] — § 38
- art. 300²⁸ § 1–2 KSH (uprawnienia indywidualne akcjonariusza — odpowiednik art. 354 KSH) [Z] — § 32
- art. 300²⁸ § 1–2 KSH (uprawnienia indywidualne oznaczonego akcjonariusza, „w szczególności uprawnienie do powołania lub odwołania członków zarządu lub rady nadzorczej”, wygasające najpóźniej z utratą statusu akcjonariusza, „chyba że umowa spółki stanowi inaczej”) [Z] — § 12, § 16, § 32
- art. 300²⁹ § 1 KSH („akcje nie mają formy dokumentu”) [Z] — § 5, § 24
- art. 300³ § 1–2 w zw. z art. 14 § 1 KSH [Z] — § 7
- art. 300³² § 1 KSH (umowa o prowadzenie rejestru) [Z] — § 12
- art. 300³² § 1–2 KSH (niezwłoczne zawarcie umowy — § 5
- art. 300³³ § 1 pkt 10 i § 2 KSH [Z] — § 13
- art. 300³³ § 1 pkt 10, art. 300³⁴ § 6 i art. 300³⁷ § 1–2 KSH [Z] — § 12
- art. 300³³ § 1 pkt 10, art. 300³⁷ § 1 i art. 300³⁸ § 1 KSH [Z] — § 12
- art. 300³³ § 1 pkt 10–11 KSH [Z] — § 30, § 38
- art. 300³³ § 1 pkt 10–11 i § 2 KSH („umowa spółki może zawierać dodatkowe postanowienia dotyczące informacji ujawnianych w rejestrze akcjonariuszy”) [Z] — § 5
- art. 300³³ § 1 pkt 10–11 i § 2 KSH [Z] — § 10, § 12
- art. 300³³ § 1 pkt 10–11, art. 300³⁴ § 4–6, art. 300³⁷ § 1 i art. 300³⁸ § 1 KSH [Z] — § 11
- art. 300³³ § 1 pkt 11 KSH (obowiązki związane z akcją w rejestrze) [Z] — § 11
- art. 300³³ § 1 pkt 11 KSH (rejestr ujawnia „postanowienia umowy spółki o związanych z akcją obowiązkach wobec spółki”) [Z] — § 33
- art. 300³³ § 1 pkt 11 KSH [Z] — § 28
- art. 300³³ § 1 pkt 11 i § 2 KSH (obowiązki związane z akcją — § 27
- art. 300³³ § 1 pkt 4 i 10 KSH (rejestr akcjonariuszy zawiera „rodzaj danej akcji i uprawnienia szczególne z akcji” oraz „ograniczenia co do rozporządzania akcją”) [Z] — § 11, § 12, § 16, § 21, § 32
- art. 300³³ § 1 pkt 5 KSH (rejestr zawiera adres poczty elektronicznej, „jeżeli akcjonariusz wyraził zgodę na komunikację w stosunkach ze spółką i podmiotem prowadzącym rejestr akcjonariuszy przy wykorzystaniu poczty elektronicznej” — § 24
- art. 300³³ § 1 pkt 6 i art. 300³⁷ § 1–2 KSH (ujawnienie zastawu w rejestrze — § 12
- art. 300³³ § 3 KSH w brzmieniu od 18 lutego 2027 r. (Dz.U. 2026 poz. 176) [Z] — § 38
- art. 300³³ § 3 i art. 594 § 1 pkt 2¹ KSH w brzmieniu obowiązującym od 18 lutego 2027 r. (Dz.U. 2026 poz. 176) [Z] — § 12
- art. 300³³ § 3 i art. 594 § 1 pkt 2¹ KSH w brzmieniu od 18.02.2027 r. (Dz.U. 2026 poz. 176) [Z] — § 10, § 12
- art. 300³¹ § 1–5 KSH (podmiot uprawniony do prowadzenia rachunków papierów wartościowych albo notariusz — § 5
- art. 300³¹ § 5 i art. 300³² § 1 KSH [Z] — § 30, § 38
- art. 300³¹–300³⁴ KSH, w szczególności art. 300³³ § 1 pkt 10 („ograniczenia co do rozporządzania akcją”) i pkt 11 („postanowienia umowy spółki o związanych z akcją obowiązkach wobec spółki”), § 2 (dodatkowe informacje ujawniane na podstawie umowy spółki) oraz art. 300³⁴ § 1 i 4–6 (wpis na żądanie spółki albo osoby mającej interes prawny — § 12
- art. 300³⁰ § 1–2 KSH (obowiązek rejestracji akcji — § 5
- art. 300³⁰ § 1–2, art. 300³¹ § 5 KSH (rejestr akcjonariuszy, wybór podmiotu przez akcjonariuszy) [Z] — § 9
- art. 300³⁰–300³³ KSH (rejestr akcjonariuszy — § 38
- art. 300³⁴ § 1 KSH (wpis „na żądanie spółki lub innej osoby mającej interes prawny”, nie później niż w 7 dni) [Z] — § 24
- art. 300³⁴ § 1 i 3 KSH (wpis na żądanie spółki lub osoby mającej interes prawny w 7 dni — § 5
- art. 300³⁴ § 1 i 4–6 KSH [Z] — § 10, § 12
- art. 300³⁴ § 1 i 4–6 KSH — dokumenty, zakres badania i uwzględnianie ograniczeń przez podmiot prowadzący rejestr [Z] — § 12
- art. 300³⁴ § 3 zd. 2 KSH w brzmieniu od 18 lutego 2027 r. (forma zgody na wpis) [Z] — § 12
- art. 300³⁵ § 1 KSH (rejestr jawny dla spółki i każdego akcjonariusza) [Z] — § 27
- art. 300³⁵ § 1–3 KSH (jawność dla spółki i akcjonariuszy) [Z] — § 5
- art. 300³⁶ § 4 (forma dokumentowa zbycia), art. 300³⁷ § 1 (konstytutywny skutek wpisu) i art. 300³⁸ § 1 KSH [Z] — § 5
- art. 300³⁶ § 4 KSH (forma dokumentowa zbycia) [Z] — § 10, § 12
- art. 300³⁶ § 4, art. 300³⁴ § 3–5, art. 300³⁷ § 1 KSH [Z] — § 10, inne
- art. 300³⁷ § 1 i art. 300³⁸ § 1 KSH (skutek wpisu) [Z] — § 12
- art. 300³⁷ § 1 i art. 300³⁸ § 1 KSH [Z] — § 10, § 12
- art. 300³⁷ § 2 KSH w brzmieniu od 18 lutego 2027 r. (Dz.U. 2026 poz. 176, art. 1 pkt 6) [Z] — § 8, inne
- art. 300³⁷ § 2 i art. 300³⁸ § 1 KSH [Z] — § 17
- art. 300³⁷–300³⁸ KSH [Z] — § 18
- art. 300³⁸ § 1 KSH [Z] — § 9
- art. 300³⁹ § 1 KSH („w inny sposób je ograniczyć”) i § 6 [Z] — § 12
- art. 300³⁹ § 1 KSH [Z] — § 11, § 14
- art. 300³⁹ § 1–2 KSH (ograniczenia rozporządzania akcją w umowie) [Z] — § 24
- art. 300³⁹ § 1–2 KSH („chyba że umowa spółki stanowi inaczej”) [Z] — § 11, § 12, § 16, § 21, § 32
- art. 300³⁹ § 1–2 KSH [Z] — § 10, § 12, § 13, § 30, § 38, inne
- art. 300³⁹ § 1–2 i § 6 KSH [Z] — § 13
- art. 300³⁹ § 1–6 KSH [Z] — § 12, § 16, § 32
- art. 300³⁹ § 2, 3 i 5 KSH [Z] — § 12
- art. 300³⁹ § 2–5 KSH [Z] — § 12, § 19
- art. 300³⁹ § 3–5 i art. 4 § 2¹ KSH [Z] — § 12
- art. 300¹ § 3 KSH (akcjonariusz zobowiązany tylko do świadczeń określonych w umowie) [Z] — § 24
- art. 300¹ § 3 KSH (obowiązki akcjonariusza z umowy) [Z] — § 33
- art. 300¹ § 3 KSH („akcjonariusze są zobowiązani jedynie do świadczeń określonych w umowie spółki”) [Z] — § 27, § 28
- art. 300¹ § 3 KSH [Z] — § 8, § 10, § 12, § 21, § 30, § 31, § 32, § 38, inne
- art. 300¹ § 3 i art. 2 KSH w zw. z art. 353¹, art. 57 i art. 58 KC [Z] — inne
- art. 300¹ § 3 i art. 4 § 2¹ KSH [Z] — § 12
- art. 300¹ § 3, art. 300³³, art. 300³⁹ § 6 KSH [Z] — § 11
- art. 300¹ § 3, art. 300⁹ § 2 KSH [Z] — § 38
- art. 300¹² § 1–4 KSH (zgłoszenie, załączniki, lista akcjonariuszy) [Z] — § 30, § 38
- art. 300¹² § 2 pkt 2 KSH (przedmiot działalności w zgłoszeniu) [Z] — § 4
- art. 300¹² § 2 pkt 4–5, art. 300³³ § 1 pkt 4 KSH [Z] — § 32
- art. 300¹²⁵ § 1 KSH (odpowiedzialność członka organu wobec spółki za szkodę, chyba że nie ponosi winy) [Z] — § 23
- art. 300¹²⁵ § 1–2 KSH (odpowiedzialność za szkodę, chyba że członek organu nie ponosi winy — § 21
- art. 300¹²⁹ KSH (actio pro socio do roszczeń o zwrot wypłat) [Z] — § 30
- art. 300¹³ § 1–2 w zw. z art. 164 § 3, art. 165, art. 169 § 1 i art. 172 KSH (drobne uchybienia, braki usuwalne, termin 6 miesięcy, braki po wpisie) [Z] — § 30, § 38
- art. 300¹³² KSH (odpowiedzialność za zobowiązania spółki przy bezskutecznej egzekucji — przepis mówi literalnie o „członkach zarządu”, a art. 300¹³³ rozciąga go tylko na likwidatorów) [Z] — § 21
- art. 300¹¹ § 1–2 KSH (spółka w organizacji — § 30, § 38
- art. 300¹¹ § 1–2 KSH (spółka w organizacji) [Z] — § 7
- art. 300¹¹ § 1–2 KSH [Z] — § 26
- art. 300¹¹⁰ § 1–3 KSH (pięcioletnie upoważnienie Rady, porównawczo) [Z] — § 9
- art. 300¹¹⁴–300¹¹⁸ KSH (warunkowa emisja akcji), art. 300¹¹⁹ KSH (warranty subskrypcyjne), art. 300⁸¹ pkt 4 KSH [Z] — § 8, inne
- art. 300¹⁰ § 1 KSH (wyrównanie znacznie zawyżonego wkładu na kapitał akcyjny) [Z] — § 30, § 38
- art. 300¹⁰² § 2 KSH (termin sześciu miesięcy na zgłoszenie zmiany umowy) [Z] — § 8, inne
- art. 300¹⁰³ KSH (emisja na podstawie postanowień umowy „przewidujących maksymalną liczbę akcji i termin ich emisji” bez trybu zmiany umowy) [Z] — § 11, § 12, § 16, § 21, § 32
- art. 300¹⁰³ KSH [Z] — § 9
- art. 300¹⁰³ i 300¹⁰⁶ § 2 KSH (emisja jako zmiana umowy — § 25
- art. 300¹⁰³, art. 300¹⁰⁴ § 1 pkt 1–7 i § 2, art. 300¹⁰⁵ § 1–3, art. 300¹⁰⁶ § 1–2 i 6, art. 300¹⁰⁷ § 1–3 KSH [Z] — § 8, inne
- art. 300¹⁰³–300¹⁰⁵ KSH (emisja i objęcie akcji nowej emisji) [Z] — § 12
- art. 300¹⁰³–300¹⁰⁷ KSH [Z] — § 12, § 16, § 32
- art. 300¹⁰¹ KSH w zw. z art. 422 § 1 KSH [Z] — § 32
- art. 300¹⁰¹ KSH w zw. z art. 422 § 2 KSH (legitymacja do zaskarżenia uchwały) [Z] — § 9
- art. 300¹⁰¹ KSH w zw. z art. 422 § 2 pkt 4 KSH (legitymacja akcjonariusza nieobecnego „jedynie w przypadku wadliwego zwołania walnego zgromadzenia”) [Z] — § 24
- art. 300¹⁰¹ w zw. z art. 422 § 1 KSH (uchylenie uchwały krzywdzącej akcjonariusza) [Z] — § 38
- art. 300¹⁰⁰ § 1 KSH (protokół z listą akcjonariuszy głosujących elektronicznie) i art. 300¹⁰¹ KSH (art. 422–427 stosowane odpowiednio do zaskarżania uchwał) [Z] — § 24
- art. 300¹⁰⁴ § 1 KSH [Z] — § 9
- art. 300¹⁰⁴ § 1 pkt 2 KSH (uprzywilejowanie akcji nowej emisji w uchwale o emisji) [Z] — § 12, § 16, § 32
- art. 300¹⁰⁴ § 1 pkt 2 KSH [Z] — § 11, § 12, § 16, § 21, § 32
- art. 300¹⁰⁵ § 1–3, art. 300¹⁰⁷ § 3, art. 300¹¹⁸ § 1 KSH [Z] — § 9
- art. 300¹⁰⁶ § 1–2 KSH (prawo poboru, „jeżeli umowa spółki lub uchwała akcjonariuszy nie stanowią inaczej” — § 11, § 12, § 16, § 21, § 32
- art. 300¹⁰⁶ § 1–3 i 6 KSH [Z] (§ 1: prawo poboru przysługuje, „jeżeli umowa spółki lub uchwała akcjonariuszy nie stanowią inaczej”) — § 13
- art. 300¹⁰⁶ § 2 KSH (pozbawienie prawa poboru) [Z] — § 12, § 16, § 32
- art. 300¹⁰⁸–300¹¹³ KSH (upoważnienie zarządu albo rady dyrektorów do emisji akcji) [Z] — § 8, inne
- art. 300¹⁵ § 2 i 4–6 KSH [Z] — § 17
- art. 300¹⁵ § 2 i 5 KSH (test bilansowy — § 30
- art. 300¹⁵ § 2 i § 4–6 KSH (kwota dostępna do wypłaty i test wypłacalności) [Z] — § 14
- art. 300⁴ pkt 3, art. 300⁹ § 1–3, art. 300¹⁰ § 1–2, art. 300¹² § 2 pkt 6–7, § 3 pkt 2–3 i § 4, art. 300¹²³, art. 300¹²⁴, art. 587 § 1 KSH [Z] — § 7
- art. 300⁴¹ § 1 KSH [Z] — § 17, § 19, inne
- art. 300⁴¹ § 1, art. 300³⁴ § 1 i 4, art. 300³⁷ § 2, art. 300³⁸ § 1, art. 300⁴⁴–300⁴⁶, art. 300⁴⁷ KSH [Z] — § 17
- art. 300⁴¹ § 1–2 KSH [Z] — § 17
- art. 300⁴⁰ § 2 KSH (14-dniowy termin ustawowy dla zgody na zbycie akcji nie w pełni pokrytej) [Z] — § 12
- art. 300⁴⁴–300⁴⁶ KSH (umorzenie przymusowe i automatyczne, spłata nie niższa od wartości godziwej) [Z] — § 17
- art. 300⁴⁵ § 1–2 KSH [Z] — § 10
- art. 300⁴⁵ § 2 KSH [Z] — § 19
- art. 300⁴⁵ § 2, art. 300⁴⁷ § 9 oraz art. 300⁴⁹–300⁵⁰ KSH [Z] — § 11
- art. 300⁴⁷ KSH [Z] — § 12, § 14, § 16, § 32
- art. 300⁴⁷ § 1 pkt 2, § 2–3 i § 9 KSH (nabycie na podstawie i w granicach upoważnienia udzielonego w uchwale akcjonariuszy — § 14
- art. 300⁴⁷ § 1–2 KSH [Z] — § 17
- art. 300⁴⁷ § 9 KSH [Z] — § 10
- art. 300⁴⁹ § 2 w zw. z art. 266 § 3 oraz art. 300⁵⁰ § 3 KSH (wyłączenie i ustąpienie akcjonariusza przez sąd) [Z] — § 19
- art. 300⁵ KSH (treść umowy) [Z] — § 12
- art. 300⁵ KSH [Z] — § 13
- art. 300⁵ § 1 KSH (elementy umowy) [Z] — § 30, § 38
- art. 300⁵ § 1 pkt 2 KSH (przedmiot działalności jako element umowy) [Z] — § 4
- art. 300⁵ § 1 pkt 3, art. 300²⁵ § 1–2, art. 300²⁶ KSH (akcje uprzywilejowane, akcje założycielskie) [Z] — § 32
- art. 300⁵ § 1 pkt 3, art. 300¹⁰⁰ § 2, art. 300¹⁰² § 1–2, art. 300¹⁰⁷ § 3 KSH [Z] — § 9
- art. 300⁵ § 1 pkt 3–4, art. 300¹⁰⁰ § 2, art. 300¹⁰² § 1–2 KSH [Z] — § 38
- art. 300⁵ § 1 pkt 3–5 i § 2 KSH [Z] — Zał. 1
- art. 300⁵² § 1 i art. 300⁵³ KSH (dyrektorzy podlegają ograniczeniom ustanowionym w umowie spółki), art. 18 § 1–2 KSH (wymogi ustawowe dla członków organów) [Z] — § 21
- art. 300⁵⁴ KSH (staranność i lojalność) i art. 300⁵⁵ § 1 KSH (konflikt interesów) [Z] — § 33
- art. 300⁵⁴ KSH (staranność zawodowa i lojalność członka organu) [Z] — § 27
- art. 300⁵⁴ KSH („staranności wynikającej z zawodowego charakteru swojej działalności oraz dochować lojalności wobec spółki”) [Z] — § 21
- art. 300⁵⁵ i 300⁷⁹ KSH [Z] — § 30
- art. 300⁵⁵ § 1 KSH (konflikt interesów) [Z] — § 27
- art. 300⁵⁵ § 1 KSH (obowiązek ujawnienia i wstrzymania się od udziału w rozstrzyganiu) [Z] — § 29
- art. 300⁵⁵ § 1 KSH („powinien ujawnić sprzeczność interesów i wstrzymać się od udziału w rozstrzyganiu takich spraw oraz może żądać zaznaczenia tego w protokole”) [Z] — § 21
- art. 300⁵⁵ § 1 KSH [Z] — § 19
- art. 300⁵⁵ § 1 i art. 300⁵⁸ § 2 KSH [Z] — § 10
- art. 300⁵⁵ § 2 KSH („członek organu nie może ujawniać tajemnic spółki, także po wygaśnięciu mandatu”) [Z] — § 27
- art. 300⁵⁵ § 3 KSH (dyrektor „nie może bez zgody spółki zajmować się interesami konkurencyjnymi ani uczestniczyć w spółce konkurencyjnej”, w tym przy co najmniej 10% głosów lub udziałów w konkurencyjnej spółce kapitałowej, „chyba że umowa spółki stanowi inaczej” — § 33
- art. 300⁵⁶ § 1–4 KSH (mandat — § 21
- art. 300⁵⁷ § 1 KSH (regulamin organu) [Z] — § 21
- art. 300⁵⁸ KSH (uchwały Rady) [Z] — § 12
- art. 300⁵⁸ § 1–5 KSH (§ 1 warunek prawidłowego zawiadomienia wszystkich członków o posiedzeniu albo głosowaniu na piśmie lub na odległość — § 21
- art. 300⁵⁸ § 2 KSH (quorum) [Z] — § 29
- art. 300⁵⁸ § 4 KSH („Uchwały organu zapadają bezwzględną większością głosów, chyba że umowa spółki stanowi inaczej” — § 23
- art. 300⁶ KSH (forma aktu notarialnego) [Z] — § 30, § 38, Zał. 1
- art. 300⁷ § 1 i 4 KSH (wzorzec — niewykorzystany — § 30, § 38
- art. 300⁷³ § 1 KSH (Rada Dyrektorów wykonuje kompetencje zarządu) [Z] — § 7
- art. 300⁷³ § 3 KSH (dyrektorów powołują akcjonariusze uchwałą, chyba że umowa stanowi inaczej) [Z] — § 32
- art. 300⁷³ § 3 KSH (powoływanie dyrektorów uchwałą akcjonariuszy) [Z] — § 29
- art. 300⁷³ § 3 KSH („Dyrektorów powołują i odwołują oraz zawieszają w czynnościach, z ważnych powodów, akcjonariusze uchwałą, chyba że umowa spółki stanowi inaczej”) [Z] — § 21
- art. 300⁷³ § 3 i art. 300⁷⁴ § 1 KSH (odwołanie dyrektora) [Z] — § 10
- art. 300⁷³–300⁷⁹ KSH (rada dyrektorów) i art. 300⁸⁰–300⁸¹ KSH (uchwały akcjonariuszy) [Z] — § 35
- art. 300⁷⁴ § 1–2 KSH (odwołanie w każdym czasie uchwałą akcjonariuszy — § 21
- art. 300⁷⁵ § 1–2 i art. 300⁷⁶ § 1 KSH [Z] — § 23
- art. 300⁷⁵ § 2 KSH (uchwały Rady wymaga podejmowanie decyzji o strategicznym znaczeniu, ustalanie planów biznesowych, ustalenie struktury organizacyjnej) [Z] — § 25
- art. 300⁷⁵ § 2 KSH [Z] — § 21, § 29, § 33
- art. 300⁷⁶ KSH (delegacja czynności prowadzenia przedsiębiorstwa umową, regulaminem albo uchwałą Rady, z wyjątkiem art. 300⁷⁵ § 2–3 — § 21
- art. 300⁷⁷ § 2 KSH (nieograniczalność prawa reprezentacji dyrektora wobec osób trzecich), art. 300⁵³ KSH [Z] — § 31
- art. 300⁷⁷ § 2 KSH („Prawa dyrektora do reprezentowania spółki nie można ograniczyć ze skutkiem prawnym wobec osób trzecich”) [Z] — § 23
- art. 300⁷⁹ KSH [Z] — § 29
- art. 300⁷⁹ § 1 KSH [Z] — § 9
- art. 300⁸¹ KSH (katalog czynności wymagających uchwały akcjonariuszy: pkt 2 zbycie i wydzierżawienie przedsiębiorstwa albo ZCP oraz ustanowienie na nich ograniczonego prawa rzeczowego — bez opt-out — § 25
- art. 300⁸¹ pkt 2 KSH („zbycie i wydzierżawienie przedsiębiorstwa albo jego zorganizowanej części oraz ustanowienie na nich ograniczonego prawa rzeczowego” — uchwała akcjonariuszy z mocy ustawy, bez klauzuli opt-out, gdy wkład do Przedsięwzięcia ma taki charakter) [Z] — § 33
- art. 300⁸¹ pkt 2 i 4, art. 300¹¹⁴ § 3 KSH (uchwały akcjonariuszy wymagane ustawą) [Z] — § 31
- art. 300⁸⁰ § 1–2 KSH (uchwały poza WZ na piśmie albo elektronicznie — § 24
- art. 300⁸⁰ § 1–3 KSH (uchwała akcjonariuszy poza WZ — § 29
- art. 300⁸⁷ § 1 KSH (zwołanie walnego zgromadzenia pocztą elektroniczną na adres wpisany do rejestru) [Z] — § 5
- art. 300⁸⁷ § 1 KSH („Walne zgromadzenie zwołuje się pocztą elektroniczną na adres akcjonariusza wpisany do rejestru akcjonariuszy, na adres do doręczeń elektronicznych lub za pomocą listu poleconego lub przesyłki nadanej pocztą kurierską” — § 24
- art. 300⁸⁷ § 4 KSH (zawiadomienie „powinno zawierać dokładny opis sposobu uczestnictwa w walnym zgromadzeniu i wykonywania prawa głosu”) [Z] — § 24
- art. 300⁸⁸ § 1–2 KSH (WZ „odbywa się w siedzibie spółki, jeżeli umowa spółki nie wskazuje innego miejsca” — § 24
- art. 300⁹ § 1 KSH (wniesienie wkładów w całości w 3 lata od wpisu) [Z] — § 30, § 38
- art. 300⁹ § 3, art. 300¹² § 2 pkt 7, § 3 i § 4 KSH (zgłoszenie, oświadczenia, lista akcjonariuszy) [Z] — Zał. 1
- art. 300⁹² § 1–2 KSH (umowa „może dopuszczać” udział elektroniczny — § 24
- art. 300⁹⁰ KSH (uchwały mimo braku formalnego zwołania, jeżeli reprezentowane są wszystkie akcje i nikt nie zgłosił sprzeciwu) [Z] — § 24
- art. 300⁹⁶ KSH (ustawowe wyłączenie od głosowania: odpowiedzialność, absolutorium, zwolnienie z zobowiązania, spór) [Z] — § 24
- art. 300⁹⁶ KSH (wyłączenie od głosowania — nie obejmuje głosowania nad własnym odwołaniem) [Z] — § 21
- art. 300⁹⁸ § 1 KSH (bezwzględna większość głosów jako reguła domyślna, „jeżeli przepisy niniejszego działu lub umowa spółki nie stanowią inaczej”) [Z] — § 21
- art. 300⁹⁸ § 1–2 KSH (bezwzględna większość jako reguła — § 24
- art. 300⁹⁸ § 1–2 KSH (większości kwalifikowane 3/4 — § 25
- art. 300⁹⁸ § 2 i art. 300¹⁰³ KSH [Z] — § 30, § 38
- art. 300⁹⁸ § 2 pkt 1, art. 300¹⁰⁰ § 2 i art. 300¹⁰² § 1–2 KSH (zmiana umowy: większość trzech czwartych, protokół notarialny, wpis do rejestru, zgłoszenie w 6 miesięcy) [Z] — § 4
- art. 300⁹⁸ § 2 pkt 2 KSH (zbycie przedsiębiorstwa albo ZCP — 3/4 głosów) [Z] — § 33
- art. 300⁹⁸ § 2–5 KSH (większość 3/4 dla zmiany umowy — § 38
- art. 300⁹⁸ § 3 KSH (zmiana umowy „uszczuplająca prawa indywidualne poszczególnych akcjonariuszy, wymaga zgody wszystkich akcjonariuszy, których dotyczy”) [Z] — § 24
- art. 300⁹⁸ § 4–5, art. 300¹⁰⁰ § 2, art. 300¹⁰²–300¹⁰⁴, art. 300¹⁰⁶ § 1–2, art. 300¹¹⁰ § 5 KSH [Z] — § 32
- art. 300⁹⁹ § 2 i art. 300⁸⁰ § 3 KSH (tajne głosowanie przy powołaniu i odwołaniu — § 21
- art. 362 § 1 pkt 8 KSH (dla porównania: pięcioletni limit upoważnienia w spółce akcyjnej) [Z] — § 14
- art. 394 § 1 KSH (S.A.: nabycie mienia od założyciela lub akcjonariusza za cenę ponad 1/10 wpłaconego kapitału zakładowego przed upływem dwóch lat od zarejestrowania — uchwała WZ większością 2/3 — § 30
- art. 4 § 1 pkt 10 KSH (bezwzględna większość: „więcej niż połowę głosów oddanych”) [Z] — § 21
- art. 4 § 1 pkt 4 KSH (definicja spółki dominującej — pomocniczo do pojęcia kontroli) [Z] — § 10
- art. 4 § 1 pkt 9–10 KSH (głosy „za”, „przeciw” lub „wstrzymujące się” oddane — § 24
- art. 419 § 1 KSH (S.A., porównawczo) [Z] — § 38
- art. 444 § 1 KSH (porównawczo) [Z] — § 8, § 9, inne
- art. 506 § 1, 541 § 1 (3/4 głosów przy reprezentacji co najmniej połowy kapitału), 575 (2/3 kapitału) i 577 § 1 pkt 1 KSH (3/4 głosów przy połowie kapitału), każdorazowo „chyba że umowa ... przewiduje surowsze warunki” [Z] — § 25
- ustawa z 23 stycznia 2026 r. (Dz.U. 2026 poz. 176): od 18 lutego 2027 r. art. 300³² § 1¹–1³ i § 3, art. 300³³ § 3, art. 300³⁴ § 3 zdanie drugie i § 9, art. 300³⁵ § 1¹ KSH, art. 38 pkt 8a lit. j ustawy o KRS, art. 83a ust. 4ac ustawy o obrocie instrumentami finansowymi, art. 90a § 1 Prawa o notariacie [Z] — § 5

**Konstytucja**

- art. 21 ust. 1 i art. 64 Konstytucji RP [Z] — § 17
- art. 21 ust. 1, art. 31 ust. 3, art. 64 ust. 1–3 Konstytucji RP [Z] — § 17
- art. 42 ust. 3 Konstytucji RP (domniemanie niewinności — pomocniczo) [Z] — § 10

**Prawo własności przemysłowej**

- art. 53 ustawy o prawie autorskim, art. 12 ust. 1–2 i art. 67 ust. 2–3 PWP [Z] — § 30, § 38

**Rozporządzenie 2019/452**

- inwestycja greenfield poza obowiązkowym zakresem) i art. 30 ust. 1 i 3 oraz art. 31 (stosowanie od 17.01.2028 r., z tym dniem uchylenie rozporządzenia 2019/452 — § 33
- rozporządzenie (UE) 2019/452 (obowiązuje do 16 stycznia 2028 r — § 12

**Rozporządzenie 2021/697 (EDF)**

- art. 2 pkt 6 i 24, art. 5 i art. 9 ust. 1–4 i 7 rozporządzenia (UE) 2021/697 (EDF) [Z] — § 12, § 16, § 32
- art. 2 pkt 6 i 24, art. 5 oraz art. 9 ust. 3–4 i 7 rozporządzenia 2021/697 (EDF: kontrola przez państwo trzecie) [Z] — § 11
- art. 2 pkt 6, 7 i 24, art. 5 oraz art. 9 ust. 1–4 i 7 rozporządzenia (UE) 2021/697 (EDF) [Z] — inne
- art. 5 i art. 9 rozporządzenia (UE) 2021/697 (EDF): państwa stowarzyszone to członkowie EFTA należący do EOG (art. 5) — § 33
- art. 9 ust. 3–4 rozporządzenia (UE) 2021/697 (EDF: odbiorcy i podwykonawcy uczestniczący w działaniu nie podlegają kontroli niestowarzyszonego państwa trzeciego ani podmiotu z takiego państwa — § 31

**Rozporządzenie 2021/821 (dual-use)**

- art. 1 oraz art. 2 pkt 2 lit. d i pkt 10 lit. c rozporządzenia (UE) 2021/821 [Z] (tekst EN, wersja skonsolidowana na 26.05.2023) — § 11
- art. 2 pkt 2 lit. d i pkt 3 lit. b, art. 3 ust. 1, art. 8 ust. 1–3, art. 12 ust. 1 oraz załącznik II sekcje A–F (EU001–EU006) rozporządzenia (UE) 2021/821 [Z] (tekst EN) — § 27
- rozporządzenie (UE) 2021/821 (tekst skonsolidowany na 26 maja 2023 r., EN): art. 2 pkt 1–3, 9–10 i 21 (definicje produktów podwójnego zastosowania, wywozu — w tym transmisji elektronicznej i udostępnienia oprogramowania lub technologii osobom poza obszarem celnym Unii, eksportera, pomocy technicznej, wewnętrznego programu zgodności), art. 3 ust. 1, art. 4 ust. 1–2 (klauzula catch-all i obowiązek powiadomienia), art. 8 ust. 1–3 (pomoc techniczna), art. 11 ust. 1 i 9 (transfer wewnątrzunijny), art. 12 ust. 1 i 4 (rodzaje zezwoleń — § 28
- rozporządzenie (UE) 2021/821 (unijny system kontroli wywozu, pośrednictwa, pomocy technicznej, tranzytu i transferu produktów podwójnego zastosowania — § 11, § 12, § 16, § 21, § 32
- rozporządzenie (UE) 2021/821 i unijne generalne zezwolenie na wywóz EU001 (załącznik II sekcja A — § 33
- rozporządzenie (UE) 2021/821, art. 2 pkt 2 lit. d (eksportem jest przekazanie oprogramowania lub technologii drogą elektroniczną do miejsca przeznaczenia poza obszarem celnym Unii, w tym udostępnienie ich w formie elektronicznej osobom spoza tego obszaru) i art. 4 ust. 1 (klauzula catch-all: zezwolenie na wywóz pozycji spoza załącznika I po poinformowaniu przez organ o przeznaczeniu) [Z] (tekst EN, wersja skonsolidowana 2023) — § 33
- rozporządzenie (UE) 2021/821, załącznik I (tekst skonsolidowany na 26 maja 2023 r., EN — Zał. 3
- rozporządzenie (UE) 2021/821: art. 2 pkt 1 (produkty podwójnego zastosowania obejmują oprogramowanie i technologię) [Z] (tekst EN) — § 4, § 11
- ustawa z 29.11.2000 r. o obrocie z zagranicą towarami, technologiami i usługami o znaczeniu strategicznym (art. 2: obrót dozwolony na zasadach rozporządzenia 2021/821 — § 33

**Rozporządzenie 2026/1386 (kontrola inwestycji zagranicznych)**

- art. 1 ust. 4 i ust. 5 lit. b, art. 2 pkt 1, 5, 7 i 9, art. 3 ust. 1–2, art. 4 ust. 2, 4–5, 7, 9, 11 i 15–17, art. 5 ust. 1–2, art. 6, art. 9, art. 11 ust. 3–5, art. 12 ust. 1 i 3, art. 19 ust. 1 lit. a–b i ust. 2 lit. a–b, d–e, art. 20 ust. 1 i 4, art. 30 ust. 1–3, art. 31, motywy 14, 15 i 20 oraz załączniki I–III rozporządzenia (UE) 2026/1386 z 17 czerwca 2026 r. w sprawie kontroli inwestycji zagranicznych [Z] (tekst EN) — § 12
- art. 2 pkt 1 rozporządzenia (UE) 2026/1386 [Z] (tekst EN) — § 31
- art. 2 pkt 1, 2, 5 i 7 oraz art. 4 ust. 9 i 15–17 rozporządzenia (UE) 2026/1386 (inwestor zagraniczny to osoba fizyczna bez obywatelstwa państwa członkowskiego albo podmiot utworzony według prawa państwa trzeciego, także działający przez spółkę zależną w UE — § 33
- art. 2 pkt 1, 5 i 7, art. 4 ust. 1, 2, 9 i 15 lit. a–c, art. 5 ust. 1–2, art. 6, art. 11 ust. 3 i 5, art. 20 ust. 4 lit. a, art. 30–31, motywy 14–15 i 20, zał. I pkt 1–3 i zał. II pkt 14 rozporządzenia (UE) 2026/1386 [Z] (tekst EN) — § 11, § 12, § 16, § 21, § 32
- art. 2 pkt 1, 5 i 7, art. 4 ust. 1, 2, 9 i 15, art. 5 ust. 2 lit. a, art. 11 ust. 3 i 5, art. 30 ust. 3, art. 31 oraz załącznik II pkt 14 rozporządzenia (UE) 2026/1386 [Z] (tekst EN) — § 32
- art. 2 pkt 1, 5 i 7, art. 4 ust. 15 lit. a–b i ust. 17, art. 30 ust. 1, art. 31 oraz motywy 14, 15 i 20 rozporządzenia (UE) 2026/1386 (kontrola inwestycji zagranicznych, stosowane od 17 stycznia 2028 r.) [Z] (tekst EN) — inne
- art. 2 pkt 1, 5 i 7, art. 4 ust. 2, 9 i 15, art. 5 ust. 1–2, art. 15 ust. 1 lit. b i ust. 3, art. 19 ust. 2 lit. e oraz motywy 14–15 rozporządzenia (UE) 2026/1386 (kontrola inwestycji zagranicznych, stosowane od 17 stycznia 2028 r., art. 31) [Z] (tekst EN) — § 12, § 16, § 32
- art. 2 pkt 1, 5, 7 i 8, art. 4 ust. 15, art. 5 ust. 1 lit. a, art. 15 ust. 1 lit. a–b i ust. 3, art. 19 ust. 2 lit. e oraz motyw 18 rozporządzenia (UE) 2026/1386 (od 17 stycznia 2028 r.) [Z] (tekst EN) — § 11
- art. 2 pkt 1, 7 i 8 oraz art. 19 ust. 2 lit. e rozporządzenia (UE) 2026/1386 [Z] (tekst EN) — § 11
- do jego zał. I odsyła art. 4 ust. 15 lit. a rozporządzenia 2026/1386) [Z] (tekst EN, konsolidacja na 26.05.2023 r.) — § 11, § 12, § 16, § 21, § 32

**Rozporządzenie 2026/877 (TTBER)**

- rozporządzenia (UE) 2023/1066 (B+R) i 2023/1067 (specjalizacja) oraz wytyczne horyzontalne 2023 (wspólna produkcja) [W] — art. 9 rozporządzenia 2026/877 wyłącza jego stosowanie do licencji w umowach B+R i specjalizacyjnych objętych tymi rozporządzeniami [Z] (tekst EN) — § 33

**TFUE**

- art. 101 ust. 1 TFUE (klauzule niekonkurowania w JV jako ograniczenia akcesoryjne) [W] — § 33
- art. 101 ust. 1 i 3 TFUE [W] — § 33
- art. 18 TFUE [W] — § 17
- art. 18, 49 i 63 TFUE (adresowane do państw — § 33
- art. 18, 49, 63, 65 ust. 1 lit. b i art. 346 ust. 1 lit. b TFUE [W] — inne
- art. 63 TFUE (dziedziczenie jako przepływ kapitału w orzecznictwie TSUE) [W] — § 17
- rozporządzenie Komisji (UE) 2026/877 z 16.04.2026 r. w sprawie stosowania art. 101 ust. 3 TFUE do kategorii porozumień o transferze technologii (art. 1 ust. 1 lit. b pkt vii: prawa do technologii obejmują prawa autorskie do oprogramowania — § 33

**Ustawa o CIT**

- art. 11a–11t ustawy o CIT [W] — § 30
- art. 12 ust. 1 pkt 2 ustawy o CIT [W] — § 7

**Ustawa o PIT**

- art. 12 ust. 1 i art. 17 ust. 1 pkt 6 lit. a ustawy o PIT [Z] — § 10
- art. 17 ust. 1 pkt 9, art. 19 ust. 1 i 3–4, art. 21 ust. 1 pkt 109, art. 22 ust. 1e i 1f ustawy o PIT [Z] — § 7
- art. 17 ust. 1 pkt 9, art. 19 ust. 1 i 4, art. 22 ust. 1e pkt 3 ustawy o PIT [Z] — § 7
- art. 19 ust. 1 w zw. z art. 17 ust. 2 oraz art. 11 ust. 2b ustawy o PIT [Z] — § 10
- art. 23m–23zf ustawy o PIT (rozdział 4b: ceny transferowe — § 30

**Inne**

- 250 zł za zmianę) [Z] — § 30, § 38
- 3/4 głosów dla zmiany umowy, zbycia przedsiębiorstwa lub ZCP, obligacji zamiennych i rozwiązania, „chyba że umowa spółki przewiduje surowsze warunki”) [Z] — § 24
- 30 dni roboczych i 120 dni) [Z] — § 12
- 5A002.a, 5D002, 5E002 (kryptografia) oraz załącznik IV (w tym 1C101 i 1D103 — redukcja wykrywalności, także BSP z 9A012) [Z] (tekst EN) — Zał. 3
- 6A008 (radary, w tym SAR), 6D001–6D002, 6E001 — Zał. 3
- 7A003 (inercyjne urządzenia pomiarowe — Zał. 3
- ICP przy zezwoleniu globalnym), art. 17 ust. 1 (aktualizacja załączników I i IV aktami delegowanymi), art. 27 ust. 1, 3–4 (ewidencja), załącznik II sekcja A (EU001, część 2–3) i sekcja G (EU007) [Z] (tekst EN — § 28
- Minister Obrony Narodowej jako organ dla sektora zbrojeniowego) [Z] — § 12
- NATO Innovation Fund (wspierany przez 24 państwa NATO, inwestuje w spółki z siedzibą w jednym z tych państw — `web_nif_about.txt`) [Z] — § 11
- SN, wyrok z 23 czerwca 2020 r., V CSK 522/18 [Z] — § 32
- Wspólny wykaz uzbrojenia UE, ML10 (BSP) i ML21/ML22 [W] — Zał. 3
- `vc.md` sekcja 6 pkt 1 [W] — § 11
- art. 1 pkt 16–27 (zmiany dotyczące wyłącznie spółki akcyjnej, m.in. uchylenie art. 334 i zmiany art. 337, 351, 352, 356, 361, 406¹, 432, 434, 453, 476) [Z] — § 5, § 24
- art. 1 pkt 1–2 w zw. z art. 2 ust. 1 ustawy z 13 kwietnia 2022 r. o szczególnych rozwiązaniach w zakresie przeciwdziałania wspieraniu agresji na Ukrainę (lista krajowa prowadzona przez ministra właściwego do spraw wewnętrznych — § 12
- art. 1 pkt 2, art. 2, art. 6 ust. 1–2, art. 6a ust. 1, 11, 15–16 i 27, art. 6b ust. 1 i 4 oraz art. 6da ustawy z 13 kwietnia 2022 r. o szczególnych rozwiązaniach w zakresie przeciwdziałania wspieraniu agresji na Ukrainę oraz służących ochronie bezpieczeństwa narodowego [Z] — § 11
- art. 1 ust. 1 lit. c pkt i: umowa licencyjna zawarta „w celu wytwarzania produktów objętych umową przez licencjobiorcę lub jego podwykonawców” (tłum. robocze) — § 33
- art. 10 ust. 1 pkt 2 ustawy z 13 czerwca 2019 r. (koncesja) [Z] — § 12
- art. 10 ust. 1 pkt 2 w zw. z pkt 1 lit. a ustawy z 13 czerwca 2019 r. — wymogi obywatelstwa osób kierujących działalnością koncesjonowaną [Z] — § 21
- art. 11 ust. 1–2 i 4 oraz art. 18 ust. 1 ustawy z 16 kwietnia 1993 r. o zwalczaniu nieuczciwej konkurencji [Z] — § 27
- art. 11 ust. 1–3, art. 12 ust. 1–2, art. 20, art. 67 ust. 2–3, art. 72 ust. 1 ustawy Prawo własności przemysłowej [Z] — § 26
- art. 11: wejście w życie 1.05.2026 r., wygaśnięcie 30.04.2038 r.) [Z] (tekst EN) — § 33
- art. 11³ Kodeksu pracy — dotyczy „dyskryminacji w zatrudnieniu”, nie stosunku organizacyjnego [Z] — § 21
- art. 12a–12k ustawy z 24 lipca 2015 r. o kontroli niektórych inwestycji [Z] — inne
- art. 12a–12k ustawy z 24 lipca 2015 r. o kontroli niektórych inwestycji, w szczególności art. 12a ust. 1 pkt 1, art. 12c ust. 1 pkt 1, 4 i 5, art. 12d ust. 3 pkt 7 i ust. 4, art. 12e ust. 4, art. 12f ust. 1 i 5, art. 12h ust. 5 i 8, art. 12k ust. 1 oraz art. 16a [Z] — § 12
- art. 17 ust. 1 pkt 2 tej ustawy (numer KRS we wniosku „o ile przedsiębiorca taki numer lub wpis posiada”) [Z] — § 4
- art. 2 (art. 90a § 1 Prawa o notariacie) [Z] — § 5, § 24
- art. 2 ust. 2 pkt 1 lit. a ustawy AML (beneficjent rzeczywisty) [Z] — § 11
- art. 2 ust. 2 pkt 1 ustawy AML [Z] — § 11, § 12, § 16, § 21, § 32
- art. 2 ust. 2 pkt 1 ustawy z 2018 r. o przeciwdziałaniu praniu pieniędzy oraz finansowaniu terroryzmu (beneficjent rzeczywisty: osoba fizyczna sprawująca kontrolę, w tym mająca „więcej niż 25% ogólnej liczby udziałów lub akcji” albo głosów, a w braku takiej osoby — osoba na wyższym stanowisku kierowniczym) [Z] — § 12, § 16, § 32
- art. 2 wyłączenie — § 33
- art. 28–34 (przepisy przejściowe) [Z] — § 5, § 24
- art. 3 pkt 10 organ kontroli obrotu — minister właściwy do spraw gospodarki), znowelizowana ustawą z 13.03.2026 r. (Dz.U. 2026 poz. 471, ogłoszona 7.04.2026 r., wejście w życie po 14 dniach) [Z] — § 33
- art. 3 pkt 5b pomoc techniczna — § 33
- art. 3 ust. 1 (zezwolenie na wywóz pozycji z załącznika I), art. 8 ust. 1 (zezwolenie na pomoc techniczną dotyczącą pozycji z załącznika I, gdy organ poinformował o przeznaczeniu z art. 4 ust. 1) i ust. 3 lit. a (wyłączenie dla pomocy w państwach z części 2 sekcji A załącznika II), art. 11 ust. 1 i załącznik IV (zezwolenie na transfer wewnątrzunijny pozycji z załącznika IV) [Z] (tekst EN), pozycje załącznika IV nieweryfikowane — § 33
- art. 3 ust. 1 pkt 12: technologia to „informacje niezbędne do rozwoju, produkcji lub używania danego wyrobu ... mające postać danych technologicznych lub pomocy technicznej”) [Z] — § 33
- art. 3 ust. 1 pkt 12–13 (definicje technologii i wyrobów o przeznaczeniu wojskowym lub policyjnym), art. 4, art. 5, art. 7 ust. 1, art. 8 ust. 1–2, art. 9 ust. 1, art. 10 ust. 1 pkt 2–3, art. 11–12, art. 17 i art. 133 tej ustawy [Z] — § 4, § 11
- art. 3 ust. 1 pkt 5–6 i art. 4 tej ustawy (wykaz podmiotów podlegających ochronie — § 12
- art. 300³³ § 1 pkt 10–11 i § 2) [Z] — § 38
- art. 35 (wejście w życie po upływie 12 miesięcy od ogłoszenia, tj. 18 lutego 2027 r., z wyjątkiem art. 28 i 33 — 28 lutego 2026 r.) [Z] — § 5, § 24
- art. 37 i n. ustawy Prawo przedsiębiorców [numery do sprawdzenia] [W] — § 4
- art. 3: progi 20% łącznie dla konkurentów i 30% dla każdej ze stron wśród niekonkurentów — § 33
- art. 4 ust. 1 pkt 1 ustawy z 29 lipca 2005 r. o obrocie instrumentami finansowymi (domy maklerskie, banki prowadzące działalność maklerską, banki powiernicze, zagraniczne firmy inwestycyjne działające przez oddział, KDPW, NBP) [Z] — § 5
- art. 5 i art. 7 ust. 1 ustawy z 13 czerwca 2019 r. (koncesja warunkuje *wykonywanie* działalności) [Z] — § 4
- art. 5 ust. 1 lit. a: wyłączeniem nie jest objęte „bezpośrednie lub pośrednie zobowiązanie licencjobiorcy do udzielenia licencji wyłącznej albo przeniesienia praw, w całości lub w części, na licencjodawcę […] w odniesieniu do własnych ulepszeń albo własnych nowych zastosowań licencjonowanej technologii” (tłum. robocze) — § 33
- art. 54 ust. 1–2 ustawy z 5 sierpnia 2010 r. o ochronie informacji niejawnych (świadectwo bezpieczeństwa przemysłowego) [Z] — § 27
- art. 57 ust. 2 pkt 1 ustawy z 5 sierpnia 2010 r. o ochronie informacji niejawnych (bezpieczeństwo przemysłowe) [Z] — § 12
- art. 92 § 1 ustawy Prawo o notariacie [W] — Zał. 1
- bezwzględna większość) [Z] — § 24
- brak Turcji, którą obejmują tylko wąskie zezwolenia EU002–EU006) [Z] (tekst EN, wersja skonsolidowana 2023) — § 33
- brak odpowiednika w P.S.A., wzorzec) [Z] — § 30
- brak w niej ustawowej definicji „wytwarzania” i „obrotu” [Z] — § 4, § 11
- brzmienie identyczne) [Z] i orzecznictwo do sp. z o.o. [W] — § 17
- część 1: wszystkie pozycje z załącznika I poza wymienionymi w sekcji I załącznika II — § 33
- część 2: Australia, Kanada, Islandia, Japonia, Nowa Zelandia, Norwegia, Szwajcaria z Liechtensteinem, Zjednoczone Królestwo, USA — § 33
- daty stosowania do sprawdzenia pod kątem późniejszych zmian [?]) — § 28
- dodatkowe informacje ujawniane w rejestrze na podstawie umowy) [Z] — § 27
- dokumenty — § 12
- dostęp podmiotów zagranicznych na podstawie umów dwustronnych [W] — § 33
- dyrektywa (UE) 2016/943 [W] — § 27
- dyrektywa 2011/61/UE (AIFMD) [W] — § 11
- dyrektywa 2011/61/UE [W] — § 11
- działanie „w granicach uzasadnionego ryzyka gospodarczego”) [Z] — § 21
- głosowanie elektroniczne, jeżeli środki wskazano w umowie) [Z] — § 24
- inne miejsce za zgodą wszystkich akcjonariuszy w formie dokumentowej) [Z] — § 24
- kadencja liczona w latach obrotowych — § 21
- katalog otwarty: uprzywilejowanie „może dotyczyć w szczególności prawa głosu, prawa do dywidendy lub podziału majątku w przypadku likwidacji spółki”) [Z] — § 12, § 16, § 32
- miejsce za granicą wymaga dodatkowo miejsca w Polsce — § 24
- nie dotyczy uchwał podejmowanych poza zgromadzeniem) [Z] — § 21
- nowych przepisów nie stosuje się do inwestycji zakończonych albo kontrolowanych w tym dniu) [Z] (tekst EN) — § 33
- objęcie art. 300¹³² dyrektorów w drodze wykładni [?] — § 21
- od 18 lutego 2027 r. zastaw rejestrowy powstaje z wpisem do rejestru zastawów bez wpisu w rejestrze akcjonariuszy) [Z] — § 12
- odbiorcy i podwykonawcy „nie podlegają kontroli niestowarzyszonego państwa trzeciego lub podmiotu z niestowarzyszonego państwa trzeciego” (art. 9 ust. 3) — § 33
- oddzielne głosowanie w grupie akcji jednorodzajowych) [Z] — § 38
- odstępstwo dla podmiotu z siedzibą w UE lub państwie stowarzyszonym kontrolowanego z takiego państwa tylko przy gwarancjach zatwierdzonych przez państwo członkowskie lub stowarzyszone jego siedziby, m.in. że odbiorca pozostanie właścicielem praw własności intelektualnej wynikających z działania i rezultatów, a te nie będą podlegały kontroli ani ograniczeniu ze strony niestowarzyszonego państwa trzeciego ani podmiotu z takiego państwa (art. 9 ust. 4 lit. c) — § 33
- opłata za ogłoszenie w MSiG 100 zł [W] — § 30, § 38
- osoba trzecia działająca na rachunek spółki) [Z] — § 14
- pkt 3 „nabycie i zbycie nieruchomości, użytkowania wieczystego lub udziału w nieruchomości, chyba że umowa spółki stanowi inaczej” — § 25
- pkt 4 obligacje zamienne i warranty — § 25
- pkt 5 umowa o zarządzanie spółką zależną) [Z] — § 25
- po nowelizacji Dz.U. 2026 poz. 176, od 18.02.2027 r., pkt 5 zachowuje wymóg zgody i dodaje PESEL albo datę urodzenia) [Z] — § 24
- podmioty powiązane od 25% udziałów lub głosów, art. 23m ust. 1 pkt 4) [Z] — § 30
- postać elektroniczna, dopuszczalna baza rozproszona — § 5
- powiadomienie osoby, której prawa mają być wykreślone, zmienione lub obciążone) [Z] — § 5
- pozbawienie prawa poboru „większością czterech piątych głosów”) [Z] — § 25
- pozbawienie uchwałą większością 4/5) [Z] — § 11, § 12, § 16, § 21, § 32
- pozycje 9A012.a (BSP), 9A112 (BSP o zasięgu 300 km albo z autonomicznym sterowaniem i rozpylaczem), 9D001–9D002, 9D004.e (oprogramowanie do działania BSP z 9A012), 9E001–9E002, 9E101–9E102 — Zał. 3
- praktyka rynkowa: wzorce NVCA po aktualizacji z 2 października 2025 r. (`web_nvca_2025_press.txt`, `web_nvca_2025_foley.txt`) [Z], omówienia PFR Startup (`web_pfr_umowa_inwestycyjna.txt`, `pfr_startup_umowa_inwestycyjna.txt`, pfr_startup_term_sheet.txt) [Z], strony programów PFR Ventures (`pfr_pfrv_starter.txt`, `pfr_pfrv_biznest.txt`, `pfr_pfrv_otwarte_innowacje.txt`, `pfr_pfrv_koffi.txt`) [Z], wzorce BVCA i treść wzorów term sheet PFR Ventures (same wzory nie zostały pobrane, `pfr_pfrv_feng_dokumentacja.txt`) [W] — § 12, § 16, § 32
- przedawnienie 3 lata, chyba że odbiorca wiedział o bezprawności) [Z] — § 30
- przeniesienie własności wyników działań badawczych albo udzielenie licencji wyłącznej na rzecz niestowarzyszonego państwa trzeciego lub podmiotu z takiego państwa wymaga uprzedniego powiadomienia Komisji, a gdy jest sprzeczne z interesami bezpieczeństwa i obronności Unii — zwrotu wsparcia (art. 20 ust. 4) [Z] — § 33
- przesunięcie daty stosowania na 31 grudnia 2020 r. rozporządzeniem wykonawczym (UE) 2020/746 [W] — § 4, § 11
- przy wzorcu tylko wkłady pieniężne) [Z] — § 30, § 38
- reprezentacja) [Z] — § 30, § 38
- rozporządzenie (UE) 2018/1139, art. 2 ust. 3 lit. a [W] — § 4, § 11
- rozporządzenie (UE) 2021/697, art. 9 ust. 4 [Z] — § 28
- rozporządzenie (UE) 2024/1689 (AI Act): art. 2 ust. 2, 3, 6 i 8, art. 3 pkt 1, art. 6 ust. 1, art. 108, art. 113, motyw 12, załącznik I sekcja B pkt 20 [Z] (tekst EN — § 28
- rozporządzenie 833/2014 [W] — § 12
- rozporządzenie Rady Ministrów z 17 września 2019 r. w sprawie klasyfikacji rodzajów materiałów wybuchowych, broni, amunicji oraz wyrobów i technologii o przeznaczeniu wojskowym lub policyjnym, na których wytwarzanie lub obrót jest wymagane uzyskanie koncesji (Dz.U. 2019 poz. 1888): część IV, kategoria WT V ust. 3, WT XI ust. 2, WT XIII ust. 3–4 oraz definicje pkt 12–15 załącznika [Z] — § 4, § 11
- rozporządzenie delegowane (UE) 2019/945 [W] — § 4, § 11
- rozporządzenie wykonawcze (UE) 2019/947 (tekst pierwotny): art. 2 pkt 1 i 17, art. 3–6, art. 12, art. 14 ust. 5–6, art. 23 ust. 1–2, załącznik część A pkt UAS.OPEN.060 ust. 2 lit. d i część B pkt UAS.SPEC.050 ust. 1 lit. b [Z] (tekst EN) — § 4, § 11
- rozwiązanie przez spółkę tylko pod warunkiem zawarcia nowej — § 5
- skutek horyzontalny ograniczony) [W] — § 33
- solidarna odpowiedzialność członków organów, „chyba że nie ponoszą winy” — § 30
- stały nadzór dyrektorów niewykonawczych) [Z] — § 21
- stosowanie art. 15 do dyrektora w drodze wykładni [?] — § 25
- strony programów PFR Ventures (`pfr_pfrv_starter.txt`, `pfr_pfrv_biznest.txt`, `pfr_pfrv_otwarte_innowacje.txt`, `pfr_pfrv_koffi.txt`) [Z] — § 11
- t.j. Dz.U. 2023 poz. 1743), zmieniona art. 2 ustawy z 13 marca 2026 r. (Dz.U. 2026 poz. 471) [Z] — § 4, § 11
- tajne głosowanie z art. 300⁹⁹ § 2 nie ma tu zastosowania) [Z] — § 29
- tekst niedostępny) [W] — § 12
- teksty orzeczeń niedostępne) — § 10, § 18, inne
- test wypłacalności na 6 miesięcy) [Z] — § 30
- umowa może przewidzieć głos rozstrzygający „prezesa, przewodniczącego lub innego członka organu”), § 2 (umowa może przewidywać surowsze wymagania dotyczące kworum) i § 5 (protokół z imionami i nazwiskami głosujących oraz wynikiem) [Z] — § 23
- umowa „może zawierać inne postanowienia, w szczególności ograniczać prawo odwołania do ważnych powodów”) [Z] — § 21
- unijne generalne zezwolenia na wywóz EU001 (załącznik II sekcja A, bez Turcji) i EU002–EU006 (sekcje B–F: Turcja objęta tylko dla wąskich kategorii pozycji albo operacji — np. EU002: 1A001, 1A003, 3C003–3C006) [Z] (tekst EN, wersja skonsolidowana 2023) — § 33
- uprzednie zezwolenie przed zamknięciem transakcji — § 33
- uwaga 2 wyłącza urządzenia certyfikowane dla lotnictwa cywilnego), 7A103, 7D002–7D004, 7E001, 7E004.b — Zał. 3
- uwzględnianie ograniczeń) [Z] — § 12
- warunki NATO DIANA (siedziba w państwie NATO) [W] — § 11
- warunki: pełne pokrycie, próg 25%, celowy kapitał rezerwowy — § 14
- wpis po wpisie spółki) [Z] — § 5
- wspólna kadencja — § 21
- współpraca z podmiotami spoza UE i państw stowarzyszonych albo przez nie kontrolowanymi jest dopuszczalna, gdy nie jest sprzeczna z interesami bezpieczeństwa Unii, bez nieuprawnionego dostępu do informacji niejawnych i bez kwalifikowalności kosztów (art. 9 ust. 6) — § 33
- wybór uchwałą akcjonariuszy, „przy zawiązaniu spółki wyboru dokonują akcjonariusze”) [Z] — § 5
- wygaśnięcie mandatu z dniem odbycia WZ zatwierdzającego sprawozdanie za ostatni rok kadencji — każdorazowo „chyba że umowa spółki stanowi inaczej”) [Z] — § 21
- wykaz zawiera kategorie WT I–XIV, nie ma kategorii WT XXI/XXII [Z] — § 4, § 11
- wymaganej wyłącznie umową — ważność, odpowiedzialność wobec spółki) [Z] — § 23
- wymogi „jedynie” niezbędne do identyfikacji i bezpieczeństwa — § 24
- wypowiedzenie przez podmiot z ważnych powodów, nie krócej niż 3 miesiące) [Z] — § 5
- wysyłka co najmniej dwa tygodnie przed WZ) [Z] — § 24
- wytyczne Komisji w sprawie transferu technologii (2026) [W] — § 33
- zajęcie ujawniane w rejestrze akcjonariuszy) [Z] — § 12
- zakaz udostępniania) [Z] (tekst EN, pierwotny, bez konsolidacji) — § 12
- zakaz zwolnienia — § 30
- załącznik I zmieniany po 2023 r.) — § 28
- załącznik zmieniany po tej dacie): uwaga ogólna do technologii (GTN), uwaga ogólna do oprogramowania (GSN), definicje „technologii”, „wymaganej”, „rozwoju”, „informacji powszechnie dostępnych” i „podstawowych badań naukowych” — Zał. 3
- zgoda wszystkich akcjonariuszy, których dotyczy uchwała zwiększająca świadczenia lub uszczuplająca prawa indywidualne — § 38
- zmianę w toku działania zgłasza się Komisji (art. 9 ust. 7) — § 33
- § 11 ust. 1 i 6 — § 31
- § 11 ust. 14, § 32 ust. 1 — § 9
- § 11 ust. 5–6, § 12 ust. 7, § 14 ust. 1 — § 13
- § 12 ust. 2 lit. e — § 12
- § 19 ust. 7 — § 35
- § 2 kworum „co najmniej połowa jej członków”, umowa „może przewidywać surowsze wymagania dotyczące kworum” — § 21
- § 23 ust. 1 lit. d), f), k), § 25 ust. 1 lit. f), n), § 31 ust. 4–5 — § 33
- § 25 ust. 1 lit. a — § 4
- § 25 ust. 1 lit. j — § 14
- § 28 ust. 2 i § 23 ust. 1 lit. h — Zał. 3
- § 29 ust. 1–2, § 33 ust. 5–7, umowa wykonawcza (shareholder_agreement.tex — zakaz po odejściu z tym samym wyjątkiem) — § 33
- § 3 głosujący na piśmie albo na odległość liczeni do kworum, „chyba że umowa spółki lub regulamin organu stanowią inaczej” — § 21
- § 4 większość i głos rozstrzygający — § 21
- § 5 protokół) [Z] — § 21
- „Jeżeli umowa spółki nie stanowi inaczej, zgody udziela organ uprawniony do powoływania członka organu”) [Z] — § 33
- „Szczegółowe zasady dotyczące sposobu uczestnictwa w walnym zgromadzeniu przy wykorzystaniu środków komunikacji elektronicznej określa regulamin walnego zgromadzenia”) [Z] — § 24
- „chyba że umowa spółki przewiduje surowsze warunki”) [Z] — § 25

**Inne rozporządzenia**

- art. 1 lit. e–g, art. 2 ust. 1–2, art. 4–7 i art. 9 rozporządzenia Rady (UE) nr 269/2014 [Z] (tekst EN, pierwotny, bez konsolidacji) — § 11
- art. 1 lit. f–g i art. 2 ust. 1–2 rozporządzenia (UE) nr 269/2014 (zamrożenie środków obejmujące „stocks and shares” — § 12
- art. 10: okres przejściowy 1.05.2026–30.04.2027 r. tylko dla umów obowiązujących 30.04.2026 r. i spełniających warunki rozporządzenia 316/2014 — § 33
- art. 2 pkt 6 i 24, art. 5 i art. 9 ust. 1–4 i 7 rozporządzenia (UE) 2021/697 [Z] — § 11, § 12, § 16, § 21, § 32
- art. 3 ust. 1, art. 4 ust. 1–2 i art. 11 ust. 1 rozporządzenia [Z] (tekst EN) — Zał. 3
- art. 61 rozporządzenia finansowego (UE) 2018/1046 i zasada konkurencyjności w programach dotacyjnych [W] — § 30
- art. 9 ust. 7 rozporządzenia 2021/697 [Z] — § 11
- odpowiednie stosowanie środków z art. 2 rozporządzenia 269/2014 — zamrożenie i zakaz udostępniania środków — oraz z art. 9 — zakaz udziału w obchodzeniu tych środków) [Z] — § 12
- podmiot kontrolowany kwalifikuje się tylko na podstawie gwarancji zatwierdzonych przez państwo siedziby, które według ust. 4 lit. c muszą m.in. zapewniać, że odbiorca pozostanie właścicielem praw własności intelektualnej i rezultatów działania, a te nie będą podlegać kontroli ani ograniczeniu ze strony takiego państwa lub podmiotu ani nie zostaną wyeksportowane poza Unię i państwa stowarzyszone bez zgody państwa siedziby), art. 2 pkt 6 i 24, art. 5, art. 20 ust. 3–4 i 9, art. 23 ust. 2–4 rozporządzenia (UE) 2021/697 [Z] — § 31
- rozporządzenia sankcyjne UE (m.in. 833/2014, 269/2014) [W] — § 28
- to, które państwa EFTA/EOG faktycznie uczestniczą w Funduszu, nie wynika z tekstu rozporządzenia [W] — § 33

**Inne ustawy**

- art. 1 ust. 1 pkt 1 lit. k i ust. 3 pkt 2, art. 1a pkt 2, art. 6 ust. 1 pkt 8 i art. 7 ust. 1 pkt 9 ustawy o PCC [Z] — § 7
- art. 11 ust. 1–2 ustawy o zwalczaniu nieuczciwej konkurencji (tajemnica przedsiębiorstwa) [Z] — § 33
- art. 11 ust. 1–2 ustawy o zwalczaniu nieuczciwej konkurencji [Z] — § 26
- art. 12a ust. 1 pkt 1, art. 12c ust. 1 pkt 1 i 5, ust. 4–5 oraz art. 12d ust. 3 pkt 7 i ust. 4 ustawy o kontroli niektórych inwestycji [Z] — § 11, § 12, § 16, § 21, § 32
- art. 12f ust. 1 i 5 oraz art. 12h ust. 5 i 8 ustawy o kontroli niektórych inwestycji (uprzednie zawiadomienie nabywcy — § 12
- art. 16 pkt 3 (art. 83a ust. 4ac ustawy o obrocie instrumentami finansowymi) [Z] — § 5, § 24
- art. 19 ust. 1 ustawy o KRS [Z] — Zał. 1
- art. 23 ust. 1 ustawy o KRS (zakres kognicji sądu rejestrowego) [Z] — § 12
- art. 28 ust. 6 ustawy o rachunkowości (definicja wartości godziwej) [Z] — § 19
- art. 3 ust. 1 pkt 1, art. 12c ust. 6 i art. 12e ust. 4 ustawy o kontroli niektórych inwestycji (podmiot dominujący, nabycie pośrednie, spółki zależne podmiotów z państw trzecich) [Z] — § 11
- art. 36 ust. 1 i 2aa ustawy o rachunkowości [Z] — § 7
- art. 4 pkt 1 i art. 7 ust. 1 pkt 1 lit. b ustawy o PCC [Z] — § 10, inne
- art. 4 ust. 1 pkt 7 ustawy o kontroli niektórych inwestycji (wytwarzanie i obrót wyrobami i technologią o przeznaczeniu wojskowym jako działalność, dla której podmiot „może być uznany za podmiot objęty ochroną” rozporządzeniem Rady Ministrów) [Z] — § 33
- art. 40 pkt 1 ustawy o KRS („nie więcej niż dziesięć pozycji, w tym jeden przedmiot przeważającej działalności na poziomie podklasy”) [Z] — § 4
- art. 40 pkt 1 ustawy o KRS [Z] — § 30, § 38
- art. 5 (art. 10 ust. 4a pkt 4, art. 25da i art. 38 pkt 8a lit. j ustawy o KRS) [Z] — § 5, § 24
- art. 52 ust. 1 i art. 55 ust. 1 ustawy o kosztach sądowych w sprawach cywilnych (500 zł za wpis — § 30, § 38
- art. 54 ust. 1–2 ustawy o ochronie informacji niejawnych (warunkiem dostępu przedsiębiorcy do informacji niejawnych „poufne” lub wyższych jest świadectwo bezpieczeństwa przemysłowego wydawane przez ABW albo SKW) [Z] — § 33
- art. 55 ust. 1 ustawy o kosztach sądowych w sprawach cywilnych (250 zł od wniosku o zmianę wpisu) [Z] — § 4
- art. 55 ust. 1 ustawy o kosztach sądowych w sprawach cywilnych [Z] — § 5, § 24
- art. 6 ustawy o ochronie konkurencji i konsumentów [W] — § 33
- art. 60 ust. 1 pkt 1 ustawy o przeciwdziałaniu praniu pieniędzy (CRBR: 14 dni od wpisu) [Z] — § 30, § 38
- art. 7 ustawy o zastawie rejestrowym i rejestrze zastawów [W] — § 31
- art. 7, art. 19 ust. 2 i 5–6, art. 19a ust. 5, 5a i 5d, art. 20a ust. 1 i 3, art. 23 ust. 1 ustawy o KRS [Z] — § 30, § 38
- art. 87 ust. 1 pkt 5–6 ustawy o ofercie publicznej (definicja działania w porozumieniu, jako wzorzec redakcyjny) [W] — § 11
- art. 9 ust. 1–3, art. 12 ust. 1, art. 14 ust. 1, art. 16, art. 41 ust. 2–4, art. 46, art. 50, art. 53, art. 74 ust. 1, 3 i 4 ustawy o prawie autorskim i prawach pokrewnych [Z] — § 26
- art. 9 ust. 4 ustawy o KRS (tekst jednolity umowy) [Z] — § 38
- ustawa Prawo lotnicze (t.j. Dz.U. 2025 poz. 1431): art. 1 ust. 3–4, art. 2 pkt 1a, 1b, 2 i 24–26, dział VIa (art. 156a i n.), art. 156b ust. 3 [Z] — § 4, § 11
- ustawa o PCC: art. 1 ust. 1 pkt 1 lit. k, art. 1a pkt 1–2, art. 6 ust. 1 pkt 8 lit. a, art. 7 ust. 1 pkt 9 [Z] — § 30, § 38
- ustawa o funduszach inwestycyjnych i zarządzaniu AFI (ZASI, rejestr KNF) [W] — § 11
- ustawa o kontroli niektórych inwestycji [W] — § 12, § 16, § 32
- ustawa o ochronie baz danych [W] — § 26
- ustawa z 13 czerwca 2019 r. (Dz.U. 2019 poz. 1214 — § 4, § 11
- ustawa z 13 kwietnia 2022 r. o szczególnych rozwiązaniach w zakresie przeciwdziałania wspieraniu agresji na Ukrainę oraz służących ochronie bezpieczeństwa narodowego (t.j. Dz.U. 2025 poz. 514) [Z] — § 28
- ustawa z 13.06.2019 r. o wykonywaniu działalności gospodarczej w zakresie wytwarzania i obrotu materiałami wybuchowymi, bronią, amunicją oraz wyrobami i technologią o przeznaczeniu wojskowym lub policyjnym (art. 7 ust. 1 pkt 2: „obrotu technologią o przeznaczeniu wojskowym lub policyjnym — wymaga uzyskania koncesji” — § 33
- ustawa z 23 stycznia 2026 r. o zmianie ustawy — Kodeks spółek handlowych oraz niektórych innych ustaw (Dz.U. 2026 poz. 176, ogłoszona 17 lutego 2026 r.) [Z] — § 5, § 24
- ustawa z 27 maja 2004 r. o funduszach inwestycyjnych i zarządzaniu alternatywnymi funduszami inwestycyjnymi (ASI, ZASI) [W] — § 11
- ustawa z 29 listopada 2000 r. o obrocie z zagranicą towarami, technologiami i usługami o znaczeniu strategicznym dla bezpieczeństwa państwa, a także dla utrzymania międzynarodowego pokoju i bezpieczeństwa (t.j. Dz.U. 2023 poz. 1582, zm. Dz.U. 2026 poz. 471): art. 2, art. 3 pkt 10, art. 6, art. 9 ust. 2 pkt 11, art. 11, art. 17a, art. 24a, art. 33 ust. 1 i 2a [Z] — § 28
- ustawa z 29 listopada 2000 r. o obrocie z zagranicą towarami, technologiami i usługami o znaczeniu strategicznym: art. 3 pkt 10, art. 6, art. 33 ust. 1 [Z] — § 4, § 11
- ustawa z 29 listopada 2000 r.: art. 3 pkt 10 (organem kontroli obrotu jest minister właściwy do spraw gospodarki), art. 10 ust. 1 (wiążące wyjaśnienie w sprawie konieczności uzyskania zezwolenia), art. 11 (wewnętrzny system kontroli przy uzbrojeniu), art. 17a ust. 1 pkt 2 (rozstrzyganie o konieczności zezwolenia w przypadkach catch-all) [Z] — Zał. 3

## 6. Orzecznictwo powołane w memorandum

Sygnatury pochodzą z wiedzy ogólnej; teksty orzeczeń nie zostały pobrane (`src/legal/todo.md`, sekcja b), więc każde powołanie wymaga sprawdzenia przez prawnika w bazie orzeczeń SN.

### II CSKP 593/22

Powołane w odpowiedziach: 1.1.4, 1.5.3, 3.3.1.

> 1047 KPC [Z]; SN II CSKP 593/22 [Z].

> 300³⁷ § 1 KSH [Z]; SN V CSK 522/18 i II CSKP 593/22 [Z] (tezy według psa_feedback.

> 64 KC sam obowiązku nie kreuje (SN II CSKP 593/22): § 10 plus uchwała o stwierdzeniu Odejścia i uchwała o wskazaniu nabywcy z ceną taki obowiązek oznaczają.

### III CSKP 65/21

Powołane w odpowiedziach: 1.7.1.

> 300³⁷–300³⁸ KSH [Z]; SN III CZP 109/22, III CSKP 65/21, III CZP 32/16 [Z] (tezy według psa_feedback.

> tex: akcje nabyte ze środków wspólnych mogą należeć do majątku wspólnego (III CZP 32/16 — do udziałów, stosowane analogicznie), lecz akcjonariuszem jest małżonek, który je objął i jest wpisany do rejestru (III CSKP 65/21), a ustanowienie rozdzielności nie daje drugiemu małżonkowi praw korporacyjnych (III CZP 109/22).

### III CZP 109/22

Powołane w odpowiedziach: 1.7.1.

> 300³⁷–300³⁸ KSH [Z]; SN III CZP 109/22, III CSKP 65/21, III CZP 32/16 [Z] (tezy według psa_feedback.

> tex: akcje nabyte ze środków wspólnych mogą należeć do majątku wspólnego (III CZP 32/16 — do udziałów, stosowane analogicznie), lecz akcjonariuszem jest małżonek, który je objął i jest wpisany do rejestru (III CSKP 65/21), a ustanowienie rozdzielności nie daje drugiemu małżonkowi praw korporacyjnych (III CZP 109/22).

### III CZP 32/16

Powołane w odpowiedziach: 1.7.1.

> 300³⁷–300³⁸ KSH [Z]; SN III CZP 109/22, III CSKP 65/21, III CZP 32/16 [Z] (tezy według psa_feedback.

> tex: akcje nabyte ze środków wspólnych mogą należeć do majątku wspólnego (III CZP 32/16 — do udziałów, stosowane analogicznie), lecz akcjonariuszem jest małżonek, który je objął i jest wpisany do rejestru (III CSKP 65/21), a ustanowienie rozdzielności nie daje drugiemu małżonkowi praw korporacyjnych (III CZP 109/22).

### V CSK 522/18

Powołane w odpowiedziach: 1.5.3, 3.3.1.

> 300³⁷ § 1 KSH [Z]; SN V CSK 522/18 i II CSKP 593/22 [Z] (tezy według psa_feedback.

> 101 § 1–2 KC; SN V CSK 522/18); umowa wspólników i § 10 taki stosunek tworzą.

> , V CSK 522/18 [Z].


## 7. Co sprawdzić przed podpisaniem

- Wszystkie założenia z sekcji 2 — to decyzje Założycieli, nie prawnika.
- Fragmenty zredagowane przy wdrożeniu samodzielnie (memorandum dawało tylko kierunek, bez gotowego brzmienia) — wymienione w sekcji 8.
- Przepisy oznaczone [W] i [?] oraz orzecznictwo z sekcji 6.
- Załącznik nr 3 memorandum: lista aktów, których tekstu nie udało się pobrać (TFUE, część aktów UE w wersji polskiej, orzeczenia SN).
- Ujednolicenie z umową akcjonariuszy (`shareholder_agreement.tex`) i dokumentami w `extra.tex`.

## 8. Fragmenty redagowane samodzielnie

- § 11 ust. 14 (uwaga 24) — baza z odpowiedzi 1.4.3 (D3), uzupełniona o elementy brzmienia I z 4.4.2.
- § 11 ust. 16 (uwaga 26) — obowiązek koncesyjny akcjonariusza z pakietem od 20%; memorandum mówi tylko „rozważyć”.
- § 12 ust. 2 lit. e (uwaga 30) — kto składa zawiadomienie do organu kontroli inwestycji i kiedy ustaje wstrzymanie; na podstawie Rekomendacji 1.1.2.
- § 12 ust. 4 (uwaga 33) — derogacja art. 300³⁹ § 3–5 KSH dla odmowy z lit. f.
- § 14 ust. 6 (uwaga 43) — wyłączenie prawa pierwszeństwa przy przeniesieniu do podmiotu kontrolowanego; wtrącenie „także po upływie Okresu Ograniczenia Zbywania Akcji”.
- § 17 ust. 4 zd. 2 (uwaga 53) — skrócone do „Kolejne raty są płatne w równych odstępach miesięcznych.”, bo stare zdanie kolidowało z nowym zdaniem pierwszym.
- § 17 ust. 2 i § 19 ust. 2 (uwagi 51, 56) — tekst z części „Kierunek” memorandum; miejsce wstawienia wybrane przy wdrożeniu.
- § 16 ust. 5 i § 19 ust. 4 — znaczniki memorandum zamienione na pola do uzupełnienia: [48] miesięcy, [instytucja neutralna].
- **§ 21 ust. 3 (uwagi 59, 60, 62) — do decyzji:** ogólny wyjątek dla dyrektora spoza Kryterium (1.1.5) zastąpiono węższym brzmieniem V z 4.4.2 (jeden dyrektor niewykonawczy wskazany przez Kwalifikowanego Inwestora Finansowego), żeby nie obowiązywały dwa sprzeczne wyjątki.
- § 29 ust. 7 zd. 2 (uwaga 64) — odesłanie do definicji pełnego składu (§ 21 ust. 9); dyrektora wyłączonego nie wlicza się do quorum.
- § 24 ust. 2 i ust. 7 (uwagi 68, 69) — miejsce wstawienia zdań z 4.3.3 wybrane przy wdrożeniu.
- § 25 ust. 1 lit. f (uwaga 72) — rozszerzenie o wydzierżawienie przedsiębiorstwa i ograniczone prawo rzeczowe; opcjonalne obniżenie większości dla lit. i pominięte.
- § 32 (uwaga 71) — znacznik [5] zamieniony na pole do uzupełnienia.
- Załącznik nr 3 pkt 4 (uwaga 77) — zakres danych klasyfikacji eksportowej.
- Umowa wykonawcza (uwagi 10, 11, 13, 14, 17, 66) — dostosowania w `shareholder_agreement.tex`: limit 24 miesięcy przekwalifikowania Odejścia, ograniczenie kar umownych wobec założyciela-pracownika, wyłączenie nabywcy zależnego od Spółki, odesłania do definicji, warstwa kontroli UE/EOG (D6), poprawione odesłania po usunięciu przekreśleń.
- § 30 ust. 2 i 5 (uwaga 81) — próg 500 000 zł i lit. d (nabycie mienia od Założyciela w ciągu 2 lat) przyjęte z brzmienia memorandum; wysokość progu to decyzja Założycieli.
- § 31 ust. 3 (uwaga 83) — bez odesłania do Kryterium EU/NATO (memorandum zostawia to Założycielom); odesłanie byłoby bezpieczniejsze dla EDF, ale ograniczyłoby finansowanie.
- § 32 ust. 4 (uwaga 86, K15) — istniejąca lit. f wkomponowana w nowe brzmienie, dodane odesłanie „(lit. f)” przy zgodzie serii.
- § 33 ust. 4 (uwaga 90) — zakres „państw zaufanych” z brzmienia memorandum (EU001 albo umowa o bezpieczeństwie informacji z UE lub NATO); Ukraina nie jest wymieniona wprost — decyzja Założycieli.
- § 38 ust. 2 i 5 (uwagi 94, 95) — brzmienia memorandum dla dawnych ust. 3 i 6 wstawione do obecnych ust. 2 i 5 (numeracja po usunięciu przekreśleń); bez indywidualnych praw weta Założycieli.
- Załącznik nr 1 (uwaga 98, K13) — tabela zbiorcza i wiersze dla Założycieli A–E; numery akcji, kwoty, wartości i podstawy wyceny pozostały polami; termin wkładu pieniężnego: „przed zgłoszeniem Spółki do rejestru”.
- Umowa wykonawcza § 13 ust. 6–7 (uwaga 85) — kara umowna (kwota jako pole) i nieodwołalne pełnomocnictwo do głosowania w sprawach Kwalifikowanej Rundy: udzielane w 7 dni od uchwały kierunkowej, ograniczone do jej treści, pełnomocnika wskazuje Rada i nie może nim być inwestor Rundy.
- Umowa wykonawcza § 10 ust. 4 i § 12 (uwaga 91) — od Dnia Odejścia tylko pasywne posiadanie udziału w Przedsięwzięciu Produkcyjnym do czasu zbycia; aktualizacje Załącznika nr 3 zatwierdza Rada Dyrektorów albo Walne Zgromadzenie.

## 9. Zmiany spoza memorandum (na wniosek Założycieli)

### § 5 ust. 7–8 — nabycie akcji własnych przez Spółkę

Commit `c531141` · wzory uchwał: `uchwaly.tex`, Część 1 (commit `cbb8101`) · pytanie do prawnika: `law_uzup.md` U.6 (commit `2139566`)

- **Co:** Walne Zgromadzenie może upoważnić Radę Dyrektorów do nabywania akcji własnych na okres do 5 lat. Uchwała określa: liczbę akcji (łącznie najwyżej 25%), cele (prawo pierwszeństwa z § 14 ust. 3, akcje spadkobiercy z § 17, program motywacyjny z § 8, umorzenie), widełki ceny (najwyżej Wartość Godziwa z § 19), kapitał rezerwowy na ten cel i sposób rozporządzenia akcjami. Nabywać można tylko akcje w pełni pokryte, za cenę mieszczącą się w kapitale rezerwowym i bez utraty płynności na 6 miesięcy. Poza § 14 i § 17 oferta idzie do wszystkich akcjonariuszy na jednakowych warunkach. Dyrektor-zbywca nie głosuje w Radzie. Nie trzeba odrębnej uchwały z § 30. Spółka nie wykonuje praw z akcji własnych, a zbyć je może tylko Dopuszczalnemu Nabywcy spełniającemu Kryterium.
- **Dlaczego:** przed tą zmianą umowa dopuszczała nabycie akcji własnych tylko pośrednio (§ 14 ust. 3, § 17 ust. 2–2a) i zostawiała je w całości ustawie. Założyciele chcieli mieć jasną, z góry określoną ścieżkę odkupu, kiedy Spółka będzie miała zyski. Postanowienie przenosi do umowy warunki z KSH i dokłada zabezpieczenia własne: limit ceny, równe traktowanie, Kryterium przy dalszym zbyciu.
- **Podstawa prawna:** art. 300⁴⁷ § 1 pkt 1–2, § 2, § 3, § 6–9 KSH [Z]; art. 300¹⁵ § 2 i § 4–6 KSH (źródła wypłaty, test wypłacalności) [Z]; art. 300⁴⁴ § 1–2 i § 4 KSH (umorzenie jako zmiana umowy, spłata ze środków z art. 300¹⁵ § 2) [Z]; art. 20 KSH (jednakowe traktowanie akcjonariuszy) [W].
- **Powiązania:** § 10 ust. 11–12 (zwrotne zbycie nie jest nabyciem akcji własnych), § 25 ust. 1 (uchwała 75%), § 32 ust. 4 lit. f (po rundzie może być potrzebna zgoda serii inwestorskiej).
- **Do decyzji i weryfikacji:** pytania U.6 w `law_uzup.md` i „Pytania do prawnika” w `uchwaly.tex`.

