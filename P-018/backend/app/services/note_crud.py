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
    db: Session,
    skip: int = 0,
    limit: int = 10,
    search: Optional[str] = None,
    sort_by: str = "updated_at__desc",
    status: str = "Aktif",
):
    try:
        sort_by = sort_by.lower()
        part_sort = sort_by.split("__")
        is_active = status.lower() == "aktif"  # ini akan menghasilkan True/False
        query = db.query(Note)  # ditampilkan semua dulu
        if search:
            search = f"%{search}%"
            query = query.filter(or_(Note.judul.ilike(search), Note.isi.ilike(search)))

        # maintenance data aktif/nonaktif
        print(is_active)
        if is_active:
            query = query.filter(Note.deleted_at.is_(None))
        else:
            query = query.filter(Note.deleted_at.is_not(None))

        total = query.count()  # untuk memberi tahu jumlah total data yang cocok

        # maintenance sortby
        if len(part_sort) == 2:
            field_name, direction = part_sort
            column = getattr(Note, field_name, None)
            if column is not None:
                if direction == "asc":
                    query = query.order_by(column.asc())
                elif direction == "desc":
                    query = query.order_by(column.desc())
        else:
            query = query.order_by(Note.updated_at.desc())
        items = query.offset(skip).limit(limit).all()
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


# Update catatan berdasarkan ID
def update(db: Session, catatan_id: int, catatan_in: NoteCreate) -> Optional[Note]:
    try:
        catatan = get_by_id(db, catatan_id)
        if not catatan:
            return None

        if catatan_in.judul is not None:
            catatan.judul = catatan_in.judul  # type: ignore
        if catatan_in.isi is not None:
            catatan.isi = catatan_in.isi  # type: ignore

        db.commit()
        db.refresh(catatan)
        return catatan
    except Exception as e:
        db.rollback()
        print(f"[ERROR update] {e}")
        return None


# ==============================


# Soft delete catatan
def soft_delete(db: Session, catatan_id: int) -> bool:
    try:
        catatan = get_by_id(db, catatan_id)
        if not catatan:
            return False

        catatan.deleted_at = func.now()  # type: ignore
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        print(f"[ERROR soft_delete] {e}")
        return False


# Restore catatan yang sudah soft delete
def restore(db: Session, catatan_id: int) -> bool:
    try:
        catatan = (
            db.query(Note)
            .filter(Note.id == catatan_id, Note.deleted_at.is_not(None))
            .first()
        )
        if not catatan:
            return False

        catatan.deleted_at = None  # type: ignore
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        print(f"[ERROR restore] {e}")
        return False


# Force delete catatan dari database (hapus permanen)
def force_delete(db: Session, catatan_id: int) -> bool:
    try:
        catatan = db.query(Note).filter(Note.id == catatan_id).first()
        if not catatan:
            return False

        db.delete(catatan)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        print(f"[ERROR force_delete] {e}")
        return False
