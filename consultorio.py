class Paciente:
    def __init__(self, nombre, motivo):
        self.nombre = nombre
        self.motivo = motivo
        self.citas = []  # Lista para almacenar las fechas de las citas

    def agregar_cita(self, fecha):
        self.citas.append(fecha)

    def tiene_citas_previas(self):
        return len(self.citas) > 0


class Secretaria:
    def __init__(self):
        self.pacientes = {}  # Diccionario para almacenar pacientes por su nombre

    def registrar_paciente(self, nombre, motivo):
        if nombre in self.pacientes and self.pacientes[nombre].tiene_citas_previas():
            print(f"El paciente {nombre} ya tiene una consulta previa, pase a la sala de espera.")
        else:
            paciente = Paciente(nombre, motivo)
            self.pacientes[nombre] = paciente
            print(f"Paciente {nombre} registrado con motivo: {motivo}")

    def asignar_cita(self, nombre, fecha):
        if nombre in self.pacientes:
            self.pacientes[nombre].agregar_cita(fecha)
            print(f"Cita asignada para {nombre} el {fecha}.")
        else:
            print(f"El paciente {nombre} no está registrado.")


class Doctor:
    def __init__(self, nombre):
        self.nombre = nombre


# Ejemplo de uso
secretaria = Secretaria()

# Registrar pacientes
secretaria.registrar_paciente("Juan Perez", "Dolor de cabeza")
secretaria.registrar_paciente("Ana Lopez", "Dolor de espalda")

# Asignar citas
secretaria.asignar_cita("Juan Perez", "2024-09-01")
secretaria.asignar_cita("Ana Lopez", "2024-09-02")

# Intentar registrar un paciente con una cita previa
secretaria.registrar_paciente("Juan Perez", "Chequeo general")
