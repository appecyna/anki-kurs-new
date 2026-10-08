# Postęp kursu

Aktualizowane po każdej turze zgodnie z [`PROMPT_NAUCZYCIELA.md`](PROMPT_NAUCZYCIELA.md).

**Kurs wystartował od nowa 2026-10-07** (nowy notatnik "Basic (type in the
answer + pronunciation)" + rejestr odpowiedzi JSONL). Brak wcześniejszego
postępu do uwzględnienia.

## Aktualna pozycja w programie

- **Poziom:** A1
- **Moduł:** 1/12 — w toku (powitania, uprzejmości, alfabet, liczby 0–100)
- **Zrobione w module:** powitania + uprzejmości (partia 1), liczby 1–10 (partia 2)
- **Następny krok:** liczby 11–20 i dziesiątki do 100 (oba kierunki), potem
  domknięcie uprzejmości (`excuse me` tylko EN→PL). Alfabet/literowanie na
  koniec modułu — przy typed-answer wymaga osobnego formatu fiszki.

## Jak czytać rejestr (ważne operacyjnie)

**Nie czytaj pliku `.jsonl` surowo w całości.** Zmierzone: ~200 B/linię, czyli
~65 tokenów. Przy ~100–150 powtórkach dziennie plik szybko przekracza rozsądny
rozmiar dla wczytania do kontekstu (ok. 1500 linii to już granica).

Używaj [`raport.sh`](raport.sh) — agreguje po stronie systemu plików i zwraca
~20 linii podsumowania **niezależnie od rozmiaru pliku**: `sh kurs/raport.sh`

Skrypt celowo robi `cat "$DIR"/*.jsonl` (wszystkie pliki) — zabezpieczenie na
wypadek, gdyby historia znów rozbiła się na dwie nazwy. Treść fiszek dociągaj przez `cardsInfo`
**tylko dla `card_id` wskazanych przez raport jako problematyczne**, nie dla
całego decka.

Narzędzia na tej maszynie: `awk`/`sed`/`grep` są dostępne. **`python` i `jq`
NIE są** (`python` to zaślepka ze Microsoft Store, nie interpreter) — dlatego
raport jest w awk, nie w Pythonie.

## Stan techniczny

- [x] AnkiConnect odpowiada (`version` → 6), aktywny profil: **Nowy kurs angielski**.
- [x] Kolekcja wyzerowana przed partią 1: **0 notatek** w całej kolekcji,
      jedyny deck "Domyślna". Rejestr: katalog `user_files` pusty.
- [x] Deck `Kurs Angielskiego::A1` (id 1791408751368).
- [x] Dedykowany preset opcji **"Kurs Angielskiego"** (id **1791408751411**,
      klon domyślnego, niewspółdzielony) z `newGatherPriority: 3` (Random notes)
      i `newSortOrder: 4` (Random), przypisany do decka — zweryfikowane przez
      `getDeckConfig`. **Każdy kolejny deck poziomu przypisuj do tego samego presetu.**
- Limit nowych kart: `new.perDay: 20` (domyślny) — zgodny z rozmiarem partii.
- Audio: brak (użytkownik dokleja sam).

### Nazwa pliku rejestru — ROZWIĄZANE 2026-10-08

Objaw: rejestr zapisywał się jako `Nowy kurs angielski.jsonl` (surowa nazwa
profilu), a nie `nowy_kurs_angielski.jsonl` zgodnie ze specyfikacją
w [`PROMPT_NAUCZYCIELA.md`](PROMPT_NAUCZYCIELA.md).

Przyczyna: Anki trzymało w pamięci **starszą wersję dodatku**. Plik
`__init__.py` w `addons21` został zaktualizowany 2026-10-07 o 23:00 (dodanie
slugifikacji w `_log_path()`), ale proces Anki wystartował wcześniej i działał
na kodzie wczytanym przy starcie.

Rozwiązanie (2026-10-08, przy zamkniętym Anki — `AnkiConnect` nie odpowiadał):
- [x] Zmieniona nazwa `Nowy kurs angielski.jsonl` → `nowy_kurs_angielski.jsonl`.
      Bezstratnie: docelowa nazwa nie istniała, więc był to czysty `mv`, bez
      scalania. 30 linii, 6015 B przed i po.
- [x] Zweryfikowane, że zainstalowany `_log_path()` slugifikuje, czyli po
      restarcie dodatek dopisuje **do tego samego pliku** — historia zostaje
      ciągła.
- [x] `diff -r` źródła w repo z `addons21`: bez różnic (poza samym plikiem danych).
- [x] [`raport.sh`](raport.sh) czyta nową nazwę poprawnie (30 powtórek, 87%).
- Kopia zapasowa 30 linii leży w katalogu scratchpad sesji
  (`rejestr-backup-2026-10-08.jsonl`) — do usunięcia, gdy przestanie być
  potrzebna; nie jest to trwałe miejsce.

**Nauka na przyszłość:** po każdej edycji kodu dodatku trzeba zrestartować
Anki, inaczej zmiany nie działają, mimo że pliki na dysku są poprawne. Jeśli
w `user_files` pojawią się kiedyś dwa pliki `.jsonl`, to jest ten sam objaw —
scal je (sortując po `ts`) i zrestartuj Anki.
## Log partii

| # | Data | Poziom | Temat | Kierunki | Liczba fiszek | Deck |
|---|------|--------|-------|----------|----------------|------|
| 1 | 2026-10-07 | A1 §1 | powitania, uprzejmości | pl-en 10 + en-pl 10 | 20 | `Kurs Angielskiego::A1` |
| 2 | 2026-10-07 | A1 §1 | liczby 1–10 | pl-en 10 + en-pl 10 | 20 | `Kurs Angielskiego::A1` |

**Stan decka po partii 2: 39 kart** (20 + 20 − 1 usunięta, patrz niżej).

### Partia 1 — zawartość (2026-10-07)

10 jednostek, każda w obu kierunkach: cześć/hello, dzień dobry (rano)/good
morning, dobry wieczór/good evening, dobranoc/good night, do widzenia/goodbye,
Jak się masz?/How are you?, dziękuję/thank you, proszę/please,
przepraszam/sorry, nie ma za co/you're welcome.

Decyzje: oba kierunki wszędzie (pary 1:1); podpowiedzi w nawiasie na awersie
PL→EN tam, gdzie polskie słowo jest wieloznaczne; kolejność dodawania
przeplatana. **Odłożone:** `yes`/`no` → A1 §2 (razem z `to be` i pytaniami);
`excuse me` → później, tylko EN→PL (PL→EN kolidowałby z `przepraszam → sorry`).

### Partia 2 — zawartość (2026-10-07)

**Liczby 1–10**, każda w obu kierunkach (20 fiszek), tag `temat::liczby`:
one/jeden, two/dwa, three/trzy, four/cztery, five/pięć, six/sześć,
seven/siedem, eight/osiem, nine/dziewięć, ten/dziesięć.

Decyzje dydaktyczne:
- **`zero` pominięte** — polskie "zero" i angielskie "zero" są identyczne,
  fiszka miałaby zerową wartość dydaktyczną. Wejdzie ewentualnie dopiero przy
  czytaniu numerów (telefony, wyniki: "oh" / "nil").
- Oba kierunki: PL→EN trenuje produkcję, EN→PL utrwala pisownię
  (`eight`, `nine` to niebanalna ortografia).
- Kolejność dodawania **celowo nie 1→10**, a pomieszana i z przeplatanymi
  kierunkami — liczby to historycznie materiał podatny na przecieki
  (`pięć`/`sześć`), więc poza losowym presetem dochodzi ta warstwa.
- **Bez bloku remediacyjnego** na `dobry wieczór`/`dobranoc` — uzasadnienie
  w sekcji o słabych punktach.

### Korekty istniejących fiszek (2026-10-07, po partii 1)

Rejestr pokazał, że dwa "błędy" były w rzeczywistości **wadami projektu
fiszki** — użytkownik wpisał poprawny angielski/polski, którego pole `Back`
nie przewidywało:

- **Poprawiona** nota 1791408815151 (PL→EN `przepraszam` → `sorry`):
  wpisał `I'm sorry`, co jest równie poprawne. Awers zmieniony na
  `przepraszam (wyrażając żal — jedno słowo)`, żeby odpowiedź była
  jednoznaczna.
- **Usunięta** nota 1791408815153 (EN→PL `you're welcome` → `nie ma za co`):
  wpisał `proszę bardzo` — też w pełni poprawne. "You're welcome" ma w polskim
  kilka równoważnych odpowiedników (`nie ma za co`, `proszę bardzo`, `proszę`),
  więc kierunek EN→PL jest nieocenialny przy dokładnym dopasowaniu stringa.
  Zgodnie z zasadą "pomiń kierunek zwrotny, gdy tłumaczenie nie jest 1:1".
  Kierunek PL→EN (z podpowiedzią) zostaje.

**Wniosek na przyszłość:** przy tworzeniu fiszki sprawdzaj nie tylko czy
`Back` jest poprawne, ale czy **nie istnieje inna równie poprawna odpowiedź**.
Jeśli istnieje — albo podpowiedź na awersie ją odcina, albo kierunek wypada.

## Zidentyfikowane słabe punkty

Po 30 powtórkach (partia 1, wszystkie 20 kart zobaczone, 26/30 poprawnych, 87%):

| Sygnał | Liczba | Ocena |
|---|---|---|
| Realne błędy (`correct:false` + `ease:1`) | 4 | z tego **2 to wady fiszki**, nie błędy ucznia (poprawione wyżej) |
| Wpadki techniczne (`correct:false` + `ease:3/4`) | 0 | — |
| `ease:2` (Hard) | 0 | — |
| Flagi `bad_pronunciation` | 0 | brak sygnału ≠ dowód perfekcji; checkbox nie był użyty ani razu |

Zostają **dwa prawdziwe** punkty obserwacji:

1. **`dobry wieczór` / `dobranoc` (good evening / good night)** — przy
   EN→PL `good evening` wpisał `dobranoc`. Dokładnie ta kolizja, którą
   przewidziałem w uwagach do partii 1. **Bez remediacji na razie:** jedno
   wystąpienie, w dniu pierwszego kontaktu, i sam się poprawił w dwóch
   kolejnych powtórkach tej samej karty (oba razy `correct:true`).
   `PROMPT_NAUCZYCIELA.md` wyraźnie mówi nie uruchamiać remediacji na błędach
   dnia pierwszego. **Jeśli wróci po kilku dniach — wchodzi blok
   kontrastujący pory dnia** (wtedy już w formie zdań, po `to be` z §2).
2. **`goodbye` pisane łącznie** — wpisał `good bye`. To realny fakt
   ortograficzny, nie literówka. Karta zostaje bez zmian, bo właśnie tego ma
   uczyć. Do sprawdzenia w następnej turze, czy się utrwaliło.

Ocena ogólna: materiał partii 1 **opanowany**, nic nie blokuje wejścia w
liczby. Dominują `ease:3/4`, zero flag Hard, zero wpadek technicznych —
polskie diakrytyki i apostrof w `you're welcome` wpisał bezbłędnie, więc
przewidywane ryzyko techniczne się nie zmaterializowało.

## Uwagi

- Do obserwacji w partii 2: pisownia `eight`, `nine`, `three`; w kierunku
  EN→PL polskie ogonki (`pięć`, `sześć`, `dziewięć`, `dziesięć`) — literówki
  tam to wpadki techniczne, próg eskalacji ~20.
- Wymowa: checkbox "Bad pronunciation" nie był użyty ani razu w 30 powtórkach.
  Jeśli to kwestia tego, że użytkownik o nim zapomina — warto przypomnieć, bo
  bez tego sygnału wymiar wymowy jest dla mnie całkowicie niewidoczny.
  Naturalni kandydaci w dotychczasowym materiale: `th` w `thank you` i `three`,
  samogłoska w `evening`, dyftong w `eight`.
