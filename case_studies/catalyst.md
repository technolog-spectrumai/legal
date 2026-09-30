# Catalyst: rynek obligacji GPW jako źródło finansowania firmy obronnej

Dokument wewnętrzny Basilisk Systems, informacyjny. Nie jest opinią prawną ani rekomendacją inwestycyjną i nie zmienia umowy spółki. Powstał jako uzupełnienie `case_studies/wb_electronics.md`: WB Electronics finansowało rozwój m.in. obligacjami notowanymi na Catalyst, a strona z notowaniami obligacji korporacyjnych (https://gpwcatalyst.pl/notowania-obligacji-obligacje-korporacyjne) pokazuje, jak taki dług wygląda z zewnątrz. Dokument wyjaśnia, czym jest Catalyst, co widać w tabeli notowań, jak wygląda emisja i wprowadzenie obligacji, ile to kosztuje i co z tego wynika dla Basiliska. Odesłania do umowy według `psa.tex` w wersji 0.9.4-C (numery § według `spis_tresci.md`).

Stan na 30 września 2026 r. Oznaczenia wiarygodności jak w `regulations.md`: **[Z]** — sprawdzone w źródle urzędowym albo w dokumencie GPW/KDPW/KNF; **[M]** — doniesienie prasowe albo streszczenie; **[W]** — wiedza ogólna o prawie albo praktyce rynkowej, do potwierdzenia u kancelarii albo w domu maklerskim; **[?]** — szacunek albo hipoteza. Uwaga metodyczna: strony gpwcatalyst.pl, lexlege.pl, forbes.pl i inne były w tej sesji niedostępne do pełnego odczytu (blokada sieciowa); fakty pochodzą ze streszczeń wyszukiwarki, a przepisy trzeba sprawdzić w tekście ustawy i Regulaminu ASO przed decyzją.

---

## 1. Główny wniosek

1. **Catalyst to rynek wtórny obligacji prowadzony przez GPW i BondSpot**, działający od 30 września 2009 r. **[W]**, na którym notowane są obligacje skarbowe, korporacyjne, komunalne, spółdzielcze i listy zastawne. Na 1 czerwca 2026 r. było na nim 876 serii w złotych o wartości emisji ponad 1,73 bln zł, z czego zdecydowana większość to obligacje skarbowe; obligacje korporacyjne i listy zastawne to ok. 75 mld zł, a obligacje komunalne ok. 53 mld zł **[M]**.
2. **Strona z notowaniami obligacji korporacyjnych to lista serii obligacji firm dopuszczonych do obrotu**, wiersz po wierszu: kod serii (np. WBE1126 = WB Electronics, wykup w listopadzie 2026 r.), kurs w procentach wartości nominalnej, oprocentowanie bieżące (zwykle WIBOR plus marża), termin wykupu i obroty. To odpowiednik tabeli notowań akcji, tylko dla długu; sekcja 2 wyjaśnia, jak ją czytać.
3. **Obligacje na Catalyst są instrumentem dla firm z przepływami, nie dla startupów**: WB wyemitowało pierwsze obligacje w 2014 r., po 17 latach działalności, przy ok. 300 mln zł przychodów, i płaciło WIBOR plus 2–3,7 pp; rynek w 2026 r. wycenia ryzyko zwykle na 3–5 pp ponad WIBOR, a dla dużych, znanych emitentów ok. 3 pp **[M]**.
4. **Emisja obligacji i wprowadzenie ich do ASO Catalyst są proceduralnie proste** (dokument informacyjny bez zatwierdzenia przez KNF, brak wymogu Autoryzowanego Doradcy dla obligacji, kapitał własny emitenta co najmniej 2 mln zł), ale wiążą się z obowiązkami informacyjnymi (raporty bieżące i okresowe w EBI/ESPI, rozporządzenie MAR) i kosztami stałymi rzędu kilkudziesięciu tysięcy złotych na serię plus prowizja plasowania **[M]/[W]**.
5. **Prosta spółka akcyjna może emitować obligacje** (emitentem może być osoba prawna prowadząca działalność gospodarczą), ale obligacje zamienne P.S.A. może oferować tylko przez firmę inwestycyjną albo wyłącznie własnym akcjonariuszom **[W]/[Z]**. W projekcie umowy Basiliska emisja instrumentów zamiennych jest Sprawą Zastrzeżoną (§ 25 ust. 1 lit. b, § 31 ust. 4), a zabezpieczenia na Kluczowej Własności Intelektualnej wymagają uchwały WZ (§ 31 ust. 4).
6. **Rynek się zmienia**: GPW zapowiedziało rewitalizację Catalyst (szczegóły w listopadzie 2026 r., wdrożenie od 2027 r.: krótsza droga do notowania, płynność, emisje detaliczne), a od 1 stycznia 2027 r. działają Osobiste Konta Inwestycyjne (OKI) z limitem 100 tys. zł bez podatku od zysków kapitałowych, co ma zwiększyć popyt detaliczny na obligacje korporacyjne **[M]**.

---

## 2. Co pokazuje strona z notowaniami

Strona https://gpwcatalyst.pl/notowania-obligacji-obligacje-korporacyjne to tabela wszystkich serii obligacji korporacyjnych notowanych na Catalyst (na rynku regulowanym GPW i w alternatywnym systemie obrotu GPW), z filtrem po pierwszej literze nazwy emitenta. Jak ją czytać **[W]**:

| Kolumna | Co znaczy | Przykład WB Electronics |
|---|---|---|
| Nazwa / kod serii | skrót emitenta i termin wykupu: trzy litery plus miesiąc i rok (MMRR) | WBE1126: WB Electronics, wykup 6 listopada 2026 r. |
| Kurs (odniesienia, otwarcia, ostatni) | cena w procentach wartości nominalnej, bez odsetek narosłych; 100,00 oznacza cenę równą nominałowi (1000 zł za obligację o nominale 1000 zł); poniżej 100 rynek żąda wyższej rentowności niż kupon | kurs do sprawdzenia na stronie; przy stabilnym emitencie i krótkim terminie zwykle blisko 100 **[?]** |
| Zmiana | zmiana kursu w punktach procentowych względem kursu odniesienia | — |
| Oprocentowanie bieżące | stawka w bieżącym okresie odsetkowym: dla obligacji zmiennokuponowych WIBOR 3M albo 6M plus marża | WBE1126: WIBOR 3M plus marża ustalona w book-buildingu w 2023 r. (Obligacje.pl podaje wcześniejsze serie: 2,78 pp w 2017 r., 2,56 pp w 2020 r.) **[M]** |
| Termin wykupu | dzień, w którym emitent zwraca nominał | 6 listopada 2026 r. |
| Wartość emisji | łączny nominał serii wprowadzonej do obrotu | 100 mln zł (seria 1/2023) **[Z]** |
| Wolumen, obrót | liczba i wartość obligacji, które zmieniły właściciela na sesji; dla większości serii korporacyjnych obroty są małe, płynność jest główną słabością rynku | — |

Cena obligacji na Catalyst nie zawiera odsetek narosłych: kupujący płaci kurs razy nominał plus odsetki od ostatniej wypłaty, dlatego notowania „w procentach" mało się zmieniają, a zysk inwestora to kupon. Dwie rzeczy, których w tabeli nie ma, a które decydują o ryzyku: zabezpieczenie (np. zastaw rejestrowy na akcjach Radmoru w emisjach WB, do 150 % wartości długu) i kowenanty (np. marża wyższa o 1,2 pp, jeżeli dźwignia przekroczy 0,75×; limity dywidendy), zapisane w warunkach emisji i w dokumencie informacyjnym **[M]**.

---

## 3. Czym jest Catalyst

| Element | Opis | Wiar. |
|---|---|---|
| Operatorzy | Giełda Papierów Wartościowych w Warszawie i BondSpot (spółka z grupy GPW) | [Z] |
| Platformy | cztery: rynek regulowany GPW i ASO GPW (obrót detaliczny, jednostka transakcyjna to jedna obligacja) oraz rynek regulowany BondSpot i ASO BondSpot (obrót hurtowy, dla instytucji); emitent wybiera, gdzie wprowadza serię, może na więcej niż jedną | [W] |
| Instrumenty | obligacje skarbowe, korporacyjne (w tym banków), komunalne, spółdzielcze, listy zastawne; w euro i złotych | [Z] |
| Skala (1 czerwca 2026 r.) | 876 serii w złotych, wartość emisji ponad 1,73 bln zł łącznie ze skarbowymi; papiery nieskarbowe ok. 161 mld zł, w tym korporacyjne i listy zastawne ok. 75 mld zł, komunalne ok. 53 mld zł; inne zestawienia z 2026 r. podają ok. 95–106 mld zł obligacji korporacyjnych w zależności od definicji | [M] |
| Emisje 2025–2026 | rekordowe: wartość nowych publicznych emisji korporacyjnych w latach 2025–2026 ok. 8,65 mld zł, z nadsubskrypcjami; kompresja marż czwarty rok z rzędu (spadek o 1,5–3,0 pp) | [M] |
| Autoryzacja | osobny status dla serii nienotowanych: emitent przyjmuje obowiązki informacyjne Catalyst i rejestruje emisję; wymaga emisji o wartości co najmniej równowartości 400 tys. EUR; nie jest warunkiem wprowadzenia do obrotu | [M] |
| Reforma | GPW ogłosi kierunki i harmonogram rewitalizacji Catalyst w listopadzie 2026 r. (Catalyst Forum), zmiany od początku 2027 r.: krótsza i prostsza droga od decyzji o finansowaniu do pierwszego notowania, wsparcie płynności i dużych emisji detalicznych; animator działa dziś przy ok. 76 % serii na rynku regulowanym | [M] |
| Popyt detaliczny od 2027 r. | ustawa z 3 lipca 2026 r. o Osobistych Kontach Inwestycyjnych: od 1 stycznia 2027 r. zamiast podatku od zysków kapitałowych podatek od wartości aktywów, ze zwolnieniem do 100 tys. zł dla akcji, funduszy i obligacji korporacyjnych oraz do 25 tys. zł dla lokat i obligacji oszczędnościowych | [M] |

Dlaczego to ważne dla firmy obronnej: WB Electronics jest jedynym emitentem z sektora zbrojeniowego na Catalyst (Portal Analiz: „nietypowa branża, dywersyfikacja sektorowa") **[M]**; dług obronny w Polsce to poza tym kredyty bankowe, gwarancje BGK i zaliczki zamawiającego, a nie rynek publiczny.

---

## 4. Jak wygląda emisja obligacji i wprowadzenie do obrotu

### 4.1 Podstawa prawna i kto może emitować

- **Ustawa z 15 stycznia 2015 r. o obligacjach**: emitentem może być m.in. osoba prawna prowadząca działalność gospodarczą, więc także prosta spółka akcyjna **[W]**. Obligacje nie mogą mieć formy dokumentu; od 1 lipca 2019 r. każda emisja, także prywatna, wymaga rejestracji w KDPW za pośrednictwem agenta emisji (dom maklerski albo bank), który sprawdza zgodność emisji z prawem i pośredniczy w rejestracji **[M]/[W]**.
- **Obligacje zamienne** (art. 19 ustawy): spółka może je emitować, jeżeli statut (umowa) tak stanowi; gdy emitentem jest P.S.A., mogą być oferowane wyłącznie za pośrednictwem firmy inwestycyjnej, chyba że wyłącznie akcjonariuszom tej spółki; uchwała o emisji obligacji zamiennych i akcji wydawanych w zamian podlega zgłoszeniu do sądu rejestrowego, a w P.S.A. wpisowi podlega także maksymalna liczba akcji **[Z]/[W]**. Obligacje zamienne nie mogą być emitowane poniżej wartości nominalnej ani wydawane przed pełną wpłatą.
- **Oferta**: prywatna (bez oferty publicznej, do zamkniętego kręgu) albo publiczna; oferta publiczna powyżej progów z ustawy o ofercie publicznej wymaga prospektu zatwierdzonego przez KNF, mniejsze oferty memorandum albo dokumentu informacyjnego **[W]**. Większość emisji małych i średnich firm na Catalyst to oferty prywatne plasowane przez dom maklerski, a dopiero potem wprowadzane do ASO **[W]**.
- **Zabezpieczenie**: hipoteka, zastaw rejestrowy (WB: na akcjach spółki zależnej), poręczenie; przy zabezpieczeniu rzeczowym ustanawia się administratora zabezpieczeń, który działa na rzecz obligatariuszy **[W]**.

### 4.2 Wprowadzenie do ASO Catalyst

| Wymóg | Treść | Wiar. |
|---|---|---|
| Dokument informacyjny | sporządzony według załącznika do Regulaminu ASO; nie podlega zatwierdzeniu przez KNF, GPW ani BondSpot | [M] |
| Kapitał własny emitenta | co najmniej 2 mln zł (organizator może odstąpić w przypadku spółki celowej emitującej dług) | [M] |
| Zbywalność | obligacje muszą być zdematerializowane i nieograniczone w obrocie; wobec emitenta nie może toczyć się postępowanie upadłościowe ani likwidacyjne | [M] |
| Autoryzowany Doradca | dla dłużnych instrumentów finansowych w ASO nie jest wymagany (inaczej niż dla akcji na NewConnect) | [M]/[W] |
| Rynek regulowany | wymaga prospektu albo memorandum zatwierdzonego przez KNF; wartość nominalna serii co najmniej 4 mln zł | [M]/[W] |
| Obowiązki informacyjne po wprowadzeniu | raporty bieżące (zdarzenia wpływające na zdolność obsługi długu, zmiany warunków emisji, zgromadzenia obligatariuszy) i okresowe: roczne i półroczne w ASO, na rynku regulowanym także kwartalne (terminy: kwartalny do 60 dni, półroczny do 3 miesięcy, roczny do 4 miesięcy); kanał EBI (ASO) albo ESPI; do tego rozporządzenie MAR (informacje poufne, listy insiderów) | [M]/[W] |

### 4.3 Koszty

| Pozycja | Rząd wielkości | Wiar. |
|---|---|---|
| Agent emisji (obowiązkowy od 2019 r.) | 10–20 tys. zł na serię | [M] |
| Rejestracja w KDPW | 4–50 tys. zł na serię, plus opłaty za wykup według cennika | [M] |
| Opłata GPW za wprowadzenie do Catalyst | 6–50 tys. zł jednorazowo, zależnie od wartości nominalnej serii | [M] |
| Opłata roczna za notowanie | 3–12 tys. zł | [M] |
| Administrator zabezpieczeń | wynagrodzenie roczne przy emisjach zabezpieczonych | [M] |
| Dom maklerski (plasowanie, dokument informacyjny) | prowizja od uplasowanej kwoty, zwykle kilka procent przy małych emisjach | [W] |
| Doradca prawny, biegły rewident (sprawozdania do dokumentu informacyjnego) | kilkadziesiąt tysięcy złotych i więcej | [W] |
| **Razem dla emisji 10–20 mln zł** | **kilka procent wartości emisji w pierwszym roku** (szacunek); GPW udostępnia kalkulator kosztów | [?] |

### 4.4 Cena pieniądza: marże na Catalyst

| Emitent (przykład) | Warunki | Wiar. |
|---|---|---|
| WB Electronics, listopad 2014 (80 mln zł, 3 lata, na odkup Radmoru) | WIBOR plus 2 pp (Forsal) albo 3,7 pp (Obligacje.pl); źródła rozbieżne | [M] |
| WB Electronics, 2017 (80 mln zł) | WIBOR 3M plus 2,78 pp; cele finansowe i kowenanty dywidendowe w warunkach emisji | [M] |
| WB Electronics, 2020 (60 mln zł) | WIBOR 3M plus 2,56 pp; +1,2 pp przy dźwigni powyżej 0,75×; zastaw na akcjach Radmoru do 150 % długu | [M] |
| WB Electronics, 2023 (100 mln zł) | WIBOR 3M plus marża z book-buildingu; ten sam mechanizm podwyżki marży | [Z]/[M] |
| Kruk, 2026 (400 mln zł, 7 lat) | WIBOR 3M plus 3 pp; pierwsza w historii oferta 7-letnia | [M] |
| Victoria Dom, 2026 | WIBOR 6M plus 3,80–4,10 pp, wykup 2030 r. | [M] |
| Marvipol, 2026 | ponad 3 pp ponad WIBOR („mniejsza skala, słabsze postrzeganie") | [M] |
| Rynek, 2026 | marża za ryzyko najczęściej 3–5 pp; czwarty rok kompresji, łącznie o 1,5–3,0 pp | [M] |

Wniosek **[?]**: WB pożyczało taniej niż typowy mały emitent (2–3,7 pp), bo miało zabezpieczenie na spółce zależnej, kontrakty z MON i historię na rynku od 2014 r.; startup bez przychodów nie dostanie takich warunków, a najpewniej żadnych: rynek Catalyst wymaga EBITDA, zabezpieczeń i sprawozdań, których spółka na etapie B+R nie ma.

---

## 5. Co z tego wynika dla Basiliska

| Pytanie | Odpowiedź | Gdzie w dokumentach | Wiar. |
|---|---|---|---|
| Czy P.S.A. może wyemitować obligacje? | Tak; ustawa o obligacjach nie ogranicza emitentów do S.A. Obligacje zamienne: tylko przez firmę inwestycyjną albo tylko dla akcjonariuszy; umowa spółki powinna wprost dopuszczać ich emisję | § 25 ust. 1 lit. b (emisja instrumentów zamiennych: 75 %), § 31 ust. 4 (instrument z prawem konwersji, warrantem, prawem nominacji dyrektora, wetem albo zabezpieczeniem na IP: Sprawa Zastrzeżona); do rozważenia zdanie w § 31, że Spółka może emitować obligacje, w tym zamienne i z prawem pierwszeństwa **[W]** | [W]/[Z] |
| Kiedy obligacje mają sens? | Gdy są przepływy z kontraktów i majątek do zabezpieczenia: WB po 17 latach, przy 300 mln zł przychodów. Dla Basiliska realny moment to pierwszy wieloletni kontrakt z zamawiającym publicznym, gdy potrzebny jest kapitał obrotowy na produkcję przed płatnościami | § 31 ust. 1 (finansowanie eksportu, zaliczki), § 31 ust. 5 (Plan Finansowania) | [?] |
| Co do tego czasu zamiast obligacji? | Granty i pożyczki publiczne (EIC, Ścieżka SMART, BGK, PARP), venture debt przy rundzie VC (zwykle z warrantami, czyli Sprawa Zastrzeżona z § 31 ust. 4), zaliczki zamawiającego, faktoring należności od MON | `psa_todo.md` sekcja 6; `vc.md` sekcja 8 („Ograniczenia finansowania") | [W] |
| Jakie zgody w spółce? | Emisja w ramach budżetu i Planu Finansowania: Rada Dyrektorów (§ 23 ust. 1 lit. d); poza budżetem albo z zabezpieczeniem powyżej 500 tys. zł: WZ 75 % (§ 25 ust. 1 lit. k); zabezpieczenie na Kluczowej Własności Intelektualnej: zawsze WZ (§ 31 ust. 4); kowenanty dywidendowe wiążą przez § 34 ust. 3 | § 23, § 25, § 31, § 34 | [W] |
| Co z tajemnicą? | Obligacje notowane oznaczają raporty EBI/ESPI, sprawozdania roczne i półroczne oraz MAR; treść kontraktów wojskowych i klasyfikacja produktów nie muszą być ujawniane, ale wyniki, zadłużenie i zdarzenia istotne tak. To ten sam problem, który WB dostrzegło przy IPO („co z wojskowymi tajemnicami") | § 27 (poufność), `regulations.md` sekcja 4 (bramka G4) | [W] |
| Jaka cena? | Dla firmy z kontraktami MON i zabezpieczeniem: WIBOR plus 2–4 pp (WB, Kruk jako punkty odniesienia); dla małego emitenta bez historii: 4–6 pp albo brak popytu | sekcja 4.4 | [?] |
| Czy Catalyst zastępuje giełdę akcji? | Nie, ale ją poprzedza: WB zbudowało 9 lat historii raportowania przed rozmowami o IPO. Obligacje nie wymagają przekształcenia P.S.A. w S.A. (zakaz z art. 300³⁶ § 2 KSH dotyczy akcji, nie obligacji) **[W]**, więc to jedyna droga Basiliska na rynek publiczny bez zmiany formy prawnej | `case_studies/swarmer.md` sekcja 10, `case_studies/wb_electronics.md` sekcja 10 | [W] |

Trzy zadania do `psa_todo.md` po decyzji Założycieli **[?]**: (1) zdanie w § 31 dopuszczające emisję obligacji, w tym zamiennych i z prawem pierwszeństwa, ze wskazaniem organu (uchwała WZ jako Sprawa Zastrzeżona); (2) w Planie Finansowania z § 31 ust. 5 kategoria „dług publiczny" z limitem i listą dopuszczalnych zabezpieczeń (udziały w Przedsięwzięciach Produkcyjnych, wierzytelności z kontraktów; nigdy Kluczowa Własność Intelektualna); (3) w umowie akcjonariuszy zgoda inwestorów na przyszłe kowenanty dywidendowe i informacyjne wynikające z obligacji.

---

## 6. Źródła sprawdzone 30 września 2026 r.

- Catalyst, strona główna i notowania obligacji korporacyjnych — https://gpwcatalyst.pl/ ; https://gpwcatalyst.pl/notowania-obligacji-obligacje-korporacyjne ; o rynku — https://gpwcatalyst.pl/o-rynku ; kalkulator kosztów — https://gpwcatalyst.pl/jak-zaczac-emitowac-kalkulator ; Regulamin ASO (tekst z 22 listopada 2024 r.) — https://gpwcatalyst.pl/pub/CATALYST/files/regulacje_prawne/0_14_15_Regulamin_ASO_cz_ogolna_22_11_2024.pdf ; Załącznik nr 4 do Regulaminu ASO — https://gpwcatalyst.pl/pub/CATALYST/files/regulacje/4_4_Zalacznik_Nr_4_do_Regulaminu.pdf
- Przewodniki GPW: „Obligacje korporacyjne na Catalyst. Przewodnik dla potencjalnych emitentów" — https://gpwcatalyst.pl/pub/CATALYST/files/materialy_informacyjne_o_rynku/Catalyst_broszura_korporacyjne.pdf ; „Catalyst Bond Handbook" — https://gpwcatalyst.pl/pub/CATALYST/files/Catalyst-HANDBOOK.pdf ; przewodnik dla inwestorów — https://gpwcatalyst.pl/pub/CATALYST/files/materialy_informacyjne_o_rynku/Catalyst_przewodnik_inwestorzy.pdf
- Statystyki i reforma: Bankier „Rynek Catalyst puchnie w oczach" — https://www.bankier.pl/wiadomosc/Rynek-Catalyst-puchnie-w-oczach-Inwestorzy-pakuja-miliony-w-obligacje-9074594.html ; StockWatch „GPW rozwija Catalyst" — https://www.stockwatch.pl/wiadomosci/obligacje-korporacyjne-polska-boom-catalyst-emisje,obligacje,377078 ; Analizy.pl — https://www.analizy.pl/puls-rynku/39992/gpw-chce-odswiezyc-rynek-obligacji-catalyst-zmiany-maja-pojawic-sie-jesienia ; https://www.analizy.pl/puls-rynku/40232/gpw-szuka-nowego-napedu-dla-catalyst ; bank.pl (harmonogram w listopadzie 2026 r.) — https://bank.pl/w-listopadzie-26-gpw-przedstawi-harmonogram-rewitalizacji-rynku-obligacji-catalyst/ ; Bankier o reformie — https://www.bankier.pl/wiadomosc/GPW-we-wspolpracy-z-rynkiem-przygotowuje-reforme-rynku-Catalyst-9169045.html ; przegląd rynku DM BOŚ (kwiecień 2026) — https://bossa.pl/sites/b30/files/2026-04/document_gpw_editor/Catalyst_6_GPW_21_2026_DM_BO%C5%9A_PL.pdf
- Marże 2026: Parkiet „Korporacyjne marże rekordowo niskie" — https://www.parkiet.com/parkiet-plus/art44573541-korporacyjne-marze-rekordowo-niskie-inwestorzy-traca-cierpliwosc ; StockWatch „Obligacje 2026" — https://www.stockwatch.pl/wiadomosci/jakie-obligacje-warto-kupic-w-2026-roku-skarbowe-korporacyjne-czy-indeksowane-inflacja,obligacje,373285 ; Strefa Inwestorów (aktywne prospekty) — https://strefainwestorow.pl/obligacje/obligalcje-korporacyjne-aktywne-prospekty ; Obligacje.pl — https://obligacje.pl/
- Emisja i koszty: prawo.pl „Nowe zasady emisji obligacji korporacyjnych" — https://www.prawo.pl/biznes/nowe-zasady-emisji-obligacji-korporacyjnych,438172.html ; „Emisja prywatnych obligacji, nowe wymogi od 2019 r." — https://www.prawo.pl/biznes/emisja-prywatnych-obligacji-nowe-wymogi-od-2019-roku,350282.html ; Deloitte (1 lipca 2019) — https://www2.deloitte.com/pl/pl/pages/financial-services/articles/newsletter/newsletter-legal-maj2019/nowe-wymagania-dla-emisji-obligacji-od-1-lipca-2019.html ; StockWatch „Emisja obligacji korporacyjnych: koszty, proces, ryzyka" — https://www.stockwatch.pl/wiadomosci/kiedy-obligacje-korporacyjne-sa-lepsze-niz-kredyt-bankowy-ekspertka-noble-securities-tlumaczy,obligacje,373073 ; Best Capital „Rynek regulowany i ASO Catalyst" — https://bestcapital.pl/rynek-regulowany-i-aso-catalyst/ ; Obligacje.pl „Obowiązki informacyjne emitentów obligacji w nowym kształcie" — https://obligacje.pl/pl/a/obowiazki-informacyjne-emitentow-obligacji-w-nowym-ksztalcie-q-a ; KNF, poradnik dla emitentów — https://www.knf.gov.pl/knf/pl/komponenty/img/Jak%20prawidlowo_do%20NETU_38960.pdf
- Ustawa o obligacjach: art. 19 (obligacje zamienne, w tym zasady dla P.S.A.) — https://arslege.pl/obligacje-zamienne/k1335/a82773/ ; https://lexlege.pl/o-obligacjach/art-19/ ; rozdział 2 (rodzaje obligacji) — https://lexlege.pl/o-obligacjach/rozdzial-2-rodzaje-obligacji/9113/ ; tekst jednolity (Dz.U. 2024 poz. 708) — https://www.inforlex.pl/wersje-fragmentu/tresc,DZU.2024.129.0000708,-1,USTAWA-z-dnia-15-stycznia-2015-r-o-obligacjach.html
- OKI: StockWatch — https://www.stockwatch.pl/wiadomosci/osobiste-konto-inwestycyjne-oki-ustawa-2027,akcje,371583 ; PAP — https://www.pap.pl/aktualnosci/osobiste-konta-inwestycyjne-co-zmieni-uchwalona-ustawa ; Gazeta Prawna (podpis Prezydenta) — https://www.gazetaprawna.pl/biznes/finanse-i-gospodarka/artykuly/11289697,oki-od-2027-roku-prezydent-podpisal-ustawe-podatek-belki.html
- WB Electronics na Catalyst: debiut 4 maja 2015 r. — https://www.wbgroup.pl/aktualnosci/wb-electronics-debiutuje-na-catalyst-rynku-obligacji-gpw/ ; Forsal (emisja 80 mln zł) — https://forsal.pl/artykuly/858947,wb-electronics-wchodzi-na-gielde-wprowadzi-na-rynek-catalyst-obligacje-warte-80-mln-zl.html ; Defence24 (2015, decyzja o GPW) — https://defence24.pl/sily-zbrojne/debiut-wb-electronics-rynku-catalyst-decyzja-o-wejsciu-na-gpw-pod-koniec-roku ; money.pl (2015) — https://www.money.pl/gielda/wiadomosci/artykul/wb-electronics-na-gpw-decyzja-do-konca-roku,210,0,1784018.html ; Portal Analiz — https://portalanaliz.pl/obligacje/wb-electronics-drony-w-ukrainie-obligacje-na-catalyst/ ; StockWatch (emitent WBE) — https://www.stockwatch.pl/obligacje/emitent-prywatny/wbe ; pozostałe źródła o obligacjach WB w `case_studies/wb_electronics.md` sekcja 12
- Strony gpwcatalyst.pl, forbes.pl, inwestomat.eu, lexlege.pl, forsal.pl i special-ops.pl były w tej sesji niedostępne do pełnego odczytu (blokada sieciowa); tezy oparte na streszczeniach z wyszukiwarki oznaczono [Z] tylko tam, gdzie streszczenie dokumentu było jednoznaczne.
