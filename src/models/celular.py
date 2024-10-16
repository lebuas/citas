class Celular:
    def __init__(self, celular, mensaje):
        self.celular = celular
        self.mensaje = mensaje
        self.enviar_mensaje()

    def enviar_mensaje(self):
        print(
            f"Enviando mensaje de texto para {self.celular}, con contenido: {self.mensaje}")
