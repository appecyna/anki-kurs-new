"""Note type "Basic (type in the answer + pronunciation)".

Same as the stock type-in note type, plus a "Bad pronunciation" checkbox.
Every answer is appended to user_files/<profile>.jsonl
"""

import json
import os
import re
from datetime import datetime

from anki.utils import strip_html
from aqt import gui_hooks, mw

NOTETYPE_NAME = "Basic (type in the answer + pronunciation)"

QFMT = """{{Front}}

{{type:Back}}"""

# {{type:Back}} only renders the typed/expected comparison - Anki strips
# [sound:...] tags out of it, so audio stored in Back is never played.
# {{Back}} below renders the field normally, which gives the replay button
# and lets Anki autoplay it on the answer side.
AFMT = """{{Front}}

<hr id=answer>

{{type:Back}}

<div class="answer-audio">{{Back}}</div>

<div class="pron-check">
  <label>
    <input type="checkbox" onchange="pycmd('talog:badpron:' + (this.checked ? '1' : '0'))">
    Bad pronunciation
  </label>
</div>"""

CSS = """.card {
    font-family: arial;
    font-size: 20px;
    text-align: center;
    color: black;
    background-color: white;
}

.answer-audio {
    margin-top: 0.8em;
}

.pron-check {
    margin-top: 1.5em;
    font-size: 16px;
}"""

ADDON_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(ADDON_DIR, "user_files")

# checkbox state for the card currently being reviewed
_bad_pronunciation = False


def ensure_notetype() -> None:
    mm = mw.col.models
    nt = mm.by_name(NOTETYPE_NAME)
    if nt is None:
        nt = mm.new(NOTETYPE_NAME)
        mm.add_field(nt, mm.new_field("Front"))
        mm.add_field(nt, mm.new_field("Back"))
        tmpl = mm.new_template("Card 1")
        tmpl["qfmt"] = QFMT
        tmpl["afmt"] = AFMT
        mm.add_template(nt, tmpl)
        nt["css"] = CSS
        mm.add_dict(nt)
        return
    # keep an already installed note type in sync with the add-on
    tmpl = nt["tmpls"][0]
    if tmpl["qfmt"] == QFMT and tmpl["afmt"] == AFMT and nt["css"] == CSS:
        return
    tmpl["qfmt"] = QFMT
    tmpl["afmt"] = AFMT
    nt["css"] = CSS
    mm.update_dict(nt)


def _log_path() -> str:
    # active profile name as a slug: lowercase, non-word characters -> "_"
    profile = re.sub(r"\W+", "_", mw.pm.name).strip("_").lower() or "profile"
    return os.path.join(DATA_DIR, profile + ".jsonl")


def on_js_message(handled, message, context):
    if message.startswith("talog:badpron:"):
        global _bad_pronunciation
        _bad_pronunciation = message.endswith("1")
        return (True, None)
    return handled


def on_show_question(card) -> None:
    global _bad_pronunciation
    _bad_pronunciation = False


def on_answer_card(reviewer, card, ease) -> None:
    if card.note_type()["name"] != NOTETYPE_NAME:
        return
    typed = (reviewer.typedAnswer or "").strip()
    back = mw.col.media.strip_av_tags(card.note()["Back"])
    expected = strip_html(back).strip()
    entry = {
        "ts": datetime.now().astimezone().isoformat(timespec="seconds"),
        "card_id": card.id,
        "deck": mw.col.decks.name(card.odid or card.did),
        "typed": typed,
        "expected": expected,
        "correct": typed == expected,
        "bad_pronunciation": _bad_pronunciation,
        "ease": ease,
    }
    path = _log_path()
    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except OSError as exc:
        print("typed_answer_log: could not write %s: %s" % (path, exc))


gui_hooks.profile_did_open.append(ensure_notetype)
gui_hooks.webview_did_receive_js_message.append(on_js_message)
gui_hooks.reviewer_did_show_question.append(on_show_question)
gui_hooks.reviewer_did_answer_card.append(on_answer_card)
