from sqlalchemy.orm import Session
from sqlalchemy import func, or_
from app.models.note_model import Note
from app.schemas.note_schema import NoteCreate
from typing import Optional, List


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
