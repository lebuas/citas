from gestion_de_datos import GestionDeDatos
from medico import Medico
from paciente import Paciente
import pandas as pd


class Hospital:
    def __init__(self):
        self.gestionar_datos = GestionDeDatos()
        # diccionario proveniente de un JSON
        self.datos_de_medicos = self.gestionar_datos.datos_medicos
        self.datos_de_pacientes = self.gestionar_datos.datos_pacientes  # DataFrame
        self.datos_de_citas = self.gestionar_datos.datos_citas  # DataFrame

    def agregar_medico(self, nombre, cedula, celular, especialidad):
        medico = Medico(nombre, cedula, celular, especialidad)
        nuevo_medico = medico.crear_medico()
        self.datos_de_medicos.update(nuevo_medico)

    def agregar_paciente(self, cedula, nombre, celular, correo):
        paciente = Paciente(cedula, nombre, celular, correo)
        # Supongamos que esto devuelve un dict
        nuevo_paciente = paciente.crear_paciente()

        # Convertir nuevo_paciente (dict) a DataFrame
        # Usa una lista para crear un DataFrame
        nuevo_paciente_df = pd.DataFrame([nuevo_paciente])

        # Actualiza el DataFrame de pacientes usando concat
        self.datos_de_pacientes = pd.concat(
            [self.datos_de_pacientes, nuevo_paciente_df], ignore_index=True)

    def consultar_medico(self, cedula):
        for medico in self.datos_de_medicos.values():
            if medico['cedula'] == cedula:
                return medico
        return None

    def consultar_paciente(self, cedula):
        # Usar DataFrame para la consulta
        paciente = self.datos_de_pacientes[self.datos_de_pacientes['cedula'] == cedula]
        return paciente.to_dict(orient='records')[0] if not paciente.empty else None

    def guardar_datos(self, data):
        # Llamar a los métodos de actualización para guardar los datos
        if data == "medicos":
            self.gestionar_datos.actualizar_datos_json(self.datos_de_medicos)
        elif data == "pacientes":  # Corregido de "pecientes" a "pacientes"
            self.gestionar_datos.actualizar_datos_csv(
                'pacientes', self.datos_de_pacientes)
        else:
            self.gestionar_datos.actualizar_datos_csv(
                'citas', self.datos_de_citas)
