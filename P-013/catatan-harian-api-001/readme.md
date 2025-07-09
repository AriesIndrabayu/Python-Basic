# 📝 Catatan Harian API

API sederhana berbasis **FastAPI** untuk mengelola catatan harian. Aplikasi ini mendukung operasi dasar seperti menampilkan seluruh catatan dan melihat detail catatan berdasarkan ID.

---

## 🚀 Fitur Utama

- [x] Ambil semua catatan
- [x] Ambil catatan berdasarkan ID
- [ ] (Coming Soon) Tambah, ubah, dan hapus catatan

---

## 🧠 Teknologi yang Digunakan

- [FastAPI](https://fastapi.tiangolo.com/) - Web framework modern berbasis Python
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM untuk mengakses database
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Validasi skema data
- SQLite - Database default (bisa diganti MySQL/PostgreSQL)

---

## 📁 Struktur Folder

tests/
├── test_note_routes.py
app/
├── main.py # Entry point FastAPI
├── crud/
│ └── note_crud.py # (opsional) logika manipulasi data
├── database/
│ └── connection.py # Koneksi DB SQLAlchemy
├── models/
│ └── note_model.py # Model Note (SQLAlchemy)
├── schemas/
│ └── note_schema.py # Skema Pydantic
├── routes/
│ └── note_routes.py # Routing endpoint
requirements.txt # Dependency Python

---

## 🛠️ Instalasi & Menjalankan

1. **Clone repo ini:**

git clone https://github.com/AriesIndrabayu/Python-Basic/P-013/catatan-harian-api-001.git
cd catatan-harian-api-001

2. **Buat dan aktifkan virtual environment (opsional tapi disarankan):**
   python -m venv venv
   source venv/bin/activate # Linux/macOS
   venv\Scripts\activate # Windows

3. **Install dependencies:**
   isi file requirements.txt
   fastapi → framework utama untuk membuat REST API
   uvicorn[standard] → server ASGI untuk menjalankan FastAPI
   pydantic → untuk validasi input/output (otomatis sudah include di FastAPI, tapi bisa eksplisit)
   sqlalchemy → ORM untuk koneksi ke database
   mysql-connector-python → driver koneksi ke MySQL (via SQLAlchemy)
   pytest → Framework testing untuk unit & integration test
   httpx → HTTP client async/sync, cocok untuk testing API FastAPI

   pip install -r requirements.txt

4. **Jalankan server FastAPI:**
   uvicorn app.main:app --reload

5. **Akses dokumentasi otomatis:**
   Swagger UI: http://localhost:8000/docs
   Redoc: http://localhost:8000/redoc

## 📌 Contoh Endpoint

1. **GET Semua Catatan**
   GET /api/notes
   http://localhost:8000/api/notes

2. **GET Catatan Berdasarkan ID**
   GET /api/notes/{note_id}
   http://localhost:8000/api/notes/1

## 📌 Menjalankan test

    posisikan terminal di root project lalu ketik:

    pytest

    Ini otomatis mencari semua file yang diawali dengan test_ dan menjalankan fungsinya.

    Atau untuk menjalankan file tertentu:
    pytest tests/test_note_routes.py

    Hasilnya di Terminal:
    (venv)
    Indrabayu@DESKTOP-INDRABAYU MINGW64 /d/Les Private/Materi Ajar/Live/Python-Basic/P13
    $ pytest
    ========================================================= test session starts =========================================================
    platform win32 -- Python 3.13.4, pytest-8.4.1, pluggy-1.6.0
    rootdir: D:\Les Private\Materi Ajar\Live\Python-Basic\P13
    plugins: anyio-4.9.0
    collected 2 items

    tests\test_note_routes.py ..                                                                                                     [100%]

    ========================================================== 2 passed in 0.73s ==========================================================

## Rencana Pengembangan

1.  **_Tambah fitur POST/PUT/DELETE_**
2.  **_Autentikasi pengguna_**
