
class Cita:
    def __init__(self, fecha, hora, paciente, medico):
        self.fecha = fecha
        self.hora = hora
        self.paciente = paciente
        self.medico = medico

    def crear_cita(self, fecha, hora, paciente, medico):
        return {
            "fecha": [fecha.strftime("%Y-%m-%d")],  # Convertir a string
            "hora": [hora.strftime("%H:%M:%S")],    # Convertir a string
            "paciente": [paciente],
            "medico": [medico]
        }
