# Rundy poprawek i audytów — umowy Basilisk Systems P.S.A. i Appolonia P.S.A.

Punkt wyjścia: audyt v0 (`audyt.md`, commit `99b14ac`) — 3 ryzyka krytyczne, 5 wysokich, 11 średnich, 7 niskich.

Cykl: **poprawka (U) → audyt nowego tekstu (A)**, trzy razy.

Obie umowy są na gałęzi `psa_simple2`:
- Basilisk Systems: `psa.tex`;
- Appolonia: `appolonia.tex`, przeniesiona z `psa_appolonia` (commit `410f00f`).

Każda zmiana jest wprowadzana w obu umowach jednakowo. Różnią się tylko firmą, siedzibą, przedmiotem działalności (§ 2), § 15 ust. 1 i wariantem cywilnym Appolonii (§ 8 ust. 2 lit. a, § 14 ust. 4, § 17 ust. 3).

---

## Runda 1

### U1 — co zmieniono (Basilisk 2.1-S, Appolonia 1.1-S)

| Ryzyko z audytu v0 | Zmiana | Gdzie |
|---|---|---|
| **K1** pełnomocnik do umów z dyrektorami | Uchwała akcjonariuszy może powołać pełnomocnika do rodzajów umów z dyrektorami (aport IP, umowy wykonawcze vestingu, umowy IP, kwartalne potwierdzenia); pełnomocnikiem nie może być strona umowy. Pełnomocnik wskazywany w uchwałach założycielskich. Umowy z dyrektorem w § 14 i w Załączniku nr 1 podpisuje pełnomocnik. | § 11 ust. 3, § 18 ust. 6, § 14 ust. 1, Załącznik nr 1 |
| **K2** aport IP | Przeniesienie IP w dniu aktu ma pierwszeństwo przed 14-dniowym terminem dla innych wkładów | § 4 ust. 5 |
| **W1** odkup przez Spółkę po cenie emisyjnej | Nabywcą w vestingu nie może być Spółka ani osoba działająca na jej rachunek; usunięty cel „(c)” wykupu; Spółka nie nabywa akcji w wykonaniu obowiązku zbycia | § 9 ust. 4, § 3 ust. 7–8 |
| **W2** nabywca wtórny | Zdarzenia dotyczące pierwotnego Akcjonariusza Funkcjonalnego uruchamiają obowiązek także u nabywcy | § 9 ust. 7 |
| **W3** uchwały obiegowe | Przed terminem uchwała zapada tylko przy większości **wszystkich** głosów w Spółce | § 12 ust. 3 |
| **W4** konflikt interesów | Umowa o Współpracy określa metody cen; spór o cenę rozstrzyga niezależny biegły | § 15 ust. 2 |
| **W5** dominacja | Objęcie lub nabycie akcji spółki siostrzanej wymaga uchwały WZ 75% i zawiadomienia z art. 6 KSH | § 15 ust. 9 (nowy) |
| **Ś1** fikcja zgody | Umowa z podmiotem prowadzącym rejestr: zgłoszenie z dowodem doręczenia i brak odmowy w 14 dni = dowód zgody | § 8 ust. 1 |
| **Ś2** pożyczki dla dyrektorów | Zgoda WZ 75% | § 13 ust. 1 lit. k (nowa) |
| **Ś3** program P a PIT | Regulamin programu zatwierdza WZ | § 7 ust. 5 |
| **Ś4** zakaz konkurencji | Obejmuje Założycieli Pierwotnych i Akcjonariuszy Funkcjonalnych (dopóki są akcjonariuszami) oraz dyrektorów, a nie wszystkich akcjonariuszy | § 14 ust. 5 |
| **Ś5** obowiązek wobec osób trzecich | Obowiązek zawarcia umowy IP ciąży na Spółce (wobec pracowników i współpracowników) i na Założycielach | § 14 ust. 1 |
| **Ś6** art. 41 ust. 3 pr. aut. | Utwory „określone w tej umowie albo w stosunku, w ramach którego twórca działa dla Spółki” | § 14 ust. 1 lit. a |
| **Ś11** Appolonia | Przeniesione poprawki IP z `psa_simple2` (§ 4 ust. 6, § 14 ust. 1–2, § 15 ust. 5) i wszystkie zmiany rundy 1 | `appolonia.tex` |
| **N1** rok obrotowy | Rok kalendarzowy; pierwszy rok może być połączony z następnym (art. 3 ust. 1 pkt 9 UoR) | § 16 ust. 5 (nowy) |
| **N2** zaliczki | Upoważnienie Rady do wypłaty zaliczek na dywidendę | § 16 ust. 4 (nowy) |
| **N3** głos zastawnika | Zastawnik i użytkownik nie głosują (wariant A wzorca S24) | § 3 ust. 9 (nowy) |
| **N4** limit upoważnienia | Upoważnienie do nabycia akcji własnych najwyżej na 5 lat | § 3 ust. 7 |
| **N5** mediacja | Nie wpływa na terminy zaskarżenia uchwał | § 18 ust. 4 |
| **N6** test wypłacalności | Odesłanie do art. 300⁴⁷ § 3 w zw. z art. 300¹⁵ § 4–6 KSH | § 3 ust. 8 lit. e |

**Kontrola techniczna:**
- obie umowy się kompilują (po 24 strony), nierozwiązanych odwołań: 0;
- po usuniętym celu „(c)” nie zostało żadne odwołanie;
- porównanie obu umów: różnice tylko w zamierzonych miejscach.

### A1 — audyt tekstu po rundzie 1

| ID | Ustalenie | Gdzie | Pr. | Kierunek poprawki |
|---|---|---|---|---|
| A1-1 | Brak terminu na wskazanie nabywcy akcji niezwolnionych i brak rozwiązania zastępczego. Akcje mogą pozostawać w zawieszeniu bezterminowo (por. memorandum 1.1.4, luka 1). | § 9 ust. 4 | **W** | Termin 3 miesięcy dla Rady; potem prawo nabycia dla pozostałych Założycieli Pierwotnych; po kolejnych 3 miesiącach obowiązek wygasa |
| A1-2 | Status spółki siostrzanej zależy od tego, czy Założyciele Pierwotni *tej* spółki kontrolują drugą. Przy innym składzie założycieli Appolonii § 15 może się nie uruchomić. | § 15 ust. 1 | **W** | Kryterium: założyciele obu spółek łącznie mają ponad 50% głosów w każdej z nich |
| A1-3 | Licencja na technologię sprzed założenia na 5 lat wygasa po upływie okresu. Bez żądania przeniesienia Spółka traci prawo korzystania. | § 14 ust. 2 | **Ś** | Obowiązek Rady żądania przeniesienia przed upływem okresu i automatyczne przedłużenie licencji |
| A1-4 | Umowa nabycia akcji własnych od dyrektora też jest umową z dyrektorem (art. 300⁷⁹ § 1) i nie ma jej na liście z § 11 ust. 3. Nie wskazano, że uchwała o pełnomocniku może zapaść poza WZ (art. 300⁸⁰), co jest istotne dla kwartalnych potwierdzeń. | § 11 ust. 3 | **Ś** | Dopisać nabycie akcji własnych; uchwała wskazuje osobę i umowy, może zapaść poza WZ |
| A1-5 | „Dowód doręczenia Spółce” bez wskazania adresu doręczeń | § 8 ust. 1 | **Ś** | Adres siedziby albo adres do doręczeń elektronicznych |
| A1-6 | Dokumentacja: `prosta.md` i `analiza_ip_aport.md` odsyłają do „§ 4 ust. 5” dla klauzuli IP (to ust. 6); `prosta.md` nie odzwierciedla zmian 2.1-S (luki S24 zamknięte, wykup bez celu „c”, zakaz konkurencji, § 13 lit. k) | dokumenty | **Ś** | Poprawić odwołania i opis |
| A1-7 | Rok obrotowy oparty na art. 3 ust. 1 pkt 9 UoR — brzmienie przepisu z wiedzy ogólnej | § 16 ust. 5 | **N** | Do pytań dla prawnika i księgowego |
| A1-8 | Bez zmian po rundzie 1: podatki (Ś7–Ś9), Umowa o Współpracy (Ś10), firma i siedziba Appolonii, weryfikacja PKD (N7) | — | — | Poza umową albo decyzje Założycieli |

---

## Runda 2

### U2 — co zmieniono (Basilisk 2.2-S, Appolonia 1.2-S)

| Ustalenie A1 | Zmiana | Gdzie |
|---|---|---|
| **A1-1** vesting bez terminu | Rada wskazuje nabywcę w 3 miesiące od ustania zaangażowania. W braku wskazania pozostali Założyciele Pierwotni mogą nabyć akcje proporcjonalnie w kolejnych 30 dniach. Jeżeli akcji nie zbyto w 6 miesięcy z przyczyn niezależnych od Akcjonariusza Funkcjonalnego, obowiązek wygasa. | § 9 ust. 4 |
| **A1-2** definicja spółki siostrzanej | Status trwa, dopóki założyciele **obu** spółek łącznie mają ponad 50% głosów w każdej z nich | § 15 ust. 1 |
| **A1-3** licencja 5-letnia | Automatyczne przedłużanie o kolejne 5 lat, chyba że Założyciel oświadczy inaczej na rok przed upływem. Wtedy Rada musi przed upływem okresu zażądać przeniesienia, jeśli technologia jest w produktach. | § 14 ust. 2 |
| **A1-4** pełnomocnik | Lista obejmuje nabycie akcji własnych od dyrektora. Uchwała wskazuje osobę i umowy (albo ich rodzaj) i może zapaść poza WZ. | § 11 ust. 3 |
| **A1-5** doręczenie zgłoszenia | Adres siedziby albo adres do doręczeń elektronicznych Spółki | § 8 ust. 1 |
| **A1-6** dokumentacja | `analiza_ip_aport.md`: 5 odesłań „§ 4 ust. 5” poprawionych na ust. 6. `prosta.md` przepisana pod 2.2-S: luki S24 zamknięte, wykup bez vestingu, terminy w vestingu, § 13 lit. k, zakres zakazu konkurencji, definicja spółki siostrzanej, ust. 9 § 15. | dokumenty |

**Kontrola techniczna:** obie umowy się kompilują (po 24 strony), nierozwiązanych odwołań: 0, różnice między umowami tylko w zamierzonych miejscach (34 wiersze, bez zmian względem rundy 1).

### A2 — audyt tekstu po rundzie 2

| ID | Ustalenie | Gdzie | Pr. | Kierunek poprawki |
|---|---|---|---|---|
| A2-1 | **Pętla w vestingu.** Według ust. 7 zdarzenia dotyczące pierwotnego Akcjonariusza Funkcjonalnego uruchamiają obowiązek u każdego nabywcy. Po zbyciu w wykonaniu obowiązku (albo po jego wygaśnięciu lub zwolnieniu przez WZ) można czytać, że obowiązek odżywa u kupującego. Brak też obowiązku wykreślenia wzmianki z rejestru. | § 9 ust. 4, 5, 7 | **W** | Akcje zbyte w wykonaniu obowiązku, zwolnione albo objęte wygaśnięciem przestają być objęte obowiązkiem; Spółka zgłasza zmianę do rejestru |
| A2-2 | **Podatek przy cenie emisyjnej.** Dla sprzedającego organ może szacować przychód (art. 19 PIT); dla kupującego (inny założyciel, uczestnik programu) — przychód z częściowo odpłatnego świadczenia (art. 11 ust. 2b PIT; memorandum 1.5.2, T9 pkt 6). „Uzasadnioną przyczyną” jest mechanizm z umowy spółki, ale trzeba to udokumentować. | § 9 ust. 6 | **Ś** | Umowa wykonawcza wskazuje, że cena wynika z umowy spółki; interpretacja indywidualna przed pierwszym odejściem |
| A2-3 | **Głos zastawnika.** Bezwzględny zakaz może utrudnić finansowanie zabezpieczone na akcjach (bank często żąda głosu po naruszeniu). | § 3 ust. 9 | **N** | Wyjątek za zgodą WZ (75%), przy spełnieniu warunków ustawowych |
| A2-4 | Akcje nabyte przez innego założyciela w wykonaniu obowiązku są wolne. Czy mają wejść do jego vestingu, to decyzja biznesowa — domyślnie nie. | § 9 ust. 4 | **N** | Decyzja Założycieli (bez zmiany) |
| A2-5 | Otwarte decyzje bez zmian: próg odwołania dyrektora (§ 10 ust. 2), czas poufności (§ 14 ust. 3), firma, siedziba i skład założycieli Appolonii, weryfikacja PKD, Umowa o Współpracy, interpretacje podatkowe, dokumenty zależne z „??” | — | — | Poza umową albo decyzje Założycieli |
