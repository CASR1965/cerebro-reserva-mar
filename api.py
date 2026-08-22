from flask import Blueprint, jsonify, request
from orchestrator import Orchestrator

api_bp = Blueprint('api', __name__)
orquestador = Orchestrator()

@api_bp.route("/info", methods=["GET"])
def info():
    return jsonify({
        "proyecto": "Cerebro Digital Reserva del Mar",
        "version": "1.6.0",
        "empresa": "Condominio Reserva del Mar",
        "ubicacion": "Playa Salguero, Santa Marta, Colombia",
        "web": "https://reservadelmar.lovable.app/"
    })

@api_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@api_bp.route("/procesar", methods=["POST"])
def procesar():
    data = request.get_json()
    mensaje = data.get("mensaje", "") if data else ""
    resultado = orquestador.procesar(mensaje)
    return jsonify(resultado)
