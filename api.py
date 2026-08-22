from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from orchestrator import Orchestrator

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

orc = Orchestrator()

@app.get("/")
def read_root():
    return {"status": "online"}

@app.post("/api/chat")
def chat(data: dict):
    return orc.procesar(data.get("mensaje", ""))
