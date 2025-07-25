import requests
from typing import Optional, List

# Ganti dengan base URL API FastAPI kamu
API_BASE_URL = "http://127.0.0.1:8000/api/v1/notes"


# Ambil semua catatan (dengan optional pencarian)
def get_all(search: Optional[str] = None) -> Optional[List[dict]]:
    try:
        params = {"search": search} if search else {}
        response = requests.get(API_BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"[ERROR get_all] {e}")
        return None


# Ambil catatan berdasarkan ID
def get_by_id(id: int) -> Optional[dict]:
    try:
        response = requests.get(f"{API_BASE_URL}/{id}")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"[ERROR get_by_id] {e}")
        return None


# Tambah catatan baru
def create(judul: str, isi: str) -> Optional[dict]:
    try:
        payload = {"judul": judul, "isi": isi}
        response = requests.post(API_BASE_URL, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"[ERROR create] {e}")
        return None


# Perbarui catatan berdasarkan ID
def update(id: int, judul: str, isi: str) -> bool:
    try:
        payload = {"judul": judul, "isi": isi}
        response = requests.put(f"{API_BASE_URL}/{id}", json=payload)
        print("[DEBUG] response:", response)
        return response.status_code == 200
    except Exception as e:
        print(f"[ERROR update] {e}")
        return False


# Hapus catatan berdasarkan ID
def delete(id: int) -> bool:
    try:
        response = requests.delete(f"{API_BASE_URL}/{id}")
        return response.status_code == 200
    except Exception as e:
        print(f"[ERROR delete] {e}")
        return False


def restore_note(note_id):
    try:
        response = requests.patch(f"{API_BASE_URL}/restore/{note_id}")
        data = response.json()
        return data.get("success", False), data.get("message", "")
    except Exception as e:
        return False, f"Gagal restore: {e}"


def force_delete_note(note_id):
    try:
        response = requests.delete(f"{API_BASE_URL}/force/{note_id}")
        data = response.json()
        return data.get("success", False), data.get("message", "")
    except Exception as e:
        return False, f"Gagal force delete: {e}"
