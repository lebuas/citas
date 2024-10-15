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

    print("\n --Opciones disponible para Pacientes ")
    print("1. Agendar una cita")
    print("2. Reagendar una cita")
    print("1. Cancelar una cita")
    print("1. Consutar cita disponibles")
    print("0. Salir")
    opcion = input("Ingrese una opcion: ")


def opcione4():
    pass


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
    elif opcion == "4":
        opcione4()
    elif opcion == "0":
        print("Saliendo.......")
        break
    else:
        print("Opciones invalida, intentar nuevamente..")
