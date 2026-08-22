import re
import unicodedata
from datetime import datetime

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

    def extraer_fechas(self, mensaje_norm):
        # Patrón simple para detectar menciones de fechas (ej: "del 10 al 15")
        match_rango = re.search(r'(?:del\s*)?(\d{1,2})\s*(?:al|hasta)\s*(\d{1,2})', mensaje_norm)
        if match_rango:
            return f"Días {match_rango.group(1)} al {match_rango.group(2)}"
        return "Por confirmar"

    def procesar(self, mensaje_usuario):
        mensaje_norm = self.normalizar_texto(mensaje_usuario)
        
        # 1. Detección refinada de intenciones
        es_reserva = any(k in mensaje_norm for k in ["reservar", "reserva", "precio", "disponibilidad", "cuanto vale", "cotizacion"])
        es_turistica = any(k in mensaje_norm for k in ["playa", "vacaciones", "mar", "santa marta", "caribe", "apartamento", "salguero"])
        
        tipo_intencion = "general"
        if es_reserva:
            tipo_intencion = "reserva"
        elif es_turistica:
            tipo_intencion = "turística"

        # 2. Extracción de entidades (Personas y Fechas)
        personas = None
        match_personas = re.search(r'(\d+)\s*(personas|persona|huespedes|adultos)', mensaje_norm)
        if match_personas:
            personas = int(match_personas.group(1))

        fecha_estancia = self.extraer_fechas(mensaje_norm)
        reserva_completa = bool(personas and fecha_estancia != "Por confirmar")

        # 3. Construcción del mensaje de respuesta adaptado
        if es_reserva:
            mensaje_respuesta = (
                "¡Excelente elección! Estás a un paso de asegurar tu estancia en el Condominio Reserva del Mar (Playa Salguero). "
                "Para brindarte disponibilidad inmediata y tarifas exactas, contáctanos directamente por nuestro canal oficial."
            )
        else:
            mensaje_respuesta = (
                "Bienvenido al Condominio Reserva del Mar en Playa Salguero, Santa Marta. "
                "Disfruta del mejor descanso frente al mar Caribe con exclusividad y confort."
            )

        return {
            "version": "1.7.0-geo",
            "intencion": {
                "tipo": tipo_intencion,
                "es_reserva": es_reserva,
                "es_turistica": es_turistica,
                "coincidencias": [mensaje_usuario] if (es_reserva or es_turistica) else []
            },
            "datos_reserva": {
                "personas": personas,
                "fecha_llegada": fecha_estancia,
                "fecha_salida": "Por confirmar",
                "reserva_completa": reserva_completa
            },
            "respuesta": {
                "mensaje": mensaje_respuesta,
                "recursos_oficiales": self.recursos_oficiales
            }
        }
