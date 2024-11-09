# Ordenar estudiantes por promedio de calificaciones 
# Tienes una lista de estudiantes y su promedio de calificaciones. 
# Implementa un algoritmo que ordene a los estudiantes de acuerdo 
# con su promedio utilizando el algoritmo de ordenamiento por selección. 
# Al final, el estudiante con el promedio más alto debe estar en primer lugar.

# Lista de estudiantes y sus promedios de calificaciones
# Cada elemento es una tupla con el nombre del estudiante y su promedio de calificación
estudiantes = [("José", 8), ("Laura", 9), ("María", 7), ("Nicolás", 12), ("Soledad", 11)]

# Función para ordenar estudiantes por promedio de calificación en orden descendente usando el algoritmo de selección
def ordenamiento_seleccion(estudiantes):
    n = len(estudiantes)  # Cantidad de estudiantes en la lista

    # Bucle para recorrer cada posición de la lista de estudiantes
    for i in range(n):
# Suponemos que el elemento en la posición actual i tiene el promedio más alto (índice mínimo temporal)
        min_idx = i

# Bucle interno para encontrar el estudiante con el promedio más alto en la parte no ordenada de la lista
        for j in range(i + 1, n):
# Comparamos los promedios: si encontramos un promedio mayor, actualizamos min_idx
            if estudiantes[j][1] > estudiantes[min_idx][1]:  # [1] accede al promedio en cada tupla
                min_idx = j  # Actualizamos min_idx al índice del estudiante con el promedio mayor encontrado

# Intercambiamos el estudiante con el promedio más alto encontrado con el primer elemento no ordenado
        estudiantes[i], estudiantes[min_idx] = estudiantes[min_idx], estudiantes[i]

# Llamada a la función para ordenar la lista de estudiantes en orden descendente según el promedio
ordenamiento_seleccion(estudiantes)

# Imprime la lista ordenada de estudiantes con sus promedios
print("Estudiantes ordenados por promedio de calificaciones (de mayor a menor):")
for estudiante in estudiantes:
    print(f"{estudiante[0]}: {estudiante[1]}")  # Imprime el nombre y promedio de cada estudiante

