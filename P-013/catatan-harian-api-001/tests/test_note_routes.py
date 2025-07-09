from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app


client = TestClient(app)


def test_get_all_notes():
    response = client.get("/api/notes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_note_by_id():
    # Asumsikan ID 1 sudah ada di database
    response = client.get("/api/notes/1")
    assert response.status_code in [200, 404]  # tergantung apakah datanya ada
