# Poza Kryterium: Szwajcaria, Izrael, Singapur, ZEA, Cypr i Malta

Dokument wewnętrzny Basilisk Systems, informacyjny. Nie jest opinią prawną ani podatkową i nie zmienia umowy spółki. Część katalogu `jurisdictions/` (przegląd: `README.md`; kryteria: `kryteria.md`). Odesłania do umowy według `psa.tex` w wersji 0.9.4-C.

Stan na 30 września 2026 r. Oznaczenia wiarygodności: **[Z]** — akt prawny, portal urzędowy albo publikacja kancelarii lub doradcy podatkowego; **[M]** — prasa, portal informacyjny albo doradca komercyjny; **[W]** — wiedza ogólna, do potwierdzenia; **[?]** — szacunek albo teza niepotwierdzona. Uwaga metodyczna: dla Singapuru, ZEA, Cypru i Malty nie odnaleziono w tej sesji żadnego źródła podatkowego; dane podatkowe w sekcji 4 są wiedzą ogólną [W] i wymagają sprawdzenia przed jakąkolwiek decyzją.

---

## 1. Werdykt

Żadna z sześciu jurysdykcji nie nadaje się na siedzibę główną ani spółkę bazową Basiliska. Cztery (Szwajcaria, Izrael, Singapur, ZEA) są poza UE, EOG i NATO, więc spółka-matka z nich narusza Kryterium § 11 i test kontroli EDF art. 9, a przez to zamyka EDF, SAFE, EDIP, DIANA i NIF. Cypr i Malta są w UE (spełniają Kryterium i test EDF), ale nie w NATO (bez DIANA i NIF), a ich zaletą jest wyłącznie arbitraż podatkowy, który u klienta obronnego i w kontroli FDI (NSI, CFIUS, polski UOKiK) obniża wiarygodność.

| Jurysdykcja | UE/EOG | NATO | Kryterium § 11 | EDF | Horizon | DIANA | NIF | SAFE | Rola możliwa |
|---|---|---|---|---|---|---|---|---|---|
| Szwajcaria | nie (EFTA, nie EOG) | nie | nie | nie | stowarzyszona od 2025 r. (przejściowo) | nie | nie | nie | spółka zależna tylko pod klienta szwajcarskiego; KMG i neutralność blokują Ukrainę |
| Izrael | nie | nie | nie | nie | stowarzyszony | nie | nie | nie | partner technologiczny, nie spółka |
| Singapur | nie | nie | nie | nie | nie | nie | nie | nie | brak |
| ZEA | nie | nie | nie | nie | nie | nie | nie | nie | brak; EDGE (właściciel Milrem) jako potencjalny klient albo nabywca |
| Cypr | UE | nie | tak | tak (państwo członkowskie) | tak | nie | nie | tak | holding technicznie możliwy, niezalecany |
| Malta | UE | nie | tak | tak | tak | nie | nie | tak | holding technicznie możliwy, niezalecany |

---

## 2. Szwajcaria

| Element | Treść | Wiar. |
|---|---|---|
| Członkostwa | poza UE, EOG i NATO; Horizon Europe: negocjacje zakończone w styczniu 2025 r., stowarzyszenie wsteczne od 1 stycznia 2025 r. po podpisaniu; przejściowo wnioski jak stowarzyszony | [M] |
| EDF | podmiot kontrolowany ze Szwajcarii to „podmiot kontrolowany przez niestowarzyszone państwo trzecie": kwalifikowalność tylko z gwarancjami zatwierdzonymi przez państwo członkowskie (art. 9 ust. 4), droga niepewna i powolna | [Z] |
| KMG (ustawa o materiałach wojennych) | sesja zimowa grudzień 2025 r.: dla 25 państw zachodnich zgoda eksportowa automatyczna nawet w konflikcie i bez deklaracji o niereeksporcie, z wetem Rady Federalnej; referendum do 17 kwietnia 2026 r. (wynik nieodnaleziony); dostawy i reeksport do Ukrainy nadal niemożliwe z powodu neutralności; klienci europejscy omijają szwajcarskich dostawców; jeden nagłówek AA twierdzi, że parlament dopuścił reeksport do Ukrainy — prawdopodobnie wcześniejsze głosowanie, nie ustawa | [M] |
| Podatki | CIT federalny 8,5 % ustawowo; łącznie 12–21 % zależnie od kantonu (Zug ok. 11,9 %); zwolnienie udziałowe; umowa z Polską — niezweryfikowane | [W] |
| SECO | licencje dual-use z ustawy o kontroli towarów — nieodnalezione | [?] |
| Wniosek | szwajcarska spółka-matka odziedziczyłaby limity neutralności: nic z listy materiałów wojennych nie trafi do Ukrainy; zamknięte EDF, DIANA, NIF | — |

## 3. Izrael

| Element | Treść | Wiar. |
|---|---|---|
| Członkostwa | poza UE, EOG i NATO; Horizon Europe stowarzyszony | [M] |
| DECA | Defense Export Control Agency w MO od 2006 r.; ustawa o kontroli eksportu obronnego z 2007 r.: licencja marketingowa do negocjacji i licencja eksportowa do wysyłki; obowiązki także pośredników; listy Wassenaar i MTCR; złagodzenie: negocjacje systemów jawnych z większością państw bez licencji marketingowej, ale bez umowy wiążącej przed zgodą DECA | [Z]/[M] |
| Podatki | CIT 23 %; Preferred Technological Enterprise 12 %/7,5 %; Angels Law; umowa z Polską 5 %/10 % — niezweryfikowane | [W] |
| Wniosek | druga warstwa licencyjna (marketing + eksport) nad regułami państwa klienta; izraelskie pochodzenie komplikuje niektóre zamówienia w UE (wnioskowanie polityczne); zamknięte EDF, DIANA, NIF | — |

## 4. Singapur, ZEA, Cypr i Malta

| Jurysdykcja | Co wiadomo z tej sesji | Dane podatkowe [W], do sprawdzenia |
|---|---|---|
| Singapur | poza UE, NATO i listą stowarzyszonych z Horizon; spółka-matka z Singapuru czyni polską spółkę podmiotem kontrolowanym przez państwo trzecie w EDF | CIT 17 % z częściowymi zwolnieniami; brak podatku od zysków kapitałowych i podatku u źródła od dywidend; umowa z Polską 5 %/10 %; licencje dual-use ze Strategic Goods (Control) Act |
| ZEA (ADGM, DIFC) | jak Singapur; EDGE Group (Abu Zabi) jest właścicielem Milrem Robotics (`estonia.md`) | CIT federalny 9 % od czerwca 2023 r. (0 % do 375 tys. AED), 0 % dla Qualifying Free Zone Person, 15 % minimalny podatek dla dużych grup od 2025 r.; usunięte z listy Annex II UE (2023 r.) i z szarej listy FATF (luty 2024 r.); umowa z Polską 0 %/5 %; kontrola eksportu obronnego przez Executive Office for Control and Non-Proliferation |
| Cypr | UE, nie NATO; spełnia test EDF „established in the Union"; nie jest LP NIF | CIT 12,5 % (projekt 15 %); IP box (80 % zwolnienia, ok. 2,5 % efektywnie); odliczenie odsetek nominalnych; brak podatku u źródła od dywidend do nierezydentów; non-dom dla założycieli; dyrektywa 0 % w Polsce z zastrzeżeniem pay-and-refund >2 mln zł i testu beneficjenta rzeczywistego |
| Malta | UE, nie NATO; konstytucyjna neutralność | CIT 35 % z refundacją 6/7 (ok. 5 % efektywnie); opcjonalny 15 % podatek końcowy od 2025 r.; pełna imputacja; zwolnienie udziałowe |

Uwaga: żadna z czterech nie była w tej sesji sprawdzona pod kątem listy jurysdykcji niechętnych współpracy UE; stan „nie na liście" jest przekonaniem, nie ustaleniem [W].

## 5. Skutki dla Basiliska

| Wniosek | Gdzie u nas | Stan | Co zrobić |
|---|---|---|---|
| Inwestor ze Szwajcarii, Izraela, Singapuru albo ZEA narusza § 11 bez wyjątku; po skreśleniu ust. 14 dotyczy to także funduszy z tych państw | § 11; `regulations.md` sekcja 3b | OK | nie negocjować z takimi funduszami przed zmianą umowy uchwałą 75 % |
| Cypryjski albo maltański holding spełnia § 11 i EDF, ale przy koncesji MSWiA, ŚBP i NSI/CFIUS obniża wiarygodność i podpada pod pay-and-refund oraz test beneficjenta rzeczywistego | `polska.md` sekcja 4; `przeniesienie_i_podatki.md` sekcje 3.1–3.4 | DEC | nie zakładać; jeśli inwestor wiodący wymaga holdingu w UE, wybrać Holandię (`holandia_luksemburg_irlandia.md`) |
| EDGE (ZEA) jako nabywca Milrem pokazuje, że kupiec spoza Kryterium może pojawić się przy exicie; § 11 wymaga wtedy uchwały 75 % | § 11; § 25 ust. 1 lit. e; `case_studies/README.md` | OK | opisać w umowie inwestycyjnej ścieżkę zgody na exit poza Kryterium |
| Izraelski albo szwajcarski partner technologiczny (nie właściciel) jest dopuszczalny; sprawdzać DECA i KMG w każdej umowie licencyjnej | `regulations.md` sekcja 3 | DEC | klauzula o kontroli eksportu w umowach partnerskich |

## 6. Luki do sprawdzenia

- Szwajcaria: wynik referendum KMG po 17 kwietnia 2026 r.; stawki kantonalne; SECO dla oprogramowania autonomii; umowa z Polską.
- Izrael: stawki PTE; Angels Law; umowa z Polską; praktyka DECA dla oprogramowania.
- Singapur, ZEA, Cypr, Malta: wszystkie dane podatkowe; status na liście UE; praktyka polskiego pay-and-refund dla holdingu cypryjskiego.
- Czy Ukraina i Kanada mogą być partnerami SAFE na innych warunkach niż EOG-EFTA (Kanada od 1 grudnia 2025 r. wg `kryteria.md`).

---

## 7. Źródła sprawdzone 30 września 2026 r.

- EDF art. 9 — https://defence-industry-space.ec.europa.eu/system/files/2024-05/EDF%20Tutorial%20-%20Ownership%20and%20control%20assessment%20(Info%20Days%202023).pdf ; https://defence-industry-space.ec.europa.eu/document/download/62c6bdf2-9e99-4632-a3eb-b4fed7bc31f8_en?filename=EDF+FAQ+v3.pdf ; https://www.defencefinancemonitor.com/p/edf-article-9-explained-foreign-control ; https://www.defencefinancemonitor.com/p/unlocking-edf-2026-navigating-article ; https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/edf/guidance/list-3rd-country-participation_edf_en.pdf ; https://www.iiss.org/globalassets/media-library---content--migration/files/research-papers/2024/10/euro-defence/iiiss_the-impact-of-the-european-defence-fund-on-cooperation-with-third-country-entities.pdf
- Szwajcaria — https://www.swissinfo.ch/eng/neutrality/switzerland-eases-arms-export-rules-as-its-industry-shunned-by-europe/90836288 ; https://www.terredeshommesschweiz.ch/en/war-material-act-swiss-weapons-to-unjust-states/ ; https://theswisstimes.ch/switzerland-easing-arms-re-exports-to-ukraine/ ; https://www.aa.com.tr/en/europe/swiss-parliament-allows-arms-re-export-to-ukraine/2916553 ; Horizon — https://futureneeds.eu/eligible-countries-for-horizon-europe-funding-the-complete-2025-guide/ ; https://era.gv.at/horizon-europe/international-cooperation/
- Izrael — https://exportctrl.mod.gov.il/en ; https://en.globes.co.il/en/article-israels-defense-ministry-eases-arms-export-rules-1001258720 ; https://www.goldfarb.com/pdf1/The%20Fundamentals%20of%20Defense%20Export%20Supervision%20-%20Obtaining%20a%20Marketing%20License.pdf ; https://www.goldfarb.com/pdf1/Will_the_Recent_Amendment_of_the_Defense_Export_Control_Law_Ease_the_Licensing_Process.pdf
- Członkostwa — https://www.nato.int/cps/en/natohq/news_217864.htm ; https://www.nif.fund/about/ ; https://eufundingportal.eu/horizon-europe-associated-countries/ ; https://pitchbook.com/profiles/company/268732-36
