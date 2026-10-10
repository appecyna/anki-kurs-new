# Postęp kursu

Aktualizowane po każdej turze zgodnie z [`PROMPT_NAUCZYCIELA.md`](PROMPT_NAUCZYCIELA.md).

**Kurs wystartował od nowa 2026-10-07** (nowy notatnik "Basic (type in the
answer + pronunciation)" + rejestr odpowiedzi JSONL). Brak wcześniejszego
postępu do uwzględnienia.

## Aktualna pozycja w programie

- **Poziom:** A1
- **Moduł:** §1–§4 domknięte, §5 rozpoczęty (Present Simple)
- **Zrobione:** p. 1 powitania+uprzejmości, p. 2–4 liczby 0–100 + alfabet
  26/26, p. 5–6 `to be` (pełny) + zaimki + a/an/the, p. 7–8 rodzina +
  wygląd + `my`/`your`, p. 9–10 `have got` (pełny) + dom + przymiotniki,
  p. 11 Present Simple (twierdzenia) + czasowniki codzienne
- **Stan decka:** 346 kart (253 PL→EN, 93 EN→PL)
- **Następny krok:** Present Simple — `do`/`does` w przeczeniach i pytaniach
  + krótkie odpowiedzi, jeśli `-s`/`-es`/`-ies` utrzymają się w rejestrze.
  Potem §6 (czas, dni, miesiące) jako materiał na częstotliwość.
- **Ostatnia ocena rejestru:** 2026-10-10, 491 powtórek.
  Per grupa: **§4a 100%, §3 97%, §2 97%, liczby 95%, §4b 92%,
  powitania 88%, alfabet 79%** (alfabet: 75% → **90%** dzień do dnia).
- **Obserwacje w tle** (bez raportowania „nadal czekam"): reguła „u" w
  `four`/`forty`/`fourteen`; podpowiedzi `ay`/`eye`; opuszczanie `got`
  w krótkich odpowiedziach (`Yes, they have.`). (`has` w trzeciej osobie
  potwierdzone 2026-10-09 — zamknięte.)

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

---

## Partia 3 — 2026-10-08 (liczby 11–100, tylko PL→EN)

### Ocena rejestru przed partią (59 powtórek, 43 unikalnych kart)

| Metryka | Wartość |
|---|---|
| Poprawne | **55/59 (93%)** |
| `ease` 1/2/3/4 | 4 / 0 / 13 / **42** |
| Realne błędy (`ease:1`) | 4 — **wszystkie z 2026-10-07**, zero nowych |
| Wpadki techniczne | 0 |
| Flagi `bad_pronunciation` | 0 |

- **29 nowych powtórek od ostatniej tury, zero błędów.** Cztery błędy w
  rejestrze to te same cztery z dnia pierwszego (dwa z nich były wadami
  fiszek, poprawione).
- **Liczby 1–10: 20/20 poprawnie, wszystkie `ease: 4` przy pierwszym
  kontakcie.** Ani jednej pomyłki, ani jednego Hard.
- Oba `zero` (dodane na Twoją uwagę): poprawnie, `ease: 4`.
- Naprawiona fiszka `you're welcome` z podpowiedzią wykluczającą
  („nie «proszę bardzo»"): poprawnie, `ease: 4` — **podpowiedź zadziałała**,
  czyli usunięcie kierunku było przedwczesne. Stąd nowa sekcja o hierarchii
  podpowiedzi w `PROMPT_NAUCZYCIELA.md`.
- 43 unikalne karty w rejestrze przy 42 w decku = 42 aktualne + 1 usunięta
  (historyczna). Wszystkie aktualne karty były co najmniej raz powtarzane.

### Decyzja o tempie: ten materiał jest za łatwy, przyspieszam

Rejestr nie daje żadnego sygnału do remediacji. Przy 20/20 `ease: 4` na
liczbach 1–10 kierunek EN→PL dla liczb jest **kosztem czasu powtórki bez
wartości** — rozpoznawanie jest ewidentnie opanowane, a cała trudność siedzi
w **produkcji i pisowni**. Dlatego partia 3 jest **w całości PL→EN** i za te
same 20 fiszek obejmuje 11–100 zamiast 11–20 w dwóch kierunkach.

To decyzja o tempie, nie o zakresie — zgodnie z zasadą „tempo reguluj, zakresu
nie okrawaj". Żadna pozycja z serii nie wypada.

### Zawartość (20 fiszek, wszystkie PL→EN, `temat::liczby`)

- **11–20:** eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen,
  eighteen, nineteen, twenty
- **Dziesiątki:** thirty, forty, fifty, sixty, seventy, eighty, ninety
- **100:** one hundred — awers `sto (dokładna liczba; nie „a hundred”)`,
  podpowiedź wykluczająca, bo `a hundred` jest równie poprawne w innym
  rejestrze (potocznie, nieprecyzyjnie)
- **Liczby złożone z łącznikiem:** twenty-one, forty-five

Celowo **bez podpowiedzi o łączniku** przy `twenty-one` / `forty-five`.
Pisownia z łącznikiem w 21–99 to sztywna reguła, a nie jedna z kilku
poprawnych opcji — więc pierwsza pomyłka jest tu właściwą lekcją, nie
fałszywym błędem. Jeśli w rejestrze pojawi się `twenty one`, to prawidłowy
sygnał diagnostyczny, nie wada fiszki.

Pułapki ortograficzne, pod które ta partia jest zaprojektowana:
`four` → `fourteen` ale `forty` (bez „u"), `nine` → `nineteen` ale `ninety`
(bez „e"), `five` → `fifteen`/`fifty`, `two` → `twelve`/`twenty`,
`three` → `thirteen`/`thirty`.

### Stan decka po partii 3

| | Liczba |
|---|---|
| Razem | **62 karty** |
| PL→EN | 41 |
| EN→PL | 21 |
| **PL→EN bez audio (do nagrania)** | **20** |

**Do nagrania: 20 plików** — cała partia 3 jest PL→EN, więc każda z tych
fiszek czeka na nagranie.

### Audio i szablon (zweryfikowane 2026-10-08)

Użytkownik dodał nagrania do **wszystkich 21** istniejących fiszek PL→EN i tak
będzie robił dalej; EN→PL świadomie bez audio. Szablon rewersu dostał
`<div class="answer-audio">{{Back}}</div>`, żeby dźwięk dał się odtworzyć.

**Nie zaburza rejestru** — sprawdzone na realnych danych: 0 linii z `sound:`
i 0 z HTML w polu `expected`, czyli `correct` pozostaje wiarygodne. Checkbox
„Bad pronunciation" w szablonie nietknięty. Szczegóły w
[`PROMPT_NAUCZYCIELA.md`](PROMPT_NAUCZYCIELA.md#dźwięk-i-wymowa--audio-stan-od-2026-10-08).

### Zmiany w `PROMPT_NAUCZYCIELA.md` (2026-10-08)

Na podstawie Twoich uwag doszły trzy rzeczy:
1. **„Nie pomijaj materiału oczywistego"** — nowa sekcja. Kognaty,
   internacjonalizmy i pozycje domykające serię zawsze dostają fiszkę.
   Ocena „to oczywiste" jest oceną z mojej perspektywy, nie Twojej.
2. **Hierarchia podpowiedzi** — usunięcie kierunku to ostateczność, nie
   pierwszy ruch. Najlepsza podpowiedź to semantyczna/rejestrowa przez
   wykluczenie konkurenta. Test: czy uczeń wciąż musi wydobyć z pamięci całą
   frazę? Doszła też kontrola jakości: sprawdzaj nie czy `Back` jest poprawne,
   ale czy nie istnieje **inna równie poprawna** odpowiedź.
3. **Sekcja o audio przepisana** pod stan faktyczny (PL→EN tak, EN→PL nie)
   + obowiązek podawania liczby nowych fiszek PL→EN jako porcji pracy.

### Następny krok

Domknięcie §1 (alfabet/literowanie — wymaga osobnego formatu fiszki), potem
**A1 §2: czasownik `to be`, zaimki osobowe, rodzajniki a/an/the** — w tym
`yes`/`no`, odłożone z partii 1. Przy §2 wracam do obu kierunków: zdania z
`to be` to materiał, w którym EN→PL ma realną wartość, bo testuje szyk i
odmianę, a nie samo rozpoznanie słowa.

---

## Partia 4 — 2026-10-08 (wzmocnienie liczb + alfabet)

### Ocena rejestru (104 powtórki, 63 unikalne karty, 74 nowe od ostatniej tury)

| Metryka | Wartość |
|---|---|
| Poprawne | **93/104 (89%)** |
| `ease` 1/2/3/4 | 9 / 0 / 53 / 42 |
| Realne błędy (`ease:1`) | 9 (4 historyczne z 7.10 + **5 nowych**) |
| Wpadki techniczne | 2 (puste odpowiedzi — pominięte wpisywanie) |
| Flagi `bad_pronunciation` | 0 |

Partia 3 (liczby 11–100) przerobiona w całości: 20 kart, 45 powtórek.

### Wzorzec błędów — potwierdzony, nie szum

Pięć nowych błędów, wszystkie na liczbach, i **trzy z nich to jeden spójny
problem**:

| Wpisane | Oczekiwane | Diagnoza |
|---|---|---|
| `forteen` | `fourteen` | **zgubione „u"** |
| `fourty` | `forty` | **dodane „u"** |
| `twenty` | `twelve` | kolizja `tw-` |
| `hundred` | `one hundred` | brak określnika przed 100 |
| `one hundreed` | `one hundred` | literówka |

`forteen` + `fourty` to **ta sama reguła pomylona w obie strony w jednej
sesji** — `four` zachowuje „u" w `fourteen`, ale traci je w `forty`. To nie
jest przypadkowa literówka, tylko nieopanowana reguła ortograficzna, i dokładnie
pod tę pułapkę partia 3 była zaprojektowana. Zadziałała jako diagnostyka.

### Decyzja: wzmocnienie punktowe, nie pełna remediacja

Błędy padły w dniu pierwszego kontaktu, co zgodnie z
[`PROMPT_NAUCZYCIELA.md`](PROMPT_NAUCZYCIELA.md) samo nie uzasadnia remediacji.
Ale wzorzec `four`/`forty`/`fourteen` jest **systematyczny i skończony**, a
błąd ortograficzny tego typu dobrze reaguje na kontrast. Dlatego nie buduję
bloku remediacyjnego, tylko dokładam **5 fiszek „pakujących" obie pułapki w
jedną odpowiedź**:

| Fiszka | Co wymusza |
|---|---|
| `czterdzieści cztery` → `forty-four` | `forty` **i** `four` obok siebie, w jednym wpisie |
| `dziewięćdziesiąt dziewięć` → `ninety-nine` | `ninety` (bez „e") i `nine` (z „e") |
| `dwadzieścia dwa` → `twenty-two` | rozbija kolizję `twelve`/`twenty` |
| `pięćdziesiąt pięć` → `fifty-five` | `fifty`/`five` |
| `trzydzieści trzy` → `thirty-three` | `thirty`/`three` |

Każda z nich dodatkowo utrwala łącznik w 21–99, więc jedna fiszka pracuje na
trzech poziomach: pisownia dziesiątki, pisownia jednostki, łącznik.

### Poprawiona fiszka `sto` — mój błąd w podpowiedzi

Awers był: `sto (dokładna liczba; nie „a hundred”)`. Wpisał `hundred`.
Podpowiedź wykluczyła `a hundred`, ale **nie zasygnalizowała, że określnik
jest obowiązkowy** — mogła go wręcz popchnąć do porzucenia go w ogóle.

Nowy awers: `sto (nie „a hundred”, ani samo „hundred”)`. Wyklucza oba błędne
warianty i zostawia `one hundred` jako jedyną możliwość, którą nadal trzeba
wydobyć z pamięci. Zgodne z hierarchią podpowiedzi — wykluczenie konkurenta,
nie podanie odpowiedzi.

### Alfabet — 15 fiszek, domknięcie §1 (część 1/2)

Nazwy liter, których Polak nie odgadnie z pisowni:
`aitch` (H), `double-u` (W), `wye` (Y), `zed` (Z), `cue` (Q), `ar` (R),
`gee` (G), `jay` (J), `kay` (K), `ef` (F), `el` (L), `em` (M), `en` (N),
`ess` (S), `vee` (V).

Format awersu: `nazwa litery: H`. Podpowiedzi tam, gdzie istnieje druga
plauzybilna pisownia — zgodnie z kontrolą jakości z promptu:
- `W (pisownia z łącznikiem)` → odcina `double u` / `double you`
- `Y (nie „why”)` → `why` to inne słowo, pisownia nazwy litery to `wye`
- `Z (wersja brytyjska)` → `zed` vs amerykańskie `zee`; **podpowiedź uczy tu
  realnej różnicy BrE/AmE**, a nie tylko odcina wariant

**Zostaje 11 liter do następnej partii** (A, B, C, D, E, I, O, P, T, U, X) —
pisownia ich nazw jest bardziej regularna (`bee`, `cee`, `dee`, `pee`, `tee`,
`ex` + samogłoski), więc świadomie w drugiej kolejności. To kolejność, nie
okrojenie zakresu — alfabet będzie kompletny (26/26).

### Stan decka po partii 4

| | Liczba |
|---|---|
| Razem | **82 karty** |
| PL→EN | 61 |
| EN→PL | 21 |
| `temat::liczby` | 47 |
| `temat::alfabet` | 15 |
| **PL→EN bez audio (do nagrania)** | **20** |

Audio do partii 3 już uzupełnione (HyperTTS) — brakuje tylko tych 20 z partii 4.

### Następny krok

Domknięcie alfabetu (11 liter) **+ start A1 §2: `to be`, zaimki osobowe,
rodzajniki a/an/the**, w tym odłożone `yes`/`no` i `excuse me` (EN→PL).
Od §2 **powrót do obu kierunków** — w zdaniach z `to be` EN→PL testuje szyk
i odmianę, a nie samo rozpoznanie słowa, więc kierunek zwrotny znów ma
wartość. Uwaga przy projektowaniu: `you` → `ty`/`wy` i `it` → `to`/`ono` są
niejednoznaczne w EN→PL, więc albo podpowiedź, albo tylko PL→EN.

---

## Partia 5 — 2026-10-09 (A1 §2: `to be`, zaimki, rodzajniki)

### Ocena rejestru (178 powtórek, 83 unikalne karty, 74 nowe)

| Metryka | Wartość |
|---|---|
| Poprawne | 153/178 (86%) |
| `ease` 1/2/3/4 | 22 / 0 / 108 / 48 |
| Realne błędy | 22 |
| Wpadki techniczne | 3 (puste odpowiedzi) |
| Flagi `bad_pronunciation` | 0 |

Spadek z 89% na 86% **nie jest regresem** — jest w całości wytłumaczony przez
jedną grupę fiszek:

| Grupa | Powtórki | Realne błędy | Skuteczność |
|---|---|---|---|
| **Alfabet (nazwy liter)** | 44 | **12** | **73%** |
| Reszta decka | 134 | 10 | **93%** |

### Post-mortem: fiszki z nazwami liter były moim błędem projektowym

Użytkownik zapytał, skąd wziął się pomysł na nazwy liter. Zapis dla potomności:
`PROGRAM.md` A1 §1 wymienia „alfabet", a ja **wymusiłem go w domyślnym
formacie typed-answer**, mimo że ten sam `POSTEP.md` dwie partie wcześniej
notował, że „alfabet/literowanie wymaga osobnego formatu fiszki". Zauważyłem
problem i go zignorowałem.

Rejestr pokazuje, **jak** to nie działa — liczy się treść błędów, nie ich liczba:

| Wpisane | Oczekiwane |
|---|---|
| `kju` | `cue` |
| `wi`, `wee`, `wii` | `vee`, `double-u` |
| `zet` | `zed` |
| `es` (×2) | `ess` |
| `key` | `kay` |
| `way`, `yaj` | `wye` |
| `aich`, `eg` | `aitch` |

To **nie są błędy wiedzy**. `kju` znaczy, że użytkownik wie, że Q czyta się
/kjuː/ — czyli zna dokładnie to, co fiszka miała nauczyć. Zapisuje tę wiedzę
polską transkrypcją fonetyczną, a system liczy mu to jako pomyłkę, bo
oczekuje angielskiej **konwencji ortograficznej nazwy litery** (`cue`, `vee`,
`zed`, `ess`) — czegoś, czego praktycznie nigdy nie będzie pisał.

Czyli fiszka testuje umiejętność, która nie jest celem (pisownia nazwy litery),
a nie testuje tej, która jest celem (rozpoznanie i wymówienie litery przy
literowaniu nazwiska czy adresu e-mail). Typed-answer nie ma rozpoznawania
mowy, więc **tej umiejętności nie da się w tym medium zmierzyć** — i trzeba to
przyznać, zamiast podstawiać surogat.

**Wniosek metodyczny, do przestrzegania:** jeśli umiejętność docelowa jest
ustna, a jedyny dostępny test jest pisemny, to nie wolno testować „czegoś
obok" tylko dlatego, że da się to wpisać. Lepiej dostarczyć wiedzę w innej
formie (materiał referencyjny do przeczytania raz, plus audio) niż produkować
fiszki generujące fałszywe błędy, które zatruwają diagnostykę całego decka.

**Status:** 15 fiszek alfabetu zostaje na razie w decku, decyzja o ich
zawieszeniu przekazana użytkownikowi (zawieszenie jest odwracalne, usunięcie
niszczy też dograne audio). **11 brakujących liter świadomie NIE zostało
dodanych** — nie powtarzam błędu, dopóki nie ma decyzji o formacie.

### Pozostałe sygnały z rejestru

- `forteen` → `fourteen` **powtórzone 9.10**, czyli reguła „u" jeszcze nie
  siedzi. Fiszki kontrastowe z partii 4 (`forty-four` itd.) były wtedy świeżo
  dodane i jeszcze nie weszły w cykl — ocena ich skuteczności w następnej turze.
  Jeśli `forteen` wróci po nich, wchodzi właściwa remediacja.
- Pozostałe błędy to te same historyczne pozycje, bez nowych wzorców.
- Audio: **0 fiszek PL→EN bez nagrania** — użytkownik nadążył z całą partią 4.

### Zawartość partii 5 — 32 fiszki (19 PL→EN, 13 EN→PL)

Start A1 §2. Powrót do obu kierunków, bo w zdaniach z `to be` kierunek
zwrotny testuje szyk i odmianę, a nie samo rozpoznanie słowa.

- **Zaimki osobowe (13):** ja/I, ty/you, on/he, ona/she, to-ono/it, my/we,
  wy/you, oni/they. EN→PL tylko dla jednoznacznych (`I`, `he`, `she`, `we`,
  `they`), bo `you` → `ty`/`wy` i `it` → `to`/`ono` nie są 1:1.
  Fiszka `wy` → `you` jest celowa: uczy, że **angielski ma jedną formę** dla
  liczby pojedynczej i mnogiej.
- **`to be` w zdaniach (11):** I am tired. / You are ready. / He is here. /
  She is happy. / We are late. / They are hungry. — PL→EN dla wszystkich,
  EN→PL tylko tam, gdzie polskie zdanie nie jest zależne od rodzaju
  (`On jest tutaj.`, `Ona jest szczęśliwa.`).
- **Rodzajniki a/an (6):** It is a cat. / It is an apple. / It is a car. —
  kontrast `a` przed spółgłoską vs `an` przed samogłoską, osadzony w zdaniu
  z `to be`, oba kierunki.
- **Odłożone pozycje domknięte (5):** tak/yes, nie/no (oba kierunki) oraz
  `excuse me` → `przepraszam` tylko EN→PL, zgodnie z planem z partii 1.

**Wszystkie 9 zdań PL→EN mają podpowiedź `(forma pełna, bez skrótu)`** —
bez niej `I'm tired.` byłoby równie poprawne jak `I am tired.`, a to dokładnie
ten typ wady, który w partii 1 wyprodukował fałszywy błąd `I'm sorry`.
Podpowiedź jednocześnie sygnalizuje, że forma skrócona istnieje.

### Stan decka po partii 5

| | Liczba |
|---|---|
| Razem | **114 kart** |
| PL→EN / EN→PL | 80 / 34 |
| `temat::zaimki-osobowe` | 13 |
| `temat::czasownik-to-be` | 11 |
| `temat::rodzajniki` | 6 |
| `temat::tak-nie` | 4 |
| `temat::alfabet` | 15 (status do decyzji) |
| **PL→EN bez audio (do nagrania)** | **19** |

### Następny krok

Dokończenie §2: przeczenia (`I am not…`) i pytania (`Are you…?`, `Is he…?`)
razem z krótkimi odpowiedziami (`Yes, I am.` / `No, he isn't.`) — tu `yes`/`no`
z tej partii zaczynają pracować w kontekście. Potem `the` w opozycji do
`a`/`an`. Alfabet wraca tylko wtedy, gdy ustalimy dla niego format inny niż
wpisywanie nazw liter.

### Uzupełnienie partii 5 — alfabet domknięty 26/26 (decyzja użytkownika, 2026-10-09)

Zgłosiłem zastrzeżenie do formatu (patrz post-mortem wyżej) i przedstawiłem
trzy opcje. **Użytkownik wybrał: zostawić 15 istniejących i dodać 11
brakujących.** To jego rozstrzygnięcie, więc format zostaje i **nie wracam
do tej dyskusji**.

Dodane 11 liter (PL→EN, `temat::alfabet`):
`ay` (A), `bee` (B), `cee` (C), `dee` (D), `ee` (E), `eye` (I), `oh` (O),
`pee` (P), `tee` (T), `you` (U), `ex` (X).

Przy tych literach podpowiedzi wykluczające mają **realną wartość
dydaktyczną**, większą niż w pierwszej piętnastce: nazwy liter są homofonami
częstych angielskich słów, więc wykluczenie uczy pary.

| Fiszka | Podpowiedź | Czego uczy |
|---|---|---|
| B | `(nie „be”)` | `bee` (pszczoła) ≠ `be` |
| C | `(nie „see”)` | `cee` ≠ `see` (widzieć) |
| T | `(nie „tea”)` | `tee` ≠ `tea` (herbata) |
| P | `(nie „pea”)` | `pee` ≠ `pea` (groszek) |
| U | `(nie samo „u”)` | nazwa litery U to `you` |
| I | `(nie samo „i”)` | nazwa litery I to `eye` |
| A, E, O | `(nie samo „a/e/o”)` | `ay`, `ee`, `oh` |

Skuteczność grupy `temat::alfabet` **monitoruję osobno** w kolejnych turach —
jeśli dalej będzie odstawać od reszty decka, raportuję liczbę bez ponownego
podważania decyzji.

### Stan decka po uzupełnieniu

| | Liczba |
|---|---|
| Razem | **125 kart** |
| `temat::alfabet` | **26 (pełny)** |
| **PL→EN bez audio (do nagrania)** | **30** (19 z §2 + 11 liter) |

---

## Partia 6 — 2026-10-09 (§2: przeczenia, pytania, krótkie odpowiedzi, `the`)

### Ocena rejestru (245 powtórek, 126 unikalnych kart, 67 nowych)

Ogółem 212/245 (87%), `ease` 1/2/3/4 = 30/0/138/77, 3 wpadki techniczne,
0 flag wymowy. Rozbicie na grupy — zgodnie z ustaleniem alfabet raportowany
osobno:

| Grupa | Powtórki | Realne błędy | Skuteczność |
|---|---|---|---|
| **§2 (`to be`, zaimki, rodzajniki)** | 35 | 1 | **97%** |
| Liczby | 98 | 6 | **94%** |
| Powitania / uprzejmości | 36 | 4 | **89%** |
| **Alfabet** | 76 | **19** | **75%** |

Alfabet odpowiada za **19 z 30 wszystkich realnych błędów (63%)** przy 31%
powtórek. Zgodnie z decyzją z 2026-10-09 raportuję liczbę i nie wracam do
dyskusji o formacie. Reszta decka trzyma 89–97%.

Nowy start §2 jest najmocniejszą grupą w całym decku (97%) — materiał
gramatyczny wchodzi lepiej niż leksyka.

### Fiszki kontrastowe z partii 4 — werdykt wstrzymany, ale rokuje dobrze

Wszystkie 5 fiszek (`forty-four`, `ninety-nine`, `twenty-two`, `fifty-five`,
`thirty-three`) powtórzone **9 razy, 9/9 poprawnie**.

Chronologia `fourteen` jest pouczająca:

| Czas | Wpisane |
|---|---|
| 08.10 21:38 | `forteen` ❌ |
| 08.10 21:40 / 21:43 | `fourteen` ✓ ✓ |
| **09.10 21:30** | `forteen` ❌ (**przed** powtórką fiszek kontrastowych) |
| 09.10 21:32–21:39 | fiszki kontrastowe, 9/9 ✓ |
| **09.10 21:37** | `fourteen` ✓ (**po** `forty-four` o 21:35) |

Czyli błąd wrócił w dniu drugim, ale **przed** kontaktem z fiszkami
kontrastowymi, a po nich odpowiedź była poprawna. To jedna obserwacja, nie
dowód. **Decyzja: nadal bez remediacji** — rozstrzygające będzie, czy
`forteen` pojawi się w kolejnej sesji, gdy fiszki kontrastowe będą już
zadomowione w cyklu.

### Dwie wady fiszek wykryte i naprawione

1. **`To jest…` → `It is…` vs `This is…`** (3 fiszki). Wpisał
   `This is a car.` zamiast `It is a car.` — i **miał rację**, polskie
   „To jest samochód." znaczy jedno i drugie. Moja wada, nie jego błąd.
   Awersy dostały podpowiedź wykluczającą `nie „This is…”` (fiszki
   `kot`, `jabłko`, `samochód`). Konstrukcja `This is…` wejdzie później,
   gdy da się ją osadzić w polskim zdaniu, które wymusza wskazanie
   (np. z zaimkiem dzierżawczym: „To jest mój kot." → „This is my cat.").
2. **Kolizja `ay` (A) ↔ `eye` (I)** — wpisał `eye` na literę A i `ay` na
   literę I, czyli pomylił, która litera ma którą nazwę. Pułapkę stworzyłem
   sam, dodając obie w jednej partii z podpowiedziami, które nie odróżniały
   ich od siebie (`nie samo „a”` / `nie samo „i”`). Podpowiedzi zmienione na
   wzajemnie wykluczające: `A (nie „eye”, nie samo „a”)` i
   `I (nie „ay”, nie samo „i”)`.

Pozostałe błędy alfabetu (`ju`→`you`, `eks`→`ex`, `zet`→`zed`, `es`→`ess`,
`wi`/`wee`→`vee`, `yaj`/`way`→`wye`) to ten sam, znany wzorzec polskiej
transkrypcji fonetycznej — oczekiwana właściwość formatu, bez działań.

### Zawartość partii 6 — 30 fiszek (26 PL→EN, 4 EN→PL)

Domknięcie §2 wokół `to be`:

- **Przeczenia (9):** I am not tired. / He is not here. / She is not hungry. /
  We are not late. / They are not ready. / It is not a cat. / It is not an
  apple. + EN→PL dla dwóch jednoznacznych.
- **Pytania (8):** Are you ready? / Is he here? / Is she happy? /
  Are they hungry? / Is it a cat? / Is it an apple? / Are we late? /
  **Am I late?** — inwersja we wszystkich trzech osobach.
- **Krótkie odpowiedzi (8):** Yes, I am. / No, I am not. / Yes, he is. /
  No, he is not. / Yes, they are. / No, they are not. / Yes, it is. /
  No, it is not. Tu `yes`/`no` z partii 5 zaczynają pracować w kontekście.
- **Rodzajnik `the` (5):** The sun is hot. / The moon is big. (oba kierunki)
  + fiszka kontrastowa **`It is a car. The car is red.`** — pierwsza
  wzmianka `a`, druga `the` w jednym wpisie. To sedno różnicy, więc warte
  dłuższej odpowiedzi.

**Decyzja projektowa: pytania i krótkie odpowiedzi tylko PL→EN.** W kierunku
EN→PL polski szyk i leksyka są zbyt swobodne dla dokładnego dopasowania
stringa — `Is he here?` to równie dobrze „Czy on jest tutaj?" jak „Czy on tu
jest?", więc kierunek zwrotny produkowałby fałszywe błędy. EN→PL zostaje
tylko przy zdaniach twierdzących i przeczących o ustalonym szyku.

Wszystkie zdania z formą pełną `am not` / `is not` / `are not` mają
podpowiedź `(forma pełna, bez skrótu)` — bez niej `I'm not` i `isn't` byłyby
równie poprawne.

### Stan decka po partii 6

| | Liczba |
|---|---|
| Razem | **155 kart** |
| PL→EN / EN→PL | 117 / 38 |
| `temat::czasownik-to-be` | 28 |
| `temat::alfabet` | 26 |
| `temat::liczby` | 47 |
| `temat::rodzajniki` | 11 |
| `temat::przeczenia` / `pytania` / `krotkie-odpowiedzi` | 9 / 8 / 8 |
| **PL→EN bez audio (do nagrania)** | **26** |

### Następny krok

§2 jest materiałowo domknięte poza `the` (dopiero 11 fiszek, w tym tylko
jedna kontrastowa `a` → `the`) — więc albo rozszerzenie rodzajników, albo
przejście do **A1 §3: rodzina, wygląd, podstawowe przymiotniki**, które da
`to be` naturalny materiał leksykalny do pracy („My sister is tall.").
Decyzja po następnej ocenie rejestru: jeśli przeczenia i pytania wejdą tak
dobrze jak reszta §2, idę w §3 i rodzajniki dociągam po drodze w zdaniach.

---

## Partia 7 — 2026-10-09 (A1 §3: rodzina, wygląd, przymiotniki)

### Ocena rejestru (279 powtórek, 34 nowe)

| Grupa | Powtórki | Realne błędy | Skuteczność |
|---|---|---|---|
| **§2a (`to be`, zaimki, a/an)** | 35 | 1 | **97%** |
| **§2b (przeczenia, pytania, krótkie odp., `the`)** | 34 | 1 | **97%** |
| Liczby | 98 | 6 | **94%** |
| Powitania / uprzejmości | 36 | 4 | **89%** |
| Alfabet | 76 | 19 | **75%** (raportowane osobno, bez działań) |

**Partia 6 przerobiona w całości** — wszystkie 30 kart powtórzone, 34
powtórki, tylko **dwie** odpowiedzi niepoprawne. Przeczenia, pytania,
inwersja i krótkie odpowiedzi weszły tak samo dobrze jak twierdzenia (97%),
co potwierdza wniosek z poprzedniej tury: materiał gramatyczny wchodzi
lepiej niż leksyka. Decyzja o przejściu do §3 bez utrwalania §2 — podjęta.

### Dwie niepoprawne odpowiedzi z partii 6

| Wpisane | Oczekiwane | `ease` | Ocena |
|---|---|---|---|
| `The Sun is hot.` | `The sun is hot.` | 1 | kalka z polskiego — patrz niżej |
| `Are they hungry.` | `Are they hungry?` | 3 | wpadka techniczna (brak znaku pytania), bez działań |

**`The Sun` → `the sun`** to transfer z polskiego, gdzie „Słońce" i „Księżyc"
pisze się często wielką literą. W codziennym angielskim `sun`, `moon` i
`earth` są **małą literą**; wielka pojawia się tylko w rejestrze
astronomicznym (*the Sun is a G-type star*). Fiszka zostaje bez zmian, bo
uczy normy A1. Odnotowane jako punkt do obserwacji — jeśli wróci, rozważę
podpowiedź, ale na razie to jednorazowy błąd dnia pierwszego.

### `forteen` — brak nowych danych

Karta `fourteen` **nie była powtarzana** od 09.10 21:37, więc rozstrzygnięcie
nadal wisi. Fiszki kontrastowe stoją na 9/9. Sprawdzam dalej w następnej turze.

### Kolizja `ay` / `eye` — poprawka jeszcze nieprzetestowana

Ważne dla interpretacji: wszystkie błędy tej pary (22:01 i wcześniej)
**poprzedzają** moją poprawkę podpowiedzi, którą wprowadziłem dopiero po
tych powtórkach. Trzy ostatnie próby (22:01) były poprawne, czyli
użytkownik poprawił się sam, **bez** udziału nowych podpowiedzi. Skuteczności
poprawki jeszcze nie znam — nie przypisuję sobie tego sukcesu.

### Zawartość partii 7 — 30 fiszek (20 PL→EN, 10 EN→PL)

Start A1 §3. Słownictwo osadzone w `to be`, żeby §2 pracowało dalej zamiast
zastygnąć.

- **Rodzina, 10 rzeczowników w obu kierunkach (20):** mother, father, sister,
  brother, daughter, son, parents, wife, husband, family.
  `matka` i `ojciec` mają podpowiedź `(formalnie, nie „mum”/„dad”)` —
  bez niej formy potoczne byłyby równie poprawne.
- **Przymiotniki wyglądu (4, PL→EN):** tall, short, young, old.
  `wysoki (o człowieku, nie „high”)` i `niski (o wzroście, nie „low”)` —
  podpowiedzi wykluczające, bo polskie przymiotniki nie rozróżniają tego,
  co angielskie `tall/high` i `short/low`. **To jest realna pułapka dla
  Polaka**, nie formalność.
- **Zdania z rodziną (4, PL→EN):** My sister is tall. / My brother is not
  tall. / Is your sister young? / My family is big. — twierdzenie, przeczenie
  i pytanie na nowym słownictwie.
- **Zaimki dzierżawcze `my` / `your` (2, PL→EN)** — patrz niżej.

### Odstępstwo od programu: `my`/`your` wyciągnięte z A2 §9

`PROGRAM.md` umieszcza zaimki dzierżawcze w **A2 §9**. Wyciągam `my` i `your`
do przodu, bo **słownictwo rodzinne jest bez nich bezużyteczne** — nie da się
powiedzieć nic naturalnego o rodzinie bez „mój/twój", a „The sister is tall."
to zdanie, którego nikt nie wypowie. To dwie fiszki, nie cały temat:
`his`/`her`/`our`/`their` i `whose` zostają w A2 §9 zgodnie z programem.

Podpowiedź `(przed rzeczownikiem)` odcina `mine`/`yours` — formy samodzielne
wejdą razem z resztą tematu w A2.

### Stan decka po partii 7

| | Liczba |
|---|---|
| Razem | **185 kart** |
| PL→EN / EN→PL | 137 / 48 |
| `temat::rodzina` | 24 |
| `temat::przymiotniki` | 4 |
| `temat::zaimki-dzierzawcze` | 2 |
| **PL→EN bez audio (do nagrania)** | **20** |

Audio do partii 6 uzupełnione — brakuje tylko tych 20 z partii 7.

### Następny krok

Dokończenie §3: pozostałe słownictwo rodzinne (grandmother, grandfather,
child/children, aunt, uncle, cousin) + rozszerzenie przymiotników
(beautiful, handsome, thin, slim, dark-haired, blonde) i opisywanie wyglądu
w zdaniach. Potem §4 (`have got`, dom i przedmioty), gdzie `have got` da
pierwszy czasownik poza `to be`.

---

## Partia 8 — 2026-10-09 (§3 ciąg dalszy: dalsza rodzina, wygląd)

### Ocena rejestru (311 powtórek, 32 nowe)

| Grupa | Powtórki | Błędy | Wpadki tech. | Skuteczność |
|---|---|---|---|---|
| **§3 (rodzina, wygląd)** | 32 | 1 | 1 | **97%** |
| §2b (przeczenia, pytania, krótkie odp., `the`) | 34 | 1 | 1 | **97%** |
| §2a (`to be`, zaimki, a/an) | 35 | 1 | 0 | **97%** |
| Liczby | 98 | 6 | 3 | **94%** |
| Powitania / uprzejmości | 36 | 4 | 0 | **89%** |
| Alfabet | 76 | 19 | 0 | **75%** (osobno, bez działań) |

**Partia 7 przerobiona w całości** (30/30 kart). Trzy ostatnie partie trzymają
równe 97% — tempo jest właściwe, nic nie wymaga utrwalania.

### Trzy otwarte pytania z poprzedniej tury — rozstrzygnięte

**1. `forteen` — werdykt niemożliwy dzisiaj, bo karta jest zaplanowana na jutro.**
Sprawdzone bezpośrednio w harmonogramie Anki, nie zgadywane:

| Pole karty `fourteen` | Wartość |
|---|---|
| `interval` | 1 dzień |
| `reps` / `lapses` | 5 / 1 |
| `prop:due` | **=1, czyli jutro** |

Od ostatniej poprawki (09.10 21:37, poprawnej) karta nie wróciła do kolejki i
nie wróci przed jutrem. Fiszki kontrastowe stoją na **11/11 poprawnie**
(`forty-four` ×2, `ninety-nine`, `twenty-two`, `fifty-five` ×2,
`thirty-three` ×2 + `forty` ×2). Rozstrzygnięcie w następnej turze —
to ograniczenie harmonogramu SRS, nie brak danych do analizy.

**2. Podpowiedzi `ay`/`eye` — nadal nieprzetestowane, potwierdzone znacznikami czasu.**
Poprawkę wprowadziłem **09.10 o 22:04:32**. Wszystkie powtórki tej pary
odbyły się **22:01:22 i wcześniej**. Czyli każda obserwacja — i te błędne, i
trzy poprawne na końcu — pochodzi z okresu *przed* poprawką. Użytkownik
poprawił się sam; nowym podpowiedziom nie przypisuję żadnej zasługi.

**3. `The Sun` → `the sun` — zamknięte, nie wróciło.**
Po błędzie o 22:35 karta wróciła dwa razy (22:36 i 22:40) i **oba razy była
poprawna**. Klasyczny błąd dnia pierwszego, który opadł sam. Bez działań.

### Wada fiszki wykryta i naprawiona

Jedyny realny błąd partii 7: `mama` wpisane przy `mother` → oczekiwano
`matka`. **To moja wada** — ostrzegałem przed tym ryzykiem w poprzedniej
turze i go nie zabezpieczyłem. „Mother" to po polsku równie dobrze „mama",
zwłaszcza w mowie potocznej.

Naprawione **oba** kierunki zagrożone tą samą niejednoznacznością:
- `mother (formalnie, nie „mama”)` → `matka`
- `father (formalnie, nie „tata”)` → `ojciec`

Lustrzane podpowiedzi istniały już w kierunku PL→EN (`matka (formalnie, nie
„mum”)`), więc teraz para jest symetryczna. Drugi „błąd" to `son.` z kropką
przy `ease: 4` — wpadka techniczna, bez działań.

### Zawartość partii 8 — 30 fiszek (22 PL→EN, 8 EN→PL)

- **Dalsza rodzina (13):** grandmother, grandfather, child, children, aunt,
  uncle + `cousin`. `babcia`/`dziadek` z podpowiedzią `(nie „grandma”/„grandpa”)`.
  **`cousin` tylko PL→EN** — angielski nie rozróżnia rodzaju, więc EN→PL
  („kuzyn" czy „kuzynka"?) byłoby nieocenialne.
- **Przymiotniki wyglądu (6, PL→EN):** beautiful, handsome, slim, strong,
  pretty, small. Podpowiedzi wykluczające na parach, które polski zlewa w
  jedno słowo: `piękny (nie „pretty”)`, `ładny (nie „beautiful”)`,
  `szczupły (nie „thin”)`, `mały (nie „little”)`.
- **Części ciała / wygląd (4):** `hair`, `eyes` — oba kierunki.
  **`włosy` → `hair` to osobna lekcja gramatyczna**: polski ma liczbę mnogą,
  angielski rzeczownik niepoliczalny w liczbie pojedynczej.
- **Zdania opisujące (7, PL→EN):** My grandmother is old. / My grandfather is
  not tall. / Is your brother handsome? / My sister is beautiful. /
  My children are small. / My eyes are blue. / My father is strong. —
  twierdzenia, przeczenie i pytanie na nowym słownictwie.

`blue` pojawia się tu po raz pierwszy, w zdaniu, a nie jako samodzielna
fiszka — kolory mają własny moduł (§9) i tam wejdą systematycznie.

### Stan decka po partii 8

| | Liczba |
|---|---|
| Razem | **215 kart** |
| PL→EN / EN→PL | 159 / 56 |
| `temat::rodzina` | 44 |
| `temat::wyglad` | 21 |
| `temat::przymiotniki` | 10 |
| `temat::czasownik-to-be` | 39 |
| **PL→EN bez audio (do nagrania)** | **22** |

### Następny krok

§3 jest materiałowo domknięte. Dalej **A1 §4: `have got`, przedmioty
codzienne, dom i pokoje** — `have got` to pierwszy czasownik poza `to be`,
więc partia będzie budowana ostrożnie: najpierw twierdzenia w trzech osobach
(`I have got` / `he has got`), bez przeczeń i pytań, które wchodzą dopiero
po utrwaleniu formy `has` w trzeciej osobie. Uwaga przy projektowaniu:
`have got` vs `have` (AmE) jest niejednoznaczne — podpowiedź musi wymusić
jeden wariant.

---

## Partia 9 — 2026-10-09 (A1 §4: `have got`, dom, przedmioty)

### Ocena rejestru (344 powtórki, 33 nowe)

| Grupa | Powtórki | Błędy | Skuteczność |
|---|---|---|---|
| §3b (dalsza rodzina, wygląd) | 33 | 1 | **97%** |
| §3a (rodzina, wygląd) | 32 | 1 | **97%** |
| §2b (przeczenia, pytania, krótkie odp.) | 34 | 1 | **97%** |
| §2a (`to be`, zaimki, a/an) | 35 | 1 | **97%** |
| Liczby | 98 | 6 | 94% |
| Powitania / uprzejmości | 36 | 4 | 89% |
| Alfabet | 76 | 19 | 75% (osobno) |

Partia 8 przerobiona w całości. **Cztery kolejne partie na równym 97%.**

### Wzorzec, który trafia mnie trzeci raz: polskie pary formalna/potoczna

Jedyny realny błąd: `ciocia` wpisane przy `aunt` → oczekiwano `ciotka`.
To **trzeci raz** ta sama wada w moich fiszkach (wcześniej `mama`/`matka`
i prewencyjnie `tata`/`ojciec`). Polskie nazwy członków rodziny prawie
zawsze mają parę **formalna / potoczna**, a potoczna jest w mowie
częstsza — więc jako odpowiedź EN→PL jest równie poprawna.

Naprawione: `aunt (formalnie, nie „ciocia”)`, `uncle (nie „wuj”)`.
Zasada dopisana do [`PROMPT_NAUCZYCIELA.md`](PROMPT_NAUCZYCIELA.md), żeby nie
powtarzać tego przy kolejnych rzeczownikach pokrewieństwa.

Drugi „błąd": `wójek` zamiast `wujek` przy `ease: 4` — polska literówka,
wpadka techniczna, bez działań.

### Zawartość partii 9 — 31 fiszek (19 PL→EN, 12 EN→PL)

Start §4. Zgodnie z planem z poprzedniej tury: **`have got` tylko w
twierdzeniach**, bez przeczeń i pytań, dopóki `has` w trzeciej osobie
nie usiądzie.

- **`have got`, 7 zdań (PL→EN):** I have got a cat. / You have got a car. /
  He has got a sister. / She has got a brother. / We have got a house. /
  They have got children. / My sister has got a dog.
  **`has` występuje trzy razy** (he, she, my sister) — to forma, na której
  Polacy się wywracają, więc dostaje najwięcej kontaktu już w pierwszej partii.
- **Dom i przedmioty, 10 rzeczowników w obu kierunkach (20):** house, room,
  kitchen, bathroom, bedroom, table, chair, bed, window, door.
- **Zwierzęta (4):** dog, cat — oba kierunki. `kot` i `pies` istniały do tej
  pory tylko wewnątrz zdań, nie jako samodzielne słówka.

Podpowiedzi wykluczające tam, gdzie polski zlewa dwa angielskie słowa albo
odwrotnie:
- **`(„have got”, forma pełna)` przy wszystkich 7 zdaniach** — bez tego
  `I have a cat.` i `I've got a cat.` byłyby równie poprawne. To była
  pułapka, którą zapisałem sobie do zabezpieczenia w poprzedniej turze.
- `dom (nie „home”)` → `house` — `house` to budynek, `home` to miejsce
  zamieszkania; polski „dom" znaczy jedno i drugie.
- `pokój (w domu)` → `room` — odcina „pokój" w znaczeniu „pokój/spokój".
- `drzwi (liczba pojedyncza w angielskim)` → `door` — polski ma tylko liczbę
  mnogą, angielski rozróżnia `door`/`doors`. Ten sam typ niezgodności co
  `włosy` → `hair` z partii 8.

### Stan decka po partii 9

| | Liczba |
|---|---|
| Razem | **246 kart** |
| PL→EN / EN→PL | 178 / 68 |
| `temat::have-got` | 7 |
| `temat::dom` | 20 |
| `temat::zwierzeta` | 4 |
| **PL→EN bez audio (do nagrania)** | **19** |

### Następny krok

Rozszerzenie `have got`: **przeczenia (`have not got` / `has not got`) i
pytania (`Have you got…?` / `Has he got…?`) z krótkimi odpowiedziami** —
ale tylko jeśli rejestr pokaże, że `has` w trzeciej osobie siedzi. Jeśli
będzie się mylić z `have`, najpierw więcej twierdzeń w trzeciej osobie.
Potem dalsze przedmioty codzienne i pozostałe pomieszczenia.

---

## Partia 10 — 2026-10-09 (§4 rozszerzone: `have got` pełny + dom)

### Ocena rejestru (375 powtórek, 31 nowych)

| Grupa | Powtórki | Błędy | Wpadki tech. | Skuteczność |
|---|---|---|---|---|
| **§4 (`have got`, dom)** | 31 | **0** | 1 | **100%** |
| §3 (rodzina, wygląd) | 65 | 2 | 2 | **97%** |
| §2 (`to be`, zaimki, rodzajniki) | 69 | 2 | 1 | **97%** |
| Liczby | 98 | 6 | 3 | 94% |
| Powitania / uprzejmości | 36 | 4 | 0 | 89% |
| Alfabet | 76 | 19 | 0 | 75% (osobno) |

Partia 9 przerobiona w całości, **zero realnych błędów**. Jedyna niepoprawna
odpowiedź to `We have got aa house.` przy `ease: 4` — podwójna litera,
wpadka techniczna.

### `has` w trzeciej osobie — trzyma, więc rozszerzam

To był warunek z poprzedniej tury. Wszystkie trzy zdania z `has got`
poprawnie przy pierwszym kontakcie, każde na `ease: 4`:

| Zdanie | Wynik |
|---|---|
| He has got a sister. | ✓ `ease: 4` |
| She has got a brother. | ✓ `ease: 4` |
| My sister has got a dog. | ✓ `ease: 4` |

Forma, na której Polacy zwykle się wywracają, nie sprawiła problemu —
decyzja o ostrożnym wprowadzeniu (najpierw same twierdzenia, `has` trzy razy
w siedmiu zdaniach) okazała się wystarczająca. **Wchodzą przeczenia,
pytania i krótkie odpowiedzi.**

### Zawartość partii 10 — 50 fiszek (40 PL→EN, 10 EN→PL)

- **`have got` — przeczenia (7, PL→EN):** I have not got a car. /
  He has not got a brother. / She has not got a dog. / We have not got a
  house. / They have not got children. / My brother has not got a cat. /
  I have not got a key. — `has not` w trzech osobach.
- **`have got` — pytania (7, PL→EN):** Have you got a car? /
  Has he got a sister? / Has she got children? / Have they got a house? /
  Has your brother got a dog? / Have we got a table? / Have you got a mirror?
  — inwersja `Have`/`Has` w obu liczbach.
- **`have got` — krótkie odpowiedzi (6, PL→EN):** Yes, I have. /
  No, I have not. / Yes, he has. / No, he has not. / Yes, they have. /
  No, they have not.
- **Dom, 10 rzeczowników w obu kierunkach (20):** lamp, mirror, wardrobe,
  sofa, carpet, wall, ceiling, garden, floor, key.
- **Zdania łączące (3, PL→EN):** We have got a big garden. /
  She has got a new car. / **My house has got four rooms.** — ta ostatnia
  wciąga liczby z §1 do nowej struktury, żeby stary materiał nie leżał odłogiem.
- **Przymiotniki (7, PL→EN):** new, big, clean, dirty, comfortable,
  expensive, cheap.

Podpowiedzi wykluczające (BrE/AmE i polskie zlewanie się znaczeń):
- `(„have not got” / „have not”, forma pełna)` przy wszystkich przeczeniach
  i krótkich odpowiedziach — odcina `haven't got` oraz amerykańskie
  `I don't have`.
- `szafa (brytyjskie)` → `wardrobe` (nie `closet`),
  `ogród (brytyjskie)` → `garden` (nie `yard`).
- `kanapa (nie „couch”)` → `sofa`, `dywan (na całą podłogę, nie „rug”)`
  → `carpet`, `duży (nie „large”)` → `big`, `drogi (o cenie)` → `expensive`.
- **`floor (część pokoju, nie piętro)` → `podłoga`** — w EN→PL `floor` jest
  niejednoznaczne, bo znaczy też „piętro".

### Stan decka po partii 10

| | Liczba |
|---|---|
| Razem | **296 kart** |
| PL→EN / EN→PL | 218 / 78 |
| `temat::have-got` | 30 |
| `temat::dom` | 43 |
| `temat::przymiotniki` | 17 |
| `temat::przeczenia` / `pytania` / `krotkie-odpowiedzi` | 16 / 15 / 14 |
| **PL→EN bez audio (do nagrania)** | **40** |

**Uwaga o nakładzie pracy:** partia jest w 80% PL→EN, więc to 40 nagrań —
dwa razy więcej niż zwykle. Wynika z charakteru materiału (`have got` ćwiczy
się produkcyjnie, a EN→PL dla zdań z `have got` byłoby nieocenialne przy
swobodnym polskim szyku), nie z przeoczenia.

### Następny krok

§4 domknięte. Dalej **A1 §5: Present Simple** — twierdzenia, przeczenia,
pytania i czasowniki codzienne. To największy skok dotąd: pierwszy czas
z końcówką `-s` w trzeciej osobie i pierwsze `do`/`does` w pytaniach
i przeczeniach. Wprowadzam go tak samo ostrożnie jak `have got`: najpierw
twierdzenia z naciskiem na trzecią osobę, potem reszta po potwierdzeniu
w rejestrze.

---

## Partia 11 — 2026-10-10 (A1 §5: Present Simple, twierdzenia)

### Ocena rejestru (491 powtórek, 57 nowych z 2026-10-10)

| Grupa | Powtórki | Błędy | Wpadki tech. | Skuteczność |
|---|---|---|---|---|
| §4a (`have got` twierdz., dom) | 31 | 0 | 1 | **100%** |
| §3 (rodzina, wygląd) | 66 | 2 | 2 | **97%** |
| §2 (`to be`, zaimki, rodzajniki) | 72 | 2 | 1 | **97%** |
| Liczby | 112 | 6 | 3 | **95%** |
| **§4b (`have got` pełny)** | 62 | 5 | 1 | **92%** |
| Powitania / uprzejmości | 43 | 5 | 1 | 88% |
| Alfabet | 105 | 22 | 0 | 79% |

Partia 10 przerobiona w całości (50/50 kart).

### Alfabet — ocena użytkownika potwierdzona danymi

Użytkownik napisał, że litery „powoli mu się zapamiętują" i że trzeba im dać
czas. Rejestr to potwierdza — rozbicie po dniach:

| Dzień | Powtórki | Błędy | Skuteczność |
|---|---|---|---|
| 2026-10-09 (pierwszy kontakt) | 76 | 19 | **75%** |
| 2026-10-10 | 29 | 3 | **90%** |

**Skok o 15 punktów dzień do dnia.** Łączne 79% to po prostu średnia
obciążona dniem pierwszego kontaktu. Format działa, nic nie wymaga zmiany,
raportuję dalej osobno i bez komentarza.

### §4b na 92% — co dokładnie zawiodło

Pięć realnych błędów. Trzy z nich to **wady moich fiszek**, jeden to realna
luka gramatyczna, jeden to pomyłka leksykalna:

| Wpisane | Oczekiwane | Diagnoza |
|---|---|---|
| `mur` | `ściana` | **wada fiszki** — `wall` to po polsku i „ściana", i „mur" |
| `cupboard` | `wardrobe` | **wada fiszki** — `szafa` to też `cupboard`; moja podpowiedź `(brytyjskie)` odcinała tylko `closet` |
| `Yes, they have got.` (×2) | `Yes, they have.` | **realna luka** — patrz niżej |
| `carpet` | `floor` | pomyłka leksykalna (`podłoga` ≠ `dywan`), fiszka poprawna |

**`Yes, they have got.` to jedyny prawdziwy punkt gramatyczny z tej partii.**
W krótkich odpowiedziach z `have got` **`got` się opuszcza**: „Yes, they
have.", nie „Yes, they have got.". Błąd pojawił się dwa razy w jednej sesji,
czyli jest konsekwentny, a nie przypadkowy. Fiszka uczy poprawnie, więc
zostaje bez zmian i bez podpowiedzi — podpowiedź zepsułaby lekcję.
Do obserwacji przy kolejnym cyklu.

Dodatkowo z 2026-10-10: `you are welcome` zamiast `you're welcome` —
**znowu wada fiszki**, tym razem odwrotna niż zwykle: oczekiwana była forma
**skrócona**, a użytkownik podał pełną, która jest równie poprawna. Wszędzie
indziej wymuszam formę pełną, więc ta jedna fiszka wyłamywała się z konwencji.

`you're wolcome` przy `ease: 3` — literówka, którą użytkownik sam zgłosił
w rozmowie. Wpadka techniczna, nie liczona jako błąd.

### Naprawione fiszki

- `wall (w pomieszczeniu, nie „mur”)` → `ściana`
- `szafa (na ubrania, brytyjskie — nie „cupboard”)` → `wardrobe`
- `nie ma za co (w odpowiedzi na podziękowanie; forma skrócona)` → `you're welcome`

### Zawartość partii 11 — 50 fiszek (35 PL→EN, 15 EN→PL)

Start §5. Zgodnie z planem **tylko twierdzenia** — `do`/`does` w przeczeniach
i pytaniach dopiero po potwierdzeniu, że końcówka `-s` siedzi. Ta sama
ostrożna procedura, która sprawdziła się przy `have got`.

- **Czasowniki codzienne, 12 w obu kierunkach (24):** work, live, eat, drink,
  read, write, like, want, know, study, cook, watch.
  `uczyć się (nie „learn”)` → `study` — jedyna para wymagająca podpowiedzi.
- **Trzecia osoba z `-s`, 12 zdań (PL→EN):** He works. / She lives in Warsaw. /
  My brother reads books. / She writes letters. / He likes coffee. /
  She wants a new car. / My father cooks. / She knows. / He eats an apple. /
  She drinks water. + **dwa przypadki nieregularnej pisowni**:
  - **`She watches TV.`** — końcówka `-es` po `ch`
  - **`He studies English.`** — końcówka `-ies` po spółgłoska + `y`
- **Pozostałe osoby dla kontrastu, 8 zdań (PL→EN):** I work. / I live in
  Poland. / You read books. / We like coffee. / They live in London. /
  We want a new house. / I eat an apple. / They watch TV.
  Kontrast jest celowy: `live`/`lives`, `watch`/`watches`, `eat`/`eats`
  w tej samej partii, żeby `-s` nie zrosło się z czasownikiem jako całość.
- **Rzeczowniki ze zdań jako samodzielne słówka (6):** book, water, coffee —
  oba kierunki. `letter` i `TV` zostają na razie tylko w zdaniach.

Zdania wciągają stary materiał: `an apple` (rodzajniki z §2), `a new car`
i `a new house` (przymiotniki z p. 10), rodzina z §3.

### Stan decka po partii 11

| | Liczba |
|---|---|
| Razem | **346 kart** |
| PL→EN / EN→PL | 253 / 93 |
| `temat::present-simple` | 20 (w tym 12 z `trzecia-osoba`) |
| `temat::czasowniki` | 24 |
| **PL→EN bez audio (do nagrania)** | **35** |

### Następny krok

Rozszerzenie Present Simple: **`do`/`does` w przeczeniach i pytaniach**
+ krótkie odpowiedzi (`Yes, he does.` / `No, I do not.`) — pod warunkiem, że
rejestr pokaże, że `-s`, `-es` i `-ies` w trzeciej osobie trzymają. Jeśli
`watches`/`studies` będą się mylić, najpierw więcej zdań z tymi końcówkami.
Potem §6 (czas, dni tygodnia, miesiące), który da Present Simple naturalny
materiał na określenia częstotliwości.
