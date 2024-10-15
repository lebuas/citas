import os
import json
import pandas as pd


class GestionDeDatos:
    def __init__(self):
        base_dir = os.path.join(os.getcwd(), "src", "data")
        self.ruta_datos_json_medicos = os.path.join(base_dir, "medicos.json")

        # Cargar datos al inicializar la clase
        self.datos_medicos = self.cargar_datos_json_medicos()
        self.datos_pacientes = pd.read_csv(os.path(base_dir, 'pacientes.csv'))
        self.datos_citas = pd.read_csv(os.path(base_dir, 'citas.csv'))

    def cargar_datos_json_medicos(self):
        with open(self.ruta_datos_json_medicos, 'r', encoding='utf-8') as file:
            return json.load(file)

    def actualizar_datos_json(self, nuevos_datos):
        # Guardar datos de médicos en JSON
        with open(self.ruta_datos_json_medicos, 'w', encoding='utf-8') as file:
            json.dump(nuevos_datos, file, ensure_ascii=False, indent=4)

    def actualizar_datos_csv(self):
        pass
