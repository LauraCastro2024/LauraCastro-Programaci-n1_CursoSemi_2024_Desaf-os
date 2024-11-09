# Actualizar la cantidad de libros disponibles en un archivo CSV 
# Tienes un archivo inventario.csv que contiene una lista de libros 
# y el número de copias disponibles. Escribe un programa que permita 
# actualizar la cantidad de copias de un libro específico. 
# El programa debe leer el archivo, modificar el número de copias
# y volver a escribir el archivo.

import csv  # Importamos el módulo csv para poder trabajar con archivos CSV (Comma-Separated Values)

def actualizar_copias(nombre_archivo, titulo_libro, nuevas_copias):
# Inicializamos una lista vacía para almacenar las filas actualizadas del archivo
    filas_actualizadas = []
# Variable para verificar si encontramos el libro
    encontrado = False

# Abrimos el archivo CSV en modo lectura ("r" significa "read")
    with open(nombre_archivo, "r") as archivo_csv:
# Creamos un lector CSV que nos permitirá leer el contenido del archivo
        lector_csv = csv.reader(archivo_csv)
        
# Iteramos sobre cada fila del archivo CSV
        for fila in lector_csv:
            print(fila)  # Línea de depuración para verificar el contenido de la fila actual
            
# La primera columna es el título del libro y la segunda es la cantidad de copias
# Comparamos el título del libro en la fila con el título que buscamos
# Usamos strip() para eliminar espacios en blanco y lower() para hacer la comparación sin importar mayúsculas
            if fila[0].strip().lower() == titulo_libro.lower():
                fila[1] = str(nuevas_copias)  # Actualizamos la cantidad de copias a las nuevas copias proporcionadas
                encontrado = True  # Marcamos que hemos encontrado el libro
            
# Agregamos la fila (actualizada o no) a la lista de filas actualizadas
            filas_actualizadas.append(fila)

# Si encontramos el libro, escribimos los cambios en el archivo
    if encontrado:
# Abrimos el archivo nuevamente, esta vez en modo escritura ("w" significa "write")
        with open(nombre_archivo, "w", newline="") as archivo_csv:
# Creamos un escritor CSV que nos permitirá escribir en el archivo
            escritor_csv = csv.writer(archivo_csv)
# Escribimos todas las filas actualizadas en el archivo CSV
            escritor_csv.writerows(filas_actualizadas)
        
# Imprimimos un mensaje confirmando que la cantidad de copias fue actualizada
        print(f"Cantidad de copias de '{titulo_libro}' actualizada a {nuevas_copias}.")
    else:
# Si no encontramos el libro, imprimimos un mensaje indicando que no se encontró
        print(f"El libro '{titulo_libro}' no se encontró en el inventario.")

# Llamamos a la función con el nombre del archivo, el título del libro y la nueva cantidad de copias
actualizar_copias("inventario.csv", "El alquimista", 5)

