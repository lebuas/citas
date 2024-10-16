from correo import Correo
from whatsapp import WhatsApp
from celular import Celular


class Notificaciones:
    def __init__(self, nombre, celular, correo, fecha, hora, asunto):
        self.celular = celular
        self.correo = correo

        self.mensajes = {
            1: f"Señor(a) {nombre}, se le ha agendado una cita con fecha {fecha} y hora {hora}",
            2: f"Señor(a) {nombre}, su cita se ha movido a la fecha {fecha} y hora {hora}",
            3: f"Señor(a) {nombre}, su cita del día {fecha} y hora {hora} ha sido eliminada"
        }

        indice = {
            "agendar": 1,
            "reagendar": 2,
            "cancelar": 3
        }.get(asunto, 3)  # Por defecto, cancelar

        mensaje = self.mensajes[indice]
        self.notificar_a_correo = Correo(self.correo, asunto, mensaje)
        self.notificar_a_whatsapp = WhatsApp(self.celular, mensaje)
        self.notificar_a_celular = Celular(self.celular, mensaje)

    def enviar_notificaciones(self):
        self.notificar_a_correo.enviar_correo()
        self.notificar_a_celular.enviar_mensaje()
        self.notificar_a_whatsapp.enviar_whatsapp()
