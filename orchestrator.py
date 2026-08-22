import re
import unicodedata

class Orchestrator:
    def __init__(self):
        self.recursos_oficiales = {
            "web": "https://reservadelmar.lovable.app/",
            "google_business": "https://g.co/kgs/4WkkCu9",
            "youtube": "https://www.youtube.com/watch?v=hIJQkULq0y8",
            "instagram": "https://www.instagram.com/reservadelmarsantamarta/",
            "tiktok": "https://www.tiktok.com/@reservadelmarsantamarta",
            "facebook": "https://www.facebook.com/profile.php?id=100090692259424",
            "whatsapp": "https://wa.me/573138902136?text=Hola%2C%20quiero%20reservar%20mi%20estancia%20en%20el%20Condominio%20Reserva%20del%20Mar"
        }

    def normalizar_texto(self, texto):
        if not texto: return ""
        texto = texto.lower()
        return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

    def procesar(self, mensaje_usuario):
        mensaje_norm = self.normalizar_texto(mensaje_usuario)
        es_reserva = any(k in mensaje_norm for k in ["reservar", "reserva", "precio"])
        
        return {
            "intencion": {"es_reserva": es_reserva},
            "respuesta": {
                "mensaje": "Bienvenido al Condominio Reserva del Mar.",
                "recursos_oficiales": self.recursos_oficiales
            }
        }
