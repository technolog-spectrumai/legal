#!/usr/bin/env bash
# Buduje dokumenty PDF w poprawnej kolejności i z czystymi plikami pomocniczymi.
#
# Użycie:
#   ./build.sh                      -> psa.pdf, extra.pdf, psa_feedback.pdf, shareholder_agreement.pdf, uchwaly.pdf, memorandum.pdf
#   ./build.sh extra psa_feedback   -> wybrane dokumenty (psa.tex zawsze jako pierwszy, bo dostarcza psa.aux
#                                      z numerami paragrafów dla pozostałych plików)
#
# Dlaczego czyścimy: psa.toc (spis treści) i psa.out (zakładki PDF) z poprzedniej wersji przeżywają
# git checkout, a pierwszy przebieg pdflatex wstawia je do PDF-a — wtedy w spisie treści i zakładkach
# widać sekcje, których w źródle już nie ma.
set -euo pipefail
cd "$(dirname "$0")"

docs=(psa psa_en appolonia appolonia_en basilisk_sha basilisk_sha_en basilisk_ip basilisk_ip_en basilisk_cennik basilisk_cennik_en basilisk_nda basilisk_nda_en basilisk_polityka basilisk_polityka_en basilisk_decyzje basilisk_decyzje_skrot basilisk_decyzje_skrot_en basilisk_decyzje_en basilisk_psa_komentarz basilisk_psa_komentarz_en basilisk_akt basilisk_akt_en decision_making_eng decisions_en_short basilisk_esop basilisk_esop_en basilisk_uprawnienia basilisk_uprawnienia_en basilisk_konsultanci basilisk_konsultanci_en extra psa_feedback shareholder_agreement uchwaly memorandum)
if [ $# -gt 0 ]; then
  # psa.tex zawsze pierwszy; potem zależności (\externaldocument{...}) każdego wskazanego pliku, na końcu sam plik.
  docs=(psa)
  add() { local x; for x in "${docs[@]}"; do [ "$x" = "$1" ] && return; done; docs+=("$1"); }
  for d in "$@"; do
    d="${d%.tex}"
    for dep in $(grep -o '\\externaldocument{[^}]*}' "$d.tex" 2>/dev/null | sed 's/.*{\(.*\)}/\1/'); do add "$dep"; done
    add "$d"
  done
fi

for d in "${docs[@]}"; do
  rm -f "$d.aux" "$d.toc" "$d.out" "$d.log" "$d.lof" "$d.lot"
done

for d in "${docs[@]}"; do
  # do 4 przebiegów, aż etykiety i spis treści się ustalą
  for pass in 1 2 3 4; do
    if ! pdflatex -interaction=nonstopmode -halt-on-error "$d.tex" > "$d.build.log" 2>&1; then
      echo "BŁĄD kompilacji: $d.tex (szczegóły: $d.log)"; exit 1
    fi
    [ "$pass" -ge 2 ] && ! grep -q 'Rerun to get\|Label(s) may have changed' "$d.log" && break
  done
  echo "$d.pdf: $(grep -o 'Output written on [^(]*([0-9]* pages' "$d.log" | grep -o '[0-9]* pages')"
done
