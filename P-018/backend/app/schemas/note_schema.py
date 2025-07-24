from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, Generic, TypeVar, List
from datetime import datetime

"""Skema untuk input (POST / PUT)"""


class NoteCreate(BaseModel):
    judul: str
    isi: str


"""Skema untuk response (GET)"""


class NoteOut(NoteCreate):
    id: int
    isi: str
    judul: str
    deleted_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


T = TypeVar("T")  # Membuat tipe generik

"""Template response paginasi"""


class PaginatedResponse(BaseModel, Generic[T]):
    page: int = Field(..., description="Halaman saat ini")
    size: int = Field(..., description="Jumlah item per halaman")
    total: int = Field(..., description="Total seluruh data")
    total_page: int = Field(..., description="Total halaman tersedia")
    has_next: bool = Field(..., description="Apakah ada halaman selanjutnya")
    has_prev: bool = Field(..., description="Apakah ada halaman sebelumnya")
    data: List[T] = Field(..., description="List data hasil query")


class Note(NoteCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
