# Audyt zgodności z prawem: umowa akcjonariuszy i umowy przeniesienia praw autorskich — Basilisk Systems P.S.A.

| | |
|----|----------------|
| **Przedmiot** | 1. Umowa akcjonariuszy — `basilisk_sha.tex`, wersja 1.0 (projekt). 2. Umowy przeniesienia autorskich praw majątkowych — `basilisk_ip.tex`, wersja 1.0: Umowa nr 1 (aport przy zawiązaniu) i Umowa nr 2 (utwory tworzone dla Spółki). |
| **Data** | listopad 2026 r.; poprawki U1 — punkt 4 (umowa akcjonariuszy i umowy IP w wersji 1.1, umowa spółki `psa.tex`) |
| **Stan prawny** | Teksty ujednolicone w `src/legal/`: KC (Dz.U. 2026 poz. 795), KSH (Dz.U. 2024 poz. 18 z późn. zm.), prawo autorskie (Dz.U. 2025 poz. 24), PWP, Kodeks pracy, PIT (Dz.U. 2026 poz. 592). |
| **Ocena** | **Dokumenty są co do zasady zgodne z prawem, ale wymagają poprawek przed podpisaniem:** 1 ryzyko krytyczne (brak umowy spółki Basilisk Systems), 3 wysokie, 4 średnie, 5 niskich. Żadne postanowienie nie jest sprzeczne z bezwzględnie obowiązującym przepisem w sposób nieusuwalny. |

> **Zmiana nazwy (U2):** dokumenty przygotowane pierwotnie dla „Aurelian” dotyczą teraz Basilisk Systems P.S.A. (`basilisk_sha.tex`, `basilisk_ip.tex`, wersje 1.3, siedziba Pruszków). Umowa spółki to `psa.tex` 3.0-S — jedna spółka, bez spółki siostrzanej; Appolonia zostanie dodana później.

**Oznaczenia.** **[Z]** — sprawdzone na tekście przepisu w `src/legal/`. **[W]** — wiedza ogólna albo wniosek audytora, do potwierdzenia przez prawnika. Raport nie zastępuje opinii adwokata ani radcy prawnego.

**Poziomy ryzyka.** **K** — krytyczne (mechanizm nie zadziała); **W** — wysokie (realne ryzyko nieważności albo sporu); **Ś** — średnie; **N** — niskie (redakcja).

---

## 1. Rejestr ryzyk

| ID | Dokument, miejsce | Problem | Podstawa | Poprawka |
|--|----|---------|----|--------|
| **K1** | oba dokumenty | Nie ma umowy spółki Basilisk Systems. Oba dokumenty odsyłają do numeracji wariantu 2.5-S (makro `\US`): vesting (§ 9), zbywanie (§ 8), IP (§ 14), Załącznik nr 1 z Częściami B1/B2. Bez tych postanowień w umowie spółki obowiązek zbycia nie jest obowiązkiem związanym z akcją, nie trafia do rejestru akcjonariuszy i nie wiąże nabywców akcji — zostaje tylko zobowiązanie między stronami umowy akcjonariuszy | art. 300³⁹ § 1, art. 300¹ § 3 KSH; art. 57 § 2 KC **[Z]** | Przygotować `psa.tex` z umowy 2.5-S (jedna spółka, bez § 15 o spółce siostrzanej) i zachować numerację albo zaktualizować makro `\US` |
| **W1** | SHA § 12 ust. 1 i 3 | Umowa zawarta na czas nieoznaczony, a jej wypowiedzenie wymaga zgody 75% głosów. Zobowiązanie bezterminowe o charakterze ciągłym wygasa po wypowiedzeniu przez każdą stronę. Wyłączenie tego prawa jest sprzeczne z naturą stosunku i grozi nieważnością postanowienia, a w sporze — uznaniem umowy za wypowiadalną w każdym czasie | art. 365¹, art. 353¹, art. 58 § 1 KC **[Z]** | Czas oznaczony (np. 10 lat z automatycznym przedłużeniem o 5 lat, chyba że strona wypowie na 12 miesięcy przed końcem) albo dopuszczenie wypowiedzenia z długim terminem; wygaśnięcie z chwilą utraty statusu akcjonariusza zostawić |
| **W2** | Umowa nr 1 § 2 ust. 4 | Warunek rozwiązujący: zwrot praw, jeżeli Spółka nie zostanie wpisana w 12 miesięcy. Ustawowo umowa spółki ulega rozwiązaniu, gdy zgłoszenia nie złożono w 6 miesięcy albo odmowa wpisu jest prawomocna. Przy przewlekłym postępowaniu przed sądem rejestrowym (wniosek złożony w terminie, wpis po 12 miesiącach) prawa wróciłyby do Założyciela, a Spółka zostałaby wpisana z niewniesionym wkładem | art. 300¹³ § 1 w zw. z art. 169 § 1 KSH; art. 89 KC **[Z]** | Powiązać warunek z rozwiązaniem umowy spółki na podstawie art. 169 § 1 w zw. z art. 300¹³ § 1 KSH (brak zgłoszenia w 6 miesięcy albo prawomocna odmowa wpisu) |
| **W3** | Umowa nr 1, komparycja; wprowadzenie | Spółkę w organizacji reprezentuje zarząd, czyli rada dyrektorów, a do jej ustanowienia — pełnomocnik powołany **jednomyślną** uchwałą akcjonariuszy. Pełnomocnik z art. 300⁷⁹ § 1 jest wymagany tylko przy umowie z dyrektorem. Wzór przewiduje zawsze „pełnomocnika z art. 300⁷⁹ § 1” — przy Założycielu niebędącym dyrektorem to podstawa niewłaściwa | art. 300¹¹ § 2, art. 300⁷⁹ § 1, art. 4 § 2¹ KSH **[Z]** | Komparycja wariantowa: (a) Założyciel-dyrektor — pełnomocnik z uchwały akcjonariuszy (art. 300⁷⁹ § 1), niebędący stroną umowy; (b) pozostali — dwóch dyrektorów (§ 11 ust. 1 umowy spółki); (c) przed powołaniem Rady — pełnomocnik z jednomyślnej uchwały (art. 300¹¹ § 2) |
| **Ś1** | SHA § 10 ust. 2 | Pożyczka od Założyciela wymaga uchwały Rady. Jeżeli pożyczkodawca jest dyrektorem, umowę po stronie Spółki musi zawrzeć pełnomocnik z uchwały akcjonariuszy; inaczej grozi nieważność | art. 300⁷⁹ § 1 KSH **[Z]**; SN II CSKP 1733/22 (art. 210 KSH) | Dopisać: „a jeżeli pożyczkodawca jest dyrektorem — umowę zawiera pełnomocnik, o którym mowa w § 11 ust. 3 Umowy Spółki” |
| **Ś2** | SHA § 5 ust. 1, Załącznik A | Nieodwołalna oferta zbycia jest skierowana do nabywcy, który zostanie wskazany w przyszłości. Oferta to oświadczenie „drugiej stronie”, więc jej skuteczność wobec nieoznaczonego adresata jest wątpliwa. Mechanizm i tak działa dzięki pełnomocnictwu (§ 5 ust. 3) | art. 66 § 1 KC **[Z]**; skutek **[W]** | Przeformułować na zobowiązanie wobec Spółki do zbycia akcji na rzecz osoby przez nią wskazanej (świadczenie na rzecz osoby trzeciej, art. 393 KC **[Z]**); ofertę zostawić jako instrument pomocniczy |
| **Ś3** | SHA § 13 ust. 1 | Zmiana umowy większością 75% wiąże strony, które się nie zgodziły. Skuteczność takiego mechanizmu wobec strony przeciwnej jest niepewna | art. 353¹ KC **[Z]**; skutek **[W]** | Zmiana za zgodą wszystkich stron; większość 75% tylko dla zmian technicznych (adresy, załączniki, dostosowanie do zmiany umowy spółki) |
| **Ś4** | SHA § 8 | Zakaz konkurencji po odejściu bez odszkodowania wobec osoby niebędącej pracownikiem. Co do zasady dopuszczalny, ale sąd może go ocenić jako nadmierny. Obecny zakres jest umiarkowany: 12 miesięcy, faktyczny przedmiot działalności, zwolnienie przy odejściu uzasadnionym bez zwolnienia akcji | art. 353¹, art. 58 § 2 KC **[Z]**; ocena **[W]** | Zostawić; dla wzmocnienia rozważyć umiarkowane odszkodowanie albo jego zastąpienie zwolnieniem akcji. Pracownicy — osobna umowa z odszkodowaniem (art. 101² KP **[Z]**), co § 8 ust. 4 już przewiduje |
| **N1** | Umowa nr 1 § 2, Umowa nr 2 § 2 (lista pól) | „Udzielanie licencji i sublicencji oraz zbywanie praw” nie jest polem eksploatacji, lecz uprawnieniem nabywcy praw | art. 41 ust. 1 pkt 2, art. 50 pr. aut. **[Z]** | Przenieść do osobnego zdania: „Spółka może udzielać licencji i przenosić nabyte prawa bez zgody Twórcy” |
| **N2** | Umowa nr 1 § 3 ust. 2, Umowa nr 2 § 3 ust. 2 | Upoważnienie do decydowania o pierwszym udostępnieniu i nadzoru — dla programów komputerowych te prawa osobiste nie istnieją | art. 77 ust. 1 w zw. z art. 16 pkt 3–5 pr. aut. **[Z]** | Dodać „w zakresie utworów niebędących programami komputerowymi” |
| **N3** | SHA § 11 ust. 2 | Impas odsyła do § 13 ust. 1 lit. j umowy spółki (Umowa o Współpracy ze Spółką Siostrzaną) — w Basilisk Systems bez spółki siostrzanej ta litera nie ma treści | — | Odesłać do lit. b i h albo do listy spraw w umowie spółki Basilisk Systems |
| **N4** | Umowa nr 2, wprowadzenie | Wzór nie jest przeznaczony dla pracowników: prawa do programu pracownika przysługują pracodawcy z mocy ustawy, a do innych utworów — z chwilą przyjęcia | art. 12, art. 74 ust. 3 pr. aut. **[Z]** | Dopisać we wprowadzeniu; dla pracowników — klauzula IP w umowie o pracę (pola eksploatacji, prawa zależne, potwierdzenia) |
| **N5** | oba dokumenty | Dane osobowe (PESEL, adresy) bez klauzuli informacyjnej | RODO art. 13 **[W]** | Krótka klauzula informacyjna Spółki jako administratora |

---

## 2. Co jest zgodne

### Umowa akcjonariuszy

- **Pełnomocnictwo do zbycia akcji.**
  - Nieodwołalność jest dopuszczalna, bo wynika z treści stosunku podstawowego (wykonanie obowiązku z umowy spółki), tak samo zastrzeżenie, że nie wygasa ze śmiercią mocodawcy (art. 101 § 1–2 KC **[Z]**; SN V CSK 522/18).
  - Pełnomocnik może być drugą stroną albo reprezentować obie strony, jeżeli dopuszcza to treść pełnomocnictwa (art. 108 KC **[Z]**) — Załącznik B to przewiduje.
  - Forma: zbycie akcji P.S.A. wymaga formy dokumentowej, a nabycie następuje z wpisem do rejestru (art. 300³⁶ § 4, art. 300³⁷ § 1 KSH **[Z]**). Pełnomocnictwo w formie co najmniej dokumentowej spełnia art. 99 § 1 KC **[Z]**.
- **Ograniczenie zbycia do osób przystępujących** (§ 2) jest ważne jako zobowiązanie (art. 57 § 2 KC **[Z]**). Zbycie wbrew niemu jest skuteczne, a skutkiem są roszczenia odszkodowawcze — dlatego ograniczenia rzeczowe muszą być w umowie spółki (K1).
- **Porozumienie o głosowaniu** (§ 4 ust. 4) — ważne między stronami (art. 353¹ KC **[Z]**); nie wiąże Spółki ani nie wpływa na ważność uchwał.
- **Cena równa cenie emisyjnej** z udokumentowaniem jej źródła — zgodne z art. 19 ust. 1 i 4 PIT **[Z]** (uzasadniona przyczyna odstępstwa od wartości rynkowej); Spółka nie jest nabywcą, więc nie ma obejścia art. 300⁴⁵ § 2 KSH.
- **Kary umowne** zastrzeżone wyłącznie za zobowiązania niepieniężne (niezbywanie i nieobciążanie akcji, poufność, zakaz konkurencji), z dopuszczeniem odszkodowania ponad karę i z limitem — zgodne z art. 483 § 1 i art. 484 § 1 KC **[Z]**. Sąd może karę miarkować (art. 484 § 2 KC) — kwoty powinny być proporcjonalne.
- **Pracownicy:** zakaz konkurencji po ustaniu stosunku pracy odesłany do umowy z odszkodowaniem (art. 101² KP **[Z]**).
- **Poufność** 5 lat, a tajemnica przedsiębiorstwa dopóki ma taki charakter — zgodne z ustawą o zwalczaniu nieuczciwej konkurencji **[W]**.
- **Spory:** mediacja i sąd właściwy dla siedziby Spółki — umowa o właściwość w formie pisemnej i dla oznaczonego stosunku (art. 46 KPC **[W]**).

### Umowy przeniesienia praw autorskich

- **Forma pisemna pod rygorem nieważności** (art. 53 pr. aut. **[Z]**); kwalifikowany podpis elektroniczny jest jej równoważny (art. 78¹ § 2 KC **[Z]**).
- **Pola eksploatacji** wymienione wprost i znane w chwili zawarcia (art. 41 ust. 2 i 4, art. 50, art. 74 ust. 4 pr. aut. **[Z]**); wyraźne przeniesienie prawa zezwalania na wykonywanie praw zależnych (art. 46 pr. aut. **[Z]**).
- **Umowa nr 2 i utwory przyszłe:** dotyczy wyłącznie utworów stworzonych w wykonaniu zadań, z wyraźnym zastrzeżeniem — zgodna z art. 41 ust. 3 pr. aut. **[Z]**. Kwartalne potwierdzenia porządkują dowód przejścia praw.
- **Wynagrodzenie:** wyłączenie odrębnego wynagrodzenia za pola (art. 45), godziwość (art. 43 ust. 2) i informacja z art. 47¹ — prawidłowo ograniczone do utworów niebędących programami (art. 77 ust. 1 pr. aut. **[Z]**).
- **Wynalazki:** przy B2B prawo do patentu przysługuje zamawiającemu z mocy ustawy, chyba że strony ustalą inaczej (art. 11 ust. 3 PWP **[Z]**); przeniesienie prawa do uzyskania patentu wymaga formy pisemnej (art. 12 ust. 2 PWP **[Z]**) — zachowana.
- **Aport (Umowa nr 1):** wynagrodzenie w akcjach, odpowiedzialność Założyciela za zawyżoną wartość wkładu (art. 300¹⁰ KSH **[Z]**), wykonanie w naturze (art. 64 KC **[Z]**), oświadczenie twórcy dla art. 17 ust. 1e i art. 5a pkt 34–35 PIT **[Z]**, podział na Części B1/B2.

---

## 3. Kolejność prac

1. **K1:** umowa spółki Basilisk Systems na bazie 2.5-S (bez § 15), z Załącznikiem nr 1 B1/B2.
2. **W1–W3:** czas trwania umowy akcjonariuszy, warunek z art. 169 KSH w Umowie nr 1, komparycja wariantowa Umowy nr 1.
3. **Ś1–Ś3:** pożyczki od dyrektorów, przebudowa oferty na zobowiązanie wobec Spółki (art. 393 KC), zmiany umowy za zgodą wszystkich.
4. **N1–N5:** poprawki redakcyjne.
5. Przegląd przez prawnika: zakaz konkurencji bez odszkodowania (Ś4) i mechanizm oferty (Ś2).

---

## 4. Poprawki U1 (umowa akcjonariuszy i umowy IP — wersja 1.1)

| ID | Status | Co zmieniono | Gdzie |
|--|--|------------|----|
| **K1** | usunięte | Umowa spółki Basilisk Systems `psa.tex` (od wersji 3.0-S: jedna spółka, bez § 15 o spółce siostrzanej i bez § 13 ust. 1 lit. j; zakres ląd i powietrze, siedziba Pruszków; wersja polska i angielska w jednym dokumencie). Numeracja § 1–14 bez zmian, więc odesłania `\US` są poprawne | `psa.tex` |
| **W1** | usunięte | Czas oznaczony 10 lat z przedłużeniem o 5 lat, chyba że strona odmówi na 12 miesięcy przed końcem; wcześniejsze wypowiedzenie tylko z ważnych powodów, bez zwolnienia z obowiązków z umowy spółki, poufności i zakazu konkurencji | SHA § 12 ust. 1 i 3 |
| **W2** | usunięte | Zwrot praw wyłącznie przy rozwiązaniu umowy spółki z art. 169 § 1 w zw. z art. 300¹³ § 1 KSH | Umowa nr 1 § 2 ust. 4 |
| **W3** | usunięte | Komparycja wariantowa (pełnomocnik z art. 300⁷⁹ § 1 / dwóch dyrektorów / pełnomocnik z art. 300¹¹ § 2), także w podpisach i protokole wydania | Umowa nr 1, wprowadzenie, Załącznik 1.3 |
| **Ś1** | usunięte | Pożyczka od dyrektora — pełnomocnik z art. 300⁷⁹ § 1 KSH | SHA § 10 ust. 2 |
| **Ś2** | usunięte | Zobowiązanie wobec Spółki do zbycia na rzecz wskazanego nabywcy z prawem nabywcy do żądania (art. 393 KC); oferta i pełnomocnictwo jako zabezpieczenie | SHA § 5 ust. 1 |
| **Ś3** | usunięte | Zmiana umowy za zgodą wszystkich stron; większość 75% tylko dla zmian technicznych, które nie zwiększają obowiązków ani nie ograniczają praw | SHA § 13 ust. 1 |
| **Ś4** | bez zmian | Zakaz konkurencji bez odszkodowania — decyzja Założycieli i ocena prawnika | SHA § 8 |
| **N1** | usunięte | Udzielanie licencji i zbywanie praw przeniesione z listy pól eksploatacji do osobnego zdania | makro `\PolaEksploatacji` |
| **N2** | usunięte | Upoważnienie do pierwszego udostępnienia i nadzoru ograniczone do utworów niebędących programami | Umowa nr 1 i 2, § 3 ust. 2 |
| **N3** | usunięte | Impas odsyła do § 13 ust. 1 lit. b albo h | SHA § 11 ust. 2 |
| **N4** | usunięte | We wprowadzeniu: wzór nr 2 nie dotyczy pracowników (art. 12, art. 74 ust. 3 pr. aut.) | `basilisk_ip.tex`, wprowadzenie |
| **N5** | usunięte | Podstawa przetwarzania danych (RODO) w postanowieniach końcowych | SHA § 13, Umowa nr 1 § 6, Umowa nr 2 § 8 |

**Kontrola techniczna:** `psa.tex`, `basilisk_sha.tex` i `basilisk_ip.tex` (po 13 stron) się kompilują; nierozwiązanych odwołań i przepełnionych wierszy: 0. Wszystkie odesłania `\US{n}` (§ 4, 5, 9, 11, 13, 14) wskazują właściwe paragrafy `psa.tex`.

**Założenia do potwierdzenia:** skład i udziały Założycieli (tabela 50/20/10/10/10 przejęta z wariantu 2.5-S).

