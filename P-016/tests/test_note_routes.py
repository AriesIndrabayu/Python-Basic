from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app


client = TestClient(app)


def test_create_note():
    global created_note_id
    payload = {"judul": "Catatan Test", "isi": "Isi dari catatan test"}
    response = client.post("/api/v1/notes", json=payload)
    assert response.status_code == 200
    json_data = response.json()
    assert "id" in json_data
    assert json_data["judul"] == payload["judul"]
    created_note_id = json_data["id"]
