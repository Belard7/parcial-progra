from datetime import datetime, timedelta

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True  # Estado del libro, si está disponible o prestado

    def marcar_como_prestado(self):
        self.disponible = False

    def marcar_como_disponible(self):
        self.disponible = True


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.sanciones = 0  # Número de sanciones acumuladas


class Prestamo:
    def __init__(self, libro, usuario, dias_prestamo=7):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=dias_prestamo)
        libro.marcar_como_prestado()

    def devolver_libro(self):
        fecha_actual = datetime.now()
        if fecha_actual > self.fecha_devolucion:
            self.usuario.sanciones += 1
            print(f"Devolución tardía. El usuario {self.usuario.nombre} ha sido sancionado. Total de sanciones: {self.usuario.sanciones}.")
        else:
            print(f"Libro devuelto a tiempo por {self.usuario.nombre}.")
        self.libro.marcar_como_disponible()


class Biblioteca:
    def __init__(self):
        self.libros = []  # Lista de libros en la biblioteca
        self.usuarios = []  # Lista de usuarios registrados
        self.prestamos = []  # Lista de préstamos activos

    def agregar_libro(self, titulo, autor):
        libro = Libro(titulo, autor)
        self.libros.append(libro)
        print(f"Libro '{titulo}' de {autor} agregado a la biblioteca.")

    def registrar_usuario(self, nombre):
        usuario = Usuario(nombre)
        self.usuarios.append(usuario)
        print(f"Usuario {nombre} registrado en la biblioteca.")

    def realizar_prestamo(self, nombre_usuario, titulo_libro):
        usuario = next((u for u in self.usuarios if u.nombre == nombre_usuario), None)
        libro = next((l for l in self.libros if l.titulo == titulo_libro and l.disponible), None)

        if usuario and libro:
            prestamo = Prestamo(libro, usuario)
            self.prestamos.append(prestamo)
            print(f"Préstamo realizado: '{libro.titulo}' para {usuario.nombre}. Fecha de devolución: {prestamo.fecha_devolucion.date()}.")
        else:
            print("No se pudo realizar el préstamo. Verifique si el usuario está registrado y si el libro está disponible.")

    def devolver_libro(self, nombre_usuario, titulo_libro):
        prestamo = next((p for p in self.prestamos if p.usuario.nombre == nombre_usuario and p.libro.titulo == titulo_libro), None)

        if prestamo:
            prestamo.devolver_libro()
            self.prestamos.remove(prestamo)
        else:
            print("Préstamo no encontrado. Verifique los datos del usuario y el libro.")


# Ejemplo de uso
biblioteca = Biblioteca()

# Agregar libros a la biblioteca
biblioteca.agregar_libro("Cien Años de Soledad", "Gabriel García Márquez")
biblioteca.agregar_libro("El Principito", "Antoine de Saint-Exupéry")

# Registrar usuarios
biblioteca.registrar_usuario("Juan Perez")
biblioteca.registrar_usuario("Ana Lopez")

# Realizar préstamos
biblioteca.realizar_prestamo("Juan Perez", "Cien Años de Soledad")
biblioteca.realizar_prestamo("Ana Lopez", "El Principito")

# Devolver libros (modificar la fecha del sistema para probar sanciones)
biblioteca.devolver_libro("Juan Perez", "Cien Años de Soledad")
biblioteca.devolver_libro("Ana Lopez", "El Principito")
