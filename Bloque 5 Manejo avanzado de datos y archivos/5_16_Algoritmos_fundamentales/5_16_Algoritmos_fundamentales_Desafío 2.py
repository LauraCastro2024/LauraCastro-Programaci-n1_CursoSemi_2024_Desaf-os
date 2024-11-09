# Implementar búsqueda secuencial en una tabla de calificaciones. 
# Tienes una tabla de calificaciones representada como una matriz, 
# donde cada fila contiene las calificaciones de un estudiante 
# en distintas materias. 
# Implementa una función que busque una calificación específica 
# en toda la matriz y devuelva el estudiante y 
# la materia en la que se encuentra.

# Matriz de calificaciones donde cada fila representa a un estudiante y cada columna una materia
calificaciones = [
    [12, 9, 8],  # Calificaciones para el Estudiante 1 en cada materia
    [9, 8, 10],  # Calificaciones para el Estudiante 2 en cada materia
    [7, 8, 9]   # Calificaciones para el Estudiante 3 en cada materia
]

# Función para buscar una calificación específica en la matriz de calificaciones
def buscar_calificacion(calificaciones, calificacion_buscar):
    # Recorre cada fila de la matriz, donde cada fila representa a un estudiante
    for i, fila in enumerate(calificaciones):  # i es el índice del estudiante (fila)
        
        # Recorre cada calificación en la fila del estudiante
        for j, calificacion in enumerate(fila):  # j es el índice de la materia (columna)
            
            # Compara la calificación actual con la calificación que estamos buscando
            if calificacion == calificacion_buscar:
                
                # Si la calificación se encuentra, retorna la posición en formato de estudiante y materia
                return f"Estudiante {i + 1}, Materia {j + 1}"
    
    # Si la calificación no se encuentra en ninguna posición de la matriz, retorna un mensaje
    return "Calificación no encontrada"

# Llamada a la función para buscar la calificación específica (en este caso, 10)
resultado = buscar_calificacion(calificaciones, 10)

# Muestra el resultado de la búsqueda en pantalla
print(resultado)