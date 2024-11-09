# Como profesor, necesitas manejar las notas de tus estudiantes. 
# Permite ingresar todas las notas de los estudiantes y realiza varias 
# operaciones con esos datos. 
# Pregunta 1: Calcula el promedio de las notas de la clase. ¿Cómo lo harías? 
# Pregunta 2: Encuentra la nota más baja y la más alta. ¿Cómo lo harías? 
# Pregunta 3: Identifica la nota que más se repite. ¿Cómo lo harías? 
# Nota: La función Counter es útil porque simplifica el conteo de elementos 
# en una lista, permitiendo identificar rápidamente la frecuencia de cada nota. 
# Pregunta 4 (Plus): Realiza un gráfico de barras con las notas. ¿Cómo lo harías? 
# Nota: La biblioteca matplotlib.pyplot es útil porque proporciona funciones 
# fáciles de usar para crear visualizaciones de datos, como gráficos de barras, 
# que pueden ayudar a visualizar la distribución de las notas de manera clara 
# y comprensible.

# Importamos librerías necesarias
import numpy as np  # Para realizar cálculos numéricos
import matplotlib.pyplot as plt  # Para realizar gráficos
from collections import Counter  # Para contar las frecuencias de cada nota

# Creamos un arreglo con las notas de los estudiantes
notas = np.array([1, 9, 7, 8, 1, 9, 9, 12, 10, 8, 9, 10, 9, 12, 4, 1, 8, 11, 8, 5, 7, 10, 9, 6, 2, 11, 12, 9, 12, 9, 3, 11, 10, 6, 10, 6, 8, 7])

# Pregunta 1: Calcula el promedio de las notas de la clase.
promedio = np.mean(notas)  # Calcula el promedio de las notas
print(f"El promedio de las notas de la clase es: {promedio:.2f}")  # Imprime el promedio con dos decimales

# Pregunta 2: Encuentra la nota más baja y la más alta.
nota_mas_baja = np.min(notas)  # Encuentra la nota más baja
nota_mas_alta = np.max(notas)  # Encuentra la nota más alta
print(f"La nota más baja es: {nota_mas_baja}")  # Imprime la nota más baja
print(f"La nota más alta es: {nota_mas_alta}")  # Imprime la nota más alta

# Pregunta 3: Identifica la nota que más se repite.
cuenta_notas = Counter(notas)  # Cuenta la frecuencia de cada nota
nota_mas_repetida = max(cuenta_notas, key=cuenta_notas.get)  # Obtiene la nota más repetida
print(f"La nota que más se repite es: {nota_mas_repetida}")  # Imprime la nota más repetida

# Pregunta 4 (Plus): Realiza un gráfico de barras con las notas.
notas_unicas, conteo = np.unique(notas, return_counts=True)  # Devuelve las notas únicas y sus frecuencias
plt.bar(notas_unicas, conteo)  # Crea el gráfico de barras
plt.xlabel("Notas")  # Etiqueta del eje x
plt.ylabel("Frecuencia con que se repiten las notas")  # Etiqueta del eje y
plt.title("Control de Notas de los Estudiantes")  # Título del gráfico
plt.xticks(notas_unicas)  # Muestra los valores únicos en el eje x
plt.show()  # Muestra el gráfico resultante