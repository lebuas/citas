from datetime import datetime
from cita import Cita
import pandas as pd
from notificacion import Notificaciones


class Agenda:
    def __init__(self, base_datos_citas):
        self.datos_csv_citas = base_datos_citas

    def agendar_cita(self, fecha, hora, paciente, medico):
        agendar = Cita(fecha, hora, paciente, medico)
        nueva_cita = pd.DataFrame(agendar.crear_cita())
        self.datos_csv_citas = pd.concat(
            [self.datos_csv_citas, nueva_cita], ignore_index=True
        )

        # Guardar el DataFrame actualizado en un archivo CSV
        self.datos_csv_citas.to_csv('../data/citas.csv', index=False)

    def reagendar_cita(self, nueva_fecha, nueva_hora, paciente, medico):
        # Agregar la nueva cita
        self.agendar_cita(nueva_fecha, nueva_hora, paciente, medico)

    def cancelar_cita(self, indice):
        # Eliminar la cita por el índice
        self.datos_csv_citas.drop(index=int(indice), inplace=True)

        # Guardar el DataFrame actualizado en el archivo CSV
        self.datos_csv_citas.to_csv('../data/citas.csv', index=False)

    def consultar_agenda_medico(self, cedula_medico):
        return self.datos_csv_citas[
            self.datos_csv_citas["medico"] == int(cedula_medico)
        ]

    def consultar_citas_paciente(self, cedula_paciente):
        return self.datos_csv_citas[
            self.datos_csv_citas["paciente"] == int(cedula_paciente)
        ]

    def horario_disponible(self, medico, fecha, hora):
        # Asegúrate de que 'fecha' es un objeto datetime y 'hora' es un objeto time
        if isinstance(fecha, str):
            # Convierte a datetime si es un string
            fecha = datetime.strptime(fecha, "%d/%m/%Y")
        if isinstance(hora, str):
            # Convierte a time si es un string
            hora = datetime.strptime(hora, "%H:%M:%S").time()

        # Combina la fecha y la hora para crear un objeto datetime
        cita_datetime = datetime.combine(
            fecha.date(), hora)  # Combina la fecha y la hora

        agenda = self.consultar_agenda_medico(medico)

        if agenda.empty:
            return True  # No hay citas, horario disponible

        for index, cita in agenda.iterrows():
            # Convierte 'fecha' y 'hora' de la cita a datetime
            cita_existente_datetime = datetime.strptime(
                f"{cita['fecha']} {cita['hora']}", "%Y-%m-%d %H:%M:%S"
            )

            # Comprobar si hay una superposición en las citas
            if abs((cita_existente_datetime - cita_datetime).total_seconds()) < 1200:
                return False  # Hay una superposición en las citas

        return True  # El horario está disponible
