from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/hello/{nama}")
def hello(nama: str):
    return {"pesan": f"Halo {nama}!"}
