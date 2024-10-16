from datetime import datetime
from cita import Cita
import pandas as pd
from datetime import datetime, timedelta


class Agenda:
    def __init__(self, base_datos_citas):
        self.datos_csv_citas = base_datos_citas

    def agendar_cita(self, fecha, hora, paciente, medico):
        agendar = Cita(fecha, hora, paciente, medico)
        nueva_cita = pd.DataFrame(
            agendar.crear_cita(fecha, hora, paciente, medico))
        self.datos_csv_citas = pd.concat(
            [self.datos_csv_citas, nueva_cita], ignore_index=True
        )
        # Guardar el DataFrame actualizado en un archivo CSV
        self.datos_csv_citas.to_csv('../data/citas.csv', index=False)

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
        # Filtrar el DataFrame por la cédula del médico
        return self.datos_csv_citas[
            self.datos_csv_citas["medico"].astype(str) == cedula_medico
        ]

    def consultar_citas_paciente(self, cedula_paciente):
        return self.datos_csv_citas[
            self.datos_csv_citas["paciente"] == cedula_paciente
        ]

    def horario_disponible(self, medico, fecha, hora):
        # Obtener la agenda del médico
        agenda = self.consultar_agenda_medico(medico)

        # Convertir la fecha y hora ingresadas en un objeto datetime
        cita_datetime = datetime.combine(fecha, hora)

        # Comprobar si la agenda está vacía
        if agenda.empty:
            return True  # No hay citas, horario disponible

        # Iterar sobre las citas existentes en la agenda
        for index, cita in agenda.iterrows():
            cita_existente_datetime = datetime.strptime(
                f"{cita['fecha']} {cita['hora']}", "%Y-%m-%d %H:%M:%S")

            # Comprobar si la nueva cita tiene al menos 20 minutos de diferencia
            if abs((cita_existente_datetime - cita_datetime).total_seconds()) < 1200:
                return False  # Hay un conflicto

        return True  # El horario está disponible

        def notificar_a_paciente(self, cedula):
            pass
