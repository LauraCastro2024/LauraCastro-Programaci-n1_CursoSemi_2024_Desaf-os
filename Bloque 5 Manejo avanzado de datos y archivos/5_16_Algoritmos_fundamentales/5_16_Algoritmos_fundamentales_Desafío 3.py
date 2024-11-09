# Optimizar la búsqueda en una lista ordenada de estudiantes. 
# Tienes una lista ordenada alfabéticamente con los nombres 
# de los estudiantes de una clase. 
# Implementa una función que realice una búsqueda binaria 
# para encontrar un estudiante específico en la lista. 
# Si el estudiante no está, la función debe mostrar un mensaje adecuado.

# Lista de estudiantes ordenados alfabéticamente
estudiantes = ["José", "Laura", "María", "Nicolás", "Soledad"]

# Función para realizar búsqueda binaria en una lista de estudiantes
def busqueda_binaria(estudiantes, nombre_buscar):
    # Definimos los límites iniciales de búsqueda en la lista
    bajo = 0  # Índice inicial (primero de la lista)
    alto = len(estudiantes) - 1  # Índice final (último de la lista)

    # Bucle que se ejecuta mientras haya elementos en el rango de búsqueda
    while bajo <= alto:  
        # Encuentra el índice central (posición media entre 'bajo' y 'alto')
        medio = (bajo + alto) // 2  
        
        # Compara el nombre en la posición media con el nombre que estamos buscando
        if estudiantes[medio] == nombre_buscar:  # Si son iguales
            # Retorna el mensaje indicando la posición (sumamos 1 para que sea más comprensible)
            return f"Estudiante encontrado en la posición: {medio + 1}"  
        
        # Si el nombre en la posición media es menor que el nombre buscado, buscamos en la mitad superior
        elif estudiantes[medio] < nombre_buscar:  
            bajo = medio + 1  # Cambiamos el límite inferior de búsqueda a la mitad superior
        
        # Si el nombre en la posición media es mayor que el nombre buscado, buscamos en la mitad inferior
        else:
            alto = medio - 1  # Cambiamos el límite superior de búsqueda a la mitad inferior

    # Si no encontramos el nombre en la lista, retornamos este mensaje
    return "Estudiante no encontrado"

# Llamada a la función para buscar al estudiante "Laura"
resultado = busqueda_binaria(estudiantes, "Laura")

# Imprime el resultado de la búsqueda en pantalla
print(resultado)
