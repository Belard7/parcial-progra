class Producto:
    def __init__(self, nombre, cantidad, precio_venta):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio_venta = precio_venta

    def actualizar_cantidad(self, cantidad):
        self.cantidad += cantidad

    def actualizar_precio(self, precio_venta):
        self.precio_venta = precio_venta


class Tienda:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar los productos por nombre

    def agregar_producto(self, nombre, cantidad, precio_venta):
        if nombre in self.productos:
            self.productos[nombre].actualizar_cantidad(cantidad)
            self.productos[nombre].actualizar_precio(precio_venta)
            print(f"Producto actualizado: {nombre}, nueva cantidad: {self.productos[nombre].cantidad}, nuevo precio de venta: {self.productos[nombre].precio_venta}")
        else:
            self.productos[nombre] = Producto(nombre, cantidad, precio_venta)
            print(f"Producto agregado: {nombre}, cantidad: {cantidad}, precio de venta: {precio_venta}")

    def registrar_venta(self, nombre, cantidad_comprada, pago_cliente):
        if nombre in self.productos and self.productos[nombre].cantidad >= cantidad_comprada:
            producto = self.productos[nombre]
            total = producto.precio_venta * cantidad_comprada
            if pago_cliente < total:
                print(f"El pago es insuficiente. Total: {total}, Pago recibido: {pago_cliente}")
                return
            
            producto.actualizar_cantidad(-cantidad_comprada)
            cambio = pago_cliente - total
            print(f"Venta registrada: {cantidad_comprada} x {producto.nombre} a {producto.precio_venta} cada uno. Total: {total}. Cambio: {cambio}.")
        else:
            print("Producto no disponible o cantidad insuficiente.")

    def recibir_proveedor(self, nombre, cantidad, precio_sugerido):
        # Agregar o actualizar el producto con el precio sugerido por el proveedor
        self.agregar_producto(nombre, cantidad, precio_sugerido)
        print(f"Proveedor recibido: {cantidad} de {nombre} con precio sugerido de venta: {precio_sugerido}.")


# Ejemplo de uso interactivo
tienda = Tienda()

while True:
    print("\n--- Menú de opciones ---")
    print("1. Agregar producto o actualizar inventario")
    print("2. Registrar venta")
    print("3. Recibir proveedor")
    print("4. Salir")
    opcion = input("Seleccione una opción (1, 2, 3, 4): ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio_venta = float(input("Ingrese el precio de venta: "))
        tienda.agregar_producto(nombre, cantidad, precio_venta)

    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto vendido: ")
        cantidad_comprada = int(input("Ingrese la cantidad comprada: "))
        pago_cliente = float(input("Ingrese el pago del cliente: "))
        tienda.registrar_venta(nombre, cantidad_comprada, pago_cliente)

    elif opcion == "3":
        nombre = input("Ingrese el nombre del producto recibido: ")
        cantidad = int(input("Ingrese la cantidad recibida: "))
        precio_sugerido = float(input("Ingrese el precio sugerido de venta: "))
        tienda.recibir_proveedor(nombre, cantidad, precio_sugerido)

    elif opcion == "4":
        print("Saliendo del sistema.")
        break

    else:
        print("Opción no válida. Intente de nuevo.")
