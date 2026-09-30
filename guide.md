# Przewodnik dla nieprawników

Ten plik tłumaczy, co jest w tym repozytorium, po co to powstało i od czego zacząć, jeśli nie jesteś prawnikiem. Nie zastępuje porady prawnej: wszystko tutaj to materiał roboczy, który przed podpisaniem umowy musi sprawdzić radca prawny albo adwokat.

## O co chodzi w jednym akapicie

Zakładamy spółkę **Basilisk Systems P.S.A.** — prostą spółkę akcyjną (P.S.A.), najprostszą polską formę dla startupów. Działamy w obronności i technologiach podwójnego zastosowania (cywilno-wojskowych), więc do zwykłej umowy spółki dodaliśmy zabezpieczenia: kto może zostać akcjonariuszem, co się dzieje z akcjami założyciela, który odchodzi albo umiera, jak chronimy technologię i jak przygotować spółkę pod inwestora. Napisaliśmy projekt umowy, zadaliśmy do niego 79 szczegółowych pytań i przygotowaliśmy na nie odpowiedzi w formie memorandum prawnego.

## Od czego zacząć (15 minut)

1. **Ten przewodnik** — słowniczek i mapa plików poniżej.
2. **`memorandum.pdf`** (budowany z `memorandum.tex`, polecenie `./build.sh memorandum`) — przeczytaj rozdział „Podsumowanie wykonawcze”: ocena projektu, 18 zmian koniecznych i 7 najważniejszych rozstrzygnięć.
3. **Załącznik nr 2 memorandum — „Decyzje Założycieli”** — 16 decyzji, które musimy podjąć sami (np. wariant A czy B, kody PKD, kto prowadzi rejestr akcjonariuszy). Bez nich prawnik nie dokończy umowy.

Resztę czytaj wtedy, gdy potrzebujesz konkretnej odpowiedzi.

## Jak czytać memorandum

Są dwie wersje tej samej treści:

- **`memorandum.pdf` / `memorandum.tex`** — tekst naszej umowy (czarny), a przy konkretnych ustępach **niebieskie ramki** z odpowiedziami. Czytasz umowę i od razu widzisz, co z danym postanowieniem jest nie tak i jak je poprawić. Na końcu jest indeks wszystkich 79 pytań z numerami stron.
- **`memorandum.md`** — pełny tekst wszystkich odpowiedzi, z całym uzasadnieniem. Do sięgania, gdy ramka to za mało.

Każda odpowiedź ma ten sam układ:

| Element | Co znaczy |
|---|---|
| **Ocena** | stan projektu: *zgodne* (w porządku), *zgodne warunkowo* (działa, jeśli coś dopiszemy), *ryzyko* (w obecnej postaci może nie zadziałać) |
| **Klasyfikacja** | co zrobić: *konieczne* (trzeba zmienić przed podpisaniem), *zalecane* (warto zmienić), *opcjonalne* (można), *bez zmian* |
| **K1–K18** | numery 18 zmian koniecznych — lista w podsumowaniu |
| **Podstawa prawna** | przepisy, na których opiera się odpowiedź |
| **Proponowane brzmienie** | gotowy tekst do wklejenia do umowy (zawsze przy zmianach koniecznych) |

Oznaczenia przy przepisach mówią, na ile jesteśmy pewni:

- **[Z]** — sprawdzone w tekście ustawy albo rozporządzenia (pliki w `src/legal/`);
- **[W]** — wiedza ogólna, trzeba sprawdzić w źródle;
- **[?]** — hipoteza; nie opierać na niej decyzji.
- „(tekst EN)” — sprawdzone tylko w angielskiej wersji aktu UE.

## Słowniczek

| Pojęcie | Po ludzku |
|---|---|
| **P.S.A.** (prosta spółka akcyjna) | polska spółka dla startupów: kapitał od 1 zł, akcje bez wartości nominalnej, zarządza Rada Dyrektorów |
| **Umowa spółki** (`psa.tex`) | „konstytucja” spółki, podpisywana u notariusza i składana do sądu; wiąże każdego przyszłego akcjonariusza |
| **Umowa akcjonariuszy / wspólników** (`shareholder_agreement.tex`) | prywatna umowa między nami; poufna, łatwiejsza do zmiany, ale wiąże tylko tych, którzy ją podpisali |
| **KRS** | rejestr sądowy spółek; wpis tworzy spółkę |
| **Rejestr akcjonariuszy** | lista właścicieli akcji; w P.S.A. prowadzi ją dom maklerski albo notariusz, a przeniesienie akcji działa dopiero po wpisie |
| **Rada Dyrektorów** | organ zarządzający P.S.A. (odpowiednik zarządu / boardu) |
| **Walne Zgromadzenie (WZ)** | zebranie akcjonariuszy, decyduje o najważniejszych sprawach |
| **Kryterium Bezpieczeństwa EU/NATO** | nasz warunek: akcjonariuszem może zostać tylko osoba lub firma z UE/EOG/NATO (z wyjątkami) |
| **Zwrotne zbycie** | odpowiednik *reverse vesting*: założyciel, który odchodzi, musi sprzedać część akcji |
| **Wartość Godziwa** | cena akcji ustalana przez niezależnego eksperta, gdy trzeba je odkupić |
| **Seria P / seria F** | akcje dla pracowników (program motywacyjny, ESOP) / dla późniejszych współzałożycieli |
| **Kwalifikowana Runda** | runda finansowania od inwestora, która uruchamia określone mechanizmy umowy |
| **Wariant A / wariant B** | dwa sposoby odmowy sprzedaży akcji komuś spoza Kryterium; rekomendujemy A |
| **Dual-use** | towary i technologie cywilne, które mogą mieć zastosowanie wojskowe; ich eksport wymaga zezwoleń (rozporządzenie UE 2021/821) |
| **Koncesja** | zezwolenie MSWiA na produkcję i handel wyrobami wojskowymi |
| **EDF** | Europejski Fundusz Obronny; wyklucza firmy kontrolowane spoza UE/EOG |
| **Kontrola inwestycji (FDI)** | państwo sprawdza inwestorów spoza UE; od 17.01.2028 r. obowiązkowo dla firm dual-use i obronnych w całej UE (rozporządzenie 2026/1386) |

## Mapa plików

**Umowy i dokumenty formalne (LaTeX → PDF przez `./build.sh`)**
- `psa.tex` — projekt umowy spółki, wersja 0.9.4-C.
- `shareholder_agreement.tex` — projekt umowy wspólników z umową wykonawczą zwrotnego zbycia.
- `extra.tex` — 6 dokumentów pomocniczych: prawa akcjonariusza, emisje, proces decyzyjny, podatki.
- `memorandum.tex` / `memorandum.md` — memorandum (patrz wyżej).
- `psa_feedback.tex` — historia rozstrzygnięć i miejsce na opinię kancelarii oraz nasze stanowisko.

**Pytania do prawnika**
- `email.md`, `mail.md` — zapytanie wysłane do kancelarii.
- `law.md` — 79 szczegółowych pytań (nie zmieniamy — tak poszło do kancelarii).
- `law_uzup.md` — miejsce na pytania uzupełniające.

**Tło biznesowe**
- `vc.md` — czego oczekują fundusze VC (Polska, świat, fundusze obronne) i jak to się ma do naszej umowy.
- `regulations.md` — mapa przepisów (koncesje, eksport, EDF, NATO) i „bramki” zgodności.
- `emisja/` — jak wydawać akcje założycielom, pracownikom i inwestorom.
- `case_studies/` — przykłady firm (ICEYE, WB Electronics, Swarmer, rynek Catalyst).

**Planowanie i historia**
- `plan_prac.md` — plan całej pracy (27 punktów) i co już zrobiono.
- `psa_todo.md` — lista rzeczy do zrobienia.
- `zmiany.md`, `spis_tresci.md` — historia zmian i spis paragrafów umowy.

**Źródła**
- `src/legal/` — pełne teksty ustaw i rozporządzeń (pliki `.txt`), z których sprawdzaliśmy memorandum; `src/legal/todo.md` — czego jeszcze brakuje.
- `src/tools/` — skrypty do pobierania źródeł; `src/notatki.md` — notatki robocze.

## Co dalej (kolejność)

1. **Decyzje Założycieli** — 16 punktów z Załącznika nr 2 memorandum; zapisujemy je w `psa_feedback.tex`.
2. **Prawnik** — radca prawny albo adwokat weryfikuje memorandum (zwłaszcza punkty [W] i [?]) i zmiany konieczne.
3. **Poprawiona umowa** — naniesienie zmian do `psa.tex`, wersja „do aktu notarialnego”.
4. **Notariusz i KRS** — podpisanie umowy, wniesienie wkładów, wpis do rejestru.
5. **Później, gdy będzie potrzeba** — koncesja (przed pierwszą sprzedażą wojskową), program zgodności eksportowej (przed pierwszym transferem technologii za granicę), dokumenty rundy (przed inwestorem).

## Dlaczego to wygląda na skomplikowane

Sama P.S.A. jest prosta. Złożoność bierze się z dwóch rzeczy: branży (obronność i dual-use są mocno regulowane w każdym kraju — w USA ITAR i CFIUS, w Wielkiej Brytanii NSI Act, w całej UE od 2028 r. obowiązkowa kontrola inwestycji) oraz z tego, że od początku wpisujemy do umowy zabezpieczenia, które inne startupy dodają dopiero przy rundzie. Tylko 18 z 98 uwag memorandum jest koniecznych przed podpisaniem; większość obowiązków uruchamia się później, przy konkretnych zdarzeniach.
