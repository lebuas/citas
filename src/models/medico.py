class Medico:
    def __init__(self, cedula, nombre, correo, especialidad):
        self.cedula = cedula
        self.nombre = nombre
        self.correo = correo
        self.especialidad = especialidad
        self.crear_medioco()

    def crear_medioco(self):
        return {
            "id": self.cedula,
            "nombre": self.nombre,
            "correo": self.correo,
            "especialidad": self.especialidad
        }
