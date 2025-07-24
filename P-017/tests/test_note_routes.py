# tests/test_notes.py
"""
@pytest.fixture(scope="module")
def created_note_id():
    payload = {"judul": "Catatan Test", "isi": "Isi dari catatan test"}
    response = client.post("/api/v1/notes", json=payload)
    assert response.status_code == 200
    return response.json()["id"]


📌 Tujuan Umum
Ini adalah pytest fixture, yaitu fungsi khusus yang digunakan untuk:
- Menyiapkan data atau kondisi awal yang akan digunakan oleh satu atau lebih fungsi test.
- Dalam kasus ini, membuat satu catatan (note), lalu mengembalikan ID-nya agar bisa dipakai oleh test lain seperti GET, UPDATE, DELETE.

@pytest.fixture(scope="module")
✅ Ini adalah decorator dari pytest yang menandai bahwa fungsi di bawahnya adalah fixture.
scope="module" artinya:
- Fixture ini akan dipanggil sekali saja untuk 1 file test (module).
- Semua test function dalam file tersebut yang menerima parameter created_note_id akan memakai hasil yang sama.
- Ini hemat waktu dan efisien (tidak membuat catatan berkali-kali).

def created_note_id():
✅ Ini adalah fungsi fixture yang akan menghasilkan nilai yang bisa digunakan di fungsi test.
- Namanya created_note_id, jadi nanti kamu bisa langsung menuliskannya sebagai parameter di fungsi test: --> def test_get_note_by_id(created_note_id):

Payload Data yang Akan Dikirim
payload = {"judul": "Catatan Test ke-2", "isi": "Isi dari catatan test ke-2"}
✅ Ini adalah data yang akan dikirim ke endpoint API kamu (POST /api/v1/notes) untuk membuat catatan baru.
- Mirip seperti form: kita isi judul dan isi catatan.

return response.json()["id"]
Ambil dan Kembalikan ID
Maka response.json()["id"] akan memberi 6, dan itu dikembalikan sebagai nilai fixture.

📥 Contoh Cara Pakai di Test
def test_get_note_by_id(created_note_id):
    response = client.get(f"/api/v1/notes/{created_note_id}")
    assert response.status_code == 200

✅ Saat test ini berjalan:
- Pytest otomatis memanggil created_note_id() fixture,
- Hasil return dari fixture (ID-nya) diberikan sebagai argumen ke fungsi ini.

📌 Kenapa Ini Lebih Baik?
| Tanpa Fixture                         | Dengan Fixture                   |
| ------------------------------------- | -------------------------------- |
| Harus buat note di setiap fungsi test | Note cukup dibuat **sekali**     |
| Harus pakai `global`                  | Tidak perlu `global`, lebih aman |
| Data tidak reusable                   | Bisa dipakai di banyak test      |
| Susah di-maintain                     | Rapi dan scalable                |

🚀 Ringkasan
@pytest.fixture(scope="module") --> Mendefinisikan fixture yang bisa digunakan oleh banyak test

client.post(...) --> Mengirim request untuk membuat data

assert ...	--> Memastikan bahwa request berhasil

return response.json()["id"] --> Mengembalikan ID note agar bisa dipakai di test lain
"""
# === FIXTURE UNTUK CREATE NOTE SEKALI, REUSABLE DI TEST LAIN ===

import pytest
from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app

client = TestClient(app)


# def test_create_note():
#     global created_note_id
#     payload = {"judul": "Catatan Test", "isi": "Isi dari catatan test"}
#     response = client.post("/api/v1/notes", json=payload)
#     assert response.status_code == 200
#     json_data = response.json()
#     assert "id" in json_data
#     assert json_data["judul"] == payload["judul"]
#     created_note_id = json_data["id"]


@pytest.fixture(scope="module")
def created_note_id():
    payload = {"judul": "Catatan Test", "isi": "Isi dari catatan test"}
    response = client.post("/api/v1/notes", json=payload)
    assert response.status_code == 200
    json_data = response.json()
    assert "id" in json_data
    assert json_data["judul"] == payload["judul"]
    return json_data["id"]


def test_get_all_notes():
    response = client.get("/api/v1/notes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_paginated():
    response = client.get("/api/v1/notes/paginated?page=1&size=5")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "page" in data
    assert "size" in data
    assert "total" in data
    assert "data" in data
    assert isinstance(data["data"], list)


def test_get_note_by_id(created_note_id):
    response = client.get(f"/api/v1/notes/{created_note_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == created_note_id


def test_update_note(created_note_id):
    payload = {"judul": "Catatan Test (Update)", "isi": "Isi setelah diupdate"}
    response = client.put(f"/api/v1/notes/{created_note_id}", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["judul"] == payload["judul"]


def test_soft_delete_note(created_note_id):
    response = client.delete(f"/api/v1/notes/{created_note_id}")
    assert response.status_code == 200
    assert "message" in response.json()


def test_restore_note(created_note_id):
    response = client.patch(f"/api/v1/notes/restore/{created_note_id}")
    assert response.status_code == 200
    assert "message" in response.json()


def test_force_delete_note(created_note_id):
    response = client.delete(f"/api/v1/notes/force/{created_note_id}")
    assert response.status_code == 200
    assert "message" in response.json()
