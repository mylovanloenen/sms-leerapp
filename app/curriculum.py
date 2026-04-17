import json
import os
import re

# ── JSON laden ────────────────────────────────────────────────────────────────
_JSON_PATH = os.path.join(os.path.dirname(__file__), "digidoen_curriculum.json")
with open(_JSON_PATH, encoding="utf-8") as _f:
    _CURRICULUM = json.load(_f)["curriculum"]

# ── Talen ─────────────────────────────────────────────────────────────────────
LANGUAGES = {
    "NL": "Nederlands",
    "EN": "English",
    "DE": "Deutsch",
    "FR": "Français",
    "ES": "Español",
}

WELCOME_MESSAGE = (
    "Welkom bij DigiDoen! 👋\n"
    "Kies jouw taal / Choose your language:\n\n"
    "1 - Nederlands\n"
    "2 - English\n"
    "3 - Deutsch\n"
    "4 - Français\n"
    "5 - Español\n"
    "6 - Türkçe\n"
    "7 - العربية\n\n"
    "Stuur het cijfer of de naam van je taal."
)

YES_WORDS = {
    "NL": ["JA", "J", "OK", "OKEY", "ZEKER", "VOLGENDE", "KLAAR", "GELUKT", "VERDER"],
    "EN": ["YES", "Y", "OK", "OKAY", "SURE", "NEXT"],
    "DE": ["JA", "J", "OK", "OKAY", "SICHER", "WEITER"],
    "FR": ["OUI", "O", "OK", "SUIVANT"],
    "ES": ["SÍ", "SI", "S", "OK", "CLARO"],
}

# ── Lessen index (id → dict) ───────────────────────────────────────────────────
_LESSON_BY_ID: dict[str, dict] = {}

# ── Modules opbouwen uit JSON ──────────────────────────────────────────────────
MODULES: list[dict] = []

for _i, _jm in enumerate(_CURRICULUM["modules"]):
    _lesson_ids = []
    _lesson_topics = []

    for _les in _jm["lessen"]:
        _LESSON_BY_ID[_les["id"]] = _les
        _lesson_ids.append(_les["id"])
        # Gebruik leerdoel als les-topic (voor AI-talen)
        _topic = _les.get("leerdoel", _les["titel"])
        _lesson_topics.append({lang: _topic for lang in LANGUAGES})

    # Stappen: één per les + module_complete aan het eind
    _steps = ["lesson"] * len(_lesson_ids) + ["module_complete"]
    _title = _jm["titel"]

    MODULES.append({
        "id": _i + 1,
        "json_id": _jm["id"],
        "title": {lang: _title for lang in LANGUAGES},
        "topic": {lang: _jm.get("beschrijving", _title) for lang in LANGUAGES},
        "lessons": _lesson_topics,
        "lesson_ids": _lesson_ids,
        "steps": _steps,
    })


# ── Hulpfuncties ──────────────────────────────────────────────────────────────

def get_module(module_id: int) -> dict | None:
    for m in MODULES:
        if m["id"] == module_id:
            return m
    return None


def get_step_type(module_id: int, step_nr: int) -> str | None:
    module = get_module(module_id)
    if not module:
        return None
    steps = module["steps"]
    if step_nr < 1 or step_nr > len(steps):
        return None
    return steps[step_nr - 1]


def lesson_index(module_id: int, step_nr: int) -> int:
    """Welk lesnummer is dit binnen de module (1-based)."""
    module = get_module(module_id)
    if not module:
        return 1
    count = sum(1 for s in module["steps"][:step_nr - 1] if s == "lesson")
    return count + 1


def quiz_index(module_id: int, step_nr: int) -> int:
    """Welk quiznummer is dit binnen de module (1-based) — alias van lesson_index."""
    return lesson_index(module_id, step_nr)


def get_lesson_topic(module_id: int, lesson_nr: int, lang: str) -> str:
    """Geeft het onderwerp van les lesson_nr (1-based) in de gegeven taal."""
    module = get_module(module_id)
    if not module or "lessons" not in module:
        return module["topic"].get(lang, "") if module else ""
    lessons = module["lessons"]
    idx = lesson_nr - 1
    if idx < 0 or idx >= len(lessons):
        return module["topic"].get(lang, "")
    return lessons[idx].get(lang, "")


def get_lesson_id_for_step(module_id: int, step_nr: int) -> str | None:
    """Geeft het JSON-les-ID voor een gegeven stap (alleen voor 'lesson' stappen)."""
    module = get_module(module_id)
    if not module or "lesson_ids" not in module:
        return None
    lnr = lesson_index(module_id, step_nr)  # 1-based
    lesson_ids = module["lesson_ids"]
    if 1 <= lnr <= len(lesson_ids):
        return lesson_ids[lnr - 1]
    return None


def get_lesson_by_id(lesson_id: str) -> dict | None:
    return _LESSON_BY_ID.get(lesson_id)


def get_lesson_content(lesson_id: str) -> str | None:
    """Geeft de kant-en-klare SMS-tekst voor deze les."""
    les = _LESSON_BY_ID.get(lesson_id)
    if not les:
        return None
    return les.get("bericht") or les.get("sms_bericht")


def check_lesson_answer(lesson_id: str, text: str) -> tuple[bool, str]:
    """
    Vergelijkt het antwoord met verwacht_antwoord.
    Geeft (correct, feedback) terug.
    'correct' is True als antwoord herkend werd of voortgang_vereist=False.
    """
    les = _LESSON_BY_ID.get(lesson_id)
    if not les:
        return True, "Verder!"

    answer = text.strip().lower()
    expected = [e.lower() for e in les.get("verwacht_antwoord", [])]
    voortgang_vereist = les.get("voortgang_vereist", True)

    matched = not expected or answer in expected or any(e in answer for e in expected)

    if matched or not voortgang_vereist:
        feedback = _pick_good_feedback(les, answer)
        return True, feedback
    else:
        fout = les.get("bij_fout_antwoord", "Probeer opnieuw.")
        return False, fout


def _pick_good_feedback(les: dict, answer: str) -> str:
    """Kies het juiste positieve antwoord op basis van het gegeven woord."""
    if "bij_goed_antwoord_ja" in les and ("ja" in answer or "klaar" in answer or "gelukt" in answer):
        return les["bij_goed_antwoord_ja"]
    if "bij_goed_antwoord_nee" in les and "nee" in answer:
        return les["bij_goed_antwoord_nee"]
    if "bij_goed_antwoord_bezig" in les and ("bezig" in answer or "wacht" in answer):
        return les["bij_goed_antwoord_bezig"]
    return les.get("bij_goed_antwoord", "Goed! Verder naar de volgende les.")


def is_lesson_id(text: str) -> bool:
    """Controleert of een string eruitziet als een JSON les-ID (bijv. M01L02)."""
    return bool(re.match(r'^M\d{2}L\d{2,3}$', text.strip()))


def total_modules() -> int:
    return len(MODULES)


def steps_in_module(module_id: int) -> int:
    module = get_module(module_id)
    return len(module["steps"]) if module else 0


def total_steps() -> int:
    return sum(len(m["steps"]) for m in MODULES)


def completed_steps(module_id: int, step_nr: int) -> int:
    done = 0
    for m in MODULES:
        if m["id"] < module_id:
            done += len(m["steps"])
        elif m["id"] == module_id:
            done += step_nr - 1
    return done


def is_yes(text: str, language: str) -> bool:
    words = YES_WORDS.get(language, YES_WORDS["NL"])
    return text.strip().upper() in words
