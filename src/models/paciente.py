class Paciente:
    def __init__(self, nombre, cedula, celular, correo):
        self.cedula = cedula
        self.nombre = nombre
        self.celular = celular
        self.correo = correo
        self.crear_paciente()

    def crear_paciente(self) -> dict:
        return {
            "cedula": self.cedula,
            "nombre": self.nombre,
            "celular": self.celular,
            "correo": self.correo
        }
