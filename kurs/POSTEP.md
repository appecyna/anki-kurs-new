# Postęp kursu

Aktualizowane po każdej turze zgodnie z [`PROMPT_NAUCZYCIELA.md`](PROMPT_NAUCZYCIELA.md).

## Aktualna pozycja w programie

- **Poziom:** A1
- **Moduł:** 4/12 zrecenzowany i oceniony (2026-09-04) — **wstrzymano
  dokładanie nowego materiału na życzenie użytkownika**, tylko ocena +
  sugestie ulepszeń.
- **Następny krok (gdy użytkownik poprosi o kontynuację):** *have got* w
  przeczeniach/pytaniach (haven't got / Have you got...?) + reszta A1 §4
  (przedmioty codzienne, pokoje w domu).

## Log partii

| # | Data | Poziom | Temat | Kierunki | Liczba fiszek | Deck |
|---|------|--------|-------|----------|----------------|------|
| 1 | 2026-09-03 | A1 | Powitania (cześć, dzień dobry, dziękuję, proszę, tak, nie) + pies/kot + zdania z *to be* (This is a dog/cat, I am a student) | pl-en i en-pl | 22 | `Kurs Angielskiego::A1` |
| 2 | 2026-09-03 | A1 | Pełna odmiana *to be* przez osoby (hungry/ready/strong/nice/big/happy/young) + rodzajniki a/an (apple, orange) + liczby 1–2 | pl-en i en-pl | 22 | `Kurs Angielskiego::A1` |
| 3 | 2026-09-03 | A1 | Liczby 3–6, rodzina (matka/ojciec/brat/siostra), przymiotniki (mały/stary/nowy), rozróżnienie miła↔uprzejmy | pl-en i en-pl | 24 | `Kurs Angielskiego::A1` |
| 4 | 2026-09-04 | A1 | Liczby 7–10, wygląd (wysoki/niski), nowe rzeczowniki (dom, samochód) + wprowadzenie *have got* (Mam psa. / He has got a car. / She has got a house.) | pl-en i en-pl | 22 | `Kurs Angielskiego::A1` |

## Ocena partii 1 (recenzja: 2026-09-03)

- 20/22 fiszek zrecenzowanych (2 nieużyte jeszcze — domyślny limit Anki 20
  nowych kart/dzień; **sugestia: podnieś limit w opcjach decka, jeśli chcesz
  widzieć całą partię tego samego dnia**).
- Słownictwo powitań i zwierząt: 100% poprawnych odpowiedzi za drugim
  podejściem — bardzo dobrze ugruntowane, brak powtarzających się błędów.
- Dwa jednorazowe, od razu skorygowane potknięcia (nie kwalifikują się jako
  wzorzec wymagający remediacji, ale obserwuję je dalej w kolejnych partiach):
  - `pies → dog`: raz dopisano zbędny rodzajnik ("a dog" zamiast "dog") —
    dlatego partia 2 świadomie kontrastuje gołe słowo z pełnym zdaniem z "a/an".
  - `To jest pies. → This is a dog.`: raz brakło kropki na końcu zdania —
    obserwować, czy to się powtórzy przy dłuższych zdaniach.
- **Wniosek:** brak konieczności remediacji — pełne przejście dalej w programie.

## Ocena partii 2 (recenzja: 2026-09-03)

Wszystkie 44 fiszki (partia 1+2) zrecenzowane, dokładność ogólna >85%. Kluczowy
wniosek: **większość błędów wynikała z dwuznaczności kart, nie z braków w
wiedzy użytkownika** — poprawiono je od razu w kolekcji zamiast dodawać
remediację:

- `To jest duże.` → wpisano *"This is big."* zamiast *"It is big."* — polskie
  "to" nie rozróżnia this/it. **Fix:** dopisano podpowiedź w Front wskazującą
  które zaimkiem chodzi (ta sama poprawka dla `To jest jabłko.`, gdzie
  zamieniono kierunek podpowiedzi na "this").
- `Jestem uczniem.` / `I am a student.` — wpisano *"Jestem studentem."*
  Naturalniejsze polskie tłumaczenie "student" to "student", nie "uczeń".
  **Fix:** zamieniono parę na `Jestem studentem.` ↔ `I am a student.`
  (tłumaczenie kognatowe, jednoznaczne).
- `My jesteśmy szczęśliwi.` / `We are happy.` — **dwukrotnie** wpisano
  *"Jesteśmy szczęśliwi."* (bez "My"). To była poprawna, naturalna polska
  wersja — "jesteśmy" jednoznacznie wskazuje 1. os. l.mn., więc "My" jest
  zbędne (inaczej niż przy "on/ona", gdzie zaimek niesie informację o
  rodzaju). **Fix:** usunięto "My" z obu kierunków karty.
- Drobne, jednorazowe pomyłki bez wzorca, bez akcji: *"You are hungry"*
  zamiast *"ready"* (interferencja sąsiednich zdań o podobnej strukturze),
  *"She is polite"* zamiast *"nice"* (sensowna pomyłka synonimiczna) — stąd
  w partii 3 dodano jawne rozróżnienie miła (nice/kind) ↔ uprzejmy (polite).
- **Wniosek:** żadnych systemowych luk w wiedzy — czysta kontynuacja programu.

## Ocena partii 3 (recenzja: 2026-09-04)

Wszystkie fiszki partii 1–2 przy dzisiejszej powtórce wypadły **bezbłędnie**
(w tym wszystkie wcześniej naprawione dwuznaczne karty — potwierdza to, że
poprawki z oceny partii 2 były trafne). Partia 3 (liczby, rodzina,
przymiotniki): bardzo dobry wynik, 3 drobne, jednorazowe potknięcia bez wzorca:

- `cztery` → pusta odpowiedź (najpewniej pośpiech/przypadek).
- `pięć` → pomylone z "six" (interferencja sąsiednich liczb w sesji).
- `pięć` (EN→PL) → wpisano "pięc" zamiast "pięć" (brak polskiej litery "ć" —
  **obserwować w kolejnych partiach**, czy to się powtarza przy innych słowach
  z ą/ć/ę/ł/ń/ó/ś/ź/ż; może wskazywać na układ klawiatury bez polskich znaków).

Użytkownik rozbudował wtyczkę o dźwięk TTS (pole `Back` kart PL→EN) i przycisk
"Zła wymowa" (`[WYMOWA]` w `History`) — patrz
[`PROMPT_NAUCZYCIELA.md`](PROMPT_NAUCZYCIELA.md#dźwięk-i-wymowa-od-partii-3-dodane-przez-użytkownika).
Żadnych artefaktów `[sound:...]` nie znaleziono w polu `History` — czyszczenie
działa poprawnie. Przycisk "Zła wymowa" jeszcze nieużyty w praktyce.

**Wniosek:** brak konieczności remediacji — pełne przejście dalej w programie.

## Ocena partii 4 (recenzja: 2026-09-04, bez dokładki materiału na życzenie użytkownika)

Wszystkie 22 fiszki zrecenzowane dwukrotnie. Wynik bardzo dobry, typowa
krzywa dla dnia 1. nowej struktury gramatycznej:

- `dziesięć` (EN→PL) → wpisano "dziesięc" (brak "ć"). **To już DRUGI raz ten
  sam wzorzec** (poprzednio `pięć`→"pięc") — patrz sekcja "Zidentyfikowane
  słabe punkty" niżej, to się potwierdza jako realna obserwacja, nie szum.
- `He has got a car.` → raz pominięte "got" ("He has a car.") — oczekiwane
  przy pierwszym kontakcie z `have got` (w polskim "mieć" wystarcza, nie ma
  odpowiednika strukturalnego). Druga próba to literówka techniczna (podwójna
  spacja, brak kropki), nie błąd językowy.
- `She has got a house.` → raz "He" zamiast "She" — zaimek "przeciekł" z
  poprzedniej karty `He has got a car.` (patrz "Sugestie ulepszeń": to
  prawdopodobnie efekt kolejności kart, nie luka w wiedzy).

**Wniosek:** brak potrzeby remediacji `have got` już teraz — to normalne
pierwsze starcie z nową strukturą. Warto dać jej więcej powtórzeń zanim
przejdziemy do przeczeń/pytań, gdy wrócimy do dokładania materiału.

## Decyzje z 2026-09-04 (po ocenie partii 4)

Ustalone z użytkownikiem, pełne uzasadnienia w
[`PROMPT_NAUCZYCIELA.md`](PROMPT_NAUCZYCIELA.md):

1. **Losowa kolejność nowych kart — zastosowana.** Utworzono dedykowany
   preset opcji decka "Kurs Angielskiego" (klon domyślnego, id
   `1788546654082`, niewspółdzielony z innymi deckami) przypisany do
   `Kurs Angielskiego::A1`, z `newGatherPriority: 3` (Random notes) i
   `newSortOrder: 4` (Random). Cel: rozbić kolejność "dodania", która
   powodowała, że podobne karty dodane blokiem trafiały do przeglądu jedna po
   drugiej. Zweryfikowano przez `getDeckConfig` po zapisie.
2. **Kalibracja czułości na błędy.** Pojedyncze literówki/pomyłki z pośpiechu
   (np. "pięc" zamiast "pięć") **nie są już traktowane jako słaby punkt** —
   próg eskalacji to ~20 powtórzeń tego samego wzorca pod rząd. Wcześniejszy
   wpis o "ć" w liczebnikach był poniżej tego progu — wycofany jako aktywna
   obserwacja, zostaje tylko w logu partii 3/4 dla kompletności historii.
3. **Weryfikacja wymowy** pozostaje samodzielnym zgłoszeniem przez przycisk
   "Zła wymowa" (brak rozpoznawania mowy) — próg reakcji: 3+ wystąpienia
   `[WYMOWA]` dla tej samej cechy fonetycznej. Na razie 0 zgłoszeń.
4. **Tempo nauczania to autonomiczna decyzja nauczyciela** (mnie) — nie
   wymaga pytania użytkownika za każdym razem. Przy `have got`: świadomie
   dam więcej powtórzeń formy twierdzącej, zanim wprowadzę przeczenia/pytania.

## Zidentyfikowane słabe punkty

_(brak — jedyne dotąd obserwacje literówkowe są poniżej progu eskalacji ~20x,
patrz "Decyzje z 2026-09-04" wyżej)_

## Uwagi

- W domyślnym decku (`Domyślna`) istnieją 2 starsze fiszki testowe użytkownika
  (dog/pies, cat/kot) sprzed uruchomienia kursu — pozostawione bez zmian, nie są
  częścią programu i można je bezpiecznie zignorować lub usunąć ręcznie.
- ~~Domyślny limit nowych kart/dzień w Anki (20)...~~ **Sprostowanie
  (2026-09-04):** sprawdzone przez `getDeckConfig` — limit to faktycznie
  `perDay: 999` (praktycznie brak limitu). Wcześniejsza sugestia była błędna,
  niedokończenie partii 1 miało inną przyczynę (brak czasu w sesji).
