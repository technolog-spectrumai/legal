# Audyt prawny (stan końcowy po trzech rundach): Basilisk Systems P.S.A. 2.3-S i Appolonia P.S.A. 1.3-S

| | |
|----|----------------|
| **Przedmiot** | 1. Umowa Basilisk Systems P.S.A. — `psa.tex`, wersja 2.3-S. 2. Umowa Appolonia P.S.A. — `appolonia.tex`, wersja 1.3-S. Obie na gałęzi `psa_simple2`, po 18 §, z Załącznikiem nr 1, lustrzane poza firmą, siedzibą, przedmiotem działalności i wariantem cywilnym Appolonii. 3. Konstrukcja spółek siostrzanych (§ 15), konsorcjum, przenoszenie IP. |
| **Przebieg** | Audyt v0 (commit `99b14ac`) → trzy rundy „poprawka → audyt” (U1/A1, U2/A2, U3/A3) → weryfikacja tez A4 (punkt 6). Szczegóły każdej rundy: `audyt_rundy.md`. |
| **Data** | listopad 2026 r. |
| **Stan prawny** | Teksty ujednolicone w `src/legal/`: KSH (t.j. Dz.U. 2024 poz. 18 z późn. zm., w tym zmiany od 18.02.2027 r. z Dz.U. 2026 poz. 176), KC (t.j. Dz.U. 2026 poz. 795), PIT (t.j. Dz.U. 2026 poz. 592 z późn. zm., stan na 16.09.2026 r.), ustawa o rachunkowości (t.j. Dz.U. 2026 poz. 522 z późn. zm.), prawo autorskie (t.j. Dz.U. 2025 poz. 24), rozporządzenie 2021/697 (EDF). Ponadto `memorandum.md` i źródła wskazane w raporcie. |
| **Ocena końcowa** | **W treści obu umów nie zostało ryzyko krytyczne ani wysokie.** Wszystkie 8 ryzyk K i W z audytu v0 oraz 3 ryzyka W wykryte w rundach usunięto w tekście. Zostają ryzyka rezydualne: czynności i dokumenty przy akcie (najważniejsze — uchwała o pełnomocniku i umowy przenoszące IP), podatki i decyzje biznesowe (punkt 1.3). Weryfikacja A4 (punkt 6) potwierdziła większość tez i wykazała trzy kwestie poza treścią umów: wzajemną dominację spółek przy wspólnych dyrektorach (z zakazem obejmowania akcji drugiej spółki), stosowanie art. 15 KSH do dyrektorów P.S.A. oraz podatek od aportu IP płatny bez gotówki. |

**Weryfikacja źródeł.** W tym środowisku nie było dostępu do ISAP, portalu orzeczeń SN, SAOS, CBOSA ani systemów Legalis/LEX. Teksty ustaw pobrane wcześniej z ISAP i EUR-Lex leżą w `src/legal/` i na nich oparto weryfikację A4.

| Znak | Znaczenie |
|--|------------------|
| **[Z]** | Zweryfikowane na tekście przepisu albo orzeczenia — w `src/legal/` (teksty ujednolicone), `memorandum.md` lub `psa_feedback.tex` (z linkami do sn.pl i eli.gov.pl) |
| **[S]** | Potwierdzone wyszukiwaniem w toku audytu: istnienie, sygnatura, data i teza według baz orzeczeń lub komentarzy. Pełnego tekstu uzasadnienia nie czytano. |
| **[W]** | Wiedza ogólna albo wniosek audytora — do potwierdzenia przez prawnika |

Raport nie zastępuje opinii adwokata, radcy prawnego ani doradcy podatkowego.

---

## 1. Wnioski

### 1.1. Bilans rund

| Runda | Wersje | Co załatwiła | Co wykrył audyt po niej |
|---|---|---------|----------|
| v0 | 2.0-S / 1.0-S | — | 3 ryzyka K, 5 W, 11 Ś, 7 N |
| **U1 → A1** | 2.1-S / 1.1-S | Wszystkie K i W z v0 w treści umów; Ś1–Ś6, Ś11; N1–N6; Appolonia dostała poprawki IP | 2 W: brak terminu w vestingu, wąska definicja spółki siostrzanej; 4 Ś: licencja 5-letnia, lista umów pełnomocnika, adres doręczenia, błędne odesłania w dokumentacji |
| **U2 → A2** | 2.2-S / 1.2-S | Wszystkie ustalenia A1 | 1 W: pętla w vestingu po zbyciu w wykonaniu obowiązku; 1 Ś: podatek przy cenie emisyjnej; 1 N: sztywny zakaz głosu zastawnika |
| **U3 → A3** | 2.3-S / 1.3-S | Wszystkie ustalenia A2 | Brak nowych ryzyk K i W w treści; ryzyka rezydualne (punkt 1.3) |
| **A4** | bez zmian | Weryfikacja tez na tekstach ustaw i w wyszukiwaniu (punkt 6) | 3 kwestie poza treścią umów (A4-1 – A4-3), propozycja doprecyzowania § 15 ust. 9, korekta tezy o art. 15 KSH |

### 1.2. Co jest dobrze

- **Ustrój i forma.** Rada Dyrektorów, reprezentacja łączna, uchwały poza WZ i udział zdalny są zgodne z KSH (art. 300⁷³–300⁷⁹, 300⁸⁰, 300⁹² **[Z]**). Forma aktu notarialnego jest konieczna, bo aport niepieniężny wyklucza S24 (art. 300⁶ § 1 **[Z]**).
- **Reprezentacja w umowach z dyrektorami.** Umowy założycieli-dyrektorów ze Spółką podpisuje pełnomocnik z uchwały akcjonariuszy (art. 300⁷⁹ § 1 **[Z]**): aport IP, umowy IP, kwartalne potwierdzenia, umowy wykonawcze vestingu, wykup akcji od dyrektora (§ 11 ust. 3, § 14 ust. 1, § 18 ust. 6, Załącznik nr 1). Pełnomocnika do rodzaju umów SN dopuścił przy analogicznym art. 210 § 1 KSH (III CZP 71/18 **[S]**).
- **Tytuł do IP.** Aport IP przenoszony w dniu aktu, z licencją tymczasową i egzekucją w naturze (art. 64 KC; SN II CSKP 593/22 **[Z]**). Ustawowe elementy umowy przeniesienia (art. 41, 46, 50, 53, 74 pr. aut. **[Z]**) są wpisane wprost. Kwartalne potwierdzenia dotyczą utworów już istniejących, co omija art. 41 ust. 3.
- **Vesting** bez udziału Spółki jako nabywcy, więc bez ryzyka obejścia art. 300⁴⁵ § 2 KSH (memorandum 1.5.2 **[Z]**):
  - terminy: 3 miesiące, potem 30 dni dla pozostałych założycieli, łącznie najwyżej 6 miesięcy;
  - jasny koniec obowiązku i wykreślenie wzmianki z rejestru;
  - skuteczność wobec nabywców wtórnych (memorandum 1.5.1 **[Z]**).
- **Ograniczenia zbywania:**
  - zamknięty katalog przyczyn odmowy;
  - wyłączenie art. 300³⁹ § 3–5 (memorandum 1.2.1: „zgodne warunkowo” **[Z]**);
  - lock-up 12 miesięcy;
  - fikcja zgody z mechanizmem dla podmiotu prowadzącego rejestr.
- **Spółki siostrzane.** § 15 wyłącza zakaz konkurencji, poufność i konflikt interesów w granicach prawa. Wymaga Umowy o Współpracy zatwierdzonej przez WZ, cen rynkowych z niezależnym biegłym, zgody WZ na udziały w siostrze (dominacja, art. 6 KSH). Działa także przy częściowo różnym składzie założycieli.
- **Parytet z S24:** rok obrotowy, zaliczki, głos zastawnika są uregulowane.

### 1.3. Rejestr ryzyk — stan końcowy

| ID | Ryzyko | Status | Ryzyko rezydualne |
|--|---------|---------|--------|
| **K1** | Umowy z założycielami-dyrektorami bez pełnomocnika — nieważność | Usunięte w treści (U1, U2). **Do wykonania:** uchwała o pełnomocniku w akcie i podpisy pełnomocnika. | N — pełnomocnika „rodzajowego” dopuszcza SN III CZP 71/18 przy art. 210 § 1 KSH **[S]**, który ma tę samą konstrukcję co art. 300⁷⁹ § 1 **[Z]** (A4) |
| **K2** | Aport IP niewniesiony | Usunięte w treści (U1). **Do wykonania:** komplet umów przeniesienia z wykazami w dniu aktu. | **Ś** — zależy od wykonania (punkt 5) |
| **K3** | Wycena wkładów | Poza treścią — Załącznik nr 1 do wypełnienia | **Ś** — art. 300¹⁰ KSH, spójność z PIT |
| W1 | Odkup przez Spółkę po cenie emisyjnej | Usunięte (U1) | N |
| W2 | Nabywca wtórny w vestingu | Usunięte (U1, U3) | N |
| W3 | Wczesne zamykanie uchwał obiegowych | Usunięte (U1) | N |
| W4 | Konflikt interesów z Appolonią | Ograniczone (U1): WZ, formuły, biegły | **Ś** — ustawowy obowiązek wstrzymania się (art. 300⁵⁵ § 1) zostaje; realny po rozejściu się akcjonariatu |
| W5 | Dominacja przez unię personalną | Ograniczone (U1): akcje siostry tylko za zgodą WZ, zawiadomienie z art. 6 | **Ś** — A4: przy wspólnych dyrektorach spółki są wzajemnie dominujące niezależnie od udziałów (art. 4 § 1 pkt 4 lit. d, § 2¹, § 5 KSH **[Z]**); zob. A4-1 |
| A1-1 | Vesting bez terminu | Usunięte (U2) | N |
| A1-2 | Definicja spółki siostrzanej | Usunięte (U2) | N |
| A2-1 | Pętla w vestingu | Usunięte (U3) | N |
| **A4-1** | Wzajemna dominacja przy wspólnych dyrektorach: zawiadomienia z art. 6 § 1, zgoda WZ spółki dominującej na pożyczkę spółki zależnej dla jej dyrektora (art. 15 § 2), zakaz obejmowania akcji drugiej spółki (art. 300⁴⁸ § 1), nabycie jej akcji jako akcji własnych (art. 300⁴⁷ § 9) **[Z]** | Nowe (A4), poza treścią umów; § 15 ust. 9 do doprecyzowania (punkt 6.3) | **Ś** — Rady, w których wspólni dyrektorzy stanowią najwyżej połowę, albo przestrzeganie skutków dominacji |
| **A4-2** | Art. 15 § 1 KSH obejmuje dyrektora P.S.A. (art. 4 § 2¹ **[Z]**); bez zgody WZ umowa jest nieważna, zgoda możliwa do 2 miesięcy po czynności (art. 17 § 1–2 **[Z]**) | Umowy zgodne (§ 13 lit. k); błąd był w `memorandum.md` 2.2.4 i w audycie | N |
| **A4-3** | Prawo autorskie po noweli: godziwe wynagrodzenie (art. 43 ust. 2–3), podwyższenie przez sąd (art. 44), informacja o przychodach (art. 47¹). Nie dotyczą programów komputerowych (art. 77 ust. 1), dotyczą dokumentacji, projektów i grafik **[Z]** | Umowy zgodne (§ 14 ust. 1 lit. d) | N — pilnować w umowach o pracę i B2B |
| Ś1 | Fikcja zgody a rejestr | Ograniczone (U1, U2): obowiązek w umowie z podmiotem prowadzącym rejestr | N — do uzgodnienia z podmiotem przed aktem; A4: brak orzeczeń i komentarzy, tekst art. 300³⁹ § 1 jej nie wyklucza **[Z]** |
| Ś6 | Art. 41 ust. 3 pr. aut. | Ograniczone (U1): utwory „w ramach zadań”, kwartalne potwierdzenia | N — A4: przepis unieważnia umowę co do wszystkich utworów (danego rodzaju) **[Z]**, nie co do utworów w ramach zadań **[S]** |
| Ś7–Ś9, A2-2 | Podatki: aport IP, licencje nieodpłatne, cena emisyjna w vestingu, seria F za pracę, ceny transferowe | Ograniczone (U1, U3: dokumentacja ceny) | **Ś** — A4: mechanika potwierdzona na tekście PIT; aport IP i seria F są opodatkowane w dniu wpisu, bez gotówki; interpretacje indywidualne nadal wskazane (punkt 6) |
| Ś10 | Umowa o Współpracy nie istnieje | Poza treścią | **Ś** — bez niej § 15 nie daje licencji ani rozliczeń |
| Ś11 | Appolonia | Poprawki przeniesione (U1–U3) | **Ś** — firma („Appolonia”/„Apollonia”), siedziba, skład założycieli, PKD |
| N7 | Kody PKD 2025 | Poza treścią | N — sprawdzić przed wnioskiem do KRS |
| — | Decyzje Założycieli: próg odwołania dyrektora (§ 10 ust. 2), czas poufności (§ 14 ust. 3), vesting dla akcji nabytych od odchodzącego (A2-4) | Do decyzji | — |
| — | Dokumenty zależne `extra.tex`, `psa_feedback.tex`, `shareholder_agreement.tex`, `uchwaly.tex` z odwołaniami „??” | Poza zakresem (zgodnie z poleceniem, dokumentacji nie zmieniano) | — |

---

## 2. Umowy — analiza postanowień (stan 2.3-S / 1.3-S)

Poniżej tylko to, co istotne dla oceny prawnej. Numeracja jest taka sama w obu umowach.

### § 1–2. Firma, siedziba, przedmiot działalności

- **Ocena:** zgodne.
- **Podstawa:** art. 300⁵ § 1 KSH **[Z]**.
- **Uwagi:**
  - zakres Basilisk („na lądzie i w powietrzu”) i Appolonii („morze i wody śródlądowe”) się nie pokrywa, co jest podstawą § 15 i zakazu konkurencji;
  - kody PKD 2025 do weryfikacji (N7);
  - firma i siedziba Appolonii do uzupełnienia.

### § 3. Akcje, rejestr, akcje własne, zastaw

- **Ocena:** zgodne.
- **Podstawa:** art. 300³¹, 300³³–300³⁴, 300⁴⁷ § 1 pkt 2, § 2–3 i § 9, art. 300¹⁵ § 2 i 4–6 KSH **[Z]**.
- **Uwagi:**
  - wykup akcji własnych tylko w celu umorzenia albo dla programu P i serii F, upoważnienie najwyżej na 5 lat (ustawa takiego limitu w P.S.A. nie przewiduje — memorandum 1.3.5 **[Z]**);
  - Spółka nie nabywa akcji w vestingu;
  - zastawnik i użytkownik nie głosują; wyjątek za zgodą WZ (75%) dla zastawu zabezpieczającego finansowanie Spółki, przy spełnieniu warunków ustawowych.

### § 4. Objęcie akcji i wkłady

- **Ocena:** zgodne, pod warunkiem wykonania czynności przy akcie (K1, K2) i wyceny (K3).
- **Podstawa:**
  - KSH: art. 300² § 1–2, art. 300³, art. 300⁵ § 1 pkt 4, art. 300⁹, art. 300¹⁰, art. 300¹¹, art. 300¹² § 3, art. 300¹²³, art. 300¹²⁴, art. 587 § 1, art. 14 **[Z]**;
  - prawo autorskie: art. 41 ust. 2–4, art. 46, art. 53, art. 74 ust. 4 **[Z]**;
  - art. 64 KC **[Z]**.
- **Orzecznictwo:**
  - SN II CSKP 593/22 **[Z]** — wyrok zastępuje oświadczenie potrzebne do wykonania istniejącego obowiązku;
  - SN I CK 381/05, III CK 124/05 **[S]** — pola eksploatacji muszą być wymienione wyraźnie i znane w chwili umowy.
- **Uwagi:**
  - ust. 6 jest kompletny: forma, pola eksploatacji, prawa zależne, współtwórcy, wynagrodzenie = akcje, licencja tymczasowa, wykonanie w naturze;
  - ust. 5 rozstrzyga kolejność: IP w dniu aktu, pozostałe wkłady niepieniężne do 14 dni po wpisie.

### § 5–7. Emisje, seria F, seria P

- **Ocena:** zgodne.
- **Podstawa:** art. 300¹⁰³–300¹⁰⁷, 300¹¹⁴–300¹¹⁸ (memorandum), art. 300² § 2 („świadczenie pracy lub usług” jako wkład niepieniężny), art. 300¹⁰⁴ § 1 pkt 7 **[Z]**.
- **Uwagi:**
  - regulamin programu P zatwierdza WZ (§ 7 ust. 5); preferencja z art. 24 ust. 11–11b PIT obejmuje program motywacyjny P.S.A. (art. 24 ust. 12b PIT **[Z]**);
  - seria F za pracę: przychód z art. 17 ust. 1 pkt 9 PIT powstaje w dniu wpisu emisji (ust. 1a pkt 2 **[Z]**), czyli przed wykonaniem pracy; kwalifikację potwierdzić interpretacją (punkt 6).

### § 8. Zbywanie

- **Ocena:** zgodne warunkowo.
- **Podstawa:** art. 300³⁹ § 1–6, art. 300³⁴ § 6 KSH **[Z]**.
- **Orzecznictwo:**
  - SN II CRN 60/93 **[S]** — bezskuteczność zawieszona przy braku zgody; zgoda działa wstecz;
  - SN V CSK 274/21 **[S]** i SA w Gdańsku V AGa 158/20 **[S]** — tak samo;
  - SN I CSK 132/11 **[S]** — skutki zależą od rodzaju ograniczenia.

  Orzeczenia dotyczą sp. z o.o. (art. 182 KSH, ta sama klauzula dyspozytywna co art. 300³⁹ § 2 — memorandum 1.2.1 **[Z]**); stosowanie do P.S.A. przez analogię **[W]**.

- **Uwagi:**
  - fikcja zgody po 14 dniach jest wsparta zaświadczeniem i obowiązkiem w umowie z podmiotem prowadzącym rejestr (adres doręczenia: siedziba albo adres do doręczeń elektronicznych);
  - wyłączenie art. 300³⁹ § 3–5 jest do obrony, bo każda przyczyna odmowy jest przejściowa albo usuwalna (art. 58 § 2, art. 353¹ KC **[Z]**).
  - A4: nie znaleziono orzeczeń ani komentarzy o fikcji zgody. Art. 300³⁹ § 1 pozwala ograniczyć rozporządzenie akcją „w inny sposób” **[Z]**, więc tekst przepisu jej nie wyklucza; praktykę trzeba uzgodnić z podmiotem prowadzącym rejestr.

### § 9. Obowiązek zbycia (vesting)

- **Ocena:** zgodne.
- **Podstawa:**
  - KSH: art. 300¹ § 3, art. 300³³ § 1 pkt 10–11, art. 300³⁹ § 1, art. 300⁴⁵ § 1–2, art. 300⁴⁷ § 9 **[Z]**;
  - art. 64 i 101 § 1 KC **[Z]**;
  - PIT: art. 17 ust. 2, art. 19, art. 11 ust. 2b **[Z]**.
- **Orzecznictwo:** SN V CSK 522/18 **[Z]**, SN II CSKP 593/22 **[Z]**.
- **Uwagi:**
  - nabywca to osoba wskazana przez Radę (nie Spółka); w braku wskazania — pozostali założyciele; po 6 miesiącach obowiązek wygasa;
  - akcje zbyte, zwolnione albo z wygasłym obowiązkiem przestają być nim objęte, a Spółka zgłasza to do rejestru;
  - umowa wykonawcza dokumentuje źródło ceny. Organ przyjmuje wartość rynkową tylko wtedy, gdy cena „bez uzasadnionej przyczyny” znacznie od niej odbiega, i najpierw wzywa do wskazania przyczyn (art. 19 ust. 1 i 4 PIT **[Z]**). Po stronie nabywcy ryzykiem jest świadczenie częściowo odpłatne (art. 11 ust. 2b **[Z]**; interpretacji nie znaleziono);
  - umowę wykonawczą z założycielem-dyrektorem podpisuje pełnomocnik.

### § 10–11. Rada Dyrektorów i reprezentacja

- **Ocena:** zgodne.
- **Podstawa:** art. 300⁵⁵ § 1, 300⁵⁸ § 2, 300⁷³, 300⁷⁵–300⁷⁶, 300⁷⁹ § 1–4, art. 4 § 2¹, art. 15 § 1, art. 17 § 1–3 KSH, art. 39 KC **[Z]**; art. 300¹²⁵ § 2 (BJR) **[S]**.
- **Orzecznictwo:**
  - SN III CZP 71/18 **[S]** — pełnomocnik z art. 210 § 1 KSH może mieć umocowanie do konkretnej umowy, konkretnego sporu albo rodzajowe; powołuje go uchwała wspólników;
  - SN II CSKP 1733/22 **[S]** — umowa z członkiem zarządu zawarta z naruszeniem art. 210 KSH jest nieważna (art. 58 § 1 KC); glosa zarzuca pominięcie art. 39 § 1 KC;
  - SN II CSK 744/11 **[S]** — przed zmianą art. 39 KC (1.03.2019 r.) czynność „fałszywego organu” była nieważna bez możliwości konwalidacji.
- **Uwagi:**
  - pełnomocnik do rodzajów umów, wskazywany w uchwale (może zapaść poza WZ — art. 300⁸⁰ **[Z]**), nie może być stroną umowy;
  - **ryzyko rezydualne (zmniejszone w A4):**
    - art. 300⁷⁹ § 1 ma tę samą konstrukcję co art. 210 § 1 KSH **[Z]**, więc teza III CZP 71/18 odnosi się do niego przez analogię **[W]**; wskazywanie rodzajów umów (§ 11 ust. 3) ma oparcie w orzecznictwie;
    - art. 39 § 1 KC **[Z]** („ważność umowy zależy od jej potwierdzenia”) daje argument za konwalidacją umowy podpisanej bez pełnomocnika, ale jego stosowanie do art. 210 jest sporne (sprawa SN I CSK 459/25 — wyniku nie ustalono).

### § 12. Uchwały akcjonariuszy

- **Ocena:** zgodne.
- **Podstawa:** art. 300⁸⁰ § 1–3, art. 300⁹² KSH **[Z]**.
- **Uwagi:**
  - uchwała obiegowa zapada przed terminem tylko przy wymaganej większości **wszystkich** głosów, więc późniejsze głosy nie mogą zmienić wyniku;
  - regulamin WZ przyjmowany przy zawiązaniu.

### § 13. Sprawy zastrzeżone

- **Ocena:** zgodne.
- **Uwagi:**
  - 11 pozycji (75% wszystkich głosów), w tym Umowa o Współpracy (lit. j) i umowy finansowe z dyrektorami (lit. k);
  - **korekta A4:** art. 15 § 1 KSH obejmuje dyrektora P.S.A., bo art. 4 § 2¹ KSH każe rozumieć „członka zarządu” jako dyrektora **[Z]**. Umowa bez zgody WZ jest nieważna; zgodę można wyrazić do 2 miesięcy po czynności, z mocą wsteczną (art. 17 § 1–2 **[Z]**);
  - lit. k jest więc zgodna z ustawą i podnosi większość do 75%. Uchwała, która nie osiąga tylko progu umownego, nie unieważnia umowy, ale rodzi odpowiedzialność dyrektorów (art. 17 § 3 **[Z]**).

### § 14. Własność intelektualna, poufność, eksport, konkurencja

- **Ocena:** zgodne.
- **Podstawa:**
  - prawo autorskie: art. 9, 12, 16, 41, 43, 44, 46, 47¹, 50, 53, 74, 77 ust. 1 **[Z]**; art. 67 ust. 5, art. 68 **[S]**;
  - PWP: art. 11 ust. 3 **[Z]**;
  - KSH: art. 300¹ § 3 **[Z]**.
- **Orzecznictwo:** SN I CSKP 62/21, SA w Warszawie VI ACa 1735/14 (licencja dorozumiana), SN II CK 51/04 (art. 68) **[S]**.
- **Uwagi:**
  - obowiązek umów IP ciąży na Spółce wobec pracowników i współpracowników oraz na Założycielach;
  - licencja na technologię sprzed założenia przedłuża się automatycznie; przy odmowie przedłużenia Rada żąda przeniesienia;
  - zakaz konkurencji obejmuje założycieli, Akcjonariuszy Funkcjonalnych (dopóki są akcjonariuszami) i dyrektorów;
  - licencja nieodpłatna — ryzyko podatkowe (Ś7).
  - A4: art. 43, 44 i 47¹ nie dotyczą programów komputerowych (art. 77 ust. 1 **[Z]**). Do dokumentacji, projektów i grafik stosuje się je w pełni: wynagrodzenie musi być „godziwe” (art. 43 ust. 2), twórca może żądać jego podwyższenia przez sąd (art. 44) i informacji o przychodach (art. 47¹, z wyjątkiem nieznacznego wkładu twórczego). § 14 ust. 1 lit. d wymaga określenia wynagrodzenia albo wskazania, że jest zawarte w wynagrodzeniu z pracy lub B2B — to wystarcza.

### § 15. Współpraca ze Spółką Siostrzaną — punkt 3.

### § 16–18. Zysk, likwidacja, postanowienia końcowe

- **Ocena:** zgodne.
- **Uwagi:**
  - zaliczki na dywidendę (ust. 4) z testem wypłacalności;
  - rok obrotowy (ust. 5) zgodny z art. 3 ust. 1 pkt 9 ustawy o rachunkowości **[Z]**: rok obrotowy określa umowa, a jednostka, która rozpoczęła działalność w drugiej połowie roku, może połączyć księgi i sprawozdanie z rokiem następnym;
  - mediacja nie wpływa na terminy zaskarżenia uchwał;
  - uchwały założycielskie obejmują pełnomocnika do umów z dyrektorami.

---

## 3. Struktura Basilisk–Appolonia

- **Konstrukcja § 15.** Dopuszczalna jako postanowienia umów spółek (art. 300¹ § 3 KSH, art. 353¹ KC **[Z]**).
  - Status trwa, dopóki założyciele obu spółek łącznie mają ponad 50% głosów w każdej z nich.
  - Wyłączenia zakazu konkurencji i poufności są skuteczne, bo te obowiązki wynikają z samej umowy.
- **Konflikt interesów (Ś rezydualne).**
  - Ustawowego obowiązku ujawnienia i wstrzymania się (art. 300⁵⁵ § 1 **[Z]**) umowa nie uchyli. Ochrona BJR (art. 300¹²⁵ § 2 **[S]**) zakłada lojalność.
  - Zabezpieczenia: Umowa o Współpracy zatwierdzona jednomyślnie przez WZ obu spółek, póki akcjonariat jest identyczny; metody cen; niezależny biegły.
  - Przy wejściu inwestora do jednej spółki potrzebny jest przegląd tych zabezpieczeń.
- **Dominacja (A4, zweryfikowane na tekście KSH **[Z]**).**
  - Spółka jest dominująca, gdy „członkowie jej zarządu stanowią więcej niż połowę członków zarządu” innej spółki kapitałowej (art. 4 § 1 pkt 4 lit. d). W P.S.A. z radą dyrektorów „zarząd” oznacza radę dyrektorów (art. 4 § 2¹).
  - Przy wspólnych dyrektorach warunek działa w obie strony. Kryteria z art. 4 § 3–4 tego nie rozstrzygają, więc obie spółki są „wzajemnie dominującymi i zależnymi” (art. 4 § 5). Wzajemne udziały nie są do tego potrzebne.
  - Skutki:
    - zawiadomienie w 2 tygodnie od powstania dominacji (art. 6 § 1). Sankcją jest zawieszenie głosu z akcji powyżej 33% „kapitału zakładowego”, czyli w P.S.A. 33% wszystkich akcji (art. 4 § 2² pkt 1). Bez wzajemnych akcji sankcja nie działa, ale obowiązek istnieje;
    - umowa kredytu, pożyczki albo poręczenia spółki zależnej z dyrektorem spółki dominującej wymaga zgody WZ spółki dominującej (art. 15 § 2);
    - spółka zależna nie może obejmować akcji spółki dominującej (art. 300⁴⁸ § 1 zd. 2). Objęcie wbrew zakazowi jest ważne, ale dyrektor odpowiada solidarnie za pełne wniesienie wkładu, chyba że nie ponosi winy (§ 2–3). Przy wspólnych Radach wyklucza to krzyżowy aport akcji;
    - nabycie akcji spółki dominującej przez zależną traktuje się jak nabycie akcji własnych: cel z katalogu, limit 25%, kapitał rezerwowy, brak głosu (art. 300⁴⁷ § 2, 8 i 9).
  - § 15 ust. 9 wymaga zgody WZ (75%) i zawiadomienia z art. 6. Warto dopisać skutki art. 300⁴⁷–300⁴⁸ i zawiadomienie przy dominacji z lit. d (propozycja w punkcie 6.3).
  - Dominacji z lit. d nie ma, jeśli wspólni dyrektorzy stanowią najwyżej połowę każdej Rady (np. Rady po 3 osoby, w tym 1 wspólna).
- **Grupa spółek** (art. 21¹–21¹⁶ KSH, Dz.U. 2022 poz. 807 **[S]**) wymaga spółki dominującej — opcja na etap holdingu.
- **IP między spółkami:**
  - forma pisemna dla przeniesień i licencji wyłącznych **[S]**;
  - współtwórcy (art. 9 **[Z]**);
  - prawa do utworu osoby pracującej dla obu spółek — dla spółki, do której obszaru utwór należy (§ 15 ust. 5).
- **Konsorcjum, przetargi, granty:**
  - umowa konsorcjum co do zasady nie jest spółką cywilną (SA w Warszawie VI ACa 357/16 **[S]**), ale zależy to od treści;
  - wspólne oferty zamiast osobnych (art. 108 ust. 1 pkt 5 Pzp **[S]**);
  - wykonawcy wspólni odpowiadają solidarnie za wykonanie umowy i zabezpieczenie — tak stanowił art. 141 dawnej Pzp (SN IV CSK 86/17 **[S]**); brzmienia art. 445 obecnej Pzp nie potwierdzono **[W]**;
  - EDF (rozporządzenie 2021/697 **[Z]**):
    - konsorcjum to co najmniej 3 podmioty z 3 państw; co najmniej 3 z nich, z co najmniej 2 państw, przez cały czas realizacji działania nie mogą być kontrolowane przez ten sam „podmiot prawny” ani kontrolować się nawzajem (art. 10 ust. 4);
    - „podmiot prawny” to osoba prawna albo jednostka bez osobowości z art. 197 ust. 2 lit. c rozporządzenia finansowego, a nie osoba fizyczna (art. 2 pkt 1); „kontrola” to zdolność wywierania decydującego wpływu (art. 2 pkt 6);
    - wspólni założyciele-osoby fizyczne sami nie przesądzają więc o braku niezależności. Wzajemna dominacja przez wspólne Rady może jednak zostać uznana za kontrolę **[W]**, dlatego nie należy liczyć Basilisk i Appolonii jako dwóch niezależnych członków;
    - wymóg nie dotyczy technologii przełomowych i studiów, np. wykonalności (art. 10 ust. 5).
- **Podatki:**
  - nieodpłatne świadczenia: przychód spółki według cen rynkowych (art. 12 ust. 1 pkt 2 i ust. 6 CIT **[S]**); szerokie pojęcie świadczenia — NSA II FPS 1/06 **[S]**;
  - ceny transferowe: spółki są powiązane, gdy ta sama osoba ma w każdej co najmniej 25% udziałów albo głosów, faktycznie może wpływać na kluczowe decyzje (np. jako dyrektor) albo gdy wpływ wywierają osoby spokrewnione (art. 23m ust. 1 pkt 4 i ust. 2 PIT **[Z]**; w CIT lustrzany art. 11a **[S]**);
  - lokalną dokumentację sporządza się powyżej 10 mln zł rocznie dla transakcji towarowej albo finansowej i 2 mln zł dla usługowej albo innej (art. 23w ust. 2 PIT **[Z]**, art. 11k ust. 2 CIT);
  - zwolnienie dla transakcji krajowych nie działa w roku, w którym którakolwiek strona poniosła stratę podatkową (art. 23z pkt 1 PIT **[Z]**, art. 11n pkt 1 CIT). Spółka ze stratą traci więc zwolnienie;
  - cena rynkowa obowiązuje niezależnie od obowiązku dokumentacji **[W]**. Artykułu o zmianach w cenach transferowych od 5.11.2026 r. nie udało się otworzyć.
- **Appolonia:**
  - umowa jest lustrzana i ma wszystkie poprawki rund 1–3;
  - otwarte: pisownia firmy, siedziba, skład założycieli, weryfikacja kodów PKD (w tym morskich kodów usługowych).

---

## 4. Orzecznictwo — zestawienie

| Sygnatura | Sąd, data | Teza (w zakresie istotnym dla audytu) | Zastosowanie | Weryf. |
|-----|-----|---------------|-----|--|
| II CSKP 593/22 | SN, 9.12.2022 | Art. 64 KC nie tworzy obowiązku, ale wyrok zastępuje oświadczenie potrzebne do wykonania istniejącego obowiązku | § 4 ust. 6, § 9 | [Z] |
| V CSK 522/18 | SN, 23.06.2020 | Stosunek podstawowy wyznacza dopuszczalność zrzeczenia się odwołania pełnomocnictwa | § 9 ust. 6 | [Z] |
| III CZP 109/22 | SN | Rozdzielność majątkowa nie daje drugiemu małżonkowi praw korporacyjnych | akcje w majątku wspólnym | [Z] |
| III CSKP 65/21 | SN | Akcjonariuszem jest małżonek, który objął akcje i jest wpisany do rejestru | jw. | [Z] |
| III CZP 32/16 | SN | Udziały mogą należeć do majątku wspólnego (analogicznie akcje) | jw. | [Z] |
| III CZP 13/13 | SN (7), 18.09.2013 | Uchwały zarządu i rady nadzorczej spółek kapitałowych można zaskarżyć powództwem o ustalenie (art. 189 KPC w zw. z art. 58 KC); OSNC 2014, nr 3, poz. 23 | uchwały Rady | [S] |
| III CZP 71/18 | SN, 30.01.2019 | Pełnomocnik z art. 210 § 1 KSH: do konkretnej umowy, konkretnego sporu albo rodzajowy; powołuje go uchwała wspólników | § 11 ust. 3, § 18 ust. 6 | [S] |
| II CRN 60/93 | SN, 7.09.1993 | Zbycie bez zgody spółki — bezskuteczność zawieszona; zgoda działa wstecz | § 8 | [S] |
| V CSK 274/21 | SN | Brak zgody — bezskuteczność zawieszona, nie nieważność | § 8 | [S] |
| I CSK 132/11 | SN, 1.12.2011 | Skutki naruszenia ograniczeń zbywalności zależą od rodzaju ograniczenia | § 8 | [S] |
| V AGa 158/20 | SA w Gdańsku, 9.02.2021 | Umowa bez zgody organu — bezskuteczność zawieszona | § 8 | [S] |
| II CSKP 1733/22 | SN, 8.11.2024 | Umowa z naruszeniem art. 210 KSH nieważna (art. 58 § 1 KC); glosa: pominięto art. 39 § 1 KC. Nie mylić z II CSKP 80/23 (26.01.2024, art. 410 KC) | § 11 ust. 3 | [S] |
| II CSK 744/11 | SN, 11.07.2012 | Czynność „fałszywego organu” nieważna, bez konwalidacji (przed zmianą art. 39 KC) | § 11 ust. 3 | [S] |
| I CK 381/05 | SN, 8.03.2006 | Pola eksploatacji muszą być wyraźnie wymienione; pola nieznane wyłączone | § 14 ust. 1 lit. b | [S] |
| III CK 124/05 | SN, 14.09.2005 | Licencja obejmuje wyraźnie wymienione pola znane w chwili zawarcia | jw. | [S] |
| I CSKP 62/21 | SN, 13.05.2021 | Licencja niewyłączna bez formy pisemnej, możliwa konkludentnie (poza zamówieniami publicznymi) | § 4, § 14, § 15 | [S] |
| VI ACa 1735/14 | SA w Warszawie | Kontynuowanie współpracy jako licencja niewyłączna per facta concludentia | § 14 | [S] |
| II CK 51/04 | SN, 15.10.2004 | Zakres art. 68 ust. 2 pr. aut. | § 14 ust. 2 | [S] |
| SK 32/14 | TK, 23.06.2015 (Dz.U. 2015 poz. 932) | Ryczałt trzykrotności wynagrodzenia za naruszenie — niekonstytucyjny | ryzyko naruszeń IP | [S] |
| C-367/15 | TSUE, 25.01.2017 | Dwukrotność opłaty licencyjnej zgodna z dyrektywą 2004/48/WE | jw. | [S] |
| VI ACa 357/16 | SA w Warszawie | Konsorcjum: podtyp spółki cywilnej, spółka cywilna albo umowa samodzielna | konsorcjum | [S] |
| IV CSK 86/17 | SN, 15.02.2018 | Solidarność wykonawców wspólnych dotyczy wykonania umowy i zabezpieczenia (art. 141 dawnej Pzp), nie etapu postępowania | konsorcjum | [S] |
| II FPS 1/06 | NSA (uchwała), 16.10.2006 | Szerokie pojęcie nieodpłatnego świadczenia | licencje nieodpłatne | [S] |
| KIO (wybór) | KIO | Odrębne oferty z jednej grupy kapitałowej — wykluczenie bez wykazania niezależności | przetargi | [S] |

**Luki w orzecznictwie** (wynik negatywny wyszukiwania): brak orzeczenia SN wprost o art. 41 ust. 3 pr. aut., o art. 300⁷⁹ KSH i o fikcji zgody na zbycie akcji P.S.A. Wyniku sprawy SN I CSK 459/25 (art. 39 KC a art. 210 KSH) nie ustalono. Nie znaleziono interpretacji podatkowych o przychodzie nabywcy akcji w vestingu, o licencji nieodpłatnej od wspólnika i o wkładzie w postaci pracy w P.S.A.

---

## 5. Lista kontrolna poza umową

**Przed aktem**

1. Uzgodnić z podmiotem prowadzącym rejestr akcjonariuszy:
   - mechanizm fikcji zgody (§ 8 ust. 1);
   - wzmianki o vestingu i lock-upie;
   - wykreślanie wzmianek po zakończeniu obowiązku (§ 9 ust. 7).
2. Wycena wkładów niepieniężnych z uzasadnieniem, spójna z PIT (K3).
3. Wykazy do aportu: repozytoria z commitami i sumami kontrolnymi, współtwórcy, open source z licencjami, oświadczenia o braku praw byłych pracodawców i uczelni.
4. Weryfikacja kodów PKD 2025. Dla Appolonii: firma, siedziba, skład założycieli.
5. Skład Rad obu spółek: wspólni dyrektorzy najwyżej połowa każdej Rady albo przyjęcie skutków wzajemnej dominacji (A4-1).
6. Gotówka założycieli na PIT od aportu IP: 19% wartości wkładu, rozliczane w zeznaniu za rok wpisu Spółki (art. 17 ust. 1 pkt 9 i ust. 1a, art. 30b ust. 1 pkt 4 PIT).

**Przy akcie**

1. Uchwała założycielska o **pełnomocniku Spółki** z nazwiskiem i listą umów (§ 18 ust. 6, § 11 ust. 3).
2. Umowy przeniesienia aportu IP, podpisane po stronie Spółki przez pełnomocnika (§ 4 ust. 6).
3. Umowy wykonawcze vestingu z pełnomocnictwami (§ 9 ust. 6), z zapisem o źródle ceny.
4. Regulamin WZ, wybór podmiotu prowadzącego rejestr, pierwsi dyrektorzy.

**Po wpisie**

1. Wzmianki w rejestrze akcjonariuszy (od 18.02.2027 r. obowiązek zgłoszenia w 7 dni **[Z]**).
2. Zgłoszenie do CRBR (P.S.A. jest objęta — art. 58 pkt 4a ustawy AML, memorandum **[Z]**), NIP, VAT-R **[W]**.
3. Umowy o pracę albo B2B założycieli z klauzulami IP i wynagrodzeniem za prawa do utworów innych niż programy (art. 43 ust. 2 pr. aut.); kwartalne potwierdzenia utworów przez pełnomocnika.
4. Umowa o Współpracy z drugą spółką, zatwierdzona uchwałami WZ obu spółek (§ 13 lit. j).
5. Regulamin programu P zatwierdzony przez WZ (§ 7 ust. 5).
6. Wnioski o interpretacje podatkowe: aport IP, licencje nieodpłatne, cena emisyjna w vestingu, seria F, seria P (punkt 6.2).
7. Przy wspólnych Radach — wzajemne zawiadomienia z art. 6 § 1 KSH w 2 tygodnie od powstania dominacji (wpis drugiej spółki albo powołanie wspólnych dyrektorów).

---

## 6. Weryfikacja tez (A4)

Tezy z dawnej listy pytań i tezy oznaczone [W] sprawdzono 5.11.2026 r. na tekstach ustaw w `src/legal/` i w wyszukiwaniu. Pełne teksty orzeczeń nadal były niedostępne, więc orzeczenia mają poziom [S].

### 6.1. Wyniki

| # | Teza | Wynik | Poziom |
|--|--------|------------------------|----|
| 1 | Pełnomocnik z art. 300⁷⁹ § 1 KSH może być powołany do rodzaju umów | **Potwierdzona przez analogię.** SN w III CZP 71/18 dopuścił przy art. 210 § 1 KSH umocowanie do konkretnej umowy, sporu albo rodzajowe. Art. 300⁷⁹ § 1 ma tę samą konstrukcję. Umowa bez pełnomocnika jest nieważna (II CSKP 1733/22); potwierdzenie z art. 39 § 1 KC jest sporne | [S]; tekst przepisów [Z] |
| 2 | Fikcja zgody na zbycie (§ 8 ust. 1) | **Niepotwierdzona.** Brak orzeczeń i komentarzy. Art. 300³⁹ § 1 KSH pozwala ograniczyć rozporządzenie „w inny sposób”, więc jej nie wyklucza. Orzecznictwo do art. 182 KSH dotyczy braku zgody (bezskuteczność zawieszona) | [Z] tekst; skutek [W] |
| 3 | Utwory „w ramach zadań” i kwartalne potwierdzenia a art. 41 ust. 3 pr. aut. | **Potwierdzona.** Przepis unieważnia umowę tylko co do wszystkich utworów (danego rodzaju) mających powstać w przyszłości. Komentarze dopuszczają przeniesienie praw do określonych utworów przyszłych. Umowa B2B sama nie przenosi praw | [Z] tekst; [S] |
| 4 | Dominacja przy wspólnych dyrektorach i próg 33% z art. 6 KSH w P.S.A. | **Rozstrzygnięta przez ustawę.** „Zarząd” to rada dyrektorów (art. 4 § 2¹). Przy wspólnych Radach spółki są wzajemnie dominujące (art. 4 § 1 pkt 4 lit. d, § 5). Próg liczy się od liczby wszystkich akcji (art. 4 § 2² pkt 1). Skutki — punkt 3 | [Z] |
| 5 | Łączenie pierwszego roku obrotowego (§ 16 ust. 5) | **Potwierdzona** (art. 3 ust. 1 pkt 9 UoR) | [Z] |
| 6a | Basilisk i Appolonia jako jedna grupa kapitałowa (Pzp) | **Częściowo.** Grupa kapitałowa to przedsiębiorcy kontrolowani przez jednego przedsiębiorcę (art. 4 pkt 14 u.o.k.k.); komentarze zaliczają do niej spółki kontrolowane przez tę samą osobę fizyczną. Przy wspólnej kontroli kilku założycieli — niepewne. Orzeczenia KIO nie znaleziono | [S]; [W] |
| 6b | Niezależność członków konsorcjum EDF | **Potwierdzona treść** (art. 10 ust. 4–5, art. 2 pkt 1 i 6 rozporządzenia 2021/697). Osoba fizyczna nie jest „podmiotem prawnym”. Ryzyko: wzajemna dominacja przez Rady jako „kontrola” | [Z]; [W] |
| 7a | PIT od aportu IP | **Potwierdzona mechanika.** Przychodem jest wartość wkładu z umowy spółki, a jeśli jest niższa od rynkowej — wartość rynkowa (art. 17 ust. 1 pkt 9). Przychód powstaje w dniu wpisu spółki (ust. 1a pkt 1). Kosztem są faktycznie poniesione wydatki na wytworzenie (art. 22 ust. 1e pkt 3). Stawka 19% (art. 30b ust. 1 pkt 4). Podatek płaci się bez gotówki ze Spółki | [Z] |
| 7b | Przychód Spółki z licencji nieodpłatnej (§ 14 ust. 2) | **Potwierdzona zasada** (art. 12 ust. 1 pkt 2 i ust. 6 CIT; NSA II FPS 1/06). Interpretacji dla licencji od wspólnika nie znaleziono | [S] |
| 7c | Cena w vestingu | **Potwierdzona mechanika.** Zbywca: wartość rynkowa tylko przy cenie znacznie odbiegającej „bez uzasadnionej przyczyny” (art. 19 ust. 1 i 4 PIT). Nabywca: świadczenie częściowo odpłatne (art. 11 ust. 2b) — teza ryzyka, interpretacji nie znaleziono | [Z] tekst; [W] praktyka |
| 7d | Seria F za pracę | **Mechanika potwierdzona, kwalifikacja otwarta.** Praca i usługi są wkładem niepieniężnym (art. 300² § 2 KSH), więc stosuje się art. 17 ust. 1 pkt 9 PIT. Przychód powstaje w dniu wpisu emisji (ust. 1a pkt 2), przed wykonaniem pracy. Organ może go jednak uznać za przychód z pracy lub usług; przepisu szczególnego w PIT nie ma | [Z] tekst; [W] kwalifikacja |
| 7e | Preferencja dla serii P | **Potwierdzona** (art. 24 ust. 12b PIT: ust. 11–11b stosuje się do programu motywacyjnego P.S.A.) | [Z] |
| 7f | Ceny transferowe między siostrami | **Potwierdzona mechanika** (punkt 3) | [Z] PIT; [S] CIT |
| 7g | Wymiana akcji przy holdingu | **Potwierdzona.** Neutralna, jeśli spółka nabywająca uzyska albo zwiększy bezwzględną większość głosów, dopłata nie przekracza 10% wartości rynkowej akcji (P.S.A. nie ma wartości nominalnej), a strony podlegają nieograniczonemu opodatkowaniu w UE/EOG (art. 24 ust. 8a–8b PIT) | [Z] |
| 8 | Art. 43 ust. 1 pr. aut. | **Potwierdzona, z uzupełnieniem.** Brzmienie bez zmian; doszły ust. 2–3 (godziwe wynagrodzenie). Art. 43, 44 i 47¹ nie dotyczą programów komputerowych (art. 77 ust. 1) | [Z] |
| 9 | Art. 15 § 1 KSH nie obejmuje dyrektora P.S.A. (memorandum 2.2.4) | **Obalona.** Obejmuje (art. 4 § 2¹); bez zgody WZ umowa jest nieważna (art. 17 § 1–2) | [Z] |
| 10 | III CZP 13/13 | **Potwierdzona.** Uchwały zarządu i rady nadzorczej można zaskarżyć powództwem o ustalenie (art. 189 KPC w zw. z art. 58 KC) | [S] |

### 6.2. Co zostaje otwarte

1. Fikcja zgody (§ 8 ust. 1): czy przyjmie ją podmiot prowadzący rejestr. Alternatywa: wyraźna zgoda Rady w krótkim terminie.
2. Art. 39 § 1 KC a umowy z dyrektorem zawarte bez pełnomocnika (sprawa SN I CSK 459/25).
3. Interpretacje indywidualne: aport IP (wartość, koszt), seria F (źródło przychodu), licencja nieodpłatna (§ 14 ust. 2), przychód nabywcy w vestingu.
4. Pzp przy wspólnej kontroli kilku założycieli; EDF — czy wzajemna dominacja przez Rady jest „kontrolą”.
5. Brzmienie art. 445 Pzp i zmiany w cenach transferowych od 5.11.2026 r. (źródło niedostępne w tej sesji).

### 6.3. Propozycja zmiany umów (niewprowadzona)

§ 15 ust. 9 obu umów. Obecnie: „Objęcie albo nabycie przez Spółkę akcji Spółki Siostrzanej wymaga uchwały Walnego Zgromadzenia podjętej większością 75% wszystkich głosów; jeżeli powstanie stosunek dominacji, Spółka dokonuje zawiadomienia, o którym mowa w art. 6 KSH.”

Propozycja: „Objęcie albo nabycie przez Spółkę akcji Spółki Siostrzanej wymaga uchwały Walnego Zgromadzenia podjętej większością 75% wszystkich głosów. Jeżeli Spółka Siostrzana jest wobec Spółki spółką dominującą, Spółka nie obejmuje jej akcji (art. 300⁴⁸ § 1 KSH), a do ich nabycia stosuje się przepisy o nabyciu akcji własnych (art. 300⁴⁷ § 9 KSH). Spółka dokonuje zawiadomień, o których mowa w art. 6 § 1 i 6 KSH, także gdy stosunek dominacji albo jego ustanie wynika z art. 4 § 1 pkt 4 lit. d KSH.”

---

## Źródła

**Repozytorium:** `memorandum.md` (1.1.4, 1.2.1, 1.3.5, 1.5.1, 1.5.2, 2.2.4, 2.3.3, 3.1.1–3.1.3, T4, T9), `psa_feedback.tex`, `prosta.md`, `analiza_ip_aport.md`, `audyt_rundy.md`, rozporządzenie MS w sprawie wzorca S24 (Dz.U. 2021 poz. 1191). Teksty ustaw: `src/legal/` (A4).

**Wyszukiwanie (poziom [S]):**

Prawo spółek

- art. 300⁷⁹ KSH: [lexlege.pl](https://lexlege.pl/ksh/art-300-79/)
- art. 300³⁹ KSH: [lexlege.pl](https://lexlege.pl/ksh/art-300-39/)
- art. 4 KSH: [lexlege.pl](https://lexlege.pl/ksh/art-4/); unia personalna: [rp.pl](https://pro.rp.pl/prawo-w-firmie/art13279531-powolywanie-tych-samych-osob-do-zarzadow-spolek-zaleznych-moze-byc-ryzykowne)
- art. 6 KSH: [lexlege.pl](https://lexlege.pl/ksh/art-6/)
- Grupa spółek: [Dz.U. 2022 poz. 807](https://api.sejm.gov.pl/eli/acts/DU/2022/807/text/T/D20220807L.pdf), [lexlege.pl](https://lexlege.pl/ksh/dzial-iv-grupa-spolek/15384/)
- BJR: [codozasady.pl](https://codozasady.pl/en/p/the-business-judgment-rule), [apcz.umk.pl](https://apcz.umk.pl/SIT/article/view/36110)
- II CSKP 1733/22 — glosa: [journals.umcs.pl](https://ns2.journals.umcs.pl/glosa/article/download/19897/pdf)
- V CSK 274/21: [sn.pl](https://www.sn.pl/sites/orzecznictwo/Orzeczenia3/V%20CSK%20274-21.pdf); I CSK 132/11: [standardyprawa.pl](https://standardyprawa.pl/orzeczenie/38302); V AGa 158/20: [dlajurysty.pl](https://dlajurysty.pl/orzeczenia/pokaz/54999/V-AGa-158-20)

Prawo autorskie

- I CK 381/05: [dlajurysty.pl](https://dlajurysty.pl/orzeczenia/pokaz/34704/I-CK-381-05); III CK 124/05: [dlajurysty.pl](https://dlajurysty.pl/orzeczenia/pokaz/35399/III-CK-124-05)
- Licencja dorozumiana (I CSKP 62/21, VI ACa 1735/14): [legeartis 2022/01](https://czasopismo.legeartis.org/2022/01/udzielenie-licencji-korzystanie-oprogramowania-per-facta-concludentia-zamowienie-publiczne/), [legeartis 2022/07](https://czasopismo.legeartis.org/2022/07/dorozumiane-przedluzenie-licencji-korzystanie-utworu-oprogramowania-per-facta-concludentia/)
- art. 41 ust. 3: [e-prawnik.pl](https://e-prawnik.pl/artykuly/czy-mozna-zawrzec-umowe-przeniesienia-autorskich-praw-majatkowych-do-wszystkich-utworow.html)
- art. 43: [lexlege.pl](https://lexlege.pl/ustawa-o-prawie-autorskim-i-prawach-pokrewnych/art-43/)
- art. 67: [lexlege.pl](https://lexlege.pl/ustawa-o-prawie-autorskim-i-prawach-pokrewnych/art-67/); projekt formy dokumentowej: [legeartis 2025/05](https://czasopismo.legeartis.org/2025/05/forma-dokumentowa-umowy-przeniesienie-praw-autorskich-licencji-wylacznej-rygore-niewaznosci-projekt/)
- art. 68: [lexlege.pl](https://lexlege.pl/ustawa-o-prawie-autorskim-i-prawach-pokrewnych/art-68/); II CK 51/04 w literaturze: [PPUW 2/2015](https://lawreview.wpia.uw.edu.pl/wp-content/uploads/2017/07/99_PDFsam_PPUW-2-2015-www.pdf)
- art. 74: [lexlege.pl](https://lexlege.pl/ustawa-o-prawie-autorskim-i-prawach-pokrewnych/art-74/)
- TK SK 32/14: [Dz.U. 2015 poz. 932](https://eli.gov.pl/api/acts/DU/2015/932/text/T/D20150932TK.pdf), [legeartis](https://czasopismo.legeartis.org/2015/06/wyrok-prawo-autorskie-sk-32-14/)
- TSUE C-367/15: [legeartis](https://czasopismo.legeartis.org/2017/01/odszkodowanie-dwukrotnosc-wynagrodzenia/)

Konsorcjum, przetargi, granty

- Konsorcjum a spółka cywilna: [standardyprawa.pl](https://standardyprawa.pl/standardy/3081), [podatki.biz](https://www.podatki.biz/artykuly/kwestie-zwiazane-z-konsorcjami-i-ksztaltowaniem-ich-relacji-wewnetrznych-i-zewnetrznych_34_45295.htm)
- Pzp, grupa kapitałowa: [rp.pl](https://pro.rp.pl/biznes/art42532791-jedna-grupa-kapitalowa-kilka-odrebnych-ofert-w-przetargu)
- EDF: [EUR-Lex 2021/697](https://eur-lex.europa.eu/eli/reg/2021/697), [streszczenie PE](https://oeil.europarl.europa.eu/oeil/en/document-summary?id=1655439)

Podatki

- NSA II FPS 1/06: [KIDP](https://archiwumdebata.kidp.pl/materialy/nieodplatne_swiadczenie.pdf)
- Wymiana udziałów: [poradnikprzedsiebiorcy.pl](https://poradnikprzedsiebiorcy.pl/-zamiana-udzialow-w-spolce-kiedy-jest-neutralna-podatkowo)

Weryfikacja A4 (teksty ustaw w `src/legal/` oraz wyszukiwanie)

- III CZP 71/18: [standardyprawa.pl](https://standardyprawa.pl/orzeczenie/376999), [rp.pl](https://pro.rp.pl/prawo-w-firmie/art1508091-uchwala-sadu-najwyzszego-kto-moze-zawierac-umowy-z-prezesem-spolki), [infor.pl](https://ksiegowosc.infor.pl/obrot-gospodarczy/spolki/3004933,Umocowanie-pelnomocnika-spolki-kapitalowej-przy-umowach-z-czlonkami-zarzadu.html), [pragmatiq.pl](https://pragmatiq.pl/mniejszosciowi/pelnomocnictwo-z-art-210-%C2%A7-1-ksh-a-spor-w-spolce/)
- Art. 39 KC a art. 210 KSH: II CSK 744/11 — [standardyprawa.pl](https://standardyprawa.pl/orzeczenie/44403); zmiana od 1.03.2019 r. — [rp.pl](https://pro.rp.pl/prawo-w-firmie/art1445791-waznosc-umowy-zawartej-z-falszywym-organem-osoby-prawnej-po-1-marca-2019-r); glosa — [journals.umcs.pl](https://ns2.journals.umcs.pl/glosa/issue/download/992/xml_5); I CSK 459/25 — [sn.pl](https://www.sn.pl/sites/orzecznictwo/Orzeczenia3/I%20CSK%20459-25.pdf)
- III CZP 13/13: [standardyprawa.pl](https://standardyprawa.pl/orzeczenie/84055); powołanie w I CSK 378/19: [sn.pl](https://www.sn.pl/sites/orzecznictwo/Orzeczenia3/I%20CSK%20378-19.pdf)
- Brak zgody na zbycie (art. 182 KSH): [prawowobrocie.pl](https://prawowobrocie.pl/prawo-handlowe-i-gospodarcze/skutki-prawne-braku-zgody-organu-na-zbycie-udzialow/1740/), [lawinbusiness](https://lawinbusiness.ostrowski.legal/zbycie-udzialow-w-spolce-z-ograniczona-odpowiedzialnoscia-bez-wymaganej-zgody-w-swietle-art-182-k-s-h/)
- Art. 41 ust. 3 i B2B: [PARP](https://www.parp.gov.pl/component/content/article/83261:umowa-o-przeniesienie-autorskich-praw-majatkowych), [poradnikprzedsiebiorcy.pl](https://poradnikprzedsiebiorcy.pl/-prawa-autorskie-a-b2b-jak-je-przeniesc-i-nie-wpasc-w-pulapke)
- Pierwszy rok obrotowy: [rp.pl](https://pro.rp.pl/rachunkowosc/art11527151-kiedy-skladac-pierwsze-sprawozdanie-finansowe)
- Konsorcjum: IV CSK 86/17 — [standardyprawa.pl](https://standardyprawa.pl/orzeczenie/368677), [UZP](https://www.uzp.gov.pl/__data/assets/pdf_file/0020/37163/wyrok-SN-z-dnia-15-lutego-2018-r.-IV-CSK-86-17.pdf); art. 141 dawnej Pzp — [e-prawnik.pl](https://e-prawnik.pl/porady-prawne/umowa-konsorcjum-a-odpowiedzialnosc-wykonawcow.html)
- Podatki: aport praw autorskich — [e-prawnik.pl](https://e-prawnik.pl/artykuly/wniesienie-praw-autorskich-jako-aportu-do-spolki-z-o-o-opinia-prawna.html); świadczenia wspólnika na rzecz spółki — [podatki.biz](https://www.podatki.biz/artykuly/uslugi-wspolnika-na-rzecz-spolki-konsekwencje-podatkowe_28_32399.htm), [rp.pl](https://pro.rp.pl/podatki/art5576651-nieodplatne-korzystanie-ze-znaku-towarowego-a-cit); progi dokumentacji cen transferowych — [akademialtca.pl](https://akademialtca.pl/blog/co-musisz-wiedziec-aby-ustalic-czy-masz-obowiazek-sporzadzenia-dokumentacji-cen-transferowych); zmiany od 5.11.2026 r. (nie otwarto — domena poza siecią sesji) — [podatki.biz](https://www.podatki.biz/artykuly/pit-i-cit-zmiany-dot-cen-transferowych-od-5-listopada-2026-r_60_64246.htm)
