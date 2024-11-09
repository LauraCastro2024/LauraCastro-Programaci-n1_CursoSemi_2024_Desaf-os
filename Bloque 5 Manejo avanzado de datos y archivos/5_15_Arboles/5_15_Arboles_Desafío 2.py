# Dado un árbol binario con números enteros en cada nodo, 
# implementa una función que recorra el árbol en inorden y 
# calcule la suma de todos los valores almacenados en los nodos. 
# El programa debe devolver el resultado final de la suma.

# Función para recorrer el árbol en inorden y calcular la suma total de los valores.
# Lo que hace suma_inorder es usar un recorrido en inorden, 
# lo que permite procesar el árbol de manera secuencial. 
# Usar inorden es útil para sumar valores en orden y para aplicaciones
# que requieren procesar cada elemento en el orden que tendrían
# en una lista ordenada.
# Definición de la clase Nodo
class Nodo:
    def __init__(self, key):
        # Cada nodo tiene un valor (key) y dos hijos (izq y der)
        self.izq = None   # El hijo izquierdo es inicialmente None (vacío)
        self.der = None   # El hijo derecho es inicialmente None (vacío)
        self.val = key    # El valor del nodo es el parámetro 'key'

# Función que recorre el árbol en inorden y calcula la suma de los valores
def suma_inorden(raiz):
    # Si el nodo es None (no existe), retornamos 0
    if raiz is None:
        return 0
    
    # Si el nodo existe, seguimos el orden: 
    # 1. Recorrer el subárbol izquierdo (llamamos recursivamente la función)
    # 2. Sumar el valor del nodo actual (raiz.val)
    # 3. Recorrer el subárbol derecho (llamamos recursivamente la función)
    return suma_inorden(raiz.izq) + raiz.val + suma_inorden(raiz.der)

# Crear el árbol de ejemplo
raiz = Nodo(1)           # Nodo raíz con valor 1
raiz.izq = Nodo(2)       # Nodo hijo izquierdo con valor 2
raiz.der = Nodo(3)       # Nodo hijo derecho con valor 3

# Añadir nodos al subárbol izquierdo
raiz.izq.izq = Nodo(4)   # Nodo hijo izquierdo del nodo 2
raiz.izq.der = Nodo(5)   # Nodo hijo derecho del nodo 2

# Añadir nodos al subárbol derecho
raiz.der.izq = Nodo(6)   # Nodo hijo izquierdo del nodo 3
raiz.der.der = Nodo(7)   # Nodo hijo derecho del nodo 3

# Añadir nodos a más niveles
raiz.izq.der.izq = Nodo(8)  # Nodo hijo izquierdo del nodo 5
raiz.izq.der.der = Nodo(9)  # Nodo hijo derecho del nodo 5
raiz.der.der.izq = Nodo(10) # Nodo hijo izquierdo del nodo 7
raiz.der.der.der = Nodo(11) # Nodo hijo derecho del nodo 7

# Calcular la suma en inorden del árbol
resultado = suma_inorden(raiz)

# Imprimir el resultado de la suma de todos los valores en el árbol
print("La suma de los valores del árbol es:", resultado)
