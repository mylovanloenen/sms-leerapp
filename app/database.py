from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:////data/sms_leerapp.db")

# Render geeft postgres:// maar SQLAlchemy wil postgresql://
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

is_sqlite = DATABASE_URL.startswith("sqlite")
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if is_sqlite else {},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
