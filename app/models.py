from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime, timezone
from app.database import Base


class User(Base):
    __tablename__ = "users"

    phone = Column(String, primary_key=True, index=True)
    language = Column(String, nullable=True)          # EN / NL / DE / FR / ES
    state = Column(String, default="NEW")             # NEW | LANG_PENDING | LEARNING | COMPLETED
    module = Column(Integer, default=1)
    step = Column(Integer, default=1)
    correct_answers = Column(Integer, default=0)
    total_questions = Column(Integer, default=0)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    last_active = Column(DateTime, default=lambda: datetime.now(timezone.utc))
