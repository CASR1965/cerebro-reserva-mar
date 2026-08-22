from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from orchestrator import Orchestrator

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

orc = Orchestrator()

@app.get("/")
def read_root():
    return {"status": "online", "proyecto": "Reserva del Mar GEO API"}

@app.post("/api/chat")
def chat(data: dict):
    mensaje = data.get("mensaje", "")
    return orc.procesar(mensaje)
