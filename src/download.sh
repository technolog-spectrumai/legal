#!/usr/bin/env bash
# Pobiera źródła prawne i rynkowe potrzebne do weryfikacji memorandum (memorandum.tex, vc.md).
# Uruchamiać poza proxy blokującym ELI/ISAP/EUR-Lex:  ./src/download.sh
# Pliki lądują w katalogu src/ (poza git; wersjonowane są tylko skrypt i README); istniejące pliki są pomijane.
# Wynik: src/MANIFEST.txt (status każdej pozycji), src/BLEDY.txt (nieudane).
set -u
cd "$(dirname "$0")"
UA="Mozilla/5.0 (X11; Linux x86_64) Basilisk-legal-sources/1.0"
: > MANIFEST.txt; : > BLEDY.txt
ok=0; bad=0; skip=0

get() { # get <plik_docelowy> <url> [opis]
  local out="$1" url="$2" desc="${3:-}"
  if [ -s "$out" ]; then echo "SKIP  $out" | tee -a MANIFEST.txt; skip=$((skip+1)); return; fi
  if curl -sS -L --fail --retry 3 --retry-delay 2 --max-time 120 -A "$UA" -o "$out" "$url"; then
    # ELI/ISAP zwracają czasem HTML z błędem zamiast PDF; sprawdź nagłówek
    if [[ "$out" == *.pdf ]] && ! head -c 5 "$out" | grep -q '%PDF'; then
      echo "BLAD  $out (nie-PDF) <- $url" | tee -a MANIFEST.txt BLEDY.txt; rm -f "$out"; bad=$((bad+1)); return
    fi
    echo "OK    $out  ($desc)" | tee -a MANIFEST.txt; ok=$((ok+1))
  else
    echo "BLAD  $out <- $url" | tee -a MANIFEST.txt BLEDY.txt; rm -f "$out"; bad=$((bad+1))
  fi
}

# ---------- Polskie akty: ELI (eli.gov.pl) ----------
# Wzorce: tekst ogłoszony  https://eli.gov.pl/api/acts/DU/<rok>/<poz>/text.pdf  (także text.html)
eli()  { get "pl_$1_$2_$3.pdf" "https://eli.gov.pl/api/acts/DU/$1/$2/text.pdf" "$4"; }
elih() { get "pl_$1_$2_$3.html" "https://eli.gov.pl/api/acts/DU/$1/$2/text.html" "$4 (HTML)"; }

# ---------- ISAP: tekst ujednolicony ----------
# isapU <WDU-id> <nazwa> <opis>. Identyfikator ISAP: WDU + rok + Nr (3 cyfry, dla Dz.U. od 2012 r. "000") + poz. (4 cyfry).
# ISAP wymaga ciasteczka sesji: najpierw strona aktu, z niej link do pliku ujednoliconego (…Lj.pdf), a gdy go brak — tekst ogłoszony (/O/).
JAR=$(mktemp)
isapU() {
  local id="$1" name="$2" desc="$3" out="pl_${1}_${2}_ujednolicony.pdf"
  if [ -s "$out" ]; then echo "SKIP  $out" | tee -a MANIFEST.txt; skip=$((skip+1)); return; fi
  local page; page=$(curl -sS -L --retry 3 --max-time 60 -A "$UA" -c "$JAR" -b "$JAR" "https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=$id") || page=""
  local rel; rel=$(printf '%s' "$page" | grep -oE "/isap\.nsf/download\.xsp/$id/U/[A-Za-z0-9]+Lj\.pdf" | head -1)
  if [ -z "$rel" ]; then
    rel=$(printf '%s' "$page" | grep -oE "/isap\.nsf/download\.xsp/$id/O/[A-Za-z0-9]+\.pdf" | head -1)
    [ -n "$rel" ] && { out="pl_${id}_${name}_ogloszony.pdf"; desc="$desc (brak tekstu ujednoliconego w ISAP; pobrano tekst ogłoszony)"; }
  fi
  if [ -z "$rel" ]; then echo "BLAD  $out (ISAP: nie znaleziono linku do PDF na stronie aktu $id)" | tee -a MANIFEST.txt BLEDY.txt; bad=$((bad+1)); return; fi
  if curl -sS -L --fail --retry 3 --max-time 120 -A "$UA" -c "$JAR" -b "$JAR" -e "https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=$id" -o "$out" "https://isap.sejm.gov.pl$rel" && head -c 5 "$out" | grep -q '%PDF'; then
    echo "OK    $out  ($desc)" | tee -a MANIFEST.txt; ok=$((ok+1))
  else
    echo "BLAD  $out <- https://isap.sejm.gov.pl$rel" | tee -a MANIFEST.txt BLEDY.txt; rm -f "$out"; bad=$((bad+1))
  fi
}

eli  2024 18   ksh_tj            "KSH tekst jednolity Dz.U. 2024 poz. 18"
elih 2024 18   ksh_tj            "KSH tekst jednolity"
isapU WDU20000941037 ksh          "KSH (Dz.U. 2000 Nr 94 poz. 1037; tekst ujednolicony ISAP)"
eli  2026 176  ksh_nowelizacja   "Ustawa z 23.01.2026 o zmianie KSH (w życie 18.02.2027)"
elih 2026 176  ksh_nowelizacja   "Ustawa z 23.01.2026 o zmianie KSH"
eli  2026 471  obrot_strategiczny_nowela "Ustawa z 13.03.2026 (obrót strategiczny, zm. ustawy koncesyjnej)"
elih 2026 471  obrot_strategiczny_nowela "Ustawa z 13.03.2026"
eli  2019 1214 koncesje_2019     "Ustawa z 13.06.2019 o wytwarzaniu i obrocie bronią... (tekst ogłoszony)"
isapU WDU20190001214 koncesje_2019 "Ustawa koncesyjna z 2019 r."
eli  2019 1888 wykaz_WT          "Rozp. RM z 17.09.2019 - wykaz wyrobów o przeznaczeniu wojskowym lub policyjnym"
isapU WDU20190001888 wykaz_WT    "Wykaz WT"
eli  2024 1936 pkd_2025          "Rozp. RM z 18.12.2024 w sprawie PKD 2025"
eli  2026 795  kc_tj             "Kodeks cywilny t.j. Dz.U. 2026 poz. 795"
eli  2026 468  kpc_tj            "Kodeks postępowania cywilnego t.j. Dz.U. 2026 poz. 468"
eli  2026 236  kro_tj            "Kodeks rodzinny i opiekuńczy t.j. Dz.U. 2026 poz. 236"
isapU WDU20150001272 kontrola_inwestycji "Ustawa z 24.07.2015 o kontroli niektórych inwestycji"
isapU WDU19971210769 krs         "Ustawa z 20.08.1997 o KRS (Dz.U. 1997 Nr 121 poz. 769)"
isapU WDU19940240083 prawo_autorskie "Prawo autorskie z 4.02.1994 (Dz.U. 1994 Nr 24 poz. 83)"
isapU WDU20010490508 pwp         "Prawo własności przemysłowej (Dz.U. 2001 Nr 49 poz. 508)"
isapU WDU19910800350 pit         "Ustawa o PIT (Dz.U. 1991 Nr 80 poz. 350)"
isapU WDU20000860959 pcc         "Ustawa o PCC (Dz.U. 2000 Nr 86 poz. 959)"
isapU WDU20180000723 aml         "Ustawa AML z 1.03.2018 (CRBR)"
isapU WDU20220000835 sankcje_2022 "Ustawa sankcyjna z 13.04.2022"
isapU WDU20051831538 obrot_instrumentami "Ustawa o obrocie instrumentami finansowymi (Dz.U. 2005 Nr 183 poz. 1538)"
isapU WDU20001191250 obrot_strategiczny "Ustawa z 29.11.2000 o obrocie z zagranicą towarami o znaczeniu strategicznym (Dz.U. 2000 Nr 119 poz. 1250)"
isapU WDU19970780483 konstytucja "Konstytucja RP (Dz.U. 1997 Nr 78 poz. 483)"
isapU WDU19941210591 rachunkowosc "Ustawa o rachunkowości (Dz.U. 1994 Nr 121 poz. 591)"
isapU WDU19740240141 kodeks_pracy "Kodeks pracy (Dz.U. 1974 Nr 24 poz. 141)"
isapU WDU20021301112 prawo_lotnicze "Prawo lotnicze (Dz.U. 2002 Nr 130 poz. 1112)"
isapU WDU20051671398 koszty_sadowe "Ustawa o kosztach sądowych w sprawach cywilnych (Dz.U. 2005 Nr 167 poz. 1398)"
isapU WDU19930470211 uznk        "Ustawa o zwalczaniu nieuczciwej konkurencji (Dz.U. 1993 Nr 47 poz. 211)"
isapU WDU20101821228 informacje_niejawne "Ustawa o ochronie informacji niejawnych (Dz.U. 2010 Nr 182 poz. 1228)"
isapU WDU19971370926 ordynacja   "Ordynacja podatkowa (Dz.U. 1997 Nr 137 poz. 926)"

# ---------- Prawo UE: EUR-Lex ----------
# EUR-Lex odpowiada stroną HTML na zapytanie o PDF bez sesji przeglądarki; pobieramy wersję HTML (pełny tekst),
# a PDF próbujemy dodatkowo z parametrem from= i akceptacją application/pdf.
eu() { # eu <CELEX> <nazwa> <opis> [jezyk]
  local celex="$1" name="$2" desc="$3" lang="${4:-PL}"; local safe="${celex//\//_}"
  get "eu_${safe}_${name}_${lang}.html" "https://eur-lex.europa.eu/legal-content/${lang}/TXT/HTML/?uri=CELEX:${celex}" "$desc (HTML, $lang)"
  local out="eu_${safe}_${name}_${lang}.pdf"
  if [ ! -s "$out" ]; then
    if curl -sS -L --fail --retry 2 --max-time 120 -A "$UA" -H "Accept: application/pdf" -o "$out" "https://eur-lex.europa.eu/legal-content/${lang}/TXT/PDF/?uri=CELEX:${celex}&from=${lang}" && head -c 5 "$out" | grep -q '%PDF'; then
      echo "OK    $out  ($desc, PDF)" | tee -a MANIFEST.txt; ok=$((ok+1))
    else rm -f "$out"; echo "INFO  $out: EUR-Lex nie wydał PDF (wystarczy wersja HTML)" | tee -a MANIFEST.txt; fi
  fi
}
eu 32021R0697 edf             "Rozp. 2021/697 - Europejski Fundusz Obronny (art. 9)"
eu 32021R0821 dual_use        "Rozp. 2021/821 - produkty podwójnego zastosowania (zał. I, IV)"
eu 32019R0452 fdi_screening   "Rozp. 2019/452 - monitorowanie BIZ"
eu 32026R0877 ttber_2026      "Rozp. 2026/877 - porozumienia o transferze technologii (od 1.05.2026)"
eu 32014R0316 ttber_2014      "Rozp. 316/2014 - TTBER (wygasło 30.04.2026, dla porównania)"
eu 32024R1689 ai_act          "Rozp. 2024/1689 - AI Act"
eu 32023R1230 maszynowe       "Rozp. 2023/1230 - maszyny"
eu 32024R2847 cra             "Rozp. 2024/2847 - Cyber Resilience Act"
eu 32019R0945 uas_945         "Rozp. 2019/945 - bezzałogowe systemy powietrzne (produkty)"
eu 32019R0947 uas_947         "Rozp. 2019/947 - operacje BSP"
eu 32014R0269 sankcje_269     "Rozp. 269/2014 - środki ograniczające (zamrożenie aktywów)"
eu 32014R0833 sankcje_833     "Rozp. 833/2014 - sankcje sektorowe"
eu 12016E/TXT tfue            "TFUE (art. 49, 63, 65, 101, 346)"
eu 32021R0697 edf             "EDF" EN
eu 32026R0877 ttber_2026      "TTBER 2026" EN

# ---------- Orzecznictwo SN cytowane w repozytorium ----------
get sn_V_CSK_522_18.html  "https://www.sn.pl/sites/orzecznictwo/OrzeczeniaHTML/v%20csk%20522-18-1.docx.html" "SN V CSK 522/18 (pełnomocnictwo nieodwołalne)"
get sn_II_CSKP_593_22.html "https://www.sn.pl/sites/orzecznictwo/OrzeczeniaHTML/ii%20cskp%20593-22.docx.html" "SN II CSKP 593/22 (art. 64 KC)"
get sn_III_CSKP_65_21.html "https://www.sn.pl/sites/orzecznictwo/OrzeczeniaHTML/iii%20cskp%2065-21-1.docx.html" "SN III CSKP 65/21 (małżonek)"
get sn_III_CZP_109_22.html "https://www.sn.pl/sprawy/SitePages/Zagadnienia_prawne_SN.aspx?ItemSID=1718-301f4741-66aa-4980-b9fa-873e90506a11&ListName=Zagadnienia_prawne&Rok=2022" "SN III CZP 109/22"
get sn_III_CZP_32_16.html  "https://www.sn.pl/sprawy/SitePages/Zagadnienia_prawne_SN.aspx?ItemSID=786-16544171-be1b-4089-b74b-413997467af2&ListName=Zagadnienia_prawne&Rok=2016" "SN III CZP 32/16"

# ---------- Rynek VC, programy, wzorce (HTML) ----------
# Strony z ochroną przed botami (PFR, BVCA, eu-startups) odrzucają curl; wtedy pobieramy sam tekst przez czytnik r.jina.ai
# (publiczny serwis; zapis jako web_<nazwa>.txt). Jeżeli i to zawiedzie, zapisz stronę ręcznie z przeglądarki pod tą nazwą.
web() {
  local name="$1" url="$2" desc="$3" out="web_$1.html"
  if [ -s "$out" ] || [ -s "web_$1.txt" ]; then echo "SKIP  $out" | tee -a MANIFEST.txt; skip=$((skip+1)); return; fi
  if curl -sS -L --fail --compressed --retry 2 --max-time 60 -A "$UA" -H "Accept: text/html,*/*" -H "Accept-Language: pl,en" -o "$out" "$url"; then
    echo "OK    $out  ($desc)" | tee -a MANIFEST.txt; ok=$((ok+1)); return; fi
  rm -f "$out"
  if curl -sS -L --fail --retry 2 --max-time 90 -A "$UA" -o "web_$1.txt" "https://r.jina.ai/$url"; then
    echo "OK    web_$1.txt  ($desc; przez czytnik r.jina.ai)" | tee -a MANIFEST.txt; ok=$((ok+1))
  else
    rm -f "web_$1.txt"; echo "BLAD  $out <- $url (zapisz ręcznie z przeglądarki jako web_$1.html)" | tee -a MANIFEST.txt BLEDY.txt; bad=$((bad+1))
  fi
}
web pfr_umowa_inwestycyjna   "https://startup.pfr.pl/artykul/prawo-w-umowie-z-vc-umowa-inwestycyjna" "PFR: prawo w umowie z VC"
web pfr_jak_wyglada_umowa    "https://startup.pfr.pl/artykul/jak-wyglada-umowa-inwestycyjna-z-vc" "PFR: jak wygląda umowa inwestycyjna"
web pfr_term_sheet           "https://startup.pfr.pl/artykul/co-jest-term-sheet-i-jak-wyglada" "PFR: term sheet"
web pfrv_feng_dokumentacja   "https://pfrventures.pl/dokumentacja-programow-opartych-o-feng" "PFR Ventures: dokumentacja programów FENG (wzory term sheet)"
web pfrv_otwarte_innowacje   "https://pfrventures.pl/en/program-dla-vc/pfr-otwarte-innowacje" "PFR Otwarte Innowacje"
web startuppoland_termsheet  "https://standardy.startuppoland.org/wiedza/przed-inwestycja/term-sheet/" "Startup Poland: standardy term sheet"
web nvca_2025_press          "https://nvca.org/press_releases/nvca-releases-2025-updates-to-model-legal-documents/" "NVCA: aktualizacja 2025"
web nvca_2025_foley          "https://www.foley.com/insights/publications/2025/10/breaking-down-the-nvca-what-founders-and-vcs-need-to-know/" "Foley: omówienie NVCA 10/2025"
web nvca_model_docs          "https://nvca.org/model-legal-documents/" "NVCA: model legal documents (linki do wzorców)"
web bvca_model_docs          "https://www.bvca.co.uk/resource/model-documents-for-early-stage-investments" "BVCA: model documents"
web nif_about                "https://www.nif.fund/about/" "NATO Innovation Fund"
web eu_startups_defence_investors "https://www.eu-startups.com/2026/09/the-21-european-investors-funding-natos-defence/" "Inwestorzy obronni w Europie"
get nif_report_2026.pdf "https://www.nif.fund/wp-content/uploads/2026/02/NIF-report-Defence-Security-and-Resilience-2026-A4-size-25mm-margin-V2.pdf" "Raport NIF 2026"
web edf_gowling             "https://gowlingwlg.com/en/insights-resources/articles/2026/the-european-defence-fund" "EDF omówienie"
web olesinski_poz471        "https://olesinski.com/aktualnosci/nowe-zasady-obrotu-towarami-strategicznymi-8-kluczowych-zmian-dla-sektora-dual-use-i-zbrojeniowego/" "Omówienie ustawy Dz.U. 2026 poz. 471"
web cgolegal_koncesja       "https://cgolegal.pl/baza-wiedzy/biezace-doradztwo-prawne/koncesja-na-obrot-specjalny/" "Wymogi koncesji MSWiA"
web psa_uprzywilejowanie    "https://prosta-spolka.pl/uprzywilejowanie-akcji-w-prostej-spolce-akcyjnej/" "Uprzywilejowanie akcji w P.S.A."
web psa_biznes_gov          "https://www.biznes.gov.pl/pl/portal/00168" "biznes.gov.pl: P.S.A."
web prs_info                "https://prs.ms.gov.pl/" "Portal Rejestrów Sądowych"
web gus_pkd2025             "https://www.biznes.gov.pl/pl/klasyfikacja-pkd" "Wyszukiwarka PKD 2025"
rm -f "$JAR"

echo
echo "Pobrane: $ok, pominięte (już były): $skip, błędy: $bad  -> MANIFEST.txt, BLEDY.txt"
echo "Po pobraniu: ./src/extract_text.py zamienia PDF i HTML na .txt. Pozycje z BLEDY.txt zapisz ręcznie z przeglądarki pod nazwą z listy."
