from fastapi import FastAPI
from app.routes import note_routes

app = FastAPI(title="Catatan Harian API", version="1.0")

# Masukkan router yang sudah berisi semua endpoint
app.include_router(note_routes.router, prefix="/api/v1")
