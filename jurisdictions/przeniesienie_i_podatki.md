# Przeniesienie struktury za granicę: polskie reguły podatkowe i korporacyjne

Dokument wewnętrzny Basilisk Systems, informacyjny. Nie jest opinią prawną ani podatkową i nie zmienia umowy spółki. Część katalogu `jurisdictions/` (przegląd: `README.md`; kryteria: `kryteria.md`). Opisuje, co dzieje się po stronie polskiej, gdy założyciele mieszkający w Polsce (1) zakładają spółkę-matkę za granicą od pierwszego dnia, (2) przenoszą istniejącą P.S.A. pod zagraniczną matkę („flip") albo (3) przekształcają P.S.A. transgranicznie w spółkę innego państwa UE. Odesłania do umowy według `psa.tex` w wersji 0.9.4-C; odpowiada na pytanie U.5 z `law_uzup.md` (koszty i ryzyka późniejszego przekształcenia, wpływ struktury holdingowej na Kryterium i programy, miejsce IP).

Stan na 30 września 2026 r. Oznaczenia wiarygodności: **[Z]** — akt prawny, portal urzędowy albo publikacja kancelarii lub doradcy podatkowego; **[M]** — prasa albo portal informacyjny; **[W]** — wiedza ogólna, do potwierdzenia u kancelarii; **[?]** — szacunek albo teza niepotwierdzona. Uwaga metodyczna: teksty ustaw były w tej sesji niedostępne do pełnego odczytu; numery artykułów podane według streszczeń kancelarii i portali; przed decyzją sprawdzić w akcie.

---

## 1. Główny wniosek

1. **Matka w UE albo EOG jest osiągalna bez podatku, matka w USA nie.** Wymiana udziałów (art. 24 ust. 8a–8c PIT) jest neutralna dla założycieli tylko wtedy, gdy spółka nabywająca podlega opodatkowaniu w UE/EOG (załącznik nr 3 do ustawy PIT), uzyskuje bezwzględną większość głosów, jest to pierwsza wymiana (art. 24 ust. 8b pkt 3, od 2022 r.) i zachowana jest ciągłość wartości **[Z]**. Flip do Delaware jest opodatkowany 19 % od wartości otrzymanych akcji (art. 17 ust. 1 pkt 9 PIT), czyli podatkiem gotówkowym od papierowego zysku **[Z]/[M]**.
2. **Matka „na papierze" jest polskim rezydentem.** Art. 3 ust. 1a CIT (od 2022 r.): spółka zagraniczna, której bieżące sprawy są prowadzone w sposób zorganizowany i ciągły z Polski, ma zarząd w Polsce i podlega tu CIT od całości dochodów **[Z]**. Estońska OÜ albo holenderska BV zarządzana z Warszawy nie daje nic poza kosztami.
3. **CFC bije w założycieli, chyba że spółka w UE ma realną działalność.** Polski rezydent z co najmniej 50 % udziału w zagranicznej jednostce kontrolowanej płaci 19 % od jej dochodu (art. 30f PIT), z wyjątkiem dla spółek z UE/EOG prowadzących „istotną rzeczywistą działalność gospodarczą" (ust. 18); spółka z Delaware z tego wyjątku nie korzysta **[Z]**.
4. **Exit tax dotyczy głównie założyciela, który się wyprowadza, i spółki, która się przekształca.** 3 % albo 19 %, dla osób fizycznych próg 4 mln zł i test rezydencji 5 z 10 lat; termin zapłaty dla osób fizycznych odroczony rozporządzeniem z 22 września 2025 r. do 31 grudnia 2027 r.; pytania prejudycjalne WSA Warszawa do TSUE z 29 maja 2025 r. **[Z]**. Przekształcenie transgraniczne P.S.A. uruchamia exit tax na poziomie spółki (art. 24f ust. 2 pkt 2 CIT) od aktywów opuszczających polską jurysdykcję, w tym IP **[Z]/[M]**.
5. **Każda matka będąca osobą prawną kończy estoński CIT** w polskiej spółce (warunek akcjonariuszy-osób fizycznych), i to wstecznie od końca poprzedniego roku według art. 28l ust. 1 pkt 4 lit. a CIT **[Z]/[?]**; wyjść z reżimu przed zamknięciem transakcji.
6. **Programy:** matka w UE/EOG zachowuje EDF, SAFE, EIC, DIANA i NIF; matka w USA zachowuje DIANA, traci EDF i SAFE (kontrola z państwa trzeciego), a PFR ogranicza ją do koszyka zagranicznego 20–40 % z warunkiem co najmniej 20 % w rękach polskich założycieli; SMART wymaga polskiej spółki albo oddziału **[Z]**. Szczegóły w `kryteria.md` sekcja 3.

---

## 2. Trzy scenariusze

| Zagadnienie | (i) Matka za granicą od pierwszego dnia (OÜ, BV albo Delaware Inc. nad polską spółką zależną) | (ii) Flip istniejącej P.S.A. pod zagraniczną matkę | (iii) Przekształcenie transgraniczne P.S.A. w OÜ albo BV (art. 580¹ i n. KSH) |
|---|---|---|---|
| PIT założycieli przy strukturze | brak przy objęciu za gotówkę; wniesienie istniejącego IP do spółki zagranicznej = przychód 19 % od wartości wkładu (art. 17 ust. 1 pkt 9 PIT) | matka z UE/EOG: neutralne, jeżeli większość głosów, pierwsza wymiana, ciągłość wartości, brak celu unikania (art. 24 ust. 19–20); matka z Delaware: 19 % od wartości otrzymanych akcji | bez zdarzenia na poziomie założycieli (ciągłość osobowości prawnej) |
| Exit tax spółki (art. 24f CIT) | brak (żadna polska spółka się nie przenosi); późniejsze przeniesienie IP ze spółki zależnej do matki to transfer aktywów (exit tax albo ceny transferowe) | brak przy samej wymianie; powstaje przy późniejszej migracji IP do matki | powstaje „co do zasady" przy zmianie rezydencji (art. 24f ust. 2 pkt 2), chyba że aktywa zostają przypisane do polskiego zakładu |
| Exit tax założyciela (art. 30da PIT) | tylko przy zmianie rezydencji założyciela (5 z 10 lat w Polsce; próg 4 mln zł; 3 %/19 %); zapłata odroczona do 31 grudnia 2027 r. | jak obok | jak obok |
| Rezydencja podatkowa matki (art. 3 ust. 1–1a CIT) | jeżeli zarządzana na co dzień z Polski: polski rezydent CIT; polski zespół to zakład | jak obok | spółka przekształcona zarządzana z Polski wraca do polskiego CIT, co przekreśla sens operacji |
| CFC (art. 30f PIT) | OÜ i BV: wyjątek przy istotnej rzeczywistej działalności w UE/EOG; Delaware: bez wyjątku, test kategorii z 2022 r. (aktywa pasywne 50 %, wysoka rentowność) | jak obok | jak obok |
| Estoński CIT | polska spółka zależna osoby prawnej nigdy nie jest uprawniona | utracony z wejściem matki, ze skutkiem od końca poprzedniego roku | ustaje z rezydencją |
| Ulgi polskie (B+R 200 %, IP Box 5 %, ekspansja, PSI, SMART) | dostępne dla polskiej spółki zależnej; SMART wymaga siedziby albo oddziału w Polsce | zachowane w polskiej spółce | utracone, chyba że zostaje polski zakład, oddział albo nowa spółka zależna |
| Podatek u źródła z polskiej spółki | matka z UE/EOG: zwolnienie z art. 22 ust. 4 CIT (10 % przez 2 lata) z „pay and refund" powyżej 2 mln zł i testem beneficjenta rzeczywistego; matka z USA: tylko traktat | jak obok | nie dotyczy bez polskiego płatnika |
| Program motywacyjny (art. 24 ust. 11–12b PIT) | odroczenie, gdy program tworzy spółka akcyjna z siedzibą w UE/EOG albo państwie z umową (Delaware Inc. tak; OÜ i BV sporne, bo to spółki z o.o.) | jak obok; program na poziomie P.S.A. objęty wprost ust. 12b | program spółki przekształconej: sporna forma |
| Procedura | brak | wycena i analiza podatkowa dla polskich akcjonariuszy (przy Delaware) | plan przekształcenia, biegły, uchwała 3/4 (umowa może zaostrzyć do 90 %), opinia Szefa KAS (art. 119zzl Ordynacji podatkowej, do 1 miesiąca), zaświadczenie sądu rejestrowego (3 miesiące, przedłużalne o 3) |
| Programy | Delaware: traci EDF i SAFE, PFR tylko koszyk zagraniczny, SMART tylko przez polską spółkę, DIANA zachowana; OÜ i BV: wszystko zachowane | jak (i) po flipie; fundusze zasilane z PFR na cap table komplikują flip do Delaware | tylko kierunki UE/EOG; instrumenty tylko dla polskiej siedziby utracone |

---

## 3. Instrumenty po kolei

### 3.1 Wymiana udziałów (art. 24 ust. 8a–8c PIT; art. 12 ust. 4d CIT)

- Neutralność wymaga, aby spółka nabywająca uzyskała (albo zwiększyła) bezwzględną większość głosów w spółce nabywanej w zamian za własne udziały, z dopłatą gotówkową do 10 % wartości nominalnej; transakcję można rozłożyć na kilka nabyć w 6 miesięcy od pierwszego **[Z]/[M]**.
- Obie spółki muszą podlegać opodatkowaniu od całości dochodów w państwie UE albo EOG (załącznik nr 3 do ustawy PIT) **[Z]**.
- Od 2022 r. (Polski Ład) udziały wnoszone przez wspólnika nie mogły zostać nabyte we wcześniejszej wymianie ani przydzielone przy łączeniu lub podziale (art. 24 ust. 8b pkt 3): neutralna jest tylko pierwsza wymiana; przekształcenie spółki albo jednoosobowej działalności nie „zużywa" tej możliwości **[Z]**.
- Interpretacja DKIS z 23 czerwca 2025 r. (0114-KDIP2-2.4010.168.2025.2.IN) dotyczyła równej wartości udziałów przy wymianie **[Z]**.
- Flip do Delaware: spółka amerykańska nie spełnia warunku UE/EOG, więc objęcie akcji za wkład niepieniężny (akcje P.S.A.) jest przychodem 19 %; kancelarie zalecają wycenę i analizę skutków przed transakcją; CK Legal opisuje osobny problem funduszy zasilanych ze środków publicznych (PFR, NCBR) na cap table **[M]/[Z]**.
- Przykłady polskie: ElevenLabs formalnie z siedzibą w Londynie i Nowym Jorku; Nomagic nadal jako polska sp. z o.o. (KRS 675685) po rundzie B 44 mln USD; brak matki w Delaware u Vue Storefront w dostępnych źródłach **[M]**.

### 3.2 Exit tax (art. 30da–30dh PIT; art. 24f–24l CIT)

- Od 1 stycznia 2019 r.; przeniesienie składnika majątku poza Polskę albo zmiana rezydencji, gdy Polska traci prawo do opodatkowania zysku; 19 % przy ustalonej wartości podatkowej, 3 % w pozostałych przypadkach; osoby fizyczne tylko powyżej 4 mln zł łącznej wartości rynkowej i przy rezydencji co najmniej 5 z 10 lat **[Z]/[M]**.
- Rozporządzenie Ministra Finansów i Gospodarki z 22 września 2025 r.: termin zapłaty dla osób fizycznych przedłużony po raz trzeci, do 7. dnia miesiąca po zbyciu składnika, jeżeli zbycie przed 1 grudnia 2027 r., w pozostałych przypadkach do 31 grudnia 2027 r. **[Z]**.
- WSA Warszawa 29 maja 2025 r. skierował do TSUE trzy pytania o zgodność podatku od osób fizycznych z prawem UE (moment obowiązku, opodatkowanie przyrostu sprzed rezydencji, pominięcie strat) **[Z]**. Sądy administracyjne (WSA Bydgoszcz I SA/Bd 375/20 i późniejsze orzeczenia NSA) ograniczały exit tax osób fizycznych do majątku związanego z działalnością **[M]/[?]**.
- Na poziomie spółki przekształcenie transgraniczne zmienia rezydencję i może uruchomić art. 24f ust. 2 pkt 2 CIT; art. 16g ust. 9–9a CIT zapewnia kontynuację wartości środków trwałych i wartości niematerialnych przy reorganizacjach transgranicznych **[Z]/[M]**.

### 3.3 CFC (art. 30f PIT; art. 24a CIT)

- 19 % od dochodu zagranicznej jednostki kontrolowanej; próg kontroli 50 % kapitału, głosów albo zysku **[Z]**.
- Wyjątek: jednostka opodatkowana od całości dochodów w UE/EOG, prowadząca tam istotną rzeczywistą działalność gospodarczą (struktura nieoderwana od przyczyn ekonomicznych, proporcja aktywności do lokalu, personelu i wyposażenia, samodzielne wykonywanie funkcji, zarząd na miejscu) **[Z]**.
- Polski Ład (2022) dodał kategorie: jednostki z co najmniej 50 % aktywów pasywnych (udziały, jednostki funduszy, nieruchomości) i jednostki o wysokiej rentowności względem aktywów; Polski Ład 3.0 doprecyzował liczenie **[Z]**. Zeznania CIT-CFC i PIT-CFC **[M]**.

### 3.4 Miejsce faktycznego zarządu (art. 3 ust. 1a CIT)

- Podatnik ma zarząd w Polsce, gdy jego bieżące sprawy są prowadzone w sposób zorganizowany i ciągły na terytorium Polski na podstawie umów, decyzji, orzeczeń albo powiązań; spółka zarejestrowana za granicą, a zarządzana z Polski, jest polskim rezydentem **[Z]**. Dla spółek nie stosuje się testu ośrodka interesów gospodarczych (ten jest dla osób fizycznych) **[M]**.
- Praktyczne minimum dla matki w Estonii albo Finlandii: dyrektor rezydent na miejscu, posiedzenia i decyzje tam, umowy i konto tam, a polski zespół jako spółka zależna z własnym zarządem; inaczej struktura kosztuje podwójnie **[?]**.

### 3.5 Przekształcenie transgraniczne (art. 580¹–580¹⁷ KSH, od 15 września 2023 r.)

- Polska spółka kapitałowa może przenieść siedzibę do innego państwa UE/EOG i przyjąć obcą formę z zachowaniem osobowości prawnej (implementacja dyrektywy 2019/2121); przepisy rozdziału o przekształceniach krajowych stosuje się odpowiednio **[Z]**. Rozdział dotyczy „spółek kapitałowych", więc obejmuje P.S.A., ale żadne źródło nie mówi tego wprost; Grant Thornton wymienia S.A., sp. z o.o. i S.K.A. **[?]**.
- Procedura: plan przekształcenia, badanie przez biegłego, uchwała większością 3/4 głosów przy obecności co najmniej połowy kapitału (umowa może wymagać do 90 %), wniosek zarządu do sądu rejestrowego, zaświadczenie o zgodności z prawem polskim w 3 miesiące (plus 3 w szczególnych przypadkach), wzmianka w rejestrze **[Z]**.
- Wraz z wnioskiem o zaświadczenie składa się wniosek o opinię Szefa KAS (dział IIIC Ordynacji podatkowej, art. 119zzl i n.), wydawaną bez zbędnej zwłoki, do miesiąca, co do podejrzenia unikania opodatkowania; podstawy odmowy w art. 119zzp **[Z]**.
- Kierunki tylko UE/EOG: przekształcenie w spółkę z Delaware jest niemożliwe **[Z]**. Basilisk: uchwała o przekształceniu jest Sprawą Zastrzeżoną z progiem 75 % wszystkich głosów (§ 25 ust. 1 lit. e), surowszym niż ustawowe 3/4 głosów oddanych.

### 3.6 Kontrola inwestycji zagranicznych

- Rozdział o inwestorach spoza UE/EOG/OECD z 2020 r. stał się bezterminowy od 24 lipca 2025 r. (Dz.U. 2025 poz. 973); organ: minister gospodarki; próg: nabycie znaczącego uczestnictwa (20 % głosów, kapitału albo zysku) albo dominacji w podmiocie chronionym z przychodami w Polsce ponad 10 mln EUR; sektory obejmują oprogramowanie strategiczne **[Z]/[M]**. Dla Basiliska istotne dopiero po przekroczeniu progu przychodów; wcześniej filtrem są koncesja i ŚBP.

### 3.7 Gdzie ma być IP

- Wniesienie IP przez założycieli do polskiej P.S.A.: przychód 19 % od wartości (art. 17 ust. 1 pkt 9 PIT), ale potem IP Box 5 % i ulga B+R w Polsce; § 26 umowy zakłada IP w Spółce.
- Późniejsze przeniesienie IP z polskiej spółki do matki: transfer aktywów z exit tax albo cenami transferowymi, kontrola eksportu (§ 28; udostępnienie technologii spoza UE jest eksportem) i utrata IP Box; memorandum T1 sygnalizuje te skutki **[Z]**.
- Wzorce: ICEYE trzyma projekt satelity w fińskiej matce i licencjonuje JV (60/40 z Rheinmetall); Swarmer trzyma IP najpewniej w Delaware, a kontrakty zawiera spółka estońska (`case_studies/`). Wniosek: IP powinno być w spółce, która składa wnioski o EDF, EIC i SMART, czyli w UE, i licencjonowane spółkom zależnym według § 33 ust. 3 **[?]**.

---

## 4. Zalecana kolejność

1. **Start jako P.S.A. w Polsce** z estońskim CIT (dopóki tylko osoby fizyczne), wkładem pracy zamiast wkładu IP tam, gdzie to możliwe (art. 17 ust. 1d), programem motywacyjnym z art. 24 ust. 12b i IP w Spółce (§ 26).
2. **Spółki zależne według rynku** (§ 33): USA dla Departamentu Wojny (ITAR, FOCI), UK dla MOD, Estonia jako wehikuł kontraktowy na NATO wschodniej flanki, Ukraina do produkcji i testów; matka zostaje w Polsce.
3. **Matka w UE/EOG tylko na żądanie inwestora prowadzącego rundę**, przed zamknięciem tej rundy i tylko przez pierwszą, większościową wymianę udziałów do spółki z realnym zarządem na miejscu (Estonia, Finlandia, Holandia); wyjście z estońskiego CIT przed transakcją; sprawdzenie, czy program motywacyjny matki spełni art. 24 ust. 12a.
4. **Flip do Delaware tylko wtedy, gdy plan finansowania porzuca programy UE** i gdy runda pokrywa 19 % PIT od wartości akcji założycieli; zawsze z polską spółką zależną dla SMART, koncesji i MON, i ze świadomością koszyków PFR.
5. **Przekształcenie transgraniczne jako ostatnia opcja**, gdy polska siedziba nie jest już potrzebna do żadnego instrumentu; koszt: exit tax od IP, opinia Szefa KAS, 4–7 miesięcy procedury.

W umowie akcjonariuszy (etap C, pkt 26 w `plan_prac.md`) warto zapisać: zobowiązanie do współdziałania przy wymianie udziałów do spółki z UE/EOG na żądanie inwestora rundy A, warunek neutralności podatkowej dla Założycieli, zakaz flipu poza UE/EOG bez zgody 75 % i bez pokrycia podatku, oraz zasadę, że IP i wnioski o programy UE pozostają w spółce z UE **[?]**.

---

## 5. Luki do sprawdzenia

- Brzmienie art. 24 ust. 19–20 PIT (klauzula przeciwko unikaniu przy wymianie udziałów) i art. 28l ust. 1 pkt 4 lit. a CIT (moment utraty estońskiego CIT).
- Czy P.S.A. jest objęta rozdziałem o przekształceniu transgranicznym (art. 4 § 1 pkt 2 KSH: definicja spółki kapitałowej).
- Koszty i realny czas flipu i przekształcenia (honoraria, wyceny).
- Stawki traktatu Polska–USA i skutki flipu po stronie amerykańskiej (sekcje 351 i 368 IRC).
- Katalog inwestorów objętych kontrolą inwestycji (spoza UE/EOG/OECD) i terminy postępowania (30 i 120 dni).
- Zwolnienie zysków ze zbycia udziałów w polskiej spółce holdingowej (art. 24o CIT).

---

## 6. Źródła sprawdzone 30 września 2026 r.

- Wymiana udziałów: interpretacja ogólna MF — https://ksiegowosc.infor.pl/wiadomosci/5251863,Wymiana-udzialow-lub-akcji-a-podatek-dochodowy-interpretacja-ogolna.html ; Polski Ład — https://rachunkowosc.com.pl/podatki-i-skladki-2022/wymiana-udzialow-i-jej-skutki-podatkowe-po-zmianach-wprowadzonych-przez-polski-lad ; https://www.prawo.pl/podatki/neutralnosc-podatkowa-wymiany-udzialow-w-polskim-ladzie,521501.html ; warunek UE/EOG — https://www.podatki.biz/artykuly/neutralna-podatkowo-wymiana-udzialow-miedzy-wspolnikami-polskiej-i-zagranicznej-spolki_49_42115.htm ; interpretacja z 23 czerwca 2025 r. — https://www.inforlex.pl/dok/tresc,FOB0000000000006989083,Neutralnosc-podatkowa-wymiany-udzialow-przy-rownowartosci-udzialow-i-akcji-w-kontekscie-podatku-dochodowego-od-osob-prawnych-Interpretacja-indywidualna-z-dnia-23-czerwca-2025-r-Dyrektor-Krajowej.html
- Flip do Delaware — https://mamstartup.pl/delaware-flip-kierunek-usa-jak-i-po-co-polskie-startupy-przenosza-sie-za-ocean/ ; https://www.clg-kuznicki.com/flip-do-usa-jak-przeniesc-strukture-startupu-do-delaware-krok-po-kroku/ ; https://ck-legal.pl/delaware-flip-z-udzialem-funduszy-finansowanych-ze-srodkow-publicznych/ ; https://cgolegal.pl/baza-wiedzy/spolki-zagraniczne-wsparcie-przedsiebiorcow-poza-granicami-rp/spolka-w-delaware/ ; przykłady — https://startup.pfr.pl/artykul/polskie-ai-kolejnym-krajowym-jednorozcem-co-robi-elevenlabs ; https://rejestr.io/krs/675685/nomagic
- Exit tax — https://www.deloitte.com/pl/pl/services/legal/perspectives/strefa-pracodawcy/exit-tax-podatek-od-wyjscia-w-polsce.html ; https://crido.pl/blog-taxes/ponowne-przedluzenie-terminu-platnosci-exit-tax/ ; https://studio.pwc.pl/aktualnosci/legislacja/termin-na-zaplate-exit-tax-wydluzony-po-raz-kolejny ; TSUE — https://www.ey.com/pl_pl/insights/tax/podatki-miedzynarodowe/exit-tax-pytanie-prejudycjalne-wsa-do-tsue ; https://pro.rp.pl/nawigator-prawny-poradnik/art44053801-wyjscie-przed-szereg-czyli-polski-exit-tax-w-swietle-standardow-unijnych-i-orzecznictwa-sadow-administracyjnych ; poziom spółki — https://rachunkowosc.com.pl/reorganizacje-spolek-wybrane-zmiany-w-ksh-i-przepisach-podatkowych ; https://www.taxpoint.pl/blog/reorganizacje-transgraniczne-i-krajowe-najwazniejsze-zmiany-w-prawie-handlowym-i-podatkowym
- CFC — https://przepisy.gofin.pl/przepisy,6,14,14,673,462970,20250807,art-24a-ustawa-z-dnia-15021992-r-o-podatku-dochodowym-od-osob.html ; https://arslege.pl/podatek-od-dochodow-zagranicznej-jednostki-kontrolowanej/k71/a80836/ ; wyjątek UE/EOG — https://tomczykowscy.pl/na-tropie-cfc-co-oznacza-prowadzenie-istotnej-rzeczywistej-dzialalnosci-gospodarczej/ ; Polski Ład — https://studio.pwc.pl/aktualnosci/alerty/zmiany-dotyczace-zagranicznych-jednostek-kontrolowanych-cfc-projekt-nowelizacji ; https://www.ey.com/pl_pl/insights/tax/podatki-miedzynarodowe/kiedy-nalezy-zaplacic-podatek-od-zagranicznej-jednostki-kontrolowanej
- Miejsce faktycznego zarządu — https://ksiegowosc.infor.pl/podatki/cit/cit/podatnicy-i-zakres-opodatkowania/5350695,Miejsce-faktycznego-zarzadu.html ; https://kancelaria-skarbiec.pl/polski-lad-wprowadza-definicje-miejsca-faktycznego-zarzadu/ ; https://polska-ksiegowosc.pl/2025/10/rezydencja-podatkowa-spolki-faktyczny-zarzad-za-granica-a-kraj-opodatkowania/
- Przekształcenie transgraniczne — https://przepisy.gofin.pl/przepisy,3,29,250,208,405361,20230915,art-5801-58017-transgraniczne-przeksztalcenie-spolek.html ; https://lexlege.pl/ksh/art-580-14/ ; https://grantthornton.pl/publikacja/przeksztalcenie-transgraniczne-na-czym-polega/ ; https://spolki.cgolegal.pl/baza-wiedzy/miedzynarodowe-doradztwo-podatkowe/transgraniczne-przeksztalcenie-spolki/ ; Clifford Chance — https://www.cliffordchance.com/content/dam/cliffordchance/briefings/2023/09/CB%20-%20pol%20nowelizacja%20ksh.pdf ; opinia Szefa KAS — https://arslege.pl/ordynacja-podatkowa/k38/s16330/ ; https://poradnikprzedsiebiorcy.pl/-opinia-szefa-kas-w-zakresie-przeciwdzialania-naduzyciom-transgranicznym
- Kontrola inwestycji — https://www.prawo.pl/biznes/nowe-przepisy-o-kontroli-inwestycji-zagranicznych-2025,533951.html ; https://dudkowiak.pl/blog/stala-kontrola-inwestycji-zagranicznych-w-polsce-jakie-sa-nowe-obowiazki-dla-inwestorow/ ; https://codozasady.pl/en/p/control-of-foreign-investments-upcoming-changes
- Estoński CIT i podatek u źródła: patrz `polska.md` sekcja 9.
