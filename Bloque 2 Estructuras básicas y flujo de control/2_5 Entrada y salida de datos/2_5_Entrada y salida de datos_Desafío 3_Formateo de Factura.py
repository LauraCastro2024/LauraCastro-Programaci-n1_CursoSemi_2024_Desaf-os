# Definir la función que crea la factura
def crear_factura(productos):

  # Cabecera de la factura
  print("\n" + "=" * 40)  # Línea para separar la factura
  print("{:^40}".format("FACTURA"))  # Título centrado con el texto "FACTURA"
  print("=" * 40)  # Línea
  print("{:<20} {:>5} {:>7} {:>7}".format("Producto", "Cant.", "Precio", "Total"))  # Cabecera de la tabla con columnas para el producto, cantidad, precio y total
  print("-" * 40)  # Línea decorativa para separar la cabecera del contenido

  # Inicializamos la variable que acumulará el total de la factura
  total_general = 0

  # Bucle para recorrer la lista de productos y generar el cuerpo de la factura
  for producto in productos:
      nombre = producto['nombre']  # Obtener el nombre del producto
      cantidad = producto['cantidad']  # Obtener la cantidad del producto
      precio = producto['precio']  # Obtener el precio del producto
      total = cantidad * precio  # Calcular el total (cantidad * precio)
      total_general += total  # Acumular el total de cada producto al total general

      # Mostrar los datos de cada producto en formato de tabla
      print("{:<20} {:>5} ${:>6.2f} ${:>6.2f}".format(nombre[:20], cantidad, precio, total))

  # Pie de la factura
  print("-" * 40)  # Línea para separar el contenido del pie
  print("{:>32} ${:>6.2f}".format("Total General:", total_general))  # Mostrar el total general de la factura
  print("=" * 40)  # Línea para cerrar la factura

# Lista para almacenar los productos ingresados por el usuario
productos = []

# Bucle para ingresar productos
while True:
  # Pedimos al usuario el nombre del producto
  nombre = input("Ingrese el nombre del producto (o presione Enter para terminar): ")

  # Si el usuario presiona Enter sin ingresar un nombre, se termina el bucle
  if nombre == "":
      break

  # Pedimos al usuario la cantidad del producto
  cantidad = int(input("Ingrese la cantidad: "))

  # Pedimos al usuario el precio unitario del producto
  precio = float(input("Ingrese el precio unitario: "))

  # Agregamos el producto como un diccionario a la lista de productos
  productos.append({
      'nombre': nombre,
      'cantidad': cantidad,
      'precio': precio
  })

# Llamamos a la función para crear y mostrar la factura con los productos ingresados
crear_factura(productos)