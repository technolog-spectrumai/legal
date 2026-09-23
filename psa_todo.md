# Zadania na później — projekt umowy P.S.A. i dokumenty towarzyszące

Lista rzeczy odłożonych świadomie: nie wchodzą do bieżącego zapytania do kancelarii (`email.md`, `law.md`), ale trzeba do nich wrócić. Stan na 21 września 2026 r., gałąź `psa_hybrid`. Odesłania do paragrafów według aktualnego `psa.pdf`.

Konwencja: `- [ ]` do zrobienia, `- [x]` zrobione; przy pozycji podajemy plik, którego dotyczy, i moment, kiedy ma sens.

---

## 1. Pytania odłożone na później (nie w tym zapytaniu)

- [ ] **Wybór jurysdykcji i struktura na przyszłość.** Zadać kancelarii po otrzymaniu memorandum albo przed rundą, nie w zapytaniu o wycenę. Treść do wykorzystania:
  > Spółka nie została jeszcze zawiązana i wybór jurysdykcji pozostaje otwarty: wariantem podstawowym jest P.S.A. w Polsce, ale rozważamy także spółkę w innym państwie UE/EOG (np. w Estonii) z polskim zespołem albo strukturę holdingową ze spółką zależną w UK lub USA pod programy NATO i klientów zagranicznych. Prosimy o uwagę w zakresie prawa polskiego, bez analizy prawa obcego: (1) które z przyjętych mechanizmów (Kryterium, zwrotne zbycie jako obowiązek związany z akcją, serie P i F z art. 300¹⁰³ KSH, prawo pierwszeństwa, drag-along) są specyficzne dla P.S.A., a które dałoby się odtworzyć w umowie wspólników; (2) koszty, czas i ryzyka późniejszego przekształcenia transgranicznego albo przeniesienia siedziby (procedura z KSH po wdrożeniu dyrektywy o mobilności, podatek od niezrealizowanych zysków, wkłady niepieniężne, ciągłość programu motywacyjnego i zwrotnego zbycia); (3) wpływ struktury holdingowej na Kryterium liczone przez beneficjentów rzeczywistych oraz na kwalifikowalność do PFR, FENG, EDF i EIC; (4) gdzie w takiej strukturze powinna być własność intelektualna i jakie to ma skutki dla rundy, kontroli eksportu i programów wymagających IP w UE.
  Kontekst: PFR Otwarte Innowacje dopuszcza spółki zagraniczne z polskimi założycielami do 40 % portfela funduszu (`regulations.md`, sekcja 3).
- [ ] **Koncesja przy licencji dla spółki celowej.** Czy udzielenie licencji na oprogramowanie autonomii partnerowi produkującemu wojskowe UAV (§ 33 ust. 3) jest „obrotem technologią” wymagającym koncesji po stronie Spółki. Dopisać do `law.md` 4.1.1 przy następnej wersji zapytania albo zadać po memorandum.
- [ ] **Wyłączenia B+R w ustawie koncesyjnej z 2019 r.** Czy prototypy i prace rozwojowe są objęte jakimkolwiek wyłączeniem; zakres definicji „wytwarzanie” (modyfikacja) i „obrót” (udostępnianie). `law.md` 4.1.1.
- [ ] **Kryterium a art. 9 EDF.** Kryterium dopuszcza kontrolę przez podmioty z NATO spoza UE (USA, UK, Turcja), a EDF i AGILE wykluczają firmy kontrolowane przez państwo niestowarzyszone. Pytanie, czy zawęzić Kryterium dla kontroli (nie dla udziału) do UE/EOG, albo zapisać to w umowie wspólników. `law.md` nowy punkt; `regulations.md` 3 i 3a.
- [ ] **Klasyfikacja dual-use produktów cywilnych.** Rozszerzyć `law.md` 4.2.2 o rozporządzenie 2021/821 (9A012.b.2, kategorie 7, 5A002, 9D/9E), transfer wewnątrzunijny (załącznik IV), zakres zezwolenia generalnego EU001 dla naszych pozycji, ITAR/EAR komponentów z USA.
- [ ] **Wymogi koncesyjne po nowelizacji z 13 marca 2026 r.** (Dz.U. 2026 poz. 471) — co zmieniło się w ustawie z 2019 r.; `regulations.md` 2.1 oznaczone [Z/?].

## 2. Po otrzymaniu memorandum kancelarii

- [ ] Wcześniej: po odpowiedzi kancelarii (albo na jej prośbę o projekt do wyceny) wysłać `mail.md` z `psa.pdf` i `law.md`; zapisać datę wysłania i commit załączników w `psa_feedback.tex`, Część 3.
- [ ] Wkleić odpowiedź jako R1 do `psa_feedback.tex`, Część 3, ze stanowiskiem Założycieli przy każdej uwadze; odesłania według numeracji `law.md`.
- [ ] **Decyzja: bramka miękka czy twarda** przy odmowie zgody z powodu Kryterium (`law.md` 1.2). Miękka jest w `psa_hybrid`, twarda na gałęzi `psa_hard`; brzmienia obu w `psa_feedback.tex`, Część 1 pkt 1.
- [ ] **Decyzja: przekreślony wyjątek dla funduszy** (§ 11 ust. 14, `law.md` 1.4): usunąć albo przywrócić w poprawionym brzmieniu.
- [ ] **Decyzja: przekreślone zdania** (siedem powtórzeń ustawy) — usunąć po potwierdzeniu.
- [ ] Zlecić wdrożenie uzgodnionych zmian i wersję do aktu notarialnego (osobna wycena, zgodnie z `email.md`, sekcja 2).
- [ ] Ponowny audyt zmienionych paragrafów: `psa_feedback.tex` Część 2 odnosi się do wersji 0.8 i nie obejmuje późniejszych zmian.

## 3. Przed zawiązaniem spółki

- [ ] **Załącznik nr 1:** dane Założycieli, numery akcji, wkłady z wartościami i tytułami prawnymi (58 pól `\field{}` w `psa.tex`); dokumenty przenoszące IP, wyceny wkładów niepieniężnych (`law.md` 3.1).
- [ ] **Załącznik nr 2:** wskazać Założycieli objętych mechanizmem czasowym z datą rozpoczęcia albo jednoznacznie stwierdzić brak takich osób.
- [ ] **Załącznik nr 3:** ujawnione aktywności każdego Założyciela (zakaz konkurencji, § 29 ust. 2).
- [ ] **Umowa wspólników** (`shareholder_agreement.tex`): dokończyć po memorandum; dopisać trzy warunki z `regulations.md` 3a: brak kontroli i weta wspólników spoza UE/EOG, dopóki firma korzysta z EDF, AGILE lub EUDIS; co najmniej dwóch członków Rady z obywatelstwem UE/EOG (pod koncesję); checkpoint G2 przed pracą zdalną spoza UE. Załączniki A–C (oferta, pełnomocnictwo, przystąpienie) do sprawdzenia przez kancelarię pod art. 101 i 108 KC.
- [ ] Wybór podmiotu prowadzącego rejestr akcjonariuszy pod kątem obsługi ograniczeń (obowiązki związane z akcją, Kryterium).
- [ ] Końcowa kontrola kodów PKD 2025 (10 do pierwszego wpisu, 72.10.Z przeważający); wojskowe kody zostają w umowie do późniejszego ujawnienia.
- [ ] Opcjonalnie w `psa.tex` § 4 ust. 7: zdanie, że samo wskazanie kodu PKD nie jest podstawą do rozpoczęcia działalności regulowanej.
- [ ] Zgłoszenie beneficjentów rzeczywistych do CRBR po wpisie.

## 4. Dokumenty wykonawcze (zakres E z zapytania)

- [ ] Regulamin Rady Dyrektorów — z bramkami G1–G6 z `regulations.md` sekcja 4 jako obowiązkowymi checkpointami dyrektora ds. zgodności (§ 21 ust. 7, § 28 ust. 4).
- [ ] Regulamin programu motywacyjnego serii P; interpretacja indywidualna podatkowa dla programu w P.S.A.
- [ ] Wzory uchwał: emisja serii P i F, zgoda na zbycie akcji, uchwała kierunkowa rundy, zgoda na Przedsięwzięcie Produkcyjne.
- [ ] Wzór umowy spółki celowej i konsorcjum z klauzulami z `regulations.md` 3b.4 (zakres licencji, ulepszenia, kontrola eksportu obu stron, brak danych ITAR bez zgody, repozytoria).
- [ ] Umowy z pracownikami i B2B: przeniesienie IP, NDA, regulamin dostępu do Kluczowej Własności Intelektualnej, zakaz pracy zdalnej spoza UE bez zgody.

## 5. Zgodność regulacyjna (bramki z `regulations.md`)

- [ ] **G1, przed pierwszym testem w terenie:** rejestracja operatora ULC, kategoria operacji i SORA przy BVLOS/rojach; przy USV zgoda urzędu morskiego i rejestracja jednostki powyżej 7,5 m lub 15 kW; pozwolenia radiowe UKE; ubezpieczenie OC.
- [ ] **G2, przed pierwszym udostępnieniem technologii poza firmę:** klasyfikacja produktu, kodu i dokumentacji według aktualnego załącznika I do 2021/821 z zapisem wyniku; kod i dokumentacja na serwerach w UE; rejestr dostępu (§ 26 ust. 6) z obywatelstwem i miejscem pracy; rejestracja EU001 w MRiT przed pierwszym transferem do UK, USA, Norwegii; wniosek o ustalenie kontroli przy wątpliwościach.
- [ ] **Program zgodności eksportowej** (§ 28 ust. 4) od startu; WSK dopiero przy uzbrojeniu.
- [ ] **G3, przed pierwszym wariantem wojskowym:** kwalifikacja wyrobu do wykazu WT; koncesja MSWiA przed wytwarzaniem lub modyfikacją; ujawnienie 30.32.Z w KRS.
- [ ] **G4, przed kontraktem z MON lub NATO:** świadectwo bezpieczeństwa przemysłowego (start procedury co najmniej 12 miesięcy wcześniej), pion ochrony, poświadczenia osób.
- [ ] **G5, przed pierwszym eksportem:** zezwolenie MRiT albo potwierdzenie braku kontroli; kraj i użytkownik końcowy; sankcje.
- [ ] Sprawdzić obowiązki z AI Act, rozporządzenia maszynowego 2023/1230 i Cyber Resilience Act dla produktów cywilnych (terminy 2026–2027).

## 6. Finansowanie — terminy do pilnowania

- [ ] EIC Accelerator: sesje pełnych wniosków 2 września i 4 listopada 2026 r.; wnioski dual-use od 9 lipca 2026 r.; kolejne cykle 2027 r.; grant do 2,5 mln EUR, inwestycja do 30 mln EUR.
- [ ] Ścieżka SMART (PARP, pojedyncze MŚP): nabór 29 października – 29 grudnia 2026 r.; wymaga realnych prac B+R, więc najpierw wyniki eksperymentów.
- [ ] NATO DIANA: wyzwania 2026; TRL co najmniej 4; 100 tys. EUR w fazie 1.
- [ ] PFR Deep Tech: fundusze Expeditions II i Balnord już zasilone; śledzić kolejne; PFR Otwarte Innowacje (ticket od ok. 5 mln zł).
- [ ] AGILE (od początku 2027 r., granty 1–5 mln EUR) i EUDIS Business Accelerator (voucher 65 tys. EUR) — sprawdzić warunki kontroli właścicielskiej przed aplikacją.

## 7. Porządki w repozytorium

- [ ] `zmiany.md` opisuje tylko zmiany 0.8 → 0.9.3; uzupełnić o podział na warianty, wydzielenie dokumentów, bramkę miękką i scalenie `psa_soft`.
- [ ] Gałęzie `psa_vs` i `psa_prod` zawierają jeszcze dawne Załączniki 4–11 w `psa.tex`; zdecydować, czy je aktualizować, czy zostawić jako archiwum.
- [ ] Gałąź `psa_soft` po scaleniu do `psa_hybrid` jest zbędna; `psa_hard` zostaje jako alternatywa do decyzji z pkt 2.
- [ ] `.gitignore` nie wyklucza `*.pdf` (linia jest zakomentowana); zdecydować, czy PDF-y wersjonować.
- [ ] Autor commitów to domyślna tożsamość sesji; ustawić `git config user.name` i `user.email`.
- [ ] `law.md` do wysyłki jako Markdown albo PDF: `pandoc` niedostępny; ewentualnie `law.tex` w stylu `basilisk_i18n.sty`.
- [ ] Po wysłaniu maila zapisać datę wysłania i commit załączników w `psa_feedback.tex`, Część 3 (rejestr korespondencji został usunięty z `email.md`).
- [ ] `extra.tex` Dokument nr 5 (mapa rundy): dopisać uwagę o kontroli spoza UE/EOG a EDF (`regulations.md` sekcja 3).
