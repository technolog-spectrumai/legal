# Źródła do pobrania — stan na 30 września 2026 r.

Katalog `src/legal/` po porządkach: akty krajowe `pl_*.txt` (komplet), `eu/` (EDF PL+EN; w wersji EN także 2021/821 skonsolidowane na 26.05.2023, 269/2014, 2019/947, AI Act, 2026/877 i nowe 2026/1386), `pfr/` (9 stron, bez dokumentów), `web/` (15 stron), `nif_report_2026.txt`, `MANIFEST.txt`. Usunięte jako bez treści: 13 pustych `eu_*.html`, 5 stron 404 `sn_*.txt`, `web_prs_info.txt`, `web_bvca_model_docs.txt` (404), `web_pfrv_feng_dokumentacja.txt` i `web_pfrv_otwarte_innowacje.txt` (sama zapora cookie; zastąpione przez `pfr/`), puste `pl_2026_176_ksh_nowelizacja.html` i `pl_2026_471_obrot_strategiczny_nowela.html` (są `.txt`).

Po każdym pobraniu: `python tools/extract_text.py` (z katalogu `src/`) zamienia PDF, HTML i DOCX na `.txt` obok, oryginały idą do `bkp/` (poza repozytorium). Zapis ręczny z przeglądarki: Ctrl+S, „tylko HTML”, pod nazwą z tabeli. Skrypty: `tools/download_eu.py` (UE, SN, strony z zaporą), `tools/pfr.py` (strony i dokumenty PFR), `tools/download.sh` (ELI/ISAP).

## 1. Prawo Unii (rozporządzenia stosowane bezpośrednio, nie wymagają transpozycji) — `eu/`

Do czego: tezy memorandum oznaczone [W]; bez tych tekstów nie da się ich podnieść do [Z]. Dla 2021/821, 269/2014 i 833/2014 wybierz na stronie aktu zakładkę „Aktualna wersja skonsolidowana” (wielokrotnie zmieniane), nazwa pliku ta sama.

| Plik | Adres | Do czego (memorandum) |
|---|---|---|
| `eu/eu_12016E_TXT_tfue_PL.html` | https://eur-lex.europa.eu/legal-content/PL/TXT/HTML/?uri=CELEX:12016E/TXT | art. 49, 63, 65, 346 TFUE: dopuszczalność Kryterium (1.1.1, T6). Uwaga: zapisana wcześniej strona „Traktat o funkcjonowaniu Unii Europejskiej _ EUR-Lex” była streszczeniem (9 kB), nie tekstem — potrzebny adres z `TXT/HTML` |
| `eu/eu_12016E_TXT_tfue_EN.html` | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:12016E/TXT | wersja EN do terminów w dokumentach NATO/VC |
| `eu/eu_32019R0452_fdi_screening_PL.html` | https://eur-lex.europa.eu/legal-content/PL/TXT/HTML/?uri=CELEX:32019R0452 | mechanizm współpracy przy kontroli inwestycji (1.1.2, 1.4.1); obowiązuje do 16.01.2028 |
| `eu/eu_32026R1386_fdi_screening_2026_PL.html` | https://eur-lex.europa.eu/legal-content/PL/TXT/HTML/?uri=CELEX:32026R1386 | **nowe** rozporządzenie 2026/1386 o kontroli inwestycji zagranicznych (uchyla 2019/452 od 17.01.2028; część przepisów od 16.07.2026) — wersja EN już jest (`eu_32026R1386_fdi_screening_2026_EN.txt`) |
| `eu/eu_32021R0821_dual_use_PL.html` | https://eur-lex.europa.eu/legal-content/PL/TXT/HTML/?uri=CELEX:32021R0821 | załącznik I (9A012, 9D/9E, 5A002), art. 4 catch-all (4.2.1–4.2.2); ustawa o obrocie strategicznym odsyła do niego po poz. 471. Jest EN skonsolidowane na 26.05.2023 — do klasyfikacji produktu potrzebna najnowsza konsolidacja (załącznik I zmieniany co roku) |
| `eu/eu_32026R0877_ttber_2026_PL.html` (EN jest) | https://eur-lex.europa.eu/legal-content/PL/TXT/HTML/?uri=CELEX:32026R0877 | klauzula licencji i ulepszeń § 33 ust. 3 (2.4.1) |
| ~~`eu/eu_32026R0877_ttber_2026_EN.html`~~ (jest) | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32026R0877 | j.w., wersja EN |
| `eu/eu_32014R0316_ttber_2014_PL.html` | https://eur-lex.europa.eu/legal-content/PL/TXT/HTML/?uri=CELEX:32014R0316 | porównanie (wygasło 30.04.2026) |
| `eu/eu_32024R1689_ai_act_PL.html` (EN jest) | https://eur-lex.europa.eu/legal-content/PL/TXT/HTML/?uri=CELEX:32024R1689 | wyłączenie wojskowe art. 2 ust. 3, terminy (T1) |
| `eu/eu_32024R2847_cra_PL.html` | https://eur-lex.europa.eu/legal-content/PL/TXT/HTML/?uri=CELEX:32024R2847 | produkty z elementami cyfrowymi, terminy (T1) |
| `eu/eu_32023R1230_maszynowe_PL.html` | https://eur-lex.europa.eu/legal-content/PL/TXT/HTML/?uri=CELEX:32023R1230 | platformy autonomiczne (T1) |
| `eu/eu_32018R1139_easa_1139_PL.html` | https://eur-lex.europa.eu/legal-content/PL/TXT/HTML/?uri=CELEX:32018R1139 | BSP cywilne vs wojskowe, art. 2 ust. 3 (T1, 4.2.1) |
| `eu/eu_32019R0945_uas_945_PL.html` | https://eur-lex.europa.eu/legal-content/PL/TXT/HTML/?uri=CELEX:32019R0945 | BSP (T1) |
| `eu/eu_32019R0947_uas_947_PL.html` (EN jest) | https://eur-lex.europa.eu/legal-content/PL/TXT/HTML/?uri=CELEX:32019R0947 | BSP, obowiązki operatora (T1) |
| `eu/eu_32014R0269_sankcje_269_PL.html` (EN jest) | https://eur-lex.europa.eu/legal-content/PL/TXT/HTML/?uri=CELEX:32014R0269 | test sankcyjny w definicji Dopuszczalnego Nabywcy, § 31 ust. 3 (1.4.2) |
| `eu/eu_32014R0833_sankcje_833_PL.html` | https://eur-lex.europa.eu/legal-content/PL/TXT/HTML/?uri=CELEX:32014R0833 | j.w. |
| `eu/eu_32024R1624_aml_PL.html` (opcjonalnie) | https://eur-lex.europa.eu/legal-content/PL/TXT/HTML/?uri=CELEX:32024R1624 | definicja beneficjenta rzeczywistego od 2027 r. (wyjątek dla funduszy, 1.4.2); dziś wystarcza ustawa AML |

Już jest (`.txt`): EDF PL i EN; po angielsku 2021/821 (konsolidacja 2023), 269/2014, 2019/947, AI Act, 2026/877, 2026/1386. Wersje PL są potrzebne do cytowania w memorandum (język urzędowy), EN wystarczą do weryfikacji tez.

## 2. Orzeczenia Sądu Najwyższego — `sn/`

Dawne adresy `.docx.html` nie istnieją (404). Wyszukaj po sygnaturze w bazie orzeczeń i zapisz stronę z treścią orzeczenia (uzasadnieniem).

| Plik | Adres | Do czego |
|---|---|---|
| `sn/sn_V_CSK_522_18.html` | https://www.sn.pl/orzecznictwo/SitePages/Baza_orzeczen.aspx?Sygnatura=V%20CSK%20522/18 | pełnomocnictwo nieodwołalne w umowie wykonawczej (1.5.3) |
| `sn/sn_II_CSKP_593_22.html` | https://www.sn.pl/orzecznictwo/SitePages/Baza_orzeczen.aspx?Sygnatura=II%20CSKP%20593/22 | art. 64 KC, zastępcze oświadczenie woli (1.5.3, T2) |
| `sn/sn_III_CSKP_65_21.html` | https://www.sn.pl/orzecznictwo/SitePages/Baza_orzeczen.aspx?Sygnatura=III%20CSKP%2065/21 | małżonek akcjonariusza (1.6.4) |
| `sn/sn_III_CZP_109_22.html` | https://www.sn.pl/orzecznictwo/SitePages/Baza_orzeczen.aspx?Sygnatura=III%20CZP%20109/22 (zapasowo: https://www.sn.pl/sprawy/SitePages/Zagadnienia_prawne_SN.aspx?ItemSID=1718-301f4741-66aa-4980-b9fa-873e90506a11&ListName=Zagadnienia_prawne&Rok=2022) | akcje a wspólność majątkowa (1.6.4) |
| `sn/sn_III_CZP_32_16.html` | https://www.sn.pl/orzecznictwo/SitePages/Baza_orzeczen.aspx?Sygnatura=III%20CZP%2032/16 (zapasowo: https://www.sn.pl/sprawy/SitePages/Zagadnienia_prawne_SN.aspx?ItemSID=786-16544171-be1b-4089-b74b-413997467af2&ListName=Zagadnienia_prawne&Rok=2016) | granice ograniczeń zbywalności (1.2.1) |

## 3. Dokumenty PFR Ventures — `pfr/`

Strona „Dokumentacja programów opartych o FENG” jest pobrana (`pfr/pfr_pfrv_feng_dokumentacja.txt`), ale wzory term sheet są pod linkami `/document/NNNN`, których poprzednia wersja `pfr.py` nie rozpoznawała; obecna wersja je pobiera (`python tools/pfr.py`). Gdyby serwis odmówił, ręcznie:

| Plik | Adres | Do czego |
|---|---|---|
| `pfr/pfr_term_sheet_starter.pdf` (+ `_en`) | https://pfrventures.pl/document/1192 , https://pfrventures.pl/en/document/1192 | wzór term sheet PFR Starter (T7, vc.md) |
| `pfr/pfr_term_sheet_biznest.pdf` (+ `_en`) | https://pfrventures.pl/document/1193 , https://pfrventures.pl/en/document/1193 | wzór term sheet PFR Biznest |
| `pfr/pfr_term_sheet_otwarte_innowacje.pdf` (+ `_en`) | https://pfrventures.pl/document/1194 , https://pfrventures.pl/en/document/1194 | wzór term sheet PFR Otwarte Innowacje |
| `pfr/pfr_term_sheet_koffi_en.pdf` | https://pfrventures.pl/en/document/1195 | wzór term sheet PFR KOFFI (strona podaje tylko EN) |
| `pfr/pfr_term_sheet_cvc.pdf` (+ `_en`) | https://pfrventures.pl/document/1196 , https://pfrventures.pl/en/document/1196 | wzór term sheet PFR CVC |

Rozszerzenie pliku (PDF/DOCX) według tego, co serwis odda; `extract_text.py` obsługuje oba. Strona `pfr/pfr_startup_baza_wiedzy.txt` ma tylko menu (lista artykułów ładowana skryptem) — nieistotne.

## 4. Strony rynkowe (opcjonalne) — `web/`

| Plik | Adres | Uwaga |
|---|---|---|
| `web/web_bvca_model_docs.html` | https://www.bvca.co.uk/resource/model-documents/ (jeśli 404: wyszukaj „Model documents” na bvca.co.uk) | wzorce BVCA (vc.md sekcja 3); niska waga |
| `web/web_prs_info.html` | https://prs.ms.gov.pl/ | Portal Rejestrów Sądowych; strona logowania, treść informacyjna minimalna — można pominąć |
| `web/web_gus_pkd2025.txt` | (jest, 4 kB) | kody PKD zweryfikowane na tekście rozporządzenia; nic nie trzeba robić |

## 5. Akty krajowe powołane w memorandum jako [W], których nie ma na liście pobierania

Do dopisania do `tools/download.sh` (funkcje `eli` / `isapU`) albo pobrania ręcznie z ELI (`https://eli.gov.pl/eli/DU/<rok>/<poz>/ogl` → tekst ujednolicony) i zapisania jako `pl_<rok>_<poz>_<nazwa>_ujednolicony.pdf`:

| Akt | Dz.U. (pierwotne) | Do czego (memorandum) |
|---|---|---|
| Ustawa o ofercie publicznej… | Dz.U. 2005 nr 184 poz. 1539 | art. 87 (działanie w porozumieniu) — 1.1.2, 1.4.1 |
| Ustawa o funduszach inwestycyjnych i zarządzaniu AFI | Dz.U. 2004 nr 146 poz. 1546 | ASI, zarządzający — wyjątek dla funduszy (1.4.1–1.4.3) |
| Ustawa o zastawie rejestrowym i rejestrze zastawów | Dz.U. 1996 nr 149 poz. 703 | zastaw na akcjach (1.2.4) |
| Ustawa o CIT | Dz.U. 1992 nr 21 poz. 86 | art. 12 ust. 1 pkt 2 (nieodpłatne przysporzenie przy wkładach poza kapitałem) — 3.1.2, T9 |
| Prawo przedsiębiorców | Dz.U. 2018 poz. 646 | art. 37 (zgłoszenie do CEIDG/KRS a działalność regulowana) — 4.1.2 |
| Prawo o notariacie | Dz.U. 1991 nr 22 poz. 91 | art. 92 (protokół), art. 90a po nowelizacji poz. 176 (rejestr akcjonariuszy u notariusza) — 4.3.1, T5 |
| Rozporządzenie RM w sprawie wykazu podmiotów podlegających ochronie | (na podstawie art. 4 ust. 2 ustawy o kontroli niektórych inwestycji) | czy Spółka może trafić do wykazu — 1.1.2 |
| Rozporządzenie MS w sprawie opłat za ogłoszenia w MSiG | — | opłata 100 zł (T3) |

## 6. Po pobraniu

1. `python tools/extract_text.py`, potem `git add src/legal && git commit`.
2. Memorandum 1.2: podnieść do [Z] tezy o EDF art. 9 (tekst już jest), TFUE, 2019/452, 2021/821 zał. I, 2026/877; orzeczenia SN w 1.2.1, 1.5.3, 1.6.4; wzory term sheet PFR w T7 i `vc.md`.
