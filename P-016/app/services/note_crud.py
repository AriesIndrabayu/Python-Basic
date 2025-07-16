from sqlalchemy.orm import Session
from sqlalchemy import func, or_
from app.models.note_model import Note
from app.schemas.note_schema import NoteCreate
from typing import Optional, List


# Ambil semua catatan (tanpa soft delete), dengan optional search
def get_all(db: Session, search: Optional[str] = None) -> Optional[List[Note]]:
    try:
        query = db.query(Note).filter(Note.deleted_at.is_(None))
        if search:
            search = f"%{search}%"
            query = query.filter(or_(Note.isi.ilike(search), Note.judul.ilike(search)))
        return query.order_by(Note.created_at.desc()).all()
    except Exception as e:
        print(f"[ERROR get_all] {e}")
        return None


# Ambil catatan dengan pagination & optional search
def get_paginated(
    db: Session, skip: int = 0, limit: int = 10, search: Optional[str] = None
):
    try:
        query = db.query(Note).filter(Note.deleted_at.is_(None))
        if search:
            search = f"%{search}%"
            query = query.filter(Note.isi.ilike(search))
        total = query.count()  # untuk memberi tahu jumlah total data yang cocok
        items = query.order_by(Note.created_at.desc()).offset(skip).limit(limit).all()
        return total, items
    except Exception as e:
        print(f"[ERROR get_paginated] {e}")
        return 0, []  # supaya tidak crash server


# Ambil catatan berdasarkan ID
def get_by_id(db: Session, catatan_id: int) -> Optional[Note]:
    try:
        return (
            db.query(Note)
            .filter(Note.id == catatan_id, Note.deleted_at.is_(None))
            .first()
        )
    except Exception as e:
        print(f"[ERROR get_by_id] {e}")
        return None


# Tambah catatan baru
def create(db: Session, catatan_in: NoteCreate) -> Optional[Note]:
    try:
        new_catatan = Note(
            judul=catatan_in.judul,
            isi=catatan_in.isi,
        )
        db.add(
            new_catatan
        )  # Tambahkan ke session, tapi Belum dikirim ke database — masih dalam transaksi.
        db.commit()  # Menyimpan perubahan secara permanen ke database.
        db.refresh(new_catatan)
        return new_catatan
    except Exception as e:
        db.rollback()
        print(f"[ERROR create] {e}")
        return None
