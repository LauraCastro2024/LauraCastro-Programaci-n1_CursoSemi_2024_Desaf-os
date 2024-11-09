#

# Definimos la clase Producto, que representará los productos en la tienda
class Producto:
    def __init__(self, nombre, precio, cantidad):
# Inicializa un producto con nombre, precio y cantidad.
        self.nombre = nombre  # Asigna el nombre del producto
        self.precio = precio  # Asigna el precio del producto
        self.cantidad = cantidad  # Asigna la cantidad disponible del producto

    def __str__(self):
#Devuelve una representación en cadena del producto.
        # Esta función se usa para mostrar información sobre el producto de una forma amigable
        return f"{self.nombre} - Precio: ${self.precio}, Cantidad: {self.cantidad}"

    def actualizar_stock(self, cantidad):
# Actualiza la cantidad del producto en stock.
        # Aquí actualizamos la cantidad del producto, sumando o restando según la cantidad que se pase
        self.cantidad += cantidad


# Definimos la clase Empleado, que representará a los empleados de la tienda
class Empleado:
    def __init__(self, nombre, id_empleado):
# Inicia un empleado con nombre e ID.
        self.nombre = nombre  # Asigna el nombre del empleado
        self.id_empleado = id_empleado  # Asigna un ID único al empleado

    def __str__(self):
# Devuelve una representación en cadena del empleado.
        # Esta función se usa para mostrar información sobre el empleado de una forma amigable
        return f"Empleado: {self.nombre}, ID: {self.id_empleado}"


# Definimos la clase Tienda, que representará una tienda en el inventario
class Tienda:
    def __init__(self, nombre):
# Inicializa una tienda con un nombre, lista de productos y empleados.
        self.nombre = nombre  # Asigna el nombre de la tienda
        self.productos = {}  # Un diccionario para almacenar los productos (clave: nombre, valor: objeto Producto)
        self.empleados = {}  # Un diccionario para almacenar los empleados (clave: ID, valor: objeto Empleado)

    def agregar_producto(self, producto):
# Agrega un producto al inventario de la tienda.
        # Aquí se agrega el producto al diccionario de productos de la tienda
        self.productos[producto.nombre] = producto

    def agregar_empleado(self, empleado):
# Agrega un empleado a la tienda.
        # Aquí se agrega el empleado al diccionario de empleados de la tienda
        self.empleados[empleado.id_empleado] = empleado

    def mostrar_inventario(self):
# Muestra el inventario de la tienda.
        print(f"\nInventario de {self.nombre}:")
        # Recorre todos los productos y los imprime
        for producto in self.productos.values():
            print(producto)

    def mostrar_empleados(self):
# Muestra los empleados de la tienda.
        print(f"\nEmpleados de {self.nombre}:")
        # Recorre todos los empleados y los imprime
        for empleado in self.empleados.values():
            print(empleado)


# Definimos la clase Transaccion, que representará las transacciones realizadas en la tienda
class Transaccion:
    def __init__(self, empleado, productos_vendidos):
# Inicializa una transacción con el empleado que la realiza y los productos 
# vendidos.
        self.empleado = empleado  # Asigna el empleado que realiza la transacción
        self.productos_vendidos = productos_vendidos  # Lista de productos vendidos
        self.total = self.calcular_total()  # Calcula el total de la transacción

    def calcular_total(self):
# Calcula el total de la transacción sumando los precios de los 
# productos vendidos.
        # Aquí sumamos el precio de todos los productos vendidos para obtener el total
        return sum(producto.precio for producto in self.productos_vendidos)

    def __str__(self):
# Devuelve una representación en cadena de la transacción.
        # Esta función muestra una cadena que describe la transacción y el total
        productos_str = ', '.join([producto.nombre for producto in self.productos_vendidos])
        return f"Transacción realizada por {self.empleado.nombre}: {productos_str} - Total: ${self.total}"


# Definimos la clase Inventario, que representará el inventario de todas las tiendas
class Inventario:
    def __init__(self):
# Inicializa el inventario con un diccionario para las tiendas.
        self.tiendas = {}  # Un diccionario para almacenar tiendas (clave: nombre de la tienda, valor: objeto Tienda)

    def agregar_tienda(self, tienda):
# Agrega una tienda al inventario.
        # Aquí se agrega la tienda al diccionario de tiendas
        self.tiendas[tienda.nombre] = tienda

    def mostrar_todas_las_tiendas(self):
# Muestra el inventario y empleados de todas las tiendas.
        # Recorre todas las tiendas y muestra su inventario y empleados
        for tienda in self.tiendas.values():
            tienda.mostrar_inventario()  # Muestra el inventario de la tienda
            tienda.mostrar_empleados()    # Muestra los empleados de la tienda

    def realizar_transaccion(self, nombre_tienda, id_empleado, productos_vendidos):
# Realiza una transacción en la tienda especificada por el empleado.
        tienda = self.tiendas.get(nombre_tienda)  # Busca la tienda por nombre
        empleado = tienda.empleados.get(id_empleado) if tienda else None  # Busca el empleado por ID

        if tienda and empleado:  # Si se encuentra la tienda y el empleado
            transaccion = Transaccion(empleado, productos_vendidos)  # Crea la transacción
            print(transaccion)  # Imprime la transacción
        else:
            print("Tienda o empleado no encontrado.")  # Maneja el caso donde no se encuentra la tienda o empleado


# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()  # Crea un nuevo inventario

    # Crear tiendas
    tienda1 = Tienda("Tienda A")  # Crea una tienda llamada "Tienda A"
    tienda2 = Tienda("Tienda B")  # Crea una tienda llamada "Tienda B"

    # Agregar productos
    producto1 = Producto("Camiseta", 19.99, 50)  # Crea un producto: Camiseta
    producto2 = Producto("Pantalón", 39.99, 30)   # Crea un producto: Pantalón
    tienda1.agregar_producto(producto1)  # Agrega camiseta a Tienda A
    tienda1.agregar_producto(producto2)  # Agrega pantalón a Tienda A

    producto3 = Producto("Zapatos", 49.99, 20)  # Crea un producto: Zapatos
    tienda2.agregar_producto(producto3)  # Agrega zapatos a Tienda B

    # Agregar empleados
    empleado1 = Empleado("Juan", "E001")  # Crea un empleado llamado Juan
    empleado2 = Empleado("Ana", "E002")    # Crea un empleado llamado Ana
    tienda1.agregar_empleado(empleado1)    # Agrega Juan a Tienda A
    tienda2.agregar_empleado(empleado2)    # Agrega Ana a Tienda B

    # Agregar tiendas al inventario
    inventario.agregar_tienda(tienda1)  # Agrega Tienda A al inventario
    inventario.agregar_tienda(tienda2)  # Agrega Tienda B al inventario

    # Mostrar inventario y empleados
    inventario.mostrar_todas_las_tiendas()  # Muestra el inventario y empleados de todas las tiendas

    # Realizar una transacción
    inventario.realizar_transaccion("Tienda A", "E001", [producto1, producto2])  # Realiza una transacción en Tienda A por Juan
