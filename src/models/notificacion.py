from correo import Correo
from whatsapp import WhatsApp
from celular import Celular


class Notificaciones:

    def __init__(self, nombre, celular, correo, fecha_hora_cita):
        self.nombre = nombre
        self.celuar = celular
        self.correo = correo
        self.fecha_hora = fecha_hora_cita

        self.notificar_a_correo = Correo()
        self.notificar_a_whatsapp = WhatsApp()
        self.notificar_a_celuar = Celular()

    def notificar_agendamieto_de_cita(self, datos_pacientes, fecha, hora):
        mensaje = f"Señor: {nombre} se le ha agendado una cita para{fechca}{hora}"

    def notificar_cancelacion_de_cita(self):
        pass

    def notificar_reagendamiento_de_cita():
        pass

    def enviar_recordatorio_de_cita():
        pass
