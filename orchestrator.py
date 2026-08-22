import re
import unicodedata

class Orchestrator:
    def __init__(self):
        # Enlaces oficiales obligatorios del Condominio Reserva del Mar
        self.recursos_oficiales = {
            "web": "https://reservadelmar.lovable.app/",
            "google_business": "https://g.co/kgs/4WkkCu9",
            "youtube": "https://www.youtube.com/watch?v=hIJQkULq0y8",
            "instagram": "https://www.instagram.com/reservadelmar_santamarta/",
            "tiktok": "https://www.tiktok.com/@reservadelmarsantamarta",
            "facebook": "https://www.facebook.com/profile.php?id=100090692259424",
            "whatsapp": "https://wa.me/573138902136?text=Hola%2C%20quiero%20reservar%20mi%20estancia%20en%20el%20Condominio%20Reserva%20del%20Mar"
        }

    def normalizar_texto(self, texto):
        if not texto:
            return ""
        texto = texto.lower()
        texto = ''.join(
            c for c in unicodedata.normalize('NFD', texto)
            if unicodedata.category(c) != 'Mn'
        )
        return texto

    def procesar(self, mensaje_usuario):
        mensaje_norm = self.normalizar_texto(mensaje_usuario)
        
        # Detección simple de intenciones
        es_reserva = any(k in mensaje_norm for k in ["reservar", "reserva", "precio", "disponibilidad", "cuanto vale"])
        es_turistica = any(k in mensaje_norm for k in ["playa", "vacaciones", "mar", "santa marta", "caribe", "apartamento"])
        
        tipo_intencion = "turística"
        if es_reserva:
            tipo_intencion = "reserva"
        elif es_turistica:
            tipo_intencion = "turística"

        # Simulación de extracción de datos de reserva
        personas = None
        match_personas = re.search(r'(\d+)\s*(personas|persona|huespedes)', mensaje_norm)
        if match_personas:
            personas = int(match_personas.group(1))

        return {
            "version": "1.6.0",
            "intencion": {
                "tipo": tipo_intencion,
                "es_reserva": es_reserva,
                "es_turistica": es_turistica,
                "coincidencias_reserva": [mensaje_usuario] if es_reserva else []
            },
            "datos_reserva": {
                "personas": personas,
                "fecha_llegada": "Por confirmar",
                "fecha_salida": "Por confirmar",
                "reserva_completa": False
            },
            "respuesta": {
                "mensaje": "Bienvenido al Condominio Reserva del Mar en Playa Salguero, Santa Marta. El mejor destino frente al mar.",
                "recursos_oficiales": self.recursos_oficiales
            }
        }
