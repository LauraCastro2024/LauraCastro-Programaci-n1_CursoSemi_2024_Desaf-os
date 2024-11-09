import numpy as np  # Importar la biblioteca NumPy para manipulación de matrices
import matplotlib.pyplot as plt  # Importar Matplotlib para visualización
import matplotlib.animation as animation  # Importar la funcionalidad de animación de Matplotlib

def crear_tablero(n, m):
    """Crea un tablero de juego n x m con un patrón inicial aleatorio."""
    return np.random.choice([0, 1], size=(n, m), p=[0.7, 0.3])  # 70% muertas (0), 30% vivas (1)

def contar_vecinos(tablero):
    """Cuenta el número de vecinos vivos para cada celda en el tablero."""
    vecinos = np.zeros(tablero.shape, dtype=int)  # Inicializar una matriz para contar vecinos
    for i in range(-1, 2):  # Iterar sobre filas vecinas
        for j in range(-1, 2):  # Iterar sobre columnas vecinas
            if not (i == 0 and j == 0):  # Ignorar la celda misma
                vecinos += np.roll(np.roll(tablero, i, axis=0), j, axis=1)  # Desplazar el tablero y contar vecinos
    return vecinos  # Retornar la matriz de conteo de vecinos

def actualizar_tablero(tablero):
    """Actualiza el tablero según las reglas del Juego de la Vida."""
    vecinos = contar_vecinos(tablero)  # Contar vecinos vivos
    nueva_generacion = np.zeros(tablero.shape, dtype=int)  # Crear una nueva matriz para la próxima generación

    # Aplicar las reglas del juego
    nueva_generacion[(tablero == 1) & ((vecinos == 2) | (vecinos == 3))] = 1  # Una célula viva sobrevive
    nueva_generacion[(tablero == 0) & (vecinos == 3)] = 1  # Una célula muerta nace
    return nueva_generacion  # Retornar la nueva generación

def simular_juego(n, m, iteraciones):
    """Simula el Juego de la Vida durante un número específico de iteraciones."""
    tablero = crear_tablero(n, m)  # Crear un tablero inicial
    fig, ax = plt.subplots()  # Crear una figura y un eje para la visualización

    def actualizar(frame):
        nonlocal tablero  # Permitir el uso de la variable tablero fuera del ámbito local
        ax.clear()  # Limpiar el eje para la nueva iteración
        ax.imshow(tablero, cmap='binary')  # Mostrar el tablero con un mapa de colores binario
        ax.set_title(f'Iteración {frame}')  # Establecer el título con la iteración actual
        tablero = actualizar_tablero(tablero)  # Actualizar el tablero a la siguiente generación

    ani = animation.FuncAnimation(fig, actualizar, frames=iteraciones, repeat=False)  # Crear la animación
    plt.show()  # Mostrar la animación

# Parámetros de la simulación
n = 10  # Número de filas en el tablero
m = 10  # Número de columnas en el tablero
iteraciones = 30  # Número de iteraciones a simular

# Ejecutar la simulación
simular_juego(n, m, iteraciones)  # Llamar a la función para iniciar la simulación