# Umowa P.S.A. — wariant prosty (2.3-S): co wyszło, co jest ponad S24, co zmieniliśmy

**Porównywane dokumenty**

| | Dokument | Objętość |
|---|---|---|
| **Teraz** | `psa.tex` — wersja 2.3-S (wariant prosty po trzech rundach poprawek z audytu, `audyt_rundy.md`) | 18 § (w tym § 15 o współpracy ze Spółką Siostrzaną), 1 załącznik, 24 strony, ok. 8,0 tys. słów |
| **Poprzednio** | `psa.tex` — wersja 1.0-RC (commit `ac5005a`) | 38 §, 3 załączniki, 57 stron, ok. 20,3 tys. słów |
| **Standard** | Wzorzec umowy P.S.A. w S24 — Załącznik nr 1 do rozporządzenia MS z 30.06.2021 r. (Dz.U. 2021 poz. 1191) | 19 §, wybór wariantów, bez pisania własnych postanowień |

**Najpierw jedna uwaga: S24 nie jest dla nas dostępne.** Wzorzec mówi wprost, że „wszystkie akcje Spółki są pokrywane wkładami pieniężnymi” (§ 7 wzorca), a my wnosimy kod, sprzęt i patenty. Umowa musi więc mieć formę aktu notarialnego (art. 300⁶ § 1 KSH). S24 służy tu tylko jako punkt odniesienia: pokazuje, co ustawodawca uważa za minimalną, „gotową” umowę P.S.A.

**Zasada wariantu prostego:** w umowie zostaje tylko to, co musi w niej być albo co działa wobec Spółki i każdego kolejnego nabywcy akcji (limity emisji, ograniczenia zbywania, obowiązki związane z akcją, tryb uchwał). Resztę reguluje się regulaminami i uchwałami albo dopisze się zmianą umowy, kiedy będzie potrzebna.

Numery paragrafów: „§ n (1.0-RC)” oznacza starą wersję, a samo „§ n” — obecną wersję 2.3-S.

---

## 1. In minus — co usunęliśmy z poprzedniej umowy (1.0-RC)

### 1.1. Mechanizmy pod inwestorów VC i transakcje wyjścia

| Usunięte | Gdzie było | Dlaczego | Jak wrócić |
|---|---|---|---|
| **Prawo pierwszeństwa** (najpierw Spółka, potem akcjonariusze, 20 + 20 dni) | § 14 (1.0-RC) | Każde zbycie trwało dodatkowe 40–100 dni, a przy pięciu założycielach i zgodzie Spółki nie daje dodatkowej ochrony. § 8 ust. 6 mówi teraz wprost, że takiego prawa nie ma. | Umowa akcjonariuszy (wiąże tylko jej strony) albo zmiana umowy przy rundzie |
| **Prawo przyłączenia (tag-along)** przy przejęciu ponad 50% głosów | § 15 (1.0-RC) | Typowo negocjowane przez inwestora. Bez inwestora chroni tylko przed sprzedażą pakietu kontrolnego — przy wspólnikach, którzy się znają, to zbędne. | Jak wyżej |
| **Prawo przymusowego współzbycia (drag-along)** od 75% głosów, z warunkami ceny, odpowiedzialności i oświadczeń | § 16 (1.0-RC) | To najbardziej „inwestorska” konstrukcja w umowie. Wymagała Wartości Godziwej, Dopuszczalnego Nabywcy i osobnych gwarancji dla mniejszości. | Przy rundzie — zwykle i tak w umowie inwestycyjnej |
| **Kwalifikowana Runda Finansowania**: uchwała kierunkowa, obowiązek współdziałania, katalog „zwyczajowych warunków” (m.in. uprzywilejowanie likwidacyjne 1× non-participating, ochrona przed rozwodnieniem) | § 32 (1.0-RC) | Wyprzedzała negocjacje, które jeszcze się nie odbyły, i z góry dawała przyszłemu inwestorowi preferencje. Każda nowa seria wymaga teraz zmiany umowy (§ 5 ust. 4) — warunki rundy wpisuje się wtedy. | Zmiana umowy przy rundzie |
| **Przeniesienia Dozwolone** dla funduszy (fundusze równoległe i kontynuacyjne, wydanie aktywów w naturze) | § 12 ust. 9 (1.0-RC) | Postanowienie wyłącznie dla funduszy VC, których jeszcze nie ma | Zmiana umowy przy rundzie |
| **Dyrektor niewykonawczy wskazany przez Kwalifikowanego Inwestora Finansowego** spoza Kryterium EU/NATO | § 21 ust. 3 (1.0-RC) | Jak wyżej | Jak wyżej |
| **Odrębne głosowanie serii** przy zmianie umowy uszczuplającej prawa danej serii | § 38 ust. 2 (1.0-RC) | Wszystkie akcje są równe (§ 3 ust. 3), więc nie ma czego chronić. Zostaje ochrona ustawowa (art. 300⁹⁸ KSH). | Razem z akcjami uprzywilejowanymi |

### 1.2. Rozbudowana maszyneria bezpieczeństwa i wyceny

| Usunięte | Gdzie było | Dlaczego | Co zostało |
|---|---|---|---|
| **Dopuszczalny Nabywca, Niedopuszczalny Nabywca, Prawnie Niedopuszczalny Posiadacz, Kryterium Bezpieczeństwa EU/NATO**, procedura weryfikacji nabywcy, zawieszenie praw, zgoda WZ dla nabywcy spoza Kryterium | § 11 (1.0-RC), odesłania w kilkunastu paragrafach | Najbardziej rozbudowany i najczęściej przywoływany blok umowy. Przy obecnym składzie akcjonariuszy nie ma kogo weryfikować. Sankcje i kontrola inwestycji obowiązują z mocy prawa niezależnie od umowy. | Zamknięta lista przyczyn odmowy zgody na zbycie: sankcje, kontrola inwestycji, kontrola eksportu, bezpieczeństwo państwa (§ 8 ust. 2 lit. a–b) |
| **Wartość Godziwa i Dzień Wyceny**: definicja, uzgodnienie w 15 dni, Niezależny Ekspert, kryteria wyceny, płatność w ratach | § 19 (1.0-RC) | Potrzebna tylko dla mechanizmów, które usunęliśmy (wskazanie nabywcy, odkup akcji zwolnionych po 80% Wartości Godziwej, spłata spadkobierców) | Jedyną ceną w umowie jest cena emisyjna (§ 9 ust. 4) |
| **Impas Decyzyjny**: negocjacje, mediator, Niezależny Ekspert, budżet „proporcjonalnie przedłużony” | § 35 (1.0-RC) | Przy pięciu założycielach i progu 75% impas rozwiązuje się rozmową albo zmianą składu Rady, a nie procedurą. Klauzula mediacyjna została w postanowieniach końcowych. | § 18 ust. 4 — negocjacje i mediacja przed sądem |
| **Przedsięwzięcia Produkcyjne / spółki celowe**: próg 500 tys. zł, licencje dla SPV, weryfikacja partnerów | § 33 (1.0-RC) | Spółki celowe jeszcze nie istnieją | Utworzenie spółki zależnej wymaga uchwały Rady (§ 10 ust. 7); większe przedsięwzięcie mieści się w progu 500 tys. zł / 25% aktywów (§ 13 ust. 1 lit. e, h) |
| **Plan Finansowania i katalog źródeł finansowania**, zakaz finansowania dającego kontrolę podmiotowi spoza Kryterium | § 31 (1.0-RC) | Opisowy. Ogranicza to, co i tak wymaga uchwały. | Progi kwotowe w § 10 ust. 7 i § 13 ust. 1 lit. h |
| **Weto dyrektora niewykonawczego ds. bezpieczeństwa i zgodności** w sprawach Rady z lit. e–i i k | § 23 ust. 2 (1.0-RC) | Paraliżowało Radę przy każdej zmianie składu („do czasu wyznaczenia — zgoda wszystkich niewykonawczych”) | Wystarcza zwykła większość Rady i wyłączenie dyrektora w konflikcie (§ 10 ust. 5–6) |
| **Kryterium EU/NATO dla dyrektorów** | § 21 ust. 3 (1.0-RC) | Jak przy Dopuszczalnym Nabywcy | Dyrektorów wybiera WZ |

### 1.3. Ograniczenia osobiste i obrót akcjami

| Usunięte | Gdzie było | Dlaczego |
|---|---|---|
| **Stosunki majątkowe małżeńskie**: obowiązki informacyjne, rozliczenie pieniężne zamiast przeniesienia akcji, dokumenty na żądanie | § 18 (1.0-RC) | Wkraczało w sferę prywatną. Ochronę daje zgoda Spółki na zbycie (§ 8) i obowiązek zbycia, który obciąża każdego posiadacza akcji (§ 9 ust. 7). |
| **Ograniczenie wstąpienia spadkobierców** (art. 300⁴¹ § 1 KSH): weryfikacja spadkobiercy, 90 dni na zgodę WZ, spłata po Wartości Godziwej, wspólny przedstawiciel | § 17 (1.0-RC) | Spadkobiercy wstępują teraz do Spółki z mocy umowy, a akcje niezwolnione zostają objęte obowiązkiem zbycia (§ 9 ust. 8). |
| **Trzy kategorie odejścia** (Usprawiedliwione, Dobrowolne, Zawinione) z wymogiem prawomocnego skazania i rozstrzyganiem sporów o kwalifikację | § 10 ust. 4–6b (1.0-RC) | Spory o kategorię odejścia byłyby najdroższą częścią vestingu. Teraz jest jedna reguła i ewentualna łaska WZ — patrz 3.4. |
| **Odkup akcji już zwolnionych** po 80% Wartości Godziwej przy Odejściu Zawinionym oraz opcja Spółki na akcje zwolnione w ciągu 6 miesięcy po Odejściu Dobrowolnym | § 10 ust. 7–9 (1.0-RC) | Akcje zwolnione z obowiązku zbycia są „zarobione” — odbieranie ich to kara, nie vesting. Roszczenie o odszkodowanie zostaje (§ 9 ust. 5 zd. 2). |
| **Zmiana Kontroli** i przyspieszone zwalnianie akcji (single/double trigger) | § 10 (1.0-RC) | Wraca przy rundzie albo sprzedaży. Do tego czasu przyspieszenie może przyznać WZ (§ 9 ust. 5). |

### 1.4. Ład korporacyjny i postanowienia opisowe

| Usunięte | Gdzie było | Dlaczego |
|---|---|---|
| **„Głosy Uprawnione w Sprawie”** i wszystkie umowne wyłączenia prawa głosu (kandydat do serii F, akcjonariusz występujący o zgodę na zbycie, strona transakcji) | § 24 ust. 10–11 (1.0-RC) | Każda większość wymagała osobnego liczenia mianownika. Teraz są tylko dwa rodzaje progów: większość głosów oddanych i % wszystkich głosów; wyłączenia głosu wynikają wyłącznie z ustawy (§ 12 ust. 7). |
| **Odrębny paragraf o transakcjach z akcjonariuszami** (godziwe warunki, uchwała WZ 75% z wyłączeniem strony) | § 30 (1.0-RC) | Wystarcza uchwała Rady (§ 10 ust. 7) i wyłączenie dyrektora w konflikcie (§ 10 ust. 6) |
| **Definicje konfliktu interesów** (Osoba Bliska, progi 2%, cztery obowiązki dyrektora w konflikcie) | § 29 ust. 4–7 (1.0-RC) | Do regulaminu Rady (§ 10 ust. 8) |
| **Kluczowa Własność Intelektualna** jako definicja z pięcioma kategoriami aktywów, oświadczenia założycieli o wkładach | § 26 (1.0-RC) | Zasada „IP należy do Spółki” zostaje (§ 14 ust. 1–2); katalog aktywów jest w Załączniku nr 1 |
| **Szczegóły bezpieczeństwa informacji i kontroli eksportu** (szyfrowanie, rozdział środowisk, klasyfikacja przed każdym transferem, lista zakazanych transakcji) | § 27–28 (1.0-RC) | To treść polityk Rady, nie umowy spółki (§ 14 ust. 3–4) |
| **Cel strategiczny** jako osobny paragraf, ograniczenia obszaru działania | § 2–3 (1.0-RC) | Połączone w jedno zdanie opisu działalności (§ 2 ust. 1) |
| **Rezerwy celowe** (B+R, IP, cyberbezpieczeństwo, certyfikacja) i wymóg 75% głosów do odejścia od reinwestowania zysku | § 34 (1.0-RC) | Rekomendacja reinwestowania zostaje, ale jest niewiążąca (§ 16 ust. 1) |
| **Pierwszeństwo regulaminu WZ nad zawiadomieniem** i odrębne zasady problemów technicznych po stronie Spółki | § 24 ust. 6–7 (1.0-RC) | Zastąpione regulaminem przyjmowanym przy zawiązaniu (§ 12 ust. 5) |
| **Załącznik nr 2** (Założyciele objęci vestingiem) | — | Wchłonięty przez Załącznik nr 1 (kolumna „Data rozpoczęcia”) |
| **Załącznik nr 3** (ujawnione aktywności, licencje i ograniczenia) | — | Ewidencja prowadzona przez Radę; zgody na konkurencję wydaje Rada (§ 14 ust. 5) |

**Skala:** z 38 paragrafów zostało 17 (później doszedł § 15 o współpracy ze Spółką Siostrzaną — razem 18), z 3 załączników — 1, z 57 stron — 24. Lista spraw zastrzeżonych dla WZ skróciła się z 14 pozycji do 9 (plus nowe: lit. j — Umowa o Współpracy, lit. k — pożyczki i poręczenia dla dyrektorów), a przyczyny odmowy zgody na zbycie — z 6 do 4.

---

## 2. In plus — co mamy ponad standardową umowę S24

### 2.1. Mapa: wzorzec S24 a nasza umowa

| § S24 | Treść wzorca | U nas |
|---|---|---|
| 1 | Stawający | Wstęp + Załącznik nr 1 |
| 2 | Firma | § 1 ust. 1 — dodatkowo skrót i oznaczenia handlowe |
| 3 | Siedziba | § 1 ust. 2 |
| 4 | Przedmiot działalności (PKD) | § 2 — dodatkowo opis działalności i zastrzeżenie koncesji |
| 5 | Akcje: jedna seria A albo kilka serii do wyboru (AZ założycielskie, AG 2 głosy, AD 150% dywidendy, AN nieme) | § 3 — tylko akcje zwykłe, uprzywilejowanie wyłączone wprost (§ 3 ust. 3) |
| 6 | Objęcie akcji | § 4 ust. 1–2 |
| 7 | **Tylko wkłady pieniężne** | § 4 ust. 3–6 — wkłady niepieniężne (kod, sprzęt, patenty) z wyceną |
| 8 | Wkłady wniesione i terminy dopłat (do 3 lat) | § 4 ust. 5–6 — pieniężne przed wpisem, prawa IP w dniu aktu, pozostałe niepieniężne do 14 dni po wpisie |
| 9 | Zbywanie: A — zgoda Spółki + wskazanie nabywcy w 1 miesiąc po wartości godziwej; B — swoboda; C — swoboda + prawo pierwszeństwa | § 8 — zgoda Spółki, ale inaczej niż w wariancie A (patrz 2.2) |
| 10 | Głos zastawnika i użytkownika: A — nie; B — tak, jeśli przewiduje to czynność i wzmianka w rejestrze | § 3 ust. 9 — **jak wariant A** (od 2.1-S); od 2.3-S wyjątek za zgodą WZ (75%) dla zastawu zabezpieczającego finansowanie Spółki |
| 11 | Zaliczki na dywidendę; kapitały rezerwowe | § 16 ust. 3–4 — kapitały rezerwowe i upoważnienie Rady do zaliczek (od 2.1-S) |
| 12 | Organy: zarząd / zarząd + RN / rada dyrektorów | § 10 ust. 1 — rada dyrektorów (jak wariant C) |
| 13 | Skład, kadencja, powołanie i odwołanie uchwałą akcjonariuszy | § 10 ust. 2–3 — 3–7 dyrektorów, wspólna kadencja 3-letnia, przedłużenie mandatu (art. 300⁵⁶) |
| 14 | Reprezentacja: C1 — dwóch dyrektorów albo dyrektor z prokurentem; C2 — każdy samodzielnie | § 11 ust. 1 — **identycznie jak C1** |
| 15 | Pierwszy skład organów | § 18 ust. 6 — w uchwałach objętych aktem zawiązania |
| 16 | Uchwały na WZ albo poza nim, na piśmie albo e-mailem na adresy z rejestru; udział i głosowanie elektroniczne na WZ | § 12 ust. 1–5 — **ta sama podstawa** plus procedura obiegowa (patrz 2.2) |
| 17 | WZ ważne bez względu na liczbę akcji | Reguła ustawowa (bez postanowienia) |
| 18 | Bezwzględna większość głosów | § 12 ust. 7 — to samo jako zasada, plus progi 75% i 4/5 |
| 19 | Rok obrotowy | § 16 ust. 5 — rok kalendarzowy, pierwszy rok można połączyć z następnym (od 2.1-S) |

### 2.2. Postanowienia, których S24 nie ma

**Kapitał i emisje — główna różnica**

| Element | Po co | Gdzie |
|---|---|---|
| **Wkłady niepieniężne** z Załącznikiem nr 1 (przedmiot, numery akcji, wartość, podstawa wyceny, dokument przeniesienia) | Wnosimy kod, sprzęt i patenty. To właśnie wyklucza S24. | § 4, Załącznik nr 1 |
| **Zasada maksymalnej liczby akcji**: każda uchwała emisyjna, upoważnienie, program i umowa dająca prawo do akcji musi podać maksymalną liczbę akcji i termin, inaczej nie jest podstawą emisji | Nikt nie wyemituje „otwartej” liczby akcji ani nie obieca nieograniczonych opcji | § 5 ust. 1 |
| **Łączny limit 2 000 000 akcji** wszystkich serii, łącznie z nierozliczonymi prawami do akcji | Sztywny sufit rozwodnienia; jego podniesienie wymaga zmiany umowy | § 5 ust. 2 |
| **Seria F** — Założyciele Funkcjonalni: limit 250 000 akcji i 20% po emisji, uchwała kwalifikacyjna, odrębna od serii P | Przyjmowanie późniejszych współzałożycieli bez zmiany umowy | § 5 ust. 3 lit. a, § 6 |
| **Seria P** — program motywacyjny: limit 176 471 akcji (15% po pełnym rozwodnieniu), tryb zwykły albo warunkowy | Opcje dla zespołu bez zmiany umowy | § 5 ust. 3 lit. b, § 7 |
| **Upoważnienie z art. 300¹⁰³ KSH** do 31.12.2036 r. | Emisje F i P na podstawie samej uchwały WZ, bez notariusza przy każdej emisji | § 5 ust. 3 |
| **Nowa seria = zmiana umowy** z limitem i terminem | Runda inwestorska zawsze przechodzi przez zmianę umowy i ma określony sufit | § 5 ust. 4 |
| **Emituje tylko WZ**; Rada wykonuje uchwałę w transzach, bez prawa przekroczenia limitu ani obniżenia ceny minimalnej | Szybkie wykonanie bez ryzyka nadużycia | § 5 ust. 5 |
| **Akcje własne (buyback)**: limit 25%, zamknięty katalog celów (umorzenie, program P i seria F), oferta proporcjonalna do wszystkich, cena nie wyższa niż wartość godziwa, wyłączenie dyrektora-zbywcy, zbycie tylko nabywcy bez przeszkód z § 8, kapitał rezerwowy, upoważnienie najwyżej na 5 lat | Zasilanie programu P i umorzenie bez ryzyka uprzywilejowania kogokolwiek. Spółka **nie** odkupuje akcji w vestingu (od 2.1-S — ryzyko obejścia art. 300⁴⁵ § 2 KSH) | § 3 ust. 7–8 |

**Zbywanie akcji i vesting**

| Element | Po co | Gdzie |
|---|---|---|
| **Milczenie Rady przez 14 dni = zgoda** na zbycie + zaświadczenie dla rejestru | Szybkość. S24 (wariant A) nie określa skutku braku odpowiedzi Spółki. | § 8 ust. 1 |
| **Zamknięta lista 4 przyczyn odmowy** (sankcje, brak zgody organu, lock-up, nabywca nie przejął vestingu) | Odmowa nie może być arbitralna | § 8 ust. 2 |
| **Brak obowiązku wskazania nabywcy po Wartości Godziwej** (S24 wariant A: wskazanie w 1 miesiąc) | Każda przyczyna odmowy to przeszkoda prawna albo umowna, a nie decyzja handlowa — przymusowy odkup po wycenie nie ma sensu | § 8 ust. 3 |
| **Lock-up 12 miesięcy** dla założycieli (seria A od wpisu, seria F od Dnia Przyznania) | Stabilność w pierwszym roku | § 8 ust. 4 |
| **Obowiązek zbycia akcji niezwolnionych (vesting)**: 48 miesięcy, cliff 12 miesięcy + 25%, potem co miesiąc; cena emisyjna; umowa wykonawcza i pełnomocnictwo | Ochrona przed odejściem założyciela z pakietem akcji | § 9 |

**Ustrój i tryb działania**

| Element | Po co | Gdzie |
|---|---|---|
| **Procedura uchwał obiegowych**: kto rozsyła projekt (Rada, Przewodniczący, akcjonariusz z 5%), termin 3 dni robocze–21 dni, uchwała zapada w chwili zebrania głosów „za”, wynik e-mailem, brak tajnego głosowania | S24 dopuszcza głosowanie e-mailem, ale nie mówi, jak je przeprowadzić. My mamy gotową procedurę. | § 12 ust. 3 |
| **Forma dokumentowa** dla wszystkich oświadczeń; e-mail z adresu z rejestru wystarcza; doręczenie z chwilą wysłania | Brak sporów o doręczenie | § 12 ust. 2 |
| **Regulamin WZ przyjmowany przy zawiązaniu** | Art. 300⁹² § 2 KSH odsyła do regulaminu — mamy go od pierwszego dnia | § 12 ust. 5 |
| **Obowiązek podania adresu e-mail do rejestru** i aktualizacji danych w 7 dni | Bez tego tryb elektroniczny nie działa | § 3 ust. 6 |
| **Elektroniczne archiwum uchwał** prowadzone przez Radę | Dowód podjęcia uchwały obiegowej | § 12 ust. 8 |
| **11 spraw zastrzeżonych dla WZ z progiem 75%** wszystkich głosów, w tym Umowa o Współpracy ze Spółką Siostrzaną i umowy finansowe z dyrektorami (S24: wszystko bezwzględną większością) | Ochrona mniejszości (B–E mają łącznie 50%) przy sprawach ustrojowych | § 13 |
| **Dyrektor wykonawczy i niewykonawczy**, delegacja z art. 300⁷⁶, głos rozstrzygający Przewodniczącego, sprawy wymagające uchwały Rady z progami 100 tys. i 250 tys. zł | Prowadzenie spraw w modelu monistycznym | § 10 |
| **Reprezentacja w sporach z dyrektorem** (art. 300⁷⁹ § 3–4) | Konflikt interesów | § 11 ust. 3 |

**Ochrona aktywów**

| Element | Gdzie |
|---|---|
| IP tworzone dla Spółki należy do Spółki; wymogi umowy przeniesienia wpisane wprost (forma pisemna, pola eksploatacji, prawa zależne, wynagrodzenie, kwartalne potwierdzenie wykazu utworów); 5-letnia licencja na technologię przedzałożycielską z obowiązkiem przeniesienia na żądanie (szczegóły: `analiza_ip_aport.md`) | § 14 ust. 1–2 |
| Aport IP przenoszony w dniu aktu (po stronie Spółki podpisuje pełnomocnik z art. 300⁷⁹ § 1 KSH), z licencją tymczasową i wykonaniem w naturze (art. 64 KC) | § 4 ust. 6, § 11 ust. 3, § 18 ust. 6 |
| Poufność akcjonariuszy i dyrektorów, także po odejściu | § 14 ust. 3 |
| Kontrola eksportu i sankcje jako obowiązek akcjonariuszy i dyrektorów | § 14 ust. 4 |
| Zakaz konkurencji z wyjątkiem inwestycji portfelowych do 5% | § 14 ust. 5 |
| Zastrzeżenie koncesji (wyroby wojskowe, towary strategiczne, UAS) | § 2 ust. 3 |
| Klasyfikacja bezpieczeństwa i eksportowa przy likwidacji | § 17 ust. 3 |
| Test wypłacalności przed wypłatą dywidendy (art. 300¹⁵ KSH) | § 16 ust. 2 |
| Mediacja przed sądem, klauzula salwatoryjna, dynamiczne odesłania do przepisów | § 18 |

### 2.3. Czego wzorzec S24 miał, a 2.0-S nie — uzupełnione w 2.1-S

Tych elementów brakowało w wersjach 1.0-RC i 2.0-S. Uzupełniono je w rundzie 1 poprawek z audytu (`audyt_rundy.md`).

| S24 | Było (2.0-S) | Jest (od 2.1-S) |
|---|---|---|
| **§ 19 — rok obrotowy** | Brak postanowienia | § 16 ust. 5: rok kalendarzowy; pierwszy rok można połączyć z następnym (art. 3 ust. 1 pkt 9 ustawy o rachunkowości) |
| **§ 11 ust. 1 — zaliczki na dywidendę** | Brak upoważnienia | § 16 ust. 4: Rada upoważniona do wypłaty zaliczek, z testem wypłacalności |
| **§ 10 — głos zastawnika i użytkownika** | Reguła ustawowa | § 3 ust. 9: zastawnik i użytkownik nie głosują (wariant A); wyjątek za zgodą WZ dla zastawu zabezpieczającego finansowanie Spółki (2.3-S) |

### 2.4. Współpraca z Appolonia — Spółka Siostrzana (§ 15)

Basilisk Systems działa na lądzie i w powietrzu, Appolonia — na morzu i wodach śródlądowych. Te same osoby mają pracować w obu spółkach i dzielić technologię. Bez osobnego postanowienia blokowałyby to trzy zasady z samej umowy:

- zakaz konkurencji (§ 14 ust. 5);
- poufność (§ 14 ust. 3);
- wyłączenie dyrektora w konflikcie interesów (§ 10 ust. 6). Przy tych samych osobach w Radach obu spółek nie byłoby nikogo, kto mógłby zatwierdzić transakcję między nimi.

Dlatego obie umowy mają lustrzany paragraf o Spółce Siostrzanej (w Basilisk § 15, w Appolonia też § 15):

| Element | Jak działa | Gdzie |
|---|---|---|
| **Kiedy obowiązuje** | Dopóki założyciele obu spółek łącznie mają ponad 50% głosów w każdej z nich (od 2.2-S — działa też przy częściowo różnym składzie założycieli Appolonii). Jeśli kontrolę przejmie ktoś inny (np. inwestor), postanowienia z ust. 3–7 wygasają po 6 miesiącach. | ust. 1, 8 |
| **Podział obszarów** | Basilisk: ląd i powietrze; Appolonia: morze i wody śródlądowe | ust. 1 |
| **Umowa o Współpracy** | Jedna umowa ramowa: wspólne B+R, personel, sprzęt, dane, licencje, rozliczenia. Zatwierdza ją raz WZ każdej spółki (75%), a w jej granicach Rada nie podejmuje osobnych uchwał. | ust. 2, 6; § 13 ust. 1 lit. j |
| **Ceny rynkowe** | Świadczenia między spółkami wycenia się jak między podmiotami niepowiązanymi — tego wymagają przepisy o cenach transferowych (spółki z tymi samymi właścicielami są dla fiskusa podmiotami powiązanymi). Metody cen określa Umowa o Współpracy, spór o cenę rozstrzyga niezależny biegły. | ust. 2 |
| **Zakaz konkurencji** | Udział, funkcje i praca w spółce siostrzanej w jej obszarze nie są konkurencją i nie wymagają zgody Rady | ust. 3 |
| **Poufność** | Informacje poufne można przekazywać spółce siostrzanej w zakresie potrzebnym do współpracy | ust. 4 |
| **Własność intelektualna** | Wyniki należą do spółki, której obszaru dotyczą. Wyniki przydatne w obu obszarach — do spółki wskazanej w Umowie o Współpracy, a druga dostaje licencję na swój obszar. | ust. 5 |
| **Konflikt interesów** | Sam udział w spółce siostrzanej nie wyłącza dyrektora z głosowania | ust. 6 |
| **Vesting** | Praca dla spółki siostrzanej nie przerywa vestingu, jeśli podział czasu zatwierdzi Rada albo określa go Umowa o Współpracy | ust. 7 |
| **Akcje spółki siostrzanej** | Objęcie lub nabycie akcji siostry tylko za zgodą WZ (75%), z zawiadomieniem o dominacji z art. 6 KSH | ust. 9 |

**Do zrobienia:** sama Umowa o Współpracy (osobny dokument), zatwierdzona uchwałami WZ obu spółek.

---

## 3. In vivo — co zmodyfikowaliśmy i dlaczego

Elementy, które były w 1.0-RC i zostały, ale w zmienionej postaci.

### 3.1. Emisje i serie

| Element | Było (1.0-RC) | Jest (2.3-S) | Dlaczego |
|---|---|---|---|
| **Limity emisji** | Rozproszone: limit serii F w § 9, puli P w § 8, akcji własnych w § 5; brak łącznego limitu; brak zasady dla nowych serii | Jeden § 5: zasada maks. liczby akcji dla każdej uchwały i upoważnienia, łączny limit 2 000 000, limity F i P, nowa seria tylko przez zmianę umowy | Wymóg „wszystko ma maksymalną liczbę akcji” zebrany w jednym miejscu i rozciągnięty na każdą emisję, także przyszłą |
| **Seria F — większość** | 75% **Głosów Uprawnionych w Sprawie**, kandydat-akcjonariusz wyłączony od głosu; emisja i cofnięcie statusu — 75% wszystkich głosów | Zawsze **75% wszystkich głosów**, bez wyłączenia kandydata | Jeden sposób liczenia. Koszt: kandydat, który już ma akcje serii A, głosuje we własnej sprawie — przy 75% wszystkich głosów nie przegłosuje reszty sam. |
| **Seria F — vesting** | Pełne odesłanie do § 10 (trzy kategorie odejścia, przyspieszenie, Wartość Godziwa) | Odesłanie do prostego § 9 | Konsekwencja uproszczenia vestingu |
| **Seria F — zakres** | Podlegała też Dopuszczalnemu Nabywcy, pierwszeństwu, tag i drag | Tylko zgoda na zbycie, lock-up i vesting | Konsekwencja usunięcia 1.1 i 1.2 |
| **Seria P** | 9 ustępów, szczegółowy opis obu trybów emisji i prawa poboru 4/5 | 5 ustępów; limit i termin w § 5; prawo poboru w ogólnej regule § 5 ust. 6 | Bez zmiany merytorycznej — mniej powtórzeń |
| **Akcje własne** | Dwa długie ustępy: cele nabycia, równe traktowanie, wyłączenie dyrektora, cena do Wartości Godziwej, zbycie tylko Dopuszczalnemu Nabywcy | Te same zabezpieczenia w § 3 ust. 7–8, w prostszej formie: 3 cele (umorzenie, program P/seria F, vesting); oferta proporcjonalna do wszystkich poza vestingiem; **wartość godziwa** w jednym zdaniu = cena z ostatniej emisji albo transakcji z niepowiązaną osobą trzecią z 12 miesięcy, a w jej braku wycena niezależnego biegłego; wyłączenie dyrektora-zbywcy; zbycie akcji własnych tylko osobie, wobec której nie ma przeszkód z § 8 ust. 2 lit. a–b (zamiast Dopuszczalnego Nabywcy) | Zabezpieczenia przed odkupem „po znajomości” są potrzebne niezależnie od VC; usunięty był tylko aparat wyceny i Kryterium EU/NATO |
| **Akcje uprzywilejowane** | Dopuszczalne „uchwałą emisyjną zgodną z umową” | Wprost wyłączone; wymagają zmiany umowy (§ 3 ust. 3) | Równe akcje = prostsze progi i brak głosowań odrębnymi seriami |

### 3.2. Zbywanie akcji

| Element | Było | Jest | Dlaczego |
|---|---|---|---|
| **Brak odpowiedzi Rady w 14 dni** | **Odmowa** (fikcja odmowy z przyczyny lit. b) → uruchamia wskazanie nabywcy | **Zgoda** + zaświadczenie w 7 dni dla rejestru akcjonariuszy | Wygoda i szybkość: bezczynność organu nie blokuje akcjonariusza |
| **Przyczyny odmowy** | 6, w tym nabywca spoza Kryterium EU/NATO bez zgody WZ i 60-dniowe wstrzymanie terminu przy brakach | 4: sankcje i kontrola, brak zgody organu (można dać zgodę warunkową), lock-up, nabywca nie przejął vestingu | Usunięcie Kryterium i procedury uzupełniania dokumentów |
| **Po odmowie** | Spółka wskazuje nabywcę w 3 miesiące, cena = Wartość Godziwa, raty, zabezpieczenia, swoboda zbycia przy braku zapłaty | Brak obowiązku wskazania; art. 300³⁹ § 3–5 KSH wyłączone; akcjonariusz może wskazać innego nabywcę | Bez Wartości Godziwej mechanizm wskazania nie działa. **Ryzyko:** memorandum oceniało pełne wyłączenie § 3–5 jako jedyny realny punkt sporny tego paragrafu (pyt. 1.2.1, 1.2.6) — do potwierdzenia u prawnika. |
| **Lock-up — zgoda** | 75% Głosów Uprawnionych w Sprawie, wnioskujący wyłączony | 75% wszystkich głosów | Jeden sposób liczenia. Przy 75% wszystkich głosów sam wnioskujący (maks. 50%) i tak nie wystarczy. |
| **Lock-up — wyjątki** | 4 (runda, tag/drag, vesting, spółka holdingowa) | 2 (vesting, spółka holdingowa) | Tag, drag i runda zniknęły |

### 3.3. Vesting (obowiązek zbycia)

| Element | Było | Jest | Dlaczego |
|---|---|---|---|
| **Harmonogram** | 48 mies., cliff 12 mies. + 25%, potem co miesiąc | Bez zmian | — |
| **Kategorie odejścia** | Usprawiedliwione / Dobrowolne / Zawinione, z definicjami, wymogiem prawomocnego skazania i ustalaniem kategorii niezależnie od podstawy zatrudnienia | **Jedna reguła**: ustanie zaangażowania → akcje niezwolnione po cenie emisyjnej. **Zwolnienie z obowiązku** może przyznać WZ (75%), w szczególności przy śmierci, chorobie, zwolnieniu bez przyczyny albo odejściu uzgodnionym | Spór o kategorię zastępuje decyzja WZ. Sytuacje, które wcześniej były „usprawiedliwione”, są wymienione jako przykłady. |
| **Cena** | Akcje niezwolnione — cena emisyjna; akcje zwolnione przy Odejściu Zawinionym — 80% Wartości Godziwej | Zawsze cena emisyjna, wyłącznie za akcje niezwolnione | Brak wyceny, brak eksperta, brak kary na akcjach zarobionych |
| **Nabywca** | Wskazany Dopuszczalny Nabywca; Spółka tylko w odrębnym trybie | Nabywca wskazany przez Radę w 3 miesiące — **nie Spółka** ani osoba działająca na jej rachunek; w braku wskazania pozostali Założyciele Pierwotni proporcjonalnie (30 dni); po 6 miesiącach obowiązek wygasa, jeśli akcji nie zbyto bez winy założyciela. Akcje zbyte, zwolnione albo z wygasłym obowiązkiem przestają być nim objęte (2.3-S). | Jak w 1.0-RC Spółka nie jest nabywcą (ryzyko obejścia art. 300⁴⁵ § 2 KSH, memorandum 1.5.2); terminy zamykają lukę „zawieszenia” akcji; koniec obowiązku usuwa wzmiankę z rejestru (od 2.1-S do 2.3-S) |
| **Umowa wykonawcza** | Długi katalog treści, umowa przedwstępna, nieodwołalne pełnomocnictwo z poświadczonym podpisem, dom maklerski | Ten sam instrument, opisany w jednym ustępie (§ 9 ust. 6); od 2.3-S umowa dokumentuje, że cena wynika z mechanizmu vestingu (art. 19 PIT) | Szczegóły należą do umowy wykonawczej, nie do umowy spółki |
| **Dziedziczenie** | Osobny § 17 z ograniczeniem wstąpienia spadkobierców | Jedno zdanie: spadkobiercy wstępują, a akcje niezwolnione nadal podlegają obowiązkowi zbycia; WZ może zwolnić | Patrz 1.3 |

### 3.4. Rada Dyrektorów i reprezentacja

| Element | Było | Jest | Dlaczego |
|---|---|---|---|
| **Odwołanie dyrektora** | Z ważnych powodów — większość głosów oddanych; bez ważnych powodów — 75% wszystkich głosów | Zawsze bezwzględna większość głosów oddanych (jak w S24 § 13) | Prostota. **Do decyzji:** A (50%) nie odwoła dyrektora sam, jeśli pozostali głosują przeciw, ale wystarczy mu wstrzymanie się jednego akcjonariusza. Jeśli to ma chronić mniejszość, przywrócić próg 75% dla odwołania bez ważnych powodów. |
| **Quorum** | Połowa składu, z wyłączeniem dyrektora w konflikcie z § 29 ust. 7 | Połowa aktualnie powołanych; dyrektor w konflikcie nie głosuje i nie liczy się do quorum | Ta sama zasada bez odesłania do usuniętego paragrafu |
| **Sprawy Rady** | 11 pozycji (lit. a–k) + weto bezpieczeństwa | 10 pozycji w jednym zdaniu, bez weta; doszły: stwierdzenie wniesienia wkładów i zgoda na zbycie akcji | Wszystkie kompetencje Rady z umowy w jednym miejscu |
| **Dyrektorzy niewykonawczy** | Katalog obszarów nadzoru (finanse, ryzyko, eksport, IP…) | Wymóg co najmniej jednego dyrektora niewykonawczego; zadania w regulaminie Rady | Treść regulaminu |
| **Reprezentacja w sporach z dyrektorem** | Dwa ustępy | Jeden ustęp, ta sama treść | Bez zmiany merytorycznej |

### 3.5. Uchwały akcjonariuszy — tryb zdalny

| Element | Było | Jest | Dlaczego |
|---|---|---|---|
| **Uchwały poza WZ** | Dopuszczone jednym zdaniem; brak procedury | Pełna procedura obiegowa: inicjator, termin 3 dni robocze–21 dni (krócej za zgodą wszystkich), uchwała zapada z chwilą zebrania wymaganych głosów, wynik e-mailem, głos po terminie nieważny | Główny cel uproszczenia: większość uchwał bez zwoływania WZ i bez czekania |
| **Udział zdalny w WZ** | Zasady w regulaminie, a **do czasu jego przyjęcia — w zawiadomieniu** | Regulamin WZ przyjmowany przy zawiązaniu Spółki | Memorandum wskazywało, że zawiadomienie nie jest regulaminem w rozumieniu art. 300⁹² § 2 KSH, co dawało podstawę do zaskarżenia uchwał |
| **Zawiadomienia** | E-mail; zgłaszanie zmian kontroli i beneficjentów rzeczywistych pod kątem Kryterium | E-mail; obowiązek aktualizacji danych w 7 dni (§ 3 ust. 6) | Bez Kryterium |
| **Forma oświadczeń** | Nieokreślona ogólnie | Forma dokumentowa; e-mail z adresu z rejestru wystarcza | Jednoznaczność |
| **Problemy techniczne** | Po stronie akcjonariusza — bez wpływu; po stronie Spółki — wpływ, jeśli mogły zmienić wynik | Tylko pierwsza część | Druga część wynika z ogólnych zasad zaskarżania |

### 3.6. Sprawy zastrzeżone dla WZ (75% wszystkich głosów)

| Było (14 pozycji) | Jest (11 pozycji) |
|---|---|
| zmiana umowy; emisje; nadanie i cofnięcie statusu F; połączenie, podział, przekształcenie, likwidacja; zbycie przedsiębiorstwa i aktywów > 25%; zbycie i wyłączna licencja na kluczowe IP; akcje własne i umorzenie; zobowiązania > 500 tys. zł poza budżetem | **Bez zmian** (lit. a–h) |
| zwiększenie lub zmiana programu motywacyjnego | Wchłonięte przez lit. b (emisje) — zwiększenie puli i tak wymaga zmiany umowy |
| istotna zmiana profilu działalności | Usunięte — zmiana przedmiotu działalności to zmiana umowy (lit. a) |
| wynagrodzenie dyrektorów i ubezpieczenie D&O | **Przeniesione do zwykłej większości** (§ 13 ust. 3) |
| ugoda lub zrzeczenie się roszczeń IP > 500 tys. zł | Usunięte — mieści się w lit. h |
| zatwierdzenie Odejścia Usprawiedliwionego | Zastąpione zwolnieniem z obowiązku zbycia (lit. i) |
| Przedsięwzięcia Produkcyjne > 500 tys. zł | Usunięte — lit. e i h |
| — | **Nowe:** zgoda na zbycie w okresie lock-upu (wcześniej § 25 ust. 3) — lit. i |
| — | **Nowe:** zawarcie, zmiana albo rozwiązanie Umowy o Współpracy ze Spółką Siostrzaną (§ 15) — lit. j |
| — | **Nowe:** umowy kredytu, pożyczki i poręczenia z dyrektorami (art. 15 § 1 KSH nie obejmuje dyrektora P.S.A.) — lit. k |

### 3.7. Pozostałe

| Element | Było | Jest | Dlaczego |
|---|---|---|---|
| **IP, poufność, eksport, konkurencja** | 4 paragrafy (§ 26–29), kilkadziesiąt ustępów | 1 paragraf (§ 14), 6 ustępów; szczegóły w politykach Rady | Umowa ustala zasadę, polityki — wykonanie |
| **Poufność — czas trwania** | 10 lat po zbyciu akcji, tajemnica przedsiębiorstwa — bezterminowo | „Także po ustaniu zaangażowania albo zbyciu akcji, przez okres i w zakresie dopuszczalnym przez prawo” | Mniej sztywno. **Do decyzji:** jeśli wolimy pewność, przywrócić 10 lat. |
| **Zakaz konkurencji — kogo dotyczy** | Akcjonariusze Funkcjonalni (w okresie zaangażowania); zgoda WZ; wyjątek 2% spółki publicznej i Załącznik nr 3 | Założyciele Pierwotni i Akcjonariusze Funkcjonalni (dopóki są akcjonariuszami) oraz dyrektorzy; zgoda Rady bez udziału zainteresowanego; wyjątek 5% portfelowo | Zgoda szybciej (Rada zamiast WZ). Inwestorzy finansowi nie są objęci (od 2.1-S). |
| **Przedmiot działalności** | Cel strategiczny (§ 3) + plan działalności (§ 4 ust. 1–3) + PKD w podziale na główne i dodatkowe + 2 ustępy zastrzeżeń | Jedno zdanie opisu + 13 kodów PKD: 9 ujawnianych w KRS przy pierwszym wpisie (lit. a, z 72.10.Z jako przeważającą) i 4 dla dalszego rozwoju (lit. b) + 1 ustęp zastrzeżeń | Zakres na lądzie i w powietrzu; jednostki nawodne i kody morskie (30.11.Z, 33.15.Z) przeszły do Appolonia P.S.A., żeby zakresy obu spółek się nie pokrywały. Bez kodów wojskowych — wariant z nimi (30.32.Z, 30.40.Z, 33.18.Z) jest na gałęzi `psa_wo`; mniej tekstu opisowego |
| **Zmiana umowy — zgoda indywidualna** | Przy zaostrzeniu vestingu, lock-upu i drag-along | Przy zaostrzeniu vestingu i lock-upu (drag-along zniknął) | Konsekwencja |
| **Załącznik nr 1** | Tabela akcji + Część A (niepieniężne) + Część B (pieniężne) | Część A (akcje + **data rozpoczęcia vestingu**) + B (niepieniężne) + C (pieniężne) | Załącznik nr 2 wchłonięty |

---

## Otwarte sprawy (zebrane z sekcji 2–3)

1. **Art. 300³⁹ § 3–5 KSH** — pełne wyłączenie wskazania nabywcy po odmowie zgody (§ 8 ust. 3). Do potwierdzenia u prawnika.
2. **Odwołanie dyrektora** — przywrócić 75% dla odwołania bez ważnych powodów? (§ 10 ust. 2)
3. **Zakaz konkurencji** — rozwiązane w 2.1-S: obejmuje założycieli, Akcjonariuszy Funkcjonalnych (dopóki są akcjonariuszami) i dyrektorów (§ 14 ust. 5).
4. **Poufność** — czy wpisać sztywne 10 lat (§ 14 ust. 3).
5. **Rok obrotowy** — rozwiązane w 2.1-S (§ 16 ust. 5).
6. **Zaliczki na dywidendę i głos zastawnika** — rozwiązane w 2.1-S (§ 16 ust. 4, § 3 ust. 9).
7. **Dokumenty zależne** — `extra.tex`, `psa_feedback.tex`, `shareholder_agreement.tex` i `uchwaly.tex` odwołują się do paragrafów 1.0-RC, których już nie ma, i pokazują „??” (odpowiednio 127, 53, 56 i 15 odwołań). Wymagają przepisania pod wersję 2.3-S.
8. **Umowa o Współpracy z Appolonia** — osobny dokument do napisania i zatwierdzenia uchwałami WZ obu spółek (§ 15 ust. 2 i 6, § 13 ust. 1 lit. j). Bez niej klauzula o Spółce Siostrzanej daje tylko podstawę, a nie konkretne licencje i rozliczenia.
9. **Prawa autorskie i krzyżowy aport** — analiza skutków braku przeniesienia praw (od osób prywatnych i między spółkami) oraz wariantów krzyżowego aportu akcji: `analiza_ip_aport.md`, z pytaniami do prawnika i doradcy podatkowego w sekcji 3.
10. **Audyt prawny z orzecznictwem** — `audyt.md` (stan po rundach poprawek); historia rund — `audyt_rundy.md`.
