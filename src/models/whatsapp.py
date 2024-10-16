class WhatsApp:
    def __init__(self, celular, mensaje):
        self.celular = celular
        self.mensaje = mensaje

    def enviar_whatsapp(self):
        print(
            f"Enviando mensaje de ewhatsapp  a {self.celular} con mensaje {self.mensaje}")
