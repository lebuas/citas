
# Mejoras Realizadas

1. **Corrección de Notificaciones**:
   - Los datos de contacto, como correo y celular, ahora son gestionados por la calse hospital

2. **Incorporación de WhatsApp**:
   - Se ha agregado WhatsApp como una nueva forma de notificación, lo que amplía las opciones de comunicación con los pacientes.

3. **Reestructuración de la Agenda**:
   - Se ha corregido la implementación de la agenda y las citas. Ahora, la agenda se gestiona a nivel  general, en lugar de estar asociada solo al medico.

4. **Corrección de la Terminología**:
   - Se ha cambiado el término "usuarios" a "pacientes", para reflejar con mayor precisión los roles dentro del sistema.

5. **Nuevos Métodos de Búsqueda**:
   - Se han implementado los métodos `buscar_paciente()` y `buscar_medico()` en la clase `Hospital`, facilitando la búsqueda de información de pacientes y medicos.

6. **Manejo de Citas**:
   - Se ha corregido los métodos de agendar y cancelar citas para que no se gestionen desde el paciente, sino desde la agenda.

7. **Búsqueda de Datos de Citas**:
   - Se ha reestructurado la forma en que se buscan los datos de una cita, permitiendo que la búsqueda desde la agenda general por medicos o por pacientes.

8. **Gestión de Citas**:
   - Se está revisando cómo manejar la opción de "mover" citas, para mejorar la flexibilidad del sistema.

9. **Mejoras en la Interfaz de Texto**:
   - Se ha mejorado la interfaz de usuario utilizando la librería Rich, lo que permite crear menús, realizar capturas de datos y generar reportes de manera más visual y amigable.

10. **Carga de Datos Iniciales**:
    - Se ha implementado la capacidad de cargar datos iniciales de pacientes, médicos y citas desde archivos CSV y JSON, facilitando la gestión de datos.

11. **Citas con Fecha y Hora**:
    - Se ha asegurado que las citas se manejen con fecha y hora, programadas en intervalos de 20 minutos, para optimizar la gestión del tiempo.

12. **Selección de Especialidad para Citas**:
    - Al crear una nueva cita, el paciente ahora selecciona la especialidad, y el sistema muestra los médicos que pertenecen a esa especialidad, mejorando la experiencia del usuario.

## Mas Mejoras
1. **Gestios de datos**

- Se creo una clase GestionDeDatos, encargada administrar los datos que carga la clase hopital al iniciar el programa.

2. **Consultar Agenda Medico**
- Se creo un metodo en la clase Agenda, qee permite ver la genda qee tiene un medico si ingresamos su numero de id*(cedula), los mismo para pacientes.

3. **Guardado de los datos**
- Se agrego funcionalida para guardar los datos que se crean durante la ejecucio del programa, como agregar un paciente, un doctor o eliminar citas, reagendar citas o eliminar citas y estos movimiento quda guardado en los archivos de datos que se cargan al iniciar el prgrama(cita.csv,pacientes.csv, medicos.json).
