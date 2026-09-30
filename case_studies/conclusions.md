# Wnioski z trzynastu case studies: co Basilisk kopiuje, czego unika, co decyduje przed rundą A

Dokument wewnętrzny Basilisk Systems, informacyjny. Nie jest opinią prawną ani rekomendacją inwestycyjną i nie zmienia umowy spółki. Synteza obu serii studiów przypadku z katalogu `case_studies/` (pierwsza: Swarmer, WB Electronics, ICEYE, Catalyst; druga: Anduril, Shield AI, Helsing, Destinus, Tekever, Milrem, Creotech, APS, Figure AI, Nomagic) i katalogu `jurisdictions/`. Odesłania do umowy według `psa.tex` w wersji 0.9.4-C (numery § według `spis_tresci.md`); dokument zamyka pytania z `psa_todo.md` sekcje 1 i 6, `law_uzup.md` U.5 i decyzję D1 z memorandum, i uzupełnia `vc.md` sekcje 8–11 oraz `plan_prac.md` etap C.

Stan na 30 września 2026 r. Oznaczenia wiarygodności jak w case studies: **[Z]** dokument pierwotny, **[M]** prasa i bazy, **[W]** wiedza ogólna, **[?]** szacunek albo teza. Wnioski poniżej są tezami wyprowadzonymi z cytowanych faktów; każdą liczbę można sprawdzić w sekcjach 5–8 właściwego pliku.

---

## 1. Dziesięć tez

1. **Punkt przegięcia to pierwszy kontrakt publiczny, nie runda.** WB 1998 r., ICEYE 2020 r., Creotech grudzień 2024 r. (przychód ×4), APS 2026 r. (SAN), Milrem 2020 r. (EDIDP), Shield AI 2016 r. (DIU), Anduril 2018 r. (CBP). Swarmer i Figure bez niego mają 0,3 mln USD i nieujawniony przychód przy wycenach odpowiednio ponad 1 mld USD i 39 mld USD. **[?]**
2. **Klient sojuszniczy albo cywilny przychodzi przed własnym MON.** APS: UK kupuje dla Ukrainy w 2022 r., SAN w 2026 r.; Tekever: UK 270 mln GBP, Portugalia poniżej 10 mln EUR; Anduril: straż graniczna przed Pentagonem; Milrem i Destinus: Niemcy i Holandia płacą za Ukrainę. Basilisk powinien planować pierwszego klienta poza MON i traktować MON jako drugiego, który mnoży skalę. **[?]**
3. **Czyste oprogramowanie dochodzi do programów of record na trzy sposoby:** jako osobna pozycja pod rządową architekturą referencyjną (Shield AI, A-GRA, czerwiec 2026 r.), jako certyfikowana warstwa AI wewnątrz kontraktu prima (Helsing w Arexis Saaba, Airbus Wingman) albo z własnym nośnikiem (Anduril, Shield AI V-BAT, Helsing HX-2). Trzecia droga przyniosła wypadki (V-BAT), spór o HX-2 i straty rzędu miliarda dolarów rocznie (Anduril). Basilisk wybiera pierwszą i drugą. **[?]**
4. **Siedziba matki idzie za prawem eksportowym i programami, spółka operacyjna za klientem.** Destinus opuścił Szwajcarię, bo KMG blokował Ukrainę i budżety NATO; Tekever zbudował spółkę w UK dziewięć lat przed przełomem; Anduril zakłada spółki po każdym programie (Australia, Tajwan, Japonia); Nomagic przeszedł pod matkę w USA w 20 miesięcy po seedzie od Khosli. Polska matka spełnia Kryterium § 11, EDF, SAFE, PFR i estoński CIT; żadne inne państwo nie daje wszystkiego naraz (`jurisdictions/README.md` sekcja 1). **[Z]/[?]**
5. **Inwestor spoza UE/EOG w roli kontrolującej kosztuje kwalifikowalność do EDF; ratunkiem są gwarancje państwa.** Milrem po sprzedaży EDGE utrzymał rolę koordynatora EDF tylko dzięki gwarancjom Estonii (lipiec 2023 r.); Swarmer z matką w USA jest poza EDF. § 11 bez wyjątku funduszowego (skreślony ust. 14) to właściwa domyślna zasada; potrzebna jest ścieżka wyjątku uchwałą 75 % i wcześniejsza rozmowa z MON. **[Z]/[W]**
6. **Kapitał cierpliwy ma trzy źródła, a VC jest tylko jednym.** Państwo jako pierwszy inwestor (ARP w Creotechu 17,1 %, Tesi i Solidium w ICEYE, PFR w WB), inwestor kotwiczny z mandatem wielorundowym (Founders Fund w 5 z 9 rund Andurila, Prima Materia w Helsingu, Khosla w każdej rundzie Nomagica) i banki rozwoju (EBI venture debt i EBOR w Nomagicu, Business Finland w ICEYE). Polskie VC odmówiło Creotechowi i nie pojawia się w historii Nomagica; APS i WB obyły się bez VC. **[M]/[?]**
7. **Granty i konsorcja EDF finansują B+R platformy, ale nie zastępują klienta.** Milrem: 30,6 mln EUR EDIDP i 50 mln EUR EDF przy ok. 6 mln USD kapitału zewnętrznego; Creotech: NCBR → ESA → SMART przed MON; ICEYE: 83 mln EUR jako dźwignia; Swarmer: 50 tys. USD i giełda; Figure i Nomagic: zero polskich grantów. Wniosek: EDF, EDIP, SMART i DIANA jako obniżenie rozwodnienia na TRL 4–7, sparowane z pierwszym płatnym pilotem. **[Z]/[?]**
8. **Giełda w Polsce działa dla deep techu z kotwicą publiczną, ale wymaga S.A. i rozwadnia założycieli.** Creotech: NewConnect 11,3 mln zł (2021 r.) → GPW 39,7 mln zł (2022 r.) → 481 mln zł (ABB 2026 r.), założyciele z 15,2 % każdy do 6–7 %; APS: dwa nieudane podejścia (2018 r., 2021 r.); Swarmer: mikro-IPO i −41 % po lock-upie; Anduril: „nie w hossie". P.S.A. nie może być notowana (art. 300³⁶ § 2 KSH), więc przekształcenie w S.A. tylko przy realnym oknie. **[Z]/[M]**
9. **Kontrola założycieli utrzymuje się jedną z czterech dróg:** własny kapitał (Figure, Destinus przez instrumenty zamienne), klient zamiast kapitału (WB 73,56 %, APS), polskie instytucje zamiast zagranicznego VC (Creotech: ARP, OFE, TFI) albo pakiet blokujący mimo megarund (Tekever 25–50 %). Utrata kontroli przyszła z giełdą (Swarmer), sprzedażą (Milrem) i późnym PE (Shield AI: zewnętrzny prezes, kapitał uprzywilejowany przed zwykłym). **[Z]/[M]**
10. **Wyceny 2026 r. to cykl hossy:** Tekever ×5 w 16 miesięcy, Figure ×15 w 19 miesięcy, Anduril ×2 rocznie, Creotech +570 % w 2025 r.; przychody Helsinga, Tekevera, Destinusa i Figure są nieujawnione albo sprzeczne. Progów Kwalifikowanej Rundy (§ 32) nie kalibrować do tych liczb. **[M]/[?]**

---

## 2. Co Basilisk kopiuje, a czego unika

| Kopiować | Od kogo | Unikać | Od kogo |
|---|---|---|---|
| Sekwencja: klient cywilny lub sojuszniczy → OTA/prototyp (DIANA, EDF, Brave1) → integracja z platformą prima → produkcja u sojusznika | Anduril, Shield AI, Milrem | Własny nośnik i fabryka przed przychodem | Helsing (HX-2), Shield AI (V-BAT), Figure |
| Autonomia jako osobna pozycja w kontrakcie pod architekturą referencyjną; produkt „Enterprise" dla OEM | Shield AI (A-GRA, KAI, Kratos, Airbus) | Zamrożona specyfikacja u powolnego zamawiającego | APS (SKYctrl 2022 r.) |
| Spółka zależna w kraju zamawiającego, wcześnie i z zespołem | Tekever (UK 2013 r.), Anduril, Helsing | Przeniesienie matki poza UE/EOG (flip do Delaware) | Swarmer, Nomagic (koszt: EDF, SAFE, 19 % PIT) |
| Państwo i banki rozwoju jako pierwszy kapitał; inwestor kotwiczny z mandatem na kolejne rundy | Creotech (ARP), ICEYE, Nomagic (EBI, EBOR), Anduril (Founders Fund) | Jedna runda PE z zegarem 3 lat bez uzgodnionej ścieżki wyjścia | APS (EI 2023 → proces sprzedaży 2026) |
| Eksport finansowany przez darczyńcę (państwa NATO płacą za Ukrainę) | Milrem, Destinus, Tekever, APS | Bezpośrednie ryzyko kredytowe Ukrainy; TOV jako centrum zysku | `jurisdictions/ukraina.md` |
| Klient jako inwestor mniejszościowy i prawa do danych z wdrożeń | Nomagic (Zalando), Figure (BMW jako pilot), Shield AI (L3Harris) | Zależność od cudzego modelu albo wyłączność modelu dla jednego klienta | Figure (OpenAI) |
| Rada z byłym urzędnikiem MON/NATO i prime'em jako partnerem-inwestorem | Destinus, Helsing (Enders), Shield AI (Saab, Hanwha) | Nieprzejrzysty wehikuł jako największy akcjonariusz | Swarmer (Theseus) |
| Klauzula gwarancji państwa dla exitu poza Kryterium | Milrem | Exit poza UE bez planu na art. 9 EDF | Milrem (6 miesięcy niepewności) |
| Polityka bezpieczeństwa systemów autonomicznych trwalsza niż runda | kontrprzykład Figure | Blokowanie secondaries pracowników | Figure |

---

## 3. Odpowiedzi na otwarte pytania z dokumentów Basiliska

| Pytanie | Odpowiedź z case studies | Wiar. |
|---|---|---|
| D1 (memorandum), `psa_todo.md` sekcja 1: gdzie siedziba? | P.S.A. w Polsce jako matka co najmniej do rundy A; spółki zależne według rynku po pierwszym kontrakcie (kolejność: Niemcy, Francja, Estonia, USA, UK, Finlandia, Litwa, Holandia, Ukraina, Portugalia w wariancie morskim); matka w UE/EOG tylko na żądanie inwestora wiodącego i pierwszą wymianą udziałów; Delaware nigdy przed rezygnacją z programów UE (`jurisdictions/README.md` sekcja 6) | [Z]/[?] |
| U.5 (`law_uzup.md`): koszty późniejszego przekształcenia | flip poza UE/EOG opodatkowany 19 %, exit tax przy przeprowadzce założycieli, utrata estońskiego CIT i „polskiego nexusa" PFR; Nomagic pokazuje, że substancja może zostać w Polsce, Swarmer, że programy UE się traci (`jurisdictions/przeniesienie_i_podatki.md`) | [Z] |
| `psa_todo.md` sekcja 6: plan finansowania | szczeble: (1) SMART, DIANA Fort Kraków, Brave1, EIC dual-use do 28 października 2026 r.; (2) pierwszy płatny pilot z producentem albo klientem sojuszniczym; (3) runda A z PFR, NIF, ARP lub Vinci i inwestorem kotwicznym z mandatem na B; (4) EBI venture debt i EBOR po przychodzie; (5) gwarancje BGK i banków pod umowę z primem; (6) przekształcenie w S.A. tylko przy oknie giełdowym | [?] |
| `vc.md` sekcja 8 („Exit": BRAK) | trzy ścieżki do zapisania w umowie akcjonariuszy: giełda w Polsce po przekształceniu (Creotech), sprzedaż do prima z UE/NATO z earn-outem i arbitrażem (Anduril–Area-I jako ostrzeżenie), odsprzedaż w rundach (ICEYE); exit poza Kryterium tylko uchwałą 75 % i po rozmowie o gwarancjach (Milrem) | [?] |
| `vc.md` sekcja 9 („czego nie oddawać") | § 25 ust. 1 lit. h (strategia), § 29–30 (podmioty powiązane), § 10 (vesting), § 26 (IP): potwierdzone przez Swarmera (przewodniczący z własną spółką), Figure (pozew o bezpieczeństwo), Shield AI (utrata fotela prezesa) | [M]/[?] |
| `regulations.md` sekcja 4 (bramki G1–G6) | G4 (pieniądze publiczne) potwierdzone jako warunek każdej skutecznej drogi; G5 (pierwszy kontrakt) jako punkt przegięcia; dodać bramkę „architektura referencyjna" (A-GRA, CFSN) przed G5 | [?] |

---

## 4. Decyzje do podjęcia przed rundą A

1. **Wariant produktowy:** warstwa autonomii licencjonowana producentom i primom (Shield AI Enterprise) plus pakiet w konsorcjach EDF (Milrem „intelligent functions"); bez własnego nośnika. Konsekwencja: § 33 ust. 3 (licencja niewyłączna, ograniczona zakresem, wypowiadalna przy zmianie kontroli) i wzór umowy „na platformę" z audytem wolumenów (`swarmer.md` sekcja 10).
2. **Pierwszy klient:** cywilny (infrastruktura krytyczna, straż graniczna) albo sojuszniczy finansowany przez darczyńcę; MON jako drugi. Konsekwencja: plan przychodów etapu C i klauzula spiralnej aktualizacji w umowach z MON (`aps.md` sekcja 10).
3. **Struktura:** P.S.A. w Polsce z estońskim CIT do wejścia osoby prawnej; klauzula anty-flipowa i klauzula współdziałania przy wymianie udziałów do UE/EOG w umowie akcjonariuszy; ścieżka exitu poza Kryterium z gwarancjami państwa (`jurisdictions/przeniesienie_i_podatki.md` sekcja 4; `milrem.md` sekcja 10).
4. **Kapitał:** inwestor kotwiczny z mandatem wielorundowym (NIF, PFR, ARP, Vinci, EIF) i prime z UE/NATO jako inwestor mniejszościowy bez wyłączności technologii; EBI i EBOR w planie po przychodzie; kapitał uprzywilejowany dopuszczony w umowie na późny etap (`shield_ai.md` sekcja 10).
5. **Kontrola:** Założyciele wybierają świadomie między drogą giełdową (rozwodnienie do 20–25 % łącznie, Creotech) a drogą kontroli (WB, APS: klient, dług, jeden inwestor mniejszościowy); od tego zależą progi § 32 i horyzont w umowie akcjonariuszy.
6. **Dane i bezpieczeństwo:** prawa do danych treningowych i telemetrycznych w każdym pilocie; polityka bezpieczeństwa systemów autonomicznych jako załącznik do data room i do oświadczeń w umowie inwestycyjnej (`figure_ai.md` sekcja 10; `nomagic.md` sekcja 10).
7. **Ukraina i bezpieczeństwo fizyczne:** obecność (biuro, Brave1) przed dużymi kontraktami, przez pakiety darczyńców; licencja eksportowa indywidualna; budżet ochrony po sabotażu u Milrem i liście celów Destinusa (`ukraina.md` sekcja 6).
8. **Rada:** dyrektor niewykonawczy z MON lub NATO od etapu C, zgodny z § 21 ust. 3 (`destinus.md`, `helsing.md` sekcja 10).

---

## 5. Czego case studies nie rozstrzygają

- Czy MON kupi autonomię jako osobną pozycję (odpowiednik A-GRA) — brak polskiego precedensu; SAN kupuje APS przez konsorcjum PGZ–Kongsberg.
- Czy fundusze PFR i NIF zaakceptują prime'a jako inwestora mniejszościowego w tej samej rundzie — nie odnaleziono przykładu.
- Jak polski UOKiK i MON potraktują exit do nabywcy spoza UE po wejściu w życie unijnego rozporządzenia FDI z czerwca 2026 r. — precedens estoński (Milrem) nie musi się powtórzyć.
- Realne mnożniki po zakończeniu cyklu hossy 2025–2026 r.; żadna z prywatnych spółek nie publikuje zbadanych wyników.
- Wszystkie liczby pochodzą ze streszczeń wyszukiwarki; przed użyciem poza firmą sprawdzić w dokumentach pierwotnych podlinkowanych w sekcji 12 każdego pliku.
