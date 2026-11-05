# Analiza: brak przeniesienia praw autorskich i „krzyżowy aport” akcji

Dotyczy: Basilisk Systems P.S.A. (ląd i powietrze) i Appolonia P.S.A. (morze), ci sami założyciele, umowa w wariancie prostym z § 15 o Spółce Siostrzanej. Gałąź `psa_simple2`.

**Pytania**

1. Co, jeśli wspólnicy powiedzą, że brak przeniesienia praw autorskich — od osoby prywatnej albo między spółkami — będzie rodził skutki prawne?
2. Czy akcje mogą być krzyżowym aportem?

Oznaczenia źródeł: „(memorandum x.y)” — teza zweryfikowana w `memorandum.md` na tekście przepisu. „**do weryfikacji**” — teza z wiedzy ogólnej, do potwierdzenia u prawnika albo doradcy podatkowego.

---

## Krótko

1. **Wspólnicy mają rację co do zasady.** Prawa autorskie zostają przy twórcy, dopóki nie podpisze pisemnej umowy przeniesienia z wymienionymi polami eksploatacji (art. 53 i art. 41 ust. 2 pr. aut.). Wyjątkiem są pracownicy: ich utwory, a zwłaszcza programy komputerowe, przechodzą na pracodawcę z mocy prawa (art. 12, art. 74 ust. 3). Sama umowa spółki praw nie przenosi (memorandum T4). Najgroźniejsze luki:
   - założyciele-dyrektorzy bez umowy o pracę — kod, który piszą, zostaje ich;
   - aport kodu bez prawidłowej umowy przeniesienia — wkład w ogóle nie został wniesiony;
   - korzystanie przez jedną spółkę z kodu drugiej bez licencji.
2. **Da się to zamknąć.** Na `psa_simple2` zmieniłem § 4 ust. 6, § 14 ust. 1–2 i § 15 ust. 5 (szczegóły w punkcie 1.4). Po tych zmianach wspólnik nie może skutecznie „przetrzymać” praw:
   - aport jest przenoszony w dniu aktu;
   - do czasu przeniesienia Spółka ma licencję;
   - obowiązek przeniesienia da się wyegzekwować wyrokiem (art. 64 KC);
   - nowy kod jest co kwartał przenoszony pisemnie z wykazem utworów.
3. **Krzyżowy aport — formalnie tak, praktycznie odradzam.**
   - Akcje innej spółki mogą być wkładem niepieniężnym.
   - Bezpośrednia wymiana „nowe akcje Basilisk za nowe akcje Appolonii” między samymi spółkami nie działa: spółka nie może wnieść ani objąć własnych akcji.
   - Wzajemne udziały można zbudować tylko innym aktywem albo akcjami wnoszonymi przez założycieli. To jednak rodzi problemy: stosunek dominacji (te same osoby w Radach), limit akcji własnych, dublowanie kapitału, podatki, kolizję z vestingiem i lock-upem.
   - Na teraz lepszy jest § 15 + Umowa o Współpracy. Gdy będzie potrzeba połączenia, właściwą drogą jest holding przez wymianę akcji.

---

## 1. Brak przeniesienia praw autorskich

### 1.1. Gdzie prawa przechodzą same, a gdzie nie

| Kto stworzył | Czy prawa przechodzą na Spółkę bez osobnej umowy | Co jest potrzebne | Źródło |
|---|---|---|---|
| **Pracownik** (umowa o pracę) | **Tak** — z chwilą przyjęcia utworu, w granicach celu umowy; programy komputerowe przysługują pracodawcy z mocy prawa | Klauzula w umowie o pracę obejmująca utwory spoza ścisłych obowiązków; pola eksploatacji przy innych utworach | art. 12 ust. 1, art. 74 ust. 3 pr. aut. (memorandum 3.1.3) |
| **Założyciel-dyrektor bez umowy o pracę** (sam akt powołania) | **Nie** — art. 12 i 74 ust. 3 dotyczą tylko pracowników | Pisemna umowa przeniesienia z polami eksploatacji | art. 53, art. 41 ust. 2 (memorandum 3.1.3) |
| **Współpracownik B2B / umowa o dzieło** | **Nie** dla praw autorskich; **tak** dla prawa do patentu na wynalazek z realizacji umowy | Pisemna umowa przeniesienia; utwory „powstałe w wykonaniu tej umowy”, a nie „wszystkie przyszłe” | art. 41 ust. 3 pr. aut.; art. 11 ust. 3 PWP (memorandum 3.1.3) |
| **Kod sprzed założenia, wnoszony aportem** | **Nie** — umowa spółki sama nie przenosi | Odrębna umowa przeniesienia w dniu aktu, z oznaczeniem utworów (repozytorium, commit, sumy kontrolne) | memorandum T4 |
| **Kod sprzed założenia, niewnoszony** | **Nie** — zostaje u założyciela | Licencja albo przeniesienie | § 14 ust. 2 |
| **Kilku współtwórców** | Każdy ma udział | Umowę podpisuje **każdy** współtwórca | art. 9 pr. aut. (memorandum 3.1.3) |
| **Uczelnia, były pracodawca, grant** | Mogą mieć tytuł do części kodu albo prawo pierwszeństwa publikacji | Oświadczenia i zgody | art. 12, 14 pr. aut.; art. 11 PWP (memorandum 3.1.3) |
| **Pracownik jednej spółki siostrzanej pracujący dla drugiej** | Prawa nabywa **pracodawca**, czyli nie ta spółka, której obszaru dotyczy utwór | Umowa między spółkami albo umowa z osobą wskazująca właściwą spółkę | art. 12, 74 ust. 3 pr. aut. |
| **Modele, wagi, zbiory danych** | Często nie są utworami | Ochrona przez tajemnicę przedsiębiorstwa i prawo do bazy danych; wydanie nośników | art. 11 u.z.n.k.; ustawa o ochronie baz danych (memorandum 3.1.3) |

### 1.2. Skutki — przeniesienie od osoby prywatnej do Spółki

| Skutek | Kogo dotyczy | Podstawa | Waga |
|---|---|---|---|
| **Spółka korzysta z cudzego utworu.** Twórca może żądać zaniechania, usunięcia skutków, naprawienia szkody, wydania korzyści. Licencja dorozumiana jest niepewna i trudna do wykazania. | Spółka, dyrektorzy | art. 79 pr. aut. | Wysoka |
| **Aport niewniesiony.** Bez skutecznego przeniesienia akcje za wkład niepieniężny są niepokryte. Wkład trzeba wnieść w ciągu 3 lat od wpisu, a Spółka ma roszczenie o jego wniesienie. | Założyciel, Spółka | art. 300⁹ § 1 KSH (memorandum 3.1.1) | Wysoka |
| **Kapitał w KRS niezgodny ze stanem faktycznym.** Dyrektorzy składają oświadczenie o wniesieniu wkładów i o wysokości kapitału. Za fałszywe dane odpowiadają wobec wierzycieli przez 3 lata, a ich przedstawienie jest przestępstwem. | Dyrektorzy | art. 300¹² § 3, art. 300¹²³, art. 587 § 1 KSH (memorandum 3.1.1) | Wysoka |
| **Zawyżona wartość wkładu.** Jeśli przeniesiono mniej, niż wyceniono (np. bez części pól eksploatacji albo bez udziału współtwórcy), wnoszący wyrównuje brakującą wartość. Dyrektorzy odpowiadają solidarnie, chyba że nie ponoszą winy. Za wady wkładu odpowiada wnoszący. | Założyciel, dyrektorzy | art. 300¹⁰ § 1–2, art. 14 § 2 KSH (memorandum 3.1.1) | Średnia |
| **Odchodzący założyciel zabiera kod.** Może go licencjonować komuś innemu. Zakaz konkurencji z § 14 ust. 5 wiąże tylko akcjonariuszy i dyrektorów, więc po wyjściu ze spółki przestaje działać. | Spółka | § 14 ust. 5 | Wysoka |
| **Roszczenie o wynagrodzenie.** Jeśli z umowy nie wynika, że przeniesienie albo licencja są nieodpłatne, twórca może później żądać wynagrodzenia. | Spółka | art. 43 ust. 1 pr. aut. — **do weryfikacji** | Średnia |
| **Wypowiedzenie licencji.** Licencja niewyłączna na czas nieoznaczony (albo dłuższy niż 5 lat — po 5 latach) może być wypowiedziana z rocznym wyprzedzeniem na koniec roku. Po wypowiedzeniu dalsze korzystanie jest naruszeniem. | Spółka | art. 68 pr. aut. — **do weryfikacji** | Średnia |
| **Due diligence inwestora.** Inwestor bada łańcuch tytułu, a nie oświadczenia. Luka oznacza warunek zamknięcia rundy, niższą wycenę albo gwarancje i escrow. | Spółka, wszyscy akcjonariusze | memorandum 3.1.3 | Wysoka |
| **Granty i finansowanie publiczne.** Zwykle wymagają, żeby beneficjent miał prawa do wyników. Brak tytułu oznacza ryzyko zwrotu dotacji. | Spółka | warunki programów — **do weryfikacji** | Średnia |
| **Podatki.** Aport IP to przychód założyciela w wysokości wartości wkładu (19%), a koszt dla samodzielnie napisanego kodu jest często zerowy. Nieodpłatne nabycie praw albo licencji przez Spółkę może być jej przychodem z nieodpłatnego świadczenia. | Założyciel, Spółka | art. 17 ust. 1 pkt 9, art. 22 ust. 1e pkt 3 PIT (memorandum 3.1.1, T9 pkt 3); art. 12 ust. 1 pkt 2 CIT — **do weryfikacji** | Średnia |

**Mocne strony Spółki, gdyby wspólnik groził „zabraniem” praw.**

- **Aport.** Obowiązek wniesienia wkładu wynika z aktu notarialnego (§ 4), więc Spółka może pozwać o złożenie oświadczenia woli. Prawomocny wyrok zastępuje oświadczenie wspólnika (art. 64 KC, art. 1047 KPC — memorandum). Warunek: obowiązek musi być dostatecznie określony, czyli przedmiot w Załączniku nr 1, a pola eksploatacji w umowie. Dlatego po zmianach pola są wpisane wprost do § 14 ust. 1 lit. b.
- **Kod pisany po założeniu.** Obecny 2.0-S zobowiązuje tylko ogólnie („zawiera umowę zapewniającą nabycie”). Taki obowiązek trudno wyegzekwować, bo brakuje w nim treści umowy. Po zmianach umowa ma ustawowe elementy, a do tego dochodzi kwartalne pisemne potwierdzenie z wykazem utworów, które samo przenosi prawa.

### 1.3. Skutki — między spółkami (Basilisk ↔ Appolonia)

| Skutek | Podstawa | Waga |
|---|---|---|
| **Naruszenie praw.** Korzystanie z kodu siostrzanej spółki bez licencji to naruszenie. Przeniesienie praw i licencja wyłączna wymagają formy pisemnej pod rygorem nieważności. | art. 53, art. 67 ust. 5 pr. aut. — **do weryfikacji** (art. 67 ust. 5) | Wysoka |
| **Blokada przy wspólnym kodzie.** Wspólnie tworzony kod bez przydziału staje się utworem współtwórców. Do korzystania z całości potrzebna jest zgoda wszystkich. Gdy relacje się popsują albo do jednej spółki wejdzie inwestor, powstaje blokada. | art. 9 ust. 3 pr. aut. (memorandum 3.1.3) | Wysoka |
| **Prawa u „złej” spółki.** Pracownik Basilisk piszący dla Appolonii: prawa nabywa Basilisk. Appolonia nie ma nic bez licencji albo przeniesienia. | art. 12, 74 ust. 3 pr. aut. | Średnia |
| **Podatki.** Nieodpłatna licencja albo usługa między spółkami może być przychodem z nieodpłatnego świadczenia u odbiorcy. Przy tych samych właścicielach spółki są podmiotami powiązanymi: organ może doszacować dochód do ceny rynkowej, a powyżej progów trzeba sporządzać dokumentację cen transferowych. | art. 12 ust. 1 pkt 2, art. 11a–11t CIT; memorandum T9 pkt 7 — **do weryfikacji** | Średnia |
| **Szkoda wspólników jednej ze spółek.** Gdy skład akcjonariatu się rozjedzie (np. inwestor tylko w Basilisk), darmowe przekazywanie wartości do Appolonii szkodzi wspólnikom Basilisk. Grozi odpowiedzialność dyrektorów wobec spółki, a przy znacznej szkodzie także karna (nadużycie zaufania). | obowiązek lojalności dyrektora; art. 296 KK — **do weryfikacji** | Wysoka po wejściu inwestora |
| **Utrata statusu Spółki Siostrzanej.** Licencje trwają tylko na zasadach Umowy o Współpracy. Bez takiej umowy po utracie statusu nie ma żadnej licencji. | § 15 ust. 8 | Wysoka bez Umowy o Współpracy |

### 1.4. Co zmieniłem w umowie (`psa_simple2`)

| Ryzyko | Zmiana | Gdzie |
|---|---|---|
| Aport bez skutecznego przeniesienia | Umowy przeniesienia aportu podpisywane najpóźniej w dniu aktu, w formie pisemnej, z polami eksploatacji i prawami zależnymi. Każdy współtwórca podpisuje osobno. | § 4 ust. 6 |
| Art. 43 (wynagrodzenie) i podatek od nieodpłatnego świadczenia przy aporcie | Wynagrodzeniem za przeniesienie i za licencję tymczasową są akcje obejmowane za wkład | § 4 ust. 6 |
| Spółka bez prawa do korzystania przed przeniesieniem | Licencja tymczasowa udzielona wprost w umowie spółki (akt notarialny spełnia formę) | § 4 ust. 6 |
| Wspólnik przetrzymuje prawa | Obowiązek wniesienia wkładu podlega wykonaniu w naturze, z wyrokiem zastępującym oświadczenie (art. 64 KC) | § 4 ust. 6 |
| Ogólnikowy obowiązek „zawarcia umowy” | Ustawowe elementy umowy przeniesienia wpisane wprost: forma, pola eksploatacji, prawa zależne, prawa osobiste, wynagrodzenie | § 14 ust. 1 lit. a–d |
| Art. 41 ust. 3 (nieważność umowy o „wszystkie przyszłe utwory”) | Przejście praw z chwilą przekazania utworu Spółce (repozytorium) plus kwartalne pisemne potwierdzenie wykazu utworów, które samo jest umową przeniesienia już istniejących, oznaczonych utworów | § 14 ust. 1 lit. a, e |
| Wynalazki dyrektorów bez umowy | Prawo do patentu dla Spółki, a gdy nie wynika to z ustawy — pisemne przeniesienie | § 14 ust. 1 zd. ostatnie |
| Wypowiadalna licencja na technologię sprzed założenia (art. 68) | Licencja na stałe 5 lat plus obowiązek przeniesienia na żądanie Rady za wartość ustaloną przez biegłego | § 14 ust. 2 |
| Przenoszenie praw między spółkami bez formy | Forma pisemna dla przeniesienia i licencji wyłącznej; pozostałe licencje co najmniej w formie dokumentowej z polami, okresem i wypowiedzeniem | § 15 ust. 5 |
| Pracownicy wspólni dla obu spółek | Umowa ma zapewnić prawa tej spółce, do której obszaru należy utwór | § 15 ust. 5 |

Zmiany przeniesiono do umowy Appolonii (`appolonia.tex` na `psa_simple2`, runda 1 — `audyt_rundy.md`).

### 1.5. Co trzeba zrobić poza umową spółki

1. **Umowy przeniesienia aportu** — dla każdego założyciela w dniu aktu. Do nich: wykaz repozytoriów z commitami i sumami kontrolnymi, wykaz współtwórców, wykaz komponentów open source z licencjami (copyleft to ryzyko), oświadczenie o braku praw byłych pracodawców i uczelni (memorandum T4).
2. **Podstawa pracy założycieli-dyrektorów.** Jedna z dwóch dróg:
   - umowa o pracę — wtedy programy przechodzą z mocy prawa (art. 74 ust. 3);
   - B2B albo umowa o współpracy z klauzulą z § 14 ust. 1.

   Przez pierwszy rok — kwartalne protokoły przekazania kodu.
3. **Umowa o Współpracy Basilisk ↔ Appolonia:**
   - przydział wyników;
   - licencje z długimi okresami wypowiedzenia (żeby nie wpaść w roczne wypowiedzenie z art. 68);
   - ceny rynkowe;
   - zasady dla pracowników wspólnych;
   - co się dzieje z licencjami po utracie statusu Spółki Siostrzanej.
4. **Interpretacja podatkowa** (memorandum T9):
   - wartość aportu IP i PIT założycieli;
   - licencje nieodpłatne;
   - ceny transferowe między spółkami siostrzanymi.
5. **Tajemnica przedsiębiorstwa** dla modeli, wag i danych: polityka dostępu, oznaczenia, umowy o poufności.

---

## 2. Czy akcje mogą być krzyżowym aportem?

### 2.1. Zasada

Akcje innej spółki są zbywalnym prawem majątkowym, więc mogą być wkładem niepieniężnym na pokrycie akcji P.S.A. (art. 300² § 1–2 i art. 14 § 1 KSH — memorandum 3.1.1). W P.S.A. nie ma obowiązkowego badania aportu przez biegłego rewidenta. Odpowiedzialność za znaczne zawyżenie wartości ponoszą wnoszący i dyrektorzy (art. 300¹⁰ — memorandum 3.1.1).

„Krzyżowy aport” może jednak oznaczać cztery różne konstrukcje:

| Wariant | Jak działa | Czy wykonalny | Główne problemy |
|---|---|---|---|
| **A. Czysty krzyż spółek** | Basilisk obejmuje nowe akcje Appolonii i płaci nowymi akcjami Basilisk, a Appolonia odwrotnie | **Nie** | Spółka nie może wnieść akcji, których nie ma — nowe akcje Basilisk po emisji należą do obejmującego, nie do Basilisk. Spółka nie może też obejmować akcji własnych. Obie emisje „pokrywałyby się” wzajemnie bez żadnego realnego majątku. (**do weryfikacji** co do podstawy przepisowej; wynika z istoty wkładu) |
| **B. Wzajemne udziały za inne aktywa** | Basilisk wnosi do Appolonii np. licencję albo IP za jej akcje, a Appolonia do Basilisk swoje aktywo | **Tak, ale ryzykownie** | Patrz 2.2 |
| **C. Założyciele wnoszą akcje jednej spółki do drugiej** | Np. założyciele wnoszą akcje Basilisk do Appolonii i obejmują w zamian nowe akcje Appolonii. Appolonia staje się spółką matką Basilisk. | **Tak**, ale tylko w jedną stronę (w obie strony to wariant A) | Patrz 2.3 |
| **D. Holding** | Założyciele wnoszą akcje obu spółek do nowej spółki holdingowej | **Tak** | Nowa spółka i koszty; poza tym najczystsza droga — patrz 2.4 |

### 2.2. Wariant B — wzajemne udziały spółek

1. **Stosunek dominacji.**
   - Spółką dominującą jest m.in. spółka, której członkowie organu zarządzającego stanowią ponad połowę członków zarządu innej spółki kapitałowej (art. 4 § 1 pkt 4 KSH — **do weryfikacji** co do litery przepisu). W P.S.A. Rada Dyrektorów wykonuje kompetencje zarządu (art. 300⁷³ § 1 KSH — memorandum 3.1.1).
   - Przy tych samych pięciu dyrektorach w obu spółkach dominacja może więc powstać **w obie strony**.
   - Gdy spółka dominująca ma akcje spółki zależnej, musi ją zawiadomić o dominacji w ciągu 2 tygodni. Inaczej traci głos z akcji powyżej 33% kapitału (art. 6 § 1 KSH — **do weryfikacji** w odniesieniu do kapitału akcyjnego P.S.A.).
2. **Akcje własne przez spółkę zależną.** Akcje spółki nabyte przez jej spółki zależne wlicza się do limitu 25% akcji własnych (art. 300⁴⁷ KSH; tak liczy `uchwaly.tex`). Do sprawdzenia jest, czy i w jakim zakresie P.S.A. ma zakaz obejmowania przez spółkę zależną akcji spółki dominującej, analogiczny do S.A. i sp. z o.o. (**do weryfikacji**).
3. **Dublowanie kapitału.** Część kapitału każdej spółki to akcje drugiej, których wartość zależy od tej pierwszej. Wycena jest więc „wzajemnie napompowana”, co zwiększa ryzyko z art. 300¹⁰ i nieufność inwestorów.
4. **Licencja jako aport.** Licencja niewyłączna jest wypowiadalna (art. 68 pr. aut.), więc jej wartość jako wkładu jest wątpliwa. Przeniesienie praw jest pewniejsze, ale wtedy IP przestaje być w spółce, której obszaru dotyczy.
5. **Podatek.** Aport spółki inny niż przedsiębiorstwo albo jego zorganizowana część to przychód wnoszącego w wartości wkładu (**do weryfikacji**).
6. **Skutek praktyczny.** Każda spółka ma inwestora strategicznego w postaci siostry. Inwestor zewnętrzny wchodzący do jednej spółki dostaje w pakiecie udział w drugiej, a to zwykle utrudnia rundę.

### 2.3. Wariant C — założyciele wnoszą akcje jednej spółki do drugiej

1. **Zgoda na zbycie.** Akcje Basilisk zmieniają właściciela, więc potrzebna jest zgoda Spółki (§ 8 ust. 1). Rada nie może odmówić bez podstawy z § 8 ust. 2.
2. **Lock-up.** Przez 12 miesięcy od wpisu zbycie wymaga zgody WZ (75% wszystkich głosów, § 8 ust. 4). Wyjątek dla podmiotu w całości kontrolowanego przez akcjonariusza nie obejmuje spółki kontrolowanej przez kilku założycieli.
3. **Vesting.** Obowiązek zbycia obciąża każdoczesnego posiadacza akcji (§ 9 ust. 7). Spółka przejmująca dostaje więc akcje niezwolnione i przy odejściu założyciela musiałaby je sprzedać po cenie emisyjnej. Vesting trzeba przenieść na poziom spółki przejmującej (nowa umowa wykonawcza).
4. **Podatek.** Wymiana udziałów może być neutralna, jeżeli spółka przejmująca uzyska większość głosów w spółce nabywanej i płaci własnymi akcjami, przy uzasadnieniu gospodarczym (art. 24 ust. 8a PIT — **do weryfikacji**). Inaczej przychód założycieli powstaje w dniu objęcia (art. 17 ust. 1 pkt 9 PIT).
5. **Skutek.** Jedna spółka staje się córką drugiej. Inwestor wybiera wtedy między spółką matką (cała grupa) a córką (jeden obszar). Przy różnych profilach inwestorów to wada.

### 2.4. Wariant D — holding

- **Jak.** Założyciele wnoszą akcje obu spółek do nowej spółki holdingowej (np. P.S.A.) i obejmują jej akcje.
- **Plusy:**
  - jedna tabela kapitalizacji;
  - możliwy jeden program motywacyjny;
  - IP wewnątrz grupy łatwiejsze do uporządkowania;
  - inwestor może wejść na poziom holdingu albo jednej ze spółek.
- **Podatek:** wymiana udziałów neutralna, jeżeli holding uzyska większość głosów w każdej spółce (**do weryfikacji**).
- **Minusy:**
  - koszty nowej spółki;
  - te same kolizje z zgodą na zbycie, lock-upem i vestingiem co w wariancie C;
  - § 15 trzeba wtedy przepisać na relację spółek z tej samej grupy.

### 2.5. Rekomendacja

1. **Teraz** — bez krzyżowych udziałów. Współpracę zapewnia § 15 + Umowa o Współpracy + porządek w IP (punkt 1.4–1.5).
2. **Przy pierwszej rundzie albo gdy profil inwestorów obu spółek okaże się wspólny** — holding przez wymianę akcji (wariant D).
3. **Jeżeli mimo to chcecie wzajemnych udziałów**:
   - tylko mniejszościowe;
   - za gotówkę albo przeniesione prawa, nigdy „akcje za akcje”;
   - różne składy Rad, żeby uniknąć dominacji przez wspólnych dyrektorów;
   - w obu umowach: wyjątek od lock-upu dla spółki siostrzanej, zasady vestingu dla akcji w jej rękach, uwzględnienie akcji siostry w limicie akcji własnych.

---

## 3. Pytania do prawnika i doradcy podatkowego

1. Czy przejście praw „z chwilą przekazania utworu Spółce” w § 14 ust. 1 lit. a, przy braku umowy o pracę albo B2B, nie narusza art. 41 ust. 3 pr. aut. Czy kwartalne potwierdzenie (lit. e) wystarcza jako zabezpieczenie.
2. Czy licencja tymczasowa i licencja na technologię sprzed założenia, udzielone wprost w umowie spółki, są skuteczne wobec Spółki w organizacji (art. 300¹¹ KSH).
3. Litera art. 4 § 1 pkt 4 KSH i art. 6 KSH w relacji Basilisk ↔ Appolonia przy tych samych dyrektorach. Czy dominacja wzajemna jest możliwa i jakie ma skutki bez wzajemnych udziałów.
4. Czy w P.S.A. obowiązuje zakaz obejmowania przez spółkę zależną akcji spółki dominującej.
5. PIT założycieli przy aporcie IP i przy ewentualnej wymianie akcji do holdingu; przychód Spółki z licencji nieodpłatnych (§ 14 ust. 2); ceny transferowe między spółkami siostrzanymi.
6. Czy dodać do § 3 ust. 7 umowny limit 5 lat dla upoważnienia do nabycia akcji własnych. W P.S.A. ustawa takiego limitu nie przewiduje (memorandum 1.3.5).
