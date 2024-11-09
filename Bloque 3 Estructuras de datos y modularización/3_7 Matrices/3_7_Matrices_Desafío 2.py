import numpy as np  # Importar la biblioteca NumPy para el manejo de matrices y operaciones matemáticas

# Definir la matriz A
A = np.array([[1, 4, 5],        # Fila 1 de la matriz A
              [0, -16, 14],     # Fila 2 de la matriz A
              [7, 0, 0]])       # Fila 3 de la matriz A

# Calcular la matriz inversa
A_inv = np.linalg.inv(A)  # Utilizar la función inv() de NumPy para calcular la inversa de A

# Calcular la traza de la matriz inversa
traza_A_inv = np.trace(A_inv)  # Calcular la traza de la matriz inversa, que es la suma de sus elementos en la diagonal principal

# Imprimir el resultado
print("La traza de la matriz inversa de A es:", traza_A_inv)  # Mostrar la traza calculada