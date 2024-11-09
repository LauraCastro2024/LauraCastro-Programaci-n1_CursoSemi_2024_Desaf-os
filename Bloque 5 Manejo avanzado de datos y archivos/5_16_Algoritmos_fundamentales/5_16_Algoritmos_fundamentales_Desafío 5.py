# Crear un árbol de clasificación de estudiantes por rendimiento 
# Dado un conjunto de estudiantes y sus promedios, 
# implementa una función que cree un árbol binario de búsqueda 
# en el que los nodos representan los promedios de los estudiantes. 
# Luego, implementa una función que recorra el árbol en inorden 
# para mostrar los estudiantes en orden ascendente de rendimiento académico.

# Definición de la clase Nodo, que representa a cada estudiante en el árbol
class Nodo:
    def __init__(self, promedio, nombre):
# Cada nodo almacena el promedio y el nombre del estudiante
        self.promedio = promedio  # Almacena el promedio de calificación del estudiante
        self.nombre = nombre      # Almacena el nombre del estudiante
# Los siguientes dos atributos representan los subárboles izquierdo y derecho
        self.izq = None           # Nodo izquierdo (contendrá estudiantes con promedio menor)
        self.der = None           # Nodo derecho (contendrá estudiantes con promedio mayor o igual)

# Función para insertar un nuevo estudiante en el árbol
def insertar(nodo, promedio, nombre):
# Si el nodo actual es None, creamos y retornamos un nuevo nodo con el estudiante
    if nodo is None:
        return Nodo(promedio, nombre)
    
# Si el promedio del estudiante es menor que el nodo actual, inserta a la izquierda
    if promedio < nodo.promedio:
        nodo.izq = insertar(nodo.izq, promedio, nombre)
# Si el promedio es mayor o igual, inserta a la derecha
    else:
        nodo.der = insertar(nodo.der, promedio, nombre)
    
# Retorna el nodo actual (útil para mantener la estructura del árbol al insertar)
    return nodo

# Función para recorrer el árbol en orden (inorden)
def recorrido_inorden(nodo):
    if nodo:
# Primero recorre el subárbol izquierdo (estudiantes con promedios más bajos)
        recorrido_inorden(nodo.izq)
# Imprime el nombre y el promedio del estudiante actual en el nodo
        print(f"{nodo.nombre}: {nodo.promedio}")
# Recorre el subárbol derecho (estudiantes con promedios más altos)
        recorrido_inorden(nodo.der)

# Creamos el árbol de estudiantes, inicialmente vacío (raiz = None)
raiz = None

# Lista de estudiantes con sus nombres y promedios de calificación
estudiantes = [("José", 8), ("Laura", 9), ("María", 7), ("Nicolás", 12), ("Soledad", 11)]

# Insertamos cada estudiante en el árbol usando la función insertar
for nombre, promedio in estudiantes:
    raiz = insertar(raiz, promedio, nombre)

# Llamada a la función para recorrer el árbol e imprimir los estudiantes en orden ascendente de promedio
print("Estudiantes en orden de rendimiento académico:")
recorrido_inorden(raiz)
