class Celular:
    def __init__(self, celular, mensaje):
        self.celular = celular
        self.mensaje = mensaje

    def enviar_mensaje(self, numero_celular, mensaje):
        print(
            f"Enviando mensaje de texto para {numero_celular}, con contenido: {mensaje}")

    def realizar_llamada(self, numero_celular):
        print(f"Realizando llamada telefónica a {numero_celular}")
