# Audyt prawny — umowa Basilisk Systems P.S.A.

**Dokument:** `psa(1)(2).tex`, wersja 3.1-S.  
**Data audytu:** 12 listopada 2026 r.  
**Zakres:** polski tekst, tłumaczenie angielskie, Załącznik nr 1 oraz zgodność z załączonym SHA i wzorami IP. Numery wierszy odnoszą się do otrzymanego pliku źródłowego.

## Co zmieniła nowa wersja

Porównano otrzymaną wersję 3.1-S z wcześniejszą 3.0-S. Zmiana merytoryczna dotyczy § 8 ust. 1 w PL i EN: zniknęła zgoda milcząca i zapis narzucający operatorowi rejestru przyjęcie jej dowodu; dodano dodatkowe wezwanie na 7 dni i odpowiedzialność za zwłokę. Pozostałe postanowienia, w tym procedury uchwał, emisje i vesting, zachowują wcześniejsze brzmienie.

| Zakres | Status po zmianie |
|---|---|
| Dowodzenie zgody milczącej wobec operatora rejestru | Usunięto tę konstrukcję; potrzebny dokument zgody. |
| Akcje niepokryte — PSA-06 | Nadal do poprawy; § 8 ust. 5 wciąż zwalnia z wymagania zgody zbyt szeroko. |
| Uchwały, emisje, vesting i aporty — PSA-01–19 | Ustalenia nadal aktualne, z uaktualnioną oceną § 8. |
| Brak decyzji rady i roszczenia za zwłokę — PSA-20 | Nowe ryzyko: blokada transakcji nie ma określonego końca. |

## Ocena

**Projekt wymaga poprawek przed podpisaniem aktu notarialnego.** Najważniejsze są procedury uchwał, emisje, zbywanie akcji niepokrytych i wykonanie reverse vestingu. Konstrukcja P.S.A., rada dyrektorów, akcje beznominałowe i oddzielenie SHA od umowy spółki są co do zasady odpowiednie.

To analiza projektu, a nie potwierdzenie jego skuteczności przez notariusza lub opiniującego pełnomocnika. Nie otrzymano danych założycieli, wycen, dokumentów nabycia IP, regulaminów ani uchwał wykonawczych. Nie można potwierdzić tytułów do aportów, wartości wkładów, rozliczeń podatkowych ani gotowości do rejestracji.

**Priorytety:** P1 — poprawić przed podpisaniem lub uruchomieniem mechanizmu; P2 — istotne ryzyko wymagające doprecyzowania; P3 — usprawnienie. „Błąd” oznacza konkretną sprzeczność lub brak; „ryzyko” oznacza ocenę zależną od interpretacji lub okoliczności. Nie każdy brak powtórzenia przepisu w umowie jest wadą.

## Ustalenia

### PSA-01 — P1 / błąd: tryb pisemny nie zależy wyłącznie od inicjatora

**Miejsce:** § 12 ust. 1–3, wiersze 277–283; odpowiednik angielski § 12.

Art. 300^80 § 2 KSH odróżnia elektroniczne głosowanie wskazane w umowie spółki od głosowania na piśmie. To drugie wymaga zgody wszystkich akcjonariuszy na ten tryb, wyrażonej w formie dokumentowej. Uprawnienie zwołującego do samodzielnego wyboru obu trybów jest zbyt szerokie. E-mail nie powinien być jednocześnie traktowany jako głos „na piśmie” w rozumieniu formy pisemnej.

**Poprawka:** pozostawić samodzielny wybór głosowania elektronicznego przewidzianego w umowie; głosowanie pisemne uzależnić od zgody wszystkich. Odrębnie opisać podpis własnoręczny/kwalifikowany i formę dokumentową. **Podstawa:** [KSH], art. 300^80; [KC], art. 77^2, 78 i 78^1.

### PSA-02 — P1 / błąd: „cały kapitał akcyjny” zamiast wszystkich akcji

**Miejsce:** § 12 ust. 4, wiersz 284; EN: „entire share capital”.

W P.S.A. akcje nie stanowią części kapitału akcyjnego. Art. 300^90 KSH wymaga reprezentowania **wszystkich akcji**, nie kapitału. To szczególnie istotne przy akcjach za pracę, której wartość nie zasila kapitału.

**Poprawka:** „Uchwały można podjąć mimo braku formalnego zwołania walnego zgromadzenia, jeżeli wszystkie akcje są reprezentowane i spełnione są pozostałe przesłanki art. 300^90 KSH”. Analogicznie poprawić EN. **Podstawa:** [KSH], art. 300^2–300^3, 300^90.

### PSA-03 — P1 / brak: dokumentacja wyłącznie elektroniczna

**Miejsce:** § 12 ust. 8, wiersz 288.

Zapis o prowadzeniu i przechowywaniu dokumentacji elektronicznej nie uwzględnia ustawowej księgi protokołów i art. 300^100 § 4 KSH, przewidującego wydruki uchwał elektronicznych poświadczone podpisem członka organu. Skan lub folder e-mailowy nie zastępuje automatycznie tej procedury.

**Poprawka:** archiwum elektroniczne prowadzić obok dokumentacji wymaganej przez KSH, z podpisanymi protokołami, listami i dowodami zawiadomień. **Podstawa:** [KSH], art. 300^52 i 300^100.

### PSA-04 — P1 / ryzyko rejestrowe: określono termin uchwał, nie termin emisji

**Miejsce:** § 5 ust. 3–5, wiersze 183–190; § 6–7.

Art. 300^103 wymaga maksymalnej liczby akcji i terminu **ich emisji**. Projekt wskazuje 31.12.2036 jako termin podjęcia uchwał. Pozostawia możliwość objęcia i rejestracji akcji znacznie później, co osłabia podstawę korzystania z wyjątku od zmiany umowy spółki.

Ponadto maksymalny pułap nie zastępuje elementów konkretnej zwykłej emisji z art. 300^104. Przy aportach osoby obejmujące akcje i ich przydziały powinny wynikać z uchwały; rada nie może swobodnie wybrać dowolnego aportującego na podstawie ogólnego upoważnienia.

**Poprawka:** wskazać termin emisji, harmonogram subskrypcji i zgłoszenia, a każdej zwykłej emisji nadać wymagane parametry. Zakres elastyczności transz ustalić z notariuszem. **Podstawa:** [KSH], art. 300^103–300^107.

### PSA-05 — P1 / brak rozróżnienia: program P i warunkowa emisja

**Miejsce:** § 7 ust. 2, 4–5, wiersze 212–216; § 5 ust. 5–6.

Projekt przedstawia emisję zwykłą i warunkową jako alternatywne drogi realizacji programu. Tymczasem realizacja praw do objęcia akcji przyznanych umową, o których mowa w art. 300^114 § 2 pkt 2, następuje w trybie warunkowej emisji. Prawa te można przyznać dopiero po rejestracji odpowiedniej zmiany umowy (art. 300^116 § 2). Sam regulamin, uchwała o puli lub zgoda na kategorię umów nie zastępują tej kolejności.

**Poprawka:** rozdzielić bezpośrednie objęcie akcji nowej emisji od przyznawania przyszłych praw opcyjnych. W drugim wariancie: uchwała i wymagane zgody → KRS → przyznanie praw → wykonanie → wpis do rejestru akcjonariuszy. Uchwała warunkowa wymaga również warunków wyłączenia poboru, w tym większości 4/5, a nie samego 75% wszystkich głosów. **Podstawa:** [KSH], art. 300^106 § 2, 300^114–300^118.

### PSA-06 — P1 / ryzyko sprzeczności: zwolnienie ze zgody przy akcjach niepokrytych

**Miejsce:** § 8 ust. 1 i 5, wiersze 223, 234; § 6 ust. 4.

Blankietowe zwolnienie ze zgody przy wykonaniu vestingu pomija art. 300^40 KSH dotyczący akcji nie w pełni pokrytych. Problem będzie realny przy serii F obejmowanej za przyszłą pracę. Umowne odstępstwo od art. 300^39 nie znosi odrębnego reżimu art. 300^40; trzeba również poinformować nabywcę o niepełnym pokryciu i uwzględnić jego solidarną odpowiedzialność ze zbywcą.

**Poprawka:** wyraźnie zastrzec stosowanie art. 300^40, przyjąć osobną udokumentowaną zgodę i informację o pozostałym wkładzie. Zmiana § 8 ust. 1 na zgodę wyraźną nie naprawia wyjątku z ust. 5. **Podstawa:** [KSH], art. 300^39–300^40.

### PSA-07 — P1 / ryzyko ekonomiczne i wykonawcze: odejście założyciela aportującego IP

**Miejsce:** § 4 i § 9 ust. 2–6, wiersze 147–176, 242–247; powiązanie z SHA § 4–5.

Założyciel może przenieść wartościową technologię, a następnie przed pierwszym rokiem stracić wszystkie objęte vestingiem akcje za cenę emisyjną 0,01 zł. Spółka zatrzymuje IP. Dotyczy to również rozwiązania współpracy przez spółkę bez istotnej przyczyny, jeżeli nie zostanie podjęta uchwała zwalniająca. SHA obiecuje głosowanie za ochroną good leavera, ale nie zapewnia automatycznego skutku korporacyjnego.

Nie jest to automatycznie nieważna konstrukcja. Znaczenie mają rzeczywista wycena, świadoma zgoda, powód odejścia i możliwość nadużycia kontroli. Nie wolno jednak przedstawiać jej jako bezpiecznej wyłącznie dlatego, że cenę wpisano do umowy.

**Poprawka:** oddzielić akcje za istniejący aport od akcji motywacyjnych za przyszłe zaangażowanie; określić automatyczne skutki good leaver w umowie spółki; zapewnić możliwość zabezpieczenia sądowego przed transferem. **Podstawa:** [KC], art. 5, 58, 353^1; [KSH], art. 20, 300^101 w zw. z art. 422–425. Ocena skuteczności całego mechanizmu wymaga indywidualnej opinii.

### PSA-08 — P2 / brak: vesting nie daje jednoznacznej liczby i numerów akcji

**Miejsce:** § 9 ust. 2, 4 i 7; Załącznik nr 1 część A.

Niepodzielne akcje mają zwalniać się „w równych częściach”, ale np. 100 000 × 75% / 36 daje ułamek. Brakuje zaokrągleń, przypisania numerów, zasad liczenia miesięcy, urlopów, choroby i przerw. Po transferze do nowego posiadacza trzeba śledzić pierwotnego założyciela i jego datę startu. Brak daty oznacza całkowity brak vestingu — to istotny wybór, nie neutralne puste pole.

**Poprawka:** skumulowana liczba zwolnionych akcji: 0 do 12 miesięcy; następnie `floor(N × m / 48)` dla pełnych miesięcy `12 ≤ m < 48`; w 48. miesiącu N. Wskazać zwalnianie według kolejnych numerów i ewidencję dla każdej transzy. Formuła jest propozycją biznesową, którą trzeba uzgodnić dla pierwszej transzy i przerw. **Podstawa:** [KSH], art. 300^2, 300^33–300^34; [KC], art. 65.

### PSA-09 — P2 / ryzyko: deklarowane obciążenie każdego nabywcy

**Miejsce:** § 9 ust. 6–8 i § 8 ust. 2 lit. d.

Wpis obowiązku w rejestrze wzmacnia jawność, lecz nie zastępuje ważnego ustanowienia obowiązku ani podpisania przez nabywcę SHA, oferty i pełnomocnictwa. Szczególnej analizy wymaga sprzedaż na rzecz osoby trzeciej jako obowiązek „wobec Spółki”, a także egzekucja, dziedziczenie i nabycie przez holding. Nie stwierdzam z góry nieważności, ale sam wpis nie gwarantuje skuteczności wobec każdego nabywcy.

**Poprawka:** uzgodnić konstrukcję z notariuszem i operatorem rejestru; opracować osobne ścieżki sukcesji oraz transferu; dla zwykłych nabywców wymagać pełnego pakietu przystąpienia przed transakcją. **Podstawa:** [KSH], art. 300^33–300^41; [KC], art. 353^1, 393, 922.

### PSA-10 — P2 / ryzyko: zbycie akcji sankcjonowanemu lub konkurencyjnemu nabywcy

**Miejsce:** § 8 ust. 2 i 5; § 9 ust. 4.

Przy zwykłej sprzedaży katalog odmów nie obejmuje samego statusu konkurenta. Po 12 miesiącach akcje zwolnione z vestingu mogą zatem trafić do konkurenta, jeżeli nie zachodzą inne podstawy odmowy. Transfer vestingowy wyłączono ze zgody, choć wybór jego nabywcy również wymaga kontroli prawnej. Sankcje i kontrola inwestycji działają niezależnie od zgody spółki.

**Poprawka:** świadomie zaakceptować otwarty obrót albo zdefiniować konkurenta i proporcjonalną podstawę odmowy. Objąć kontrolą zgodności również nabywcę wskazanego przez radę. Uzyskana zgoda spółki nie zwalnia operatora rejestru z badania dokumentów w granicach ustawowych obowiązków. **Podstawa:** [KSH], art. 300^34, 300^39; przepisy sankcyjne i inwestycyjne wymagają odrębnego badania konkretnej transakcji.

### PSA-11 — P2 / brak: wkład pracy serii F a czteroletni vesting

**Miejsce:** § 6 ust. 4 i 6; § 9 ust. 2.

Czteroletni vesting nie jest sam w sobie zakazany. Nie może jednak automatycznie oznaczać czteroletniego terminu wniesienia wkładu pracy: art. 300^9 § 1, stosowany odpowiednio przy emisji, ustanawia trzyletni termin pełnego wniesienia wkładów. Zaangażowanie po pokryciu akcji może wynikać z odrębnego stosunku.

**Poprawka:** osobno określić wkład i termin jego wykonania oraz czteroletni warunek zatrzymania akcji. Przed emisją przeanalizować ZUS akcjonariusza świadczącego pracę/usługi jako wkład oraz zbiegi ubezpieczeń. **Podstawa:** [KSH], art. 300^3, 300^9, 300^104 § 2; [ZUS].

### PSA-12 — P2 / brak: minimalny kapitał i harmonogram aportu

**Miejsce:** § 4 ust. 5–6; Załącznik nr 1 B–C.

Terminy „14 dni od wpisu” i „najpóźniej w dniu zawarcia umowy” można pogodzić jako zasadę i wyjątek, ale trzeba jednoznacznie przypisać je do składników. Przy umowie IP prawa przechodzą już w dniu podpisania. Spółka w organizacji powstaje dopiero po zawarciu umowy spółki — cesję należy podpisać potem, choćby tego samego dnia. Przed rejestracją musi być rzeczywiście wniesione minimum 1 zł kapitału. Sama łączna cena emisyjna 10 000 zł ani zadeklarowany aport tego nie dowodzą.

**Poprawka:** tabela składnik → wartość → termin przejścia → wydanie → dokument → kwota zaliczona na kapitał. Skreślić niewykorzystane warianty. „Razem wkłady” odróżnić od kapitału faktycznie wniesionego w dniu zgłoszenia. **Podstawa:** [KSH], art. 300^3–300^6, 300^9–300^12.

### PSA-13 — P2 / ryzyko: licencja do wcześniejszej technologii

**Miejsce:** § 14 ust. 2, wiersz 326; § 4 ust. 6.

Nie oznaczono technologii w oddzielnym wykazie ani praw do jej dalszego licencjonowania klientom. Niewyłączna licencja nie daje domyślnie prawa upoważniania osób trzecich (art. 67 ust. 3). Automatyczne kolejne okresy pięcioletnie nie powinny być traktowane jako pewny sposób wyłączenia art. 68 ust. 2. Żądanie cesji za wyceną biegłego nie zapewnia ciągłości produktu, jeżeli przeniesienie będzie przedmiotem sporu.

**Poprawka:** osobna umowa background IP z wykazem, uprawnieniami do modyfikacji i dystrybucji, zasadami sublicencji, wykupu, wyceny i ciągłości licencji klientów. Wyłączyć prawa cudze, których założyciel nie może przenieść. **Podstawa:** [PA], art. 41, 53, 65–68.

### PSA-14 — P2 / brak: progi, kworum i konflikt interesów

**Miejsce:** § 10 ust. 5–8, § 12 ust. 7, § 13 ust. 1.

Wyłączenie dyrektora obniża mianownik kworum, ale nie określono postępowania, gdy konflikt obejmuje wszystkich lub pozostaje tylko jedna osoba. Odesłanie do „aktualnie powołanych” nie rozstrzyga pracy rady poniżej statutowego minimum 3 osób. Progi 100/250/500 tys. zł nie wskazują VAT, waluty, sumowania transakcji powiązanych i czasu trwania zobowiązań. Wcześniejsze zamknięcie głosowania akcjonariuszy wymaga doręczenia projektu wszystkim i zachowania realnych praw udziału; sam rachunek większości nie rozwiązuje tego problemu.

**Poprawka:** procedura uzupełnienia rady, niezależna obsada przy konfliktach, zasady agregacji i przeliczania kwot oraz minimalny czas na głos. Zachować odrębność zgód wewnętrznych od reprezentacji. **Podstawa:** [KSH], art. 17, 300^54–300^58, 300^75–300^79, 300^80–300^100.

### PSA-15 — P2 / niejasność: kupione akcje własne nie stają się serią F lub P

**Miejsce:** § 3 ust. 7–8, § 6–7.

Oferowanie akcji własnych uczestnikom programu jest możliwe w ustawowych granicach. Nabyta akcja A nie zmienia jednak serii przez to, że trafia do funkcjonalnego założyciela. § 9 obejmuje nowego założyciela przede wszystkim przez akcje F, a § 7 definiuje pulę P przez emisje. Możliwe jest ominięcie zamierzonego limitu ekonomicznego programu lub brak vestingu na nabytych A.

**Poprawka:** zdecydować, czy limity obejmują także akcje istniejące i jak ustanawia się na nich obowiązki. Przy zakupie uwzględnić pełne pokrycie, akcje podmiotów zależnych, koszty nabycia i rezerwę. Cena ostatniej transakcji może być nieaktualnym miernikiem wartości; dopuścić korektę wyceny przy zmianie sytuacji spółki. **Podstawa:** [KSH], art. 20, 300^47, 300^98.

### PSA-16 — P2 / podatki: podział B1/B2 wymaga indywidualnej kwalifikacji

**Miejsce:** § 4 ust. 4 i Załącznik nr 1.

Art. 17 ust. 1e PIT rzeczywiście przewiduje nieustalanie przychodu aportowego przy spełnieniu warunków komercjalizowanej IP wnoszonej przez podmiot komercjalizujący. Wpis „B1” i oświadczenie twórcy nie tworzą jednak preferencji. Ogólne „prawo ochronne” jest szersze niż zamknięty katalog z art. 5a pkt 34: nie każde takie prawo, np. do znaku towarowego, kwalifikuje się tak samo. Dokumentacja i sprzęt wymagają oddzielnej analizy.

**Poprawka:** powiązać każdy składnik z konkretną literą definicji, dowodami autorstwa i uprawnienia, wyceną oraz podatkowym kosztem. Zbadać VAT aportu, skutki po stronie spółki i późniejszą sprzedaż akcji; cena 0,01 zł nie rozstrzyga wartości podatkowej. Audyt nie potwierdza indywidualnej neutralności aportów. **Podstawa:** [PIT], art. 5a pkt 34–35, 17 ust. 1 pkt 9 i ust. 1d–1e, 19, 22.

### PSA-17 — P2 / podatki programu: nie traktować wszystkich uczestników jednakowo

**Miejsce:** § 7 ust. 1–2.

W odczytanym tekście PIT z 2026 r. art. 24 ust. 12b przewiduje odpowiednie stosowanie ust. 11–11b także do P.S.A. Nie należy więc opierać decyzji na starszej tezie, że forma P.S.A. sama wyłącza preferencję. Jednocześnie program obejmuje B2B i doradców, a przepis wymaga odpowiedniej kwalifikacji przychodów uczestnika (art. 12 lub 13 PIT) i innych warunków programu.

**Poprawka:** osobne ścieżki dla pracowników, dyrektorów, zleceniobiorców i B2B; sprawdzić moment opodatkowania, obowiązki informacyjne/płatnika i przepisy przejściowe dla dat przyznania. Wniosek o interpretację oprzeć na gotowym regulaminie. **Podstawa:** [PIT], art. 24 ust. 11–12b. Brak regulaminu uniemożliwia końcową ocenę.

### PSA-18 — P2 / niespójność: pierwszy rok obrotowy

**Miejsce:** § 15 ust. 5.

Spółka w organizacji może rozpocząć operacje przed KRS. Ustalenie pierwszego roku wyłącznie według roku rejestracji może prowadzić do rozbieżności z otwarciem ksiąg i rokiem podatkowym. Opcja połączenia lat nie wskazuje jednoznacznie decyzji i konkretnej daty.

**Poprawka:** przed aktem uzgodnić jedną datę końca pierwszego roku, uwzględniając powstanie spółki w organizacji, rozpoczęcie działalności i art. 3 ust. 1 pkt 9 ustawy o rachunkowości. To punkt do potwierdzenia przez księgowego; nie wykonano pełnego audytu rachunkowości. **Podstawa:** [UR], art. 3 ust. 1 pkt 9 i art. 12 ust. 1 pkt 1.

### PSA-19 — P2 / zakres działalności i ochrona informacji

**Miejsce:** § 2 i § 14.

PKD 30.31.Z obejmuje produkcję cywilną, a wojskowe statki powietrzne i drony są wyodrębnione w 30.32.Z. Jeżeli spółka zacznie rzeczywiście taką produkcję, trzeba ponownie dobrać kody i przeanalizować wymagane uprawnienia. Sam klient wojskowy nie rozstrzyga automatycznie klasyfikacji każdego produktu. Zapis o uzyskaniu zezwoleń przed rozpoczęciem działalności jest właściwy.

Nie umieszczać w publicznie składanym akcie haseł, kluczy ani szczegółowego tajnego know-how. Identyfikację aportu oprzeć na wersji, sumie kontrolnej i dostatecznym opisie; szczegółowy materiał przechowywać jako kontrolowany załącznik wykonawczy, z zachowaniem wymogów oznaczenia aportu.

**Podstawa:** [PKD]; [KSH], art. 300^5; [UZK], art. 11. Nie wykonano klasyfikacji eksportowej konkretnych produktów ani badania koncesyjnego.

### PSA-20 — P2 / nowe ryzyko: bezczynność rady blokuje obrót

**Miejsce:** § 8 ust. 1 i 3, wiersze 223 i 232; odpowiedniki EN.

Wersja 3.1-S stanowi, że brak odpowiedzi nie oznacza zgody. Jednocześnie ust. 3 wyłącza obowiązek wskazania innego nabywcy i mechanizm z art. 300^39 § 3–5. Po terminie 14 dni oraz dodatkowych 7 dniach nie uruchamia się inne rozstrzygnięcie. Akcjonariusz może więc pozostawać bez możliwości zakończenia transakcji, mimo że nie zachodzi żadna dozwolona podstawa odmowy. Jest to ryzyko przyjętego ustroju, a nie automatyczna nieważność każdej zgody wymaganej przez umowę.

Zapowiedź odpowiedzialności dyrektorów nie zastępuje uzyskania zgody. Art. 300^125 dotyczy odpowiedzialności wobec spółki; bezpośrednie roszczenie akcjonariusza wymaga właściwej podstawy i wykazania przesłanek, w tym własnej szkody i związku przyczynowego. Nie należy obiecywać, że sam zapis umowy spółki daje od każdego dyrektora automatyczne odszkodowanie za utraconą sprzedaż.

**Poprawka:** wprowadzić rzeczywistą ścieżkę zastępczą, np. kompetencję WZ po bezskutecznym terminie dla rady, termin rozpoznania i sposób zawiadomienia. Alternatywą jest świadomie zaprojektowany skutek upływu terminu, z zastrzeżeniem zgód wymaganych bezwzględnie przez ustawę. Wymaganie dokumentu zgody zachować dla operatora rejestru. Odpowiedzialność dyrektorów opisać przez odesłanie do właściwych podstaw, a dodatkowe zobowiązania ustanawiać w skutecznej formie.

**Podstawa:** [KSH], art. 300^34, 300^39–300^40, 300^125 i 300^134; [KC], art. 415 i nast. oraz — gdy istnieje właściwy stosunek zobowiązaniowy — art. 471.

## Rozwiązania, których nie należy błędnie uznać za wadliwe

- Brak kwotowego określenia kapitału akcyjnego w umowie odpowiada specyfice P.S.A.
- 1 000 000 akcji × 0,01 zł = 10 000 zł; tabela 50/20/10/10/10 i zakresy numerów są arytmetycznie spójne.
- 176 471 akcji P to około 15% przy samym A+P; po pełnej emisji F i P udział P wyniesie około 12,37%. Dokument zastrzega brak innych emisji, więc nie jest to błąd matematyczny.
- 75% wszystkich głosów i 4/5 głosów oddanych to odmienne progi. Przy uchwale łączącej emisję z wyłączeniem poboru trzeba spełnić oba wymagania; nie wystarczy powiedzieć „stosujemy wyższy procent”.
- Wyłączenie obowiązku wskazania alternatywnego nabywcy w § 8 ust. 3 ma podstawę w dyspozytywnym art. 300^39 § 2. Nie traktuję go jako automatycznie nieważnego.
- Zmodyfikowany moment wygaśnięcia mandatu może opierać się na art. 300^56. Trzeba jedynie określić pierwszy i ostatni rok wspólnej kadencji oraz zastępstwa.
- Brak tag-along/drag-along jest wyraźną decyzją biznesową. Udział A=50% daje blokadę spraw wymagających 75% wszystkich głosów, ale nie zapewnia samodzielnej kontroli każdej uchwały.

## Minimalny pakiet przed podpisaniem

1. Poprawić PSA-01–06 w obu językach i uzgodnić z notariuszem emisje, vesting oraz ścieżkę decyzji po bezczynności rady (PSA-20).
2. Uzupełnić wszystkie dane i składniki aportów; potwierdzić faktyczne minimum kapitału.
3. Podpisać prawidłowo reprezentowane SHA, cesje i załączniki; odróżnić istniejące IP od przyszłej pracy.
4. Przygotować uchwały o dyrektorach, operatorze rejestru i pełnomocniku oraz regulamin WZ.
5. Uzgodnić operacyjną procedurę wpisów z prowadzącym rejestr; dopiero potem wydawać oferty i pełnomocnictwa.
6. Sporządzić oddzielną notę podatkową dla każdego aportu i kategorii uczestników programu.

## Stan prawa i źródła

Zweryfikowano tekst podstawowy KSH oraz ogłoszone zmiany z 2026 r. Nowelizacja Dz.U. 2026 poz. 1440 zmienia m.in. formę pełnomocnictwa do udziału w WZ P.S.A.; ta zmiana wchodzi w życie **3.12.2026**, a więc nie obowiązuje jeszcze w dniu audytu. Reforma rejestrów z Dz.U. 2026 poz. 176 w zasadniczej części wchodzi w życie **18.02.2027**; należy przygotować obsługę nowych danych i obowiązków rejestrowych. Nie przeniesiono przyszłych zasad na ocenę obecnego dokumentu. Źródła podatkowe sprawdzono w zakresie wskazanych przepisów; nie wykonano pełnej opinii o podatkach założycieli ani wszystkich nowelizacji podatkowych niezwiązanych z ustaleniami.

- **[KSH]** [Kodeks spółek handlowych — Dz.U. 2024 poz. 18](https://api.sejm.gov.pl/eli/acts/DU/2024/18/text.pdf).
- [Nowelizacja KSH — Dz.U. 2026 poz. 176](https://dziennikustaw.gov.pl/D2026000017601.pdf); [poz. 1440](https://dziennikustaw.gov.pl/D2026000144001.pdf). Sprawdzono też zmiany [poz. 187](https://dziennikustaw.gov.pl/D2026000018701.pdf) i [poz. 644](https://dziennikustaw.gov.pl/D2026000064401.pdf), które nie zmieniają podstaw wskazanych tu ustaleń dotyczących głosowania i obrotu akcjami P.S.A.
- **[KC]** [Kodeks cywilny — Dz.U. 2026 poz. 795](https://api.sejm.gov.pl/eli/acts/DU/2026/795/text.pdf).
- **[PA]** [Prawo autorskie — Dz.U. 2025 poz. 24](https://api.sejm.gov.pl/eli/acts/DU/2025/24/text.pdf); zmiany [Dz.U. 2026 poz. 1296](https://dziennikustaw.gov.pl/D2026000129601.pdf) i [poz. 1477](https://dziennikustaw.gov.pl/D2026000147701.pdf).
- **[PIT]** [Ustawa PIT — Dz.U. 2026 poz. 592](https://api.sejm.gov.pl/eli/acts/DU/2026/592/text.pdf).
- **[PKD]** [GUS — klasyfikacja PKD 2025 i objaśnienia](https://klasyfikacje.stat.gov.pl/static/pkd_25/pdf/KlasyfikacjaPKD2025.pdf).
- **[ZUS]** [ZUS — ubezpieczenia akcjonariuszy P.S.A.](https://bip.zus.pl/pl/web/guest/-/ubezpieczenia-spoleczne-wspolnikow-prostej-spolki-akcyjnej).
- **[UZK]** [Ustawa o zwalczaniu nieuczciwej konkurencji — Dz.U. 2026 poz. 85](https://api.sejm.gov.pl/eli/acts/DU/2026/85/text.pdf), art. 11.
- **[UR]** [Ustawa o rachunkowości — Dz.U. 2026 poz. 522](https://api.sejm.gov.pl/eli/acts/DU/2026/522/text.pdf), art. 3 i 12.
