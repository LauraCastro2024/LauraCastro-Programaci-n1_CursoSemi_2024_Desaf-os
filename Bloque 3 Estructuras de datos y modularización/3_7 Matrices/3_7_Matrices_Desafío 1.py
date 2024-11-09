import numpy as np  # Importar la biblioteca NumPy para trabajar con matrices

# Definir las matrices A y B
A = np.array([1, 3, 2, 4])  # Crear una matriz 1D A con los elementos 1, 3, 2 y 4
B = np.array([5, 7, 6, 8])  # Crear una matriz 1D B con los elementos 5, 7, 6 y 8

# Calcular 2A
result_2A = 2 * A  # Multiplicar cada elemento de A por 2

# Calcular B^T
B_T = B.reshape(-1, 1)  # Transponer B para convertirlo en una matriz columna

# Sumar 2A y B^T
result = result_2A + B_T  # Sumar la matriz resultante de 2A a la matriz columna B_T

# Imprimir el resultado
print("Resultado de 2A + B^T:", result)  # Mostrar el resultado de la suma