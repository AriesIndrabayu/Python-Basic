# 📝 Catatan Harian API

API sederhana berbasis **FastAPI** untuk mengelola catatan harian. Aplikasi ini mendukung operasi dasar seperti menampilkan seluruh catatan dan melihat detail catatan berdasarkan ID.

---

## 🚀 Fitur Utama

- ✅ Ambil semua catatan
- ✅ Ambil catatan berdasarkan ID
- ⏳ (Coming Soon) Tambah, ubah, dan hapus catatan

---

## 🧠 Teknologi yang Digunakan

- [FastAPI](https://fastapi.tiangolo.com/) — Web framework modern berbasis Python
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM untuk mengakses database
- [Pydantic](https://docs.pydantic.dev/) — Validasi skema data
- SQLite — Database default (bisa diganti ke MySQL/PostgreSQL)

---

## 📁 Struktur Folder

```
tests/
├── test_note_routes.py

app/
├── main.py                   # Entry point FastAPI
├── crud/
│   └── note_crud.py          # (opsional) logika manipulasi data
├── database/
│   └── connection.py         # Koneksi DB SQLAlchemy
├── models/
│   └── note_model.py         # Model Note (SQLAlchemy)
├── schemas/
│   └── note_schema.py        # Skema Pydantic
├── routes/
│   └── note_routes.py        # Routing endpoint

requirements.txt              # Dependency Python
```

---

## 🛠️ Instalasi & Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/AriesIndrabayu/Python-Basic/P-013/catatan-harian-api-001.git
cd catatan-harian-api-001
```

### 2. Buat & Aktifkan Virtual Environment (Opsional tapi Disarankan)

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate       # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### Isi `requirements.txt`

- `fastapi` → Framework utama untuk membuat REST API
- `uvicorn[standard]` → Server ASGI untuk menjalankan FastAPI
- `pydantic` → Validasi input/output (otomatis termasuk di FastAPI)
- `sqlalchemy` → ORM untuk koneksi ke database
- `mysql-connector-python` → Driver koneksi ke MySQL (via SQLAlchemy)
- `pytest` → Framework testing untuk unit & integration test
- `httpx` → HTTP client async/sync untuk testing API

### 4. Jalankan Server FastAPI

```bash
uvicorn app.main:app --reload
```

### 5. Akses Dokumentasi API

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📌 Contoh Endpoint

### 1. Ambil Semua Catatan

- **GET** `/api/notes`  
  → [http://localhost:8000/api/notes](http://localhost:8000/api/notes)

### 2. Ambil Catatan Berdasarkan ID

- **GET** `/api/notes/{note_id}`  
  → [http://localhost:8000/api/notes/1](http://localhost:8000/api/notes/1)

---

## 🧪 Menjalankan Test

Posisikan terminal di root project, lalu jalankan:

```bash
pytest
```

Ini akan otomatis mencari dan menjalankan semua file yang diawali `test_`.

### Menjalankan Test Tertentu

```bash
pytest tests/test_note_routes.py
```

### Contoh Output

```
========================================================= test session starts =========================================================
platform win32 -- Python 3.13.4, pytest-8.4.1, pluggy-1.6.0
rootdir: D:\Les Private\Materi Ajar\Live\Python-Basic\P13
plugins: anyio-4.9.0
collected 2 items

tests\test_note_routes.py ..                                                                                                     [100%]

========================================================== 2 passed in 0.73s ==========================================================
```

---

## 📈 Rencana Pengembangan

- [ ] Tambah fitur POST / PUT / DELETE
- [ ] Tambah autentikasi pengguna

---

## 👤 Author

> Indrabayu – [GitHub](https://github.com/AriesIndrabayu)
