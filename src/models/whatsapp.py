class Wtatsapp:
    def Correo(self, ceular, mensaje):
        self.celuar = ceular
        self.mensaje = mensaje

    def enviar_whatsapp(self):
        print(
            f"Enviando mensaje de ewhatsapp  a {self.celuar} con mensaje {self.mensaje}")
