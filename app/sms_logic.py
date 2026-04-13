"""
State machine: verwerkt een inkomende SMS en geeft een antwoord.
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
            return _set_language_and_start(user, lang, db)
        return (
            "Please reply: EN / NL / DE / FR / ES\n"
            "(Or RESTART to start over)"
        )

    # ── AAN HET LEREN ─────────────────────────────────────────────
    if user.state == "LEARNING":
        lang = user.language or "EN"
        step_type = get_step_type(user.module, user.step)

        # LESSON
        if step_type == "lesson":
            if _is_question(text):
                module = get_module(user.module)
                context = module["topic"].get(lang, "") if module else ""
                answer = ai.answer_free_question(text, context, lang)
                if answer:
                    return answer
            return _advance(user, lang, db)

        # QUIZ
        if step_type == "quiz":
            # Nog geen quizvraag gepresenteerd → genereer en sla op
            if not user.pending_quiz_text:
                return _present_quiz(user, lang, db)

            # Evalueer antwoord
            answer = text.strip().upper()
            if answer not in ("A", "B", "C"):
                answer = ai.interpret_quiz_answer(text, user.pending_quiz_text, lang)

            if not answer:
                if _is_question(text):
                    module = get_module(user.module)
                    context = module["topic"].get(lang, "") if module else ""
                    ai_reply = ai.answer_free_question(text, context, lang)
                    if ai_reply:
                        return ai_reply
                return _t(
                    lang,
                    "Please reply A, B or C.",
                    "Antwoord A, B of C.",
                    "Antworten Sie A, B oder C.",
                    "Répondez A, B ou C.",
                    "Responda A, B o C.",
                )

            correct = answer == user.pending_quiz_correct
            feedback = ai.generate_feedback(correct, answer, user.pending_quiz_correct or "?", lang)

            user.total_questions += 1
            if correct:
                user.correct_answers += 1
            user.pending_quiz_text = None
            user.pending_quiz_correct = None
            db.commit()

            next_content = _advance(user, lang, db)
            return f"{feedback}\n\n{next_content}"

        # MODULE COMPLETE
        if step_type == "module_complete":
            if is_yes(text, lang):
                return _advance(user, lang, db)
            if _is_question(text):
                module = get_module(user.module)
                context = module["topic"].get(lang, "") if module else ""
                ai_reply = ai.answer_free_question(text, context, lang)
                if ai_reply:
                    return ai_reply
            # Herhaal het afrondingsbericht
            return _generate_module_complete_msg(user.module, lang)

    # ── KLAAR ─────────────────────────────────────────────────────
    if user.state == "COMPLETED":
        lang = user.language or "EN"
        return _t(
            lang,
            "You completed all modules! 🌟 Reply RESTART to do it again.",
            "Alle modules klaar! 🌟 Antwoord OPNIEUW om opnieuw te beginnen.",
            "Alle Module abgeschlossen! 🌟 Antworten Sie NEU.",
            "Tous les modules terminés! 🌟 Répondez RECOMMENCER.",
            "¡Todos los módulos! 🌟 Responda REINICIAR.",
        )

    return "Something went wrong. Reply RESTART."


# ── Helpers ───────────────────────────────────────────────────────────────────

def _set_language_and_start(user: User, lang: str, db: Session) -> str:
    user.language = lang
    user.state = "LEARNING"
    user.module = 1
    user.step = 1
    db.commit()
    return _generate_step_content(user, lang, db)


def _present_quiz(user: User, lang: str, db: Session) -> str:
    """Genereer een quizvraag, sla op en stuur."""
    module = get_module(user.module)
    if not module:
        return "Something went wrong. Reply RESTART."

    topic = module["topic"].get(lang, module["topic"]["EN"])
    qnr = quiz_index(user.module, user.step)
    quiz = ai.generate_quiz(topic, qnr, lang)

    if not quiz:
        # Fallback: ga door
        return _advance(user, lang, db)

    user.pending_quiz_text = quiz["text"]
    user.pending_quiz_correct = quiz["correct"]
    db.commit()
    return quiz["text"]


def _advance(user: User, lang: str, db: Session) -> str:
    """Ga naar de volgende stap/module en return de inhoud."""
    max_steps = steps_in_module(user.module)

    if user.step < max_steps:
        user.step += 1
    else:
        next_module = user.module + 1
        if next_module > total_modules():
            user.state = "COMPLETED"
            db.commit()
            return ai.generate_module_complete(
                get_module(user.module)["title"].get(lang, ""),
                None,
                lang,
            )
        user.module = next_module
        user.step = 1

    db.commit()
    return _generate_step_content(user, lang, db)


def _generate_step_content(user: User, lang: str, db: Session) -> str:
    """Genereer de inhoud voor de huidige stap."""
    step_type = get_step_type(user.module, user.step)
    module = get_module(user.module)
    if not module:
        return "Something went wrong. Reply RESTART."

    topic = module["topic"].get(lang, module["topic"]["EN"])

    if step_type == "lesson":
        lnr = lesson_index(user.module, user.step)
        return ai.generate_lesson(topic, lnr, lang)

    if step_type == "quiz":
        return _present_quiz(user, lang, db)

    if step_type == "module_complete":
        return _generate_module_complete_msg(user.module, lang)

    return "Something went wrong. Reply RESTART."


def _generate_module_complete_msg(module_id: int, lang: str) -> str:
    module = get_module(module_id)
    next_module = get_module(module_id + 1)
    title = module["title"].get(lang, "") if module else ""
    next_title = next_module["title"].get(lang, "") if next_module else None
    return ai.generate_module_complete(title, next_title, lang)


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
