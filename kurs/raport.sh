#!/bin/sh
# Agregator rejestru odpowiedzi (typed_answer_log) -> zwiezly raport.
# Sens: cala praca na pliku dzieje sie TUTAJ, a do kontekstu AI wchodzi
# tylko podsumowanie. Dzieki temu rozmiar pliku przestaje miec znaczenie.
# Uzycie: sh raport.sh [liczba_dni_wstecz]

DIR="/c/Users/appec/AppData/Roaming/Anki2/addons21/typed_answer_log/user_files"

# Swiadomie zbieramy WSZYSTKIE pliki .jsonl z katalogu: historia moze byc
# rozbita miedzy "Nowy kurs angielski.jsonl" (stara wersja dodatku, surowa
# nazwa profilu) i "nowy_kurs_angielski.jsonl" (wersja po slugifikacji).
cat "$DIR"/*.jsonl 2>/dev/null \
| grep '"deck": "Kurs Angielskiego::' \
| sed -n 's/^.*"ts": "\([^"]*\)".*"card_id": \([0-9]*\).*"deck": "\([^"]*\)".*"typed": "\(.*\)", "expected": "\(.*\)", "correct": \(true\|false\), "bad_pronunciation": \(true\|false\), "ease": \([0-9]\).*$/\1\t\2\t\3\t\4\t\5\t\6\t\7\t\8/p' \
| awk -F'\t' '
{
  ts=$1; cid=$2; deck=$3; typed=$4; expd=$5; corr=$6; pron=$7; ease=$8
  n++; seen[cid]++
  if (deck ~ /::A1$/) lvl["A1"]++; else { split(deck,p,"::"); lvl[p[2]]++ }
  if (corr=="true") ok++
  else if (ease=="1") { real++; realc[cid]++; bad[cid]=bad[cid] sprintf("    %s  wpisano \"%s\"  zamiast \"%s\"  [BLAD]\n", substr(ts,1,16), typed, expd) }
  else if (ease=="2") { hardc[cid]++; bad[cid]=bad[cid] sprintf("    %s  wpisano \"%s\"  zamiast \"%s\"  [Hard]\n", substr(ts,1,16), typed, expd) }
  else { tech++; techc[cid]++; bad[cid]=bad[cid] sprintf("    %s  wpisano \"%s\"  zamiast \"%s\"  [wpadka tech.]\n", substr(ts,1,16), typed, expd) }
  if (pron=="true") { pronn++; pronc[cid]++; expected_of[cid]=expd }
  easec[ease]++
  if (ts>last) last=ts
  if (first=="" || ts<first) first=ts
}
END{
  if (n==0) { print "Rejestr pusty (brak linii z deckow Kurs Angielskiego::*)."; exit }
  printf "== REJESTR: %d powtorek, %d unikalnych kart ==\n", n, length(seen)
  printf "okres: %s  ->  %s\n", substr(first,1,16), substr(last,1,16)
  printf "poprawne: %d/%d (%.0f%%)\n", ok, n, 100*ok/n
  printf "ease  1=Again:%d  2=Hard:%d  3=Good:%d  4=Easy:%d\n", easec[1], easec[2], easec[3], easec[4]
  printf "REALNE bledy (correct:false + ease 1): %d\n", real+0
  printf "wpadki techniczne (correct:false + ease 3/4): %d\n", tech+0
  printf "flagi bad_pronunciation: %d\n", pronn+0
  printf "\npowtorki per poziom:"
  for (l in lvl) printf "  %s=%d", l, lvl[l]
  printf "\n"

  printf "\n== KARTY Z PROBLEMAMI (card_id: bledy/hard/tech/wymowa z N powtorek) ==\n"
  any=0
  for (c in seen) if (realc[c] || hardc[c] || techc[c] || pronc[c]) {
    any=1
    printf "%s: %d/%d/%d/%d z %d\n", c, realc[c]+0, hardc[c]+0, techc[c]+0, pronc[c]+0, seen[c]
    printf "%s", bad[c]
  }
  if (!any) print "(brak)"
}'
