"""
State machine: één bericht per interactie, nooit combineren.

Flow per stap:
  lesson (NL)  → stuur kant-en-klare les, wacht op antwoord, geef feedback
  lesson (overig) → AI-gegenereerde les, stap meteen vooruit
  module_complete → toon afronding, wacht op JA, zet dan module vooruit
"""
from datetime import datetime, timezone
from sqlalchemy.orm import Session

from app.models import User
from app.curriculum import (
    LANGUAGES, WELCOME_MESSAGE, get_module, get_step_type,
    total_modules, steps_in_module, is_yes,
    lesson_index, quiz_index, get_lesson_topic,
    get_lesson_id_for_step, get_lesson_content,
    check_lesson_answer, is_lesson_id,
)
from app import ai

RESTART_WORDS = ["RESTART", "OPNIEUW", "NEU", "RECOMMENCER", "REINICIAR"]


def process_message(phone: str, body: str, db: Session) -> str:
    text = body.strip()

    user = db.query(User).filter(User.phone == phone).first()
    if not user:
        user = User(phone=phone, state="LANG_PENDING")
        db.add(user)
        db.commit()
        db.refresh(user)
        return WELCOME_MESSAGE

    user.last_active = datetime.now(timezone.utc)

    # ── RESTART ───────────────────────────────────────────────────
    if text.upper() in RESTART_WORDS:
        user.state = "LANG_PENDING"
        user.language = None
        user.name = None
        user.skill_level = None
        user.module = 1
        user.step = 1
        user.correct_answers = 0
        user.total_questions = 0
        user.pending_quiz_text = None
        user.pending_quiz_correct = None
        db.commit()
        return WELCOME_MESSAGE

    # ── TAAL KIEZEN ───────────────────────────────────────────────
    if user.state == "LANG_PENDING":
        lang = ai.detect_language_from_text(text.strip())
        if lang in LANGUAGES:
            return _start(user, lang, db)
        return "Niet herkend 🤔 Typ je taal, bijv: Nederlands, English, Türkçe, العربية"

    # ── NAAM INVOEREN ─────────────────────────────────────────────
    if user.state == "NAME_PENDING":
        lang = user.language or "NL"
        name = text.strip()
        if not name:
            return ai.ask_name(lang)
        user.name = name
        user.state = "SKILL_PENDING"
        db.commit()
        return ai.ask_skills(lang, name)

    # ── VAARDIGHEDEN INVOEREN ──────────────────────────────────────
    if user.state == "SKILL_PENDING":
        lang = user.language or "NL"
        skill_text = text.strip()
        if not skill_text:
            return ai.ask_skills(lang, user.name or "")
        user.skill_level = skill_text
        # Voor NL altijd starten bij module 1 (vaste volgorde)
        starting_module = 1 if lang == "NL" else ai.assess_starting_module(skill_text, lang)
        user.module = starting_module
        user.step = 1
        user.state = "LEARNING"
        db.commit()
        module = get_module(starting_module)
        module_title = module["title"].get(lang, "") if module else ""
        return ai.welcome_to_module(module_title, user.name or "", lang)

    # ── AAN HET LEREN ─────────────────────────────────────────────
    if user.state == "LEARNING":
        lang = user.language or "NL"
        step_type = get_step_type(user.module, user.step)

        # LESSON ──────────────────────────────────────────────────
        if step_type == "lesson":
            if lang == "NL":
                return _handle_nl_lesson(user, text, db)
            else:
                # Niet-NL: AI-gegenereerde les, meteen verder
                if _is_question(text):
                    reply = _ai_question(user, text, lang)
                    if reply:
                        return reply
                content = _gen_lesson(user, lang)
                _move_next(user, db)
                return content

        # MODULE COMPLETE: wacht op JA ────────────────────────────
        if step_type == "module_complete":
            if not is_yes(text, lang):
                if _is_question(text):
                    reply = _ai_question(user, text, lang)
                    if reply:
                        return reply
                return _gen_module_complete(user.module, lang, name=user.name)

            current_title = _module_title(user.module, lang)
            _move_next(user, db)

            if user.state == "COMPLETED":
                return ai.generate_module_complete(current_title, None, lang, name=user.name)

            # Stuur eerste les van nieuwe module
            if lang == "NL":
                return _handle_nl_lesson(user, text, db)
            else:
                content = _gen_lesson(user, lang)
                _move_next(user, db)
                return content

    # ── KLAAR ─────────────────────────────────────────────────────
    if user.state == "COMPLETED":
        lang = user.language or "NL"
        return _t(lang,
            "All done! 🌟 Reply RESTART to start over.",
            "Alles klaar! 🌟 Stuur OPNIEUW om opnieuw te beginnen.",
            "Fertig! 🌟 Antworten Sie NEU.",
            "Terminé! 🌟 Répondez RECOMMENCER.",
            "¡Listo! 🌟 Responda REINICIAR.")

    return "Er ging iets mis. Stuur OPNIEUW om te herstarten."


# ── NL les-afhandeling ────────────────────────────────────────────────────────

def _handle_nl_lesson(user: User, text: str, db: Session) -> str:
    """
    Interactieve lesflow voor NL:
    - Geen pending → stuur les, sla lesson_id op
    - Pending → evalueer antwoord, geef feedback, zet stap vooruit
    """
    # Wachten op antwoord op een eerder gestuurde les?
    if user.pending_quiz_text and is_lesson_id(user.pending_quiz_text):
        lesson_id = user.pending_quiz_text
        correct, feedback = check_lesson_answer(lesson_id, text)

        if correct:
            user.pending_quiz_text = None
            user.pending_quiz_correct = None
            user.total_questions += 1
            user.correct_answers += 1
            _move_next(user, db)
            return feedback
        else:
            # Fout antwoord, voortgang_vereist=True → herhaal feedback, blijf bij stap
            user.total_questions += 1
            db.commit()
            return feedback

    # Geen pending → stuur les
    lesson_id = get_lesson_id_for_step(user.module, user.step)
    if not lesson_id:
        _move_next(user, db)
        return "Verder naar de volgende stap!"

    content = get_lesson_content(lesson_id)
    if not content:
        _move_next(user, db)
        return "Verder!"

    user.pending_quiz_text = lesson_id
    user.pending_quiz_correct = None
    db.commit()
    return content + "\n\n💡 Wil je nu al door? Stuur gewoon je antwoord!"


# ── Helpers ───────────────────────────────────────────────────────────────────

def _start(user: User, lang: str, db: Session) -> str:
    user.language = lang
    user.state = "NAME_PENDING"
    db.commit()
    return ai.ask_name(lang)


def _move_next(user: User, db: Session) -> None:
    max_steps = steps_in_module(user.module)
    if user.step < max_steps:
        user.step += 1
    else:
        nxt = user.module + 1
        if nxt > total_modules():
            user.state = "COMPLETED"
        else:
            user.module = nxt
            user.step = 1
    db.commit()


def _gen_lesson(user: User, lang: str) -> str:
    module = get_module(user.module)
    if not module:
        return "Er ging iets mis. Stuur OPNIEUW."
    lnr = lesson_index(user.module, user.step)
    topic = get_lesson_topic(user.module, lnr, lang)
    return ai.generate_lesson(topic, lnr, lang, name=user.name, skill=user.skill_level)


def _lesson_topic_for_step(user: User, lang: str) -> str:
    lnr = quiz_index(user.module, user.step)
    return get_lesson_topic(user.module, lnr, lang)


def _gen_module_complete(module_id: int, lang: str, name: str | None = None) -> str:
    module = get_module(module_id)
    next_module = get_module(module_id + 1)
    title = module["title"].get(lang, "") if module else ""
    next_title = next_module["title"].get(lang, "") if next_module else None
    return ai.generate_module_complete(title, next_title, lang, name=name)


def _module_title(module_id: int, lang: str) -> str:
    module = get_module(module_id)
    return module["title"].get(lang, "") if module else ""


def _ai_question(user: User, text: str, lang: str) -> str | None:
    module = get_module(user.module)
    context = module["topic"].get(lang, "") if module else ""
    return ai.answer_free_question(text, context, lang, name=user.name)


def _is_question(text: str) -> bool:
    t = text.strip()
    if t.endswith("?"):
        return True
    question_words = [
        "what", "how", "why", "where", "when", "who",
        "wat", "hoe", "waarom", "waar", "wanneer", "wie",
        "was", "wo", "wann", "warum",
        "que", "cómo", "dónde", "cuándo",
        "quoi", "comment", "pourquoi", "où", "quand",
    ]
    first = t.lower().split()[0] if t else ""
    return first in question_words


def _t(lang: str, en: str, nl: str = "", de: str = "", fr: str = "", es: str = "") -> str:
    return {"EN": en, "NL": nl or en, "DE": de or en, "FR": fr or en, "ES": es or en}.get(lang, en)
