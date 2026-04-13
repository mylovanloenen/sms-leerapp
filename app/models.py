from sqlalchemy import Column, String, Integer, DateTime, Text
from datetime import datetime, timezone
from app.database import Base


class User(Base):
    __tablename__ = "users"

    phone = Column(String, primary_key=True, index=True)
    language = Column(String, nullable=True)
    # States: LANG_PENDING | NAME_PENDING | SKILL_PENDING | LEARNING | COMPLETED
    state = Column(String, default="LANG_PENDING")
    module = Column(Integer, default=1)
    step = Column(Integer, default=1)
    correct_answers = Column(Integer, default=0)
    total_questions = Column(Integer, default=0)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    last_active = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Onboarding
    name = Column(String, nullable=True)
    skill_level = Column(Text, nullable=True)   # vrije tekst van de gebruiker

    # Huidige quizvraag
    pending_quiz_text = Column(Text, nullable=True)
    pending_quiz_correct = Column(String(1), nullable=True)
