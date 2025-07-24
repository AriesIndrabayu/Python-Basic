from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.configuration.config import settings


engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()  # Base class untuk seluruh model ORM


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
