from aplicacion import Aplicacion
from celular import Celular
from correo import Correo


class Notificacion:
    """
    Pide datos al metodo "cargar_datos" de la clase Hospital y genera un
    mensaje dependiendo de que tipo de nofificación se va a realizar;
    Notificación de creaciones de citas, notificacion de reagendamiento
    de citas o notificacon sobre eliminiacion de una citas.
    """

    def __init__(self):
        self.correo = Correo()
        self.celular = Celular()
        self.aplicacion = Aplicacion()

    def enviar_notificacion(self):
        return self.aplicacion.enviar_notificacion()

    def verificar_correo(self):
        print(f"Verificando correo {self.correo}")
