# Crear un archivo de préstamos de libros 
# Desarrolla un programa que cree un archivo prestamos.txt y 
# permita al usuario agregar el registro de un préstamo. 
# El registro debe incluir el nombre del libro, 
# el nombre del prestatario y la fecha del préstamo. 
# Asegúrate de no sobrescribir el archivo cada vez que se agrega 
# un nuevo préstamo.

# Definimos una función llamada agregar_prestamo, que será responsable de agregar un préstamo al archivo de texto
def agregar_prestamo():
    # Solicitamos al usuario que ingrese los detalles del préstamo, como el nombre del libro,
    # el nombre del usuario y la fecha del préstamo
    libro = input("Ingrese el nombre del libro: ")  # Pide el nombre del libro que se va a prestar
    usuario = input("Ingrese el nombre del usuario: ")  # Pide el nombre de la persona que toma el libro
    fecha = input("Ingrese la fecha del préstamo (DD/MM/AAAA): ")  # Pide la fecha del préstamo en formato DD/MM/AAAA

    # Abrimos un archivo de texto llamado "prestamos.txt" en modo "a" (agregar),
    # lo que significa que no sobrescribiremos el archivo, sino que añadiremos nueva información al final
    with open("prestamos.txt", "a") as archivo:
        # Escribimos la información del préstamo en el archivo.
        # Utilizamos f-string para formar una cadena de texto con los detalles del préstamo.
        # La línea tiene el formato "libro;prestatario;fecha" y terminamos con un salto de línea (\n)
        archivo.write(f"{libro};{usuario};{fecha}\n")
    
    # Mostramos un mensaje para confirmar que el préstamo fue agregado correctamente
    print("Préstamo agregado exitosamente.")

# Llamamos a la función para ejecutar el proceso de agregar un préstamo
agregar_prestamo()