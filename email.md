# Korespondencja z kancelarią — projekt umowy P.S.A.

## Zasady numeracji

- **Q*n*** — nasze wiadomości do kancelarii (Q1, Q2, …), numerowane chronologicznie.
- **Q*n*.*m*** — kolejne wersje tej samej wiadomości przed wysłaniem (Q1.1, Q1.2, …); wysyłamy ostatnią wersję i oznaczamy ją statusem „wysłano" z datą. Wcześniejsze wersje zostają w pliku.
- Wersję zapisujemy w całości albo jako listę zmian względem wersji poprzedniej („Zmiany względem Q*n*.*m*"); ostatnia wersja w sekcji jest wersją aktualną.
- **R*n*** — odpowiedzi kancelarii; R*n* odpowiada na Q*n*. Jeżeli jedna odpowiedź dotyczy kilku wiadomości, wskazujemy zakres (np. R3 → Q2–Q3); poprawioną odpowiedź kancelarii oznaczamy R*n*.2 itd.
- Każdy wpis zawiera: numer, status, datę, nadawcę i adresata, temat, załączniki (z commitem, z którego pochodzi załączony PDF) oraz dosłowną treść.
- Nowe wpisy i wersje dopisujemy na końcu właściwej sekcji; wcześniejszych nie edytujemy — plik ma zachować pełną historię wymiany.
- Status „projekt" oznacza wiadomość przygotowaną, jeszcze niewysłaną.
- Treść otrzymanych opinii (R*n*) wklejamy również do `psa_feedback.tex`, Część 3, pod tym samym oznaczeniem, wraz ze stanowiskiem Założycieli; `email.md` jest rejestrem korespondencji, `psa_feedback.tex` — miejscem pracy nad opiniami.
- Załącznik do wysyłki (`psa.pdf`) generujemy poleceniem `./build.sh psa` z czystego katalogu; w metadanych wpisu podajemy gałąź i commit, z którego pochodzi.

---

## Q1 — prośba o wycenę weryfikacji projektu umowy

- **Od → do:** Założyciele → kancelaria [nazwa]
- **Temat:** Projekt umowy P.S.A. (Physical AI) — prośba o wycenę weryfikacji
- **Załącznik:** projekt umowy P.S.A. (PDF) — wariant hybrydowy, gałąź `psa_hybrid`, commit `227931c`

### Q1.1

- **Status:** projekt (niewysłany)
- **Data wersji:** 2026-09-21
- **Data wysłania:** —

Szanowni Państwo,

Proszę o wycenę sprawdzenia i niezbędnej modyfikacji załączonego projektu umowy P.S.A. dla startupu z branży Physical AI. Firma jest na etapie przed zawiązaniem; pięciu założycieli — osób fizycznych — obejmuje akcje za wkłady niepieniężne (kod, modele, sprzęt, zgłoszenia patentowe) i pieniężne. Firma będzie rozwijać fizyczną sztuczną inteligencję i autonomiczne systemy bezzałogowe, przede wszystkim roje dronów, o zastosowaniach cywilnych, przemysłowych i — po uzyskaniu koncesji — obronnych. Umowa została zaprojektowana pod rundę inwestycyjną VC, program motywacyjny, dołączanie późniejszych współzałożycieli, udział w spółkach celowych z partnerami przemysłowymi oraz finansowanie dłużne i grantowe.

**1. Jak zbudowana jest umowa**

Część normatywna liczy około 40 stron: tekst umowy (38 paragrafów) oraz trzy załączniki normatywne (założyciele i wkłady, założyciele objęci mechanizmem czasowym, ujawnione aktywności). Osiem dalszych załączników ma charakter wyłącznie informacyjny i nie wymaga weryfikacji; pomocny może być Załącznik nr 9 — roboczy audyt paragraf po paragrafie (stan prawny na 18 sierpnia 2026 r.), nieobejmujący późniejszych zmian tekstu, z wyróżnioną uwagą o pięciu elementach do weryfikacji. System monistyczny (Rada Dyrektorów 3–7 osób). Główne mechanizmy: ograniczenie struktury właścicielskiej do państw UE/EOG/NATO, zgoda Spółki na zbycie akcji w reżimie art. 300³⁹ KSH z 12-miesięcznym lock-upem, prawo pierwszeństwa, tag-along i drag-along, 48-miesięczny mechanizm zwrotnego zbycia akcji założycieli, ograniczenie wstąpienia spadkobierców (art. 300⁴¹ KSH), serie P (program motywacyjny) i F (późniejsi współzałożyciele) na podstawie art. 300¹⁰³ KSH, tryb rundy inwestycyjnej, zasady udziału w spółkach celowych, kontrola eksportu i bezpieczeństwo informacji. Projekt zawiera 58 pól do uzupełnienia danymi, siedem przekreślonych zdań oznaczonych do usunięcia jako powtórzenia ustawy, jeden przekreślony ustęp merytoryczny wraz z odesłaniem do niego (wyjątek dla funduszy inwestycyjnych — pkt 3.1) oraz jeden paragraf (transakcje z akcjonariuszami) oznaczony jako wymagający opinii.

**2. Zakres prac, o którego wycenę prosimy**

A. Przegląd całości części normatywnej pod kątem zgodności z KSH (także po wejściu w życie nowelizacji z 23 stycznia 2026 r.) i innymi właściwymi przepisami — memorandum z klasyfikacją ustaleń (konieczne / zalecane / opcjonalne).
B. Pogłębiona weryfikacja punktów z pkt 3 — stanowisko wraz z proponowanym brzmieniem zmienionych postanowień.
C. Ścieżka zawiązania i rejestracji: forma zawiązania (umowa nie korzysta ze wzorca S24), dokumenty do KRS, dokumentacja wkładów niepieniężnych, podmiot prowadzący rejestr akcjonariuszy, ryzyko zastrzeżeń sądu rejestrowego wobec niestandardowych postanowień.
D. Wdrożenie uzgodnionych zmian i wersja finalna do aktu notarialnego (jedna–dwie iteracje).
E. Opcjonalnie, do odrębnej wyceny: umowa wykonawcza mechanizmu zwrotnego zbycia, regulaminy Rady i programu motywacyjnego, wzory uchwał, wzór umowy spółki celowej, kwestie podatkowe (m.in. interpretacja indywidualna dla programu motywacyjnego w P.S.A.).

Poza zakresem na tym etapie: negocjacje z inwestorami, umowa inwestycyjna, due diligence.

**3. Punkty do weryfikacji**

1) Kryterium bezpieczeństwa UE/NATO wobec nabywców akcji, spadkobierców, małżonków, dyrektorów i partnerów spółek celowych — dopuszczalność na tle KSH, swobód traktatowych UE i przepisów o kontroli inwestycji. Osobno: przekreślony wyjątek dla funduszy inwestycyjnych (siedziba, zarządzający i ośrodek decyzji inwestycyjnych w UE/EOG/NATO zamiast wymogu wobec wszystkich beneficjentów rzeczywistych; test sankcyjny bez zmian) — skłaniamy się do jego usunięcia, prosimy jednak o ocenę, czy jego zachowanie uprościłoby zarządzanie zbyciami wtórnymi i wejściem funduszy bez naruszenia wymogów programów obronnych.
2) Zgoda Spółki na rozporządzenie akcją (art. 300³⁹ KSH) i lock-up wyłączający § 3–6 tego przepisu — granice derogacji.
3) Mechanizm zwrotnego zbycia akcji założycieli — kwalifikacja jako obowiązek związany z akcją, wykonalność przez pełnomocnictwa i umowę wykonawczą, ceny 80 % / 100 % Wartości Godziwej.
4) Dziedziczenie — warunki spłaty spadkobierców niewstępujących, 90-dniowy termin, mechanizm rezerwowy.
5) Rada Dyrektorów — większości przy powołaniu i odwołaniu, przedłużenie mandatu do 6 miesięcy, głos dyrektora ds. zgodności, zastępowanie uchwały Rady uchwałą Walnego Zgromadzenia przy konflikcie interesów.
6) Serie P i F na podstawie art. 300¹⁰³ KSH — uchwała ramowa na transze i jedna uchwała 4/5 o pozbawieniu prawa poboru dla wszystkich transz.
7) Runda inwestycyjna — skuteczność zobowiązań do głosowania oraz przyznawanie warunków inwestorskich (uprzywilejowanie likwidacyjne, antyrozwodnienie) bez zmiany umowy.
8) Transakcje z akcjonariuszami i podmiotami powiązanymi — brak obowiązku przetargu, warunki rynkowe, relacja do procedury konfliktu interesów.
9) Spółki celowe — kompetencje organów z progiem kwotowym, licencja niewyłączna z prawami do ulepszeń dla Spółki (prawo konkurencji, kontrola eksportu), wyłączenie udziału założycieli spod zakazu konkurencji.
10) Klauzule koncesyjne i certyfikacyjne — podstawa z ustawy z 13 czerwca 2019 r., zakres wobec BSP i ich oprogramowania, prawo lotnicze; zasadność ujawnienia kodów wojskowych PKD przed koncesją.
11) Zmiana umowy — tryb aktualizacji załączników normatywnych, brak klauzul zgody indywidualnej, impas przy nieuchwalonej zmianie; przekreślone zdania i spójność definicji.

**4. Prośba o ofertę**

Prosimy o wycenę w podziale na zakresy A–E (ryczałt albo widełki z szacunkiem godzin i stawkami), wskazanie osoby prowadzącej i zespołu, realny termin prac, potwierdzenie braku konfliktu interesów oraz warunki współpracy. Oczekujemy memorandum, proponowanego brzmienia zmian w trybie śledzenia (na życzenie dostarczymy wersję edytowalną), jednego spotkania roboczego i wersji finalnej do aktu notarialnego; zawiązanie spółki planujemy na [miesiąc/rok]. W kolejnych etapach — runda, program motywacyjny, spółki celowe — zależy nam na stałej współpracy.

Załącznik: projekt umowy P.S.A. (PDF).

Z poważaniem,
[imię i nazwisko]
w imieniu Założycieli
[telefon] · [e-mail]

### Q1.2

- **Status:** projekt (niewysłany)
- **Data wersji:** 2026-09-21
- **Data wysłania:** —
- **Załącznik:** projekt umowy P.S.A. (PDF) — `psa_hybrid` @ `111b942`; załączniki informacyjne są od tej wersji wydzielone do `extra.tex` i nie są załączane

Zmiany względem Q1.1 (pozostała treść bez zmian):

1. Sekcja 1, dwa pierwsze zdania → „Załączony projekt liczy około 40 stron: tekst umowy (38 paragrafów) oraz trzy załączniki (założyciele i wkłady, założyciele objęci mechanizmem czasowym, ujawnione aktywności). Materiały informacyjne — m.in. roboczy audyt paragraf po paragrafie (stan prawny na 18 sierpnia 2026 r., nieobejmujący późniejszych zmian tekstu) z wyróżnioną uwagą o pięciu elementach do weryfikacji oraz punkty podatkowe — prowadzimy w odrębnym dokumencie, który prześlemy na życzenie."

### Q1.3

- **Status:** projekt (niewysłany)
- **Data wersji:** 2026-09-21
- **Data wysłania:** —
- **Załącznik:** projekt umowy P.S.A. (PDF) — `psa_hybrid`, plik `psa.tex` (bez dokumentów dodatkowych)
- **Zmiana względem Q1.2:** forma wyniku — pisemne stanowisko zamiast modyfikacji projektu; nowy zakres D (uwagi pod inwestora VC); wdrożenie zmian wyłączone z tego etapu

Temat: Projekt umowy P.S.A. (Physical AI) — prośba o wycenę weryfikacji i pisemne stanowisko

Szanowni Państwo,

Proszę o wycenę sprawdzenia załączonego projektu umowy P.S.A. dla startupu z branży Physical AI oraz o pisemne stanowisko co do jego zgodności z prawem, wykonalności przyjętych mechanizmów i ewentualnych modyfikacji, które uznają Państwo za niezbędne lub wskazane. Firma jest na etapie przed zawiązaniem; pięciu założycieli — osób fizycznych — obejmuje akcje za wkłady niepieniężne (kod, modele, sprzęt, zgłoszenia patentowe) i pieniężne. Firma będzie rozwijać fizyczną sztuczną inteligencję i autonomiczne systemy bezzałogowe, przede wszystkim roje dronów, o zastosowaniach cywilnych, przemysłowych i — po uzyskaniu koncesji — obronnych. Umowa została zaprojektowana pod rundę inwestycyjną VC, program motywacyjny, dołączanie późniejszych współzałożycieli, udział w spółkach celowych z partnerami przemysłowymi oraz finansowanie dłużne i grantowe.

1. Jak zbudowana jest umowa

Załączony projekt liczy około 40 stron: tekst umowy (38 paragrafów) oraz trzy załączniki (założyciele i wkłady, założyciele objęci mechanizmem czasowym, ujawnione aktywności). Materiały informacyjne — m.in. roboczy audyt paragraf po paragrafie (stan prawny na 18 sierpnia 2026 r., nieobejmujący późniejszych zmian tekstu) z wyróżnioną uwagą o pięciu elementach do weryfikacji oraz punkty podatkowe — prowadzimy w odrębnym dokumencie, który prześlemy na życzenie. System monistyczny (Rada Dyrektorów 3–7 osób). Główne mechanizmy: ograniczenie struktury właścicielskiej do państw UE/EOG/NATO, zgoda Spółki na zbycie akcji w reżimie art. 300³⁹ KSH z 12-miesięcznym lock-upem, prawo pierwszeństwa, tag-along i drag-along, 48-miesięczny mechanizm zwrotnego zbycia akcji założycieli, ograniczenie wstąpienia spadkobierców (art. 300⁴¹ KSH), serie P (program motywacyjny) i F (późniejsi współzałożyciele) na podstawie art. 300¹⁰³ KSH, tryb rundy inwestycyjnej, zasady udziału w spółkach celowych, kontrola eksportu i bezpieczeństwo informacji. Projekt zawiera 58 pól do uzupełnienia danymi, siedem przekreślonych zdań oznaczonych do usunięcia jako powtórzenia ustawy, jeden przekreślony ustęp merytoryczny wraz z odesłaniem do niego (wyjątek dla funduszy inwestycyjnych — pkt 3.1) oraz jeden paragraf (transakcje z akcjonariuszami) oznaczony jako wymagający opinii.

2. Zakres prac, o którego wycenę prosimy

A. Zgodność z prawem — przegląd całości części normatywnej pod kątem KSH (także po wejściu w życie nowelizacji z 23 stycznia 2026 r.) i innych właściwych przepisów, z klasyfikacją ustaleń (konieczne / zalecane / opcjonalne).
B. Wykonalność — ocena, czy mechanizmy wymienione w pkt 3 są skuteczne i egzekwowalne w praktyce (rejestr akcjonariuszy, sąd rejestrowy, spory między wspólnikami), i co należałoby zmienić, aby były.
C. Ścieżka zawiązania i rejestracji — forma zawiązania (umowa nie korzysta ze wzorca S24), dokumenty do KRS, dokumentacja wkładów niepieniężnych, podmiot prowadzący rejestr akcjonariuszy, ryzyko zastrzeżeń sądu rejestrowego wobec niestandardowych postanowień.
D. Uwagi pod inwestora VC — które postanowienia w Państwa doświadczeniu budzą zastrzeżenia funduszy inwestujących w Polsce na etapie seed/serii A, co zwykle jest przedmiotem negocjacji i jakie zmiany ułatwiłyby dostosowanie umowy do rundy bez naruszenia jej założeń (bezpieczeństwo właścicielskie, kontrola eksportu, mechanizm zwrotnego zbycia).
E. Opcjonalnie, do odrębnej wyceny: umowa wykonawcza mechanizmu zwrotnego zbycia, regulaminy Rady i programu motywacyjnego, wzory uchwał, wzór umowy spółki celowej, kwestie podatkowe (m.in. interpretacja indywidualna dla programu motywacyjnego w P.S.A.).

Forma wyniku, na której nam zależy: stanowisko w formie pisemnej (memorandum przesłane e-mailem), zawierające ocenę, zidentyfikowane ryzyka i rekomendacje wraz z ewentualnymi propozycjami brzmienia poszczególnych postanowień — jako sugestie do rozważenia. Na tym etapie nie prosimy o wprowadzanie zmian do projektu ani o przygotowanie jego nowej wersji: decyzje co do zmian podejmą Założyciele wspólnie po zapoznaniu się z Państwa stanowiskiem, a wdrożenie uzgodnionych zmian i przygotowanie wersji do aktu notarialnego zlecimy odrębnie. Poza zakresem pozostają także negocjacje z inwestorami, umowa inwestycyjna i due diligence.

3. Punkty do weryfikacji

1) Kryterium bezpieczeństwa UE/NATO wobec nabywców akcji, spadkobierców, małżonków, dyrektorów i partnerów spółek celowych — dopuszczalność na tle KSH, swobód traktatowych UE i przepisów o kontroli inwestycji. Osobno: przekreślony wyjątek dla funduszy inwestycyjnych (siedziba, zarządzający i ośrodek decyzji inwestycyjnych w UE/EOG/NATO zamiast wymogu wobec wszystkich beneficjentów rzeczywistych; test sankcyjny bez zmian) — skłaniamy się do jego usunięcia, prosimy jednak o ocenę, czy jego zachowanie uprościłoby zarządzanie zbyciami wtórnymi i wejściem funduszy bez naruszenia wymogów programów obronnych.
2) Zgoda Spółki na rozporządzenie akcją (art. 300³⁹ KSH) i lock-up wyłączający § 3–6 tego przepisu — granice derogacji.
3) Mechanizm zwrotnego zbycia akcji założycieli — kwalifikacja jako obowiązek związany z akcją, wykonalność przez pełnomocnictwa i umowę wykonawczą, ceny 80 % / 100 % Wartości Godziwej.
4) Dziedziczenie — warunki spłaty spadkobierców niewstępujących, 90-dniowy termin, mechanizm rezerwowy.
5) Rada Dyrektorów — większości przy powołaniu i odwołaniu, przedłużenie mandatu do 6 miesięcy, głos dyrektora ds. zgodności, zastępowanie uchwały Rady uchwałą Walnego Zgromadzenia przy konflikcie interesów.
6) Serie P i F na podstawie art. 300¹⁰³ KSH — uchwała ramowa na transze i jedna uchwała 4/5 o pozbawieniu prawa poboru dla wszystkich transz.
7) Runda inwestycyjna — skuteczność zobowiązań do głosowania oraz przyznawanie warunków inwestorskich (uprzywilejowanie likwidacyjne, antyrozwodnienie) bez zmiany umowy.
8) Transakcje z akcjonariuszami i podmiotami powiązanymi — brak obowiązku przetargu, warunki rynkowe, relacja do procedury konfliktu interesów.
9) Spółki celowe — kompetencje organów z progiem kwotowym, licencja niewyłączna z prawami do ulepszeń dla Spółki (prawo konkurencji, kontrola eksportu), wyłączenie udziału założycieli spod zakazu konkurencji.
10) Klauzule koncesyjne i certyfikacyjne — podstawa z ustawy z 13 czerwca 2019 r., zakres wobec BSP i ich oprogramowania, prawo lotnicze; zasadność ujawnienia kodów wojskowych PKD przed koncesją.
11) Zmiana umowy — tryb aktualizacji załączników normatywnych, brak klauzul zgody indywidualnej, impas przy nieuchwalonej zmianie; przekreślone zdania i spójność definicji.

4. Prośba o ofertę

Prosimy o wycenę w podziale na zakresy A–E (ryczałt albo widełki z szacunkiem godzin i stawkami), wskazanie osoby prowadzącej i zespołu, realny termin przygotowania memorandum, potwierdzenie braku konfliktu interesów oraz warunki współpracy. Zawiązanie spółki planujemy na [miesiąc/rok]. W kolejnych etapach — wdrożenie zmian, runda, program motywacyjny, spółki celowe — zależy nam na stałej współpracy.

Załącznik: projekt umowy P.S.A. (PDF).

Z poważaniem,
[imię i nazwisko]
w imieniu Założycieli
[telefon] · [e-mail]

### Q1.4

- **Status:** projekt (niewysłany)
- **Data wersji:** 2026-09-21
- **Data wysłania:** —
- **Załącznik:** `psa.pdf` zbudowany przez `./build.sh psa` z gałęzi `psa_correction` @ `c200d3c` (po merge PR #1; `psa.tex` identyczny na `psa_hybrid`) — umowa z Załącznikami nr 1–3, 43 strony
- **Nie załączamy:** `extra.pdf` (dokumenty dodatkowe nr 1–6) ani `psa_feedback.pdf` (nasza analiza i miejsce na opinie) — wysyłamy na życzenie

Zmiany względem Q1.3 (pozostała treść bez zmian):

1. Sekcja 1, zdanie o materiałach informacyjnych → „Materiały informacyjne — dokumenty dodatkowe (m.in. proces emisji, proces decyzyjny, punkty podatkowe) oraz naszą analizę projektu z roboczym audytem paragraf po paragrafie (stan prawny na 18 sierpnia 2026 r., nieobejmujący późniejszych zmian tekstu) — prowadzimy w odrębnych dokumentach, które prześlemy na życzenie."

### Q1.5 — wersja aktualna

- **Status:** projekt (niewysłany)
- **Data wersji:** 2026-09-21
- **Data wysłania:** —
- **Załącznik:** `psa.pdf` zbudowany przez `./build.sh psa` z gałęzi `psa_hybrid` @ `55416c7` (twarda bramka Kryterium) — umowa z Załącznikami nr 1–3, 43 strony
- **Nie załączamy:** `extra.pdf` ani `psa_feedback.pdf` — wysyłamy na życzenie; wariant alternatywny (miękka bramka, gałąź `psa_soft`) prześlemy, jeżeli kancelaria zechce porównać brzmienia

Zmiany względem Q1.4 (pozostała treść bez zmian):

1. Sekcja 3, pkt 1) — na końcu dopisać: „Dodatkowo: obowiązki akcjonariusza, który po nabyciu przestał spełniać Kryterium (zawiadomienie Rady, zbycie w 6 miesięcy, w braku zbycia nabywca wskazany przez Spółkę za Wartość Godziwą), oraz wyłączenie z Kryterium osób nabywających akcje na rachunek, w interesie albo na polecenie podmiotu spoza Kryterium (powiernik, pełnomocnik, porozumienie o wykonywaniu praw z akcji)."
2. Sekcja 3, pkt 2) → „Zgoda Spółki na rozporządzenie akcją (art. 300³⁹ KSH): odmowa zgody z powodu Kryterium oraz lock-up założycieli wyłączają § 3–6 tego przepisu, więc Spółka nie ma obowiązku wskazania innego nabywcy, a akcjonariusz może zbyć akcje innemu nabywcy spełniającemu Kryterium — prosimy o ocenę dopuszczalności takiej derogacji na tle art. 300³⁹ § 2 KSH oraz jej skuteczności wobec podmiotu prowadzącego rejestr akcjonariuszy i sądu rejestrowego. Przygotowaliśmy również wariant łagodniejszy: przy odmowie z powodu Kryterium Spółka wskazuje nabywcę w terminie 3 miesięcy za Wartość Godziwą z zapłatą ratalną na zasadach przewidzianych dla spłaty spadkobierców, a w braku nabywcy albo pierwszej raty akcjonariusz zbywa akcje swobodnie. Prosimy o stanowisko, która konstrukcja jest skuteczniejsza i bezpieczniejsza dla Spółki oraz jak obie będą odbierane przez inwestorów; wyboru dokonają Założyciele po zapoznaniu się z Państwa stanowiskiem."
3. Sekcja 3, nowy pkt 12) → „Procedura rozporządzenia akcją — treść zgłoszenia zamiaru rozporządzenia, kolejność zgody Spółki i prawa pierwszeństwa (oferta po uzyskaniu zgody albo równocześnie ze zgłoszeniem), wstrzymanie biegu terminu do czasu uzyskania wymaganej zgody organu (kontrola inwestycji, koncentracja) — zgodność z 14-dniowym terminem i formą dokumentową."
