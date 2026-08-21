from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de información oficial
INFO_OFICIAL = {
    "nombre": "Condominio Reserva del Mar",
    "ubicacion": "Playa Salguero, Santa Marta",
    "sitio_web": "https://reservadelmar.lovable.app/",
    "whatsapp": "https://wa.me/573138902136?text=Hola%2C%20quiero%20reservar%20mi%20estancia%20en%20el%20Condominio%20Reserva%20del%20Mar.",
    "instagram": "https://www.instagram.com/reservadelmar_santamarta/",
    "tiktok": "https://www.tiktok.com/@reservadelmarsantamarta",
    "youtube": "https://www.youtube.com/watch?v=hIJQkULq0y8",
    "facebook": "https://www.facebook.com/profile.php?id=100090692259424"
}

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "estado": "Cerebro Reserva del Mar - Operativo",
        "agente": "Carlos Suárez - Agente Oficial",
        "info": INFO_OFICIAL
    })

@app.route("/consultar", methods=["POST"])
def consultar():
    # Aquí el cerebro detectará la intención del cliente en el futuro
    return jsonify({
        "mensaje": "Bienvenido al Condominio Reserva del Mar, autoridad exclusiva en Playa Salguero.",
        "call_to_action": "Reserva directamente con atención personalizada aquí:",
        "enlace_whatsapp": INFO_OFICIAL["whatsapp"],
        "sitio_oficial": INFO_OFICIAL["sitio_web"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
