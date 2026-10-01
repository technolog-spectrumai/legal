# Zmiany w `psa.tex` — od wersji 0.8 do 0.9.3 (tekst czysty) z Załącznikiem nr 12

Gałąź: `psa_correction`. Punkt wyjścia: commit `1264ca2` (wersja 0.8, „tekst czysty”). Na jego szczycie leży 28 commitów, po jednej zmianie merytorycznej każdy. Stan końcowy `psa.tex` to rewizja 0.9.3 bez aparatu rewizyjnego (bez komentarzy, znaczników i bloków z poprzednim brzmieniem) oraz nowy, informacyjny Załącznik nr 12.

Plik nie był kompilowany w ramach tej rewizji. Przed wysyłką do prawnika zalecana jest kompilacja `pdflatex` i przejrzenie wyglądu nowych tabel.

## Jak korzystać z historii

- Każdy commit odpowiada jednej zmianie z planu rewizji; `git log --oneline 1264ca2..HEAD` pokazuje listę, a `git show <hash>` — dokładną różnicę w tekście.
- Commit `5194627` zawiera wersję 0.9.3 **z oznaczeniami**: ramki `[ZMIANA n — KOMENTARZ]` z uzasadnieniem, znaczniki `[ZMIENIONO]`/`[NOWE]` przy ustępach oraz bloki `[BYŁO]` z dosłownym poprzednim brzmieniem. Ta wersja jest bajt w bajt równa dawnemu plikowi `psa_new.tex`, który został usunięty z katalogu roboczego. Aby ją odtworzyć: `git show 5194627:psa.tex > psa_0.9.3_oznaczona.tex`.
- Commit `ec3a4e0` zdejmuje cały aparat rewizyjny i zostawia sam tekst umowy; commit `76c136e` dodaje Załącznik nr 12.

## Wykaz commitów

| Nr | Commit | Zmiana | Zakres |
|---:|---|---|---|
| 01 | `520e5f6` | preambuła | definicje makr oznaczeń rewizji (`\ZmianaKomentarz`, `Bylo`, `\ZM`, `\NOWE`) |
| 02 | `5f1effc` | ZMIANA 1 | § Cel strategiczny ust. 1–2; § Przedmiot działalności ust. 1, 5 (PKD przeważające 72.10.Z) |
| 03 | `3dc672e` | ZMIANA 2 | § Cel ust. 4; § Przedmiot działalności ust. 8 (klauzule koncesyjne) |
| 04 | `6e2d422` | ZMIANA 3 | § Dopuszczalny Nabywca: Kryterium Bezpieczeństwa EU/NATO, obowiązki przyszłego nabywcy |
| 05 | `5b90e1a` | ZMIANA 3 | § Zbywanie i obciążanie akcji: zgoda Spółki w reżimie art. 300^39 KSH |
| 06 | `6b430b1` | ZMIANA 3 | § Okres Ograniczenia Zbywania ust. 1: lock-up osadzony w art. 300^39 §1–2 |
| 07 | `d4f6efd` | ZMIANA 3 | § Rada Dyrektorów ust. 3: kryterium dyrektora; Załącznik nr 4 pkt 1.3 |
| 08 | `9a9da8b` | ZMIANA 4 | § Rada Dyrektorów ust. 2, 4; § Sprawy Zastrzeżone lit. i |
| 09 | `0ec873c` | ZMIANA 5 | § Zwrotne zbycie: Odejście Dobrowolne; Załączniki nr 4 i 8 |
| 10 | `e2debfe` | ZMIANA 6 | nowy § Kwalifikowana Runda Finansowania |
| 11 | `4273534` | ZMIANA 7 | § Wkłady Założycieli: wkłady pieniężne, pożyczki założycielskie |
| 12 | `97c90a5` | ZMIANA 7 | Załącznik nr 1: korekta kolumny „Cena łączna” |
| 13 | `fbd60f6` | ZMIANA 7 | Załącznik nr 1: tabela wkładów pieniężnych |
| 14 | `542b72d` | ZMIANA 8 | § Walne Zgromadzenie ust. 2–3 |
| 15 | `f0f37c4` | ZMIANA 9 | § Dziedziczenie ust. 1–2 (brzmienie rewizji 0.9) |
| 16 | `466ac09` | ZMIANA 10 | § Zakaz konkurencji ust. 8 |
| 17 | `30b81f6` | ZMIANA 11 | Załącznik nr 10 (mapa rundy) |
| 18 | `b446f00` | ZMIANA 11 | Załącznik nr 11 (podatki); wskaźnik w § Program motywacyjny |
| 19 | `d83fdd0` | ZMIANA 11 | § Postanowienia końcowe ust. 7 (zakres 4–11); noty przy Załączniku nr 9 |
| 20 | `515fe0d` | nota | „Nota rewizyjna — wykaz zmian rewizji 0.9” na początku dokumentu |
| 21 | `62a959f` | ZMIANA 12 | § Zbywanie ust. 7: Kryterium EU/NATO mimo wyłączenia zgody |
| 22 | `c08dcc4` | ZMIANA 13 | § Okres Ograniczenia ust. 2 lit. a: wyjątek rundy finansowania |
| 23 | `19b6a6b` | ZMIANA 14 | § Dziedziczenie ust. 1–2 i § Małżonek ust. 3: Kryterium EU/NATO |
| 24 | `632916d` | ZMIANA 15 | § Zwrotne zbycie, Odejście Zawinione lit. e: uporządkowana rezygnacja |
| 25 | `760932a` | ZMIANA 16 | enumeracje: umowa wykonawcza, § Seria F ust. 10, Załącznik nr 4 |
| 26 | `5194627` | wersja | wykaz zmian 0.9.3 w nocie, nagłówki i strona tytułowa „0.9.3” |
| 27 | `ec3a4e0` | tekst czysty | usunięcie komentarzy, znaczników, bloków BYŁO i not rewizyjnych |
| 28 | `76c136e` | Załącznik nr 12 | profil produkcyjny a startupowy; czerwona uwaga weryfikacyjna; zakres 4–12 |

Wszystkie commity mają jednoliniowe wiadomości i tego samego autora (`technolog`). Do repozytorium dodawany był wyłącznie `psa.tex` (oraz niniejszy plik).

## Objaśnienie zmian rewizji 0.9

### ZMIANA 1 — cel spółki: physical AI jako działalność główna (commit 02)

Odwrócono hierarchię celu. Dotychczas głównym celem było projektowanie i produkcja bezzałogowych statków powietrznych, a fizyczna sztuczna inteligencja była działalnością „powiązaną”. Po zmianie głównym przedmiotem działalności jest fizyczna (ucieleśniona) sztuczna inteligencja i systemy autonomiczne, a BSP są ich pierwszym i podstawowym zastosowaniem. Dzięki temu rozwój kolejnych zastosowań (roboty lądowe, jednostki nawodne, licencjonowanie stosu autonomii) nie stanowi „istotnej zmiany profilu działalności” wymagającej 75% głosów na podstawie § Sprawy Zastrzeżone. Spójnie przeredagowano plan działalności w § Przedmiot działalności i zmieniono działalność przeważającą PKD z 30.31.Z (produkcja cywilnych statków powietrznych) na 72.10.Z (badania naukowe i prace rozwojowe); 30.31.Z pozostaje na drugiej pozycji.

Do potwierdzenia z doradcą: jeżeli spółka od początku będzie przede wszystkim produkować sprzęt, zasadne może być pozostawienie 30.31.Z jako działalności przeważającej (statystyka GUS, wymogi programów finansowania, sprawozdawczość). Załącznik nr 12 wraca do tej decyzji.

### ZMIANA 2 — przywrócenie klauzul koncesyjnych (commit 03)

W wersji 0.8 klauzule koncesyjne w § Cel ust. 4 i § Przedmiot działalności ust. 8 były przekreślone (przeznaczone do usunięcia). Przywrócono je i doprecyzowano podstawy prawne: ustawa z 13 czerwca 2019 r. o wykonywaniu działalności gospodarczej w zakresie wytwarzania i obrotu materiałami wybuchowymi, bronią, amunicją oraz wyrobami i technologią o przeznaczeniu wojskowym lub policyjnym (Dz.U. 2019 poz. 1214 ze zm.), certyfikacja lotnicza BSP, przepisy o kontroli obrotu towarami o znaczeniu strategicznym oraz prawo lotnicze i regulacje UE o bezzałogowych systemach powietrznych. Uzasadnienie: granica między cywilnym a koncesjonowanym rozwojem BSP bywa sporna, więc wyraźne rozgraniczenie etapów ma wartość ostrożnościową wobec KRS, banków i partnerów. Klauzula nie tworzy nowego obowiązku, potwierdza obowiązki ustawowe.

### ZMIANA 3 — Kryterium Bezpieczeństwa EU/NATO i zgoda Spółki na rozporządzenie akcją (commity 04–07)

Usunięto niespójność strategiczną: dostęp do Kluczowej Własności Intelektualnej spoza UE/NATO wymagał zgody Rady, ale akcje mógł nabyć każdy niesankcjonowany podmiot z dowolnej jurysdykcji. Zmiana składa się z czterech kroków:

1. **§ Dopuszczalny Nabywca** (commit 04): nowa definicja „Kryterium Bezpieczeństwa EU/NATO” (obywatelstwo lub stałe miejsce zamieszkania w państwie UE/EOG/NATO; dla podmiotów — siedziba, rzeczywisty ośrodek zarządzania, brak kontroli spoza tych państw, beneficjenci rzeczywiści). Walne Zgromadzenie może większością 75% wszystkich głosów rozstrzygnąć przypadek graniczny albo dopuścić nabywcę spoza Kryterium. Dodano ustęp o obowiązkach osoby, która nie jest jeszcze akcjonariuszem: do czasu nabycia obowiązki informacyjne obciążają zbywcę (domknięcie pkt 1 „Podsumowania audytu”). Definicje Niedopuszczalnego Nabywcy i Prawnie Niedopuszczalnego Posiadacza pozostały bez zmian.
2. **§ Zbywanie i obciążanie akcji** (commit 05): rozporządzenie akcją wymaga zgody Spółki w rozumieniu art. 300^39 §1 KSH, udzielanej przez Radę Dyrektorów w formie dokumentowej w 14 dni. Odmowa jest możliwa wyłącznie z zamkniętego katalogu przyczyn (Niedopuszczalny Nabywca; brak Kryterium EU/NATO bez zgody WZ; Okres Ograniczenia; brak informacji — ze wstrzymaniem terminu). Przy odmowie z powodu braku Kryterium Spółka wskazuje w ciągu miesiąca innego nabywcę za Wartość Godziwą, zgodnie z mechanizmem art. 300^39 §3–6 KSH; brak wskazania lub zapłaty oznacza swobodę zbycia. Dawne ust. 3–5 zachowano jako ust. 5, 6 i 8; nowy ust. 7 wyłącza spod zgody egzekucję, prawo pierwszeństwa, przyłączenia, przymusowe współzbycie, zwrotne zbycie i Kwalifikowaną Rundę.
3. **§ Okres Ograniczenia Zbywania** (commit 06): 12-miesięczny lock-up osadzono w ustawowym reżimie art. 300^39 §1–2 KSH zamiast „twardego” zakazu umownego, którego skuteczność zakwestionował audyt (pkt 2). W Okresie Ograniczenia mechanizm wskazania innego nabywcy jest wyłączony. Do weryfikacji przez prawnika: granice dopuszczalnej derogacji §3–6 na podstawie „chyba że umowa spółki stanowi inaczej”.
4. **§ Rada Dyrektorów ust. 3** (commit 07): dyrektorem może być wyłącznie osoba fizyczna spełniająca Kryterium EU/NATO (dotychczasowe odesłanie do „kryteriów Dopuszczalnego Nabywcy” było puste treściowo). Dostosowano opis prawa rozporządzania akcjami w Załączniku nr 4.

Kontekst biznesowy: struktura właścicielska spoza UE/NATO może wykluczać Spółkę z programów EDF, NATO DIANA i części zamówień obronnych. Zmiana nie przywraca uznaniowego weta — odmowa nadal wymaga konkretnej, obiektywnej podstawy.

### ZMIANA 4 — próg powołania dyrektorów i ciągłość Rady (commit 08)

Przy podziale 50/20/10/10/10 żadna dwójka Założycieli nie osiąga 75% wszystkich głosów, więc nieobecność jednego większego akcjonariusza blokowała obsadę Rady, a mechanizm impasu nie obejmuje spraw personalnych. Po zmianie: powołanie dyrektora i odwołanie z ważnych powodów — bezwzględna większość głosów oddanych; odwołanie bez ważnych powodów przed upływem kadencji — nadal 75% wszystkich głosów. Nowy ust. 4: mandat dyrektora trwa do powołania następcy, nie dłużej niż 6 miesięcy, a przy spadku składu poniżej minimum każdy akcjonariusz może żądać zwołania WZ. W § Sprawy Zastrzeżone lit. i usunięto powołanie i odwołanie dyrektorów z katalogu 75%. Do weryfikacji przez prawnika: dopuszczalność prorogacji mandatu w P.S.A.

### ZMIANA 5 — Odejście Dobrowolne (commit 09)

Dotychczas dobrowolne odejście przed upływem 48 miesięcy było Odejściem Zawinionym (lit. f), co pozwalało odebrać także akcje już zwolnione za 80% Wartości Godziwej — ostrzej niż standard rynkowy. Usunięto lit. f i wyodrębniono trzecią kategorię „Odejście Dobrowolne”: akcje niezwolnione podlegają zbyciu po cenie emisyjnej, akcje zwolnione pozostają przy odchodzącym, a Spółka ma 6-miesięczną opcję wskazania nabywcy po 100% Wartości Godziwej. Odejście Zawinione zarezerwowano dla realnych przewinień (lit. a–e). Zaktualizowano opisy w Załącznikach nr 4 i 8.

### ZMIANA 6 — Kwalifikowana Runda Finansowania (commit 10)

Nowy paragraf przygotowuje umowę na rundę inwestycyjną: definiuje Kwalifikowaną Rundę (inwestorzy spełniający test sankcyjny i Kryterium EU/NATO; próg kwotowy lub wycena — pola do uzupełnienia), wymaga uchwały kierunkowej 75%, tworzy zobowiązanie współdziałania w dobrej wierze po jej podjęciu, wyznacza katalog zwyczajowych warunków inwestorskich dopuszczalnych bez zmiany umowy (liquidation preference non-participating do 1x, broad-based weighted average, dyrektor lub obserwator inwestora, prawa informacyjne, pro-rata) i zastrzega dalej idące warunki dla odrębnej uchwały 75%. Prawo poboru i status emisji jako Sprawy Zastrzeżonej pozostają nienaruszone. Do weryfikacji przez prawnika: skuteczność zobowiązań do głosowania (ust. 3). Mapa paragrafów przygotowujących rundę — Załącznik nr 10.

### ZMIANA 7 — wkłady pieniężne obok niepieniężnych (commity 11–13)

Dotychczas akcje serii A obejmowano wyłącznie za własność intelektualną i sprzęt, więc Spółka rodziła się bez gotówki, a P.S.A. nie zna dopłat. Dopuszczono wkłady pieniężne (lit. d), przeznaczane w całości na kapitał akcyjny i wnoszone przed wpisem do rejestru; dodano wyraźne odesłanie do pożyczek założycielskich (ust. 7). Wyłączenie pracy i usług jako wkładu pozostało.

W Załączniku nr 1 skorygowano kolumnę „Cena łączna”: kwoty 50 000 / 20 000 / 10 000 / 10 000 / 10 000 zł były dziesięciokrotnie zawyżone względem ceny emisyjnej 0,01 zł za akcję (1 000 000 akcji × 0,01 zł = 10 000 zł); po korekcie 5 000 / 2 000 / 1 000 / 1 000 / 1 000 zł. Dodano tabelę wkładów pieniężnych z wierszem „Razem (kapitał akcyjny)”.

### ZMIANA 8 — Walne Zgromadzenie (commit 14)

Domknięcie pkt 4 audytu. Dotychczasowe „albo z wykorzystaniem środków komunikacji elektronicznej” mogło być czytane jako w pełni wirtualne WZ bez miejsca, co jest wątpliwe na tle art. 300^88 i 300^92 KSH. Po zmianie WZ ma zawsze miejsce fizyczne (siedziba albo Warszawa), a udział elektroniczny jest trybem uczestnictwa. Zawiadomienia idą wyłącznie na adres e-mail wpisany do rejestru akcjonariuszy (art. 300^87 KSH); usunięto „lub wskazany Spółce” i dodano obowiązek wpisania i aktualizacji adresu.

### ZMIANA 9 — dziedziczenie w art. 300^41 KSH (commit 15)

Domknięcie pkt 3 audytu. Mechanizm osadzono wprost w art. 300^41 §1 KSH, który pozwala ograniczyć wstąpienie spadkobierców pod warunkiem określenia w umowie warunków spłaty spadkobierców niewstępujących. Warunki spłaty: 100% Wartości Godziwej na dzień otwarcia spadku, płatne na zasadach ratalnych. Dotychczasowe obowiązkowe zbycie zachowano jako mechanizm rezerwowy. Do weryfikacji przez prawnika: technika wykonania spłaty i los akcji spadkobierców niewstępujących oraz zgodność 90-dniowego terminu z art. 300^41 KSH.

### ZMIANA 10 — fallback Walnego Zgromadzenia (commit 16)

Domknięcie pkt 5 audytu. Dotychczasowy ust. 8 § Zakaz konkurencji pozwalał zastąpić uchwałę Rady uchwałą WZ także tam, gdzie uchwały Rady wymaga sama ustawa (art. 300^75 §2 KSH). Po zmianie fallback WZ działa wyłącznie w sprawach, w których wymóg uchwały Rady wynika tylko z umowy; gdzie wymaga go ustawa, transakcja czeka na przywrócenie zdolności decyzyjnej Rady (np. przez powołanie dodatkowego dyrektora wolnego od konfliktu), a uchwała WZ może być jedynie dodatkową zgodą właścicielską.

### ZMIANA 11 — nowe załączniki i noty (commity 17–19)

Załącznik nr 10 (informacyjny): mapa elementów typowego term-sheetu i paragrafów umowy, które je obsługują. Załącznik nr 11 (informacyjny): punkty do weryfikacji podatkowej — w szczególności znany spór o stosowalność preferencji z art. 24 ust. 11–12b ustawy o PIT (ESOP) do prostej spółki akcyjnej, opodatkowanie objęcia akcji serii P po 0,01 zł, wyłączenie współpracowników B2B, aport IP Założycieli oraz wkłady pieniężne i pożyczki założycielskie; zalecenie wystąpienia o interpretację indywidualną przed pierwszym grantem. W § Program motywacyjny dodano jedynie wskaźnik do Załącznika nr 11 (treść normatywna bez zmian). Zakres załączników informacyjnych w § Postanowienia końcowe rozszerzono na 4–11. Przy Załączniku nr 9 dodano noty, że audyt dotyczy wersji 0.8 (obie noty usunięto w commicie 27 razem z resztą aparatu rewizyjnego).

### Nota rewizyjna (commit 20)

Sekcja na początku dokumentu z listą [ZMIANA 1–11] i relacją do „Podsumowania audytu” (zmiany 3, 8, 9 i 10 odpowiadają punktom 2, 4, 3 i 5; punkt 1 adresuje nowy ustęp w § Dopuszczalny Nabywca). Usunięta w commicie 27; jej treść merytoryczną zastępuje niniejszy plik.

## Objaśnienie zmian rewizji 0.9.3 (Etapy 1–2 planu poprawek)

Rewizja 0.9.3 obejmuje wyłącznie poprawki spójności rewizji 0.9. Etap 1 — szczelność Kryterium EU/NATO; Etap 2 — domknięcie Odejścia Dobrowolnego. Etapy 3–5 (tempo kontraktowania, decyzje strategiczne, zbiorczy re-audyt) świadomie nie zostały wprowadzone.

### ZMIANA 12 — Kryterium EU/NATO mimo wyłączenia zgody (commit 21)

W rewizji 0.9 ścieżki wyłączone spod zgody Spółki (pierwszeństwo, przyłączenie, przymusowe współzbycie, zwrotne zbycie, Kwalifikowana Runda) zachowywały tylko test sankcyjny, a Kryterium EU/NATO było egzekwowane wyłącznie „w trybie zgody” — luka, przez którą przymusowe współzbycie (sprzedaż 100%) mogło ominąć bramkę EU/NATO. Po zmianie Kryterium (z możliwością zgody WZ 75%) obowiązuje niezależnie od wyłączenia zgody; wyjątek pozostaje tylko dla egzekucji (art. 300^39 §6 KSH). Przy drag-along spełnienie Kryterium weryfikuje się przed doręczeniem zawiadomienia.

### ZMIANA 13 — wyjątek rundy finansowania w lock-upie (commit 22)

Rewizja 0.9 posługiwała się niezdefiniowanym pojęciem „zatwierdzonej rundy finansowania”. Wyjątek od lock-upu obejmuje teraz Kwalifikowaną Rundę oraz każdą inną rundę zatwierdzoną uchwałą WZ większością 75% wszystkich głosów; dodano „objęcie akcji”, bo udział w rundzie to objęcie nowych akcji, nie zbycie.

### ZMIANA 14 — Kryterium EU/NATO dla spadkobierców i małżonków (commit 23) — DECYZJA DO POTWIERDZENIA

W rewizji 0.9 spadkobierca i małżonek przechodzili wyłącznie test sankcyjny, więc osoba spoza UE/NATO wchodziła do Spółki bez bramki. Po zmianie spadkobierca niespełniający Kryterium wstępuje tylko za zgodą WZ (75%); bez niej jest spadkobiercą niewstępującym ze spłatą 100% Wartości Godziwej. Analogicznie małżonek nabywający akcje. Alternatywa (jeżeli Założyciele uznają ochronę rodzin za ważniejszą): przywrócić brzmienie 0.9 i potraktować dziedziczenie jako świadomy wyjątek od Kryterium. Ryzyko wariantu przyjętego: spłata 100% Wartości Godziwej rodziny zmarłego wymaga realnych środków, więc ubezpieczenie na życie z § Dziedziczenie ust. 5 staje się praktycznie obowiązkowe.

### ZMIANA 15 — uporządkowana rezygnacja a Odejście Zawinione (commit 24)

Definicja Odejścia Dobrowolnego wyklucza je przy jakimkolwiek zdarzeniu z katalogu Zawinionego, a rezygnacja jest w praktyce „odmową dalszego wykonywania obowiązków” — Spółka w konflikcie z odchodzącym miała gotowy argument, by każdą rezygnację przekwalifikować na Zawinione. Po zmianie rezygnacja z zachowaniem co najmniej 30-dniowego okresu przejściowego i należytym wykonywaniem obowiązków nie wypełnia lit. e; pozostałe litery a–d działają bez zmian.

### ZMIANA 16 — uzupełnienie enumeracji o Odejście Dobrowolne (commit 25)

Ustęp o odrębnej umowie wykonawczej wymieniał tylko stwierdzanie Odejścia Usprawiedliwionego i Zawinionego; uzupełniono o Odejście Dobrowolne i tryb wykonania 6-miesięcznego prawa nabycia akcji zwolnionych. Analogicznie w § Seria F ust. 10 oraz w Załączniku nr 4 („Mechanizm czasowy”).

### Wersja 0.9.3 (commit 26)

Wykaz zmian 0.9.3 w nocie rewizyjnej oraz oznaczenia wersji (nagłówki, strona tytułowa: „0.9.3”, „[ZMIANA 1–16]”). Ten commit jest tożsamy z dawnym `psa_new.tex`.

## Tekst czysty (commit 27)

Usunięto cały aparat rewizyjny: definicje makr z preambuły, sekcję „Nota rewizyjna”, wszystkie ramki `[ZMIANA n — KOMENTARZ]` (28 sztuk), wszystkie bloki `[BYŁO]` (17 sztuk), 52 znaczniki `[ZMIENIONO]`/`[NOWE]` oraz obie noty rewizyjne przy Załączniku nr 9. Nagłówki i strona tytułowa wróciły do brzmienia „tekst czysty” („Projekt umowy — tekst czysty”, „Wersja 0.9.3 — tekst czysty”, „Tekst umowy bez komentarzy i materiałów roboczych”); numer wersji pozostał 0.9.3. Treść normatywna nie została zmieniona.

Skutek uboczny do świadomej akceptacji: Załącznik nr 9 (audyt paragraf po paragrafie) odnosi się do tekstu wersji 0.8 i nie ma już przy nim noty, która o tym informowała. Jeżeli audyt ma pozostać w dokumencie, warto dopisać jedno zdanie o jego zakresie albo zlecić ponowny audyt zmienionych paragrafów.

## Załącznik nr 12 — profil produkcyjny a profil startupowy (commit 28)

Nowy załącznik informacyjny (nie tworzy praw ani obowiązków; § Postanowienia końcowe ust. 7 rozszerzono na 4–12). Zawiera:

1. Definicje dwóch profili: produkcyjnego (wytwarzanie, certyfikacja, serwis sprzętu, finansowanie przychodowe, dotacyjne i dłużne, działalność regulowana) i startupowego (rundy kapitałowe, wynagradzanie akcjami, vesting, wyjście inwestorów) oraz oznaczenia **P** (korzystne lub konieczne dla spółki produkcyjnej), **S** (stricte startupowe), **U** (uniwersalne).
2. Tabelę 54 wierszy, która każdemu postanowieniu umowy przypisuje profil i uzasadnienie, z odesłaniami `§~\ref{}` do właściwych paragrafów — w podziale na: formę i cel; akcje i wkłady; obrót akcjami i wycenę; organy; technologię i zgodność; finansowanie i zakończenie działalności.
3. Tabelę załączników nr 1–11 według profilu.
4. Podział elementów startupowych na uśpione (program motywacyjny, seria F, Kwalifikowana Runda, instrumenty zamienne, vesting — wszystkie wymagają odrębnej uchwały 75% albo wpisu „TAK” w Załączniku nr 2) i działające z mocy samej umowy (drag-along, wyłączenia spod zgody, struktura 1 000 000 akcji po 0,01 zł, PKD 72.10.Z, katalog czynników wyceny).
5. Uwagi wykonawcze dla profilu produkcyjnego: kapitał z wkładów pieniężnych, progi kwotowe a budżet (próg 100 000 zł dla finansowania i zabezpieczeń działa niezależnie od budżetu), zabezpieczenie na Kluczowej IP jako Sprawa Zastrzeżona, czynniki wyceny, zależność zakazu konkurencji od statusu Akcjonariusza Funkcjonalnego, obowiązki zgodności od pierwszego dnia, etapowanie działalności koncesjonowanej, rezerwy i ubezpieczenie, zaplecze Założycieli.
6. Punkty decyzyjne dla Założycieli.

**Czerwona uwaga weryfikacyjna.** Na początku załącznika, przy wierszach A5, C2 i D2 tabeli oraz w sekcjach 5 i 6 dodano czerwonym drukiem zastrzeżenie, że dwa elementy wymagają sprawdzenia przez prawnika przed podpisaniem: Kryterium Bezpieczeństwa EU/NATO (dopuszczalność i skuteczność ograniczeń według obywatelstwa, siedziby i kontroli; przepisy o kontroli inwestycji; zgodność z wymogami programów, dla których je wprowadzono) oraz klauzule koncesyjne i certyfikacyjne (aktualność podstawy prawnej z ustawy z 13 czerwca 2019 r., zakres wyrobów objętych koncesją w odniesieniu do BSP i ich oprogramowania, relacja do prawa lotniczego i regulacji UE). Do czasu weryfikacji oba elementy należy traktować jako założenia projektowe.

## Zbiorcza lista punktów do decyzji i weryfikacji prawnej

| Źródło | Punkt |
|---|---|
| ZMIANA 1 | działalność przeważająca: 72.10.Z czy 30.31.Z (decyzja z doradcą) |
| ZMIANA 3 | zakres dopuszczalnej derogacji art. 300^39 §3–6 KSH w Okresie Ograniczenia (wyłączenie wskazania nabywcy) |
| ZMIANA 4 | dopuszczalność prorogacji mandatu dyrektora w P.S.A. |
| ZMIANA 6 | skuteczność i granice zobowiązań do głosowania przy Kwalifikowanej Rundzie |
| ZMIANA 9 | technika spłaty spadkobierców niewstępujących; zgodność 90-dniowego terminu z art. 300^41 KSH |
| ZMIANA 14 | Kryterium EU/NATO dla spadkobierców i małżonków — decyzja Założycieli (wariant przyjęty albo alternatywa) |
| Załącznik nr 11 | interpretacja indywidualna w sprawie ESOP w P.S.A. przed pierwszym grantem |
| Załącznik nr 12 | Kryterium EU/NATO i klauzule koncesyjne — weryfikacja prawna (czerwona uwaga) |
| tekst 0.8 | § Transakcje z Akcjonariuszami jest w umowie oznaczony „[WYMAGA OPINII PRAWNIKA]” |
| commit 27 | Załącznik nr 9 (audyt) odnosi się do wersji 0.8 — brak noty o zakresie |

## Wykryta usterka do rozstrzygnięcia (nie poprawiono)

§ Dziedziczenie ust. 2 stanowi, że spłata jest „płatna na zasadach określonych w ust. 5”, tymczasem zasady ratalne (36 rat, oprocentowanie, zabezpieczenie) zawiera ust. 4, a ust. 5 dotyczy ubezpieczenia na życie Założycieli. Błędne odesłanie pochodzi z rewizji 0.9 (komentarz do ZMIANY 9 również mówił o „zasadach ratalnych z ust. 5”). Poprawka sprowadza się do zamiany „ust.~5” na „ust.~4” w tym jednym zdaniu; nie została wprowadzona, bo dotyczy tekstu normatywnego i wymaga decyzji autora.

## Weryfikacja techniczna wykonana przy tworzeniu historii

- Każdy stan pośredni był budowany wyłącznie z linii wersji docelowej (bez ręcznego przepisywania tekstu), a stan po commicie 26 porównano bajt w bajt z `psa_new.tex` — różnica pusta.
- Po każdym commicie sprawdzano bilans nawiasów `{}` (netto zero) i parzystość `\begin{…}`/`\end{…}` dla każdego środowiska; po commicie 28 dodatkowo, że wszystkie `\ref` w Załączniku nr 12 wskazują istniejące etykiety.
- Historia: `git log 1264ca2..HEAD --format='%b'` nie zawiera treści (same jednoliniowe tematy); autor wszystkich commitów: `technolog <technolog@spectrumai.pl>`.
- Kompilacji LaTeX nie wykonywano.


# Zmiany w `psa.tex` — od wersji 0.9.4-C do 1.0-RC (wdrożenie memorandum)

Gałąź: `psa_v3`. Punkt wyjścia: commit `cab9b54` (`psa_check`, wersja 0.9.4-C wysłana kancelarii, memorandum 1.2). Jedna uwaga memorandum = jeden commit; po każdym commicie push. Uzasadnienie każdej zmiany (pytanie, ocena, rekomendacja, podstawa prawna, orzecznictwo), uwagi niewdrożone i fragmenty redagowane samodzielnie: **`comments.md`**.

## Założenia

Wdrożenie przyjmuje rekomendacje memorandum w miejsce decyzji Założycieli (Załącznik nr 2 memorandum): D2 wariant A, D3 przywrócony wyjątek dla funduszy (§ 11 ust. 14), D4 usunięte przekreślenia, D5 Kryterium wobec spadkobierców i małżonków utrzymane, D6 warstwa kontroli UE/EOG w umowie wykonawczej, D7 PKD 72.10.Z, D10 dom maklerski, D11 warunkowa emisja dla serii P. Pola `\field{}` z danymi pozostają do uzupełnienia.

## Do decyzji przed aktem notarialnym

- **§ 21 ust. 3** — ogólny wyjątek dla dyrektora spoza Kryterium (memorandum 1.1.5) zastąpiono węższym (4.4.2 V: jeden dyrektor niewykonawczy wskazany przez Kwalifikowanego Inwestora Finansowego).
- **§ 38** — zdanie „W sprawach nieuregulowanych…” nie zostało przywrócone (memorandum 4.3.1 vs D4).
- **§ 30 ust. 2 i 5** — próg 500 000 zł; **§ 33 ust. 4** — zakres „państw zaufanych” (Ukraina nie wprost); **§ 31 ust. 3** — bez odesłania do Kryterium.
- Nowe pola: § 16 ust. 5 (48 miesięcy), § 19 ust. 4 (instytucja neutralna), § 32 (5), kara umowna w umowie wykonawczej § 13 ust. 6.

## Wykaz commitów

| Nr | Commit | Zmiana | Memorandum |
|---:|---|---|---|
| 01 | `5957c54` | § 4 ust. 7: wskazanie kodu PKD nie jest podstawą do rozpoczęcia działalności regulowanej | 4.1.2 |
| 02 | `118cdd5` | § 4 ust. 8, § 3 ust. 4: klauzula koncesyjna obejmuje oprogramowanie i technologię, odesłanie dynamiczne; ocena zgodności i zezwolenia operacyjne BSP | 4.1.1 |
| 03 | `6eb54df` | § 5 ust. 2, § 9 ust. 4 i 6: usunięcie zbędnego określenia akcji imiennych | 4.3.3 |
| 04 | `d0b769a` | § 5 ust. 6: przywrócenie ustępu o rejestrze akcjonariuszy w brzmieniu merytorycznym (wybór podmiotu, zgłaszanie ograniczeń i obowiązków) | 4.3.2 |
| 05 | `2ba6155` | § 7 ust. 3: wskazanie podstawy wyceny wkładów niepieniężnych i oświadczenie Założycieli o ich wartości | 3.1.1 |
| 06 | `9a6a433` | § 7 ust. 4: przeznaczenie na kapitał akcyjny także wkładów niepieniężnych, stwierdzenie wniesienia uchwałą Rady | 3.1.2, K12 |
| 07 | `e6b6941` | § 8 ust. 3 i 5: emisja serii P w trybie warunkowej emisji akcji (tryb podstawowy) albo zwykłym; wyłączenie prawa poboru serii P w umowie | 3.2.1, K14 |
| 08 | `e9349ee` | § 9 ust. 3: uchwała kwalifikacyjna nie jest przyrzeczeniem oferty, roszczenie o akcje serii F wyłącznie z umowy objęcia | 3.2.3 |
| 09 | `9bfd334` | § 9 ust. 4, § 8 ust. 9: termin 31.12.2036 odniesiony do dnia uchwały o emisji; zwiększenie puli serii P tylko zmianą umowy | 3.2.2 |
| 10 | `9ef37ea` | § 10 ust. 6a: przesłanka przestępstwa, 24-miesięczny limit przekwalifikowania Odejścia, dopłata po ustaleniu innego rodzaju Odejścia | 1.5.4 |
| 11 | `0102d0c` | § 10 ust. 6b: kwalifikacja Odejścia niezależna od podstawy zaangażowania, skutek prawomocnego ustalenia bezzasadności rozwiązania; umowa wykonawcza: ograniczenie kar umownych wobec założycieli-pracowników | 1.5.5 |
| 12 | `9790623` | § 10 ust. 8 lit. b: 80% Wartości Godziwej jako cena umowna opcji, nie kara umowna, z zaliczeniem różnicy na odszkodowanie; umowa wykonawcza: wyłączenie nabywcy finansowanego przez Spółkę | 1.5.2 |
| 13 | `9c212c7` | § 10 ust. 10: definicje Zmiany Kontroli i Istotnej Przyczyny, okno od umowy do 12 miesięcy po zamknięciu, konstruktywne odejście | 1.5.6 |
| 14 | `b525dd9` | § 10 ust. 13: rozszerzenie obowiązkowej treści umowy wykonawczej (oferta lub umowa przedwstępna, oznaczony pełnomocnik z podpisem poświadczonym, wstrzymanie terminu, niezapłacenie ceny, zbieg z prawem pierwszeństwa) | 1.5.3, K4 |
| 15 | `1bb60c1` | § 10 ust. 14: obowiązek zbycia obciąża każdoczesnego posiadacza akcji, Spółka żąda wpisu wzmianek w rejestrze (art. 300^33 KSH) | 1.5.1, K3 |
| 16 | `65fc8d4` | Umowa wykonawcza § 13 ust. 5: warstwa kontroli UE/EOG w okresie finansowania EDF/AGILE/EUDIS, ze zgodą WZ 75% | 1.1.1, decyzja D6 |
| 17 | `f48967d` | § 11 ust. 6: definicja porozumienia i działania na cudzy rachunek, zawiadomienie o porozumieniu w 14 dni, okresowe ponowienie oświadczenia | 1.1.3 |
| 18 | `0e85d47` | § 11 ust. 11a: tryb stwierdzenia statusu Prawnie Niedopuszczalnego Posiadacza, wstrzymanie świadczeń i praw, wyłączenie głosów zawieszonych z mianownika, prawa zarządcy przymusowego; § 24 ust. 12 odesłanie | 1.7.3, K9 |
| 19 | `2f502f1` | .gitignore: pomijaj PDF-y budowane lokalnie w katalogu głównym | — |
| 20 | `a839982` | § 11 ust. 14, § 32 ust. 1: przywrócenie wyjątku dla Kwalifikowanego Inwestora Finansowego w brzmieniu uszczelnionym (zarządzający regulowany, rozproszenie, progi 25%/50%/10%, ujawnienie beneficjentów, zawiadomienia) i odesłania | 1.4.1, 1.4.3, decyzja D3 |
| 21 | `802a590` | § 11 ust. 14: test kontroli także nad zarządzającym i przez inwestora spoza Kryterium, zachowanie weryfikacji i obowiązków AML, fundusze siostrzane bez odrębnej uchwały | 4.4.2, brzmienie I |
| 22 | `06a40d7` | § 11 ust. 15: 3-miesięczny termin na wskazanie nabywcy przez Spółkę, Wartość Godziwa na dzień zdarzenia, wyłączenie Spółki jako nabywcy poza art. 300^47 KSH, skutek braku wskazania | 1.1.4 |
| 23 | `6255bdf` | § 11 ust. 16: obowiązek akcjonariusza z pakietem co najmniej 20% dostarczenia zaświadczeń o niekaralności i danych do postępowania koncesyjnego | 4.1.1 |
| 24 | `d67d64e` | § 11 ust. 15: utrata Kryterium przez Kwalifikowanego Inwestora Finansowego ograniczona do zmiany kontroli nad zarządzającym i uprawnień inwestora spoza Kryterium | 4.4.2, brzmienie II |
| 25 | `06f6c30` | § 12 ust. 1: milczenie Rady Dyrektorów jako fikcja odmowy z przyczyny ust. 2 lit. b uruchamiająca ust. 3 | 1.3.1 |
| 26 | `69edc0b` | § 12 ust. 8: Przeniesienia Dozwolone Kwalifikowanego Inwestora Finansowego (fundusz następca, równoległy, spółka celowa, wydanie inwestorom) bez zgody Spółki i prawa pierwszeństwa, z weryfikacją i Kryterium | 4.4.1, 4.4.2 brzmienie III |
| 27 | `5d857c8` | § 12 ust. 2 lit. e: zawiadomienie organu kontroli inwestycji składa nabywca przy współdziałaniu zbywcy i Spółki, termin złożenia i chwila ustania wstrzymania | 1.1.2 |
| 28 | `dfec229` | § 12 ust. 2 lit. d i e: jedno wezwanie i limit 60 dni wstrzymania, skutek braku informacji; zgoda warunkowa i 30-dniowy termin zawiadomienia organu | 1.3.2 |
| 29 | `b99588c` | § 12 ust. 2 lit. f: odmowa zgody na zbycie akcji objętych obowiązkiem zbycia nabywcy, który nie przystąpił do umowy wykonawczej | 1.5.1, K2 |
| 30 | `775f392` | § 12 ust. 4: wyraźna derogacja art. 300^39 § 3-5 KSH (z odesłaniem do § 2) przy odmowie z przyczyny ust. 2 lit. f | 1.2.1 |
| 31 | `67a005d` | § 12 ust. 3: zaświadczenie Spółki w 7 dni o powstaniu swobody zbycia jako dokument dla rejestru akcjonariuszy | 1.2.2 |
| 32 | `13c7189` | § 12 ust. 3: 90-dniowy termin końcowy wyceny z płatnością według wartości wskazanej przez Radę, raty bez zgody zbywcy tylko przy 50% z góry, do 12 rat i zastawie albo gwarancji, dzień przeniesienia | 1.2.3 |
| 33 | `ed56b6f` | § 12 ust. 4: wyraźna derogacja art. 300^39 § 3-5 KSH przy odmowie z powodu Niedopuszczalnego Nabywcy, wstrzymanie terminu nie jest odmową | 1.2.7 |
| 34 | `7c2d9db` | § 12 ust. 7: potwierdzenie wyniku weryfikacji przez Radę Dyrektorów (niebędące zgodą) jako dokument dla rejestru przy nabyciach zwolnionych ze zgody Spółki | 1.2.8 |
| 35 | `5593c71` | § 12 ust. 10: obowiązek Rady Dyrektorów ujawnienia ograniczeń i obowiązków w rejestrze akcjonariuszy w 7 dni, wpis nabywcy po przedstawieniu zgody albo potwierdzenia z ust. 7 | 1.1.6 |
| 36 | `171d699` | § 13 ust. 1: derogacja ograniczona do art. 300^39 § 3-5 KSH, ujawnienie Okresu Ograniczenia z datą końcową; § 12 ust. 7, § 14 ust. 6: przeniesienie do podmiotu kontrolowanego bez zgody Spółki i prawa pierwszeństwa | 1.2.6 |
| 37 | `6870417` | § 13 ust. 2 lit. a, § 33 ust. 2: wyjątek dla zbycia wtórnego na rzecz inwestora Rundy zatwierdzonego w uchwale kierunkowej, bez prawa pierwszeństwa, z zachowaniem zwrotnego zbycia; zgoda z § 11 ust. 6 w uchwale kierunkowej | 3.3.3 |
| 38 | `8dce83a` | § 14 ust. 1 i 4: wygaśnięcie oferty przy odmowie zgody, wskazanie nabywcy zastępuje prawo pierwszeństwa, 60 dni od upływu terminów z ust. 3, wymóg Kryterium wobec nabywcy | 1.3.4 |
| 39 | `8fc2c03` | § 14 ust. 3: nabycie przez Spółkę w granicach upoważnienia WZ (art. 300^47 § 1 pkt 2 i § 2 KSH) albo wskazanie w 20 dni samodzielnego nabywcy spełniającego Kryterium | 1.3.5 |
| 40 | `b876db3` | § 16 ust. 5: ochrona serii inwestorskiej przy przymusowym współzbyciu (zgoda większości serii albo okres ochronny z ceną minimalną), podział ceny według uprzywilejowania | 4.4.1, 4.4.2 brzmienie IV |
| 41 | `127376a` | § 17 ust. 2: dłużnik spłaty (nabywca, solidarnie Spółka), 3-miesięczny termin wskazania nabywcy, ścieżka rezerwowa przez nabycie akcji własnych albo umorzenie przymusowe z przesłanką niewstąpienia | 1.6.1, K5 |
| 42 | `6da7955` | § 17 ust. 2: wstąpienie spadkobierców z akcji za wkład pracy lub usług według § 17 zamiast zgody z art. 300^41 § 2 KSH, proporcjonalne pomniejszenie spłaty | 1.6.1, K6 |
| 43 | `ed16fed` | § 17 ust. 2: większość dla zgody na wstąpienie spadkobiercy liczona bez głosów z akcji spadkowych, uzasadnienie odmowy | 1.6.2 |
| 44 | `574cb13` | § 17 ust. 2a: tryb wezwania spadkobierców i bieg 90 dni, wszczęcie postępowania spadkowego przez Spółkę, stwierdzenie niewstąpienia uchwałą Rady, umorzenie automatyczne (art. 300^46 KSH) wobec spadkobiercy niewspółdziałającego | 1.6.3, K8 |
| 45 | `f016ffa` | § 17 ust. 4: bezwarunkowy termin spłaty (30 dni od ostatecznego ustalenia Wartości Godziwej) i raty na żądanie nabywcy albo Spółki zamiast przesłanki zagrożenia płynności | 1.6.1, K7 |
| 46 | `dc33d4b` | § 18 ust. 3: odpowiednie stosowanie § 11 ust. 15 do małżonka, który nabył akcje bez zgody Spółki i bez spełnienia Kryterium | 1.7.1 |
| 47 | `6bb1b2e` | § 19 ust. 2: Wartość Godziwa jako wynagrodzenie za umorzenie bez zgody akcjonariusza, nie niższe od minimum z art. 300^45 § 2 KSH | 1.8.1 |
| 48 | `47f3d42` | § 19 ust. 4: wspólny wybór Niezależnego Eksperta, rezerwowo przez instytucję neutralną, procedura kontradyktoryjna z terminem 60 dni | 1.8.2, K10 |
| 49 | `83e8405` | § 19 ust. 7: wyjątek oczywistej sprzeczności z zasadami wyceny i tryb ponownej wyceny przez innego Niezależnego Eksperta | 1.8.2, K11 |
| 50 | `3d5f0d1` | § 21 ust. 3: dyrektor niespełniający Kryterium za zgodą WZ 75%, przy większości Rady i Przewodniczącym spełniających Kryterium, dostęp do Kluczowej Własności Intelektualnej według § 27 ust. 6 i § 28 | 1.1.5 |
| 51 | `dcd601e` | § 21 ust. 3-4: wspólna kadencja w latach obrotowych, wygaśnięcie mandatu z powołaniem następcy nie później niż 6 miesięcy po kadencji (art. 300^56 KSH), obowiązek zwołania WZ 3 miesiące przed upływem kadencji | 2.1.1 |
| 52 | `d72a71c` | § 21 ust. 3: wyjątek od Kryterium ograniczony do jednego dyrektora niewykonawczego wskazanego przez Kwalifikowanego Inwestora Finansowego, test sankcyjny, Przewodniczący i dyrektorzy wykonawczy spełniający Kryterium, wyłączenia w regulaminie Rady | 4.4.2, brzmienie V |
| 53 | `4f219d4` | § 21 ust. 6: wyznaczenie dyrektora wykonawczego uchwałą (art. 300^76 KSH), obowiązek dyrektora niewykonawczego, delegacja bez spraw z art. 300^75 § 2-3 KSH i § 23, odwołalna | 2.1.3 |
| 54 | `c52757b` | § 21 ust. 9, § 29 ust. 7: pełny skład Rady jako liczba dyrektorów aktualnie powołanych, dyrektor wyłączony nie liczy się do quorum w danej sprawie | 2.3.2 |
| 55 | `ff191e0` | § 23 ust. 2: wyznaczenie uchwałą dyrektora ds. bezpieczeństwa lub zgodności, tryb do czasu wyznaczenia i przy wyłączeniu lub nieobecności, skutek braku głosu i przedłożenie sprawy WZ | 2.1.2 |
| 56 | `d7d6f77` | § 9 ust. 7, § 18 ust. 1, § 22 ust. 3, § 24 ust. 1, § 29 ust. 12, § 39 ust. 1: usunięcie przekreślonych zdań i ustępów, odesłania w § 24 (ust. 5, ust. 10) i w umowie wykonawczej (§ 39 ust. 3-4, § 24 ust. 2) | 3.4.4, decyzja D4 |
| 57 | `402e224` | § 24 ust. 2: kaskada doręczeń zawiadomień o WZ (e-mail z rejestru, w braku przesyłka polecona albo kurierska), obowiązek podania adresu i zgody przy wpisie, chwila doręczenia, uchwały bez formalnego zwołania | 2.2.2 |
| 58 | `d900f94` | § 24 ust. 2: 7-dniowy termin zgłaszania zmian danych podlegających wpisowi do rejestru akcjonariuszy, w tym istotnych dla Kryterium; § 38 ust. 6: klauzula dostosowawcza do zmian przepisów | 4.3.3 |
| 59 | `4b4b6f1` | § 24 ust. 6-7: regulamin WZ jako podstawa zasad udziału elektronicznego (art. 300^92 § 2 KSH) z regułą przejściową dla zawiadomienia, zastrzeżenie zakresu dopuszczalnego przez prawo przy problemach technicznych | 2.2.1 |
| 60 | `435511a` | § 24 ust. 10-11: zobowiązanie akcjonariusza wyłączonego umownie do niewykonywania głosu, konwersja progu wszystkich głosów na Głosy Uprawnione w Sprawie przy wyłączeniu ustawowym | 2.2.3 |
| 61 | `77da93d` | § 32 ust. 4 lit. f: katalog spraw wymagających zgody większości akcji serii wyemitowanej w Kwalifikowanej Rundzie bez odrębnej uchwały 75%, wygaśnięcie poniżej progu udziału | 4.4.1, 4.4.2 brzmienie VI |
| 62 | `f1ded08` | § 25 ust. 5: uchwały WZ w sprawach Rady jako zgoda, zgody ustawowe (art. 300^81 KSH), umowna zgoda WZ na kredyt, pożyczkę i poręczenie z dyrektorem lub prokurentem, nieruchomości do progu z lit. k bez uchwały WZ; ust. 1 lit. f: wydzierżawienie i obciążenie przedsiębiorstwa | 2.2.4 |
| 63 | `424d7cb` | § 26 ust. 2: obowiązek Założyciela zawarcia pisemnych umów przeniesienia praw (pola eksploatacji, prawa zależne, prawa osobiste, prawa do uzyskania patentu) w dniu umowy i w 30 dni od wpisu Spółki | 3.1.3 |
| 64 | `db993d8` | § 27 ust. 3: przetrwanie obowiązku poufności po utracie statusu akcjonariusza, pisemne zobowiązania dyrektorów niebędących akcjonariuszami i nabywców akcji | 4.2.3 |
| 65 | `a072eb9` | § 27 ust. 6: adresaci zakazu dostępu do Kluczowej Własności Intelektualnej (akcjonariusz, dyrektor, osoba działająca na rzecz Spółki), dodanie EOG, odesłanie do § 28 | 4.2.3 |
| 66 | `1b2b759` | § 28 ust. 1: przykładowe wyliczenie aktów (2021/821, ustawa o obrocie strategicznym, ustawa koncesyjna, środki ograniczające, AI Act w zakresie zastosowania) w brzmieniu obowiązującym | 4.2.1 |
| 67 | `6456051` | § 28 ust. 5: obowiązek zbycia akcji przez akcjonariusza naruszającego kontrolę eksportu na rzecz wskazanego Dopuszczalnego Nabywcy za Wartość Godziwą jako obowiązek związany z akcją | 4.2.1 |
| 68 | `14e540a` | Załącznik nr 3 pkt 4: zakres danych klasyfikacji eksportowej (pozycja wykazu, data, wersja wykazu, osoba odpowiedzialna, wiążące wyjaśnienie) | 4.2.2 |
| 69 | `8ef66e0` | § 29 ust. 8 lit. b: 14-dniowy termin zwołania WZ w celu powołania dodatkowego dyrektora po stwierdzeniu braku zdolności Rady do podjęcia uchwały | 2.3.1 |
| 70 | `59fa2c7` | § 30: usunięcie oznaczenia roboczego [WYMAGA OPINII PRAWNIKA] | 4.3.1, K16 |
| 71 | `8c30ca4` | § 30 ust. 2 i 5: granica wartości godziwej (art. 300^21 KSH) z sankcją zwrotu oraz katalog transakcji z akcjonariuszami wymagających uchwały WZ 75% Głosów Uprawnionych w Sprawie | 2.3.4 |
| 72 | `977b236` | § 31 ust. 4: prawo weta zawężone do sprzeciwu wobec uchwał organów, wyłączenie zwyczajowych kowenantów i postanowień umów o dofinansowanie | 3.3.4 |
| 73 | `39cedfd` | § 32 ust. 3: zobowiązanie do głosowania obejmuje uchwałę o emisji, zmianie umowy, pozbawieniu prawa poboru i uchwały wykonawcze Rundy; umowa wykonawcza § 13 ust. 6-7: kara umowna i nieodwołalne pełnomocnictwo do głosowania | 3.3.1 |
| 74 | `44c7526` | § 32 ust. 4: rozróżnienie warunków inwestorskich wprowadzanych zmianą umowy Spółki (uprzywilejowanie, prawo wskazania dyrektora, zgoda serii z lit. f) od kontraktowych; zgoda właścicielska w uchwale kierunkowej | 3.3.2, K15 |
| 75 | `8b341fa` | § 33 ust. 2a: sposób liczenia łącznego zaangażowania, Limit Zaangażowania zatwierdzany przez WZ, obowiązek informacyjny przed utratą kontroli, reguła kolizyjna z § 25 ust. 1 lit. k i § 31 ust. 5 | 2.4.4 |
| 76 | `ebc4d12` | § 33 ust. 3: własność ulepszeń niewydzielnych, dla pozostałych licencja niewyłączna z sublicencją i prawo pierwszeństwa, wyłączność w granicach prawa konkurencji, dokumentowana ocena Rady | 2.4.1 |
| 77 | `2081146` | § 33 ust. 4: kompetencja Rady do dopuszczenia ograniczonego dostępu partnerów z państw EU001 albo związanych umową o bezpieczeństwie informacji z UE lub NATO; warstwa programowa EDF (art. 9) z uchwałą WZ dla kontroli z państwa niestowarzyszonego | 2.4.2 |
| 78 | `7588070` | § 33 ust. 7: wyjątek od zakazu konkurencji ograniczony (próg 10% i równy udział Spółki, powyżej uchwała WZ z wyłączeniem zainteresowanego, ujawnienie wynagrodzeń, wygaśnięcie z Dniem Odejścia z ofertą udziału dla Spółki, szanse biznesowe); umowa wykonawcza § 10 ust. 4, § 12: dostosowanie | 2.4.3 |
| 79 | `6976954` | § 35 ust. 1 i 3: stwierdzenie Impasu Decyzyjnego przez Radę albo Przewodniczącego, wybór Niezależnego Eksperta przez niezależną instytucję przy wyłączeniu dyrektorów | 3.4.3 |
| 80 | `48f3c13` | § 38 ust. 2: zgoda większości akcji serii na uszczuplenie jej praw i zgoda akcjonariuszy dotkniętych zaostrzeniem obowiązków związanych z akcją | 3.4.2 |
| 81 | `35faad6` | § 38 ust. 5, § 29 ust. 2: dane historyczne Załącznika nr 1 bez aktualizacji, ujawnienia i zgody z Załącznika nr 3 uchwałą WZ bez zmiany umowy z ewidencją Rady | 3.4.1 |
| 82 | `4267f51` | § 38 ust. 7: uchwały założycielskie objęte aktem (pierwsza Rada, podmiot prowadzący rejestr) i reprezentacja Spółki w organizacji | 4.3.1, K18 |
| 83 | `1eb1977` | Załącznik nr 1: rozdzielenie numerów akcji obejmowanych za wkłady niepieniężne (Część A, z wartością wkładu i podstawą wyceny) i pieniężne (Część B), zestawienie łączne | 3.1.4, K13 |
| 84 | `d6108cd` | comments.md: komentarz do zmian 0.9.4-C → 1.0-RC (co, dlaczego, podstawa prawna, orzecznictwo, historia wersji, uwagi niewdrożone) | — |
| 85 | `888e0b3` | Umowa wykonawcza, Załączniki A–B: oferta skierowana do Spółki z prawem wskazania Nabywcy Wskazanego i zobowiązaniem do zbycia (umowa przedwstępna, art. 300^34 § 4 KSH), warunki, wstrzymanie terminu 6 miesięcy, granica 24 miesięcy, niezapłacenie ceny, dopłata, zgoda na wpis, PCC, depozyt; pełnomocnictwo dla Spółki z substytucją, nieodwołalne (art. 101 § 1 KC), z podpisem notarialnie poświadczonym, dom maklerski | 1.5.3 |
| 86 | `ae4636c` | extra.tex: opis emisji serii P zgodny z § 8 (warunkowa emisja) | 3.2.1 |
| 87 | `a4b0b06` | Umowa wykonawcza § 6–7: treść główna zgodna z Załącznikami A–B | 1.5.3 |
| 88 | `31657fd` | Oznaczenie wersji 1.0-RC w psa.tex, shareholder_agreement.tex i extra.tex (strona tytułowa, stopka) | — |
| 89 | (ten commit) | wpis 0.9.4-C → 1.0-RC w `zmiany.md` | — |

## Errata opisów commitów (bez force-push)

- `6870417`: w opisie „§ 33 ust. 2” — zmieniono § 32 ust. 2.
- `d7d6f77`: w opisie „§ 39” — chodzi o § 38.
- `69edc0b`: w opisie „§ 12 ust. 8” — Przeniesienia Dozwolone są w § 12 ust. 9.

## Weryfikacja

`./build.sh` po commicie `31657fd`: psa 57 s., shareholder_agreement 21 s., extra 29 s., psa_feedback 24 s., memorandum 232 s. — 0 błędów, 0 niezdefiniowanych odwołań. `memorandum.tex` opisuje wersję 0.9.4-C (ramki przy tekście sprzed wdrożenia).
