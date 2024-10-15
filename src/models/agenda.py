from cita import Cita
import pandas as pd


class Agenda:
    def __init__(self, base_datos_citas):
        self.datos_csv_citas = base_datos_citas

    def agendar_cita(self, fecha, hora, paciente, medico):
        agendar = Cita(fecha, hora, paciente, medico)
        nueva_cita = pd.DataFrame(agendar.crear_cita())
        self.datos_csv_citas = pd.concat(
            [self.datos_csv_citas, nueva_cita], ignore_index=True
        )
        return self.datos_csv_citas

    def reagendar_cita(self, fecha, hora, paciente, medico):
        self.cancelar_cita(paciente, fecha)
        self.agendar_cita(fecha, hora, paciente, medico)
        return self.datos_csv_citas

    def cancelar_cita(self, paciente, fecha_cita):
        df = self.datos_de_citas[
            ~(
                (self.datos_de_citas["pacientes"] == paciente)
                & (self.datos_de_citas["fecha"] == fecha_cita)
            )
        ]
        self.datos_csv_citas = df
        return self.datos_csv_citas

    def consultar_agenda_medico(self, cedula_medico):
        # Convertir la cédula del médico a string
        cedula_medico = str(cedula_medico)

        # Filtrar el DataFrame por la cédula del médico
        return self.datos_csv_citas[
            self.datos_csv_citas["medico"].astype(str) == cedula_medico
        ]

    def consultar_citas_paciente(self, cedula_paciente):
        return self.datos_csv_citas[
            self.datos_csv_citas["paciente"] == cedula_paciente
        ]

    def notificar_a_paciente(self, cedula):
        pass
