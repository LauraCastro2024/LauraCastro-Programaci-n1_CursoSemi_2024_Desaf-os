# Utiliza el módulo collections para analizar un texto y 
# generar estadísticas avanzadas, como las 10 palabras más 
# comunes y su frecuencia. Extiende esto creando un gráfico de 
# barras con matplotlib para visualizar la frecuencia de las palabras.

# Importamos la clase Counter del módulo collections, que nos ayudará a contar elementos fácilmente.
from collections import Counter

# Importamos matplotlib.pyplot como plt, que nos permite hacer gráficos en Python.
import matplotlib.pyplot as plt

# Texto de ejemplo que queremos analizar para contar la frecuencia de cada palabra.
texto = "Programacion en Python es genial y Programación es fácil de aprender. Aprender Programación es genial y Python es sencillo de aprender."

# Convertimos el texto a minúsculas y lo dividimos en palabras usando .split() para contar cada palabra.
# .lower() hace que todo el texto esté en minúsculas para evitar diferencias entre "Programación" y "programación".
palabras = texto.lower().split()

# Usamos Counter para contar la frecuencia de cada palabra en la lista 'palabras'.
contador = Counter(palabras)

# Obtenemos las 10 palabras más comunes junto con sus frecuencias usando .most_common(10).
# Esto nos devuelve una lista de tuplas (palabra, frecuencia).
mas_comunes = contador.most_common(10)

# Separamos las palabras y sus frecuencias en dos listas distintas.
# zip(*mas_comunes) nos ayuda a dividir la lista de tuplas en dos listas: una para palabras y otra para frecuencias.
palabras, frecuencias = zip(*mas_comunes)

# Creamos un gráfico de barras para mostrar la frecuencia de las palabras más comunes.
# plt.bar() toma las palabras como etiquetas en el eje x y las frecuencias en el eje y.
plt.bar(palabras, frecuencias)

# Etiquetamos el eje x del gráfico con "Palabras".
plt.xlabel("Palabras")

# Etiquetamos el eje y del gráfico con "Frecuencia".
plt.ylabel("Frecuencia")

# Asignamos un título al gráfico.
plt.title("Frecuencia de las palabras más comunes")

# Mostramos el gráfico en la pantalla.
plt.show()
