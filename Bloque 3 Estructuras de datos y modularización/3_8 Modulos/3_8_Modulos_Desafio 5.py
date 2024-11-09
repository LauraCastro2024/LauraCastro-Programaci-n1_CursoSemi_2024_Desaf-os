# Utiliza el módulo os para interactuar con el sistema operativo 
# y añade características como guardar un archivo o leer un archivo 
# existente en nuestro procesador de texto.

# Importamos el módulo os, que nos proporciona funciones para interactuar con el sistema operativo.
import os

# Definimos el texto que queremos guardar en un archivo.
texto = "Este es un texto para programación."

# Usamos 'with open' para abrir el archivo en modo escritura ('w').
# Si el archivo no existe, Python lo creará automáticamente.
# El 'with' garantiza que el archivo se cierre correctamente después de usarlo.
with open("archivo_texto.txt", "w") as archivo:
    # Escribimos el contenido de la variable 'texto' en el archivo.
    archivo.write(texto)

# Verificamos si el archivo 'archivo_texto.txt' existe en el sistema.
if os.path.exists("archivo_texto.txt"):
    # Si el archivo existe, lo abrimos en modo lectura ('r').
    with open("archivo_texto.txt", "r") as archivo:
        # Leemos el contenido del archivo y lo guardamos en la variable 'contenido'.
        contenido = archivo.read()
        # Imprimimos el contenido del archivo.
        print("Contenido del archivo:", contenido)
else:
    # Si el archivo no existe, mostramos un mensaje indicando esto.
    print("El archivo no existe.")
