#!/usr/bin/env bash
# Pobiera akty prawa UE (EUR-Lex / Urząd Publikacji) do src/legal/ — osobno od download.sh, bo EUR-Lex
# odpowiada pustą treścią na proste zapytania curl. Kolejne strategie dla każdej pozycji:
#   1) adres ELI z sesją (ciasteczko z eur-lex.europa.eu), format html:  https://eur-lex.europa.eu/eli/<typ>/<rok>/<nr>/oj/pol/html
#   2) adres ELI z negocjacją treści (Accept: text/html):                https://eur-lex.europa.eu/eli/<typ>/<rok>/<nr>/oj/pol
#   3) legal-content HTML z sesją:                                        https://eur-lex.europa.eu/legal-content/PL/TXT/HTML/?uri=CELEX:<celex>
#   4) Urząd Publikacji (CELLAR), negocjacja treści po CELEX:             http://publications.europa.eu/resource/celex/<celex>  (Accept: text/html, Accept-Language: pol)
#   5) legal-content PDF z sesją (Accept: application/pdf)
# Odpowiedź uznajemy za poprawną, gdy ma > 20 kB i zawiera „Artykuł” (PL) albo „Article” (EN) — inaczej to strona zastępcza.
# Użycie:  ./src/tools/download_eu.sh          (w src/legal/ powstają eu_<CELEX>_<nazwa>_<jezyk>.html lub .pdf)
#          potem ./src/tools/extract_text.py
set -u
cd "$(dirname "$0")/../legal" 2>/dev/null || { mkdir -p "$(dirname "$0")/../legal"; cd "$(dirname "$0")/../legal"; }
UA="Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
JAR=$(mktemp); trap 'rm -f "$JAR"' EXIT
: > MANIFEST_EU.txt; : > BLEDY_EU.txt
ok=0; bad=0; skip=0

# sesja: strona główna ustawia ciasteczka
curl -sS -L --max-time 60 -A "$UA" -c "$JAR" -b "$JAR" -o /dev/null "https://eur-lex.europa.eu/homepage.html?locale=pl" || true

valid() { # valid <plik> <html|pdf>
  local f="$1" kind="$2"
  [ -s "$f" ] || return 1
  [ "$(wc -c < "$f")" -gt 20000 ] || return 1
  if [ "$kind" = pdf ]; then head -c 5 "$f" | grep -q '%PDF'; return; fi
  grep -qiE 'Artyku|Article|Artikel' "$f"
}
try() { # try <plik> <kind> <url> [dodatkowe opcje curl...]
  local f="$1" kind="$2" url="$3"; shift 3
  curl -sS -L --fail --compressed --retry 2 --retry-delay 3 --max-time 180 -A "$UA" -c "$JAR" -b "$JAR" \
       -e "https://eur-lex.europa.eu/" -H "Accept-Language: pl,en;q=0.8" "$@" -o "$f" "$url" 2>/dev/null && valid "$f" "$kind"
}
eu() { # eu <CELEX> <eli-sciezka: reg/2021/697 | "-"> <nazwa> <opis> [jezyk PL|EN]
  local celex="$1" eli="$2" name="$3" desc="$4" lang="${5:-PL}"; local safe="${celex//\//_}"
  local lc=$(printf '%s' "$lang" | tr 'A-Z' 'a-z'); local eli_lang="pol"; [ "$lang" = EN ] && eli_lang="eng"
  local html="eu_${safe}_${name}_${lang}.html" pdf="eu_${safe}_${name}_${lang}.pdf" txt="eu_${safe}_${name}_${lang}.txt"
  if { [ -s "$html" ] && valid "$html" html; } || [ -s "$txt" ] || { [ -s "bkp/$html" ] && [ -s "$txt" ]; } || [ -s "$pdf" ]; then
    echo "SKIP  $html" | tee -a MANIFEST_EU.txt; skip=$((skip+1)); return; fi
  rm -f "$html" "$pdf"
  if [ "$eli" != "-" ]; then
    try "$html" html "https://eur-lex.europa.eu/eli/$eli/oj/$eli_lang/html" && { echo "OK    $html  ($desc; ELI html)" | tee -a MANIFEST_EU.txt; ok=$((ok+1)); return; }
    try "$html" html "https://eur-lex.europa.eu/eli/$eli/oj/$eli_lang" -H "Accept: text/html" && { echo "OK    $html  ($desc; ELI negocjacja)" | tee -a MANIFEST_EU.txt; ok=$((ok+1)); return; }
  fi
  try "$html" html "https://eur-lex.europa.eu/legal-content/$lang/TXT/HTML/?uri=CELEX:$celex" -H "Accept: text/html" && { echo "OK    $html  ($desc; legal-content html)" | tee -a MANIFEST_EU.txt; ok=$((ok+1)); return; }
  try "$html" html "http://publications.europa.eu/resource/celex/$celex" -H "Accept: text/html" -H "Accept-Language: $eli_lang" && { echo "OK    $html  ($desc; CELLAR)" | tee -a MANIFEST_EU.txt; ok=$((ok+1)); return; }
  try "$pdf" pdf "https://eur-lex.europa.eu/legal-content/$lang/TXT/PDF/?uri=CELEX:$celex" -H "Accept: application/pdf" && { echo "OK    $pdf  ($desc; legal-content pdf)" | tee -a MANIFEST_EU.txt; ok=$((ok+1)); return; }
  rm -f "$html" "$pdf"
  echo "BLAD  $html <- https://eur-lex.europa.eu/legal-content/$lang/TXT/?uri=CELEX:$celex (zapisz ręcznie z przeglądarki: „Tekst” -> Zapisz stronę jako HTML pod tą nazwą)" | tee -a MANIFEST_EU.txt BLEDY_EU.txt; bad=$((bad+1))
}

eu 32021R0697 reg/2021/697      edf           "Rozp. 2021/697 - Europejski Fundusz Obronny (art. 9)"
eu 32021R0697 reg/2021/697      edf           "EDF" EN
eu 32021R0821 reg/2021/821      dual_use      "Rozp. 2021/821 - produkty podwójnego zastosowania (zał. I, IV)"
eu 32019R0452 reg/2019/452      fdi_screening "Rozp. 2019/452 - monitorowanie BIZ"
eu 32026R0877 reg/2026/877      ttber_2026    "Rozp. 2026/877 - porozumienia o transferze technologii"
eu 32026R0877 reg/2026/877      ttber_2026    "TTBER 2026" EN
eu 32014R0316 reg/2014/316      ttber_2014    "Rozp. 316/2014 - TTBER (wygasło 30.04.2026)"
eu 32024R1689 reg/2024/1689     ai_act        "Rozp. 2024/1689 - AI Act"
eu 32023R1230 reg/2023/1230     maszynowe     "Rozp. 2023/1230 - maszyny"
eu 32024R2847 reg/2024/2847     cra           "Rozp. 2024/2847 - Cyber Resilience Act"
eu 32019R0945 reg_del/2019/945  uas_945       "Rozp. delegowane 2019/945 - bezzałogowe systemy powietrzne"
eu 32019R0947 reg_impl/2019/947 uas_947       "Rozp. wykonawcze 2019/947 - operacje BSP"
eu 32014R0269 reg/2014/269      sankcje_269   "Rozp. 269/2014 - środki ograniczające (zamrożenie aktywów)"
eu 32014R0833 reg/2014/833      sankcje_833   "Rozp. 833/2014 - sankcje sektorowe"
eu 12016E/TXT -                 tfue          "TFUE (art. 49, 63, 65, 101, 346)"

echo
echo "Pobrane: $ok, pominięte: $skip, błędy: $bad  -> MANIFEST_EU.txt, BLEDY_EU.txt"
echo "Następnie: ./src/tools/extract_text.py  (HTML -> .txt, oryginały do bkp/)"
