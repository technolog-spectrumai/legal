# Jurysdykcje dla Basilisk Systems: siedziba, spółka zależna, spółka bazowa

Dokument wewnętrzny Basilisk Systems, informacyjny. Nie jest opinią prawną ani podatkową i nie zmienia umowy spółki. Katalog `jurisdictions/` porównuje państwa, w których Basilisk może mieć siedzibę główną, spółkę zależną albo spółkę bazową (holding). Odesłania do umowy według `psa.tex` w wersji 0.9.4-C (numery § według `spis_tresci.md`). Katalog odpowiada na pytanie U.5 z `law_uzup.md`, przygotowuje decyzję D1 z memorandum i uzupełnia `regulations.md` (sekcje 3, 3a, 3b), `vc.md` (sekcje 3, 4, 9), `psa_todo.md` (sekcja 1) i `case_studies/README.md` (sekcja 5).

Stan na 30 września 2026 r. Oznaczenia wiarygodności: **[Z]** — akt prawny, portal urzędowy albo publikacja kancelarii lub doradcy podatkowego; **[M]** — prasa, portal informacyjny albo doradca komercyjny; **[W]** — wiedza ogólna, do potwierdzenia; **[?]** — szacunek albo teza niepotwierdzona. Uwaga metodyczna: strony źródłowe były w tej sesji niedostępne do pełnego odczytu (blokada sieciowa); fakty pochodzą ze streszczeń wyszukiwarki, a szereg stawek podatkowych i traktatowych jest oznaczony jako luka w plikach szczegółowych.

---

## 1. Główny wniosek

Basilisk powinien powstać jako P.S.A. w Polsce i zostać polską spółką-matką co najmniej do rundy A. Polska jest jedyną jurysdykcją, która daje jednocześnie: PFR, Vinci, Ścieżkę SMART, koncesję MSWiA, świadectwo bezpieczeństwa przemysłowego, zamówienia MON finansowane z 43,7 mld EUR SAFE, DIANA (Fort Kraków), NIF, EDF, EIC i estoński CIT dla P.S.A. z samymi osobami fizycznymi. Żadne inne państwo nie oferuje niczego, czego Polska nie ma, poza (a) większym rynkiem VC (USA, UK, Niemcy, Francja), (b) głębszym państwowym współinwestowaniem w defence (Francja: Definvest i FID; Holandia: SecFund; Estonia: SmartCap i EIS; Litwa: MILInvest) i (c) ulgami holdingowymi (Holandia, Luksemburg, Estonia, Łotwa). Każde z tych dóbr da się pozyskać spółką zależną w danym państwie (§ 33), bez przenoszenia matki.

Spółka-matka poza UE/EOG (USA, UK, Szwajcaria, Izrael, Singapur, ZEA) narusza Kryterium § 11 i test kontroli EDF art. 9, zamyka SAFE, EDIP i EIC oraz kosztuje 19 % PIT od wartości akcji założycieli przy flipie (wymiana udziałów neutralna tylko do nabywcy z UE/EOG). Spółka-matka w innym państwie UE/EOG (Holandia, Estonia, Finlandia) jest legalnie neutralna, ale odbiera estoński CIT i „polski nexus" PFR i wymaga realnego zarządu na miejscu (art. 3 ust. 1a CIT, art. 30f PIT). Dlatego zmiana matki ma sens wyłącznie na żądanie inwestora prowadzącego rundę i tylko do spółki z UE/EOG (`przeniesienie_i_podatki.md` sekcja 4).

---

## 2. Pliki

| Plik | Zakres | Werdykt w skrócie |
|---|---|---|
| `kryteria.md` | trzy role, kryteria K1–K12, macierz kwalifikowalności programów (EDF, SAFE, EDIP, EIC, DIANA, NIF, PFR, Vinci, SMART, koncesja, ŚBP, MON) | narzędzie oceny; każdy plik krajowy jest oceniany tymi kryteriami |
| `polska.md` | P.S.A., podatki 2026, koncesja MSWiA, ŚBP, kontrola eksportu, PFR, Vinci, SMART, DIANA, NIF, SAFE | siedziba: tak, wariant bazowy; spółka zależna: obowiązkowa przy matce za granicą; holding: możliwy, nie dla kapitału z USA |
| `przeniesienie_i_podatki.md` | wymiana udziałów, exit tax, CFC, miejsce zarządu, przekształcenie transgraniczne, FDI, IP; trzy scenariusze zmiany matki | flip poza UE/EOG opodatkowany 19 %; kolejność: P.S.A. → spółki zależne → matka w UE/EOG na żądanie inwestora → Delaware tylko przy rezygnacji z UE → przekształcenie transgraniczne ostatnie |
| `niemcy_francja.md` | GmbH/UG i SAS, Forschungszulage i CIR, BAFA/KrWaffKG i AFCI, CIHBw, Definvest, FID, SAFE Francji | oba: siedziba możliwa, ale droga; spółka zależna pod Bundeswehrę albo DGA; holding nie |
| `holandia_luksemburg_irlandia.md` | BV, S.à r.l., Ltd; innovation box, IP box, KDB; Vifo, WWM; SecFund; zwolnienia holdingowe | Holandia: siedziba możliwa i standardowy holding; Luksemburg: tylko holding albo IP; Irlandia: nie dla firmy obronnej (nie-NATO) |
| `estonia.md` | OÜ przez e-Residency, 0 %/22 % CIT, brak podatku u źródła, opcje po 3 latach; Komisja ds. Towarów Strategicznych; SmartCap, EIS, DIANA Tallinn i Tartu; klaster dronowy; ukraińskie firmy w Estonii | siedziba bez przewagi nad Polską; spółka zależna: tak, druga po Niemczech i Francji; holding: możliwy, ale prosty i bez PFR |
| `finlandia_nordyki.md` | Oy, AB, ApS, AS; podatki, licencje (MO Finlandii, ISP, Ministerstwo Sprawiedliwości Danii, MSZ Norwegii); Business Finland, Tesi, Vinnova, Defence Tech Denmark, EIFO, Innovation Norway; DIANA i SAFE | Finlandia: siedziba możliwa, spółka zależna tak; Szwecja, Dania, Norwegia: tylko spółka zależna pod kontrakt; Norwegia poza UE, ale w EOG i stowarzyszona z EDF |
| `czechy_baltowie.md` | s.r.o., UAB, SIA; CIT 21/17/0-20 %; ustawa 38/1994, licencje Litwy i Łotwy (test obywatelstwa); MILInvest, Coinvest, LIAA/Altum; DIANA test centra; SAFE 2,06/6,38/3,50 mld EUR | Czechy: rynek zbytu przez CSG, nie miejsce spółki; Litwa: najtańsza spółka zależna w regionie; Łotwa: tylko pod kontrakt z lokalnym partnerem |
| `wielka_brytania.md` | Ltd za 100 GBP, CT 25 %, scalona ulga B+R, EMI (niedostępne dla spółki zależnej), SSE; ECJU/SPIRE, FSC (brytyjscy dyrektorzy), NSI Act; SDR 2025, UKDI, NSSIF, DIANA HQ, NIF; SAFE odrzucone | siedziba nie (poza UE/EOG); spółka zależna pod MOD, UKDI, NSSIF; holding nie |
| `usa.md` | Delaware C-corp, Teksas SB 29; § 174A, QSBS; ITAR, EAR 9A012, deemed export, CFIUS, FOCI (SCA/SSA/Proxy), SBIR, DIU/OTA, Blue UAS; H-1B 100 tys. USD, E-2; ICEYE US i WB America | flip nie w fazie A–C; spółka zależna z FOCI pod Department of War; holding nie |
| `ukraina.md` | TOV, Defence City (ustawa 4577-IX), limit dywidend 1 mln EUR/mies., Brave1, „Build with Ukraine", kontrolowany eksport; WB Ukraina | siedziba nie; spółka zależna do integracji i testów po pierwszym kontrakcie; holding nie |
| `poza_kryterium.md` | Szwajcaria (KMG, neutralność), Izrael (DECA), Singapur, ZEA, Cypr, Malta | żadna nie nadaje się na siedzibę ani holding; Cypr i Malta spełniają Kryterium (UE), ale nie NATO i obniżają wiarygodność |

---

## 3. Macierz członkostw i kwalifikowalności

| Państwo | UE | EOG | NATO | Kryterium § 11 | EDF | SAFE (alokacja) | EIC | DIANA | NIF (LP) | Wiar. |
|---|---|---|---|---|---|---|---|---|---|---|
| Polska | tak | tak | tak | tak | tak | 43,7 mld EUR | tak | akcelerator Fort Kraków | tak | [Z] |
| Niemcy | tak | tak | tak | tak | tak | bez wniosku | tak | akcelerator Palladion (Monachium) | tak | [Z] |
| Francja | tak | tak | tak | tak | tak | 15,09 mld EUR | tak | nieodnalezione | nie | [Z]/[?] |
| Holandia | tak | tak | tak | tak | tak | bez pożyczek [W] | tak | nieodnalezione | tak (siedziba NIF w Amsterdamie [W]) | [Z]/[?] |
| Luksemburg | tak | tak | tak | tak | tak | bez pożyczek [W] | tak | nie | tak | [Z]/[?] |
| Irlandia | tak | tak | nie | tak (UE) | tak (udział do sprawdzenia) | ? | tak | nie | nie | [Z]/[?] |
| Estonia | tak | tak | tak | tak | tak | 2,34 mld EUR | tak | akcelerator Tallinn i Tartu, hub regionalny | tak | [Z] |
| Finlandia | tak | tak | tak (2023) | tak | tak | 1,0 mld EUR | tak | akcelerator VTT Otaniemi, 2 test centra | tak | [Z] |
| Szwecja | tak | tak | tak (2024) | tak | tak | bez pożyczek | tak | akcelerator LEAD (od maja 2026 r.) | tak | [Z] |
| Dania | tak | tak | tak | tak | tak | 46,8 mln EUR | tak | akcelerator BII (Kopenhaga) | tak | [Z] |
| Norwegia | nie | tak | tak | tak (EOG) | tak (jedyny stowarzyszony) | partner wspólnych zamówień, bez pożyczek | tak (stowarzyszona) | firmy w kohorcie, FFI; akcelerator niepotwierdzony | tak | [Z] |
| Czechy | tak | tak | tak | tak | tak | 2,06 mld EUR | tak | nieodnalezione | tak | [Z]/[?] |
| Litwa | tak | tak | tak | tak | tak | 6,38 mld EUR | tak | 6 test centrów | tak | [Z] |
| Łotwa | tak | tak | tak | tak | tak | 3,50 mld EUR | tak | test centrum Ādaži | tak | [Z] |
| Wielka Brytania | nie | nie | tak | tak (NATO) | nie | nie (rozmowy zerwane 28 listopada 2025 r.) | bez EIC Fund | HQ Londyn, miejsca Imperial | tak | [Z] |
| USA | nie | nie | tak | tak (NATO) | nie | nie | nie | Seattle, Boston | nie | [Z] |
| Ukraina | nie | nie | nie | nie | nie | partner wspólnych zamówień | tak (stowarzyszona) | nie | nie | [Z]/[?] |
| Szwajcaria | nie | nie (EFTA) | nie | nie | nie | nie | tak (od 2025 r.) | nie | nie | [M] |
| Izrael | nie | nie | nie | nie | nie | nie | tak (stowarzyszony) | nie | nie | [M] |
| Singapur, ZEA | nie | nie | nie | nie | nie | nie | nie | nie | nie | [W] |
| Cypr, Malta | tak | tak | nie | tak (UE) | tak | tak (państwa członkowskie) | tak | nie | nie | [Z]/[W] |

Kryterium § 11: inwestor musi być z UE, EOG albo NATO (bez wyjątku dla funduszy po skreśleniu ust. 14). EDF art. 9: brak kontroli przez państwo trzecie niestowarzyszone; NATO nie wystarcza (UK, USA nie kwalifikują się). SAFE: siedziba w UE, EOG-EFTA albo Ukrainie, 65 % komponentów. DIANA: siedziba i większość w rękach obywateli państw NATO. Szczegóły w `kryteria.md` sekcja 3.

---

## 4. Porównanie według roli

### 4.1 Siedziba główna

| Państwo | Ocena | Za | Przeciw |
|---|---|---|---|
| Polska | **wariant bazowy** | wszystkie programy bez pośredników; estoński CIT; program motywacyjny z art. 24 ust. 12b PIT; IP Box 5 %; B+R 200 % | P.S.A. nienotowalna (art. 300³⁶ § 2 KSH); 19 % przy wniesieniu IP; VC 3,4 mld zł; brak funduszu z biletem klasy Definvest |
| Holandia | możliwa | BV za 0,01 EUR, innovation box 9 %, WBSO 50 % dla startujących, SecFund do 5 mln EUR, EDF, DIANA, NIF | notariusz; brak PFR i SMART; substancja po orzecznictwie TSUE |
| Finlandia | możliwa | CIT 20 % (18 % od 2027 r. w projekcie), Oy bez kapitału, 85 % nordyckiego VC defence, Business Finland 120 mln EUR, DIANA Otaniemi | FDI obejmuje inwestorów z UE; ≥1 członek zarządu z EOG; brak PFR |
| Estonia | możliwa, bez przewagi | 0 %/22 % jak estoński CIT w Polsce; e-Residency; SmartCap; EIS; DIANA hub | zarząd z Polski = rezydencja w Polsce; brak PFR; mały rynek |
| Niemcy | droga | Forschungszulage 35 %, największy budżet, CIHBw, Palladion | CIT ok. 29,8 %, FDI od 10 % także dla UE, notariusz |
| Francja | możliwa | SAS 1 EUR, CIR 30 %, JEI, BSPCE, Definvest 0,5–10 mln EUR, FID, SAFE 15,09 mld EUR | nie LP NIF; AFCI; brak PFR |
| Litwa | możliwa, bez przewagi | CIT 17 %, 300 % B+R, opcje po 3 latach, UAB w 1–3 dni, MILInvest | mały rynek VC; brak PFR |
| Szwecja, Dania, Norwegia, Czechy, Łotwa | nie | — | licencje (ISP, Ministerstwo Sprawiedliwości, MO Łotwy z testem obywatelstwa), koszt talentu, brak przewagi |
| Luksemburg, Irlandia | nie | — | Luksemburg bez przemysłu; Irlandia nie-NATO |
| UK, USA | nie (poza UE/EOG) | EMI, SEIS/EIS, VC 2,9 mld USD (UK); QSBS, § 174A, Anduril 61 mld USD (USA) | Kryterium § 11 i EDF naruszone; SAFE i EIC zamknięte; flip 19 % PIT |
| Ukraina, Szwajcaria, Izrael, Singapur, ZEA, Cypr, Malta | nie | — | poza Kryterium (poza Cyprem i Maltą); bez DIANA i NIF; reputacja |

### 4.2 Spółka zależna (kolejność według wartości dla Basiliska)

| Kolejność | Państwo | Kiedy | Co daje | Warunek |
|---|---|---|---|---|
| 1 | Niemcy | kontrakt Bundeswehry albo JV z Rheinmetall/Helsing | CIHBw, Palladion, Forschungszulage, SPRIND | FDI od 10 % dla każdego inwestora; BAFA |
| 2 | Francja | kontrakt DGA albo JV z KNDS/MBDA/Safran | Definvest, FID, CIR 30 % | AFCI dla materiałów kategorii A2 |
| 3 | Estonia | kontrakt z Siłami Obronnymi Estonii albo umowy z Brave1 | EIS 250 tys.–3 mln EUR, SmartCap 0,5–10 mln EUR, DIANA hub, klaster dronowy | lokalny zarząd i biuro (art. 3 ust. 1a CIT) |
| 4 | USA | kontrakt Department of War | DIU CSO/OTA, DIANA, rynek | FOCI (SSA/Proxy) dla prac niejawnych; deemed export; nie SBIR |
| 5 | Wielka Brytania | kontrakt MOD | UKDI, NSSIF, fundusz 20 mln GBP, DIANA HQ, AUKUS | FSC wymaga brytyjskich dyrektorów; EMI niedostępne; NSI >25 % |
| 6 | Finlandia | kontrakt Puolustusvoimat albo partnerstwo z ICEYE | Business Finland, Tesi, DIANA Otaniemi | zgoda FDI także dla inwestora z UE |
| 7 | Litwa | kontrakt z MON Litwy | MILInvest, Coinvest, 6 test centrów DIANA, SAFE 6,38 mld EUR | sprawdzić, czy MILInvest przyjmuje spółki z zagranicznym właścicielem |
| 8 | Holandia | konsorcjum EDF albo RNLAF | SecFund do 5 mln EUR | Vifo, WWM |
| 9 | Ukraina | pierwszy grant Brave1 albo kontrakt | Brave1, Defence City, testy bojowe | TOV jako centrum kosztów; limit dywidend; licencja eksportowa z Polski |
| 10 | Czechy, Szwecja, Dania, Norwegia, Łotwa | wyłącznie pod konkretny kontrakt | rynek | licencje krajowe; Łotwa: test obywatelstwa wspólników |

### 4.3 Spółka bazowa (holding)

| Państwo | Ocena | Uwagi |
|---|---|---|
| Polska (P.S.A. jako matka) | wariant bazowy | traci estoński CIT po wejściu osoby prawnej; brak ogólnego zwolnienia zysków ze zbycia udziałów poza art. 24o CIT [W] |
| Holandia | standard, gdy inwestor wiodący wymaga holdingu w UE | deelnemingsvrijstelling, umowa z 2020 r. (0 % przy 10 % przez 24 miesiące [W]), substancja po TSUE |
| Luksemburg | tylko dla grup notowanych albo IP | zwolnienie 10 %/1,2 mln EUR/12 m/8,5 %, IP box 4,774 %; koszt 3–8 tys. EUR |
| Estonia, Łotwa | technicznie proste | 0 % od zysku zatrzymanego, brak podatku u źródła; bez PFR i bez substancji podpadają pod CFC |
| Szwecja | atrakcyjna podatkowo | näringsbetingade andelar; bez powodu biznesowego |
| Cypr, Malta | niezalecane | UE, ale nie NATO; pay-and-refund i test beneficjenta; wiarygodność u klienta obronnego |
| UK, USA, Szwajcaria, Izrael, Singapur, ZEA | nie | kontrola spoza UE/EOG; flip opodatkowany 19 % |

---

## 5. Kluczowe liczby 2026

| Państwo | Forma i kapitał | CIT | Podatek u źródła do polskiej matki | Ulga B+R / IP | Opcje pracownicze | Licencja obronna |
|---|---|---|---|---|---|---|
| Polska | P.S.A. 1 zł | 19 %/9 %; estoński 10/20 % | — | B+R 200 %, IP Box 5 % | art. 24 ust. 11–12b PIT | koncesja MSWiA; ŚBP; ZG-PL-U-1 |
| Niemcy | GmbH 25 tys. EUR, UG 1 EUR | ok. 29,8 % (spadek od 2028 r.) | 0 % dyrektywa; 5/15 % umowa [?] | Forschungszulage 25/35 % | § 19a EStG | BAFA; KrWaffKG; FDI 10 % |
| Francja | SAS 1 EUR | 25 % | 0 % dyrektywa; 5/15 % [?] | CIR 30 %, CII 20 %, JEI | BSPCE | AFCI; CIEEMG |
| Holandia | BV 0,01 EUR | 19 %/25,8 % | 0 % (10 %, 24 m) [W] | innovation box 9 %, WBSO 36/50 % | ? | WWM; Vifo |
| Luksemburg | S.à r.l. 12 tys. EUR | 23,87 % | 0 % [W] | IP box 4,774 % | ? | OCEIT |
| Irlandia | Ltd 1 EUR | 12,5 % | 0 % [W] | KDB 10 %, ulga 35 % | KEEP do 2028 r. | DETE |
| Estonia | OÜ 0,01 EUR | 0 %/22 % (22/78) | 0 % | brak | zwolnienie po 3 latach | Komisja MSZ (Stratlink) |
| Finlandia | Oy 0 EUR | 20 % (18 % w projekcie 2027) | 0 % dyrektywa; 15 % umowa | +50 % (maks. 500 tys. EUR); 150 % podwykonawstwo | ? | MO; FDI także UE |
| Szwecja | AB 25 tys. SEK | 20,6 % [W] | 5 % (≥25 %) / 15 % | składki; 200 % w projekcie | QESO | ISP produkcja i dostawa |
| Dania | ApS 20 tys. DKK | 22 % [W] | 0/5/15 % | 114 → 120 % | ? | Ministerstwo Sprawiedliwości; licencja dla nabywcy zagranicznego |
| Norwegia | AS 30 tys. NOK | 22 % [W] | 0 % (10 %, 24 m) | SkatteFUNN 19 % | ? | MSZ (własna ustawa) |
| Czechy | s.r.o. 1 CZK | 21 % | 5 % [?] | 150 % do 50 mln CZK | reforma 2026 [?] | MPO (38/1994); FDI 10 % |
| Litwa | UAB 1 tys. EUR | 17 %/7 % | 0 % (10 %, 12 m) / 15 % | 300 %; IP 5 % (7 %?) | zwolnienie po 3 latach | MGiI ≤25 dni |
| Łotwa | SIA 2,8 tys. EUR | 0 %/20 % (20/80) | 0 % | brak | ? | MO z testem obywatelstwa; 9 lat |
| Wielka Brytania | Ltd, 100 GBP | 25 %/19 % [W] | 0 % (brak podatku u źródła) | scalona 20 % (netto 15 %); ERIS | EMI (nie dla spółki zależnej) | ECJU/SPIRE; FSC; NSI |
| USA | Delaware C-corp, 109 USD | 21 % + stanowy | 5/15 % umowa 1974 r. [?] | § 174A; QSBS | ISO/NSO | ITAR/EAR; CFIUS; FOCI |
| Ukraina | TOV [?] | 18 %; Defence City 0 % przy reinwestycji [W] | limit 1 mln EUR/mies. | Defence City | ? | SSECU [?] |

Znak zapytania oznacza brak źródła w tej sesji; pliki krajowe wymieniają luki.

---

## 6. Scenariusze i rekomendacja

| Scenariusz | Struktura | Kiedy | Konsekwencje |
|---|---|---|---|
| S0 (bazowy) | P.S.A. w Polsce, estoński CIT, IP w Spółce (§ 26), ESOP (§ 27) | od zawiązania do rundy A | wszystkie programy; brak notowania (konwersja w S.A. przy IPO, § 25 ust. 1 lit. e) |
| S1 | S0 + spółki zależne według rynku (§ 33): DE/FR/EE/US/UK/FI/LT/NL/UA | po pierwszym kontrakcie w danym państwie | każda spółka zależna z lokalnym zarządem; SPV/JV po § 33 wymaga decyzji WZ; rundy tylko na poziomie P.S.A. |
| S2 | matka w UE/EOG (Holandia, Estonia, Finlandia) przez pierwszą większościową wymianę udziałów, P.S.A. jako spółka zależna | wyłącznie na żądanie inwestora prowadzącego rundę A lub B | neutralna podatkowo dla Założycieli (art. 24 ust. 8b pkt 3); utrata estońskiego CIT i „polskiego nexusa" PFR; SMART, koncesja i MON przez P.S.A. |
| S3 | flip do Delaware | tylko gdy plan finansowania porzuca programy UE i runda pokrywa 19 % PIT | Kryterium § 11 wymaga zmiany umowy (75 %); zamknięte EDF, SAFE, EIC; CFIUS przy inwestycjach w spółkę amerykańską |
| S4 | przekształcenie transgraniczne P.S.A. (art. 580¹–580¹⁷ KSH) | ostatnia opcja, gdy polska siedziba nie jest potrzebna do żadnego instrumentu | exit tax od IP, opinia Szefa KAS, 4–7 miesięcy |

Rekomendacja do D1 i U.5: **S0 od dnia zawiązania, S1 od etapu C, S2 tylko na żądanie inwestora i tylko do UE/EOG, S3 i S4 poza planem.** W umowie akcjonariuszy (etap C, pkt 26 w `plan_prac.md`) zapisać: współdziałanie przy wymianie udziałów do spółki z UE/EOG na żądanie inwestora rundy A, warunek neutralności podatkowej dla Założycieli, zakaz flipu poza UE/EOG bez zgody 75 % i bez pokrycia podatku, oraz zasadę, że IP i wnioski o programy UE zostają w spółce z UE (`przeniesienie_i_podatki.md` sekcja 4).

---

## 7. Mapowanie na dokumenty Basiliska

| Ustalenie katalogu | Gdzie w naszych dokumentach | Stan | Co zrobić |
|---|---|---|---|
| Kryterium § 11 (UE/EOG/NATO) wyklucza inwestorów ze Szwajcarii, Izraela, Singapuru, ZEA i Ukrainy, także fundusze (skreślony ust. 14); dopuszcza UK i USA | § 11; `regulations.md` sekcja 3b | OK | zachować; przy inwestorze spoza UE/EOG pilnować testu kontroli EDF art. 9 |
| Spółka zależna i SPV wymagają zgody WZ | § 33; § 25 ust. 1 | OK | dopisać do umowy inwestycyjnej listę państw dopuszczonych bez odrębnej zgody (UE/EOG/NATO) [?] |
| Zabezpieczenia na IP i obligacje zamienne wymagają WZ, co chroni przed cichym przeniesieniem IP do holdingu | § 31 ust. 4; § 26 | OK | nic |
| Próg 500 000 zł dla zgód WZ obejmuje dokapitalizowanie spółek zależnych | § 25 ust. 1 lit. k | OK | nic |
| ESOP w P.S.A. powinien objąć pracowników spółek zależnych (EMI w UK niedostępne, opcje w Estonii i na Litwie tylko dla lokalnych spółek) | § 27; art. 24 ust. 11–12b PIT | CZ | sprawdzić brzmienie § 27 pod kątem pracowników spółek zależnych [W] |
| Flip poza UE/EOG jest opodatkowany 19 %; wymiana udziałów neutralna tylko do UE/EOG i tylko pierwsza | `przeniesienie_i_podatki.md` sekcja 3.1; `psa_todo.md` sekcja 1 | DEC | D1: siedziba w Polsce; klauzula anty-flipowa w umowie akcjonariuszy |
| Estoński CIT przepada z dniem wejścia osoby prawnej, wstecznie za rok (art. 28l ust. 1 pkt 4 lit. a) | `polska.md` sekcja 4; `psa_todo.md` sekcja 6 | OK | wyjść z estońskiego CIT przed zamknięciem rundy z funduszem |
| Terminy 2026: EIC dual-use do 28 października; SMART 29 października – 29 grudnia; Defence Tech Denmark 1 października; EDF 2026 zamknięty 29 września | `psa_todo.md` sekcja 6; `plan_prac.md` etap C pkt 21–27 | BRAK | wpisać do harmonogramu finansowania |
| Kolejność spółek zależnych (DE, FR, EE, US, UK, FI, LT, NL, UA) | `plan_prac.md` etap C; `vc.md` sekcja 9 | BRAK | dopisać jako plan ekspansji po pierwszym kontrakcie |

---

## 8. Luki wspólne dla katalogu

- Stawki traktatowe Polska–każde państwo z tekstów umów; PwC Poland WHT i GOV.UK/HMRC były zablokowane.
- Stawki CIT Szwecji, Danii, Norwegii i UK (19 %) u źródła; dane podatkowe Szwajcarii, Izraela, Singapuru, ZEA, Cypru i Malty w całości.
- Reżimy opcji w Holandii, Luksemburgu, Finlandii, Danii, Norwegii i Łotwie.
- Miejsca DIANA we Francji, Holandii, Czechach i Norwegii; akceleratory na Litwie i Łotwie.
- Udział Irlandii, Holandii i Luksemburga w SAFE; warunki udziału Ukrainy i Kanady.
- Klasyfikacja oprogramowania sterującego rojem (ML21/ML22 vs 4D/4E; USML VIII/XI vs 9D610) w każdym reżimie; to decyduje, który krajowy system licencyjny obejmuje Basiliska.
- Czy fundusze krajowe (MILInvest, SmartCap, SecFund, Definvest, Business Finland) przyjmują spółki zależne z zagraniczną matką z UE.
- Wynik referendum KMG w Szwajcarii; numer i data ustawy reautoryzującej SBIR; raport NSI 2025–26.

---

## 9. Co dalej

1. Decyzja D1 (siedziba w Polsce) na podstawie `polska.md` i `przeniesienie_i_podatki.md`; klauzula anty-flipowa i klauzula współdziałania przy wymianie udziałów do umowy akcjonariuszy (etap C, pkt 26).
2. Uzupełnić `psa_todo.md` sekcję 6 o terminy 2026 z sekcji 7 i kolejność spółek zależnych z sekcji 4.2.
3. Zamówić u doradcy podatkowego stawki traktatowe i potwierdzenie art. 24 ust. 8b pkt 3 (pierwsza wymiana) dla scenariusza S2.
4. Klasyfikacja eksportowa oprogramowania (Polska: ZG-PL-U-1 i lista wojskowa; USA: commodity jurisdiction) przed pierwszą umową zagraniczną.
5. Kolejny katalog case studies (`case_studies/`, gałąź `vc2`): firmy defence tech, robotyka i physical AI z państw spoza tego katalogu wymagają dopisania profili jurysdykcji tutaj.

---

## 10. Źródła

Źródła są wymienione w każdym pliku krajowym w sekcji „Źródła sprawdzone 30 września 2026 r.". Wspólne dla katalogu:
- NIF (24 LP) — https://www.nif.fund/about/
- DIANA 2026 — https://www.diana.nato.int/connect/kicking-off-nato-dianas-2026-programme.html ; https://www.diana.nato.int/about-diana/location.html
- EDF art. 9 i lista państw — https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/edf/guidance/list-3rd-country-participation_edf_en.pdf ; https://www.defencefinancemonitor.com/p/edf-article-9-explained-foreign-control
- SAFE — https://defence-industry-space.ec.europa.eu/eu-defence-industry/safe-security-action-europe_en ; https://www.grosswald.org/safe-defence-loans-tracker/ ; https://defence-industry-space.ec.europa.eu/commission-approves-second-wave-safe-defence-funding-eight-member-states-2026-01-26_en
- EIC dual-use — https://eic.ec.europa.eu/news/european-innovation-council-opens-defence-and-dual-use-technologies-2026-06-17_en
- Horizon Europe (stowarzyszenia) — https://futureneeds.eu/eligible-countries-for-horizon-europe-funding-the-complete-2025-guide/
