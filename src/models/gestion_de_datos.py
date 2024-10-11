import os
import json
import csv


class GestionDeDatos:
    def __init__(self):
        base_dir = os.path.join(os.getcwd(), "src", "data")
        self.ruta_datos_medicos = os.path.join(base_dir, "medicos.json")
        self.ruta_datos_pacientes = os.path.join(base_dir, "pacientes.csv")
        self.ruta_datos_citas = os.path.join(base_dir, "citas.csv")

        self.datos_medicos = {}
        self.datos_pacientes = []
        self.datos_citas = []

    def cargar_datos_medicos(self):
        with open(self.ruta_datos_medicos, 'r', encoding='utf-8') as file:
            return json.load(file)

    def cargar_datos_pacientes(self):

        with open(self.ruta_datos_pacientes, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)

    def cargar_datos_citas(self):

        with open(self.ruta_datos_citas, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)

    def actualizar_datos_json(self):

        # Guardar datos de médicos en JSON
        with open(self.ruta_datos_medicos, 'w', encoding='utf-8') as file:
            json.dump(self.datos_medicos, file, ensure_ascii=False, indent=4)

    def actualizar_datos_csv(self):
        # Guardar datos de pacientes en CSV
        with open(self.ruta_datos_pacientes, 'w', encoding='utf-8', newline='') as file:
            fieldnames = self.datos_pacientes[0].keys(
            ) if self.datos_pacientes else []
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.datos_pacientes)
