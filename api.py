from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from orchestrator import Orchestrator


app = FastAPI(
    title="Cerebro Digital - Reserva del Mar",
    description="API central del sistema inteligente de conversión turística.",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


orquestador = Orchestrator()


class Solicitud(BaseModel):
    mensaje: str


@app.get("/")
def inicio():
    return {
        "nombre": "Cerebro Digital - Reserva del Mar",
        "estado": "activo",
        "mensaje": "El Cerebro Digital está funcionando."
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/info")
def info():
    return {
        "proyecto": "Cerebro Digital Reserva del Mar",
        "version": "1.0.0",
        "empresa": "Condominio Reserva del Mar",
        "ubicacion": "Playa Salguero, Santa Marta, Colombia",
        "web": "https://reservadelmar.lovable.app/"
    }


@app.post("/procesar")
def procesar(solicitud: Solicitud):
    resultado = orquestador.procesar(solicitud.mensaje)
    return resultado
