
class Cita:
    def __init__(self, paciente, medico, fecha, hora):
        self.fecha = fecha
        self.hora = hora
        self.paciente = paciente
        self.medico = medico

    def crear_cita(self) -> dict:
        return {
            "fecha": self.fecha,
            "hora": self.hora,
            "paciente": self.paciente,
            "medico": self.medico
        }
