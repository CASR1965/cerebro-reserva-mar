from flask import Flask, render_template
import api  # Conecta con tu archivo api.py

app = Flask(__name__, template_folder='frontend')

@app.route("/")
def home():
    # Renderiza la interfaz visual conectada al cerebro
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
