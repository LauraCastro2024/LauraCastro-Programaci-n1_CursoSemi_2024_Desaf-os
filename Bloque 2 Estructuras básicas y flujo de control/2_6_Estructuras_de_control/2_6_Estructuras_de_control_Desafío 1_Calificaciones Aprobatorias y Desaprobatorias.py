import csv
# Vamos a analizar las calificaciones de los estudiantes para saber cuántos aprobaron y cuántos desaprobaron.
# Se considera que una calificación de 7 o superior es aprobatoria y cualquier calificación menor a 7 es desaprobatoria.

# Leemos el archivo csv
with open('calificaciones.csv', 'r') as archivo_calificaciones:
    lector = csv.reader(archivo_calificaciones)
    next(lector) # Saltamos la cabecera del archivo

# Declaramos las variables
    aprobados = 0
    desaprobados = 0

# Verificamos cada calificación
# Convierte la calificación a un número flotante y se verifica si es mayor o igual a 7
    for fila in lector:
        calificacion = float(fila[1])  # Asumimos que la calificación está en la segunda columna
        if calificacion >= 7:
            aprobados += 1 # Se incrementa la variable
        else:
            desaprobados += 1 # Se incrementa la variable

# Imprimimos los resultados
    print(f"Estudiantes aprobados: {aprobados}")
    print(f"Estudiantes desaprobados: {desaprobados}")