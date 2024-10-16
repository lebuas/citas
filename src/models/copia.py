from datetime import datetime
from hospital import Hospital
from agenda import Agenda
from notificacion import Notificaciones
from rich.console import Console

console = Console()
hospital = Hospital()


def opcion1():
    while True:
        console.print(
            "\n[bold blue]--Opciones disponibles en el Hospital--[/bold blue]")
        console.print("1. [green]Agregar un Médico[/green]")
        console.print("2. [green]Agregar un Paciente[/green]")
        console.print("3. [yellow]Consultar Médico[/yellow]")
        console.print("4. [yellow]Consultar Paciente[/yellow]")
        console.print("0. [red]Salir[/red]")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                cedula = input("Ingrese la cédula del médico: ")
                if cedula.isdigit():
                    break
                else:
                    console.print(
                        "[red]Error: La cédula debe contener solo números.[/red]")

            if hospital.consultar_medico(cedula):
                console.print(
                    f"[red]Error: Ya existe un médico con la cédula {cedula}.[/red]")
            else:
                nombre = input("Ingrese el nombre del médico: ")
                correo = input("Ingrese el correo del médico: ")
                especialidad = input("Ingrese la especialidad del médico: ")
                hospital.agregar_medico(cedula, nombre, correo, especialidad)
                console.print(
                    f"[green]Médico {nombre} agregado exitosamente.[/green]")

        elif opcion == "2":
            while True:
                cedula = input("Ingrese la cédula del paciente: ")
                if cedula.isdigit():
                    break
                else:
                    console.print(
                        "[red]Error: La cédula debe contener solo números.[/red]")

            nombre = input("Ingrese el nombre del paciente: ")
            celular = input("Ingrese el celular del paciente: ")
            correo = input("Ingrese el correo del paciente: ")
            hospital.agregar_paciente(cedula, nombre, celular, correo)
            console.print(
                f"[green]Paciente {nombre} agregado exitosamente.[/green]")

        elif opcion == "3":
            while True:
                cedula = input(
                    "Ingrese la cédula del médico que desea consultar: ")
                if cedula.isdigit():
                    break
                else:
                    console.print(
                        "[red]Error: La cédula debe contener solo números.[/red]")

            medico = hospital.consultar_medico(cedula)
            if medico:
                console.print(
                    "\n[bold blue]Información del médico:[/bold blue]")
                for key, value in medico.items():
                    console.print(f"[cyan]{key.capitalize()}[/cyan]: {value}")
            else:
                console.print(
                    f"[red]No se encontró ningún médico con la cédula {cedula}.[/red]")

        elif opcion == "4":
            while True:
                cedula = input(
                    "Ingrese la cédula del paciente que desea consultar: ")
                if cedula.isdigit():
                    break
                else:
                    console.print(
                        "[red]Error: La cédula debe contener solo números.[/red]")

            paciente = hospital.consultar_paciente(cedula)
            if paciente:
                console.print(
                    "\n[bold blue]Información del paciente:[/bold blue]")
                for key, value in paciente.items():
                    console.print(f"[cyan]{key.capitalize()}[/cyan]: {value}")
            else:
                console.print(
                    f"[red]No se encontró ningún paciente con la cédula {cedula}.[/red]")

        elif opcion == "0":
            console.print(
                "[bold red]Saliendo del menú del hospital...[/bold red]")
            break

        else:
            console.print(
                "[red]Opción inválida, por favor intente nuevamente.[/red]")


def opcion2():
    while True:
        console.print(
            "\n[bold blue]--Opciones disponibles para Médicos--[/bold blue]")
        console.print("1. [yellow]Consulta Agenda[/yellow]")
        console.print("0. [red]Salir[/red]")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cedula = input("Ingrese la cédula del médico: ")

            if not cedula.isdigit() or len(cedula) > 10 or len(cedula) < 6:
                console.print(
                    "[red]Ingrese una cédula válida entre 6 a 10 dígitos.[/red]")
                continue

            medico = hospital.consultar_medico(cedula)
            if medico:
                agenda = Agenda(hospital.datos_de_citas)
                citas = agenda.consultar_agenda_medico(cedula)

                if not citas.empty:
                    console.print(
                        f"\n[bold blue]Agenda del médico con cédula {cedula}:[/bold blue]")
                    for index, cita in citas.iterrows():
                        console.print(
                            f"[cyan]Fecha:[/cyan] {cita['fecha']}, [cyan]Hora:[/cyan] {cita['hora']}, [cyan]Paciente:[/cyan] {cita['paciente']}")
                else:
                    console.print(
                        f"[red]No hay citas agendadas para el médico con cédula {cedula}.[/red]")
            else:
                console.print(
                    f"[red]No se encontró ningún médico con la cédula {cedula}.[/red]")

        elif opcion == "0":
            console.print(
                "[bold red]Saliendo del menú de la agenda...[/bold red]")
            break

        else:
            console.print(
                "[red]Opción inválida, por favor intente nuevamente.[/red]")


def opcion3():
    agenda = Agenda(hospital.datos_de_citas)
    while True:
        console.print(
            "\n[bold blue]--Opciones disponibles para Pacientes--[/bold blue]")
        console.print("1. [green]Agendar una cita[/green]")
        console.print("2. [yellow]Reagendar una cita[/yellow]")
        console.print("3. [red]Cancelar una cita[/red]")
        console.print("4. [cyan]Consultar citas disponibles[/cyan]")
        console.print("0. [red]Salir[/red]")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            paciente = input("Ingrese la cédula del paciente: ")
            if hospital.consultar_paciente(paciente):
                celular = obtener_celular(paciente)
                correo = obtener_correo(paciente)

                console.print("\n[bold blue]Lista de Médicos:[/bold blue]")
                for datos in hospital.datos_de_medicos:
                    console.print(
                        f"[cyan]Cédula:[/cyan] {datos['id']} [cyan]Nombre:[/cyan] {datos['nombre']} [cyan]Especialidad:[/cyan] {datos['especialidad']}")

                while True:
                    console.print(
                        "\n[bold blue]Seleccione médico de la lista:[/bold blue]")
                    medico = input("Ingrese la cédula del médico: ")
                    if hospital.consultar_medico(medico):
                        break
                    console.print(
                        "[red]Médico no encontrado, verifica la cédula.[/red]")

                while True:
                    fecha = obtener_fecha()
                    hora = obtener_hora()

                    if agenda.horario_disponible(medico, fecha, hora):
                        agenda.agendar_cita(fecha, hora, paciente, medico)
                        console.print(
                            "[green]Su cita ha sido agendada.[/green]")

                        notificaciones = Notificaciones(
                            paciente, celular, correo, fecha, hora, "agendar")
                        notificaciones.enviar_notificaciones()
                        break
                    else:
                        console.print(
                            "[red]Fecha y hora no disponibles, seleccione otro horario.[/red]")
                        continue

            else:
                console.print(
                    f"[red]Paciente {paciente} no se encuentra afiliado, o verifique la cédula ingresada.[/red]")

        # Opción 2: Reagendar una cita
        elif opcion == "2":
            paciente = input("Ingrese la cédula del paciente: ")
            if hospital.consultar_paciente(paciente):
                celular = obtener_celular(paciente)
                correo = obtener_correo(paciente)

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

                            # Enviar notificación
                            notificaciones = Notificaciones(
                                paciente, celular, correo, nueva_fecha, nueva_hora, "reagendar")
                            notificaciones.enviar_notificaciones()

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
                celular = obtener_celular(paciente)
                correo = obtener_correo(paciente)

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
                    # Obtener la información de la cita antes de cancelarla
                    cita_actual = citas_paciente.loc[int(indice_cita)]
                    fecha = cita_actual["fecha"]
                    hora = cita_actual["hora"]

                    agenda.cancelar_cita(indice_cita)
                    print(
                        f"La cita con índice {indice_cita} ha sido cancelada.")

                    # Enviar notificación
                    notificaciones = Notificaciones(
                        paciente, celular, correo, fecha, hora, "cancelar")
                    notificaciones.enviar_notificaciones()

                else:
                    print("Índice no encontrado, verifica el valor ingresado.")
            else:
                print(
                    f"Paciente {paciente} no se encuentra afiliado, o verifique cédula ingresada.")

        # Opción 4: Consultar citas disponibles
        elif opcion == "4":  # Consultar citas disponibles
            paciente = input("Ingrese la cédula del paciente: ")
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


def obtener_celular(paciente):
    paciente_data = hospital.consultar_paciente(paciente)
    if paciente_data:
        return paciente_data.get('celular')
    return None


def obtener_correo(paciente):
    paciente_data = hospital.consultar_paciente(paciente)
    if paciente_data:
        return paciente_data.get('correo')
    return None


def obtener_fecha():
    while True:
        fecha = input("Ingresar la fecha (YYYY-MM-DD) [Ejemplo: 2024-10-15]: ")
        try:
            fecha = datetime.strptime(fecha, "%Y-%m-%d")
            return fecha
        except ValueError:
            console.print(
                "[red]Formato de fecha no válido. Por favor, intente de nuevo.[/red]")


def obtener_hora():
    while True:
        hora = input("Ingresar la hora (HH:MM) [Ejemplo: 14:30]: ")
        try:
            hora = datetime.strptime(hora, "%H:%M")
            return hora.time()
        except ValueError:
            console.print(
                "[red]Formato de hora no válido. Por favor, intente de nuevo.[/red]")
