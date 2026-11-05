# Audyt prawny: Basilisk Systems P.S.A. (umowa 2.0-S) i struktura Basilisk–Appolonia

| | |
|----|----------------|
| **Przedmiot audytu** | 1. Umowa Basilisk Systems P.S.A. — `psa.tex`, gałąź `psa_simple2` (commit `da68d38`): 18 §, Załącznik nr 1. 2. Umowa Appolonia P.S.A. — `appolonia.tex`, gałąź `psa_appolonia` (commit `410f00f`). 3. Konstrukcja dwóch spółek siostrzanych (§ 15 obu umów), konsorcjum, przenoszenie IP. |
| **Data** | listopad 2026 r. |
| **Stan prawny** | Według `memorandum.md` (KSH t.j. Dz.U. 2024 poz. 18 z późn. zm., w tym zmiany od 18.02.2027 r. z Dz.U. 2026 poz. 176) oraz źródeł wskazanych w raporcie. |
| **Ocena ogólna** | Konstrukcja jest zgodna z KSH co do zasady. **Przed podpisaniem trzeba usunąć 3 ryzyka krytyczne i 5 wysokich** (punkt 1.2). Najpoważniejsze z nich to reprezentacja Spółki w umowach z założycielami-dyrektorami: grozi nieważnością umów przenoszących IP i umów wykonawczych vestingu. |

**Weryfikacja źródeł.** W tym środowisku nie było dostępu do ISAP, portalu orzeczeń SN, SAOS, CBOSA ani systemów Legalis/LEX. Przy każdej tezie podaję poziom weryfikacji:

| Znak | Znaczenie |
|--|------------------|
| **[Z]** | Zweryfikowane na tekście przepisu albo orzeczenia — w `memorandum.md` lub `psa_feedback.tex` (z linkami do sn.pl i eli.gov.pl) |
| **[S]** | Potwierdzone wyszukiwaniem w toku audytu: istnienie, sygnatura, data i teza według baz orzeczeń lub komentarzy. Pełnego tekstu uzasadnienia nie czytano. |
| **[W]** | Wiedza ogólna albo wniosek audytora — do potwierdzenia przez prawnika |

Raport nie zastępuje opinii adwokata, radcy prawnego ani doradcy podatkowego. Ma przygotować rozmowę z nimi i skrócić ją do spraw spornych.

---

## 1. Wnioski

### 1.1. Co jest dobrze

- **Ustrój P.S.A. i forma.** Rada Dyrektorów z dyrektorem wykonawczym i niewykonawczym, reprezentacja łączna, uchwały poza WZ i udział zdalny są zgodne z KSH (art. 300⁷³–300⁷⁹, 300⁸⁰, 300⁹² **[Z]**). Umowa musi mieć formę aktu notarialnego, bo wkłady niepieniężne wykluczają S24 (art. 300⁶ § 1 **[Z]**).
- **Limity emisji** (§ 5) są w pełni kontrolowalne: maksymalna liczba akcji przy każdej uchwale, limit łączny i limity serii.
- **Ograniczenia zbywania.** Zgoda Spółki z zamkniętym katalogiem przyczyn odmowy, wyłączenie art. 300³⁹ § 3–5 i 12-miesięczny lock-up mieszczą się w swobodzie z art. 300³⁹ § 1–2 KSH (memorandum 1.2.1: „zgodne warunkowo” **[Z]**).
- **Vesting** jako „obowiązek związany z akcją” ujawniany w rejestrze, który obciąża każdoczesnego posiadacza akcji (art. 300¹ § 3, art. 300³³ § 1 pkt 10–11 KSH; memorandum 1.5.1 **[Z]**). Wykonanie można wymusić wyrokiem zastępującym oświadczenie woli (art. 64 KC; SN II CSKP 593/22 **[Z]**).
- **Kapitał.** Wkłady niepieniężne przeznaczone na kapitał akcyjny — tak jak rekomendowało memorandum (3.1.2).
- **Nowe mechanizmy IP** z `psa_simple2` (§ 4 ust. 5, § 14 ust. 1–2, § 15 ust. 5) zamykają większość luk w tytule do kodu — pod warunkiem usunięcia ryzyka K1.

### 1.2. Ryzyka — zestawienie

Priorytety:

| Priorytet | Znaczenie |
|--|------------------|
| **K** | Krytyczne — bez usunięcia umowa albo kluczowe czynności mogą być nieważne |
| **W** | Wysokie — realne ryzyko sporu lub utraty ochrony |
| **Ś** | Średnie — do decyzji albo do uporządkowania przed rundą |
| **N** | Niskie — porządkowe |

| ID | Ryzyko | Gdzie | Pr. | Rekomendacja |
|--|--------------|------|-|---------|
| **K1** | Umowy Spółki z założycielami, którzy są dyrektorami, zawarte bez pełnomocnika powołanego uchwałą akcjonariuszy, są nieważne. Dotyczy: przeniesienia IP (aport), kwartalnych potwierdzeń utworów i umów wykonawczych vestingu. | § 4 ust. 5, § 9 ust. 6, § 14 ust. 1 lit. e, § 18 ust. 6; art. 300⁷⁹ § 1 KSH | **K** | Uchwała założycielska o pełnomocniku do tych umów; zmiana § 11 ust. 3 i § 18 ust. 6 (pkt 6.1) |
| **K2** | Aport IP niewniesiony skutecznie: akcje niepokryte, kapitał w KRS niezgodny ze stanem faktycznym, odpowiedzialność dyrektorów (cywilna i karna) | § 4; art. 300⁹, 300¹⁰, 300¹² § 3, 300¹²³, 587 § 1 KSH | **K** | Komplet umów przeniesienia w dniu aktu: wykaz utworów, współtwórców, open source, pola eksploatacji (pkt 5) |
| **K3** | Wartości wkładów w Załączniku nr 1 jako podstawa kapitału, PIT założycieli i odpowiedzialności z art. 300¹⁰ | Załącznik nr 1 | **K** | Jedna obronna wycena z uzasadnieniem, spójna z PIT (memorandum T4, T9) |
| **W1** | Odkup akcji niezwolnionych przez **samą Spółkę** po cenie emisyjnej, a potem umorzenie, może zostać uznany za obejście art. 300⁴⁵ § 2 KSH (umorzenie przymusowe ze spłatą nie niższą niż wartość godziwa) | § 9 ust. 4, § 3 ust. 7 lit. c, ust. 8 lit. b | **W** | Spółka nie może być nabywcą w vestingu, a jeżeli nabywa — tylko w celu przekazania akcji do programu P, bez umorzenia (pkt 6.2) |
| **W2** | Nie zapisano wprost, że zdarzenia dotyczące pierwotnego Akcjonariusza Funkcjonalnego uruchamiają obowiązek zbycia także u nabywcy wtórnego | § 9 ust. 7 | **W** | Brzmienie z memorandum 1.5.1 (pkt 6.3) |
| **W3** | Uchwała obiegowa może zostać „podjęta” przed upływem terminu przy większości **głosów oddanych**, choć późniejsze głosy mogłyby zmienić wynik | § 12 ust. 3 | **W** | Wcześniejsze zamknięcie tylko wtedy, gdy „za” jest większość **wszystkich** głosów (pkt 6.4) |
| **W4** | Wyłączenie konfliktu interesów w relacji z Appolonią („w zakresie dopuszczalnym przez prawo”) może nie uchylić ustawowego obowiązku wstrzymania się dyrektora | § 15 ust. 6; art. 300⁵⁵ § 1 KSH | **W** | Umowa o Współpracy zatwierdzona przez WZ obu spółek, formuły cenowe, niezależny biegły (pkt 3.2) |
| **W5** | Te same osoby w Radach obu spółek mogą rodzić stosunek dominacji (unia personalna), z obowiązkami z art. 6 KSH przy jakichkolwiek wzajemnych udziałach | art. 4 § 1 pkt 4 lit. d, art. 6 KSH | **W** | Bez wzajemnych udziałów; z czasem różne składy Rad (pkt 3.3) |
| **Ś1** | Fikcja zgody na zbycie po 14 dniach milczenia Rady — ryzyko, że podmiot prowadzący rejestr nie przyjmie jej bez dokumentu | § 8 ust. 1 | **Ś** | Uzgodnić z podmiotem prowadzącym rejestr; ewentualnie konstrukcja „sprzeciwu” (pkt 6.5) |
| **Ś2** | Brak wymogu zgody WZ na pożyczkę, kredyt albo poręczenie dla dyrektora (art. 15 § 1 KSH nie obejmuje dyrektora P.S.A.) | § 13 | **Ś** | Nowa lit. k w § 13 ust. 1 (pkt 6.6) |
| **Ś3** | Preferencja PIT dla programu P wymaga programu utworzonego uchwałą WZ; regulamin nie ma wskazanego organu zatwierdzającego | § 7 ust. 2; art. 24 ust. 11–12b PIT | **Ś** | Regulamin programu zatwierdzany przez WZ (memorandum T9 pkt 1) |
| **Ś4** | Zakaz konkurencji obejmuje **każdego** akcjonariusza, także przyszłych inwestorów | § 14 ust. 5 | **Ś** | Przed rundą zawęzić do założycieli i dyrektorów albo dodać wyjątek dla funduszy |
| **Ś5** | Umowa spółki nakłada obowiązek zawarcia umowy IP na osoby, które nie są jej stronami (pracownicy, współpracownicy) | § 14 ust. 1 zd. 2 | **Ś** | Przeformułować na obowiązek Spółki (pkt 6.7) |
| **Ś6** | Przejście praw do utworów „z chwilą przekazania” bez umowy o pracę albo B2B — ryzyko z art. 41 ust. 3 pr. aut. (nieważność umowy o przyszłe utwory) | § 14 ust. 1 lit. a | **Ś** | Utrzymać kwartalne potwierdzenia (lit. e) jako podstawę; założycielom dać umowę o pracę albo B2B |
| **Ś7** | Nieodpłatne licencje i nieodpłatne przeniesienia: przychód Spółki z nieodpłatnego świadczenia; między spółkami siostrzanymi — ceny transferowe | § 14 ust. 2, § 15 ust. 2 | **Ś** | Interpretacja podatkowa; w Umowie o Współpracy ceny rynkowe |
| **Ś8** | PIT założycieli od aportu IP (19% wartości wkładu, koszt często zerowy) i od odkupu po cenie emisyjnej (art. 19 PIT) | § 4, § 9 | **Ś** | Interpretacja indywidualna (memorandum T9 pkt 3 i 6) |
| **Ś9** | Seria F za pracę lub usługi — przychód w dniu objęcia według wartości rynkowej | § 6 ust. 4 | **Ś** | Wariant wkładu pieniężnego po niskiej cenie; interpretacja (T9 pkt 2) |
| **Ś10** | Umowa o Współpracy nie istnieje, a § 15 bez niej daje tylko podstawę | § 15 ust. 2, 5, 6, 8 | **Ś** | Przygotować i zatwierdzić uchwałami WZ obu spółek, póki akcjonariat jest identyczny |
| **Ś11** | Umowa Appolonii nie ma poprawek IP z `psa_simple2`; firma i siedziba do potwierdzenia | `appolonia.tex` | **Ś** | Przenieść § 4 ust. 5, § 14 ust. 1–2 i § 15 ust. 5; potwierdzić pisownię firmy |
| **N1** | Brak postanowienia o roku obrotowym (S24 § 19) | — | **N** | Dopisać do § 16 |
| **N2** | Brak upoważnienia do wypłaty zaliczek na dywidendę (S24 § 11) | § 16 ust. 2 | **N** | Odłożyć albo dopisać |
| **N3** | Brak reguły o głosie zastawnika i użytkownika (S24 § 10) | — | **N** | Rozstrzygnąć przed kredytem z zastawem na akcjach |
| **N4** | Brak limitu czasu dla upoważnienia do nabycia akcji własnych; w P.S.A. ustawa go nie przewiduje (memorandum 1.3.5 **[Z]**) | § 3 ust. 7 | **N** | Umowny limit 5 lat (pkt 6.8) |
| **N5** | Obowiązek mediacji może kolidować z ustawowymi terminami zaskarżenia uchwał | § 18 ust. 4 | **N** | Dopisać wyłączenie terminów zaskarżenia |
| **N6** | Test wypłacalności przy wykupie opisany własnymi słowami zamiast odesłania do art. 300¹⁵ § 4–6 | § 3 ust. 8 lit. e | **N** | Odesłać do przepisu |
| **N7** | Kody PKD 2025 bez końcowej weryfikacji z klasyfikacją | § 2 | **N** | Sprawdzić przed wnioskiem do KRS |

---

## 2. Umowa Basilisk 2.0-S — analiza postanowień

### § 1–2. Firma, siedziba, przedmiot działalności

- **Ocena:** zgodne.
- **Podstawa:** art. 300⁵ § 1 KSH (elementy umowy) **[Z]**.
- **Uwagi:**
  - zmiana zakresu kodów ujawnionych w KRS w granicach listy z umowy nie wymaga zmiany umowy (§ 2 ust. 2 zd. ost.) — rozwiązanie praktyczne;
  - opis „na lądzie i w powietrzu” wyznacza granicę z Appolonią, co ma znaczenie dla zakazu konkurencji (punkt 3.2);
  - kody PKD 2025 trzeba zweryfikować z klasyfikacją przed wnioskiem (memorandum: „PKD 2025 wymaga końcowej kontroli klasyfikacji”) — **N7**;
  - na gałęzi `psa_simple` § 2 ust. 3 nadal wspomina koncesję na wyroby wojskowe; w wariancie bez kodów wojskowych to tylko informacja.

### § 3. Akcje, rejestr, akcje własne

- **Ocena:** zgodne warunkowo.
- **Podstawa:** art. 300² § 3, art. 300³¹, art. 300³³–300³⁴, art. 300⁴⁷ § 1 pkt 2, § 2–3 i § 9, art. 300¹⁵ § 2 i 4–6 KSH **[Z]**; art. 20 KSH (równe traktowanie) **[W]**.
- **Uwagi:**
  1. Limit 25% akcji własnych wynika z ustawy; akcje nabyte przez spółki zależne wlicza się do limitu (tak też `uchwaly.tex`) **[Z/W]**.
  2. W P.S.A. ustawa nie ogranicza okresu upoważnienia do nabycia akcji własnych (memorandum 1.3.5 **[Z]**) — **N4**.
  3. Cena „nie wyższa niż wartość godziwa” (ust. 8 lit. b): przed pierwszą rundą każdy wykup poza vestingiem wymaga biegłego. Koszt, nie wada prawna.
  4. **Ryzyko W1:** lit. c ust. 7 w zw. z § 9 ust. 4 — patrz § 9.
  5. Ust. 8 lit. e opisuje test wypłacalności własnymi słowami; bezpieczniej odesłać do art. 300¹⁵ § 4–6 KSH — **N6**.

### § 4. Objęcie akcji i wkłady

- **Ocena:** zgodne warunkowo, z zastrzeżeniem **K1–K3**.
- **Podstawa:**
  - KSH: art. 300² § 1–2, art. 300³ § 1–2, art. 300⁵ § 1 pkt 4, art. 300⁹ § 1–2, art. 300¹⁰ § 1–2, art. 300¹¹ § 1–2, art. 300¹² § 3, art. 300¹²³, art. 300¹²⁴, art. 587 § 1, art. 14 § 1–2 **[Z]**;
  - prawo autorskie: art. 41 ust. 2–4, art. 46, art. 53, art. 74 ust. 4 **[Z]**;
  - art. 64 KC, art. 1047 KPC **[Z]**.
- **Orzecznictwo:**
  - SN II CSKP 593/22 (9.12.2022) — art. 64 KC nie tworzy obowiązku, ale wyrok może zastąpić oświadczenie potrzebne do wykonania obowiązku już istniejącego **[Z]**. Obowiązek wniesienia aportu z § 4 ust. 5 jest takim istniejącym obowiązkiem.
  - SN I CK 381/05 (8.03.2006) i III CK 124/05 (14.09.2005) — pola eksploatacji muszą być wyraźnie wymienione, a umowa obejmuje tylko pola znane w chwili jej zawarcia **[S]**.
- **Uwagi:**
  1. **K1.** Spółkę w organizacji reprezentuje Rada Dyrektorów (art. 300¹¹ **[Z]**), czyli ci sami założyciele. Umowa przeniesienia aportu między Spółką a założycielem-dyrektorem jest umową z dyrektorem, a do takiej umowy Spółkę reprezentuje **pełnomocnik powołany uchwałą akcjonariuszy** (art. 300⁷⁹ § 1 KSH **[Z]**). Sankcją naruszenia jest nieważność (memorandum, pytanie o § 29 ust. 12: „sankcją jest nieważność” **[Z]**). Ta sama linia dla art. 210 KSH: przeważający pogląd o nieważności bezwzględnej, wyrok SN II CSKP 1733/22 z 8.11.2024 r. i glosy **[S]**. Nieważne przeniesienie aportu oznacza niewniesiony wkład (K2). Dlatego uchwała o pełnomocniku musi znaleźć się w akcie założycielskim (pkt 6.1).
  2. **K2.** Jeżeli przeniesienie jest wadliwe (brak formy pisemnej, pól eksploatacji, podpisu współtwórcy), wkład nie jest wniesiony. Skutki:
     - akcjonariusz musi wnieść wkład w ciągu 3 lat od wpisu (art. 300⁹ § 1);
     - przy znacznym zawyżeniu wartości wnoszący wyrównuje różnicę, a dyrektorzy odpowiadają solidarnie, chyba że nie ponoszą winy (art. 300¹⁰);
     - za fałszywe dane w oświadczeniu o wniesieniu wkładów dyrektorzy odpowiadają wobec wierzycieli przez 3 lata (art. 300¹²³), a podanie nieprawdziwych danych jest przestępstwem (art. 587 § 1).

     Wszystko **[Z]**, memorandum 3.1.1.

  3. Licencja tymczasowa udzielona wprost w umowie spółki jest skuteczna, bo licencja niewyłączna nie wymaga formy pisemnej, a akt notarialny i tak ją spełnia **[S]** (zob. SN I CSKP 62/21 przy § 14).
  4. Wynagrodzeniem za przeniesienie i za licencję tymczasową są akcje. To zamyka roszczenia z art. 43 ust. 1 pr. aut. (zasada odpłatności) **[S/W]** i spójnie określa przychód założyciela w PIT (memorandum T9 pkt 3 **[Z]**).
  5. Drobna niespójność: ust. 4 dopuszcza wniesienie wkładów niepieniężnych do 14 dni po wpisie, a ust. 5 każe przenieść IP w dniu aktu. Dla IP rozstrzyga ust. 5 jako przepis szczególny; można to dopisać wprost.

### § 5. Emisje i maksymalne liczby akcji

- **Ocena:** zgodne.
- **Podstawa:** art. 300¹⁰³–300¹⁰⁷, art. 300¹¹⁴–300¹¹⁸ KSH **[W]** — przepisy przywołane w umowie i w memorandum. Pozbawienie prawa poboru wymaga 4/5 głosów (art. 300¹⁰⁶) **[W]**.
- **Uwagi:**
  - zasada maksymalnej liczby akcji i łączny limit 2 000 000 są postanowieniami umownymi, dopuszczalnymi w granicach swobody umowy spółki;
  - nowa seria wymaga zmiany umowy, czyli aktu notarialnego — to świadomy koszt.

### § 6–7. Seria F i seria P

- **Ocena:** zgodne warunkowo (podatki).
- **Podstawa:** art. 300² § 2 i art. 300¹⁰⁴ § 1 pkt 7 KSH (wkład w postaci pracy) **[Z]**; art. 24 ust. 11–12b PIT **[W]** (memorandum T9 pkt 1–2).
- **Uwagi:**
  - **Ś3:** regulamin programu P powinien zatwierdzać WZ, żeby nie było wątpliwości, że program „utworzono uchwałą WZ”;
  - **Ś9:** objęcie akcji serii F za pracę rodzi ryzyko przychodu w dniu objęcia według wartości rynkowej.

### § 8. Zbywanie i obciążanie akcji

- **Ocena:** zgodne warunkowo.
- **Podstawa:** art. 300³⁹ § 1–6, art. 300³⁴ § 6, art. 300³⁷ § 1 KSH **[Z]**; art. 57, 58, 353¹ KC **[Z]**.
- **Orzecznictwo:**
  - SN II CRN 60/93 (7.09.1993, OSN 1994/7–8/143) — zbycie udziałów bez wymaganej zgody spółki jest **bezskuteczne zawieszająco**, a późniejsza zgoda działa wstecz **[S]**; tak samo SN V CSK 274/21 i SA w Gdańsku V AGa 158/20 **[S]**;
  - SN I CSK 132/11 (1.12.2011) — skutki zależą od rodzaju ograniczenia (zgoda, pierwokup, pierwszeństwo) **[S]**.

  Orzeczenia dotyczą sp. z o.o. (art. 182 KSH), który ma tę samą klauzulę dyspozytywną co art. 300³⁹ § 2 (memorandum 1.2.1 **[Z]**). Stosowanie do P.S.A. przez analogię **[W]**.

- **Uwagi:**
  1. **Wyłączenie art. 300³⁹ § 3–5 (ust. 3)** jest dopuszczalne co do zasady (memorandum 1.2.1, wariant B). Granicą jest art. 58 § 2 i art. 353¹ KC: ograniczenie nie może bezterminowo wyłączyć zbywalności. Tu każda przyczyna odmowy jest przejściowa (lock-up, warunek zgody organu) albo usuwalna (nabywca spoza sankcji, przejęcie vestingu), więc realna droga wyjścia istnieje — **do obrony [W]**.
  2. **Ś1. Fikcja zgody po 14 dniach.** Podmiot prowadzący rejestr „uwzględnia ograniczenia co do rozporządzania akcją” (art. 300³⁴ § 6 **[Z]**) i może żądać dokumentu zgody. Zaświadczenie z ust. 1 zd. 3 to rozwiązuje, jeśli Spółka je wyda. Gdy Spółka odmówi wydania zaświadczenia, akcjonariusz nie ma czego przedstawić rejestrowi. Rekomendacja:
     - uzgodnić mechanizm z podmiotem prowadzącym rejestr przed aktem (memorandum 1.5.1);
     - rozważyć konstrukcję „sprzeciwu” z art. 300³⁹ § 1 („w inny sposób”): zbycie jest dopuszczalne, jeżeli Spółka nie zgłosi sprzeciwu w 14 dni (pkt 6.5).
  3. Lock-up 12 miesięcy jest bezpieczny jako ograniczenie czasowe (memorandum 1.2.1 **[Z]**).
  4. Przyczyna odmowy z lit. d (nabywca nie przejął vestingu) zamyka lukę wskazaną w memorandum 1.5.1 **[Z]**.

### § 9. Obowiązek zbycia akcji (vesting)

- **Ocena:** zgodne warunkowo, z zastrzeżeniem **W1, W2**.
- **Podstawa:**
  - KSH: art. 300¹ § 3, art. 300³³ § 1 pkt 10–11, art. 300³⁹ § 1, art. 300⁴⁵ § 1–2, art. 300⁴⁷ § 9, art. 300⁴⁹–300⁵⁰ **[Z]**;
  - KC: art. 64, art. 101 § 1 (pełnomocnictwo nieodwołalne) **[Z]**;
  - PIT: art. 17 ust. 2, art. 19, art. 11 ust. 2b **[Z]**.
- **Orzecznictwo:**
  - SN V CSK 522/18 (23.06.2020) — o zrzeczeniu się odwołania pełnomocnictwa i jego granicach decyduje stosunek podstawowy **[Z]**;
  - SN II CSKP 593/22 **[Z]** — wykonanie obowiązku przez wyrok (art. 64 KC).
- **Uwagi:**
  1. **W1.** Memorandum (1.5.2 **[Z]**) uznało zarzut obejścia przepisów o umorzeniu i akcjach własnych za słaby, bo w wersji 1.0-RC **nabywcą nie mogła być Spółka ani osoba działająca na jej rachunek** (art. 300⁴⁷ § 9). Zastrzegło, że zarzut byłby realny, gdyby nabywał podmiot finansowany przez Spółkę.

     Wersja 2.0-S idzie dalej: nabywcą może być sama Spółka (§ 9 ust. 4), po cenie emisyjnej (§ 3 ust. 8 lit. b), a akcje własne może potem umorzyć (§ 3 ust. 7 lit. a). Ekonomicznie to umorzenie przymusowe ze spłatą 0,01 zł. Tymczasem przy umorzeniu przymusowym spłata „nie może być niższa od wartości godziwej” (art. 300⁴⁵ § 2 **[Z]**). Grozi zarzut obejścia ustawy (art. 58 § 1 KC) **[W]**.

     Rekomendacja (pkt 6.2): w mechanizmie vestingu nabywcą jest osoba wskazana przez Radę, niebędąca Spółką ani osobą działającą na jej rachunek. Jeżeli nabywa Spółka — tylko w celu przekazania akcji uczestnikom programu P albo założycielom serii F (§ 3 ust. 7 lit. b), z zakazem umorzenia.

  2. **W2.** § 9 ust. 7 mówi, że obowiązek obciąża każdoczesnego posiadacza. Nie mówi jednak, że zdarzenia dotyczące pierwotnego Akcjonariusza Funkcjonalnego uruchamiają obowiązek także u nabywcy. Memorandum (1.5.1 **[Z]**) uznało to za „konieczne” i podało brzmienie (pkt 6.3).
  3. Reprezentacja Spółki w umowie wykonawczej z założycielem-dyrektorem — **K1**.
  4. Podatek: odkup po cenie emisyjnej to dla odchodzącego zbycie poniżej wartości rynkowej. Organ może szacować przychód (art. 19 PIT), ale mechanizm z umowy spółki jest „uzasadnioną przyczyną” — warto to opisać w umowie wykonawczej (T9 pkt 6 **[Z/W]**).

### § 10–11. Rada Dyrektorów i reprezentacja

- **Ocena:** zgodne, z zastrzeżeniem **Ś2** i **K1**.
- **Podstawa:** art. 300⁵⁵ § 1, art. 300⁵⁸ § 2, art. 300⁷³ § 1 i 3, art. 300⁷⁵ § 2–3, art. 300⁷⁶, art. 300⁷⁹ § 1–4 KSH **[Z]**; art. 15 § 1 KSH **[Z]**.
- **Orzecznictwo:**
  - SN II CSKP 1733/22 (8.11.2024) — umowa z członkiem zarządu a art. 210 KSH; glosy wskazują na nieważność bezwzględną jako pogląd przeważający **[S]**. W P.S.A. odpowiednikiem jest art. 300⁷⁹ § 1.
  - Uchwała SN (7) III CZP 13/13 z 18.09.2013 r. — zaskarżanie uchwał organów zarządzających powództwem o ustalenie **[W]** (w repo oznaczona jako niedostępna).
- **Uwagi:**
  1. **Ś2.** Art. 15 § 1 KSH nie wymienia dyrektora P.S.A., więc pożyczka, kredyt albo poręczenie dla dyrektora nie wymaga zgody WZ z ustawy (memorandum pkt 2.2.4 **[Z]**). Wersja 1.0-RC miała ten wymóg w umowie, a 2.0-S go nie ma. Rekomendacja: przywrócić (pkt 6.6).
  2. Wyłączenie dyrektora w konflikcie od quorum (§ 10 ust. 6) jest spójne z art. 300⁵⁵ § 1. Jeżeli wszyscy dyrektorzy są w konflikcie, Rada nie podejmie uchwały i sprawa przechodzi do WZ — dla relacji z Appolonią rozwiązuje to § 15 ust. 6.
  3. § 11 ust. 3 poprawnie odtwarza art. 300⁷⁹ § 1 i 3. Brakuje jednak samej uchwały o pełnomocniku przy zawiązaniu — **K1**.
  4. Business judgment rule: dyrektor P.S.A. nie narusza obowiązku staranności, jeżeli działa lojalnie, w granicach uzasadnionego ryzyka gospodarczego i na podstawie informacji (art. 300¹²⁵ § 2 KSH, od 13.10.2022 r.) **[S]**. Lojalność jest warunkiem ochrony — patrz punkt 3.2.

### § 12. Uchwały akcjonariuszy

- **Ocena:** zgodne warunkowo, z zastrzeżeniem **W3**.
- **Podstawa:** art. 300⁸⁰ § 1–3, art. 300⁹² KSH (udział zdalny jako opcja umowna, szczegóły w regulaminie) **[Z]**.
- **Uwagi:**
  1. **W3.** Uchwała obiegowa „zostaje podjęta, gdy w terminie oddano głosy »za« w liczbie wymaganej”, a wynik stwierdza się „po uzyskaniu wymaganej liczby głosów”. Przy progu „bezwzględnej większości głosów oddanych” wynik zależy od wszystkich głosów oddanych w terminie. Wcześniejsze zamknięcie odbiera pozostałym akcjonariuszom możliwość zmiany wyniku, a to podstawa do zaskarżenia. Poprawka w pkt 6.4.
  2. Regulamin WZ przyjmowany przy zawiązaniu usuwa zarzut z memorandum (art. 300⁹² § 2 odsyła do regulaminu, a zawiadomienie nim nie jest).
  3. Doręczenie „z chwilą wysłania” na adres z rejestru jest oparte na zgodzie akcjonariusza z § 3 ust. 6. Ryzyko sporu o skuteczność doręczenia zmniejsza archiwum z ust. 8.

### § 13. Sprawy zastrzeżone dla WZ

- **Ocena:** zgodne.
- **Podstawa:** art. 300⁷⁵ § 2, art. 300⁸¹ pkt 3 KSH **[Z]**.
- **Uwaga:** dodać zgodę na umowy kredytu, pożyczki i poręczenia z dyrektorami — **Ś2**.

### § 14. Własność intelektualna, poufność, eksport, konkurencja

- **Ocena:** zgodne warunkowo.
- **Podstawa:**
  - prawo autorskie: art. 9, 12, 16, 41 ust. 2–4, 46, 50, 53, 74 ust. 3–4 **[Z]**; art. 43 ust. 1 **[S/W]**; art. 67 ust. 5 **[S]**; art. 68 ust. 1–2 **[S]**;
  - PWP: art. 11 ust. 3, art. 12, art. 67 **[Z]**;
  - KSH: art. 300¹ § 3 (obowiązki akcjonariuszy tylko z umowy spółki) **[Z]**.
- **Orzecznictwo:**
  - SN I CK 381/05, III CK 124/05 — pola eksploatacji **[S]**;
  - SN I CSKP 62/21 (13.05.2021) — licencja niewyłączna nie wymaga formy pisemnej i może powstać w sposób dorozumiany (wyjątek: zamówienia publiczne) **[S]**;
  - SA w Warszawie VI ACa 1735/14 — kontynuowanie współpracy jako licencja dorozumiana **[S]**;
  - SN II CK 51/04 (15.10.2004) — spór o zakres art. 68 ust. 2 **[S]**.
- **Uwagi:**
  1. **Ś6.** Art. 41 ust. 3 pr. aut. unieważnia umowę „w części dotyczącej wszystkich utworów lub wszystkich utworów określonego rodzaju tego samego twórcy mających powstać w przyszłości”. Nie znaleziono orzeczenia SN wprost o tym przepisie [S — wynik negatywny]. Bezpieczna jest konstrukcja „utwory powstałe w wykonaniu danej umowy” (memorandum 3.1.3 **[Z]**). Dlatego ważne są:
     - kwartalne potwierdzenia (lit. e), które dotyczą utworów już istniejących i oznaczonych;
     - umowa o pracę albo B2B dla założycieli. Przy umowie o pracę programy przechodzą z mocy prawa (art. 74 ust. 3).
  2. **Licencja dorozumiana jako tarcza awaryjna.** Orzecznictwo dopuszcza ją dla licencji niewyłącznej (I CSKP 62/21, VI ACa 1735/14 **[S]**). Spółka korzystająca z kodu założyciela bez umowy nie jest więc bez obrony. Taka licencja jest jednak niewyłączna, ma zakres ustalany z okoliczności i jest wypowiadalna (art. 68). Nie zastąpi przeniesienia praw.
  3. **Licencja na 5 lat (ust. 2).** Licencja zawarta na dłużej niż 5 lat jest po 5 latach traktowana jak udzielona na czas nieoznaczony, a taką można wypowiedzieć na rok naprzód na koniec roku kalendarzowego (art. 68 ust. 1–2 **[S]**). Licencji „wieczystej” prawo polskie nie przewiduje (projekt zmiany nieuchwalony **[S]**). Dlatego obowiązek przeniesienia na żądanie Rady jest właściwym uzupełnieniem.
  4. **Forma.** Przeniesienie praw autorskich (art. 53) i licencja wyłączna (art. 67 ust. 5) wymagają formy pisemnej pod rygorem nieważności **[S]**. Jest projekt zastąpienia jej formą dokumentową; w lipcu 2026 r. nie obowiązywał **[S]**. Umowa trzyma się formy pisemnej, co jest bezpieczne w obu stanach prawnych.
  5. **Ś5.** Zdanie „Każdy Założyciel, dyrektor, pracownik i współpracownik zawiera ze Spółką umowę” nie wiąże pracowników i współpracowników, bo nie są stronami umowy spółki. Należy je przeformułować na obowiązek Spółki (pkt 6.7).
  6. **Ś4.** Zakaz konkurencji akcjonariuszy jest dopuszczalny jako obowiązek z umowy spółki (art. 300¹ § 3 **[Z]**), ale obejmuje też przyszłych inwestorów finansowych.
  7. **Odszkodowania za naruszenie.** Ryczałt w wysokości trzykrotności wynagrodzenia jest niekonstytucyjny (TK SK 32/14, 23.06.2015, Dz.U. 2015 poz. 932 **[S]**). Dwukrotność jest zgodna z prawem UE (TSUE C-367/15, 25.01.2017 **[S]**). Ma to znaczenie przy wycenie ryzyka korzystania z cudzego kodu.

### § 15. Współpraca ze Spółką Siostrzaną — patrz punkt 3.

### § 16–18. Zysk, likwidacja, postanowienia końcowe

- **Ocena:** zgodne.
- **Podstawa:** art. 300¹⁵ KSH **[Z]**; art. 300⁹⁸ § 3–5 KSH (zgoda dotkniętych przy zwiększeniu świadczeń) **[Z]**.
- **Uwagi:**
  - **N1–N3:** rok obrotowy, zaliczki, głos zastawnika (porównanie z S24 w `prosta.md`);
  - **N5:** mediacja nie może wydłużać ustawowych terminów zaskarżenia uchwał;
  - § 18 ust. 6 — dopisać uchwałę o pełnomocniku (**K1**).

### Załącznik nr 1

- **Ocena:** zgodne co do struktury.
- **Podstawa:** art. 300⁵ § 1 pkt 4 KSH — przedmiot wkładu, osoba, serie i numery akcji **[Z]**.
- **Uwagi:**
  - wartości i podstawy wyceny są puste — **K3**;
  - spójność z oświadczeniem dyrektorów o kapitale (art. 300¹² § 3 pkt 2 **[Z]**).

---

## 3. Struktura Basilisk–Appolonia

### 3.1. § 15 — Spółka Siostrzana: ocena ogólna

Konstrukcja jest dopuszczalna jako postanowienia umowne obu umów spółek (art. 300¹ § 3 KSH **[Z]**, art. 353¹ KC **[Z]**). Wyłączenia zakazu konkurencji i poufności działają, bo te obowiązki wynikają z samej umowy, którą wspólnicy mogą kształtować. Słabszy jest punkt dotyczący konfliktu interesów (3.2), bo tam działa także ustawa.

### 3.2. Konflikt interesów (W4)

- **Ustawa.** Dyrektor, którego interes jest sprzeczny z interesem spółki, ma obowiązek to ujawnić i wstrzymać się od udziału w rozstrzyganiu sprawy (art. 300⁵⁵ § 1 KSH **[Z]**). Postanowienie § 15 ust. 6 („w zakresie dopuszczalnym przez prawo dyrektor nie jest wyłączony… wyłącznie z tego powodu, że jest jej akcjonariuszem, dyrektorem albo pracownikiem”) może wyłączyć tylko umowną część reżimu (§ 10 ust. 6). Ustawowego obowiązku wyłączyć nie może **[W]**.
- **Skutek naruszenia.** Według komentarzy naruszenie obowiązku wstrzymania się (odpowiednik art. 209 KSH) nie powoduje samo nieważności czynności, ale rodzi odpowiedzialność dyrektora. Przy rażącej nielojalności możliwa jest nieważność z art. 58 § 2 KC **[S — komentarze, bez sygnatury SN wprost]**.
- **Ochrona BJR** (art. 300¹²⁵ § 2 **[S]**) zakłada lojalność wobec spółki. Dyrektor, który na koszt Basilisk przesuwa wartość do Appolonii, jej nie dostanie.
- **Kiedy konflikt jest realny.** Dopóki akcjonariat obu spółek jest identyczny (te same osoby, te same proporcje), przesunięcie wartości nikomu nie szkodzi i konflikt jest formalny. Staje się realny, gdy:
  - w jednej spółce pojawi się seria F, P albo inwestor;
  - ktoś odejdzie z jednej spółki, a zostanie w drugiej;
  - proporcje w Appolonii od początku są inne.
- **Rekomendacje:**
  1. Umowę o Współpracy zawrzeć **teraz**, póki akcjonariat jest identyczny, i zatwierdzić jednomyślnie uchwałami WZ obu spółek (§ 13 lit. j).
  2. Formuły zamiast decyzji: IP według obszaru, usługi po koszcie z marżą, przychody ze wspólnych projektów według udziału w pracy.
  3. Spory o cenę rozstrzyga niezależny biegły.
  4. Przy wejściu inwestora do jednej spółki — przegląd umowy, ewentualnie niezależny dyrektor albo holding.

### 3.3. Dominacja przez unię personalną (W5)

- **Ustawa.** Spółką dominującą jest m.in. spółka, której członkowie zarządu stanowią ponad połowę członków zarządu innej spółki kapitałowej (art. 4 § 1 pkt 4 lit. d KSH **[S]**). W P.S.A. Rada Dyrektorów wykonuje kompetencje zarządu (art. 300⁷³ § 1 **[Z]**). Komentarze opisują identyczne zarządy jako „unię personalną” mieszczącą się w tym przepisie **[S]**.
- **Skutek.** Przy tych samych pięciu dyrektorach dominacja może istnieć formalnie **w obie strony** **[W]**.
- **Konsekwencje praktyczne:**
  1. Spółka dominująca ma 2 tygodnie na zawiadomienie spółki zależnej o dominacji. Inaczej traci prawo głosu z akcji powyżej 33% kapitału zakładowego zależnej, a uchwała podjęta z udziałem takich głosów jest nieważna, chyba że bez nich spełnia wymogi quorum i większości (art. 6 KSH **[S]**). Dopóki spółki nie mają swoich akcji, przepis nie ma praktycznego zastosowania. Zacznie mieć przy jakimkolwiek krzyżowym udziale (stosowanie progu „kapitału zakładowego” do kapitału akcyjnego P.S.A. — **[W]**).
  2. Akcje spółki „dominującej” nabywane przez „zależną” wliczają się do limitu akcji własnych (art. 300⁴⁷ **[Z/W]**).
- **Rekomendacja:**
  - bez wzajemnych udziałów (zgodnie z `analiza_ip_aport.md`, pkt 2);
  - przy rozroście — nie powielać w 100% składu Rad; wystarczy, że w jednej spółce co najmniej połowa dyrektorów nie zasiada w drugiej.

### 3.4. Grupa spółek (prawo holdingowe)

- **Ustawa.** Od 13.10.2022 r. KSH reguluje „grupę spółek” (art. 21¹–21¹⁶ KSH, Dz.U. 2022 poz. 807 **[S]**):
  - spółka dominująca i uczestnicząca w grupie spółka zależna kierują się, obok własnego interesu, interesem grupy, jeśli nie szkodzi to wierzycielom i wspólnikom mniejszościowym spółki zależnej;
  - spółka dominująca może wydawać wiążące polecenia, w formie pisemnej albo elektronicznej pod rygorem nieważności;
  - spółka zależna musi odmówić wykonania polecenia, które groziłoby jej niewypłacalnością;
  - uczestnictwo wymaga uchwały wspólników spółki zależnej większością 3/4 i wpisu do KRS;
  - P.S.A. może uczestniczyć w grupie **[S]**.
- **Ocena.** To prawne narzędzie, które najsilniej zmniejsza zarzut konfliktu interesów. Wymaga jednak spółki dominującej (holding albo jedna spółka jako matka), więc między dwiema siostrami bez holdingu nie zadziała.
- **Rekomendacja:** rozważyć przy holdingu (`analiza_ip_aport.md`, wariant D). Numerację przepisów sprawdzić w tekście ujednoliconym.

### 3.5. Własność intelektualna między spółkami

- **Forma i co przechodzi:**
  - przeniesienie i licencja wyłączna wymagają formy pisemnej pod rygorem nieważności **[S]**;
  - licencja niewyłączna formy nie wymaga i może powstać w sposób dorozumiany (SN I CSKP 62/21 **[S]**), ale jest niepewna i wypowiadalna (art. 68 **[S]**);
  - wspólnie tworzony kod bez przydziału to utwór współtwórców: do korzystania z całości potrzebna jest zgoda wszystkich (art. 9 ust. 3 **[Z]**);
  - pracownik jednej spółki tworzący dla drugiej przenosi prawa na swojego pracodawcę (art. 12, 74 ust. 3 **[Z]**).
- **Ocena.** § 15 ust. 5 (`psa_simple2`) porządkuje formę i przydział. Wykonanie zależy od Umowy o Współpracy (**Ś10**).
- **Rekomendacja.** W Umowie o Współpracy:
  - licencje na czas oznaczony do 5 lat z obowiązkiem odnowienia albo z długimi umownymi terminami wypowiedzenia (art. 68 ust. 1 dopuszcza „terminy umowne”);
  - przeniesienie praw do wyników wspólnych na jedną spółkę;
  - rejestr przekazanych utworów.

### 3.6. Konsorcjum, przetargi, granty

- **Konsorcjum a spółka cywilna.** Umowa konsorcjum co do zasady nie jest spółką cywilną, chyba że strony tak ją ukształtują. Może być umową nienazwaną, podtypem spółki cywilnej albo spółką cywilną — zależy od treści (SA w Warszawie VI ACa 357/16 i omówienia **[S]**). Przy kwalifikacji jako spółka cywilna obie spółki odpowiadają solidarnie za zobowiązania (art. 864 KC **[W]**). Rekomendacja: w Umowie o Współpracy brak wspólnego majątku i wyraźne wyłączenie spółki cywilnej.
- **Zamówienia publiczne:**
  - osobne oferty dwóch wykonawców z tej samej grupy kapitałowej grożą wykluczeniem, chyba że wykażą, że oferty przygotowali niezależnie (art. 108 ust. 1 pkt 5 Pzp, orzecznictwo KIO **[S]**);
  - grupa kapitałowa w Pzp jest rozumiana według art. 4 pkt 14 u.o.k.k. **[S]**; czy siostry kontrolowane przez osoby fizyczne nią są, zależy od definicji przedsiębiorcy w u.o.k.k. **[W]**;
  - bezpieczniej startować wspólnie;
  - wykonawcy wspólni odpowiadają solidarnie za wykonanie umowy (art. 445 Pzp **[W]**; wcześniej art. 141 Pzp z 2004 r. **[S]**), więc w Umowie o Współpracy potrzebny jest podział odpowiedzialności i regres.
- **EDF.** Konsorcjum co najmniej 3 podmiotów z 3 państw członkowskich albo stowarzyszonych **[S]**. Wymóg, aby część członków nie była kontrolowana przez ten sam podmiot, występuje w programie poprzednim i w projektach przepisów — brzmienie ostateczne do sprawdzenia w tekście ujednoliconym rozporządzenia 2021/697 **[S/W]**. Basilisk i Appolonia same nie wystarczą.

### 3.7. Podatki między spółkami

- **Nieodpłatne świadczenia.** Szerokie pojęcie nieodpłatnego świadczenia — uchwała NSA II FPS 1/06 z 16.10.2006 r. (podtrzymująca FPS 9/02) **[S]**. Darmowa licencja albo usługa od siostry może być przychodem odbiorcy (art. 12 ust. 1 pkt 2 CIT **[W]**).
- **Ceny transferowe.** Spółki z tymi samymi właścicielami są podmiotami powiązanymi (art. 11a CIT, próg 25% **[W]**): obowiązuje cena rynkowa, a powyżej progów — dokumentacja (memorandum T9 pkt 7).
- **Rekomendacja:** w Umowie o Współpracy ceny ustalane z metodologią (koszt plus marża, stawki godzinowe) i przegląd raz w roku.

### 3.8. Umowa Appolonii (Ś11)

Stan na gałęzi `psa_appolonia`:

| Element | Stan |
|------------|-------|
| § 15 o Spółce Siostrzanej | jest, lustrzany |
| Wykup akcji z zabezpieczeniami (§ 3 ust. 7–8) | jest |
| Cywilne brzmienie, bez kodów wojskowych | tak |
| Poprawki IP z `psa_simple2` (§ 4 ust. 5, § 14 ust. 1–2, § 15 ust. 5) | **brak** — trzeba przenieść |
| Siedziba | pole do uzupełnienia |
| Firma „Appolonia” | do potwierdzenia pisowni („Apollonia”?) |
| Kody PKD (11, w tym 30.11.Z i 33.15.Z) | do weryfikacji; typowo morskie kody usługowe niedodane |
| Ryzyka K1–K3, W1–W3, Ś1–Ś9 | dotyczą Appolonii **tak samo** jak Basilisk |

---

## 4. Orzecznictwo — zestawienie

| Sygnatura | Sąd, data | Teza (w zakresie istotnym dla audytu) | Zastosowanie | Weryf. |
|-----|-----|---------------|-----|--|
| II CSKP 593/22 | SN, 9.12.2022 | Art. 64 KC nie tworzy obowiązku, ale wyrok zastępuje oświadczenie potrzebne do wykonania istniejącego obowiązku | § 4 ust. 5, § 9 | [Z] |
| V CSK 522/18 | SN, 23.06.2020 | Stosunek podstawowy wyznacza dopuszczalność zrzeczenia się odwołania pełnomocnictwa i jego granice | § 9 ust. 6 | [Z] |
| III CZP 109/22 | SN | Ustanowienie rozdzielności majątkowej nie daje drugiemu małżonkowi praw korporacyjnych | akcje w majątku wspólnym (klauzula usunięta w 2.0-S) | [Z] |
| III CSKP 65/21 | SN | Akcjonariuszem jest małżonek, który objął akcje i jest wpisany do rejestru | jw. | [Z] |
| III CZP 32/16 | SN | Udziały mogą należeć do majątku wspólnego (stosowane do akcji przez analogię) | jw. | [Z] |
| III CZP 13/13 | SN (7), 18.09.2013 | Zaskarżanie uchwał organów zarządzających — powództwo o ustalenie | uchwały Rady | [W] |
| II CRN 60/93 | SN, 7.09.1993 | Zbycie bez wymaganej zgody spółki — bezskuteczność zawieszona; zgoda działa wstecz | § 8 | [S] |
| V CSK 274/21 | SN | Brak zgody na zbycie — bezskuteczność zawieszona, nie nieważność (powołuje II CRN 60/93) | § 8 | [S] |
| I CSK 132/11 | SN, 1.12.2011 | Skutki naruszenia ograniczeń zbywalności zależą od rodzaju ograniczenia | § 8 | [S] |
| V AGa 158/20 | SA w Gdańsku, 9.02.2021 | Umowa zawarta bez zgody organu — bezskuteczność zawieszona | § 8 | [S] |
| II CSKP 1733/22 | SN, 8.11.2024 | Umowa z członkiem zarządu a art. 210 KSH (glosy: nieważność bezwzględna jako pogląd przeważający) | § 11 ust. 3, K1 (art. 300⁷⁹) | [S] |
| I CK 381/05 | SN, 8.03.2006 | Pola eksploatacji muszą być wyraźnie wymienione; art. 41 ust. 4 wyklucza pola nieznane | § 14 ust. 1 lit. b | [S] |
| III CK 124/05 | SN, 14.09.2005 | Umowa licencyjna obejmuje wyraźnie wymienione pola znane w chwili zawarcia | jw. | [S] |
| I CSKP 62/21 | SN, 13.05.2021 | Licencja niewyłączna nie wymaga formy pisemnej, może powstać konkludentnie (z wyjątkiem zamówień publicznych) | § 4 ust. 5, § 14, § 15 | [S] |
| VI ACa 1735/14 | SA w Warszawie | Kontynuowanie współpracy na dotychczasowych warunkach jako licencja niewyłączna per facta concludentia | § 14 | [S] |
| II CK 51/04 | SN, 15.10.2004 | Zakres art. 68 ust. 2 pr. aut. (spór w doktrynie) | § 14 ust. 2 | [S] |
| SK 32/14 | TK, 23.06.2015 (Dz.U. 2015 poz. 932) | Ryczałt trzykrotności wynagrodzenia za zawinione naruszenie — niezgodny z Konstytucją | ryzyko naruszeń IP | [S] |
| C-367/15 | TSUE, 25.01.2017 | Odszkodowanie w wysokości dwukrotności opłaty licencyjnej zgodne z dyrektywą 2004/48/WE | jw. | [S] |
| VI ACa 357/16 | SA w Warszawie | Umowa konsorcjum może być podtypem spółki cywilnej, spółką cywilną albo umową samodzielną | konsorcjum (3.6) | [S] |
| II FPS 1/06 | NSA (uchwała), 16.10.2006 | Szerokie pojęcie nieodpłatnego świadczenia (podtrzymanie FPS 9/02) | licencje nieodpłatne (3.7) | [S] |
| KIO (wybór) | KIO | Odrębne oferty wykonawców z jednej grupy kapitałowej — wykluczenie bez wykazania niezależności | przetargi (3.6) | [S] |

**Luki w orzecznictwie** (wynik negatywny wyszukiwania): nie znaleziono orzeczenia SN wprost o art. 41 ust. 3 pr. aut., o art. 300⁷⁹ KSH ani o fikcji zgody na zbycie akcji P.S.A. Ocenę opiera się na tekście ustawy, analogii do sp. z o.o. i S.A. oraz komentarzach.

---

## 5. Lista kontrolna poza umową

**Przed aktem**

1. Uzgodnić z podmiotem prowadzącym rejestr akcjonariuszy wzmianki (vesting, lock-up) i przyjmowanie zaświadczeń o zgodzie (§ 8 ust. 1).
2. Wycena wkładów niepieniężnych z uzasadnieniem, spójna z PIT (K3).
3. Wykazy do aportu: repozytoria z commitami i sumami kontrolnymi, współtwórcy, komponenty open source z licencjami, oświadczenia o braku praw byłych pracodawców i uczelni (memorandum T4).
4. Weryfikacja kodów PKD 2025.

**Przy akcie**

1. Uchwała akcjonariuszy o **pełnomocniku Spółki** do umów z dyrektorami (K1).
2. Umowy przeniesienia aportu podpisane przez pełnomocnika ze strony Spółki (K1, K2).
3. Umowy wykonawcze vestingu z pełnomocnictwami — również przez pełnomocnika (K1).
4. Regulamin WZ (§ 12 ust. 5), wybór podmiotu prowadzącego rejestr, pierwsi dyrektorzy.

**Po wpisie**

1. Wzmianki w rejestrze akcjonariuszy (art. 300³³ § 1 pkt 10–11; od 18.02.2027 r. obowiązek zgłoszenia w 7 dni pod groźbą grzywny **[Z]**).
2. CRBR, NIP, VAT-R **[W]**.
3. Umowy o pracę albo B2B założycieli z klauzulami IP; kwartalne potwierdzenia utworów podpisywane przez pełnomocnika.
4. Umowa o Współpracy z Appolonią, zatwierdzona uchwałami WZ obu spółek.
5. Wnioski o interpretacje podatkowe (aport IP, licencje nieodpłatne, odkup po cenie emisyjnej, seria F i P).

---

## 6. Proponowane brzmienia

### 6.1. K1 — pełnomocnik do umów z dyrektorami

§ 11 ust. 3 — nowe zdanie drugie:

> „Uchwała akcjonariuszy może powołać pełnomocnika do zawierania i wykonywania z dyrektorami umów określonego rodzaju, w szczególności umów, o których mowa w § 4 ust. 5, § 9 ust. 6 i § 14 ust. 1, oraz potwierdzeń, o których mowa w § 14 ust. 1 lit. e.”

§ 18 ust. 6 — dopisać po „pierwszy regulamin Walnego Zgromadzenia”:

> „…oraz pełnomocnika Spółki, o którym mowa w art. 300⁷⁹ § 1 KSH, do zawarcia z Założycielami będącymi dyrektorami umów, o których mowa w § 4 ust. 5 i § 9 ust. 6…”

**Do weryfikacji:** dopuszczalność pełnomocnika „rodzajowego” na tle art. 300⁷⁹ § 1. Ostrożnie — osobny pełnomocnik do każdego pakietu umów. Pełnomocnikiem nie powinna być osoba, z którą Spółka zawiera daną umowę.

### 6.2. W1 — nabywca akcji niezwolnionych

§ 9 ust. 4 zdanie pierwsze:

> „…akcje niezwolnione podlegają zbyciu — po cenie równej ich cenie emisyjnej — na rzecz nabywcy wskazanego przez Radę Dyrektorów, niebędącego Spółką ani osobą działającą na jej rachunek, w szczególności innego akcjonariusza albo uczestnika programu motywacyjnego. Spółka może nabyć te akcje wyłącznie w celu, o którym mowa w § 3 ust. 7 lit. b; akcji tak nabytych nie umarza się.”

§ 3 ust. 7 lit. c — skreślić albo zastąpić odesłaniem do lit. b.

### 6.3. W2 — nabywca wtórny

§ 9 ust. 7 — dodać:

> „Zdarzenia dotyczące Akcjonariusza Funkcjonalnego, od którego akcje pochodzą, uruchamiają obowiązek zbycia także wobec nabywcy tych akcji.”

(memorandum 1.5.1)

### 6.4. W3 — uchwały obiegowe

§ 12 ust. 3 zdanie trzecie:

> „Uchwała zostaje podjęta z upływem terminu oddania głosu, jeżeli oddano za nią wymaganą większość głosów. Przed upływem terminu uchwała zostaje podjęta z chwilą, gdy za uchwałą oddano głosy stanowiące wymaganą większość wszystkich głosów w Spółce, bez względu na głosy, które mogłyby zostać oddane później.”

### 6.5. Ś1 — sprzeciw zamiast fikcji zgody (wariant)

§ 8 ust. 1 zdanie trzecie:

> „Rozporządzenie akcją jest dopuszczalne, jeżeli Rada Dyrektorów nie zgłosi sprzeciwu w formie dokumentowej w terminie 14 dni od zgłoszenia; sprzeciw może być oparty wyłącznie na przyczynach z ust. 2.”

### 6.6. Ś2 — umowy finansowe z dyrektorami

§ 13 ust. 1 — nowa lit. k:

> „zawarcie przez Spółkę umowy kredytu, pożyczki, poręczenia lub innej podobnej umowy z dyrektorem, prokurentem albo likwidatorem albo na rzecz którejkolwiek z tych osób.”

### 6.7. Ś5 — umowy IP z pracownikami i współpracownikami

§ 14 ust. 1 zdanie drugie:

> „Spółka zawiera z każdym dyrektorem, pracownikiem i współpracownikiem umowę zapewniającą nabycie przez Spółkę tych praw oraz przeniesienie nośników i dokumentacji, a Założyciele są obowiązani zawrzeć taką umowę.”

### 6.8. N4 — limit czasu upoważnienia do nabycia akcji własnych

§ 3 ust. 7 — dodać:

> „Upoważnienie dla Rady Dyrektorów do nabywania akcji własnych udziela się na okres nie dłuższy niż 5 lat.”

---

## 7. Pytania do prawnika i doradcy podatkowego

1. **Art. 300⁷⁹ § 1 KSH.** Czy pełnomocnik może zostać powołany do rodzaju umów (IP, umowy wykonawcze, kwartalne potwierdzenia) czy do każdej umowy osobno? Czy pełnomocnikiem może być inny założyciel-dyrektor?
2. **Odkup akcji niezwolnionych po cenie emisyjnej** (W1). Czy przy nabywcy innym niż Spółka zarzut obejścia art. 300⁴⁵ § 2 KSH jest wykluczony? Jakie są granice dyskonta przy good i bad leaver?
3. **Fikcja zgody albo sprzeciw** (§ 8 ust. 1). Która konstrukcja jest bezpieczniejsza wobec art. 300³⁴ § 6 KSH i praktyki podmiotów prowadzących rejestr?
4. **Art. 41 ust. 3 pr. aut.** Czy przejście praw „z chwilą przekazania” bez stosunku podstawowego jest ważne? Czy kwartalne potwierdzenia wystarczą?
5. **Art. 4 § 1 pkt 4 lit. d i art. 6 KSH.** Jak stosować je do P.S.A. z Radą Dyrektorów i do „wzajemnej” dominacji sióstr? Jak art. 6 stosuje się do kapitału akcyjnego?
6. **Grupa spółek** (art. 21¹ i nast. KSH). Czy przy holdingu warto formalnie utworzyć grupę? Jakie będą skutki dla wspólników mniejszościowych?
7. **Pzp i EDF.** Czy Basilisk i Appolonia są „grupą kapitałową” w rozumieniu u.o.k.k.? Jakie jest ostateczne brzmienie wymogu niezależności członków konsorcjum EDF?
8. **Podatki:**
   - PIT od aportu IP (wartość i koszt);
   - przychód Spółki z licencji nieodpłatnych (§ 14 ust. 2);
   - odkup po cenie emisyjnej (art. 19 PIT);
   - seria F za pracę;
   - preferencja z art. 24 ust. 11 PIT dla serii P;
   - ceny transferowe między spółkami siostrzanymi;
   - wymiana akcji przy holdingu (art. 24 ust. 8a PIT).

---

## Źródła wykorzystane w toku audytu

**Repozytorium:** `memorandum.md` (pytania 1.1.4, 1.2.1, 1.3.5, 1.5.1, 1.5.2, 2.2.4, 2.3.3, 3.1.1–3.1.3; tematy T4, T9), `psa_feedback.tex` (linki do sn.pl i eli.gov.pl), `prosta.md`, `analiza_ip_aport.md`, rozporządzenie MS w sprawie wzorca S24 (Dz.U. 2021 poz. 1191, plik przekazany przez użytkownika).

**Wyszukiwanie (poziom [S]):**

Prawo spółek

- art. 300⁷⁹ KSH: [lexlege.pl](https://lexlege.pl/ksh/art-300-79/)
- art. 300³⁹ KSH: [lexlege.pl](https://lexlege.pl/ksh/art-300-39/)
- art. 4 KSH: [lexlege.pl](https://lexlege.pl/ksh/art-4/); unia personalna: [rp.pl](https://pro.rp.pl/prawo-w-firmie/art13279531-powolywanie-tych-samych-osob-do-zarzadow-spolek-zaleznych-moze-byc-ryzykowne)
- art. 6 KSH: [lexlege.pl](https://lexlege.pl/ksh/art-6/)
- Grupa spółek: [Dz.U. 2022 poz. 807](https://api.sejm.gov.pl/eli/acts/DU/2022/807/text/T/D20220807L.pdf), [lexlege.pl — dział IV](https://lexlege.pl/ksh/dzial-iv-grupa-spolek/15384/)
- BJR w P.S.A.: [codozasady.pl](https://codozasady.pl/en/p/the-business-judgment-rule), [apcz.umk.pl](https://apcz.umk.pl/SIT/article/view/36110)
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
