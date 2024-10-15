import os
import json
import pandas as pd


class GestionDeDatos:
    def __init__(self):
        # Base directory for data files
        base_dir = os.path.join(os.getcwd(), "src", "data")

        # Paths to files
        self.ruta_datos_json_medicos = os.path.join(base_dir, "medicos.json")
        self.ruta_datos_pacientes = os.path.join(base_dir, 'pacientes.csv')
        self.ruta_datos_citas = os.path.join(base_dir, 'citas.csv')

        # Load data when the class is initialized
        self.datos_medicos = self.cargar_datos_json_medicos()
        self.datos_pacientes = pd.read_csv(self.ruta_datos_pacientes)
        self.datos_citas = pd.read_csv(self.ruta_datos_citas)

    def cargar_datos_json_medicos(self):
        # Load JSON data for doctors
        if os.path.exists(self.ruta_datos_json_medicos):
            with open(self.ruta_datos_json_medicos, 'r', encoding='utf-8') as file:
                return json.load(file)
        else:
            print(f"Archivo {self.ruta_datos_json_medicos} no encontrado.")
            return {}

    def actualizar_datos_json(self, nuevos_datos):
        # Save updated doctors data to JSON
        with open(self.ruta_datos_json_medicos, 'w', encoding='utf-8') as file:
            json.dump(nuevos_datos, file, ensure_ascii=False, indent=4)

    def actualizar_datos_csv(self, tipo, datos):
        # Save updated data to CSV files
        if tipo == 'pacientes':
            datos.to_csv(self.ruta_datos_pacientes, index=False)
        elif tipo == 'citas':
            datos.to_csv(self.ruta_datos_citas, index=False)
