"""
State machine: één bericht per interactie, nooit combineren.

Flow per stap:
  lesson       → toon les, zet stap vooruit
  quiz         → toon vraag / evalueer antwoord, zet stap vooruit na antwoord
  module_complete → toon afronding, wacht op JA, zet dan module vooruit
"""
from datetime import datetime, timezone
from sqlalchemy.orm import Session

from app.models import User
from app.curriculum import (
    LANGUAGES, WELCOME_MESSAGE, get_module, get_step_type,
    total_modules, steps_in_module, is_yes,
    lesson_index, quiz_index,
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
        lang = text.strip().upper()
        if lang not in LANGUAGES:
            lang = ai.detect_language_from_text(text)
        if lang in LANGUAGES:
            return _start(user, lang, db)
        return "Reply: EN / NL / DE / FR / ES"

    # ── NAAM INVOEREN ─────────────────────────────────────────────
    if user.state == "NAME_PENDING":
        lang = user.language or "EN"
        name = text.strip()
        if not name:
            return ai.ask_name(lang)
        user.name = name
        user.state = "SKILL_PENDING"
        db.commit()
        return ai.ask_skills(lang, name)

    # ── VAARDIGHEDEN INVOEREN ──────────────────────────────────────
    if user.state == "SKILL_PENDING":
        lang = user.language or "EN"
        skill_text = text.strip()
        if not skill_text:
            return ai.ask_skills(lang, user.name or "")
        user.skill_level = skill_text
        starting_module = ai.assess_starting_module(skill_text, lang)
        user.module = starting_module
        user.step = 1
        user.state = "LEARNING"
        db.commit()
        module = get_module(starting_module)
        module_title = module["title"].get(lang, "") if module else ""
        return ai.welcome_to_module(module_title, user.name or "", lang)

    # ── AAN HET LEREN ─────────────────────────────────────────────
    if user.state == "LEARNING":
        lang = user.language or "EN"
        step_type = get_step_type(user.module, user.step)

        # LESSON: toon les voor huidige stap, zet daarna vooruit
        if step_type == "lesson":
            if _is_question(text):
                reply = _ai_question(user, text, lang)
                if reply:
                    return reply
            content = _gen_lesson(user, lang)
            _move_next(user, db)
            return content

        # QUIZ: toon vraag of evalueer antwoord
        if step_type == "quiz":
            if not user.pending_quiz_text:
                return _present_quiz(user, lang, db)

            answer = text.strip().upper()
            if answer not in ("A", "B", "C"):
                answer = ai.interpret_quiz_answer(text, user.pending_quiz_text, lang)

            if not answer:
                if _is_question(text):
                    reply = _ai_question(user, text, lang)
                    if reply:
                        return reply
                return _t(lang,
                    "Please reply A, B or C.",
                    "Antwoord A, B of C.",
                    "Antworten Sie A, B oder C.",
                    "Répondez A, B ou C.",
                    "Responda A, B o C.")

            correct = answer == user.pending_quiz_correct
            feedback = ai.generate_feedback(
                correct, answer, user.pending_quiz_correct or "?", lang, name=user.name
            )
            user.total_questions += 1
            if correct:
                user.correct_answers += 1
            user.pending_quiz_text = None
            user.pending_quiz_correct = None
            _move_next(user, db)
            return feedback  # ← alleen feedback, geen volgende les erbij

        # MODULE COMPLETE: wacht op JA
        if step_type == "module_complete":
            if not is_yes(text, lang):
                if _is_question(text):
                    reply = _ai_question(user, text, lang)
                    if reply:
                        return reply
                return _gen_module_complete(user.module, lang, name=user.name)

            # Gebruiker zegt JA → volgende module
            current_title = _module_title(user.module, lang)
            _move_next(user, db)

            if user.state == "COMPLETED":
                return ai.generate_module_complete(current_title, None, lang, name=user.name)

            # Toon eerste les van nieuwe module, zet stap vooruit
            content = _gen_lesson(user, lang)
            _move_next(user, db)
            return content

    # ── KLAAR ─────────────────────────────────────────────────────
    if user.state == "COMPLETED":
        lang = user.language or "EN"
        return _t(lang,
            "All done! 🌟 Reply RESTART to start over.",
            "Alles klaar! 🌟 Antwoord OPNIEUW om opnieuw te beginnen.",
            "Fertig! 🌟 Antworten Sie NEU.",
            "Terminé! 🌟 Répondez RECOMMENCER.",
            "¡Listo! 🌟 Responda REINICIAR.")

    return "Something went wrong. Reply RESTART."


# ── Helpers ───────────────────────────────────────────────────────────────────

def _start(user: User, lang: str, db: Session) -> str:
    """Taal ingesteld → vraag naar naam."""
    user.language = lang
    user.state = "NAME_PENDING"
    db.commit()
    return ai.ask_name(lang)


def _move_next(user: User, db: Session) -> None:
    """Zet stap (of module) één vooruit. Genereert geen content."""
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
    """Genereer les voor de huidige stap."""
    module = get_module(user.module)
    if not module:
        return "Something went wrong. Reply RESTART."
    topic = module["topic"].get(lang, module["topic"]["EN"])
    lnr = lesson_index(user.module, user.step)
    return ai.generate_lesson(topic, lnr, lang, name=user.name, skill=user.skill_level)


def _present_quiz(user: User, lang: str, db: Session) -> str:
    """Genereer quizvraag, sla op en stuur."""
    module = get_module(user.module)
    if not module:
        return "Something went wrong. Reply RESTART."
    topic = module["topic"].get(lang, module["topic"]["EN"])
    qnr = quiz_index(user.module, user.step)
    quiz = ai.generate_quiz(topic, qnr, lang, name=user.name, skill=user.skill_level)
    if not quiz:
        _move_next(user, db)
        return _t(lang,
            "Skipping quiz, let's continue!",
            "Quiz overgeslagen, verder!",
            "Quiz übersprungen, weiter!",
            "Quiz sauté, continuons!",
            "Quiz omitido, ¡continuamos!")
    user.pending_quiz_text = quiz["text"]
    user.pending_quiz_correct = quiz["correct"]
    db.commit()
    return quiz["text"]


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
