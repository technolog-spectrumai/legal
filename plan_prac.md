# Plan prac: przegląd, memorandum i wdrożenie projektu umowy P.S.A. Basilisk Systems

Gałąź: `psa_check`. Repozytorium: `technolog-spectrumai/legal`. Data planu: 30 września 2026 r.

## Kontekst

Repozytorium zawiera projekt umowy prostej spółki akcyjnej w wersji 0.9.4-C (wariant hybrydowy, „bramka miękka” przy odmowie zgody z powodu Kryterium EU/NATO) oraz komplet materiałów roboczych Założycieli:

| Plik | Rola |
|---|---|
| `psa.tex` | projekt umowy: 38 §, Załączniki nr 1–3, 58 pól `\field{}`, 9 fragmentów przekreślonych (`\BoilerplateStrike`) |
| `law.md` | 79 pytań szczegółowych do kancelarii w numeracji 1.1.1–4.4.2, z odesłaniami do § i ust. |
| `email.md`, `mail.md` | zapytanie o wycenę z zakresami A–E i mail wysyłkowy |
| `spis_tresci.md` | mapa § → tytuł → strona → liczba ustępów (numeracja zgodna z `psa.tex`) |
| `psa_feedback.tex` | Część 1: rozstrzygnięte wątpliwości; Część 2: audyt § po § wersji 0.8; Część 3: pusty wpis R1 na opinię kancelarii |
| `shareholder_agreement.tex` | projekt umowy wspólników połączony z umową wykonawczą zwrotnego zbycia (Załączniki A–C: oferta, pełnomocnictwo, przystąpienie) |
| `extra.tex` | 6 dokumentów informacyjnych (prawa akcjonariusza, checklista emisji, proces decyzyjny, Akcjonariusz Funkcjonalny, mapa rundy, punkty podatkowe) |
| `regulations.md` | mapa reżimów regulacyjnych, bramki G0–G6, wymogi programów EDF/DIANA/EIC |
| `emisja/*.md` | strategie emisji serii F, P i inwestorskiej |
| `psa_todo.md`, `zmiany.md` | lista odłożonych zadań i historia zmian 0.8 → 0.9.3 |
| `build.sh`, `basilisk_i18n.sty` | budowa PDF (pdflatex ×2, `psa.tex` zawsze pierwszy, bo dostarcza `psa.aux` dla `xr-hyper`) |

Lista 27 punktów użytkownika to rozwinięcie zakresów A–E z `email.md`: punkty 1–15 to memorandum (zakresy A–D), 16–20 wariant z wdrożeniem, 21–27 dokumenty po odrębnym zleceniu (zakres E). Zadanie polega na zaplanowaniu i wykonaniu tych prac w repozytorium, tak aby każdy punkt miał deliverable w postaci pliku, a decyzje Założycieli były jawnymi bramkami między etapami.

## Założenia i ograniczenia

1. **Rola.** Prace wykonujemy w roli recenzenta („kancelarii”). Memorandum jest dokumentem roboczym do weryfikacji przez radcę prawnego lub adwokata przed podpisaniem umowy; każda odpowiedź niesie oznaczenie wiarygodności źródła w konwencji z `regulations.md`: **[Z]** sprawdzone w akcie prawnym (link ELI/EUR-Lex), **[W]** wiedza ogólna do potwierdzenia, **[?]** hipoteza.
2. **Stan prawny.** Na dzień memorandum; akty do sprawdzenia w źródłach urzędowych (WebFetch/WebSearch): KSH t.j. Dz.U. 2024 poz. 18 ze zm., nowelizacja z 23.01.2026 (Dz.U. 2026 poz. 176, wejście w życie 18.02.2027), ustawa z 13.03.2026 (Dz.U. 2026 poz. 471), ustawa o kontroli niektórych inwestycji, rozporządzenie PKD 2025 (Dz.U. 2024 poz. 1936), ustawa o prawie autorskim (art. 41, 53, 64), Prawo własności przemysłowej (art. 67, 72), ustawa o PIT (art. 17 ust. 1 pkt 9, art. 24 ust. 11–12b), rozporządzenie (UE) 2019/452, art. 49, 63 i 346 TFUE. Repozytorium nie zawiera adresu ani treści dla: ustawy o KRS (wezwanie, termin 7 dni, załączniki do wniosku o wpis P.S.A. poza S24), ustawy o obrocie instrumentami finansowymi (podmioty uprawnione do prowadzenia rejestru akcjonariuszy), ustawy AML i CRBR (beneficjent rzeczywisty a § 11 ust. 6 lit. b), ustawy sankcyjnej z 13.04.2022 r. (tryb zawieszenia praw z akcji), nowego rozporządzenia o transferze technologii po wygaśnięciu 316/2014 z dniem 30.04.2026 r. (licencja z § 33 ust. 3), załącznika I do rozporządzenia 2021/821 (pozycje 9A012, 9D/9E, 5A002), art. 9 rozporządzenia 2021/697 (EDF), art. 21 i 64 Konstytucji (pytanie 1.6.2) oraz ustawy o rachunkowości (wkłady poza kapitałem). Jeżeli sieć nie pozwoli sprawdzić aktu, odpowiedź dostaje **[W]** i trafia na listę do weryfikacji.
3. **Numeracja.** Odpowiedzi w numeracji `law.md`; paragrafy według `spis_tresci.md` (§ 1 firma … § 38 postanowienia końcowe). W plikach `.tex` używamy `\ref{art:...}` przez `xr-hyper`, więc numery aktualizują się same po zmianach.
4. **Narzędzia.** W środowisku, w którym prowadzone są prace, nie ma `pdflatex`, `latexdiff` ani `pandoc`. Weryfikacja: bilans nawiasów i środowisk, kontrola, że każdy `\ref{art:...}` wskazuje istniejący `\label`, oraz przegląd tekstu; kompilację PDF wykonuje użytkownik przez `./build.sh`.
5. **Bramki.** Etap B zaczyna się po decyzjach Założycieli (wariant A/B, wyjątek dla funduszy, przekreślenia, Kryterium wobec spadkobierców, PKD przeważające, dane do Załączników). Etap C po odrębnym zleceniu. Punkty wymagające osób trzecich (18 notariusz, 27 doradca podatkowy, 15 pytania Założycieli) przygotowujemy jako gotowe pakiety do przekazania i miejsce na wpisanie odpowiedzi.
6. **Konwencje.** Dokumenty formalne w LaTeX w stylu `basilisk_i18n.sty` z `\externaldocument{psa}`; notatki robocze w Markdown. Jeden commit na jedną zmianę merytoryczną (konwencja z `zmiany.md`). Nie tworzymy PR-a. Push na `psa_check`. Plików już wysłanych kancelarii (`law.md`, `email.md`, `mail.md`) nie edytujemy; nowe pytania i konkordancje idą do nowych plików.
7. **Wariant B istnieje tylko jako tekst.** Gałęzie `psa_hard`, `psa_soft`, `psa_vs`, `psa_prod` z `psa_todo.md` nie istnieją w tym klonie ani na `origin`; brzmienie wariantu B jest w `law.md` 1.2 i `psa_feedback.tex` Część 1 pkt 1 i tam je oceniamy. Nie odtwarzamy gałęzi; jeżeli Założyciele wybiorą B, wdrażamy go commitami na `psa_check`.
8. **Dwie skale ocen.** `law.md` prosi o ocenę stanu (zgodne / zgodne warunkowo / ryzyko), a zakres pkt 6 o priorytet zmiany (konieczne / zalecane / opcjonalne). Reguła: „ryzyko” → konieczne; „zgodne warunkowo” → zalecane, chyba że warunek spełnia się poza umową (wtedy opcjonalne albo bez zmiany); „zgodne” → bez zmiany albo opcjonalne, gdy proponujemy ulepszenie. Odstępstwa od reguły uzasadniamy przy odpowiedzi.

## Mapowanie zakresu na deliverables

| Pkt | Deliverable | Plik | Etap |
|---|---|---|---|
| 1–7, 12–14 | memorandum z odpowiedziami 1.1.1–4.4.2, sekcjami tematycznymi, klasyfikacją i brzmieniami | `memorandum.tex` | A |
| 8 | ścieżka zawiązania poza S24 i lista dokumentów do KRS | `memorandum.tex` sekcja T3 + `krs/dokumenty_krs.md` | A (lista), B (wzory) |
| 9 | wymogi dokumentacji wkładów i przeniesienia praw | `memorandum.tex` sekcja T4 + `krs/wklady_checklista.md` | A |
| 10 | kryteria wyboru podmiotu prowadzącego rejestr akcjonariuszy | `memorandum.tex` sekcja T5 + `krs/rejestr_akcjonariuszy.md` (tabela kryteriów i pytań do oferentów) | A |
| 11 | weryfikacja PKD i ryzyka zastrzeżeń sądu | `memorandum.tex` sekcja T6 | A |
| 13 | tabela: umowa spółki / umowa akcjonariuszy / oba | `memorandum.tex` sekcja T8 | A |
| 15 | runda odpowiedzi uzupełniających | `law_uzup.md` (pytania Założycieli) + `memorandum_uzupelnienie.tex` | A9 |
| 16 | naniesienie uzgodnionych zmian | `psa.tex` (wersja 1.0-RC) + wpis w `zmiany.md` | B |
| 17 | wersja czysta i z zaznaczonymi zmianami | `psa.tex` (czysta) + `psa_zmiany.tex` (oznaczona makrami rewizyjnymi z commitu `5194627`) | B |
| 18 | uzgodnienie z notariuszem | `krs/notariusz.md` (brief, pytania, lista niestandardowych postanowień, miejsce na ustalenia) | B |
| 19 | dokumenty do zawiązania i KRS | `krs/` (wzory oświadczeń, list, zgód, uchwał założycielskich; instrukcja PRS) | B |
| 20 | odpowiedź na wezwanie sądu | `krs/odpowiedz_na_wezwanie.md` (szablon + gotowe uzasadnienia dla każdego niestandardowego postanowienia) | B |
| 21 | umowa wykonawcza zwrotnego zbycia | `umowa_wykonawcza.tex` (wydzielona z `shareholder_agreement.tex`, z ofertą i pełnomocnictwem) | C |
| 22 | regulamin Rady Dyrektorów | `regulamin_rady.tex` | C |
| 23 | regulamin programu motywacyjnego | `regulamin_programu.tex` | C |
| 24 | wzory uchwał Rady i WZ | `uchwaly.tex` (jeden plik, sekcja na wzór) | C |
| 25 | wzór umowy spółki celowej / JV | `umowa_spv.tex` | C |
| 26 | umowa akcjonariuszy | `shareholder_agreement.tex` (po wydzieleniu części wykonawczej) | C |
| 27 | wniosek o interpretację indywidualną | `interpretacja_pit.md` (projekt ORD-IN + lista pytań do doradcy) | C |

## Etap A — memorandum (pkt 1–15)

### A0. Przygotowanie (przed pisaniem)

- Zbudować tabelę „pytanie → § → ustęp → aktualne brzmienie” z `law.md` i `psa.tex`, aby każda odpowiedź cytowała obowiązujący tekst (audyt w `psa_feedback.tex` Część 2 odnosi się do wersji 0.8, więc nie kopiujemy z niego ocen bez sprawdzenia).
- Sprawdzić w źródłach urzędowych akty z założenia 2; wynik zapisać w `memorandum.tex` jako wykaz źródeł z datą sprawdzenia. Szczególnie: treść nowelizacji KSH z 23.01.2026 w zakresie P.S.A. (pkt 2 zakresu, pytanie 4.3.3) i zmiany ustawy koncesyjnej z 2019 r. wprowadzone ustawą z 13.03.2026 (pytanie 4.1.1, `regulations.md` 2.1 oznaczone [Z/?]).
- Ustalić szkielet `memorandum.tex`: preambuła jak w `psa_feedback.tex` (klasa `report`, `xr-hyper`, `basilisk_i18n`), strona tytułowa „Memorandum — wersja 1.0”, spis treści.

### A1–A6. Pakiety odpowiedzi (można prowadzić równolegle, po jednym subagencie na pakiet)

Każda odpowiedź ma stały format: **Ocena** (zgodne / zgodne warunkowo / ryzyko), **Podstawa prawna** (artykuł + link ELI, oznaczenie [Z]/[W]/[?]), **Uzasadnienie**, **Rekomendacja**, **Klasyfikacja** (konieczne / zalecane / opcjonalne), a dla „konieczne” **Proponowane brzmienie** w środowisku `quote` gotowe do wklejenia do `psa.tex`; dla „zalecane/opcjonalne” **Kierunek i konsekwencje** (co się zmienia dla Spółki, akcjonariuszy, inwestora, rejestru).

| Pakiet | Pytania `law.md` | Pkt zakresu | Kluczowe paragrafy `psa.tex` | Główne zagadnienia |
|---|---|---|---|---|
| A1 Kryterium i obrót | 1.1–1.4 | 1, 3, 5 | § 11, 12, 13, 14 | dopuszczalność Kryterium (art. 300³⁹, 300⁴¹ KSH; art. 49, 63 TFUE; ustawa o kontroli inwestycji), wariant A (ratalny, § 12 ust. 3) vs wariant B (wyłączający, brzmienie w `psa_feedback.tex` Część 1 pkt 1), granice „chyba że umowa stanowi inaczej” w art. 300³⁹ § 2, lock-up, skutek milczenia Rady, wstrzymanie terminu, przekreślony § 11 ust. 14 (fundusze), ujawnienie w rejestrze (art. 300³¹–300³⁴) |
| A2 Zwrotne zbycie i rozliczenia | 1.5–1.8 | 4 | § 10, 17, 18, 19, 36 | obowiązek związany z akcją, 80 % Wartości Godziwej a art. 300⁴⁵/300⁴⁷, oferta i pełnomocnictwo (art. 101, 108 KC), art. 64 KC i 1047 KPC, spłata spadkobierców z art. 300⁴¹ § 1 (usterka odesłania § 17 ust. 2 opisana w `zmiany.md` jest już poprawiona w 0.9.4-C: odsyła do ust. 4), małżonek (SN III CZP 109/22), wiążąca wycena eksperta |
| A3 Organy | 2.1–2.4 | 1, 3 | § 21–25, 29, 30, 33 | prorogacja mandatu, głos dyrektora ds. zgodności, fallback WZ a art. 300⁷⁵ § 2, WZ elektroniczne (art. 300⁸⁸, 300⁹²), e-mail z rejestru (art. 300⁸⁷), Głosy Uprawnione w Sprawie, § 30 oznaczony „[WYMAGA OPINII PRAWNIKA]” (art. 300¹⁵ i n.), licencja dla Przedsięwzięcia a TTBER |
| A4 Kapitał, emisje, runda | 3.1–3.4 | 1, 9, 12, 14 | § 5–9, 26, 31, 32, 38 | dokumentacja wkładów (art. 300², 300⁵, 300¹⁰), wkłady niepieniężne poza kapitałem, przeniesienie IP (pola eksploatacji, forma pisemna, cesja zgłoszeń patentowych), uchwała ramowa serii P (art. 300¹⁰³–300¹⁰⁷), zobowiązania do głosowania, uprzywilejowanie bez zmiany umowy, aktualizacja Załączników, brak klauzul zgody indywidualnej |
| A5 Zgodność i zawiązanie | 4.1–4.3 | 2, 8, 10, 11 | § 3, 4, 27, 28 | ustawa z 13.06.2019 po nowelizacji, PKD wojskowe przed koncesją, końcowa kontrola PKD 2025, forma zawiązania (akt notarialny, art. 300⁶), dokumenty do KRS przez PRS, ujawnienia w rejestrze, dobór podmiotu prowadzącego rejestr, nowelizacja KSH 2026 |
| A6 Inwestor VC | 4.4 | 12 | § 10–16, 25, 31, 32 | co budzi zastrzeżenia na seed/serii A, co negocjują fundusze, zmiany ułatwiające rundę bez naruszenia założeń |

### A7. Sekcje tematyczne (punkty zakresu bez wprost odpowiadającego pytania)

- **T1 Zmiany przepisów (pkt 2):** tabela akt → zmiana → wpływ na § umowy → wpływ na procedury Spółki (rejestr, WZ, emisje, kontrola eksportu, koncesje) → czy zmieniać umowę teraz, czy po 18.02.2027. Obejmuje nowelizację KSH z 23.01.2026, ustawę z 13.03.2026 (poz. 471) wraz ze zmianą ustawy koncesyjnej z 2019 r., PKD 2025, nowe rozporządzenie o transferze technologii, terminy AI Act, rozporządzenia maszynowego i CRA z `psa_todo.md` sekcja 5. Jeżeli zawiązanie może nastąpić po 18.02.2027, odpowiedzi dotknięte nowelizacją podajemy w dwóch stanach prawnych.
- **T1a Pytania odłożone przez Założycieli:** cztery zagadnienia z `psa_todo.md` sekcja 1 (koncesja przy licencji dla spółki celowej, wyłączenia B+R w ustawie z 2019 r., Kryterium a art. 9 EDF, klasyfikacja dual-use produktów cywilnych) omawiamy skrótowo już w memorandum, tam gdzie odpowiedź wynika z A5/T1, i oznaczamy jako materiał do rundy uzupełniającej; pytanie o jurysdykcję i strukturę holdingową tylko sygnalizujemy (decyzja D1 poniżej).
- **T2 Wykonalność mechanizmów (pkt 3):** dla każdego mechanizmu (zgoda Spółki, lock-up, zwrotne zbycie, drag-along, dziedziczenie, utrata Kryterium) trzy kolumny: rejestr akcjonariuszy (czy i jak ujawni, czy odmówi wpisu), sąd rejestrowy (ryzyko wezwania), spór między akcjonariuszami (droga: art. 64 KC, powództwo o ustalenie, zabezpieczenie).
- **T3 Ścieżka zawiązania poza S24 i lista dokumentów KRS (pkt 8).**
- **T4 Dokumentacja wkładów niepieniężnych i przeniesienia praw (pkt 9):** osobno kod (utwór, pola eksploatacji, protokół wydania, sumy kontrolne, licencje OSS), sprzęt (protokół, numery seryjne, dowody nabycia), zgłoszenia patentowe (cesja, wpis w UPRP/EPO, prawo do uzyskania patentu), wycena i odpowiedzialność z art. 300¹⁰.
- **T5 Kryteria wyboru podmiotu prowadzącego rejestr (pkt 10):** uprawnienie (art. 300³¹ § 2), obsługa ograniczeń i obowiązków związanych z akcją, wpisy warunkowe, API/e-głosowanie, koszty, umowa o prowadzenie rejestru, pytania do oferentów.
- **T6 PKD i ryzyka sądu (pkt 11):** kontrola 19 kodów wobec rozporządzenia PKD 2025, 10 do wpisu, przeważający 72.10.Z czy 30.31.Z, katalog postanowień z ryzykiem wezwania (Kryterium, derogacja art. 300³⁹ § 3–6, obowiązki związane z akcją, uchwała ramowa, mandat do 6 miesięcy, § 30) z oceną prawdopodobieństwa i gotową argumentacją.
- **T7 Oczekiwania VC (pkt 12):** rozwinięcie A6 w listę zmian „przed rundą” i „w rundzie”; punkt wyjścia: `vc.md` i `strategikon/vc/vc.md` (standard światowy, praktyka polska, fundusze zagraniczne i obronne, mapowanie na § umowy).
- **T8 Podział umowa spółki / umowa akcjonariuszy / oba (pkt 13):** tabela dla każdego mechanizmu z uzasadnieniem (skuteczność erga omnes vs elastyczność, jawność w KRS, forma aktu notarialnego, koszt zmian); uwzględnia trzy warunki z `regulations.md` 3a (kontrola spoza UE/EOG a EDF, dwóch dyrektorów z UE/EOG pod koncesję, checkpoint G2).
- **T9 Ryzyka podatkowe (pkt 14):** art. 24 ust. 11–12b PIT dla P.S.A., wyłączenie B2B, objęcie po 0,01 zł, aport IP (art. 17 ust. 1 pkt 9 PIT), wkłady poza kapitałem a PCC, pożyczki założycielskie, wkład w postaci pracy dla serii F; rekomendacja zakresu interpretacji indywidualnej (łącznik z pkt 27).

### A8. Synteza i kontrola

- **Podsumowanie wykonawcze** na początku memorandum: lista uwag koniecznych (z numerami § i brzmieniami), rekomendacja wariantu A/B z uzasadnieniem, stanowisko co do § 11 ust. 14 i pozostałych przekreśleń, decyzje wymagane od Założycieli.
- **Załącznik 1 memorandum:** zbiorcza tabela uwag (nr, §, klasa, treść, brzmienie lub kierunek).
- **Załącznik 2 memorandum:** lista decyzji Założycieli (wejście do bramki).
- **Załącznik 3 memorandum:** wykaz źródeł z datą sprawdzenia i oznaczeniami [Z]/[W]/[?] oraz lista rzeczy do weryfikacji przez uprawnionego prawnika.
- Kontrola spójności: każde z 79 pytań `law.md` ma odpowiedź w części numerowanej, niezależnie od tego, czy mapuje się na któryś z punktów 1–14 zakresu (ok. 25 pytań, m.in. 1.7, 2.1–2.4, 3.2.3, 3.3.4, 4.2, dotyczy wyłącznie ogólnej zgodności z pkt 1 i bez tej zasady wypadłoby z klasyfikacji); każdy `\ref{art:...}` istnieje w `psa.tex`; brzmienia nie kolidują ze sobą (np. wariant B zmienia § 11 ust. 5, § 12 ust. 3–4, § 13 ust. 1 łącznie).
- Dopisać `memorandum` do listy `docs` w `build.sh`; w `psa_feedback.tex` Część 3 wpis R1 z datą, zakresem i odesłaniem do `memorandum.tex` (pole „Stanowisko Założycieli” zostaje do uzupełnienia przez Założycieli); w `psa_todo.md` odhaczyć pozycje z sekcji 2 wykonane w tym etapie.

### Bramka A → B: decyzje Założycieli

Lista decyzji (Załącznik 2 memorandum) trafia do `psa_feedback.tex` Część 3 (R1, „Stanowisko Założycieli”). Zestaw:

| Nr | Decyzja | Warunek dla |
|---|---|---|
| D1 | jurysdykcja: P.S.A. w Polsce czy inna struktura (pytanie odłożone w `psa_todo.md` 1) | całego etapu B |
| D2 | wariant A (ratalny) czy B (wyłączający) | 16, 21 |
| D3 | § 11 ust. 14 (fundusze): usunąć czy przywrócić w nowym brzmieniu | 16 |
| D4 | usunięcie siedmiu przekreślonych zdań | 16 |
| D5 | Kryterium wobec spadkobierców i małżonków (ZMIANA 14): utrzymać czy wrócić do 0.9 | 16 |
| D6 | zawężenie „kontroli” do UE/EOG pod art. 9 EDF: w umowie spółki czy w umowie akcjonariuszy | 13, 26 |
| D7 | PKD przeważające 72.10.Z czy 30.31.Z; kody wojskowe przy wpisie czy po koncesji | 11, 19 |
| D8 | kto objęty mechanizmem zwrotnego zbycia (Załącznik nr 2) albo „brak” | 21 |
| D9 | progi Kwalifikowanej Rundy w § 32 ust. 1 | 16 |
| D10 | podmiot prowadzący rejestr (notariusz czy dom maklerski) | 19, forma pełnomocnictw |
| D11 | model programu motywacyjnego (obietnica i emisja po nabyciu uprawnień / emisja z góry / instrument gotówkowy; osoby B2B) | 23, 27 |
| D12 | czy umowa wykonawcza (21) i umowa akcjonariuszy (26) pozostają jednym dokumentem | etap C |
| D13 | data zawiązania i notariusz; przed czy po 18.02.2027 | 18, 19, T1 |
| D14–D15 | doradca podatkowy (27) i specjalista od klasyfikacji dual-use (4.2.2) | 27, T1 |
| D16 | które uwagi zalecane i opcjonalne wdrożyć; dane do Załączników nr 1–3 (wkłady, wartości, daty, role) | 16, 19 |

### A9. Runda pytań uzupełniających (pkt 15)

Pytania Założycieli trafiają do nowego pliku `law_uzup.md` (numeracja „U.1, U.2 …”, z odesłaniem do numeru pytania pierwotnego albo sekcji T), bo `law.md` jest zamrożony jako wysłany. Odpowiedzi: `memorandum_uzupelnienie.tex` w tej samej numeracji, z odesłaniem do zmienianych fragmentów memorandum; bez ponownego otwierania odpowiedzi, o które nie zapytano. Do czasu pytań oba pliki zawierają tylko szkielet i instrukcję; cztery pytania odłożone z `psa_todo.md` 1 wpisujemy do `law_uzup.md` od razu jako propozycję.

## Etap B — wdrożenie (pkt 16–20), po bramce

1. **B1 Naniesienie zmian (16).** Najpierw tabela konkordancji ustępów „stary → nowy” w `zmiany.md`, bo etykiety `art:*` przeżyją zmiany, ale numery ustępów nie (w `.tex` jest 58 twardych odesłań `ust.~N`, w `.md` ok. 200 zapisów „§ N ust. M”). Potem w `psa.tex` jedna zmiana = jeden commit, w kolejności: przekreślenia i znacznik „[WYMAGA OPINII PRAWNIKA]” w § 30 → decyzja A/B (§ 11 ust. 5, § 12 ust. 3–4, § 13 ust. 1) → uwagi konieczne → zalecane przyjęte → opcjonalne przyjęte → uzupełnienie pól `\field{}` danymi od Założycieli (Załączniki nr 1–3, § 32 ust. 1) → wersja „1.0-RC” na stronie tytułowej i w `\BusinessPlanVersionText`. Po każdym commicie: bilans `{}` i `\begin`/`\end`, kontrola `\ref`. Wpis w `zmiany.md` (nowa sekcja „0.9.4-C → 1.0-RC”, tabela commitów jak dla 0.9).
2. **B2 Wersja z zaznaczonymi zmianami (17).** `psa_zmiany.tex`: kopia `psa.tex` z makrami rewizyjnymi z commitu `5194627` (`\ZmianaKomentarz`, `\ZM`, `\NOWE`, bloki `Bylo` z dosłownym poprzednim brzmieniem) — bez `latexdiff` w kontenerze to jedyna powtarzalna metoda; dodać do `build.sh` (po `psa`). Czysta wersja to sam `psa.tex`.
3. **B3 Spójność dokumentów towarzyszących.** Według konkordancji z B1 zaktualizować: `spis_tresci.md` (liczby ustępów, pól, przekreśleń, nota że wersja wysłana kancelarii to 0.9.4-C), `shareholder_agreement.tex` (28 odesłań `ust.~N`, wersja), `extra.tex` (Dokument nr 1 pkt 3 i nr 5 przy wariancie B; progi w Dokumencie nr 3; uwaga o EDF w Dokumencie nr 5 z `psa_todo.md` 7), `emisja/*.md` (odesłania; sekcje „Otwarte punkty u kancelarii” zastąpić odpowiedziami), `regulations.md` (2.1, 2.9, sekcja 3 po D6, G0 po D7), `psa_feedback.tex` (Część 1 pkt 1 wariant przyjęty, czerwona uwaga do zamknięcia, nota o zakresie audytu w Części 2), `psa_todo.md`. `law.md` zostaje bez zmian.
4. **B4 Notariusz (18).** `krs/notariusz.md`: forma (akt notarialny, art. 300⁶ KSH), co notariusz sprawdzi (dane, PESEL, wkłady, reprezentacja, pełnomocnictwa do zawiązania, tłumaczenia), lista postanowień do omówienia (Kryterium, derogacje art. 300³⁹, obowiązki związane z akcją, uchwała ramowa, Załączniki jako część aktu), pytania o taksę i termin, miejsce na ustalenia i ich przeniesienie do `psa.tex` (kolejne commity B1).
5. **B5 Dokumenty do zawiązania i KRS (19).** Katalog `krs/`: `dokumenty_krs.md` (lista z podstawą prawną: umowa w formie aktu, oświadczenie dyrektorów o wniesieniu wkładów w wymaganej części, oświadczenie o wysokości kapitału akcyjnego, lista akcjonariuszy z liczbą akcji, dowody wpłat, zgody dyrektorów na powołanie i adresy do doręczeń, oświadczenie o adresie Spółki, umowa o prowadzenie rejestru akcjonariuszy albo oświadczenie o wyborze podmiotu, uchwała o powołaniu Rady, pełnomocnictwa, opłaty, PRS zamiast S24), wzory w `.tex` lub `.md` dla każdego dokumentu, instrukcja wniosku przez Portal Rejestrów Sądowych, czynności po wpisie (CRBR, NIP-8, VAT-R, dyspozycje wpisu akcji, protokoły wydania wkładów niepieniężnych w 14 dni z § 7 ust. 4). Dodatkowo dwa dokumenty, których lista 21–27 nie zawiera, a które muszą istnieć najpóźniej w dniu podpisania umowy (§ 7 ust. 4, § 26 ust. 4): `krs/przeniesienie_praw.tex` — wzory umów przeniesienia praw od Założycieli w trzech wariantach (kod i modele: utwór, pola eksploatacji, prawa zależne, protokół wydania z sumami kontrolnymi, wykaz OSS; sprzęt: protokół wydania z numerami seryjnymi; zgłoszenia patentowe i prawa do uzyskania patentu: cesja z wnioskiem o wpis w UPRP/EPO), oraz `krs/rejestr_umowa_checklista.md` — wymagania do umowy z podmiotem prowadzącym rejestr (wpis ograniczeń i obowiązków związanych z akcją, adres e-mail akcjonariusza, forma dyspozycji i pełnomocnictw, koszty).
6. **B6 Odpowiedź na wezwanie sądu (20).** `krs/odpowiedz_na_wezwanie.md`: szablon pisma (sygnatura, termin 7 dni, żądanie) i bank gotowych uzasadnień dla każdego postanowienia z listy ryzyk T6, z podstawą prawną i alternatywnym brzmieniem „awaryjnym”, gdyby sąd nie ustąpił.

## Etap C — dokumenty po odrębnym zleceniu (pkt 21–27)

Każdy dokument to osobny plik `.tex` w stylu repozytorium, z `\externaldocument{psa}`, statusem „projekt” i sekcją „Punkty do weryfikacji prawnej”. Kolejność zalecana: 21 → 26 → 22 → 24 → 23 → 27 → 25 (21 i 26 warunkują zawiązanie; 22–24 potrzebne w pierwszych miesiącach; 23 i 27 przed pierwszym grantem; 25 przy pierwszym partnerze).

1. **21 Umowa wykonawcza.** Wydzielić z `shareholder_agreement.tex` §§ status, odejście, nabywca, oferta, pełnomocnictwo, cena, śmierć oraz Załączniki A–B do `umowa_wykonawcza.tex`; wprowadzić uwagi z A2 (art. 101 § 2 i 108 KC, depozyt, tryb rejestru, stwierdzanie rodzaju Odejścia, sprzeciw, terminy). Zachować relację do § 10 ust. 13 i § 36 ust. 3 umowy.
2. **26 Umowa akcjonariuszy.** Pozostała część `shareholder_agreement.tex` (współdziałanie, zakaz konkurencji, IP, poufność, przystąpienie, Załącznik C) uzupełniona o tabelę T8 i trzy warunki z `regulations.md` 3a; odesłania do `umowa_wykonawcza.tex`.
3. **22 Regulamin Rady.** Z § 21 ust. 11 i § 23: podział kompetencji, limity, komitety, konflikty (§ 29), karta decyzji i rejestr decyzji z `extra.tex` Dokument nr 3, bramki G1–G6 z `regulations.md` sekcja 4 jako obowiązkowe checkpointy dyrektora ds. zgodności, posiedzenia zdalne, protokoły.
4. **23 Regulamin programu motywacyjnego.** Model 1 z `emisja/pracownik.md` (obietnica, emisja po nabyciu uprawnień): uczestnicy, harmonogram, good/bad leaver, Kryterium, ograniczenia z § 8 ust. 8, tryb transz przez Radę, wzór umowy uczestnictwa, warunki preferencji z art. 24 ust. 11–12b PIT, wariant gotówkowy dla osób spoza Kryterium.
5. **24 Wzory uchwał.** `uchwaly.tex`: WZ — uchwała ramowa serii P, 4/5 o prawie poboru, kwalifikacyjna F, emisyjna F, kierunkowa rundy, zgoda na zbycie w lock-upie, zgoda dla nabywcy spoza Kryterium, stwierdzenie Odejścia Usprawiedliwionego, zgoda na Przedsięwzięcie powyżej progu, powołanie dyrektorów, zatwierdzenie regulaminów; Rada — weryfikacja nabywcy (§ 11 ust. 9), zgoda na rozporządzenie akcją (§ 12 ust. 1), wskazanie nabywcy, stwierdzenie rodzaju Odejścia, wykonanie transzy P, klasyfikacja eksportowa (§ 23 ust. 1 lit. h), zgoda z § 27 ust. 6, Plan Finansowania.
6. **25 Wzór umowy spółki celowej / JV.** Z § 33 ust. 3–5 i `regulations.md` 3b.4: licencja niewyłączna ograniczona zakresem, ulepszenia dla Spółki, prawa informacyjne i kontrolne, zakaz przeniesienia udziału na Niedopuszczalnego Nabywcę, prawo pierwszeństwa i wyjścia, kontrola eksportu obu stron, brak danych ITAR bez zgody, repozytoria w UE, prawo właściwe; warianty: spółka celowa (sp. z o.o.) i konsorcjum kontraktowe.
7. **27 Wniosek o interpretację.** `interpretacja_pit.md`: opis stanu faktycznego i zdarzenia przyszłego (P.S.A., seria P, uchwała ramowa, uczestnicy z art. 12 i 13 PIT, B2B osobno), pytania, stanowisko wnioskodawcy z uzasadnieniem, lista danych do uzupełnienia przez doradcę podatkowego, harmonogram (przed pierwszym grantem).

## Konwencje repozytorium podczas prac

- Gałąź `psa_check`; commity jednoliniowe po polsku, jedna zmiana merytoryczna na commit; push `git push -u origin psa_check` po każdym etapie.
- Nowe pliki `.tex` kopiują preambułę z `psa_feedback.tex` (klasa, `xr-hyper`, `basilisk_i18n`, makra `\paragraf`, `\field`, `\BoilerplateStrike`), a `build.sh` dostaje je w tablicy `docs` po `psa`.
- Nie zmieniamy `psa.tex` w etapie A (zgodnie z `law.md` „Na tym etapie nie prosimy o wprowadzanie zmian do projektu”); zmiany tekstu normatywnego wyłącznie w etapie B po bramce.
- `zoo.tex` (szablon sp. z o.o. innej spółki) nie jest przedmiotem prac; można z niego wziąć porównawczo konstrukcję podwyższenia bez zmiany umowy.

## Weryfikacja

1. **Kompletność:** Grep po `memorandum.tex` dla każdego numeru pytania z `law.md` (79 numerów) i każdej sekcji T1–T9; tabela w Załączniku 1 memorandum ma tyle wierszy, ile uwag w tekście.
2. **Odesłania:** każdy `\ref{art:...}` w nowych plikach ma `\label` w `psa.tex` (Grep listy etykiet vs listy odesłań); w etapie B po każdym commicie sprawdzić, że żadne odesłanie nie „przeskoczyło” na inny § (porównać numerację ze `spis_tresci.md`), a każde twarde odesłanie `ust.~N` w `.tex` i „§ N ust. M” w `.md` zgadza się z konkordancją z `zmiany.md`.
3. **Składnia LaTeX bez kompilatora:** bilans `{}` netto zero, parzystość `\begin{…}`/`\end{…}` dla każdego środowiska, brak niezamkniętych `\field{`; w `.md` poprawność tabel.
4. **Kompilacja PDF** u użytkownika: `./build.sh` (wszystkie) albo `./build.sh memorandum`; sprawdzić w `.log` brak „undefined references” i „multiply defined labels”.
5. **Spójność merytoryczna:** brzmienia proponowane w memorandum muszą dać się wkleić do `psa.tex` bez kolizji (test w etapie B: czy każde „konieczne” ma swój commit); wariant B zmienia co najmniej cztery miejsca jednocześnie.
6. **Przegląd końcowy:** lista rzeczy do weryfikacji przez uprawnionego prawnika (Załącznik 3 memorandum) nie może być pusta ani ukryta; oznaczenia [W]/[?] policzone i wymienione w podsumowaniu.

## Kolejność i zależności

1. A0 (przygotowanie, weryfikacja aktów) → A1–A6 równolegle → A7 → A8 → commit + push → **przekazanie memorandum**.
2. Bramka: decyzje Założycieli (wpis R1 w `psa_feedback.tex`) → A9 (pytania uzupełniające, jeżeli wpłyną).
3. B1 → B2 → B3 → B4 (notariusz; ustalenia wracają do B1) → B5 → B6 → push → **wersja do aktu notarialnego**.
4. C w kolejności 21 → 26 → 22 → 24 → 23 → 27 → 25, każdy po odrębnym zleceniu; 21 i 26 najpóźniej w dniu podpisania umowy założycielskiej (§ 10 ust. 13: umowa wykonawcza „najpóźniej w dniu objęcia mechanizmem”).

## Etap A-W: weryfikacja memorandum na tekstach aktów (wykonane 30.09.2026)

Po pobraniu źródeł do `src/legal/` (skrypty `src/tools/download.sh`, `extract_text.py`) sześć pakietów A1–A6 zostało sprawdzonych przepis po przepisie w tekstach ujednoliconych; wynik to `memorandum.tex` w wersji 1.1. Oznaczenia wiarygodności: [Z] 194 → 607, [W] 370 → 163, [?] 36 → 22. Korekty merytoryczne (71 pozycji) są wymienione w podsumowaniu memorandum („Co zmieniła weryfikacja”); najważniejsze: tryb emisji serii P (3.2.1) stał się uwagą konieczną, bo KSH zna upoważnienie Rady do emisji (art. 300¹¹⁰–300¹¹³) i warunkową emisję akcji (art. 300¹¹⁴–300¹¹⁸), a prawo poboru jest dyspozytywne; organ kontroli inwestycji to minister ds. gospodarki, a próg podmiotowy to przychód powyżej 10 mln EUR; termin zgłaszania zmian do rejestru od 18.02.2027 r. wynosi 7 dni; wszystkie 19 kodów PKD zgadza się z PKD 2025 co do znaku; ustawa z 13.03.2026 r. zmienia w ustawie koncesyjnej tylko art. 44 i 56; umowa P.S.A. według wykładni literalnej nie podlega PCC. Do zrobienia: prawo Unii i orzeczenia SN po pobraniu przeglądarką (`src/tools/download_eu.py`) → memorandum 1.2.
