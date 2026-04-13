"""
Core state machine: processes an incoming SMS and returns a reply.
"""
from datetime import datetime, timezone
from sqlalchemy.orm import Session

from app.models import User
from app.curriculum import (
    LANGUAGES,
    WELCOME_MESSAGE,
    get_step,
    get_module,
    total_modules,
    is_yes,
)

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

    # Update last active
    user.last_active = datetime.now(timezone.utc)

    # ── RESTART at any point ──────────────────────────────────────
    if text.upper() in RESTART_WORDS:
        user.state = "LANG_PENDING"
        user.language = None
        user.module = 1
        user.step = 1
        user.correct_answers = 0
        user.total_questions = 0
        db.commit()
        return WELCOME_MESSAGE

    # ── LANGUAGE PENDING ─────────────────────────────────────────
    if user.state == "LANG_PENDING":
        lang = text.strip().upper()
        if lang not in LANGUAGES:
            return (
                "Please reply with one of:\n"
                "EN / NL / DE / FR / ES\n\n"
                "(Or type RESTART to start over)"
            )
        user.language = lang
        user.state = "LEARNING"
        user.module = 1
        user.step = 1
        db.commit()
        # Send first lesson
        step_data = get_step(1, 1)
        return step_data["content"][lang]

    # ── LEARNING ─────────────────────────────────────────────────
    if user.state == "LEARNING":
        lang = user.language or "EN"
        step_data = get_step(user.module, user.step)

        if not step_data:
            return _t(lang, "Hmm, something went wrong. Reply RESTART to begin again.")

        stype = step_data["type"]

        # LESSON step — any reply advances
        if stype == "lesson":
            return _advance(user, lang, db)

        # QUIZ step — expect A, B or C
        if stype == "quiz":
            answer = text.strip().upper()
            if answer not in ("A", "B", "C"):
                return _t(
                    lang,
                    "Please reply with A, B or C.",
                    "Antwoord A, B of C.",
                    "Antworten Sie A, B oder C.",
                    "Répondez A, B ou C.",
                    "Responda A, B o C.",
                )

            user.total_questions += 1
            if answer == step_data["correct"]:
                user.correct_answers += 1
                feedback = step_data["feedback_correct"][lang]
            else:
                feedback = step_data["feedback_wrong"][lang]
            db.commit()

            next_reply = _advance(user, lang, db)
            return f"{feedback}\n\n{next_reply}"

        # MODULE COMPLETE step — wait for yes
        if stype == "module_complete":
            if is_yes(text, lang):
                return _advance(user, lang, db)
            # Show the module complete message again
            return step_data["content"][lang]

    # ── COMPLETED ────────────────────────────────────────────────
    if user.state == "COMPLETED":
        lang = user.language or "EN"
        if text.upper() in RESTART_WORDS:
            user.state = "LANG_PENDING"
            user.language = None
            user.module = 1
            user.step = 1
            db.commit()
            return WELCOME_MESSAGE
        return _t(
            lang,
            "You have completed all modules! 🌟 Reply RESTART to do it again.",
            "Je hebt alle modules voltooid! 🌟 Antwoord OPNIEUW om opnieuw te beginnen.",
            "Sie haben alle Module abgeschlossen! 🌟 Antworten Sie NEU um neu zu starten.",
            "Vous avez terminé tous les modules! 🌟 Répondez RECOMMENCER pour reprendre.",
            "¡Ha completado todos los módulos! 🌟 Responda REINICIAR para volver a empezar.",
        )

    return "Something went wrong. Reply RESTART to start over."


def _advance(user: User, lang: str, db: Session) -> str:
    """Move to the next step/module and return the content of that step."""
    current_module = user.module
    current_step = user.step

    module_data = get_module(current_module)
    max_steps = len(module_data["steps"]) if module_data else 0

    if current_step < max_steps:
        user.step = current_step + 1
    else:
        # Move to next module
        next_module = current_module + 1
        if next_module > total_modules():
            user.state = "COMPLETED"
            db.commit()
            # Return the final module_complete content (already shown, so just done msg)
            step_data = get_step(current_module, current_step)
            return step_data["content"][lang]
        user.module = next_module
        user.step = 1

    db.commit()

    next_step = get_step(user.module, user.step)
    if not next_step:
        return "Something went wrong. Reply RESTART to start over."

    return next_step["content"] if isinstance(next_step.get("content"), str) else (
        next_step.get("content", {}).get(lang, "")
        or next_step.get("question", {}).get(lang, "")
    )


def _t(lang: str, en: str, nl: str = "", de: str = "", fr: str = "", es: str = "") -> str:
    mapping = {"EN": en, "NL": nl or en, "DE": de or en, "FR": fr or en, "ES": es or en}
    return mapping.get(lang, en)
