# Asegúrate de que esta clase maneje la carga de datos de médicos y pacientes
from datetime import datetime, timedelta
from hospital import Hospital
from agenda import Agenda
hospital = Hospital()


def opcion1():
    while True:
        print("\n--Opciones disponibles en el Hospital--")
        print("1. Agregar un Médico")
        print("2. Agregar un Paciente")
        print("3. Consultar Médico")
        print("4. Consultar Paciente")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Ingreso de cédula como string
            while True:
                cedula = input("Ingrese la cédula del médico: ")
                if cedula.isdigit():
                    # Salir del bucle si es un número válido (cadena numérica)
                    break
                else:
                    print("Error: La cédula debe contener solo números.")

            # Verificar si ya existe un médico con esa cédula
            if hospital.consultar_medico(cedula):
                print(f"Error: Ya existe un médico con la cédula {cedula}.")
            else:
                nombre = input("Ingrese el nombre del médico: ")
                correo = input("Ingrese el correo del médico: ")
                especialidad = input("Ingrese la especialidad del médico: ")
                hospital.agregar_medico(cedula, nombre, correo, especialidad)
                print(f"Médico {nombre} agregado exitosamente.")

        elif opcion == "2":
            # Agregar paciente
            while True:
                cedula = input("Ingrese la cédula del paciente: ")
                if cedula.isdigit():
                    # Salir del bucle si es un número válido (cadena numérica)
                    break
                else:
                    print("Error: La cédula debe contener solo números.")

            nombre = input("Ingrese el nombre del paciente: ")
            celular = input("Ingrese el celular del paciente: ")
            correo = input("Ingrese el correo del paciente: ")
            hospital.agregar_paciente(cedula, nombre, celular, correo)
            print(f"Paciente {nombre} agregado exitosamente.")

        elif opcion == "3":
            # Consultar médico
            while True:
                cedula = input(
                    "Ingrese la cédula del médico que desea consultar: ")
                if cedula.isdigit():
                    # Salir del bucle si es un número válido (cadena numérica)
                    break
                else:
                    print("Error: La cédula debe contener solo números.")

            medico = hospital.consultar_medico(cedula)
            if medico:
                print("\nInformación del médico:")
                for key, value in medico.items():
                    print(f"{key.capitalize()}: {value}")
            else:
                print(f"No se encontró ningún médico con la cédula {cedula}.")

        elif opcion == "4":
            # Consultar paciente
            while True:
                cedula = input(
                    "Ingrese la cédula del paciente que desea consultar: ")
                if cedula.isdigit():
                    # Salir del bucle si es un número válido (cadena numérica)
                    break
                else:
                    print("Error: La cédula debe contener solo números.")

            paciente = hospital.consultar_paciente(cedula)
            if paciente:
                print("\nInformación del paciente:")
                for key, value in paciente.items():
                    print(f"{key.capitalize()}: {value}")
            else:
                print(
                    f"No se encontró ningún paciente con la cédula {cedula}.")

        elif opcion == "0":
            # Salir
            print("Saliendo del menú del hospital...")
            break

        else:
            print("Opción inválida, por favor intente nuevamente.")


def opcion2():
    while True:
        print("\n --Opciones disponibles para Médicos --")
        print("1. Consulta Agenda")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Consulta Agenda
            cedula = input("Ingrese la cédula del médico: ")

            # Validar que la cédula es numérica y tiene la longitud correcta
            if not cedula.isdigit() or len(cedula) > 10 or len(cedula) < 6:
                print("Ingrese una cédula valida entre de 6 a 10 digitos.")
                continue

            # Consultar médico primero para validar que existe
            medico = hospital.consultar_medico(cedula)
            if medico:
                # Si el médico existe, consultar la agenda
                agenda = Agenda(hospital.datos_de_citas)
                citas = agenda.consultar_agenda_medico(cedula)

                if not citas.empty:
                    print(f"\nAgenda del médico con cédula {cedula}:")
                    for index, cita in citas.iterrows():
                        print(
                            f"Fecha: {cita['fecha']}, Hora: {cita['hora']}, Paciente: {cita['paciente']}")
                else:
                    print(
                        f"No hay citas agendadas para el médico con cédula {cedula}.")
            else:
                print(f"No se encontró ningún médico con la cédula {cedula}.")

        elif opcion == "0":
            # Salir
            print("Saliendo del menú de la agenda...")
            break

        else:
            print("Opción inválida, por favor intente nuevamente.")


def opcion3():
    agenda = Agenda(hospital.datos_de_citas)
    while True:
        print("\n --Opciones disponibles para Pacientes --")
        print("1. Agendar una cita")
        print("2. Reagendar una cita")
        print("3. Cancelar una cita")
        print("4. Consultar citas disponibles")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        # Opción 1: Agendar una cita
        if opcion == "1":
            paciente = input("Ingrese la cédula del paciente: ")
            if hospital.consultar_paciente(paciente):
                print("\n")
                for datos in hospital.datos_de_medicos:
                    print(
                        f"Cédula: {datos['id']} Nombre: {datos['nombre']} Especialidad: {datos['especialidad']}"
                    )

                # Seleccionar médico
                while True:
                    print("\nSeleccione médico de la lista....")
                    medico = input("Ingrese la cédula del médico: ")
                    if hospital.consultar_medico(medico):
                        break
                    print("Médico no encontrado, verifica la cédula.")

                # Seleccionar fecha y hora
                while True:
                    fecha = obtener_fecha()
                    hora = obtener_hora()

                    if agenda.horario_disponible(medico, fecha, hora):
                        agenda.agendar_cita(fecha, hora, paciente, medico)
                        print("Su cita ha sido agendada.")
                        break
                    else:
                        print("Fecha y hora no disponibles, seleccione otro horario.")
                        continue

            else:
                print(
                    f"Paciente {paciente} no se encuentra afiliado, o verifique cédula ingresada."
                )

        # Opción 2: Reagendar una cita
        elif opcion == "2":
            paciente = input("Ingrese la cédula del paciente: ")
            if hospital.consultar_paciente(paciente):
                citas_paciente = agenda.consultar_citas_paciente(paciente)
                if citas_paciente.empty:
                    print(f"El paciente {paciente} no tiene citas agendadas.")
                    continue

                # Mostrar citas actuales del paciente con sus índices
                print("Citas actuales del paciente (índice - fecha - hora - médico):")
                print(citas_paciente.reset_index()[
                    ['index', 'fecha', 'hora', 'medico']
                ])

                # Solicitar el índice de la cita a reagendar
                indice_cita = input(
                    "Ingrese el índice de la cita a reagendar: ")

                # Verificar si el índice es válido
                if int(indice_cita) in citas_paciente.index:
                    cita_actual = citas_paciente.loc[int(indice_cita)]
                    medico_actual = cita_actual["medico"]

                    # Solicitar nueva fecha y hora
                    while True:
                        print("\nIngrese la nueva fecha")
                        nueva_fecha = obtener_fecha()
                        print("\nIngrese la nueva hora")
                        nueva_hora = obtener_hora()

                        # Verificar disponibilidad
                        if agenda.horario_disponible(medico_actual, nueva_fecha, nueva_hora):
                            agenda.cancelar_cita(indice_cita)
                            agenda.agendar_cita(
                                nueva_fecha, nueva_hora, paciente, medico_actual)
                            print("Cita reagendada exitosamente.")
                            break
                        else:
                            print(
                                "El horario no está disponible, elija otro horario.")
                else:
                    print("Índice no encontrado, verifica el valor ingresado.")
            else:
                print(
                    f"Paciente {paciente} no se encuentra afiliado, o verifique cédula ingresada.")

        # Opción 3: Cancelar una cita
        elif opcion == "3":
            paciente = input("Ingrese la cédula del paciente: ")
            if hospital.consultar_paciente(paciente):
                citas_paciente = agenda.consultar_citas_paciente(paciente)
                if citas_paciente.empty:
                    print(f"El paciente {paciente} no tiene citas agendadas.")
                    continue

                # Mostrar citas actuales del paciente con sus índices
                print("Citas actuales del paciente (índice - fecha - hora - médico):")
                print(citas_paciente.reset_index()[
                    ['index', 'fecha', 'hora', 'medico']
                ])

                # Solicitar el índice de la cita a cancelar
                indice_cita = input(
                    "Ingrese el índice de la cita a cancelar: ")

                # Verificar si el índice es válido
                if int(indice_cita) in citas_paciente.index:
                    agenda.cancelar_cita(indice_cita)
                    print(
                        f"La cita con índice {indice_cita} ha sido cancelada.")
                else:
                    print("Índice no encontrado, verifica el valor ingresado.")
            else:
                print(
                    f"Paciente {paciente} no se encuentra afiliado, o verifique cédula ingresada.")

        elif opcion == "4":  # Consultar citas disponibles
            paciente = input("Ingrese la cedula del paciente: ")
            if hospital.consultar_paciente(paciente):
                citas_paciente = agenda.consultar_citas_paciente(paciente)
                if citas_paciente.empty:
                    print(f"El paciente {paciente} no tiene citas agendadas.")
                else:
                    print("Citas actuales del paciente:")
                    print(citas_paciente[['fecha', 'hora', 'medico']])
            else:
                print(
                    f"Paciente {paciente} no se encuentra afiliado, o verifique cedula ingresada.")

        # Opción 0: Salir
        elif opcion == "0":
            break


def obtener_fecha():
    while True:
        fecha = input("Ingresar la fecha (YYYY-MM-DD) [Ejemplo: 2024-10-15]: ")
        try:
            # Validar y convertir la fecha
            fecha = datetime.strptime(fecha, "%Y-%m-%d")
            return fecha  # Devolver la fecha si es válida
        except ValueError:
            print("Formato de fecha no válido. Por favor, intente de nuevo.")


def obtener_hora():
    while True:
        hora = input("Ingresar la hora (HH:MM:SS) [Ejemplo: 14:30:00]: ")
        try:
            # Validar y convertir la hora
            hora = datetime.strptime(hora, "%H:%M:%S").time()
            return hora  # Devolver la hora si es válida
        except ValueError:
            print("Formato de hora no válido. Por favor, intente de nuevo.")


while True:
    print("\n--- Menú ---")
    print("1.Hospital")
    print("2.Medico")
    print("3.Paciente")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        opcion1()
    elif opcion == "2":
        opcion2()
    elif opcion == "3":
        opcion3()
    elif opcion == "0":
        print("Saliendo.......")
        break
    else:
        print("Opciones invalida, intentar nuevamente..")
