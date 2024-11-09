import numpy as np  # Importar la biblioteca NumPy para trabajar con matrices y realizar operaciones matemáticas

# Definir la matriz A
A = np.array([[1, 4, 7],        # Fila 1 de la matriz A
              [2, 5, 8],        # Fila 2 de la matriz A
              [3, 6, 9]])       # Fila 3 de la matriz A

# Calcular la transpuesta de A
A_T = A.T  # Utilizar la propiedad T de NumPy para obtener la transpuesta de la matriz A

# Calcular A + A^T
resultante = A + A_T  # Sumar la matriz A a su transpuesta

# Calcular el rango de la matriz resultante
rango_resultante = np.linalg.matrix_rank(resultante)  # Calcular el rango de la matriz resultante usando matrix_rank()

# Imprimir el resultado
print("El rango de la matriz resultante de (A + A^T) es:", rango_resultante)  # Mostrar el rango calculado