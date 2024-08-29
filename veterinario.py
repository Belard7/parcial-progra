class Animal:
    def __init__(self, nombre, especie, edad, caracteristicas, area):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.caracteristicas = caracteristicas
        self.area = area
        self.tratamientos = []  # Lista de tratamientos asignados al animal

    def asignar_tratamiento(self, tratamiento):
        self.tratamientos.append(tratamiento)

    def mostrar_tratamientos(self):
        if not self.tratamientos:
            print(f"{self.nombre} ({self.especie}) no tiene tratamientos asignados.")
        else:
            print(f"Tratamientos de {self.nombre} ({self.especie}):")
            for t in self.tratamientos:
                print(f"- {t.nombre}: {t.dosis} cada {t.frecuencia} horas.")


class Tratamiento:
    def __init__(self, nombre, dosis, frecuencia):
        self.nombre = nombre
        self.dosis = dosis
        self.frecuencia = frecuencia  # Frecuencia en horas


class Zoologico:
    def __init__(self):
        self.animales = []  # Lista de todos los animales en el zoológico

    def agregar_animal(self, nombre, especie, edad, caracteristicas, area):
        animal = Animal(nombre, especie, edad, caracteristicas, area)
        self.animales.append(animal)
        print(f"Animal agregado: {nombre}, Especie: {especie}, Área: {area}.")

    def listar_animales(self):
        print("\n--- Lista de Animales en el Zoológico ---")
        for animal in self.animales:
            print(f"{animal.nombre} ({animal.especie}), Edad: {animal.edad}, Área: {animal.area}")

    def listar_animales_en_tratamiento(self):
        print("\n--- Animales en Tratamiento ---")
        en_tratamiento = [animal for animal in self.animales if animal.tratamientos]
        if not en_tratamiento:
            print("No hay animales en tratamiento.")
        else:
            for animal in en_tratamiento:
                animal.mostrar_tratamientos()

    def asignar_tratamiento_a_animal(self, nombre_animal, nombre_tratamiento, dosis, frecuencia):
        animal = next((a for a in self.animales if a.nombre == nombre_animal), None)
        if animal:
            tratamiento = Tratamiento(nombre_tratamiento, dosis, frecuencia)
            animal.asignar_tratamiento(tratamiento)
            print(f"Tratamiento {nombre_tratamiento} asignado a {nombre_animal}.")
        else:
            print(f"Animal {nombre_animal} no encontrado.")


# Ejemplo de uso interactivo
zoologico = Zoologico()

while True:
    print("\n--- Menú de opciones ---")
    print("1. Agregar animal")
    print("2. Listar todos los animales")
    print("3. Asignar tratamiento a un animal")
    print("4. Listar animales en tratamiento")
    print("5. Salir")
    opcion = input("Seleccione una opción (1, 2, 3, 4, 5): ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del animal: ")
        especie = input("Ingrese la especie del animal: ")
        edad = int(input("Ingrese la edad del animal: "))
        caracteristicas = input("Ingrese las características del animal: ")
        area = input("Ingrese el área del zoológico donde se encuentra: ")
        zoologico.agregar_animal(nombre, especie, edad, caracteristicas, area)

    elif opcion == "2":
        zoologico.listar_animales()

    elif opcion == "3":
        nombre_animal = input("Ingrese el nombre del animal: ")
        nombre_tratamiento = input("Ingrese el nombre del tratamiento: ")
        dosis = input("Ingrese la dosis del tratamiento: ")
        frecuencia = int(input("Ingrese la frecuencia del tratamiento (en horas): "))
        zoologico.asignar_tratamiento_a_animal(nombre_animal, nombre_tratamiento, dosis, frecuencia)

    elif opcion == "4":
        zoologico.listar_animales_en_tratamiento()

    elif opcion == "5":
        print("Saliendo del sistema.")
        break

    else:
        print("Opción no válida. Intente de nuevo.")
