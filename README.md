

# Sistema de Gestión de Citas Médicas

Este proyecto es un sistema de gestión de citas médicas diseñado para permitir a los pacientes solicitar citas, a los médicos gestionar sus agendas y generar reportes detallados. El sistema incluye funciones para notificaciones, verificación de disponibilidad y cancelación de citas, y está basado en los requerimientos obtenidos del cliente.

## Requerimientos

- **Verificación de Disponibilidad**: El sistema verifica la disponibilidad de los médicos según su especialidad y la fecha de la cita.
- **Asignación de Médico Preferido**: Los pacientes pueden seleccionar un médico preferido para futuras citas.
- **Gestión de Agenda**: Los médicos tienen una agenda donde se almacenan las citas pendientes y realizadas.
- **Notificaciones**: Se envían notificaciones a los pacientes para recordar sus citas a través de llamadas, mensajes de texto o correo electrónico.
- **Cancelación y Reprogramación de Citas**: Los pacientes pueden cancelar y reprogramar citas según la disponibilidad de los médicos.
- **Generación de Reportes**: El sistema puede generar reportes de demanda, tendencias de citas, causas de cancelaciones, y ausentismo, los cuales pueden exportarse a Excel.

## Clonar el repositorio:
Para clonar el repositorio, ingresamos a la terminal y nos dirigimos a la carpeta donde vamos a clonar el repositorio e ingresamos en siguiente comando:

 ```bash
    git clone https://github.com/lebuas/citas.git
 ```

## Activar entorno virtual:
Para activar un entorno virtual, nos ubicamos en la raíz de la carpeta donde esta el directorio del entorno virtual donde clonamos el repositorio, e ingresamos el siguiente comando:

##### Para windows:

 ```bash
   venv\Scripts\activate
 ```


##### Para linux(ubuntu):

 ```bash
   source vevn/bin/activate
 ```

## Instalar requerimientos
Una vez el entorno virtual este activo, usamos este comando en la raiz del directorio donde esta el proyecto para instalar requerimientos:

 ```bash
    pip install -r requirements.txt
 ```


## Ejecución del programa
Para ejecutar el programa, teniendo el entorno virtual activo con los requerimientos instalados, usamos el siguientes comando desde la raíz del proyecto.

 ```bash
    python src/models/main.py
 ```


