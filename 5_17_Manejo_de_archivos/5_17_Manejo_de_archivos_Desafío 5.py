#Contar las palabras más comunes en un archivo de texto 
# Desarrolla una función que lea un archivo de texto grande, 
# como libros.txt, y cuente cuántas veces aparece cada palabra. 
# Luego, muestra las 5 palabras más comunes y cuántas veces aparecen.

# Importamos el módulo Counter de la librería collections para contar las ocurrencias de elementos en una lista.
from collections import Counter  

# Importamos re, que es la librería de expresiones regulares que nos permite buscar patrones en cadenas de texto.
import re  

# Definimos una función que toma el nombre de un archivo como parámetro y cuenta las palabras más comunes en ese archivo.
def contar_palabras_comunes(nombre_archivo):
    
# Iniciamos un contador vacío usando Counter, que nos ayudará a contar las palabras que encontremos en el archivo.
    contador = Counter()

# Abrimos el archivo en modo lectura (r). Usamos with para asegurarnos de que el archivo se cierre automáticamente después de usarlo.
    with open(nombre_archivo, "r") as archivo:
        
# Leemos cada línea del archivo una por una dentro de un bucle for.
        for linea in archivo:
            
# Usamos re.findall() para encontrar todas las palabras en la línea.
# La expresión regular '\b\w+\b' busca cualquier palabra que esté formada por letras y números.
# linea.lower() convierte la línea a minúsculas para que las palabras sean contadas sin importar si son mayúsculas o minúsculas.
            palabras = re.findall(r'\b\w+\b', linea.lower())  
            
# Actualizamos el contador con las palabras encontradas en esta línea.
# update() agrega las palabras encontradas al contador y actualiza las cantidades.
            contador.update(palabras)  

# Usamos el método most_common(5) para obtener las 5 palabras más comunes y sus cantidades.
    palabras_comunes = contador.most_common(5)
    
# Mostramos los resultados, es decir, las 5 palabras más comunes y cuántas veces aparecen en el archivo.
    print("Las 5 palabras más comunes son:")
    
# Iteramos sobre las palabras y sus cantidades, y las mostramos en consola.
    for palabra, cantidad in palabras_comunes:
        print(f"{palabra}: {cantidad} veces")

# Llamamos a la función contar_palabras_comunes pasando el nombre del archivo 'libros.txt' como argumento.
contar_palabras_comunes("libros.txt")
