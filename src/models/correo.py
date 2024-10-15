class Correo:
    def Correo(self, correo, asunto, mensaje):
        self.correo = correo
        self.asunto = asunto
        self.mensaje = mensaje

    def enviar_correo(self, para, asunto):
        print(f"Enviando correo a {para} con asunto: {asunto}")
