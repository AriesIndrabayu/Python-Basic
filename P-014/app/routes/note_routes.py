from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.models.note_model import Note as NoteModel
from app.schemas.note_schema import Note, NoteCreate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/notes")
def get_notes(db: Session = Depends(get_db)):
    return db.query(NoteModel).all()


@router.get("/notes/{note_id}")
def get_note(note_id: int, db: Session = Depends(get_db)):
    return db.query(NoteModel).filter(NoteModel.id == note_id).first()
