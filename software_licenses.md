# Licencje oprogramowania w robotyce — przewodnik dla Basilisk

Stan na 9 października 2026 r. Materiał roboczy dla Założycieli i dyrektora ds. zgodności; nie zastępuje porady prawnej. Dotyczy stosu oprogramowania pojazdów autonomicznych (łaziki, drony, jednostki pływające) budowanych jako produkt zamknięty (closed source), w tym w wariancie obronnym i podwójnego zastosowania.

Dokument łączy się z umową spółki: § 26 ust. 5 lit. c (oświadczenie Założyciela o ujawnieniu komponentów otwartego oprogramowania, ich licencji i obowiązków), § 26 ust. 6 (rejestr komponentów otwartego oprogramowania i zestawienie składników oprogramowania prowadzone przez Radę), § 28 ust. 2 (klasyfikacja przed udostępnieniem), § 33 ust. 3 (licencja dla Przedsięwzięcia Produkcyjnego), Załącznik nr 1 (wykaz licencji zewnętrznych przy wkładzie) i Załącznik nr 3 pkt 3 (wykaz otwartego oprogramowania i licencji o podwyższonym ryzyku). Patrz też `regulations.md` sekcja 2.2 (kontrola obrotu) i `plan_prac.md` T4 (dokumentacja wkładów).

**Oznaczenia pewności** (jak w `guide.md`):

- **[Z]** — sprawdzone w tekście źródłowym: plik LICENSE lub oficjalna strona projektu odczytana 9.10.2026 (adresy w sekcji 11), albo tekst ustawy z `src/legal/`;
- **[W]** — wiedza ogólna albo tylko wyniki wyszukiwania; oficjalna strona była niedostępna z naszego środowiska; sprawdzić przed oparciem decyzji;
- **[?]** — wniosek własny albo hipoteza; nie opierać na niej decyzji bez prawnika.

Nazwy licencji podajemy w identyfikatorach SPDX (MIT, BSD-3-Clause, Apache-2.0, LGPL-2.1, GPL-3.0, AGPL-3.0, MPL-2.0, EPL-2.0). Cytaty z licencji zostawiamy po angielsku, bo wiążąca jest wersja oryginalna.

---

## 1. Weryfikacja wcześniejszych ustaleń (YOLO, YOLOX, ROS 2, PyTorch)

Sprawdziliśmy odpowiedzi z wcześniejszej rozmowy. Wynik: ustalenia są trafne, z uzupełnieniami poniżej.

| Teza z rozmowy | Wynik weryfikacji | Uzupełnienie |
|---|---|---|
| „YOLO nie jest tylko do badań; zależy od implementacji” | **trafna** | Pełna tabela rodzin YOLO w sekcji 4.1. Oryginalny Darknet (YOLOv1–v4) jest w domenie publicznej **[Z]**; YOLOv5 (od 14.04.2023) i YOLOv8/11/26 Ultralytics — AGPL-3.0 **[Z]**; YOLOv7 i YOLOv9 — GPL-3.0 **[Z]**; YOLOv10 — AGPL-3.0 **[Z]**; YOLO-NAS — kod Apache-2.0, ale wagi na licencji niekomercyjnej **[Z]**. |
| „AGPL nie znaczy niekomercyjne; wymaga udostępnienia kodu przy dystrybucji i przy zmodyfikowanej usłudze sieciowej” | **trafna** | AGPL-3.0 § 13 dotyczy wyłącznie **zmodyfikowanej** wersji, z którą użytkownicy „interact … remotely through a computer network” **[Z]**. Niezmodyfikowany program za siecią nie uruchamia § 13; dystrybucja (conveying) uruchamia § 5–6 niezależnie od modyfikacji. |
| „Ultralytics publikuje szerszą interpretację, także dla użytku wewnętrznego, i kieruje robotykę wbudowaną do płatnej licencji Enterprise” | **trafna** | README Ultralytics: licencja Enterprise „enables seamless integration … including internal tools, automated workflows, and production deployments, bypassing the open-source requirements of AGPL-3.0” **[Z]**. Strona ultralytics.com/license była niedostępna; według wyników wyszukiwania wymienia „internal business tools or private company applications” jako wymagające Enterprise **[W]**. To stanowisko dostawcy, nie treść licencji — czysto wewnętrzne użycie bez dystrybucji i bez zdalnych użytkowników nie rodzi w tekście AGPL obowiązku ujawnienia kodu **[?]**. Spór z dostawcą jest jednak kosztem samym w sobie; patrz sekcja 9. |
| „Osobny kontener nie rozstrzyga, czy YOLO i autonomia to jeden program” | **trafna** | Stanowisko FSF (FAQ GPL): o tym, czy to jeden program, decyduje mechanizm komunikacji (ten sam plik wykonywalny albo wspólna przestrzeń adresowa — jeden program; potoki, gniazda, argumenty wiersza poleceń — zwykle osobne programy) **oraz** jej semantyka (wymiana „złożonych wewnętrznych struktur danych” może łączyć w jeden program) **[W]**. Kontener to tylko izolacja procesów; liczy się interfejs. |
| „YOLOX: kod Apache-2.0, ale w oficjalnym repozytorium jest nieodpowiedziane pytanie o licencję wag” | **trafna** | LICENSE Megvii: Apache-2.0 **[Z]**. Issue #1865 (31.03.2026, „licensing of official pretrained weights for commercial iOS app bundling”) — otwarte, 0 komentarzy; issue #1684 (26.06.2023, „Commercial use”) — otwarte, bez odpowiedzi opiekunów **[Z]**. W repozytorium nie ma osobnej licencji dla wag; domyślnie obejmuje je ten sam plik LICENSE **[?]**. |
| „ROS 2: rdzeń Apache-2.0, w tym rclcpp i rclpy; sprawdzać pakiet po pakiecie” | **trafna** | rclcpp, rclpy — Apache-2.0 **[Z]**. Przewodnik deweloperski ROS 2: każdy pakiet ma plik LICENSE, „typically the Apache 2.0 license … unless the package has an existing permissive license (e.g. rviz uses three-clause BSD)” **[Z]**. Wyjątki w ekosystemie: nav2_amcl — LGPL-2.1-or-later, nav2_mppi_controller — MIT, slam_toolbox — LGPL-2.1-only, ORB-SLAM3 i OpenVINS — GPL-3.0 (sekcja 4.4). ROS 1 (roscpp) — BSD **[Z]**. |
| „PyTorch: BSD-3-Clause; zachować noty, nie sugerować poparcia wymienionych organizacji” | **trafna** | Klauzula 3: „Neither the names of Facebook, Deepmind Technologies, NYU, NEC Laboratories America and IDIAP Research Institute nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.” **[Z]** |
| „Uruchomienie modelu Ultralytics przez PyTorch nie zdejmuje warunków AGPL/Enterprise” | **trafna** | Licencje warstw się sumują: framework (BSD) + kod modelu (AGPL) + wagi (licencja wag) + dane treningowe (warunki zbioru). Sekcja 2.4. |

Dwie rzeczy, których w rozmowie nie było, a które zmieniają obraz:

1. **Operator zdalny a AGPL § 13.** Jeśli zmodyfikowany detektor AGPL działa na dronie, a operator klienta w stacji naziemnej „wchodzi z nim w interakcję zdalnie przez sieć komputerową” (łącze radiowe IP, telemetria, strumień detekcji), § 13 może wymagać zaoferowania mu kodu źródłowego tej wersji — nawet bez sprzedaży drona. FSF przyjmuje, że „użytkownikiem” jest osoba korzystająca z programu, nie serwer po drugiej stronie **[W]**; czy operator pojazdu jest takim użytkownikiem, nie zostało rozstrzygnięte **[?]**. Ostrożnie: traktować operatora klienta jak użytkownika zdalnego.
2. **Klauzule „no military use” w licencjach modeli.** Coraz więcej modeli (Llama, DINOv3, pierwotny DeepSeek-V3) zakazuje zastosowań wojskowych w samej licencji. Dla Basiliska to kryterium wykluczające niezależne od pytania o copyleft. Sekcja 5.

---

## 2. Podstawy: co w licencji ma znaczenie dla pojazdu zamkniętego

### 2.1. Rodziny licencji

| Rodzina | Przykłady | Co wolno | Co trzeba | Dla produktu zamkniętego |
|---|---|---|---|---|
| **Permisywne** | MIT, BSD-2/3, Apache-2.0, ISC, BSL-1.0, zlib, Unlicense/domena publiczna | używać, modyfikować, sprzedawać, zamykać kod | zachować notę o prawach autorskich i tekst licencji; Apache-2.0 § 4: dołączyć kopię licencji, oznaczyć zmienione pliki, zachować noty, przekazać plik NOTICE **[Z]**; BSD-3 kl. 3: nie używać nazw autorów do promocji **[Z]** | bez ryzyka, o ile dokumentujemy noty (sekcja 7) |
| **Słaby copyleft (plikowy / biblioteczny)** | LGPL-2.1, LGPL-3.0, MPL-2.0, EPL-2.0, EDL-1.0 | łączyć z kodem zamkniętym | udostępnić kod **samej biblioteki** ze zmianami; LGPL: umożliwić użytkownikowi podmianę biblioteki i ponowne linkowanie (dynamiczne linkowanie albo dostarczenie plików obiektowych), zezwolić na inżynierię wsteczną do debugowania **[Z]**; LGPL-3.0 § 4 lit. e: „Installation Information” tylko gdy wymagałby jej GPL § 6 **[Z]**; MPL/EPL: zmienione pliki biblioteki na tej samej licencji | akceptowalne pod warunkiem architektury (linkowanie dynamiczne, brak zmian albo zmiany ujawnione) i procedury dostarczania źródeł |
| **Silny copyleft** | GPL-2.0, GPL-3.0 | używać wewnętrznie bez ograniczeń; sprzedawać | przy dystrybucji (conveying) udostępnić **pełny kod odpowiadający** (Corresponding Source) całego programu będącego dziełem pochodnym, na GPL; GPL-3.0 § 6: dla „User Product” także „Installation Information” (anty-tivoization) **[Z]** | produkt zamknięty wyklucza GPL w jednym programie z własnym kodem; dopuszczalny tylko jako osobny program (sekcja 2.3) albo z alternatywną licencją komercyjną |
| **Copyleft sieciowy** | AGPL-3.0 | jak GPL | jak GPL **plus** § 13: zmodyfikowana wersja musi oferować użytkownikom zdalnym kod źródłowy **[Z]** | jak GPL, a dodatkowo ryzyko przy zdalnej obsłudze i usługach w chmurze |
| **Podwójne (dual)** | Ultralytics (AGPL/Enterprise), Qt (LGPL/GPL/komercyjna), wolfSSL (GPL-3.0/komercyjna), UHD Ettus (GPL-3.0/alternatywna), ORB-SLAM3 i VINS-Fusion (GPL-3.0/kontakt z autorami), ChibiOS (GPL-3.0/komercyjna, HAL Apache-2.0), CoppeliaSim (Edu/Pro) | wybrać wariant | zapłacić za licencję komercyjną albo spełnić copyleft | wybór należy zapisać w rejestrze komponentów i w umowie z dostawcą |
| **EULA własnościowe SDK** | NVIDIA (CUDA, TensorRT, JetPack, DeepStream, Isaac ROS), ZED SDK, Spinnaker, Hailo DFC, RTI Connext, DJI SDK | to, co w umowie | zwykle: redystrybucja tylko wskazanych bibliotek, binarnie, w produkcie „with material additional functionality”, warunki przeniesione na klienta; klauzule eksportowe USA; klauzule „Critical Applications” | **największe ryzyko dla obronności**: klauzule wyłączające zastosowania wojskowe bez osobnej umowy (sekcja 4.2) |
| **Licencje modeli i wag** | Llama Community License, DINOv3 License, YOLO-NAS License, NVIDIA Open Model License, Stability Community License, OpenRAIL-M, PML-1.0 (Roboflow) | zależnie | ograniczenia użycia (AUP), progi przychodu/użytkowników, flow-down na użytkowników, prawo zdalnego ograniczenia | sprawdzać osobno od kodu; sekcje 4.1 i 5 |
| **Dane treningowe** | CC BY 4.0, CC BY-NC-SA, warunki ImageNet, DOTA | zależnie | atrybucja; NC = zakaz użycia komercyjnego; SA = ten sam warunek dla pochodnych | sekcja 4.9 |

### 2.2. Pojęcia, od których zależy wynik

- **Dystrybucja / conveying.** GPL/AGPL działają przy przekazaniu kopii osobie trzeciej. Sprzedaż pojazdu z oprogramowaniem, dzierżawa, użyczenie do pilotażu, przekazanie obrazu systemu partnerowi albo spółce celowej — każde jest dystrybucją. GPL-3.0 § 6 mówi wprost o transakcji, w której prawo posiadania i używania „is transferred to the recipient in perpetuity or for a fixed term (regardless of how the transaction is characterized)” **[Z]**. Czysty użytek wewnętrzny, demonstracja własnym pojazdem przez własny personel i udostępnienie podwykonawcy pracującemu na nasze zlecenie (według FSF) dystrybucją nie są **[W]**.
- **Kod odpowiadający (Corresponding Source).** Wszystko, co potrzebne do zbudowania i uruchomienia dzieła: kod, skrypty budowania, definicje interfejsów. Nie obejmuje kompilatora, jądra ani bibliotek systemowych, z których dzieło korzysta („System Libraries”) **[W]**.
- **Jeden program czy dwa.** FSF: ten sam plik wykonywalny albo wspólna przestrzeń adresowa — jeden program; potoki, gniazda, argumenty — zwykle osobne; linkowanie statyczne i dynamiczne biblioteki GPL — w ocenie FSF zawsze dzieło łączone **[W]**. Sądy nie rozstrzygnęły tego jednolicie; to pole sporu, nie pewnik **[?]**.
- **Tivoization (GPL-3.0 § 6).** „User Product” to produkt konsumencki („normally used for personal, family, or household purposes”) albo przeznaczony do zabudowy w mieszkaniu; „doubtful cases shall be resolved in favor of coverage”; produkt jest konsumencki, chyba że użycia niekonsumenckie „represent the only significant mode of use of the product” **[Z]**. Łazik, dron klasy przemysłowej albo wojskowej czy łódź autonomiczna sprzedawane wyłącznie podmiotom instytucjonalnym nie są User Product, więc nie musimy dostarczać kluczy do wgrania zmodyfikowanego firmware **[?]**. Ten sam dron sprzedawany hobbystom — jest. Granica przebiega po klasie produktu, nie po konkretnym kliencie.
- **AGPL § 13.** Dotyczy tylko wersji **zmodyfikowanej** i tylko „if your version supports such interaction” zdalnej **[Z]**. Modyfikacją jest też zmiana konfiguracji wbudowana w kod, własne głowice, fine-tuning w repozytorium kodu **[?]**; same wagi wytrenowane własnym zbiorem danych nie są modyfikacją programu, ale Ultralytics twierdzi inaczej **[W]**.
- **Licencja a prawo polskie.** Licencja open source jest umową licencyjną niewyłączną (art. 67 ust. 2 prawa autorskiego **[Z]**) — nie wymaga formy pisemnej (forma pisemna pod rygorem nieważności dotyczy tylko licencji wyłącznej, art. 67 ust. 5 **[Z]**). Dwa skutki praktyczne: (1) nie można wnieść aportem ani przenieść na Spółkę praw do cudzego kodu open source — można tylko wskazać, że Spółka korzysta z niego na licencji (art. 41 ust. 1 pkt 1 i art. 53 dotyczą tylko praw własnych) **[Z]**; (2) licencja „na czas nieoznaczony” w polskim prawie jest wypowiadalna (art. 68 ust. 1), a licencja na dłużej niż 5 lat staje się po tym czasie licencją na czas nieoznaczony (art. 68 ust. 2) **[Z]** — dla licencji OSS przyjmuje się, że klauzula „perpetual” i prawo właściwe wskazane w licencji wyłączają ten mechanizm, ale to pogląd doktryny, nie przepis **[?]**. Dla licencji, których udzielamy sami (§ 33 ust. 3), art. 66 i 68 trzeba wyłączyć wprost w umowie.

### 2.3. Izolacja komponentu copyleft — co działa, a co nie

| Technika | Ocena | Komentarz |
|---|---|---|
| Osobny proces, komunikacja przez ROS 2 topic/serwis (DDS) z prostą semantyką (obraz wejściowy, lista ramek wyjściowych) | **prawdopodobnie osobne programy** **[?]** | mieści się w kryterium FSF „pipes, sockets”; semantyka prosta (detekcje) przemawia za rozdzielnością; wciąż trzeba udostępnić kod samego węzła GPL/AGPL przy dystrybucji |
| Osobny kontener Docker, ale współdzielona pamięć (shared memory, zero-copy) z wymianą wewnętrznych struktur | **ryzyko jednego programu** **[?]** | FSF: pamięć współdzielona ze złożonymi strukturami „pretty much equivalent to dynamic linking” **[W]** |
| Wtyczka GPL ładowana dynamicznie do własnego procesu (np. plugin Nav2, filtr GStreamer) | **jeden program** **[W]** | FSF: dynamiczne linkowanie i wzajemne wywołania funkcji łączą w jeden program |
| Biblioteka LGPL linkowana dynamicznie, bez zmian | **dozwolone** **[Z]** | LGPL-2.1 § 6 lit. b / LGPL-3.0 § 4 lit. d pkt 1; dostarczyć kopię licencji i notę; przy zmianach — kod biblioteki |
| Biblioteka LGPL linkowana statycznie (typowe na mikrokontrolerach) | **dozwolone warunkowo** **[Z]** | trzeba dostarczyć pliki obiektowe własnej aplikacji, aby użytkownik mógł zlinkować ją ponownie ze zmienioną biblioteką (LGPL-2.1 § 6 lit. a) — w praktyce ujawnia strukturę binarną; unikać na firmware zamkniętym |
| Komputer towarzyszący z kodem zamkniętym obok autopilota GPL (ArduPilot) | **dozwolone** **[Z]** | tak opisuje to sama dokumentacja ArduPilot: „you can use a companion computer to run closed source code”; kod autopilota wraz ze zmianami udostępnić klientowi, poinformować go, że to open source |
| „Wywołanie przez CLI” programu GPL z własnego programu | **zwykle osobne programy** **[W]** | FAQ FSF; semantyka musi pozostać prosta |

Wniosek dla architektury: moduł GPL/AGPL może istnieć w pojeździe tylko jako **osobny proces z wąskim, udokumentowanym interfejsem**, z kodem źródłowym tego procesu gotowym do wydania klientowi i bez naszego kodu wrażliwego po tej samej stronie interfejsu. Jeżeli percepcja jest Kluczową Własnością Intelektualną, nie wolno jej budować na AGPL.

### 2.4. Warstwy: kod, wagi, dane, usługa

Każda warstwa ma własną licencję i wszystkie muszą pozwalać na nasze użycie:

1. **Framework** (PyTorch BSD-3, TensorFlow Apache-2.0, ONNX Runtime MIT) — bez ograniczeń.
2. **Kod modelu / architektura** (repozytorium detektora) — tu siedzi copyleft (Ultralytics AGPL) albo permisywność (YOLOX, RT-DETR, D-FINE Apache-2.0).
3. **Wagi pretrenowane** — osobna licencja albo brak (YOLOX), licencja niekomercyjna (YOLO-NAS, Depth Anything V2 Base/Large), licencja z zakazem wojskowym (DINOv3), licencja subskrypcyjna (RF-DETR Plus).
4. **Dane treningowe** — warunki zbioru przenoszą się, według części poglądów, na wagi (ImageNet, DOTA, KITTI, nuScenes: niekomercyjne) **[?]**. Nie ma orzecznictwa; praktyka branży traktuje wagi jako osobne dzieło, ale regulaminy zbiorów (ImageNet: „only for non-commercial research and educational purposes” **[W]**) są umową, którą pobierający podpisał.
5. **Usługa** (API modeli, chmura) — regulamin dostawcy (sekcja 5.2).

---

## 3. Scenariusze użycia i obowiązki

Legenda: **—** brak obowiązków poza wewnętrzną ewidencją; **N** — noty i tekst licencji w produkcie (permisywne, LGPL, MPL); **B** — kod biblioteki ze zmianami + możliwość ponownego linkowania (LGPL/MPL/EPL); **S** — pełny kod odpowiadający programu copyleft na tej samej licencji (GPL/AGPL); **S+** — jak S plus oferta kodu dla użytkowników zdalnych (AGPL § 13, tylko wersja zmodyfikowana); **E** — warunki EULA (lista redystrybuowalnych bibliotek, pass-through, eksport, Critical Applications); **AUP** — zakazy użycia z licencji modelu.

| # | Scenariusz | Permisywne | LGPL/MPL/EPL | GPL | AGPL | EULA SDK | Modele z AUP | Uwagi |
|---|---|---|---|---|---|---|---|---|
| S1 | B+R wewnętrzne, prototyp w laboratorium, pojazd nie opuszcza Spółki | — | — | — | — (bez użytkowników zdalnych spoza Spółki) | E (klauzule Critical Applications i eksportowe obowiązują od pierwszego dnia) | AUP obowiązuje od pierwszego dnia (zakaz wojskowy dotyczy też prac rozwojowych **[?]**) | Ultralytics twierdzi, że użycie wewnętrzne wymaga Enterprise **[W]**; tekst AGPL tego nie wymaga **[?]** |
| S2 | Demonstracja u klienta lub MON; pojazd i operator ze Spółki | — | — | — | — / S+ jeżeli przedstawiciel klienta obsługuje zdalnie zmodyfikowany program **[?]** | E | AUP | brak dystrybucji; dokument klasyfikacyjny z § 28 ust. 2 i tak potrzebny |
| S3 | Pilotaż, dzierżawa, użyczenie pojazdu klientowi (posiadanie bez własności) | N | N, B | S (GPL-3.0 § 6 obejmuje „for a fixed term”) **[Z]** | S, S+ | E | AUP | pierwsza prawdziwa dystrybucja; przygotować pakiet źródeł i pisemną ofertę (GPL-3.0 § 6 lit. b: 3 lata) |
| S4 | Sprzedaż pojazdu z wbudowanym oprogramowaniem (B2B, MON, partner NATO) | N | N, B | S; „Installation Information” tylko gdy User Product (sekcja 2.2) | S, S+ | E (pass-through na klienta, zakaz zastosowań Critical Applications bez umowy z NVIDIA) | AUP (Llama/DINOv3: zakaz wojskowy — produkt dla MON wyklucza) | **scenariusz bazowy Basiliska** |
| S5 | Sprzedaż / licencja samego stosu oprogramowania (SDK autonomii) | N | N, B | S | S, S+ | E | AUP | jak S4; dodatkowo własna EULA musi być zgodna z licencjami składników (nie można zakazać tego, na co pozwala GPL) |
| S6 | Usługa w chmurze Spółki: zarządzanie flotą, przetwarzanie nagrań, trening | — | — | — (GPL nie ma klauzuli sieciowej) | S+ jeżeli program zmodyfikowany | E (licencje serwerowe NVIDIA, zakaz „commercial hosting services” w części EULA **[W]**) | AUP | serwer w UE (regulations.md: chmura poza UE = eksport) |
| S7 | Zdalna obsługa pojazdu klienta przez jego operatora (stacja naziemna, VPN, łącze IP) | — | — | — | S+ **[?]** | E | AUP | ryzyko omówione w sekcji 1; traktować operatora jako użytkownika zdalnego |
| S8 | Licencja dla spółki celowej / konsorcjum (§ 33 ust. 3) | N | N, B | S | S, S+ | E (sublicencjonowanie zwykle zakazane — partner musi mieć własną licencję NVIDIA/ZED) | AUP (flow-down) | kontrola eksportu i koncesja (regulations.md 2.1 pkt b, 2.2); licencja niewyłączna ograniczona zakresem; wyłączyć art. 66 i 68 pr. aut. |
| S9 | Aport kodu Założyciela do Spółki (Załącznik nr 1) | wykaz w dokumentacji wkładu | wykaz | wykaz; **kod własny połączony z GPL w jeden program jest sam objęty GPL** — obniża wartość aportu **[?]** | jak GPL | SDK nie podlegają aportowi (licencja osobista, niezbywalna) | — | § 26 ust. 5 lit. c; wycena biegłego powinna wyłączyć komponenty obce |
| S10 | Projekt grantowy (EDF, NCBR, Horyzont Europa) | N | N, B | S | S, S+ | E | AUP | umowa grantowa może wymagać otwartego dostępu do wyników lub praw dostępu konsorcjantów — to osobne zobowiązanie nakładające się na OSS **[W]** |
| S11 | Dostawa do MON / zamówienie publiczne / system niejawny | N | N, B | S — kod dostarczamy zamawiającemu; GPL daje mu prawo dalszej redystrybucji, którego umową nie da się wyłączyć (sekcja 6.5) | jak GPL | E | AUP | klauzule przeniesienia praw w umowach publicznych nie mogą objąć kodu obcego — wymagają wyłączenia (carve-out) |
| S12 | Publikacja własnych komponentów / wkład upstream | wybór własnej licencji | — | zgodność licencji | — | zakaz publikacji części SDK | — | przed publikacją klasyfikacja eksportowa (§ 28 ust. 2; regulations.md 2.2: publikacja technologii kontrolowanej to udostępnienie); CLA/DCO upstream |
| S13 | Trening modeli na danych zewnętrznych | — | — | — | — | — | warunki zbioru (NC, SA, atrybucja) | sekcja 4.9; dziennik pochodzenia danych |

---

## 4. Katalog komponentów

Kolumna „Produkt zamknięty” odpowiada scenariuszowi S4 (sprzedaż pojazdu). Pewność dotyczy odczytu licencji, nie oceny prawnej.

### 4.1. Detektory obiektów i modele percepcji

| Komponent | Kod | Wagi | Pewność | Produkt zamknięty | Uwagi |
|---|---|---|---|---|---|
| Ultralytics (YOLOv8, YOLO11, YOLO26 — wydanie 8.4.0, 14.01.2026) | AGPL-3.0 | AGPL-3.0 (ten sam plik) | [Z] | **nie** bez licencji Enterprise | README: Enterprise dla „internal tools … production deployments”; YOLO27 zapowiedziany |
| Ultralytics YOLOv5 | AGPL-3.0 od 14.04.2023 (PR #11359); tagi ≤ v7.0: GPL-3.0 | jw. | [Z] | **nie** (GPL/AGPL) | stare tagi GPL nie są wyjściem — nadal silny copyleft |
| YOLOv7, YOLOv9 (WongKinYiu) | GPL-3.0 | GPL-3.0 | [Z] | **nie** jako część własnego programu | |
| YOLOv10 (THU-MIG) | AGPL-3.0 | AGPL-3.0 | [Z] | **nie** | zbudowany na kodzie Ultralytics |
| YOLO-NAS (Deci super-gradients) | Apache-2.0 | **„YOLO-NAS License”: zakaz użycia komercyjnego i produkcyjnego, zakaz dystrybucji i modyfikacji** | [Z] | **nie** z wagami oficjalnymi; tak przy treningu od zera | „you may not use the Software for any commercial use, including in connection with any models used in a production environment” |
| Darknet YOLOv1–v4 (pjreddie, AlexeyAB) | domena publiczna („YOLO LICENSE v2”) | jw. | [Z] | tak | „Darknet is public domain. Do whatever you want with it.”; wagi trenowane na COCO/ImageNet — sekcja 4.9 |
| **YOLOX (Megvii)** | Apache-2.0 | brak osobnej licencji; pytania #1684 i #1865 bez odpowiedzi | [Z] | **tak** (kod); wagi — zalecany trening własny albo własna ocena ryzyka | kandydat główny |
| PP-YOLOE (PaddleDetection) | Apache-2.0 | Apache-2.0 (repozytorium) | [Z] | tak | ekosystem Paddle (Baidu) — ocena łańcucha dostaw osobno **[?]** |
| RT-DETR (lyuwenyu) | Apache-2.0 | Apache-2.0 | [Z] | tak | |
| RF-DETR (Roboflow) | Apache-2.0 (pakiet `rfdetr` i wagi „Apache-designated”) | **wagi „Plus” (XL, 2XL, a także Atto/Femto/Pico oznaczone jako Plus) — PML-1.0**: wymaga aktywnego planu platformy Roboflow, śledzenia użycia, zakaz obchodzenia | [Z] | tak dla wariantów Apache; **nie** dla Plus bez subskrypcji | sprawdzić tabelę w README przy każdej wersji |
| D-FINE | Apache-2.0 | Apache-2.0 | [Z] | tak | |
| Detectron2, MMDetection | Apache-2.0 | zależnie od modelu | [Z] | tak (kod) | |
| SAM 2 (Meta) | Apache-2.0 | Apache-2.0 | [Z] | tak | |
| DINOv2 (Meta) | Apache-2.0 | Apache-2.0 | [Z] | tak | |
| **DINOv3 (Meta)** | „DINOv3 License” (19.08.2025) | jw. | [Z] | **nie** dla zastosowań wojskowych | pkt 1.b.v: zakaz użycia „for any activities subject to ITAR or end uses prohibited by Trade Controls, including those related to military or warfare purposes, nuclear industries or applications, espionage, or the development or use of guns or illegal weapons”; Meta może zmienić umowę w każdej chwili |
| Depth Anything V2 | Apache-2.0 | Small: Apache-2.0; Base/Large/Giant: **CC-BY-NC-4.0** | [Z] | tylko Small | |
| CLIP (OpenAI) | MIT | MIT | [Z] | tak | |
| supervision (Roboflow) | MIT | — | [Z] | tak | |

### 4.2. Frameworki ML, runtime wnioskowania, SDK sprzętowe

| Komponent | Licencja | Pewność | Produkt zamknięty | Uwagi |
|---|---|---|---|---|
| PyTorch | BSD-3-Clause | [Z] | tak | noty; klauzula o poparciu (sekcja 1) |
| TensorFlow, LiteRT (d. TFLite) | Apache-2.0 | [Z] | tak | |
| ONNX Runtime | MIT | [Z] | tak | |
| OpenVINO | Apache-2.0 | [Z] | tak | |
| TensorRT — część otwarta (parsery, wtyczki) | Apache-2.0 | [Z] | tak | |
| **TensorRT — biblioteki binarne** | NVIDIA SLA + TensorRT Supplement (odczytana kopia z 2021 r.) | [Z] kopia 2021 / [W] wersja bieżąca | tak, warunkowo | redystrybucja tylko `libnvinfer`, `libnvinfer_plugin`, binarnie, jako składnik własnego produktu „with material additional functionality”, na warunkach co najmniej tak samo restrykcyjnych dla klienta; dla Jetson — cały TensorRT; **§ 2.1(x) Critical Applications: użycie m.in. w „nuclear, avionics, navigation, military, medical…” wymaga osobnej umowy „Critical Applications agreement”**; klauzula eksportowa USA |
| **CUDA Toolkit** | NVIDIA EULA + CUDA Supplement (odczytana kopia z 2018 r.; bieżąca 13.x niedostępna) | [Z] kopia 2018 / [W] bieżąca | tak, warunkowo | redystrybucja bibliotek z Attachment A (runtime, cuBLAS, cuFFT…), bez modyfikacji; zakaz inżynierii wstecznej; zakaz użycia „in any manner that would cause it to become subject to an open source software license”; **Critical Applications: „Examples include use in nuclear, avionics, navigation, military, medical, life support…”**; prawo eksportowe USA |
| **JetPack / Jetson Linux (L4T)** | EULA NVIDIA (Jetson) + Tegra Software License Agreement | [W] | tak, warunkowo | Critical Applications wymienia „autonomous vehicle applications, automotive products, military”; redystrybucja ograniczona do binariów z systemem na licencji OSI; plik `Tegra_Software_License_Agreement-Tegra-Linux.txt` w pakiecie L4T — odczytać dla używanej wersji |
| DeepStream | SLA NVIDIA + DeepStream Supplement (kopia 2021) | [Z] kopia / [W] bieżąca | tak, warunkowo | redystrybucja plików `.so`; Graph Composer tylko do użytku wewnętrznego; zakaz publikacji benchmarków; Critical Applications; eksport USA |
| **Isaac ROS** | mieszane: `isaac_ros_common`, `isaac_ros_visual_slam` — „NVIDIA ISAAC ROS SOFTWARE LICENSE” (17.11.2021); `isaac_ros_nitros` — Apache-2.0 | [Z] | tak, warunkowo | tylko dla systemów z GPU NVIDIA; zakaz poddania OSS; **Critical Applications: „autonomous vehicle applications, … military”**; eksport USA; sprawdzać każde repozytorium osobno |
| Isaac Sim | kod Apache-2.0 (od 5.0, 2025), ale wymaga Omniverse Kit SDK i zasobów na „Isaac Sim Additional Software and Materials License” | [Z] kod / [W] dodatkowe | symulacja wewnętrzna: tak; redystrybucja / usługa: wymaga NVIDIA AI Enterprise **[W]** | |
| HailoRT | MIT (libhailort, pyhailort, CLI); wtyczka GStreamer `hailonet` LGPL-2.1-or-later | [Z] | tak | |
| Hailo Dataflow Compiler | EULA własnościowa (Developer Zone) | [W] | narzędzie wewnętrzne | odczytać LICENSE z paczki wheel |
| Google Coral libedgetpu | Apache-2.0 | [Z] | tak | kompilator Edge TPU — nie sprawdzono |
| Hugging Face transformers | Apache-2.0 | [Z] | tak | |
| llama.cpp | MIT | [Z] | tak | |
| Intel RealSense (librealsense) | Apache-2.0 | [Z] | tak | |
| Stereolabs ZED SDK | „Stereolabs Software and Services License Agreement” (15.11.2024); próbki MIT | [W] | warunkowo | klient końcowy musi być związany EULA „at least as protective of Stereolabs”; moduł własnych modeli — licencje tych modeli (np. Ultralytics) |
| Ouster SDK | BSD-3-Clause | [Z] | tak | |
| Velodyne (sterownik ROS) | BSD | [Z] | tak | |
| Livox SDK | MIT | [Z] | tak | producent chiński — ocena łańcucha dostaw i sankcji osobno **[?]** |
| Teledyne FLIR Spinnaker | EULA w instalatorze | [W] | warunkowo | produkt „may fall under ITAR or EAR controls” — klasyfikacja na żądanie; dane ITAR u nas ograniczają dostęp według obywatelstwa (regulations.md 3b) |
| DJI Mobile SDK / Payload SDK | EULA DJI (próbki MIT; PSDK częściowo MIT) | [Z] repozytoria / [W] EULA | **unikać** | zakaz zastosowań, w których awaria grozi śmiercią lub szkodą, bez pisemnej zgody DJI; nota eksportowa EAR; brak wyraźnego zakazu wojskowego w odczytanych fragmentach **[W]**; ryzyko sankcyjne i reputacyjne w obronności UE **[?]** |

### 4.3. Middleware robotyczne i komunikacja

| Komponent | Licencja | Pewność | Produkt zamknięty | Uwagi |
|---|---|---|---|---|
| ROS 2 (rclcpp, rclpy, rmw, ros2cli) | Apache-2.0 | [Z] | tak | pakiety spoza rdzenia sprawdzać w `package.xml` |
| ROS 1 (roscpp) | BSD | [Z] | tak | koniec wsparcia Noetic 2025 **[W]** |
| Fast DDS (eProsima) | Apache-2.0 | [Z] | tak | |
| Cyclone DDS | EPL-2.0 OR EDL-1.0 (BSD-3) | [Z] | tak (wybrać EDL) | |
| RTI Connext DDS | własnościowa; pakiety z apt ROS — niekomercyjne, „not eligible for production”; Connext Robotics Toolkit — darmowy dla prototypów przedkomercyjnych i badań | [W] | tylko z płatną licencją | |
| Zenoh, rmw_zenoh | Apache-2.0 OR EPL-2.0; rmw_zenoh Apache-2.0 | [Z] | tak | |
| micro-ROS (rclc, Micro-XRCE-DDS) | Apache-2.0 | [Z] | tak | |
| Mosquitto (MQTT) | EPL-2.0 OR EDL-1.0 | [Z] | tak | |
| ZeroMQ (libzmq) | MPL-2.0 od 4.3.5 (9.10.2023); wcześniej LGPL-3.0+ z wyjątkami | [Z] | tak | |
| Protobuf | BSD-3-Clause | [Z] | tak | |
| gRPC | Apache-2.0 | [Z] | tak | |
| MAVLink — nagłówki C (c_library_v2) | MIT na mocy wyjątku w COPYING generatora; **brak pliku LICENSE w repozytorium nagłówków** | [Z] | tak | generator (L)GPL-3.0; do rejestru wpisać podstawę (COPYING mavlink/mavlink) |
| pymavlink | LGPL-3.0-or-later; kod generowany MIT | [Z] | tak (B) | |
| MAVSDK | BSD-3-Clause | [Z] | tak | |
| MAVROS | potrójna: GPL-3.0 / LGPL-3.0 / BSD | [Z] | tak (wybrać BSD) | |
| OpenSSL 3.x | Apache-2.0 | [Z] | tak | |
| wolfSSL | GPL-3.0 (wybór GPL-2.0 tylko dla wymienionych programów) **lub komercyjna** | [Z] | tylko komercyjna | |
| Mbed TLS | Apache-2.0 OR GPL-2.0-or-later | [Z] | tak (Apache) | |
| libsodium | ISC | [Z] | tak | |
| WireGuard | moduł jądra GPL-2.0; wireguard-go MIT | [Z] | tak (jądro i tak GPL; sekcja 4.7) | |
| OpenVPN 2.x | GPL-2.0 z wyjątkiem dla OpenSSL | [Z] | jako osobny program | |
| Tailscale (klient) | BSD-3-Clause; nakładki GUI zamknięte; usługa na regulaminie Tailscale (AUP: zakaz prac nad bronią jądrową, chemiczną, biologiczną **[W]**) | [Z] kod / [W] regulamin | zależy od regulaminu usługi | serwery koordynacyjne poza UE — kontrola eksportu metadanych **[?]** |
| **GNU Radio** | GPL-3.0 | [Z] | **nie** w jednym programie z kodem zamkniętym | radio programowalne: pisać własne bloki jako osobne procesy albo nie używać w produkcie |
| SoapySDR | BSL-1.0 | [Z] | tak | |
| UHD (Ettus) | GPL-3.0 (licencja alternatywna przez Ettus) | [Z] | tylko jako osobny proces albo z licencją Ettus | |
| LoRaMac-node, LoRa Basics Modem | BSD-3-Clause; BSD-3-Clause-Clear | [Z] | tak | |

### 4.4. Autopiloty, nawigacja, SLAM, planowanie

| Komponent | Licencja | Pewność | Produkt zamknięty | Uwagi |
|---|---|---|---|---|
| **PX4** | BSD-3-Clause | [Z] | tak | NuttX Apache-2.0 [Z]; preferowany autopilot dla firmware zamkniętego |
| **ArduPilot** | GPL-3.0 | [Z] | tylko jako osobny program z udostępnionym kodem | wiki ArduPilot: „Inform your customers that the software is open source and provide the actual source code in the product”; anty-tivoization: właściciel musi móc wgrać zmodyfikowany firmware, gdy technicznie możliwe (ale tylko dla User Product, sekcja 2.2 **[?]**); kod zamknięty na komputerze towarzyszącym dozwolony [Z]; ChibiOS: jądro GPL-3.0 (lub licencja komercyjna), HAL Apache-2.0 [Z] |
| Betaflight, INAV | GPL-3.0 | [Z] | jak ArduPilot | |
| Paparazzi UAV | GPL-2.0(-or-later w nagłówkach) | [Z] | jak ArduPilot | |
| QGroundControl | Apache-2.0 (wymaga komercyjnej licencji Qt) OR GPL-3.0 | [Z] | zależy od Qt | |
| Mission Planner, MAVProxy | GPL-3.0 | [Z] | osobne narzędzie, nie część produktu | |
| Nav2 | w większości Apache-2.0; `nav2_amcl` LGPL-2.1-or-later; `nav2_mppi_controller` MIT; `nav2_costmap_2d`, `nav2_map_server`, `nav2_navfn_planner`, `nav2_util` Apache-2.0 + BSD-3; `nav2_voxel_grid` BSD-3 | [Z] | tak; AMCL jako osobny węzeł (B) | audyt `package.xml` na gałęzi main 9.10.2026 |
| MoveIt 2 | BSD-3-Clause | [Z] | tak | |
| OMPL | BSD-3-Clause | [Z] | tak | |
| Cartographer | Apache-2.0 | [Z] | tak | projekt nierozwijany **[W]** |
| slam_toolbox | LGPL-2.1-only | [Z] | tak jako osobny węzeł (B); zmiany ujawnić | |
| RTAB-Map | BSD-3-Clause | [Z] | tak | |
| **ORB-SLAM3** | GPL-3.0; wersja zamknięta komercyjna u autorów (Uniwersytet w Saragossie) | [Z] | tylko z licencją komercyjną | |
| **OpenVINS** | GPL-3.0 | [Z] | nie | |
| **VINS-Fusion** | GPL-3.0; kontakt komercyjny HKUST | [Z] | tylko z licencją komercyjną | |
| **FAST-LIO / FAST-LIO2** | GPL-2.0 | [Z] | nie | |
| LIO-SAM | BSD-3-Clause | [Z] | tak | |
| KISS-ICP | MIT | [Z] | tak | |
| Kimera-VIO | BSD-2-Clause | [Z] | tak | |
| stella_vslam | BSD-2-Clause | [Z] | tak | |
| GTSAM | BSD | [Z] | tak | |
| Ceres Solver | BSD-3-Clause | [Z] | tak | |
| g2o | rdzeń BSD; `csparse_extension` LGPL-2.1+; `g2o_viewer`, `g2o_incremental`, `slam2d_g2o` GPL-3.0+ | [Z] | tak z wyłączeniem części GPL | |

### 4.5. Widzenie komputerowe, matematyka, media

| Komponent | Licencja | Pewność | Produkt zamknięty | Uwagi |
|---|---|---|---|---|
| OpenCV ≥ 4.5 | Apache-2.0 (≤ 4.4: BSD-3) | [Z] | tak | `opencv_contrib` moduły non-free (SURF i in.) za flagą `OPENCV_ENABLE_NONFREE` — nie włączać w produkcie [Z] |
| PCL | BSD | [Z] | tak | |
| Open3D | MIT | [Z] | tak | |
| Eigen | MPL-2.0; pojedyncze pliki LGPL-2.1 — wyłączyć makrem `EIGEN_MPL2_ONLY` | [Z] | tak | |
| Boost | BSL-1.0 | [Z] | tak | |
| **FFmpeg** | LGPL-2.1-or-later domyślnie; `--enable-gpl` (libx264, libx265) → GPL-2.0-or-later; `--enable-nonfree` (FDK-AAC) → binarium nieredystrybuowalne | [Z] | tak tylko w konfiguracji LGPL, dynamicznie | kodowanie H.264/H.265 — patenty i opłaty (Via-LA, Access Advance) niezależnie od licencji oprogramowania **[W]** |
| GStreamer | LGPL-2.1 (wtyczki GPL tylko z `-Dgpl=enabled`) | [Z] | tak (B) | |
| x264, x265 | GPL-2.0 | [Z] | nie (albo licencja komercyjna) | |
| OpenH264 (Cisco) | BSD-2-Clause; binarium Cisco z pokryciem patentowym tylko gdy pobierane osobno przez użytkownika końcowego, z możliwością wyłączenia i notą | [Z] kod / [W] warunki binarium | ograniczone | |
| NumPy, SciPy, scikit-learn | BSD-3-Clause | [Z] | tak | |
| Pillow | MIT-CMU | [Z] | tak | |
| Kornia, Albumentations | Apache-2.0; MIT | [Z] | tak | |

### 4.6. Symulacja, GUI, stacja naziemna, mapy

| Komponent | Licencja | Pewność | Produkt zamknięty | Uwagi |
|---|---|---|---|---|
| Gazebo (gz-sim) | Apache-2.0 | [Z] | tak | |
| Webots | Apache-2.0 | [Z] | tak | |
| MuJoCo | Apache-2.0 | [Z] | tak | |
| AirSim (Microsoft) | MIT; repozytorium do archiwizacji; Project AirSim (IAMAI) MIT | [Z] | tak | |
| CARLA | MIT (kod), CC-BY (zasoby), Unreal Engine — EULA Epic | [Z] | symulacja wewnętrzna | |
| CoppeliaSim | własnościowa: Edu tylko dla szkół i uczelni, Pro komercyjna | [W] | tylko Pro | |
| **Qt** | LGPL-3.0-only / GPL-2.0 / GPL-3.0 / komercyjna | [Z] zestaw / [W] warunki Qt Company | tak na LGPL: linkowanie dynamiczne, użytkownik musi móc podmienić Qt i **uruchomić** przelinkowany program na urządzeniu (LGPL-3.0 — anty-tivoization), pełne źródła Qt albo pisemna oferta; dla urządzeń zamkniętych Qt Company oczekuje licencji komercyjnej **[W]** | stacja naziemna i HMI pojazdu — decyzja: LGPL z otwartym urządzeniem albo licencja komercyjna |
| RViz2, rqt | BSD | [Z] | tak | |
| PlotJuggler | MPL-2.0 | [Z] | tak | |
| **Foxglove** | Studio v1 (MPL-2.0) zarchiwizowane 18.07.2024; v2 — produkt własnościowy na regulaminie Foxglove; plan darmowy z limitami (5 urządzeń i in.) | [Z] archiwum / [W] regulamin | narzędzie wewnętrzne; nie wbudowywać | czy plan darmowy dopuszcza użycie komercyjne — nie potwierdzono |
| MapLibre GL JS / Native | BSD-3 / BSD-2 | [Z] | tak | |
| CesiumJS | Apache-2.0 | [Z] | tak (kod) | Cesium ion (usługa, zasoby 3D): plan Community tylko do użytku osobistego i niekomercyjnego **[W]** |
| QGIS | GPL-2.0 z wyjątkiem dla Qt | [Z] | narzędzie, nie składnik | |
| Dane OpenStreetMap | ODbL 1.0 | [W] | atrybucja; bazy pochodne na ODbL | |

### 4.7. System operacyjny, firmware, platforma

| Komponent | Licencja | Pewność | Produkt zamknięty | Uwagi |
|---|---|---|---|---|
| Jądro Linux | GPL-2.0 WITH Linux-syscall-note | [Z] | tak: programy użytkownika korzystające z wywołań systemowych nie są dziełem pochodnym [Z]; **własne moduły jądra / sterowniki — GPL** **[W]** | obowiązek: kod jądra ze zmianami i konfiguracją (`.config`) dla każdego dostarczonego obrazu |
| BusyBox | GPL-2.0-only | [Z] | tak, z kodem | historycznie najczęściej egzekwowana licencja w embedded **[W]** |
| glibc / musl | LGPL-2.1 / MIT | [Z] | tak | |
| U-Boot | GPL-2.0-or-later; „standalone” aplikacje nie są dziełem pochodnym | [Z] | tak, z kodem | |
| Yocto / OpenEmbedded | narzędzia; obraz = suma licencji | [Z] | tak | `create-spdx` (SBOM SPDX 3.0.1), `license.manifest`, `INCOMPATIBLE_LICENSE`, `archiver.bbclass` do pakietu źródeł — gotowa mechanika zgodności |
| FreeRTOS | MIT | [Z] | tak | |
| Zephyr | Apache-2.0 | [Z] | tak | |
| Apache NuttX | Apache-2.0 | [Z] | tak | |
| STM32Cube | HAL/BSP BSD-3; CMSIS Apache-2.0; middleware ST (USB, TouchGFX, STemWin) — **SLA0044**: tylko na układach ST, zakaz poddania OSS | [Z] | tak na układach ST | kod generowany przez CubeMX dziedziczy licencję z pliku LICENSE komponentu |
| ESP-IDF | Apache-2.0 | [Z] | tak | |
| Raspberry Pi firmware (VideoCore) | licencja Broadcom: tylko do użytku z urządzeniami Raspberry Pi | [Z] | tak na RPi | |
| OpenWrt | GPL-2.0 | [Z] | tak, z kodem | |
| Ubuntu | komponenty na własnych licencjach; polityka IP Canonical: zmodyfikowany obraz wymaga usunięcia znaków towarowych albo certyfikacji | [W] | tak | |
| Docker Engine / Desktop | Apache-2.0 / regulamin subskrypcji: Desktop darmowy tylko < 250 pracowników i < 10 mln USD przychodu; **podmioty rządowe tylko z płatną subskrypcją** | [Z] | Engine: tak | |

### 4.8. Modele fundamentalne, VLA, język, mowa

| Model | Licencja | Pewność | Użycie obronne | Uwagi |
|---|---|---|---|---|
| **Llama 3.x / 4 (Meta)** | Llama Community License + AUP | [Z] | **zakazane** | AUP: zakaz „Military, warfare, nuclear industries or applications, espionage, use for materials or activities that are subject to ITAR…”, „Guns and illegal weapons (including weapon development)”, a także „Operation of critical infrastructure, transportation technologies, or heavy machinery”; **Llama 4 multimodalne: prawa nie są udzielane firmom z siedzibą w UE** (poza użytkownikami końcowymi); wyjątki Meta dla rządu USA, Five Eyes, a od 09.2025 dla FR/DE/IT/JP/KR oraz instytucji NATO i UE — osobne porozumienia, Polska niewymieniona **[W]** |
| Gemma (Google) | Gemma Terms + Prohibited Use Policy | [W] | niejasne | klauzuli wojskowej nie znaleziono; regulamin zmieniany (2024, 2025) — odczytać bieżący |
| Qwen3 (Alibaba) | Apache-2.0 („All our open-weight models”) | [Z] | tak (licencja) | Qwen2.5-3B — licencja badawcza, Qwen2.5-72B — Qwen License **[W]**; pochodzenie chińskie — ocena łańcucha dostaw i akceptowalność u klienta obronnego **[?]** |
| DeepSeek-R1 | MIT (kod i wagi) | [Z] | tak (licencja) | jw. co do pochodzenia |
| DeepSeek-V3 (pierwotne wagi) | kod MIT; model: „DEEPSEEK LICENSE AGREEMENT 1.0” (2023): **„For military use in any way” zakazane**, prawo ChRL, sądy w Hangzhou | [Z] | **zakazane** | V3-0324 ponownie wydany na MIT **[W]** — zależy od checkpointu |
| Mistral | większość Apache-2.0 (Mistral 7B, Mixtral, Small 3, rodzina Mistral 3); część MRL (niekomercyjna), MNPL (nieprodukcyjna), zmodyfikowany MIT z progiem 20 mln USD przychodu | [W] | zależy od modelu | karta modelu jest wiążąca |
| NVIDIA Nemotron, Cosmos, GR00T | kod Apache-2.0 [Z]; wagi: NVIDIA Open Model License (komercyjne, atrybucja, wygaśnięcie przy obejściu zabezpieczeń) **[W]**; repozytorium Cosmos: OpenMDW-1.1 (permisywna) [Z] | mieszane | prawdopodobnie tak | README GR00T niespójne co do licencji wag — pytać NVIDIA |
| OpenVLA | MIT | [Z] | tak | |
| openpi (π0, π0.5; Physical Intelligence) | Apache-2.0 | [Z] | tak | |
| Whisper (OpenAI) | MIT | [Z] | tak | |
| Stability AI (Community License) | darmowa poniżej 1 mln USD rocznego przychodu; rejestracja przy użyciu komercyjnym; wygasa powyżej progu | [Z] | warunkowo | |
| Modele OpenRAIL-M (Stable Diffusion 1.x itp.) | ograniczenia użycia (m.in. zakaz generowania informacji dla wymiaru sprawiedliwości, organów ścigania, imigracji; porady medyczne), flow-down, prawo zdalnego ograniczenia | [Z] | brak klauzuli wojskowej, ale klauzula „organy ścigania” może dotyczyć klientów publicznych **[?]** | |

### 4.9. Zbiory danych i pochodzenie wag

| Zbiór | Warunki | Pewność | Użycie komercyjne | Uwagi |
|---|---|---|---|---|
| ImageNet | „only for non-commercial research and educational purposes”; pracodawca komercyjny badacza także związany | [W] | **nie** | większość wag „ImageNet-pretrained” (backbone’y) wywodzi się stąd — ryzyko dla całej branży, bez orzecznictwa **[?]** |
| COCO | adnotacje CC BY 4.0; obrazy — regulamin Flickr, konsorcjum nie ma praw do obrazów | [Z] | adnotacje tak; obrazy — każdy na własnej licencji | |
| Open Images V7 | adnotacje CC BY 4.0; obrazy „listed as” CC BY 2.0, bez gwarancji | [Z] | tak, z atrybucją i własną weryfikacją | |
| xView | oficjalny regulamin niedostępny; według Ultralytics CC-BY-NC-SA-4.0 | [W] | prawdopodobnie nie | zdjęcia satelitarne DigitalGlobe |
| DOTA | „academic purposes only, but any commercial use is prohibited”; obrazy Google Earth na warunkach Google | [Z] | **nie** | |
| VisDrone | brak licencji w oficjalnym repozytorium; kopie podają CC BY-NC-SA 3.0 | [Z] brak / [W] | nie bez zgody autorów | najpopularniejszy zbiór dronowy — pułapka |
| nuScenes | CC BY-NC-SA 4.0; licencja komercyjna przez Motional | [W] | tylko z licencją | devkit Apache-2.0 [Z] |
| KITTI | CC BY-NC-SA 3.0 | [W] | nie | |
| Waymo Open Dataset | „Waymo Dataset License Agreement for Non-Commercial Use” | [Z] (README) | nie | |
| SeaDronesSee (morski) | kod MIT, dane CC0 1.0 | [Z] | **tak** | dobry zbiór startowy dla jednostek nawodnych |
| Dane syntetyczne z symulatorów | licencja symulatora (Isaac Sim: Additional Materials License; CARLA: zasoby CC-BY) | [W] | sprawdzić | |

Praktyczna zasada: modele do produktu trenować na danych własnych, CC0/CC BY, zakupionych albo z pisemną licencją; dla każdego checkpointu w produkcie prowadzić dziennik pochodzenia (zbiór, wersja, licencja, data pobrania, kto zaakceptował regulamin). Backbone z ImageNet zastąpić wagami o jasnym pochodzeniu (np. trening własny, dane z licencją komercyjną) albo przyjąć ryzyko świadomą decyzją Rady wpisaną do rejestru **[?]**.

---

## 5. Klauzule zakazu zastosowań wojskowych i „etyczne”

Dla spółki obronnej to kryterium wykluczające, niezależne od copyleftu. Klauzule bywają w licencji modelu, w EULA SDK, w regulaminie usługi albo jako opcjonalny moduł licencji.

### 5.1. W licencjach komponentów

| Źródło | Klauzula | Pewność | Skutek dla Basiliska |
|---|---|---|---|
| Llama 3.x / 4 AUP | zakaz „Military, warfare, nuclear industries or applications, espionage, … ITAR”, broń, a także „critical infrastructure, transportation technologies, or heavy machinery” | [Z] | wykluczone w produkcie i w B+R pod produkt obronny; także pojazdy cywilne (klauzula „transportation technologies”) **[?]** |
| DINOv3 License (Meta) | zakaz użycia dla działań ITAR i końcowych zastosowań zakazanych przez kontrolę handlu, „including those related to military or warfare purposes … espionage, or the development or use of guns or illegal weapons” | [Z] | wykluczone w wariancie obronnym; w cywilnym — ryzyko jednostronnej zmiany umowy przez Meta |
| DeepSeek License 1.0 (pierwotne V3) | „For military use in any way” | [Z] | wykluczone |
| NVIDIA SLA (CUDA, TensorRT, DeepStream, JetPack, Isaac ROS) | „Critical Applications”: zakaz użycia w systemach, których awaria grozi śmiercią lub stratą katastrofalną, „including … nuclear, avionics, navigation, military, medical, life support”, „autonomous vehicle applications”, bez osobnej umowy z NVIDIA | [Z] kopie 2018–2021 / [W] bieżące | **każdy pojazd autonomiczny Basiliska** mieści się w tej definicji; potrzebna umowa z NVIDIA (Critical Applications agreement / umowa partnerska) albo rezygnacja z redystrybucji SDK NVIDIA — pytanie do kancelarii i do NVIDIA |
| Hippocratic License 3.0 | rdzeń bez klauzuli wojskowej; moduły opcjonalne: Mass Surveillance (3.1.19), **Military Activities (3.1.20)**, Law Enforcement (3.1.21) | [Z] | sprawdzać, które moduły włączono; moduł 3.1.20 wyklucza samą Spółkę jako licencjobiorcę |
| OpenRAIL-M | brak klauzuli wojskowej; zakazy dotyczące organów ścigania, imigracji, porad medycznych, zautomatyzowanych decyzji; flow-down na użytkowników | [Z] | ostrożnie przy klientach z sektora bezpieczeństwa wewnętrznego |
| DJI SDK | zakaz zastosowań, w których awaria grozi śmiercią lub szkodą, bez zgody DJI; nota eksportowa EAR | [W] | unikać |
| Tailscale AUP | zakaz prac nad bronią jądrową, chemiczną, biologiczną | [W] | nie dotyczy, ale usługa poza UE |

### 5.2. W regulaminach usług API

| Dostawca | Klauzula | Pewność |
|---|---|---|
| Anthropic (Usage Policy, wersja obowiązująca od 12.11.2026) | zakaz m.in. „Weaponize or integrate weapons onto drones, vehicles, or any unmanned or autonomous platforms, or develop weapons delivery systems”, oprogramowania do „targeting, fire control, or engagement”, śledzenia osób bez zgody; umowy rządowe mogą modyfikować ograniczenia | [Z] |
| OpenAI | od 01.2024 usunięto „military and warfare”; pozostaje zakaz rozwoju, nabywania i użycia broni | [W] |
| Google Gemini API | Generative AI Prohibited Use Policy; klauzuli wojskowej nie znaleziono | [W] |

Wniosek: modele i usługi z klauzulami z 5.1–5.2 nie mogą być składnikiem produktu ani narzędziem w pracach nad wariantem wojskowym (projektowanie, testy, generowanie danych). W pracach biurowych (dokumentacja, kod niezwiązany z funkcją bojową) — granica wymaga wewnętrznej polityki użycia narzędzi AI **[?]**.

---

## 6. Styk z innymi reżimami prawnymi

### 6.1. Kontrola obrotu (rozporządzenie 2021/821, ustawa o obrocie strategicznym)

- Oprogramowanie „w domenie publicznej” (udostępnione bez ograniczeń dalszego rozpowszechniania; ograniczenia prawnoautorskie nie wyłączają tego statusu) nie podlega kontroli — ogólna uwaga do oprogramowania i technologii w załączniku I **[W]**. Licencja open source nie zmienia tego: GPL to ograniczenie prawnoautorskie, a nie ograniczenie rozpowszechniania **[?]**.
- **Nasze modyfikacje nie są w domenie publicznej**, dopóki ich nie opublikujemy; zmodyfikowany ArduPilot, własne modele i konfiguracje klasyfikuje się osobno (9D/9E, 7D/7E; regulations.md 2.2a) **[?]**.
- Obowiązek dostarczenia kodu z GPL **nie zwalnia** z zezwolenia eksportowego: jeśli klient jest spoza UE, przekazanie kodu odpowiadającego (w tym naszych zmian) jest eksportem technologii. Kolizja: GPL wymaga przekazania kodu każdemu odbiorcy binarium, a prawo eksportowe może tego zakazać → nie dostarczać binarium GPL odbiorcy, któremu nie możemy dostarczyć kodu **[?]**.
- Publikacja własnych komponentów (S12) wyprowadza je spod kontroli, ale samo opublikowanie technologii kontrolowanej może być nielegalnym udostępnieniem — klasyfikacja przed publikacją (§ 28 ust. 2).

### 6.2. Koncesja (ustawa z 13.06.2019 r.)

Licencja na oprogramowanie autonomii dla partnera produkującego wyroby wojskowe może być „obrotem technologią” objętym koncesją po stronie Spółki (regulations.md 2.1 pkt b, psa_todo.md pkt 1) **[W]**. Dotyczy to naszych licencji wychodzących, nie licencji OSS przychodzących.

### 6.3. Cyber Resilience Act (rozporządzenie 2024/2847)

- Wejście w życie 10.12.2024; obowiązki raportowania (art. 14) od 11.09.2026; pełne stosowanie od 11.12.2027 **[W]**.
- Art. 2 ust. 7: nie stosuje się do produktów „developed or modified exclusively for national security or defence purposes” ani zaprojektowanych do przetwarzania informacji niejawnych **[W]**. Produkt podwójnego zastosowania sprzedawany także cywilnie **pozostaje w zakresie**; wariant cywilny Basiliska (dron inspekcyjny, łódź pomiarowa) podlega CRA.
- CRA wymaga od producenta m.in. zarządzania podatnościami w komponentach — w praktyce SBOM i śledzenie komponentów OSS, czyli to samo, co § 26 ust. 6 umowy spółki. Jeden rejestr obsługuje oba obowiązki.
- „Open-source software steward” (art. 24) dotyczy fundacji i podmiotów wspierających OSS, nie producenta pojazdu.

### 6.4. AI Act (rozporządzenie 2024/1689), dyrektywa o odpowiedzialności za produkt (2024/2853)

- AI Act art. 2 ust. 3: wyłączenie systemów używanych „exclusively for military, defence or national security purposes” **[W]**; wariant cywilny podlega AI Act (systemy wysokiego ryzyka w produktach regulowanych, np. komponenty bezpieczeństwa maszyn). Licencja modelu nie ma tu znaczenia, ale AI Act wymaga dokumentacji danych treningowych — dziennik z sekcji 4.9 służy obu celom.
- PLD: oprogramowanie jest produktem (art. 4 ust. 1); stosowanie do produktów wprowadzonych po 9.12.2026; wolne oprogramowanie wyłączone tylko gdy „developed or supplied outside the course of a commercial activity” (art. 2 ust. 2) **[W]**. Skutek: za wadę komponentu OSS w naszym pojeździe odpowiadamy my jako producent; licencje OSS wyłączają gwarancje autorów („AS IS”), więc regresu nie ma. Przy EULA NVIDIA/ZED — klauzule indemnifikacji działają w drugą stronę (my chronimy dostawcę).

### 6.5. Umowy publiczne i niejawne (MON, agencje, NATO)

- Wzorce umów publicznych zwykle wymagają przeniesienia autorskich praw majątkowych na zamawiającego z wymienieniem pól eksploatacji (art. 41 ust. 2, art. 53, art. 74 ust. 4 pr. aut. **[Z]**). Praw do kodu obcego nie da się przenieść; umowa musi wyłączyć komponenty OSS i SDK z przeniesienia i wskazać, na jakiej licencji zamawiający z nich korzysta **[?]**.
- GPL w dostawie dla MON: musimy dostarczyć zamawiającemu kod odpowiadający, a GPL daje mu prawo dalszej redystrybucji na GPL (także konkurentom). Nie da się tego umownie wyłączyć (GPL-3.0 § 10) **[Z]**. Przepisy o ochronie informacji niejawnych ograniczają faktyczną redystrybucję, ale nie uchylają licencji **[?]**. Dlatego własna wartość nie może siedzieć w programie GPL.
- Klauzule „no military use” (sekcja 5) są dla dostaw obronnych bezwzględnym wykluczeniem.

### 6.6. Prawo autorskie — co z OSS przy aporcie i licencji dla SPV

- Aport (Załącznik nr 1, plan_prac T4): dokumentacja wkładu zawiera „wykaz licencji zewnętrznych”; biegły wycenia tylko kod własny; kod własny stanowiący dzieło pochodne GPL ma wartość ograniczoną licencją **[?]**; oświadczenie z § 26 ust. 5 lit. c jest zapewnieniem — jego nieprawdziwość to podstawa odpowiedzialności Założyciela.
- Licencja dla Przedsięwzięcia (§ 33 ust. 3): zakres pól eksploatacji wymienić wyraźnie (art. 41 ust. 2), wyłączyć art. 66 ust. 1 (5 lat) i art. 68 (wypowiedzenie) postanowieniem o czasie i terytorium; zastrzec zakaz sublicencji (art. 67 ust. 3 — domyślnie zakazana, ale lepiej wprost) **[Z]**; w załączniku do licencji wskazać komponenty OSS i SDK, których partner używa na własnych licencjach.

---

## 7. Proces zgodności (program OSS Spółki)

Minimalny program, który spełnia § 26 ust. 6 umowy spółki, przygotowuje Załącznik nr 3 pkt 3, CRA i due diligence inwestora (vc.md). Wzorowany na OpenChain (ISO/IEC 5230) **[W]**.

### 7.1. Polityka licencyjna (do uchwały Rady)

| Kategoria | Licencje | Reguła |
|---|---|---|
| **Zielone** — bez zgody | MIT, BSD-2/3, Apache-2.0, ISC, BSL-1.0, zlib, Unlicense/CC0, MIT-CMU, BSD-3-Clause-Clear, EDL-1.0, OpenMDW | wpis do rejestru; noty w produkcie |
| **Żółte** — zgoda dyrektora ds. zgodności, warunki architektoniczne | LGPL-2.1/3.0, MPL-2.0, EPL-2.0, CDDL, OFL (czcionki), CC BY (dane), licencje modeli z progami (Stability, PML-1.0), EULA SDK | linkowanie dynamiczne albo osobny proces; zmiany ujawnione; dla EULA — lista bibliotek redystrybuowalnych i klauzule Critical Applications sprawdzone |
| **Czerwone** — zakaz w produkcie bez uchwały Rady | GPL-2.0/3.0, AGPL-3.0, SSPL, CC BY-SA i CC BY-NC (dane i wagi), licencje z zakazem użycia komercyjnego (YOLO-NAS, MRL, MNPL), licencje z klauzulą wojskową (Llama, DINOv3, DeepSeek 1.0, Hippocratic z modułem 3.1.20), komponenty z nieustaloną licencją | dozwolone w narzędziach deweloperskich i w laboratorium; w produkcie tylko jako osobny program z gotowym pakietem źródeł i decyzją Rady wpisaną do Załącznika nr 3 pkt 3 |
| **Zakazane** | kod bez licencji („all rights reserved” domyślnie), kod skopiowany z forów/StackOverflow bez ustalenia licencji (CC BY-SA 4.0 **[W]**), SDK naruszające sankcje lub Kryterium Bezpieczeństwa przy dostępie do IP, wagi na danych NC w produkcie bez decyzji Rady | — |

### 7.2. Ewidencja i narzędzia

1. **SBOM** generowany automatycznie dla każdego obrazu i wydania: Yocto `create-spdx` (SPDX 3.0.1) dla obrazu Linux; `syft` lub `ORT` (OSS Review Toolkit) dla pakietów Python/ROS; `ScanCode` dla skanowania nagłówków licencyjnych w kodzie **[W]**. Format SPDX albo CycloneDX; SBOM jest też wymogiem CRA i rosnącym wymogiem zamówień publicznych **[W]**.
2. **Rejestr komponentów** (§ 26 ust. 6): komponent, wersja, licencja (SPDX), kategoria z 7.1, sposób integracji (proces / linkowanie dynamiczne / statyczne / wtyczka), kto zatwierdził, data; osobne zakładki dla wag i zbiorów danych (sekcja 4.9) oraz dla SDK z EULA (data akceptacji, wersja EULA, klauzule krytyczne).
3. **Nagłówki SPDX** w każdym własnym pliku źródłowym (`SPDX-License-Identifier: LicenseRef-Basilisk-Proprietary`), aby skanery odróżniały kod własny od obcego — kluczowe przy aporcie i due diligence.
4. **Bramka CI**: budowa nie przechodzi, gdy SBOM zawiera licencję z kategorii czerwonej bez wpisu wyjątku (Yocto: `INCOMPATIBLE_LICENSE`; ORT: reguły polityki).
5. **Pakiet zgodności wydania** (release compliance pack) dla każdej wersji oprogramowania pojazdu: SBOM, plik NOTICES (teksty licencji i noty, Apache-2.0 § 4 lit. d), pisemna oferta kodu dla GPL/LGPL (3 lata, GPL-3.0 § 6 lit. b), archiwum kodu odpowiadającego (Yocto `archiver.bbclass`), lista bibliotek SDK z podstawą redystrybucji, wykaz wag i ich pochodzenia. Pakiet trafia do dokumentacji produktu i do wersji umowy z klientem.
6. **Dokumentacja produktu** dostarczana klientowi: informacja o komponentach OSS i o prawie do kodu (wymóg GPL/LGPL; dla Qt na LGPL — instrukcja podmiany biblioteki); w EULA własnej — pass-through warunków NVIDIA/ZED i zastrzeżenie, że komponenty OSS pozostają na swoich licencjach.

### 7.3. Umowy

- **Pracownicy i współpracownicy**: obok przeniesienia praw (§ 26 ust. 2) — zobowiązanie do wprowadzania komponentów obcych tylko przez rejestr; zakaz wklejania kodu z nieustaloną licencją; zakaz używania narzędzi AI z klauzulami z sekcji 5 do prac nad produktem obronnym; prawo do wkładów upstream tylko za zgodą (publikacja = § 28 ust. 2).
- **Podwykonawcy i dostawcy oprogramowania**: zapewnienie o zgodności z polityką 7.1, obowiązek dostarczenia SBOM z dostawą, odpowiedzialność za naruszenie licencji, zakaz GPL/AGPL w dostarczanym kodzie bez zgody.
- **Klienci**: EULA własna spójna z licencjami składników; załącznik z notami OSS; przy GPL — oferta kodu; przy kliencie spoza UE — warunek uzyskania zezwolenia eksportowego przed przekazaniem kodu (sekcja 6.1).
- **Partnerzy / SPV (§ 33)**: partner uzyskuje licencje SDK bezpośrednio od dostawców (NVIDIA nie pozwala na sublicencję **[W]**); nasza licencja wylicza, co jest nasze, a co obce.

### 7.4. Lista kontrolna przed pierwszą dostawą (S3/S4)

1. SBOM wygenerowany i przejrzany; brak pozycji „NOASSERTION” i brak kategorii czerwonej bez wyjątku.
2. Każdy komponent GPL/AGPL działa jako osobny proces z udokumentowanym interfejsem; pakiet kodu odpowiadającego zbudowany i przetestowany (buduje się z archiwum).
3. Każda biblioteka LGPL linkowana dynamicznie albo z plikami obiektowymi do przelinkowania; Qt — decyzja LGPL/komercyjna.
4. Lista bibliotek NVIDIA zgodna z aktualnym Attachment A / Supplement; klauzule Critical Applications i eksportowe omówione z NVIDIA albo udokumentowana decyzja Rady.
5. Każdy checkpoint modelu ma wpis pochodzenia; brak wag na licencjach NC lub z klauzulą wojskową.
6. Plik NOTICES i oferta kodu w dokumentacji produktu; EULA własna uzgodniona z kancelarią.
7. Klasyfikacja eksportowa produktu i kodu odpowiadającego (§ 28 ust. 2) z datą i osobą odpowiedzialną.
8. Wpis do Załącznika nr 3 pkt 3 i do rejestru Rady.

---

## 8. Rekomendacje dla Basiliska

1. **Detekcja**: budować na YOLOX, RT-DETR, D-FINE lub RF-DETR w wariantach Apache-2.0, trenując od zera lub na danych o jasnym pochodzeniu; Ultralytics tylko z licencją Enterprise (wycena do budżetu) albo wyłącznie w laboratorium bez przekazywania wyników do produktu. YOLO-NAS, DINOv3, Depth Anything V2 Base/Large — poza produktem.
2. **Autopilot**: PX4 (BSD-3) dla firmware zamkniętego. ArduPilot tylko jako nietknięty lub w pełni ujawniony osobny program z własną logiką na komputerze towarzyszącym — i z decyzją, że klient dostanie kod autopilota.
3. **SLAM/VIO**: RTAB-Map, LIO-SAM, KISS-ICP, Kimera, stella_vslam, Cartographer (permisywne); ORB-SLAM3, OpenVINS, VINS-Fusion, FAST-LIO — nie, chyba że licencja komercyjna od autorów. slam_toolbox i nav2_amcl jako osobne węzły.
4. **NVIDIA**: przed wyborem Jetson jako platformy produktu uzyskać od NVIDIA stanowisko (albo umowę) co do klauzuli Critical Applications dla pojazdów autonomicznych i zastosowań obronnych oraz aktualną listę bibliotek redystrybuowalnych; rozważyć alternatywy (Hailo — HailoRT MIT; OpenVINO; ONNX Runtime) jako ścieżkę zapasową.
5. **GUI / stacja naziemna**: Qt na LGPL tylko dla stacji naziemnej na otwartym komputerze; na urządzeniu zamkniętym — licencja komercyjna Qt albo stos bez Qt (np. web/MapLibre). Foxglove i Cesium ion jako narzędzia wewnętrzne po sprawdzeniu regulaminu.
6. **Radio**: GNU Radio i UHD nie wchodzą do produktu jako część własnego programu; SoapySDR i własne sterowniki.
7. **Modele językowe/VLA**: Llama poza produktem i poza pracami obronnymi; preferować Apache-2.0/MIT (openpi, OpenVLA, Whisper, Qwen3 z zastrzeżeniem pochodzenia, Mistral Apache); narzędzia API dla zespołu — zgodnie z polityką użycia narzędzi AI.
8. **Dane**: SeaDronesSee (CC0), Open Images (CC BY), dane własne; VisDrone, DOTA, xView, nuScenes, KITTI — tylko do badań wewnętrznych bez przenoszenia wag do produktu, chyba że licencja komercyjna.
9. **System**: Yocto z `create-spdx` i `archiver` od pierwszego obrazu; pakiet zgodności wydania jako artefakt CI.
10. **Umowa spółki i dokumenty**: wpisać do Załącznika nr 3 pkt 3 komponenty czerwone używane w laboratorium; w Załączniku nr 1 do wkładu kodu dołączyć SBOM i wykaz licencji; w `law_uzup.md` dodać pytania z sekcji 10.

---

## 9. Czy Ultralytics ma rację co do użytku wewnętrznego — ocena ryzyka

Tekst AGPL-3.0 uzależnia obowiązki od **conveying** (§ 5–6) i od **modyfikacji z interakcją zdalną** (§ 13) **[Z]**. Program niezmodyfikowany uruchamiany wewnętrznie, nawet komercyjnie, nie rodzi obowiązku ujawnienia czegokolwiek. Ultralytics twierdzi, że użycie wewnętrzne wymaga licencji Enterprise **[W]**. Trzy powody, by mimo to nie opierać produktu na AGPL bez licencji:

1. **Granica „modyfikacji”** jest cienka: własne konfiguracje, głowice, eksport do TensorRT z poprawkami w kodzie — każde może być modyfikacją; a operator zdalny (sekcja 1) uruchamia § 13.
2. **Dystrybucja jest nieunikniona** w modelu biznesowym Basiliska (S3–S5, S8, S11): wtedy AGPL działa w pełni, a własna percepcja stałaby się częścią programu AGPL.
3. **Koszt sporu** z dostawcą, który aktywnie egzekwuje swoją interpretację, i sygnał dla inwestora w due diligence (vc.md) przeważają nad korzyścią.

Wniosek: AGPL Ultralytics dopuszczalny wyłącznie w laboratorium (S1), bez wnoszenia wyników do produktu; produkt na Apache-2.0 albo Enterprise.

---

## 10. Do weryfikacji (pytania do kancelarii i do dostawców)

Oficjalne strony niżej wymienione były niedostępne z naszego środowiska 9.10.2026 (blokada sieci); dane oznaczone [W] pochodzą z wyników wyszukiwania.

1. **NVIDIA** — bieżące teksty: CUDA EULA 13.x (Attachment A), TensorRT Supplement (lista bibliotek), JetPack EULA, `Tegra_Software_License_Agreement-Tegra-Linux.txt`, DeepStream `LicenseAgreement.pdf`; pytanie do NVIDIA o umowę Critical Applications dla pojazdów autonomicznych i zastosowań obronnych oraz o pass-through na klienta rządowego.
2. **Ultralytics** — strona licencyjna i cennik Enterprise; czy wagi wytrenowane własnymi danymi w kodzie AGPL są „modyfikacją” w ich rozumieniu.
3. **YOLOX** — ewentualne zapytanie do Megvii o licencję wag (albo decyzja o treningu własnym).
4. **Qt Company** — warunki LGPL dla urządzeń wbudowanych; wycena licencji komercyjnej.
5. **Foxglove, Cesium ion, CoppeliaSim, RTI Connext** — regulaminy i progi użycia komercyjnego.
6. **Stereolabs, Teledyne FLIR, Hailo, DJI** — pełne EULA; klasyfikacja ITAR/EAR kamer FLIR.
7. **Zbiory danych** — regulaminy ImageNet, xView, VisDrone, nuScenes, KITTI, Waymo na żywych stronach.
8. **Gemma, Gemini API, NVIDIA Open Model License** — czy zawierają klauzule wojskowe.
9. **Kancelaria**: (a) status operatora zdalnego jako „użytkownika” w AGPL § 13; (b) czy pojazd przemysłowy/wojskowy jest „User Product” w GPL-3.0 § 6; (c) kolizja obowiązku dostarczenia kodu GPL z zezwoleniem eksportowym; (d) przeniesienie praw w umowach z MON a komponenty obce — wzór wyłączenia; (e) czy regulaminy zbiorów danych (ImageNet) wiążą co do wag; (f) status licencji OSS wobec art. 66 i 68 pr. aut.; (g) odpowiedzialność za wady komponentów OSS pod PLD 2024/2853 i możliwość ubezpieczenia; (h) czy CRA obejmuje wariant cywilny naszych pojazdów (art. 2 ust. 7) i od kiedy.
10. **EUR-Lex** — potwierdzić daty i brzmienie: CRA art. 2 ust. 7, art. 71; AI Act art. 2 ust. 3; PLD art. 2 ust. 2, art. 4 ust. 1, art. 22; 2021/821 uwaga ogólna do technologii i oprogramowania (załącznik I w wersji aktualnego rozporządzenia delegowanego).

---

## 11. Źródła

Pliki licencji odczytane 9.10.2026 z oficjalnych repozytoriów (raw.githubusercontent.com lub gitlab.com) dla: ultralytics/ultralytics, ultralytics/yolov5 (gałąź master i tag v7.0, PR #11359), Megvii-BaseDetection/YOLOX (LICENSE, issues #1684 i #1865), WongKinYiu/yolov7, WongKinYiu/yolov9, THU-MIG/yolov10, Deci-AI/super-gradients (LICENSE.md, LICENSE.YOLONAS.md), pjreddie/darknet, AlexeyAB/darknet, PaddlePaddle/PaddleDetection, lyuwenyu/RT-DETR, roboflow/rf-detr (LICENSE, README; PML-1.0 z pakietu rfdetr-plus 1.1.0 na PyPI), Peterande/D-FINE, facebookresearch/sam2, facebookresearch/dinov2, facebookresearch/dinov3 (LICENSE.md), DepthAnything/Depth-Anything-V2, openai/CLIP, facebookresearch/detectron2, open-mmlab/mmdetection, roboflow/supervision; cocodataset/cocodataset.github.io (termsofuse), storage.googleapis.com/openimages (factsfigures_v7), CAPTAIN-WHU/DOTA (dataset.html), VisDrone/VisDrone-Dataset, nutonomy/nuscenes-devkit, waymo-research/waymo-open-dataset, Ben93kie/SeaDronesSee; ros2/rclcpp, ros2/rclpy, ros2/ros2_documentation (Developer-Guide), ros/ros_comm, eProsima/Fast-DDS, eclipse-cyclonedds/cyclonedds, eclipse-zenoh/zenoh, ros2/rmw_zenoh, micro-ROS/micro_ros_setup, ros2/rclc, eProsima/Micro-XRCE-DDS, eclipse-mosquitto/mosquitto, zeromq/libzmq (LICENSE, NEWS), protocolbuffers/protobuf, grpc/grpc, PX4/PX4-Autopilot, ArduPilot/ardupilot (COPYING.txt, README), ArduPilot/ardupilot_wiki (license-gplv3.rst), mavlink/mavlink (COPYING), mavlink/c_library_v2, ArduPilot/pymavlink, mavlink/MAVSDK, mavlink/mavros, mavlink/qgroundcontrol (.github/COPYING.md), ArduPilot/MissionPlanner, betaflight/betaflight, iNavFlight/inav, ChibiOS/ChibiOS (license.txt, ch.h, hal.h, chlicense.h), apache/nuttx, paparazzi/paparazzi, ros-navigation/navigation2 (LICENSE i wszystkie package.xml), moveit/moveit2, ompl/ompl, cartographer-project/cartographer, SteveMacenski/slam_toolbox, introlab/rtabmap, UZ-SLAMLab/ORB_SLAM3, rpng/open_vins, HKUST-Aerial-Robotics/VINS-Fusion, hku-mars/FAST_LIO, TixiaoShan/LIO-SAM, PRBonn/kiss-icp, borglab/gtsam, ceres-solver/ceres-solver, RainerKuemmerle/g2o, MIT-SPARK/Kimera-VIO, stella-cv/stella_vslam, gazebosim/gz-sim, cyberbotics/webots, isaac-sim/IsaacSim, microsoft/AirSim, iamaisim/ProjectAirSim, carla-simulator/carla, google-deepmind/mujoco, qt/qtbase (LICENSES), foxglove/studio (stan archiwum), facontidavide/PlotJuggler, ros2/rviz, ros-visualization/rqt, maplibre/maplibre-gl-js, maplibre/maplibre-native, CesiumGS/cesium, qgis/QGIS; pytorch/pytorch, tensorflow/tensorflow, google-ai-edge/LiteRT, microsoft/onnxruntime, openvinotoolkit/openvino, NVIDIA/TensorRT, NVIDIA/warp (kopia CUDA EULA 2018), NVIDIA-ISAAC-ROS/gxf (kopia DeepStream Supplement 2021), NVIDIA-ISAAC-ROS/isaac_ros_common, isaac_ros_visual_slam, isaac_ros_nitros, NVIDIA-AI-IOT/deepstream_python_apps, hailo-ai/hailort, google-coral/libedgetpu, huggingface/transformers, ggml-org/llama.cpp, IntelRealSense/librealsense, stereolabs/zed-sdk, ouster-lidar/ouster-sdk, ros-drivers/velodyne, Livox-SDK/Livox-SDK, dji-sdk/Mobile-SDK-Android-V5, dji-sdk/Payload-SDK, opencv/opencv (4.x, 4.4.0), opencv/opencv_contrib, PointCloudLibrary/pcl, isl-org/Open3D, libeigen/eigen (COPYING.README), boostorg/boost, FFmpeg/FFmpeg (LICENSE.md), GStreamer/gstreamer, mirror/x264, multicoreware/x265_git, cisco/openh264, numpy, scipy, scikit-learn, python-pillow, kornia, albumentations, torvalds/linux (COPYING, Linux-syscall-note, drivers/net/wireguard), mirror/busybox, bminor/glibc, kraj/musl, u-boot/u-boot (Licenses/README), openembedded/openembedded-core (create-spdx, license_image, archiver), FreeRTOS/FreeRTOS-Kernel, zephyrproject-rtos/zephyr, STMicroelectronics (stm32f4xx-hal-driver, STM32CubeF4, stm32-mw-usb-device), espressif/esp-idf, raspberrypi/firmware (LICENCE.broadcom), openwrt/openwrt, moby/moby, docker.com (subscription agreement), openssl/openssl, wolfSSL/wolfssl (LICENSING, COPYING), Mbed-TLS/mbedtls, jedisct1/libsodium, WireGuard/wireguard-go, OpenVPN/openvpn, tailscale/tailscale, gnuradio/gnuradio, pothosware/SoapySDR, EttusResearch/uhd, Lora-net/LoRaMac-node, Lora-net/SWL2001; meta-llama/llama-models (LICENSE i USE_POLICY dla llama3, 3.1, 3.2, 3.3, 4), QwenLM/Qwen3, deepseek-ai/DeepSeek-R1, deepseek-ai/DeepSeek-V3 (LICENSE-CODE, LICENSE-MODEL), NVIDIA/Isaac-GR00T, NVIDIA/Cosmos, openvla/openvla, Physical-Intelligence/openpi, openai/whisper, Stability-AI/stable-fast-3d (Community License), CompVis/stable-diffusion (OpenRAIL-M), ContributorCovenant/hippocratic-license (3.0), spdx/license-list-data (AGPL-3.0, GPL-3.0, LGPL-2.1, LGPL-3.0, MIT, BSD-3-Clause), apache.org/licenses/LICENSE-2.0.txt, anthropic.com/legal/aup.

Ustawa o prawie autorskim: `src/legal/pl_1994_83_prawo_autorskie_ujednolicony.txt` (t.j. 2025), art. 41, 53, 64–68, 74–77.

Niedostępne z naszego środowiska (dane [W]): ultralytics.com, image-net.org, xviewdataset.org, nuscenes.org, cvlibs.net, waymo.com/open/terms, docs.nvidia.com, developer.nvidia.com, qt.io, foxglove.dev, cesium.com, coppeliarobotics.com, rti.com, stereolabs.com, teledynevisionsolutions.com, hailo.ai, developer.dji.com, llama.com, about.fb.com, ai.google.dev, openai.com, mistral.ai, gnu.org (FAQ), eur-lex.europa.eu, isap.sejm.gov.pl.
