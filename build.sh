#!/usr/bin/env bash
# Buduje dokumenty PDF w poprawnej kolejności i z czystymi plikami pomocniczymi.
#
# Użycie:
#   ./build.sh                      -> psa.pdf, extra.pdf, psa_feedback.pdf, shareholder_agreement.pdf
#   ./build.sh extra psa_feedback   -> wybrane dokumenty (psa.tex zawsze jako pierwszy, bo dostarcza psa.aux
#                                      z numerami paragrafów dla pozostałych plików)
#
# Dlaczego czyścimy: psa.toc (spis treści) i psa.out (zakładki PDF) z poprzedniej wersji przeżywają
# git checkout, a pierwszy przebieg pdflatex wstawia je do PDF-a — wtedy w spisie treści i zakładkach
# widać sekcje, których w źródle już nie ma.
set -euo pipefail
cd "$(dirname "$0")"

docs=(psa extra psa_feedback shareholder_agreement)
if [ $# -gt 0 ]; then
  docs=(psa)
  for d in "$@"; do [ "$d" != psa ] && docs+=("${d%.tex}"); done
fi

for d in "${docs[@]}"; do
  rm -f "$d.aux" "$d.toc" "$d.out" "$d.log" "$d.lof" "$d.lot"
done

for d in "${docs[@]}"; do
  for pass in 1 2; do
    if ! pdflatex -interaction=nonstopmode -halt-on-error "$d.tex" > "$d.build.log" 2>&1; then
      echo "BŁĄD kompilacji: $d.tex (szczegóły: $d.log)"; exit 1
    fi
  done
  echo "$d.pdf: $(grep -o 'Output written on [^(]*([0-9]* pages' "$d.log" | grep -o '[0-9]* pages')"
done
