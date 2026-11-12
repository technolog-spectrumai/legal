# Audyt zgodności z prawem: Basilisk Systems P.S.A. — umowa spółki 3.0-S, umowa akcjonariuszy 1.3, umowy przeniesienia praw autorskich 1.3

| | |
|----|----------------|
| **Przedmiot** | 1. Umowa spółki — `psa.tex` 3.0-S (jedna spółka, bez spółki siostrzanej, wersja polska i angielska w jednym dokumencie). 2. Umowa akcjonariuszy — `basilisk_sha.tex` 1.3. 3. Umowy przeniesienia autorskich praw majątkowych — `basilisk_ip.tex` 1.3 (Umowa nr 1 — aport, Umowa nr 2 — utwory tworzone dla Spółki). |
| **Podstawa** | Wcześniejsze audyty: `audyt.md` (umowa spółki, rundy A1–A4, U4–U5) i `basilisk_audyt.md` (umowa akcjonariuszy i umowy IP, U1). Ten audyt sprawdza stan po zmianach U6 (usunięcie § 15, wersja dwujęzyczna, zmiana nazwy) i spójność trzech dokumentów między sobą. |
| **Data** | listopad 2026 r. |
| **Ocena** | **Treść jest zgodna z prawem; 1 ryzyko wysokie dotyczy podpisania umowy akcjonariuszy, nie jej treści.** Brak ryzyk krytycznych. 3 ryzyka średnie, 6 niskich. Kontrola techniczna bez błędów. |

**Oznaczenia.** **[Z]** — sprawdzone na tekście przepisu w `src/legal/` (w tym i wcześniejszych audytach). **[W]** — wiedza ogólna albo wniosek audytora, do potwierdzenia przez prawnika. Raport nie zastępuje opinii adwokata ani radcy prawnego.

---

## 1. Kontrola techniczna

| Sprawdzenie | Wynik |
|----|----|
| Kompilacja trzech dokumentów (PL + EN) | bez błędów; przepełnione wiersze: 0 |
| Nierozwiązane odesłania („??”) w PDF | 0 we wszystkich trzech |
| Ślady spółki siostrzanej (Siostrzana, Sister, Appolonia) w trzech dokumentach | brak |
| § 13 ust. 1 umowy spółki po usunięciu lit. j | 10 pozycji (a–j); dawna lit. k (pożyczki dla dyrektorów) to teraz lit. j; § 13 ust. 4 odsyła do lit. h — nadal właściwej |
| Odesłania `\US` / `\USen` z umowy akcjonariuszy i umów IP do umowy spółki | § 4, 5, 9, 11, 13, 14 — każde wskazuje właściwy paragraf i ustęp 3.0-S; impas: § 13 ust. 1 lit. b i h — emisje i transakcje ponad 500 000 zł |
| Numeracja wersji polskiej i angielskiej | identyczna (§ 1–17, ustępy, litery) |

---

## 2. Rejestr ryzyk

| ID | Dokument, miejsce | Problem | Podstawa | Rekomendacja |
|--|----|---------|----|--------|
| **W1** | Umowa akcjonariuszy — komparycja i podpisy | Umowa jest umową Spółki z Założycielami, a co najmniej część z nich to dyrektorzy. W takiej umowie Spółkę reprezentuje wyłącznie pełnomocnik z uchwały akcjonariuszy. Obecna komparycja dzieli reprezentację („zgodnie z § 11, a w zakresie dotyczącym dyrektorów — pełnomocnik”), a blok podpisów przewiduje „dyrektorzy albo pełnomocnik”. Podpis dyrektorów-Założycieli po stronie Spółki grozi nieważnością umowy w części, w której Spółka jest stroną (wykonanie vestingu, IP, kary) | art. 300⁷⁹ § 1 KSH **[Z]**; SN II CSKP 1733/22 (art. 210 KSH) **[S]**; § 11 ust. 3 i § 17 ust. 6 umowy spółki | Spółkę reprezentuje **tylko** pełnomocnik z uchwały akcjonariuszy. Ponieważ stronami są wszyscy Założyciele, pełnomocnikiem musi być osoba spoza Stron (np. prawnik albo przyszły dyrektor niebędący Założycielem). Uchwała założycielska z § 17 ust. 6 obejmuje umowę z § 9 ust. 6, a umowa akcjonariuszy jest tą umową — wystarczy wskazać tę osobę |
| **Ś1** | Umowa spółki — wersja angielska w tym samym dokumencie | Akt notarialny sporządza się po polsku. Tekst angielski nie może być częścią aktu jako druga wersja umowy spółki; dokument to zaznacza („convenience translation”), ale notariuszowi trzeba przekazać samą wersję polską albo wersję angielską oznaczyć jako tłumaczenie | Prawo o notariacie, ustawa o języku polskim **[W]** | Do aktu — wyłącznie część polska; część angielska jako informacyjne tłumaczenie poza aktem |
| **Ś2** | Umowa akcjonariuszy § 8 | Zakaz konkurencji po odejściu bez odszkodowania wobec osób niebędących pracownikami — dopuszczalny, ale podlega ocenie sądu (bez zmian od poprzedniego audytu, Ś4) | art. 353¹, art. 58 § 2 KC **[Z]**; ocena **[W]** | Decyzja Założycieli; ewentualnie umiarkowane odszkodowanie |
| **Ś3** | Umowa spółki § 8 ust. 1 | Fikcja zgody na zbycie akcji — tekst art. 300³⁹ § 1 KSH jej nie wyklucza, ale brak orzeczeń i praktyki (rezydualne z `audyt.md`) | art. 300³⁹ § 1 KSH **[Z]** | Uzgodnić z podmiotem prowadzącym rejestr akcjonariuszy przed aktem |
| **N1** | Umowa akcjonariuszy — blok podpisów | Po W1: „za Spółkę: pełnomocnik” (PL i EN) | — | Poprawka redakcyjna razem z W1 |
| **N2** | Umowa akcjonariuszy § 5, Załączniki A i B | Akcje w majątku wspólnym małżonków: akcjonariuszem jest małżonek wpisany do rejestru, ale dla pewności co do zobowiązania do zbycia warto mieć oświadczenie małżonka | SN III CSKP 65/21, III CZP 109/22 **[Z]** (memorandum); art. 37 KRO **[W]** | Krótka zgoda małżonka Założyciela na umowę akcjonariuszy i ofertę zbycia |
| **N3** | Umowa akcjonariuszy § 9 | Kwoty kar umownych do uzupełnienia; zbyt wysokie mogą zostać zmiarkowane | art. 484 § 2 KC **[Z]** | Kwoty proporcjonalne do wartości akcji i szkody |
| **N4** | Umowa spółki — Załącznik nr 1, tabela § 4 ust. 1 | Skład i udziały Założycieli (50/20/10/10/10), daty rozpoczęcia vestingu, wkłady w Częściach B1/B2 — do uzupełnienia | — | Uzupełnić przed aktem; dla Części B1 — oświadczenia twórców (Załącznik 1.2 umów IP) |
| **N5** | Dokumentacja poza tymi trzema plikami | `prosta.md` i `audyt.md` opisują wersję 2.5-S (z § 15, § 13 lit. k, § 16–18); `appolonia.tex` nadal wskazuje Basilisk jako spółkę siostrzaną, choć umowa Basilisk takiego postanowienia już nie ma | — | Przy zakładaniu Appolonii przywrócić klauzulę w obu umowach albo usunąć ją z Appolonii; dokumentację uaktualnić przy następnej rundzie |
| **N6** | Umowy IP — Umowa nr 2 § 4 ust. 3 | Wynagrodzenie dyrektora bez wynagrodzenia za prawa — kwota do uzupełnienia; przy kwocie zerowej umowa powinna wprost stanowić o nieodpłatności (art. 43 ust. 1) dla utworów innych niż programy | art. 43 ust. 1, art. 77 ust. 1 pr. aut. **[Z]** | Wpisać kwotę albo wprost „nieodpłatnie” |

---

## 3. Co jest zgodne

**Umowa spółki 3.0-S**

- Usunięcie § 15 nie narusza spójności: brak osieroconych odesłań, § 1–14 bez zmian, sprawy zastrzeżone 10 pozycji z poprawnymi odesłaniami.
- Utrzymane wszystkie rozwiązania z rund U1–U5 ocenione w `audyt.md`: pełnomocnik do umów z dyrektorami (art. 300⁷⁹ § 1, uchwała III CZP 71/18), vesting bez Spółki jako nabywcy (art. 300⁴⁵ § 2), uchwały poza WZ (art. 300⁸⁰), udział zdalny (art. 300⁹²), limity emisji (art. 300¹⁰³), rok obrotowy (art. 3 ust. 1 pkt 9 UoR), Załącznik nr 1 z Częściami B1/B2 (art. 17 ust. 1e PIT) **[Z]**.
- Bez spółki siostrzanej znikają ryzyka z A4-1 (wzajemna dominacja, art. 4 § 1 pkt 4 lit. d, art. 300⁴⁸ KSH), ceny transferowe między siostrami i kwestia EDF/Pzp.
- Pożyczki dla dyrektorów: zgoda WZ wymagana umową (§ 13 ust. 1 lit. j) i ustawą (art. 15 § 1 w zw. z art. 4 § 2¹ KSH) **[Z]**.

**Umowa akcjonariuszy 1.3**

- Czas oznaczony 10 lat z przedłużeniem (art. 365¹ KC nie ma zastosowania), zobowiązanie wobec Spółki na rzecz wskazanego nabywcy (art. 393 KC), nieodwołalne pełnomocnictwo (art. 101 § 1–2, art. 108 KC), forma zbycia akcji (art. 300³⁶ § 4, art. 300³⁷ § 1 KSH), kary umowne tylko za zobowiązania niepieniężne (art. 483 § 1, art. 484 § 1 KC), zmiany za zgodą wszystkich, pracownicy — art. 101² KP **[Z]**.
- Klauzula językowa: rozstrzyga wersja polska; wersja angielska zgodna co do treści i numeracji.

**Umowy przeniesienia praw autorskich 1.3**

- Forma pisemna (art. 53 pr. aut., art. 78¹ § 2 KC), pola eksploatacji (art. 41 ust. 2 i 4, art. 50, art. 74 ust. 4), prawa zależne (art. 46), utwory przyszłe tylko w ramach zadań (art. 41 ust. 3), wynagrodzenie i art. 77 ust. 1, prawo do patentu (art. 11 ust. 3, art. 12 ust. 2 PWP), warunek z art. 169 § 1 w zw. z art. 300¹³ § 1 KSH, reprezentacja wariantowa (art. 300¹¹ § 2, art. 300⁷⁹ § 1), odpowiedzialność za wartość aportu (art. 300¹⁰) **[Z]**.
- Siedziba Pruszków i nazwa Basilisk Systems spójne we wszystkich trzech dokumentach.

---

## 4. Przed aktem notarialnym

1. **W1:** wskazać w uchwale założycielskiej pełnomocnika spoza grona Założycieli do podpisania umowy akcjonariuszy i umów z § 4 ust. 6 i § 9 ust. 6 z Założycielami-dyrektorami; poprawić komparycję i podpisy umowy akcjonariuszy.
2. **Ś1:** do notariusza — tylko część polska umowy spółki.
3. **Ś3:** uzgodnić z podmiotem prowadzącym rejestr akcjonariuszy fikcję zgody i wzmianki o vestingu.
4. **N2–N4, N6:** zgody małżonków, kwoty kar, tabela Założycieli, Załącznik nr 1 (B1/B2) z oświadczeniami twórców, wynagrodzenie w Umowie nr 2.
5. Decyzja w sprawie zakazu konkurencji (Ś2) i przegląd całości przez prawnika.

---

## 5. Poprawki na gałęzi `dev_1211` (umowa spółki 3.1-S, umowa akcjonariuszy 1.4)

| ID | Status | Zmiana |
|--|--|------|
| **W1**, **N1** | usunięte | Umowa akcjonariuszy: Spółkę reprezentuje wyłącznie pełnomocnik z uchwały akcjonariuszy objętej aktem zawiązania (art. 300⁷⁹ § 1 KSH, § 11 ust. 3 i § 17 ust. 6 umowy spółki), niebędący Stroną; podpis „za Spółkę: pełnomocnik” (PL i EN) |
| **Ś3** | usunięte | Decyzja Założycieli: rezygnacja z fikcji zgody. § 8 ust. 1: Rada udziela albo odmawia zgody w 14 dni w formie dokumentowej; milczenie nie jest zgodą; akcjonariusz może wezwać Radę do zajęcia stanowiska w dodatkowe 7 dni, a dyrektorzy odpowiadają za szkodę z bezpodstawnej zwłoki. Zamknięta lista przyczyn odmowy (§ 8 ust. 2) bez zmian. Wersja z fikcją zgody zostaje na gałęzi `psa_simple2` |
| **N2** | usunięte | Umowa akcjonariuszy 1.5: obowiązek przedstawienia zgody małżonka przy wspólności majątkowej (także przez przystępujących) i Załącznik D / Schedule D — wzór zgody (umowa, oferta, pełnomocnictwo, zbycie po cenie emisyjnej, przystąpienie po ustaniu wspólności) |
| **N6** | usunięte | Umowy IP 1.4, Umowa nr 2 § 4 ust. 1 i 3: wariant „przeniesienie nieodpłatne” (art. 43 ust. 1 pr. aut.) obok kwoty wynagrodzenia (PL i EN) |
