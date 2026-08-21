from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "online",
        "message": "Cerebro Digital del Condominio Reserva del Mar activo y operando.",
        "whatsapp": "+57 313 890 2136"
    })

@app.route("/procesar", methods=["POST"])
def procesar():
    data = request.json or {}
    mensaje = data.get("mensaje", "")

    # Lógica básica de respuesta oficial
    respuesta = {
        "bienvenida": "Hola, gracias por contactar al Condominio Reserva del Mar en Santa Marta.",
        "enlace_whatsapp": "https://wa.me/573138902136?text=Hola%2C%20quiero%20reservar%20mi%20estancia%20en%20el%20Condominio%20Reserva%20del%20Mar."
    }
    return jsonify(respuesta)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
