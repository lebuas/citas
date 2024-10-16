
class Cita:
    def __init__(self, fecha, hora, paciente, medico):
        self.fecha = fecha  # Se espera un objeto datetime
        self.hora = hora    # Se espera un objeto time
        self.paciente = paciente
        self.medico = medico

    def crear_cita(self):
        return {
            # Formato para almacenamiento
            "fecha": [self.fecha.strftime("%Y-%m-%d")],
            # Formato para almacenamiento
            "hora": [self.hora.strftime("%H:%M:%S")],
            "paciente": [self.paciente],
            "medico": [self.medico]
        }
