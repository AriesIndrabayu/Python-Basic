from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Optional
from app.database.connection import get_db

# from app.models.note_model import Note
from app.schemas.note_schema import NoteCreate, NoteOut, PaginatedResponse
from app.services import note_crud as catatan_service


router = APIRouter(prefix="/notes", tags=["Catatan V1"])


# Ambil semua catatan (tanpa pagination), bisa search
@router.get("/", response_model=list[NoteOut])
def get_all(search: Optional[str] = None, db: Session = Depends(get_db)):
    data = catatan_service.get_all(db, search)
    if data is None:
        raise HTTPException(status_code=500, detail="Gagal mengambil data")
    return data


# Ambil catatan dengan pagination + optional search
@router.get("/paginated", response_model=PaginatedResponse[NoteOut])
def get_paginated(
    page: int = Query(1, gt=0),
    size: int = Query(10, gt=0),
    search: Optional[str] = None,
    sort_by: str = Query("updated_at__desc"),
    status: str = Query("Aktif"),
    db: Session = Depends(get_db),
):
    skip = (page - 1) * size
    total, items = catatan_service.get_paginated(
        db, skip, size, search, sort_by, status
    )
    total_page = (total + size - 1) // size  # pembulatan ke atas

    return PaginatedResponse(
        page=page,
        size=size,
        total=total,
        total_page=total_page,
        has_next=page < total_page,
        has_prev=page > 1,
        data=items,
    )


# Ambil catatan by ID
@router.get("/{catatan_id}", response_model=NoteOut)
def get_by_id(catatan_id: int, db: Session = Depends(get_db)):
    data = catatan_service.get_by_id(db, catatan_id)
    if not data:
        raise HTTPException(status_code=404, detail="Catatan tidak ditemukan")
    return data


# Tambah catatan baru
@router.post("/", response_model=NoteOut)
def create(catatan_in: NoteCreate, db: Session = Depends(get_db)):
    data = catatan_service.create(db, catatan_in)
    # if not data:
    #     raise HTTPException(status_code=500, detail="Gagal menyimpan catatan")
    # return data
    if data:
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "success": True,
                "message": "Catatan berhasil ditambahkan",
                "data": {
                    "id": data.id,
                    "judul": data.judul,
                    "isi": data.isi,
                    "created_at": data.created_at.isoformat(),
                },
            },
        )
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"success": False, "message": "Gagal menambahkan catatan"},
    )


# Update catatan
@router.put("/{catatan_id}", response_model=NoteOut)
def update(catatan_id: int, catatan_in: NoteCreate, db: Session = Depends(get_db)):
    data = catatan_service.update(db, catatan_id, catatan_in)
    # if not data:
    #     raise HTTPException(
    #         status_code=404, detail="Catatan tidak ditemukan atau gagal update"
    #     )
    # return data
    if data:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "message": "Catatan berhasil diupdate",
                "data": {
                    "id": data.id,
                    "judul": data.judul,
                    "isi": data.isi,
                    "created_at": data.created_at.isoformat(),
                },
            },
        )
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"success": False, "message": "Gagal mengubah catatan"},
    )


# Soft delete catatan
@router.delete("/{catatan_id}")
def soft_delete(catatan_id: int, db: Session = Depends(get_db)):
    if not catatan_service.soft_delete(db, catatan_id):
        raise HTTPException(
            status_code=404, detail="Catatan tidak ditemukan atau gagal dihapus"
        )
    return {"message": "Catatan berhasil dihapus (soft delete)"}


# Restore catatan
@router.patch("/restore/{catatan_id}")
def restore(catatan_id: int, db: Session = Depends(get_db)):
    if not catatan_service.restore(db, catatan_id):
        raise HTTPException(
            status_code=404, detail="Catatan tidak ditemukan atau gagal direstore"
        )
    return {"success": True, "message": "Catatan berhasil direstore"}


# Force delete catatan (hapus permanen)
@router.delete("/force/{catatan_id}")
def force_delete(catatan_id: int, db: Session = Depends(get_db)):
    if not catatan_service.force_delete(db, catatan_id):
        raise HTTPException(
            status_code=404,
            detail="Catatan tidak ditemukan atau gagal dihapus permanen",
        )
    return {"success": True, "message": "Catatan berhasil dihapus permanen"}
