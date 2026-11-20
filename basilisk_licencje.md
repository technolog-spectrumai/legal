# Basilisk Systems P.S.A. — wzory licencji na oprogramowanie

**Oprogramowanie robotów (Basilisk Onboard), oprogramowanie symulacyjne (Basilisk Sim) i oprogramowanie serwerowe (Basilisk Server)**

Wersja 1.1 — projekt · Dokument poufny · Stan prawny: listopad 2026 r.

Pola do uzupełnienia oznaczono **[nawiasami kwadratowymi]**. Odesłania „US” oznaczają umowę spółki Basilisk Systems P.S.A. (wersja 3.4-S), „UA” — umowę akcjonariuszy, „Umowa nr 1/2” — umowy przeniesienia praw autorskich, „Polityka” — politykę bezpieczeństwa informacji, „NDA” — wzór umowy o zachowaniu poufności. Skróty aktów prawnych — jak w bibliografii (`basilisk_bib.tex`).

---

## Spis treści

- [Wprowadzenie — jak korzystać ze wzorów](#wprowadzenie--jak-korzystać-ze-wzorów)
- [Część I — Ogólne warunki licencyjne (OWL)](#część-i--ogólne-warunki-licencyjne-owl)
- [Część II — Moduły produktowe](#część-ii--moduły-produktowe)
  - [Moduł M1 — Oprogramowanie robotów (Basilisk Onboard)](#moduł-m1--oprogramowanie-robotów-basilisk-onboard)
  - [Moduł M2 — Oprogramowanie symulacyjne (Basilisk Sim)](#moduł-m2--oprogramowanie-symulacyjne-basilisk-sim)
  - [Moduł M3 — Oprogramowanie serwerowe (Basilisk Server)](#moduł-m3--oprogramowanie-serwerowe-basilisk-server)
  - [Moduł M4 — Sektor publiczny i obronny](#moduł-m4--sektor-publiczny-i-obronny)
- [Część III — Wzór zamówienia licencyjnego](#część-iii--wzór-zamówienia-licencyjnego)
- [Załącznik A — Komponenty osób trzecich i licencje open source](#załącznik-a--komponenty-osób-trzecich-i-licencje-open-source)
- [Załącznik B — Oświadczenie użytkownika końcowego](#załącznik-b--oświadczenie-użytkownika-końcowego)
- [Załącznik C — Poziom usług (SLA) dla Basilisk Server](#załącznik-c--poziom-usług-sla-dla-basilisk-server)
- [Załącznik D — Lista kontrolna przed udzieleniem licencji (wewnętrzna)](#załącznik-d--lista-kontrolna-przed-udzieleniem-licencji-wewnętrzna)
- [Podstawy prawne](#podstawy-prawne)

---

## Wprowadzenie — jak korzystać ze wzorów

### Konstrukcja

Licencja składa się z trzech warstw, które razem tworzą jedną umowę:

| Warstwa | Treść | Kiedy się zmienia |
|---|---|---|
| **Zamówienie licencyjne** (Część III) | strony, produkty, liczba urządzeń / stanowisk / instancji, okres, terytorium, cena, warunki szczególne | przy każdej transakcji |
| **Moduł produktowy** (Część II: M1, M2, M3) | zasady właściwe dla danego produktu | rzadko; dołącza się tylko moduły kupowanych produktów |
| **Ogólne warunki licencyjne — OWL** (Część I) | zasady wspólne: zakres licencji, pola eksploatacji, dane, eksport, odpowiedzialność, rozwiązanie | rzadko; jedna wersja dla wszystkich klientów |

W razie sprzeczności pierwszeństwo ma Zamówienie, potem Moduł, potem OWL, a na końcu Dokumentacja.

### Który moduł

| Produkt | Przykłady | Moduł | Model licencji |
|---|---|---|---|
| Oprogramowanie robotów | autonomia, percepcja, nawigacja, łączność, koordynacja roju, firmware | **M1** | per Urządzenie (numer seryjny) |
| Oprogramowanie symulacyjne | symulator środowisk i sensorów, scenariusze, trening i walidacja modeli, cyfrowy bliźniak | **M2** | per stanowisko, licencja pływająca albo per węzeł obliczeniowy |
| Oprogramowanie serwerowe | zarządzanie flotą, planowanie misji, fuzja danych, aktualizacje urządzeń, API | **M3** | on-premise per instancja i liczba zarządzanych Urządzeń albo usługa hostowana (SaaS) |
| Klient z sektora publicznego lub obronnego | Siły Zbrojne RP, Agencja Uzbrojenia, NSPA, integratorzy obronni | **M4** (dodatkowo do M1–M3) | jak w M1–M3, ze zmianami z M4 |

### Zasady, których wzór pilnuje

1. **Licencja jest niewyłączna.** Licencja wyłączna wymaga formy pisemnej pod rygorem nieważności (art. 67 ust. 5 PrAut), a udzielenie wyłącznej licencji na kluczową własność intelektualną — uchwały Rady Dyrektorów albo Walnego Zgromadzenia (US § 10 ust. 7, § 13 ust. 1 lit. f).
2. **Okres i terytorium wpisuje się zawsze.** Bez nich licencja obowiązuje tylko 5 lat i tylko w państwie siedziby licencjobiorcy (art. 66 ust. 1 PrAut).
3. **Licencja „wieczysta” to licencja na czas nieoznaczony.** Licencja na ponad 5 lat po tym czasie uważana jest za udzieloną na czas nieoznaczony i — jeżeli umowa nie stanowi inaczej — może zostać wypowiedziana na rok naprzód (art. 68 PrAut). OWL wyłączają to wypowiedzenie i dopuszczają rozwiązanie tylko z ważnych powodów (§ 19).
4. **Pola eksploatacji wymienia się wprost** (art. 67 ust. 1 PrAut). Tego, czego nie wymieniono, licencjobiorcy nie wolno.
5. **Nie zakazujemy tego, czego nie wolno zakazać.** Kopia zapasowa, badanie działania programu i dekompilacja w celu współdziałania z innym programem są dozwolone z mocy ustawy, a postanowienia sprzeczne z nimi są nieważne (art. 75 ust. 2–3 i art. 76 PrAut).
6. **Nie wyłączamy odpowiedzialności, której nie wolno wyłączyć:** za szkodę umyślną (art. 473 § 2 KC) i za produkt niebezpieczny (art. 449⁹ KC). Rękojmię między przedsiębiorcami można wyłączyć, ale nie przy podstępnym zatajeniu wady (art. 558 KC).
7. **Kontrola eksportu.** Oprogramowanie autonomii, percepcji i dowodzenia może być produktem podwójnego zastosowania (rozp. 2021/821) albo technologią o przeznaczeniu wojskowym (wykaz WT, Dz.U. 2019 poz. 1888 — m.in. bezzałogowe statki powietrzne i ich systemy). Udostępnienie kodu za granicę — także przez pobranie, aktualizację OTA albo dostęp zdalny — jest wywozem. Obrót technologią o przeznaczeniu wojskowym wymaga koncesji (art. 7 UWT).
8. **TTBER (rozp. 2026/877).** Licencje między przedsiębiorcami nie mogą przewidywać wyłącznego zwrotnego przeniesienia ulepszeń licencjobiorcy; OWL przewidują jedynie niewyłączną licencję zwrotną (§ 9 ust. 4). Wzór nie zawiera klauzuli zakazu kwestionowania praw Spółki.
9. **Spółka musi mieć prawa, które licencjonuje.** Prawa do kodu wnieśli Założyciele (Umowa nr 1) i nabywa Spółka od twórców (Umowa nr 2). Komponenty open source są licencjonowane na własnych warunkach (Załącznik A).

### Kto podpisuje za Spółkę

- Dwóch dyrektorów łącznie albo dyrektor z prokurentem (US § 11 ust. 1).
- Licencja dla podmiotu powiązanego z akcjonariuszem albo dyrektorem — uchwała Rady Dyrektorów (US § 10 ust. 7); umowę z dyrektorem podpisuje pełnomocnik (US § 11 ust. 3).
- Licencja wyłączna, nieodwołalna lub bezterminowa na kluczową własność intelektualną poza zwykłym tokiem działalności — Walne Zgromadzenie, 75% wszystkich głosów (US § 13 ust. 1 lit. f). Zwykła licencja niewyłączna dla klienta mieści się w zwykłym toku działalności.
- Wartość powyżej progów z US § 10 ust. 7 (umowa poza budżetem ponad 250 000 zł) — uchwała Rady Dyrektorów.

---

## Część I — Ogólne warunki licencyjne (OWL)

### § 1. Definicje

1. **Spółka** albo **Licencjodawca** — Basilisk Systems prosta spółka akcyjna z siedzibą w Pruszkowie, KRS **[numer]**.
2. **Licencjobiorca** — przedsiębiorca albo podmiot publiczny wskazany w Zamówieniu. OWL nie mają zastosowania do konsumentów.
3. **Oprogramowanie** — program komputerowy Spółki wskazany w Zamówieniu, w postaci kodu wynikowego, wraz z Aktualizacjami, z wyłączeniem Komponentów Osób Trzecich. Licencja nie obejmuje kodu źródłowego, chyba że Zamówienie stanowi inaczej.
4. **Dokumentacja** — instrukcje, specyfikacje i informacje bezpieczeństwa dotyczące Oprogramowania, udostępniane przez Spółkę.
5. **Moduł** — część II niniejszego dokumentu właściwa dla danego produktu (M1, M2, M3).
6. **Zamówienie** — zamówienie licencyjne według wzoru z Części III, podpisane przez strony.
7. **Urządzenie** — robot, bezzałogowy statek powietrzny, pojazd, stacja naziemna albo komputer, oznaczony numerem seryjnym w Zamówieniu.
8. **Instancja** — jedna uruchomiona kopia Oprogramowania serwerowego w jednym środowisku.
9. **Użytkownik** — osoba fizyczna upoważniona przez Licencjobiorcę do korzystania z Oprogramowania.
10. **Aktualizacja** — poprawka, łatka bezpieczeństwa albo nowa wersja Oprogramowania udostępniona przez Spółkę.
11. **Komponenty Osób Trzecich** — oprogramowanie, biblioteki, modele i dane osób trzecich, w tym open source, wymienione w Załączniku A.
12. **Dane Licencjobiorcy** — dane wprowadzone do Oprogramowania albo wytworzone przez Urządzenia Licencjobiorcy, w szczególności dane z czujników, mapy, scenariusze, plany misji i wyniki.
13. **Dane Operacyjne** — dane techniczne o działaniu Oprogramowania: wersje, konfiguracja, logi błędów, wskaźniki wydajności, niezawierające treści Danych Licencjobiorcy.
14. **Okres Licencji** i **Terytorium** — okres i obszar wskazane w Zamówieniu.
15. **Informacje Kontrolowane** — informacje i technologie objęte przepisami o kontroli obrotu towarami, technologiami i usługami o znaczeniu strategicznym albo przepisami o wyrobach o przeznaczeniu wojskowym.

### § 2. Przedmiot i dokumenty umowy

1. Spółka udziela Licencjobiorcy licencji na korzystanie z Oprogramowania i Dokumentacji na zasadach Zamówienia, właściwego Modułu i OWL.
2. W razie sprzeczności pierwszeństwo ma Zamówienie, następnie Moduł, następnie OWL, a na końcu Dokumentacja. Ogólne warunki zakupów Licencjobiorcy nie mają zastosowania, chyba że Zamówienie stanowi inaczej.

### § 3. Zakres licencji

1. Licencja jest **niewyłączna**, nieprzenoszalna i bez prawa udzielania sublicencji, chyba że Zamówienie stanowi inaczej.
2. Licencja obejmuje korzystanie z Oprogramowania wyłącznie na Terytorium, w Okresie Licencji i w zakresie ilościowym wskazanym w Zamówieniu (liczba Urządzeń, stanowisk, równoczesnych sesji, węzłów albo Instancji).
3. Licencjobiorca może korzystać z Oprogramowania na potrzeby własnej działalności, w tym przez swoich pracowników, współpracowników i podwykonawców działających w jego imieniu, za których odpowiada jak za własne działania.
4. Licencja wyłączna może zostać udzielona wyłącznie w formie pisemnej pod rygorem nieważności.

### § 4. Pola eksploatacji

1. Licencja obejmuje następujące pola eksploatacji:
   1. trwałe i czasowe zwielokrotnianie Oprogramowania w zakresie niezbędnym do jego instalacji, uruchamiania, wyświetlania, stosowania, przekazywania i przechowywania;
   2. wprowadzanie Oprogramowania do pamięci Urządzeń, komputerów i sieci Licencjobiorcy w liczbie wskazanej w Zamówieniu;
   3. konfigurację Oprogramowania i jego integrację z innymi systemami Licencjobiorcy za pomocą interfejsów opisanych w Dokumentacji;
   4. zwielokrotnianie Dokumentacji na potrzeby własne Licencjobiorcy.
2. Bez zgody Spółki w formie dokumentowej Licencjobiorca nie może w szczególności: tłumaczyć, przystosowywać ani w inny sposób zmieniać Oprogramowania; rozpowszechniać go, wynajmować, użyczać ani udostępniać osobom trzecim, także w modelu usługi; usuwać ani obchodzić zabezpieczeń technicznych i oznaczeń praw — w każdym przypadku z zastrzeżeniem § 5.

### § 5. Uprawnienia ustawowe

1. Żadne postanowienie umowy nie ogranicza uprawnień przyznanych przez art. 75 ust. 2 i 3 PrAut, w szczególności do sporządzenia kopii zapasowej, obserwowania, badania i testowania funkcjonowania Oprogramowania oraz zwielokrotniania kodu i tłumaczenia jego formy w zakresie niezbędnym do osiągnięcia współdziałania z niezależnie stworzonym programem.
2. Strony postanawiają, w rozumieniu art. 75 ust. 1 PrAut, że błędy Oprogramowania poprawia Spółka w ramach wsparcia. Licencjobiorca może poprawić błąd samodzielnie, jeżeli Spółka go nie usunęła w terminie określonym we właściwym Module albo w Załączniku C.
3. Kopia zapasowa nie może być używana równocześnie z Oprogramowaniem, z wyjątkiem środowiska zapasowego (DR) przewidzianego w Module M3.

### § 6. Dostawa, aktywacja i zabezpieczenia

1. Spółka dostarcza Oprogramowanie przez pobranie, nośnik albo preinstalację na Urządzeniu, w terminie wskazanym w Zamówieniu.
2. Oprogramowanie może wymagać klucza licencyjnego. Dla środowisk bez dostępu do sieci (air-gapped) Spółka zapewnia aktywację bez połączenia z internetem.
3. Mechanizmy licencyjne zbierają wyłącznie dane niezbędne do weryfikacji zakresu licencji. Spółka nie stosuje mechanizmów zdalnego wyłączania Oprogramowania w czasie jego działania na Urządzeniu.

### § 7. Aktualizacje i wsparcie

1. W okresie wsparcia wskazanym w Zamówieniu Spółka udostępnia Aktualizacje i świadczy wsparcie na zasadach właściwego Modułu.
2. Spółka udostępnia poprawki bezpieczeństwa dla każdej wersji objętej wsparciem przez co najmniej **[24]** miesiące od jej wydania.
3. Licencjobiorca instaluje Aktualizacje oznaczone jako krytyczne dla bezpieczeństwa w terminie wskazanym w Module. Spółka nie odpowiada za szkody, którym zapobiegłaby taka Aktualizacja, jeżeli Licencjobiorca jej nie zainstalował.

### § 8. Wynagrodzenie

1. Wynagrodzenie, model licencji (wieczysta z opłatą za wsparcie, subskrypcja albo rozliczenie za użycie) i terminy płatności określa Zamówienie. Kwoty są kwotami netto, powiększanymi o należny podatek VAT.
2. Faktury są płatne w terminie **[30]** dni od doręczenia.
3. Opłaty subskrypcyjne i za wsparcie podlegają waloryzacji przy każdym odnowieniu o średnioroczny wskaźnik cen towarów i usług konsumpcyjnych ogółem za poprzedni rok kalendarzowy, ogłaszany przez Prezesa GUS w „Monitorze Polskim”, jeżeli wskaźnik ten przekracza 100.
4. Jeżeli przepisy państwa Licencjobiorcy nakładają podatek u źródła, Licencjobiorca dostarcza Spółce certyfikat rezydencji i dokumenty pozwalające zastosować umowę o unikaniu podwójnego opodatkowania; kwoty potrącone ponad stawkę z tej umowy Licencjobiorca dopłaca.

### § 9. Własność intelektualna

1. Spółka zachowuje wszystkie prawa do Oprogramowania i Dokumentacji. Licencjobiorca nabywa wyłącznie prawa wyraźnie przyznane w umowie.
2. Licencjobiorcy przysługują prawa do Danych Licencjobiorcy oraz do wyników uzyskanych z użyciem Oprogramowania, w tym modeli wytrenowanych przez Licencjobiorcę na jego danych.
3. Uwagi i sugestie dotyczące Oprogramowania Spółka może wykorzystywać bez ograniczeń i bez wynagrodzenia.
4. Do ulepszeń Oprogramowania stworzonych przez Licencjobiorcę w granicach licencji, dających się od Oprogramowania odłączyć, prawa przysługują Licencjobiorcy; Licencjobiorca udziela Spółce na nie niewyłącznej, nieodpłatnej licencji. Umowa nie przewiduje wyłącznego zwrotnego przeniesienia ani licencji na ulepszenia Licencjobiorcy.

### § 10. Dane

1. Spółka przetwarza Dane Licencjobiorcy wyłącznie w zakresie niezbędnym do świadczenia wsparcia i usług hostowanych.
2. Spółka może wykorzystywać Dane Operacyjne do utrzymania, zabezpieczenia i rozwoju Oprogramowania, w tym w postaci zagregowanej do trenowania modeli, chyba że Zamówienie stanowi inaczej. Dla Licencjobiorców z sektora obronnego domyślnie przyjmuje się, że Dane Operacyjne nie opuszczają infrastruktury Licencjobiorcy.
3. Jeżeli Spółka przetwarza dane osobowe w imieniu Licencjobiorcy, strony zawierają umowę powierzenia przetwarzania zgodną z art. 28 RODO.
4. Spółka nie przetwarza informacji niejawnych w rozumieniu ustawy o ochronie informacji niejawnych, chyba że posiada wymagane świadectwo bezpieczeństwa przemysłowego i strony zawarły odrębną umowę.

### § 11. Komponenty Osób Trzecich

1. Komponenty Osób Trzecich wymienia Załącznik A wraz z ich licencjami. Do tych komponentów stosuje się w pierwszej kolejności ich licencje.
2. Spółka zapewnia, że korzystanie z Oprogramowania zgodnie z umową nie narusza licencji Komponentów Osób Trzecich, a jeżeli licencja komponentu tego wymaga — udostępnia jego kod źródłowy na żądanie.

### § 12. Kontrola eksportu, sankcje i użytkownik końcowy

1. Oprogramowanie, Dokumentacja i Aktualizacje mogą stanowić Informacje Kontrolowane. Licencjobiorca składa oświadczenie użytkownika końcowego według wzoru z Załącznika B i nie wywozi, nie przekazuje ani nie udostępnia ich poza Terytorium ani osobom z państw spoza Unii Europejskiej bez wymaganych zezwoleń i bez zgody Spółki w formie dokumentowej.
2. Licencjobiorca oświadcza, że ani on, ani podmioty go kontrolujące nie są objęte sankcjami ani środkami ograniczającymi, i niezwłocznie zawiadamia Spółkę o zmianie tego stanu.
3. Spółka może wstrzymać dostawę, Aktualizacje albo usługi, jeżeli brak wymaganego zezwolenia albo zachodzi ryzyko naruszenia przepisów o sankcjach; wstrzymanie z tych przyczyn nie stanowi niewykonania umowy przez Spółkę.
4. Jeżeli udzielenie licencji stanowi obrót technologią o przeznaczeniu wojskowym, Spółka udziela jej na podstawie koncesji nr **[numer]**.

### § 13. Zgodne z prawem i bezpieczne użytkowanie

1. Licencjobiorca odpowiada za korzystanie z Oprogramowania i Urządzeń zgodnie z prawem, w tym z przepisami lotniczymi, o bezzałogowych statkach powietrznych, o ruchu drogowym, o ochronie danych i z międzynarodowym prawem humanitarnym.
2. Licencjobiorca zapewnia nadzór człowieka nad funkcjami autonomicznymi w zakresie wymaganym przez Dokumentację i prawo, nie wyłącza funkcji bezpieczeństwa i przed użyciem operacyjnym przeprowadza testy w swoich warunkach.
3. Strony niezwłocznie, nie później niż w ciągu 24 godzin, zawiadamiają się o wykrytych podatnościach i incydentach bezpieczeństwa dotyczących Oprogramowania.

### § 14. Gwarancja

1. Spółka gwarantuje, że przez **[90]** dni od dostawy, a w okresie subskrypcji albo wsparcia — przez cały ten okres, Oprogramowanie działa w istotnym zakresie zgodnie z Dokumentacją.
2. W razie niezgodności Spółka, według swojego wyboru, usuwa ją, dostarcza obejście albo — jeżeli nie jest to możliwe w rozsądnym terminie — zwraca wynagrodzenie za niezgodną część za okres niezgodności.
3. Spółka nie gwarantuje, że Oprogramowanie będzie wolne od wszystkich błędów ani że wyniki symulacji odpowiadają zachowaniu Urządzeń w świecie rzeczywistym.
4. Odpowiedzialność z tytułu rękojmi jest wyłączona, z wyjątkiem wady podstępnie zatajonej przez Spółkę (art. 558 KC).

### § 15. Odpowiedzialność

1. Łączna odpowiedzialność każdej ze stron z tytułu umowy jest ograniczona do wynagrodzenia zapłaconego albo należnego za 12 miesięcy poprzedzających zdarzenie, a żadna ze stron nie odpowiada za utracone korzyści.
2. Ograniczenia z ust. 1 nie dotyczą:
   1. szkody wyrządzonej umyślnie (art. 473 § 2 KC);
   2. odpowiedzialności za szkodę wyrządzoną przez produkt niebezpieczny (art. 449¹ i 449⁹ KC);
   3. szkody na osobie;
   4. zobowiązań z § 16;
   5. korzystania z Oprogramowania przez Licencjobiorcę z przekroczeniem licencji albo z naruszeniem § 12.

### § 16. Roszczenia osób trzecich

1. Spółka zwalnia Licencjobiorcę z odpowiedzialności wobec osób trzecich, które zarzucają, że Oprogramowanie narusza ich prawa własności intelektualnej, pod warunkiem że Licencjobiorca niezwłocznie zawiadomi Spółkę, powierzy jej prowadzenie obrony i współdziała przy niej.
2. Spółka może według swojego wyboru uzyskać prawo dalszego korzystania, zmienić Oprogramowanie tak, by nie naruszało praw, albo rozwiązać licencję i zwrócić wynagrodzenie za niewykorzystany okres.
3. Ust. 1 nie dotyczy naruszeń wynikających ze zmian dokonanych przez Licencjobiorcę, z połączenia z produktami niedostarczonymi przez Spółkę ani z korzystania niezgodnego z Dokumentacją.

### § 17. Poufność i depozyt kodu

1. Do informacji poufnych stron stosuje się postanowienia wzoru NDA Spółki, z wyjątkiem kar umownych, chyba że Zamówienie stanowi inaczej.
2. Jeżeli Zamówienie tak przewiduje, Spółka składa kod źródłowy Oprogramowania u niezależnego depozytariusza. Kod zostaje wydany Licencjobiorcy wyłącznie do utrzymania Oprogramowania na własne potrzeby, jeżeli Spółka zostanie postawiona w stan likwidacji albo upadłości albo trwale zaprzestanie wsparcia objętej umową wersji.

### § 18. Audyt licencyjny

1. Spółka może raz w roku, po zawiadomieniu z wyprzedzeniem co najmniej 14 dni, zweryfikować zgodność korzystania z licencją.
2. W obiektach chronionych i środowiskach niejawnych weryfikacja następuje przez sprawozdanie Licencjobiorcy podpisane przez osobę upoważnioną, bez dostępu Spółki do infrastruktury.
3. Jeżeli weryfikacja wykaże niedopłatę wyższą niż 5%, Licencjobiorca dopłaca różnicę i zwraca koszty weryfikacji.

### § 19. Okres i rozwiązanie

1. Licencja obowiązuje w Okresie Licencji. Licencja oznaczona w Zamówieniu jako „wieczysta” jest licencją na czas nieoznaczony; strony wyłączają prawo jej wypowiedzenia przez Spółkę na podstawie art. 68 ust. 1 PrAut, a Spółka może ją rozwiązać wyłącznie z przyczyn określonych w ust. 3.
2. Subskrypcja odnawia się na kolejne okresy roczne, chyba że strona wypowie ją najpóźniej **[60]** dni przed końcem okresu.
3. Strona może rozwiązać umowę ze skutkiem natychmiastowym, jeżeli druga strona istotnie narusza umowę i nie usunie naruszenia w terminie 30 dni od wezwania. Spółka może rozwiązać umowę bez wezwania w razie naruszenia § 12.
4. Po rozwiązaniu albo wygaśnięciu Licencjobiorca zaprzestaje korzystania z Oprogramowania, usuwa jego kopie i potwierdza to w formie dokumentowej. Spółka udostępnia Dane Licencjobiorcy do pobrania przez 30 dni, a następnie je usuwa.
5. Postanowienia §§ 9, 10, 12, 15–17 i 21 obowiązują po rozwiązaniu umowy.

### § 20. Siła wyższa

Strona nie odpowiada za niewykonanie zobowiązania spowodowane zdarzeniem, którego nie mogła przewidzieć ani mu zapobiec, w szczególności działaniami wojennymi, aktami władzy publicznej, w tym odmową zezwolenia eksportowego, i rozległymi awariami infrastruktury. Strona niezwłocznie zawiadamia drugą stronę o takim zdarzeniu.

### § 21. Prawo właściwe i spory

1. Umowa podlega prawu polskiemu, z wyłączeniem Konwencji Narodów Zjednoczonych o umowach międzynarodowej sprzedaży towarów.
2. Spory rozstrzyga sąd powszechny właściwy dla siedziby Spółki, a jeżeli Zamówienie tak przewiduje — Sąd Arbitrażowy przy Krajowej Izbie Gospodarczej w Warszawie według jego regulaminu. Postanowienie to nie ogranicza prawa do żądania zabezpieczenia.

### § 22. Postanowienia końcowe

1. Umowę zawiera się w formie dokumentowej, w tym przez podpisanie Zamówienia kwalifikowanym podpisem elektronicznym; licencja wyłączna wymaga formy pisemnej. Zmiany wymagają formy dokumentowej.
2. Licencjobiorca nie może przenieść praw z umowy bez zgody Spółki. Spółka może przenieść umowę na następcę prawnego albo nabywcę przedsiębiorstwa lub jego części obejmującej Oprogramowanie.
3. Jeżeli postanowienie umowy jest nieważne, pozostałe postanowienia zachowują moc, a strony zastąpią je postanowieniem najbliższym jego celowi.
4. Umowę można sporządzić w języku polskim i angielskim; w razie rozbieżności rozstrzyga wersja polska.

---

## Część II — Moduły produktowe

### Moduł M1 — Oprogramowanie robotów (Basilisk Onboard)

**§ M1.1. Przedmiot.** Moduł dotyczy oprogramowania wbudowanego i aplikacyjnego Urządzeń: autonomii, percepcji, nawigacji, łączności, koordynacji zespołowej i roju oraz firmware, dostarczanego preinstalowanego na Urządzeniu Spółki albo do instalacji na Urządzeniu Licencjobiorcy zgodnym z listą kompatybilności w Dokumentacji.

**§ M1.2. Licencja per Urządzenie.**
1. Licencja jest przypisana do Urządzenia o numerze seryjnym wskazanym w Zamówieniu.
2. Przy sprzedaży Urządzenia Spółki Oprogramowanie nie jest sprzedawane, lecz licencjonowane na zasadach niniejszej umowy.
3. Przeniesienie licencji wraz z Urządzeniem na osobę trzecią wymaga zgody Spółki w formie dokumentowej, przyjęcia przez nabywcę warunków umowy i spełnienia wymogów z § 12 OWL. Przeniesienie na inne Urządzenie jest dopuszczalne tylko przy wymianie serwisowej.

**§ M1.3. Aktualizacje.**
1. Aktualizacje są dostarczane zdalnie (OTA) albo, w środowiskach bez dostępu do sieci, na nośniku albo przez Basilisk Server.
2. Licencjobiorca może odroczyć Aktualizacje niekrytyczne. Aktualizacje krytyczne dla bezpieczeństwa instaluje w ciągu **[30]** dni, a przed instalacją może je przetestować w swoich warunkach.

**§ M1.4. Bezpieczeństwo.**
1. Licencjobiorca korzysta z trybów autonomii, ograniczeń geograficznych (geofencing) i funkcji bezpieczeństwa zgodnie z Dokumentacją i nie modyfikuje parametrów bezpieczeństwa poza zakresem przez nią dopuszczonym.
2. W przypadku bezzałogowych statków powietrznych Licencjobiorca jako operator odpowiada za spełnienie wymogów rozporządzeń (UE) 2019/945 i 2019/947 oraz prawa lotniczego, w tym kategorii operacji i zezwoleń.

**§ M1.5. Dane.** Dane z czujników Urządzenia są Danymi Licencjobiorcy. Logi diagnostyczne są Danymi Operacyjnymi.

**§ M1.6. Usuwanie błędów.** Termin, o którym mowa w § 5 ust. 2 OWL: błąd uniemożliwiający bezpieczne działanie Urządzenia — **[5]** dni roboczych na obejście; pozostałe błędy — w najbliższej Aktualizacji, nie później niż w ciągu **[90]** dni.

**§ M1.7. Odpowiedzialność za produkt.** Jeżeli Spółka dostarcza Urządzenie z Oprogramowaniem, jej odpowiedzialność jako producenta za produkt niebezpieczny nie podlega wyłączeniu ani ograniczeniu.

### Moduł M2 — Oprogramowanie symulacyjne (Basilisk Sim)

**§ M2.1. Przedmiot.** Moduł dotyczy symulatora środowisk, modeli fizycznych i modeli sensorów, biblioteki scenariuszy i zasobów 3D, narzędzi do trenowania i walidacji modeli oraz cyfrowych bliźniaków Urządzeń.

**§ M2.2. Modele licencji.** Zamówienie wskazuje jeden z modeli: (a) stanowisko nazwane — jeden Użytkownik; (b) licencja pływająca — określona liczba równoczesnych sesji; (c) węzeł obliczeniowy — określona liczba serwerów albo procesorów graficznych, w infrastrukturze Licencjobiorcy albo w chmurze w regionie wskazanym w Zamówieniu.

**§ M2.3. Treści Spółki.** Scenariusze, zasoby 3D, modele i dane dostarczone przez Spółkę wolno wykorzystywać wyłącznie w Oprogramowaniu i na potrzeby własne Licencjobiorcy; nie wolno ich wyodrębniać ani udostępniać osobom trzecim.

**§ M2.4. Wyniki Licencjobiorcy.**
1. Scenariusze, dane syntetyczne i modele wytworzone przez Licencjobiorcę z użyciem Oprogramowania należą do Licencjobiorcy.
2. Licencjobiorca nie wykorzystuje Oprogramowania ani wyników do stworzenia symulatora konkurencyjnego wobec Oprogramowania ani do odtworzenia jego funkcji, z zastrzeżeniem § 5 OWL.

**§ M2.5. Charakter wyników.** Wyniki symulacji mają charakter pomocniczy i nie zastępują testów w świecie rzeczywistym, certyfikacji ani oceny zgodności. Decyzja o użyciu Urządzenia należy do Licencjobiorcy.

**§ M2.6. Licencja ewaluacyjna.** Zamówienie może przewidywać nieodpłatną licencję ewaluacyjną na **[30]** dni, bez wsparcia i bez prawa użytku produkcyjnego; § 14 OWL do niej nie stosuje się, a odpowiedzialność Spółki ogranicza się do szkody wyrządzonej umyślnie.

**§ M2.7. Publikacja porównań.** Publikacja wyników testów porównawczych Oprogramowania wymaga uprzedniego udostępnienia Spółce metodyki i umożliwienia jej przedstawienia uwag w terminie 14 dni.

### Moduł M3 — Oprogramowanie serwerowe (Basilisk Server)

**§ M3.1. Przedmiot.** Moduł dotyczy oprogramowania do zarządzania flotą Urządzeń, planowania i nadzoru misji, przetwarzania i fuzji danych, dystrybucji Aktualizacji oraz interfejsów programistycznych (API).

**§ M3.2. Warianty.** Zamówienie wskazuje wariant:
1. **on-premise** — instalacja w infrastrukturze Licencjobiorcy, także bez dostępu do sieci; licencja per Instancja i liczba zarządzanych Urządzeń;
2. **chmura prywatna** — instalacja w chmurze Licencjobiorcy w regionie wskazanym w Zamówieniu;
3. **usługa hostowana (SaaS)** — Spółka udostępnia funkcje Oprogramowania przez sieć z infrastruktury przez siebie zapewnionej; Licencjobiorca nie otrzymuje kopii Oprogramowania, a §§ 4–6 OWL stosuje się odpowiednio.

**§ M3.3. Środowiska.** Licencja on-premise obejmuje bez dodatkowej opłaty jedno środowisko testowe (bez użytku produkcyjnego) i jedno zapasowe środowisko DR, uruchamiane wyłącznie w razie awarii środowiska produkcyjnego.

**§ M3.4. API i integratorzy.** Licencjobiorca może integrować z Oprogramowaniem własne systemy. Udostępnienie API osobom trzecim jest dopuszczalne wyłącznie dla integratorów wskazanych w Zamówieniu, działających na rzecz Licencjobiorcy.

**§ M3.5. Użytkownicy.** Konta są imienne. Licencjobiorca odpowiada za nadawanie i odbieranie uprawnień oraz za uwierzytelnianie wieloskładnikowe Użytkowników.

**§ M3.6. Usługa hostowana — postanowienia dodatkowe.**
1. Dane Licencjobiorcy są przechowywane w Unii Europejskiej, w lokalizacji wskazanej w Zamówieniu, szyfrowane w spoczynku i w transmisji.
2. Spółka wykonuje kopie zapasowe co najmniej raz na dobę i przechowuje je przez **[30]** dni.
3. Poziom usług określa Załącznik C.
4. W razie zaległości w płatności przekraczającej 30 dni Spółka może zawiesić usługę po bezskutecznym wezwaniu z terminem nie krótszym niż 14 dni; nie zawiesza usługi w czasie trwania zgłoszonej misji, jeżeli Licencjobiorca o niej uprzedził.
5. Informacji niejawnych nie przetwarza się w usłudze hostowanej; wymagają one wariantu on-premise w akredytowanej infrastrukturze Licencjobiorcy.
6. Po zakończeniu umowy Spółka udostępnia Dane Licencjobiorcy do eksportu w formacie opisanym w Dokumentacji przez 30 dni, a następnie trwale je usuwa.

**§ M3.7. Usuwanie błędów.** Terminy, o których mowa w § 5 ust. 2 OWL — jak w Załączniku C.

### Moduł M4 — Sektor publiczny i obronny

Moduł stosuje się dodatkowo do M1–M3, gdy Licencjobiorcą jest Skarb Państwa, jednostka organizacyjna Sił Zbrojnych RP, Agencja Uzbrojenia albo inny zamawiający publiczny, organizacja międzynarodowa (np. NSPA) albo integrator działający na ich rzecz. W zakresie uregulowanym w M4 jego postanowienia mają pierwszeństwo przed OWL.

**§ M4.1. Umowa zamawiającego.** Jeżeli licencji udziela się w postępowaniu o udzielenie zamówienia, umową podstawową jest umowa zamawiającego, a OWL i Moduły stanowią jej załącznik techniczno-licencyjny. W razie sprzeczności rozstrzyga umowa zamawiającego, z wyjątkiem § 5, § 12 i § 15 ust. 2 OWL, które zawsze stosuje się w zakresie wymaganym przez prawo.

**§ M4.2. Terytorium.** Terytorium obejmuje, poza państwami wskazanymi w Zamówieniu, miejsca czasowego rozmieszczenia sił zbrojnych Licencjobiorcy, w tym w ramach misji, operacji i ćwiczeń NATO lub Unii Europejskiej, z zastrzeżeniem § 12 OWL i wymaganych zezwoleń eksportowych.

**§ M4.3. Przeniesienie licencji.** Licencjobiorca może przenieść licencję bez zgody Spółki na inną jednostkę organizacyjną Skarbu Państwa albo na następcę prawnego w wyniku reorganizacji, zawiadamiając Spółkę w formie dokumentowej w terminie 30 dni.

**§ M4.4. Integratorzy i serwis.** Licencjobiorca może udzielić sublicencji integratorom, wykonawcom i podmiotom serwisowym wskazanym w Zamówieniu albo zaakceptowanym przez Spółkę w formie dokumentowej, wyłącznie w zakresie niezbędnym do integracji, utrzymania i naprawy Urządzeń na rzecz Licencjobiorcy, pod warunkiem przyjęcia przez nich obowiązków z § 12 i § 17 OWL. Akceptacji nie można odmówić bez uzasadnionej przyczyny.

**§ M4.5. Cykl życia i bezpieczeństwo dostaw.** Spółka zapewnia wsparcie i Aktualizacje bezpieczeństwa dla wersji objętej Zamówieniem przez **[10–20]** lat od dostawy, na warunkach odpłatności określonych w Zamówieniu, oraz zawiadamia Licencjobiorcę z wyprzedzeniem co najmniej **[24]** miesięcy o zamiarze zakończenia wsparcia, umożliwiając zamówienie ostatniej partii licencji i usług (*last-time buy*).

**§ M4.6. Depozyt kodu.** Depozyt kodu źródłowego (§ 17 ust. 2 OWL) jest obowiązkowy. Depozytariusz ma siedzibę w Rzeczypospolitej Polskiej, kod jest aktualizowany przy każdym wydaniu, a jego kompletność weryfikuje się co najmniej raz w roku. Wydanie kodu następuje także w razie: zmiany kontroli nad Spółką na rzecz podmiotu spoza Unii Europejskiej lub NATO, utraty koncesji, objęcia Spółki sankcjami albo istotnego naruszenia obowiązków wsparcia niewyeliminowanego w terminie 60 dni od wezwania. Wydany kod Licencjobiorca może wykorzystywać wyłącznie do utrzymania i rozwoju Oprogramowania na własne potrzeby, z zachowaniem § 12 OWL.

**§ M4.7. Siła wyższa.** Działania wojenne, mobilizacja i stan wyjątkowy w państwie Licencjobiorcy nie stanowią siły wyższej zwalniającej Spółkę z obowiązków wsparcia, w zakresie w jakim ich wykonanie jest prawnie i faktycznie możliwe.

**§ M4.8. Odpowiedzialność.** Limit z § 15 ust. 1 OWL wynosi **[100]%** wartości brutto umowy zamawiającego, a dla licencji wieczystej opłaconej jednorazowo — nie mniej niż łączne wynagrodzenie zapłacone za licencję i wsparcie.

**§ M4.9. Dane i suwerenność.** Dane Licencjobiorcy i Dane Operacyjne nie opuszczają infrastruktury Licencjobiorcy, a w usłudze hostowanej przechowuje się je wyłącznie w Rzeczypospolitej Polskiej. Dostęp do nich ma wyłącznie personel Spółki będący obywatelami państw Unii Europejskiej lub NATO, wskazany imiennie, a w razie potrzeby posiadający poświadczenie bezpieczeństwa. Spółka prowadzi wykaz podwykonawców przetwarzania i zawiadamia o jego zmianach z wyprzedzeniem 30 dni.

**§ M4.10. Informacje niejawne i zgodność.** Jeżeli wykonanie umowy wymaga dostępu do informacji niejawnych, strony zawierają odrębną umowę bezpieczeństwa, a Spółka przedstawia wymagane świadectwo bezpieczeństwa przemysłowego. Przed złożeniem oferty Spółka przygotowuje matrycę zgodności wymagań zamawiającego z OWL i Modułami.

---

## Część III — Wzór zamówienia licencyjnego

**Zamówienie licencyjne nr [numer]** z dnia **[data]**

| Pozycja | Treść |
|---|---|
| Licencjodawca | Basilisk Systems P.S.A., Pruszków, KRS **[numer]**, NIP **[numer]** |
| Licencjobiorca | **[firma, siedziba, numer rejestrowy, NIP]**, reprezentowany przez **[imię, nazwisko, funkcja]** |
| Moduły | ☐ M1 Basilisk Onboard ☐ M2 Basilisk Sim ☐ M3 Basilisk Server ☐ M4 Sektor publiczny i obronny |
| Oprogramowanie i wersja | **[nazwa, wersja]** |
| Model licencji | ☐ wieczysta + wsparcie ☐ subskrypcja roczna ☐ za użycie: **[jednostka]** ☐ ewaluacyjna (M2) |
| Zakres ilościowy | Urządzenia: **[liczba, numery seryjne]**; stanowiska / sesje / węzły: **[liczba]**; Instancje i zarządzane Urządzenia: **[liczba]** |
| Wariant M3 | ☐ on-premise ☐ chmura prywatna (region **[...]**) ☐ usługa hostowana (lokalizacja **[...]**) |
| Terytorium | **[państwa]** |
| Okres Licencji | **[od — do / czas nieoznaczony]** |
| Okres wsparcia | **[od — do]** |
| Wynagrodzenie | **[kwota]** zł netto; płatność: **[harmonogram]** |
| Dane Operacyjne do rozwoju Oprogramowania (§ 10 ust. 2 OWL) | ☐ tak ☐ nie |
| Depozyt kodu źródłowego (§ 17 ust. 2 OWL) | ☐ tak — depozytariusz **[...]** ☐ nie |
| Rozstrzyganie sporów | ☐ sąd powszechny ☐ Sąd Arbitrażowy przy KIG |
| Kontrola eksportu | klasyfikacja: **[numer pozycji 2021/821 / WT / brak]**; zezwolenie: **[numer / niewymagane]**; koncesja Spółki: **[numer / niewymagana]**; oświadczenie użytkownika końcowego: ☐ złożone |
| Integratorzy z dostępem do API (M3) | **[nazwy]** |
| Warunki szczególne | **[...]** |

Zamówienie wraz z wybranymi Modułami i Ogólnymi warunkami licencyjnymi w wersji **[1.1]** stanowi umowę licencyjną. Licencjobiorca potwierdza, że zapoznał się z nimi przed podpisaniem.

**[za Spółkę — dwóch dyrektorów albo dyrektor i prokurent]** · **[za Licencjobiorcę]**

---

## Załącznik A — Komponenty osób trzecich i licencje open source

| Komponent | Wersja | Licencja | Sposób użycia (statyczne / dynamiczne łączenie, usługa) | Obowiązki (np. udostępnienie kodu, nota) | Moduł |
|---|---|---|---|---|---|
| **[nazwa]** | **[...]** | **[np. Apache-2.0, MIT, BSD-3-Clause, LGPL-3.0]** | **[...]** | **[...]** | **[M1/M2/M3]** |

Zasady: komponenty na licencjach wymagających udostępnienia kodu całości (np. GPL, AGPL) wolno łączyć z Oprogramowaniem wyłącznie po zgodzie dyrektora odpowiedzialnego za technologię. Wykaz utrzymuje się automatycznie (SBOM) i aktualizuje przy każdym wydaniu.

---

## Załącznik B — Oświadczenie użytkownika końcowego

My, **[firma Licencjobiorcy]**, z siedzibą w **[...]**, oświadczamy, że:

1. jesteśmy użytkownikiem końcowym Oprogramowania **[nazwa, wersja]** dostarczanego przez Basilisk Systems P.S.A. na podstawie Zamówienia nr **[...]**;
2. Oprogramowanie będzie wykorzystywane wyłącznie w **[państwo]**, do celu: **[opis]**;
3. nie będziemy go wywozić, przekazywać ani udostępniać, w tym zdalnie, innym osobom ani do innych państw bez wymaganych zezwoleń i bez zgody Spółki;
4. Oprogramowanie nie będzie wykorzystywane do celów związanych z bronią chemiczną, biologiczną lub jądrową ani przenoszącymi ją pociskami, ani przez podmioty objęte sankcjami lub środkami ograniczającymi;
5. niezwłocznie zawiadomimy Spółkę o każdej zmianie danych zawartych w niniejszym oświadczeniu.

**[miejscowość, data]** · **[podpis osoby upoważnionej]**

---

## Załącznik C — Poziom usług (SLA) dla Basilisk Server

| Parametr | Wartość |
|---|---|
| Dostępność usługi hostowanej | **[99,5]%** w miesiącu kalendarzowym, z wyłączeniem okien serwisowych zapowiedzianych co najmniej 5 dni roboczych wcześniej (łącznie nie więcej niż **[8]** godzin w miesiącu) |
| Kredyt serwisowy | dostępność 99,0–99,5%: **[5]%** miesięcznej opłaty; 95,0–99,0%: **[10]%**; poniżej 95,0%: **[25]%** |

| Priorytet zgłoszenia | Przykład | Czas reakcji | Obejście albo usunięcie |
|---|---|---|---|
| P1 — krytyczny | brak dostępu do usługi, brak łączności z flotą, błąd zagrażający bezpieczeństwu | **[1]** godzina, całą dobę | **[8]** godzin |
| P2 — wysoki | istotna funkcja nie działa, istnieje obejście | **[4]** godziny robocze | **[3]** dni robocze |
| P3 — normalny | błąd bez istotnego wpływu na działanie | **[1]** dzień roboczy | w najbliższej Aktualizacji |

Kredyty serwisowe są jedynym świadczeniem z tytułu niedotrzymania dostępności, z wyjątkiem szkody wyrządzonej umyślnie; Licencjobiorca może rozwiązać umowę, jeżeli dostępność spadnie poniżej 95% w dwóch miesiącach z rzędu.

---

## Załącznik D — Lista kontrolna przed udzieleniem licencji (wewnętrzna)

| # | Sprawdzenie | Podstawa | Odpowiedzialny |
|---|---|---|---|
| 1 | Spółka ma prawa do całego licencjonowanego kodu (Umowa nr 1, Umowa nr 2, potwierdzenia kwartalne) | Umowy IP | dyrektor ds. technologii |
| 1a | Technologia Założycieli niewniesiona aportem albo jeszcze nieprzeniesiona jest objęta licencją z prawem do sublicencji (US § 4 ust. 6, § 14 ust. 2) i wykazem ujawnionej technologii (UA § 6 ust. 4) | art. 67 ust. 3 PrAut | dyrektor ds. technologii |
| 2 | Aktualny wykaz komponentów open source (SBOM) i zgodność licencji | § 11 OWL, Załącznik A | dyrektor ds. technologii |
| 3 | Klasyfikacja eksportowa Oprogramowania: pozycja z rozp. 2021/821, wykaz WT albo brak kontroli | UOTS, rozp. 2021/821, WT | Odpowiedzialny z Polityki |
| 4 | Koncesja na obrót technologią o przeznaczeniu wojskowym, jeżeli wymagana | art. 7 UWT | Rada Dyrektorów |
| 5 | Sprawdzenie Licencjobiorcy i podmiotów go kontrolujących na listach sankcyjnych | rozp. 833/2014 i 269/2014, USank | Odpowiedzialny z Polityki |
| 6 | Oświadczenie użytkownika końcowego i zezwolenie eksportowe | § 12 OWL, Załącznik B | Odpowiedzialny z Polityki |
| 7 | Organ zatwierdzający: Rada (podmiot powiązany, kwota ponad próg) albo Walne Zgromadzenie (licencja wyłączna na kluczowe IP) | US § 10 ust. 7, § 13 ust. 1 lit. f | Przewodniczący Rady |
| 8 | Umowa powierzenia, jeżeli Spółka przetwarza dane osobowe (wsparcie, usługa hostowana) | art. 28 RODO | dyrektor wykonawczy |
| 9 | Kwalifikacja systemu w świetle AI Act (wyłączenie wyłącznie wojskowe albo obowiązki dla systemu podwójnego zastosowania) | rozp. 2024/1689 | dyrektor ds. technologii |
| 10 | Licencja na technologię dla konkurenta albo z ograniczeniami terytorialnymi — ocena w świetle TTBER (progi udziału w rynku 20% / 30%) | rozp. 2026/877 | doradca prawny |
| 11 | Obowiązki dla produktów z elementami cyfrowymi i nowe zasady odpowiedzialności za oprogramowanie jako produkt — do weryfikacji przed wprowadzeniem Urządzeń do obrotu | rozp. 2024/2847 (CRA), dyrektywa 2024/2853 | doradca prawny |
| 12 | NDA przed ujawnieniem informacji poufnych w negocjacjach | NDA, UA § 7 ust. 2 lit. b | dyrektor wykonawczy |

---

## Podstawy prawne

| Postanowienie | Podstawa | Uwagi |
|---|---|---|
| Licencja niewyłączna, forma licencji wyłącznej (§ 3) | art. 67 ust. 2 i 5 PrAut | licencja wyłączna — forma pisemna pod rygorem nieważności |
| Zakaz sublicencji bez zgody (§ 3 ust. 1) | art. 67 ust. 3 PrAut | reguła ustawowa, potwierdzona w umowie |
| Pola eksploatacji (§ 4) | art. 67 ust. 1, art. 74 ust. 4 PrAut | wymienione wprost |
| Okres i terytorium (§ 3 ust. 2, Zamówienie) | art. 66 ust. 1 PrAut | bez wskazania: 5 lat, państwo siedziby licencjobiorcy |
| Licencja „wieczysta” i wypowiedzenie (§ 19 ust. 1) | art. 68 PrAut | wypowiedzenie ustawowe wyłączone umową („jeżeli umowa nie stanowi inaczej”) |
| Uprawnienia nienaruszalne (§ 5) | art. 75 ust. 1–3, art. 76 PrAut | postanowienia sprzeczne z art. 75 ust. 2–3 są nieważne |
| Gwarancja i wyłączenie rękojmi (§ 14) | art. 558 KC | wyłączenie bezskuteczne przy podstępnym zatajeniu wady |
| Ograniczenie odpowiedzialności (§ 15) | art. 473 § 2, art. 449¹, 449⁹ KC | szkoda umyślna i produkt niebezpieczny — bez ograniczeń |
| Licencja zwrotna na ulepszenia (§ 9 ust. 4) | rozp. 2026/877 (TTBER), art. 5 | tylko niewyłączna |
| Kontrola eksportu, sankcje (§ 12) | UOTS, rozp. 2021/821, art. 7 UWT, wykaz WT, rozp. 833/2014 i 269/2014, USank | wywozem jest też przekazanie elektroniczne |
| Dane osobowe (§ 10 ust. 3) | art. 28 RODO | umowa powierzenia |
| Informacje niejawne (§ 10 ust. 4, § M3.6 ust. 5) | UONI | świadectwo bezpieczeństwa przemysłowego |
| Tajemnica przedsiębiorstwa (§ 17) | art. 11 UZNK | wymaga realnych działań ochronnych (Polityka) |
| Bezzałogowe statki powietrzne (§ M1.4) | rozp. 2019/945 i 2019/947, Prawo lotnicze | obowiązki operatora |
| Reprezentacja i zgody organów (Wprowadzenie) | US § 10 ust. 7, § 11 ust. 1 i 3, § 13 ust. 1 lit. f; art. 300⁷⁹ KSH | — |
| Waloryzacja (§ 8 ust. 3) | art. 358¹ § 2 KC (klauzula waloryzacyjna), komunikaty Prezesa GUS | jak w Cenniku i umowie akcjonariuszy |

Wzór wymaga przeglądu przez doradcę prawnego przed pierwszym użyciem, w szczególności w zakresie: klasyfikacji eksportowej konkretnych produktów, wymogów koncesyjnych, rozporządzenia (UE) 2024/2847 (CRA) i dyrektywy (UE) 2024/2853 o odpowiedzialności za produkty — tekstów tych aktów nie zweryfikowano w ramach przygotowania wzoru.
