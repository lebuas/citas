# Asegúrate de que estés utilizando rich para el prompt
from rich.prompt import Prompt
from datetime import datetime
from rich import print
from rich.panel import Panel
from rich.table import Table
from hospital import Hospital
from agenda import Agenda
from notificacion import Notificaciones

# Inicializar el hospital
hospital = Hospital()


def obtener_fecha():
    while True:
        fecha_input = Prompt.ask("Ingrese la fecha (DD/MM/AAAA)")
        try:
            # Convierte la entrada a un objeto datetime
            fecha = datetime.strptime(fecha_input, "%d/%m/%Y")
            return fecha  # Retorna el objeto datetime directamente
        except ValueError:
            print(
                "[red]Error: La fecha ingresada no es válida. Asegúrese de usar el formato DD/MM/AAAA.[/red]")


def obtener_hora():
    while True:
        hora_input = Prompt.ask("Ingrese la hora (HH:MM:SS)")
        try:
            # Convierte la entrada a un objeto time
            hora = datetime.strptime(hora_input, "%H:%M:%S").time()
            return hora  # Retorna el objeto time directamente
        except ValueError:
            print(
                "[red]Error: La hora ingresada no es válida. Asegúrese de usar el formato HH:MM:SS.[/red]")


def obtener_celular(cedula):
    paciente = hospital.consultar_paciente(cedula)
    return paciente["celular"] if paciente else None


def obtener_correo(cedula):
    paciente = hospital.consultar_paciente(cedula)
    return paciente["correo"] if paciente else None


def opcion1():
    while True:
        print(Panel("Opciones disponibles en el Hospital", title="Menú Principal"))
        print("[1] Agregar un Médico")
        print("[2] Agregar un Paciente")
        print("[3] Consultar Médico")
        print("[4] Consultar Paciente")
        print("[0] Salir")

        opcion = Prompt.ask("Seleccione una opción", choices=[
                            "1", "2", "3", "4", "0"])

        if opcion == "1":
            # Agregar Médico
            while True:
                cedula = Prompt.ask("Ingrese la cédula del médico")
                if cedula.isdigit():
                    break
                else:
                    print("[red]Error: La cédula debe contener solo números.[/red]")

            if hospital.consultar_medico(cedula):
                print(
                    f"[red]Error: Ya existe un médico con la cédula {cedula}.[/red]")
            else:
                nombre = Prompt.ask("Ingrese el nombre del médico")
                correo = Prompt.ask("Ingrese el correo del médico")
                especialidad = Prompt.ask("Ingrese la especialidad del médico")
                hospital.agregar_medico(cedula, nombre, correo, especialidad)
                print(f"[green]Médico {nombre} agregado exitosamente.[/green]")

        elif opcion == "2":
            # Agregar Paciente
            while True:
                cedula = Prompt.ask("Ingrese la cédula del paciente")
                if cedula.isdigit():
                    break
                else:
                    print("[red]Error: La cédula debe contener solo números.[/red]")

            nombre = Prompt.ask("Ingrese el nombre del paciente")
            celular = Prompt.ask("Ingrese el celular del paciente")
            correo = Prompt.ask("Ingrese el correo del paciente")
            hospital.agregar_paciente(cedula, nombre, celular, correo)
            print(f"[green]Paciente {nombre} agregado exitosamente.[/green]")

        elif opcion == "3":
            # Consultar Médico
            while True:
                cedula = Prompt.ask(
                    "Ingrese la cédula del médico que desea consultar")
                if cedula.isdigit():
                    break
                else:
                    print("[red]Error: La cédula debe contener solo números.[/red]")

            medico = hospital.consultar_medico(cedula)
            if medico:
                table = Table(title="Información del Médico",
                              title_justify="left")
                table.add_column("Campo", justify="left")
                table.add_column("Valor", justify="left")
                for key, value in medico.items():
                    table.add_row(key.capitalize(), str(value))
                print(table)
            else:
                print(
                    f"[red]No se encontró ningún médico con la cédula {cedula}.[/red]")

        elif opcion == "4":
            # Consultar Paciente
            while True:
                cedula = Prompt.ask(
                    "Ingrese la cédula del paciente que desea consultar")
                if cedula.isdigit():
                    break
                else:
                    print("[red]Error: La cédula debe contener solo números.[/red]")

            paciente = hospital.consultar_paciente(cedula)
            if paciente:
                table = Table(title="Información del Paciente",
                              title_justify="left")
                table.add_column("Campo", justify="left")
                table.add_column("Valor", justify="left")
                for key, value in paciente.items():
                    table.add_row(key.capitalize(), str(value))
                print(table)
            else:
                print(
                    f"[red]No se encontró ningún paciente con la cédula {cedula}.[/red]")

        elif opcion == "0":
            print("[yellow]Saliendo del menú del hospital...[/yellow]")
            break

        else:
            print("[red]Opción inválida, por favor intente nuevamente.[/red]")


def opcion2():
    while True:
        print(Panel("Opciones disponibles para Médicos", title="Menú Médico"))
        print("[1] Consulta Agenda")
        print("[0] Salir")

        opcion = Prompt.ask("Seleccione una opción", choices=["1", "0"])

        if opcion == "1":
            cedula = Prompt.ask("Ingrese la cédula del médico")

            if not cedula.isdigit() or len(cedula) > 10 or len(cedula) < 6:
                print("[red]Ingrese una cédula válida entre 6 a 10 dígitos.[/red]")
                continue

            medico = hospital.consultar_medico(cedula)
            if medico:
                agenda = Agenda(hospital.datos_de_citas)
                citas = agenda.consultar_agenda_medico(cedula)

                if not citas.empty:
                    print(
                        f"[green]Agenda del médico con cédula {cedula}:[/green]")
                    for index, cita in citas.iterrows():
                        print(
                            f"[cyan]Fecha:[/cyan] {cita['fecha']}, [cyan]Hora:[/cyan] {cita['hora']}, [cyan]Paciente:[/cyan] {cita['paciente']}")
                else:
                    print(
                        f"[yellow]No hay citas agendadas para el médico con cédula {cedula}.[/yellow]")
            else:
                print(
                    f"[red]No se encontró ningún médico con la cédula {cedula}.[/red]")

        elif opcion == "0":
            print("[yellow]Saliendo del menú de la agenda...[/yellow]")
            break

        else:
            print("[red]Opción inválida, por favor intente nuevamente.[/red]")


def opcion3():
    while True:
        hospital = Hospital()
        agenda = Agenda(hospital.datos_de_citas)

        print(Panel("Opciones disponibles para Pacientes", title="Menú Paciente"))
        print("[1] Agendar una cita")
        print("[2] Reagendar una cita")
        print("[3] Cancelar una cita")
        print("[4] Consultar citas disponibles")
        print("[0] Salir")
        opcion = Prompt.ask("Seleccione una opción", choices=[
                            "1", "2", "3", "4", "0"])
        # Agendar una cita
        if opcion == "1":
            paciente = Prompt.ask("Ingrese la cédula del paciente")
            if hospital.consultar_paciente(paciente):
                celular = obtener_celular(paciente)
                correo = obtener_correo(paciente)

                print("\n[cyan]Médicos disponibles:[/cyan]")
                for datos in hospital.datos_de_medicos:
                    print(
                        f"Cédula: {datos['id']} | Nombre: {datos['nombre']} | Especialidad: {datos['especialidad']}")

                # Seleccionar médico
                while True:
                    medico = Prompt.ask("Ingrese la cédula del médico")
                    if hospital.consultar_medico(medico):
                        break
                    print("[red]Médico no encontrado, verifica la cédula.[/red]")

                # Seleccionar fecha y hora
                while True:
                    fecha = obtener_fecha()
                    hora = obtener_hora()

                    if agenda.horario_disponible(medico, fecha, hora):
                        agenda.agendar_cita(fecha, hora, paciente, medico)
                        print("[green]Su cita ha sido agendada.[/green]")

                        # Enviar notificación
                        notificaciones = Notificaciones(
                            paciente, celular, correo, fecha, hora, "agendar")
                        notificaciones.enviar_notificaciones()

                        break
                    else:
                        print(
                            "[red]Fecha y hora no disponibles, seleccione otro horario.[/red]")
                        continue

            else:
                print(
                    f"[red]Paciente {paciente} no se encuentra afiliado, o verifique cédula ingresada.[/red]")

        elif opcion == "2":
            # Reagendar cita
            paciente = Prompt.ask("Ingrese la cédula del paciente")
            if hospital.consultar_paciente(paciente):
                celular = obtener_celular(paciente)
                correo = obtener_correo(paciente)

                citas_paciente = agenda.consultar_citas_paciente(paciente)
                if citas_paciente.empty:
                    print(
                        f"[red]El paciente {paciente} no tiene citas agendadas.[/red]")
                    continue

                # Mostrar citas actuales del paciente con sus índices
                print(
                    "[cyan]Citas actuales del paciente (índice - fecha - hora - médico):[/cyan]")
                print(citas_paciente.reset_index()[
                    ['index', 'fecha', 'hora', 'medico']])

                # Solicitar el índice de la cita a reagendar
                indice_cita = Prompt.ask(
                    "Ingrese el índice de la cita a reagendar")

                # Verificar si el índice es válido
                if int(indice_cita) in citas_paciente.index:
                    cita_actual = citas_paciente.loc[int(indice_cita)]
                    medico_actual = cita_actual["medico"]
                    while True:
                        nueva_fecha_input = Prompt.ask(
                            "[yellow]Ingrese la nueva fecha (DD/MM/AAAA)[/yellow]")
                        nueva_hora_input = Prompt.ask(
                            "[yellow]Ingrese la nueva hora (HH:MM:SS)[/yellow]")

                        # Convertir la nueva fecha y hora a los tipos correctos
                        try:
                            nueva_fecha = datetime.strptime(
                                nueva_fecha_input, "%d/%m/%Y")  # Convertir a datetime
                            nueva_hora = datetime.strptime(
                                nueva_hora_input, "%H:%M:%S").time()  # Convertir a time
                        except ValueError:
                            print(
                                "[red]Error: Fecha o hora ingresadas no son válidas. Asegúrese de usar el formato correcto.[/red]")
                            continue  # Volver a solicitar

                        # Comprobar disponibilidad
                        if agenda.horario_disponible(medico_actual, nueva_fecha, nueva_hora):
                            agenda.cancelar_cita(indice_cita)
                            agenda.reagendar_cita(
                                nueva_fecha, nueva_hora, paciente, medico_actual)
                            print("[green]Su cita ha sido reagendada.[/green]")

                            # Enviar notificación
                            notificaciones = Notificaciones(paciente, celular, correo, nueva_fecha.strftime(
                                "%Y-%m-%d"), nueva_hora.strftime("%H:%M:%S"), "reagendar")
                            notificaciones.enviar_notificaciones()

                            break
                        else:
                            print(
                                "[red]Fecha y hora no disponibles, seleccione otro horario.[/red]")
                            continue
                else:
                    print(
                        "[red]Índice inválido, verifique la cita seleccionada.[/red]")

            else:
                print(
                    f"[red]Paciente {paciente} no se encuentra afiliado, o verifique cédula ingresada.[/red]")

        elif opcion == "3":
            paciente = Prompt.ask("Ingrese la cédula del paciente")
            if hospital.consultar_paciente(paciente):
                celular = obtener_celular(paciente)
                correo = obtener_correo(paciente)

                citas_paciente = agenda.consultar_citas_paciente(paciente)
                if citas_paciente.empty:
                    print(
                        f"[red]El paciente {paciente} no tiene citas agendadas.[/red]")
                    continue

                # Mostrar citas actuales del paciente con sus índices
                print(
                    "[cyan]Citas actuales del paciente (índice - fecha - hora - médico):[/cyan]")
                print(citas_paciente.reset_index()[
                      ['index', 'fecha', 'hora', 'medico']])

                # Solicitar el índice de la cita a cancelar
                indice_cita = Prompt.ask(
                    "Ingrese el índice de la cita a cancelar")

                # Verificar si el índice es válido
                if int(indice_cita) in citas_paciente.index:
                    agenda.cancelar_cita(indice_cita)
                    print("[green]Su cita ha sido cancelada.[/green]")

                    # Enviar notificación
                    notificaciones = Notificaciones(paciente, celular, correo, citas_paciente.loc[int(indice_cita)]["fecha"],
                                                    citas_paciente.loc[int(indice_cita)]["hora"], "cancelar")
                    notificaciones.enviar_notificaciones()
                else:
                    print(
                        "[red]Índice inválido, verifique la cita seleccionada.[/red]")

            else:
                print(
                    f"[red]Paciente {paciente} no se encuentra afiliado, o verifique cédula ingresada.[/red]")

        # Opción 4: Consultar citas disponibles
        elif opcion == "4":  # Consultar citas disponibles
            paciente = Prompt.ask("Ingrese la cédula del paciente: ")
            if hospital.consultar_paciente(paciente):
                citas_paciente = agenda.consultar_citas_paciente(paciente)
                if citas_paciente.empty:
                    print(f"El paciente {paciente} no tiene citas agendadas.")
                else:
                    print("Citas actuales del paciente:")
                    print(citas_paciente[['fecha', 'hora', 'medico']])
            else:
                print(
                    f"Paciente {paciente} no se encuentra afiliado, o verifique cédula ingresada.")

        elif opcion == "0":
            print("[yellow]Saliendo del menú de pacientes...[/yellow]")
            break

        else:
            print("[red]Opción inválida, por favor intente nuevamente.[/red]")


def menu():
    while True:
        print(Panel("Bienvenido al Sistema del Hospital", title="Menú Principal"))
        print("[1] Opción de Administrador")
        print("[2] Opción de Médico")
        print("[3] Opción de Paciente")
        print("[0] Salir")

        opcion = Prompt.ask("Seleccione una opción",
                            choices=["1", "2", "3", "0"])

        if opcion == "1":
            opcion1()
        elif opcion == "2":
            opcion2()
        elif opcion == "3":
            opcion3()
        elif opcion == "0":
            print("[yellow]Saliendo del sistema...[/yellow]")
            break
        else:
            print("[red]Opción inválida, por favor intente nuevamente.[/red]")


if __name__ == "__main__":
    menu()
