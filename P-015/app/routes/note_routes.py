from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from app.database.connection import get_db
from app.models.note_model import Note
from app.schemas.note_schema import NoteCreate, NoteOut, PaginatedResponse
from app.services import note_crud as catatan_service

router = APIRouter(prefix="/notes", tags=["Catatan V1"])


# Tambah catatan baru
@router.post("/", response_model=NoteOut)
def create(catatan_in: NoteCreate, db: Session = Depends(get_db)):
    data = catatan_service.create(db, catatan_in)
    if not data:
        raise HTTPException(status_code=500, detail="Gagal menyimpan catatan")
    return data
