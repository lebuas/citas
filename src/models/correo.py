class Correo:
    def __init__(self, correo, asunto, mensaje):
        self.correo = correo
        self.asunto = asunto
        self.mensaje = mensaje

    def enviar_correo(self):
        print(
            f"Enviando correo a {self.correo} con asunto: {self.asunto} y mensaje {self.mensaje}")
