# Desarrolla un programa que abra un archivo de texto, 
# lea su contenido y lo muestre. 
# Implementa manejo de excepciones para archivos que no existan 
# y usa finally para asegurarte de que el archivo 
# se cierre adecuadamente en cualquier caso.

try:
    # Abre el archivo en modo lectura
    archivo = open("5_14_Excepciones.txt", "r")
    
    # Lee el contenido del archivo
    contenido = archivo.read()
    print(contenido)

# Imprime el error si el archivo no existe
except FileNotFoundError:
    print("Error: El archivo no existe.")

# El archivo se cierra si fue abierto
finally:
    try:
        archivo.close()
    except NameError:
        # Si el archivo no se abrió, no se intenta cerrarlo
        print("El archivo no se abrió, por lo cual no es necesario cerrarlo.")