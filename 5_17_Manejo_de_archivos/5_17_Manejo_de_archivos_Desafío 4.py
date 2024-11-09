# Eliminar registros de un archivo de préstamos 
# Escribe un programa que permita eliminar el registro de un préstamo 
# de un archivo prestamos.txt. 
# El programa debe mostrar los registros actuales, 
# permitir al usuario seleccionar cuál eliminar, 
# y luego actualizar el archivo sin el registro eliminado.

def eliminar_prestamo():
    try:
# Abrimos el archivo "prestamos.txt" en modo lectura ("r")
# El 'with' asegura que el archivo se cierre automáticamente después de ser leído
        with open("prestamos.txt", "r") as archivo:
            prestamos = archivo.readlines()  # Leemos todas las líneas del archivo y las guardamos en la lista 'prestamos'
        
# Verificamos si el archivo está vacío, si no tiene registros de préstamos
        if not prestamos:
            print("No hay préstamos registrados.")  # Mensaje si no hay préstamos para eliminar
            return  # Salimos de la función si no hay registros

# Mostramos los préstamos actuales en la consola
        print("Registros de préstamos:")
        for idx, prestamo in enumerate(prestamos):  # Iteramos sobre cada préstamo con su índice
            print(f"{idx + 1}: {prestamo.strip()}")  # Mostramos el índice + 1 y el préstamo (el 'strip()' elimina espacios y saltos de línea)

# Pedimos al usuario que ingrese el número del préstamo que desea eliminar
# Convertimos la entrada a entero con 'int()' y restamos 1 para ajustar el índice
        seleccion = int(input("Seleccione el número del préstamo a eliminar: ")) - 1

# Verificamos si la selección del usuario está dentro del rango de préstamos disponibles
        if 0 <= seleccion < len(prestamos):
            # Si la selección es válida, eliminamos el préstamo de la lista
            prestamos.pop(seleccion)  # 'pop()' elimina el elemento de la lista en la posición indicada

# Ahora abrimos el archivo "prestamos.txt" en modo escritura ("w") para guardar los registros actualizados
            with open("prestamos.txt", "w") as archivo:
                archivo.writelines(prestamos)  # Escribimos de nuevo todas las líneas (sin el préstamo eliminado)

            print("Préstamo eliminado exitosamente.")  # Confirmamos que el préstamo fue eliminado
        else:
            print("Selección inválida.")  # Mensaje si el número ingresado no es válido

# Si el archivo no existe, se lanza una excepción FileNotFoundError
    except FileNotFoundError:
        print("El archivo 'prestamos.txt' no existe.")  # Mensaje si el archivo no se encuentra

# Si ocurre cualquier otro error, lo capturamos y mostramos un mensaje
    except Exception as e:
        print(f"Ocurrió un error: {e}")  # Mostramos el error inesperado que ocurrió

# Llamamos a la función para ejecutar el proceso de eliminación de un préstamo
eliminar_prestamo()
