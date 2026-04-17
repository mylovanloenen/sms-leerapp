"""
Dagelijkse les-pusher.
Stuurt elke dag op DAILY_LESSON_HOUR (UTC) een SMS naar alle actieve gebruikers.
"""
import os
from twilio.rest import Client
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import User
from app.sms_logic import (
    _handle_nl_lesson, _gen_lesson, _gen_module_complete,
    _move_next,
)
from app.curriculum import get_step_type


def _twilio_client():
    return Client(
        os.getenv("TWILIO_ACCOUNT_SID"),
        os.getenv("TWILIO_AUTH_TOKEN"),
    )


def _send_sms(to: str, body: str) -> None:
    _twilio_client().messages.create(
        body=body,
        from_=os.getenv("TWILIO_PHONE_NUMBER"),
        to=to,
    )


def _daily_lesson_for(user: User, db: Session) -> str | None:
    """Geeft de lesinhoud voor vandaag terug, of None als er niets te sturen is."""
    lang = user.language or "NL"

    # Nog een openstaand antwoord → stuur een herinnering
    if user.pending_quiz_text:
        reminders = {
            "NL": "👋 Vergeet je les niet! Stuur je antwoord om door te gaan.",
            "EN": "👋 Don't forget your lesson! Send your answer to continue.",
            "DE": "👋 Vergiss deine Lektion nicht! Sende deine Antwort.",
            "FR": "👋 N'oublie pas ta leçon! Envoie ta réponse pour continuer.",
            "ES": "👋 ¡No olvides tu lección! Envía tu respuesta para continuar.",
        }
        return reminders.get(lang, reminders["EN"])

    step_type = get_step_type(user.module, user.step)

    if step_type == "lesson":
        if lang == "NL":
            return _handle_nl_lesson(user, "", db)
        else:
            content = _gen_lesson(user, lang)
            _move_next(user, db)
            return content

    if step_type == "module_complete":
        return _gen_module_complete(user.module, lang, name=user.name)

    return None


def send_daily_lessons() -> None:
    """Wordt dagelijks aangeroepen door de scheduler."""
    db: Session = SessionLocal()
    try:
        users = db.query(User).filter(User.state == "LEARNING").all()
        print(f"📨 Dagelijkse les: {len(users)} gebruiker(s)")
        for user in users:
            try:
                content = _daily_lesson_for(user, db)
                if content:
                    _send_sms(user.phone, content)
                    print(f"  ✅ Verstuurd naar {user.phone}")
            except Exception as e:
                print(f"  ❌ Fout bij {user.phone}: {e}")
    finally:
        db.close()
