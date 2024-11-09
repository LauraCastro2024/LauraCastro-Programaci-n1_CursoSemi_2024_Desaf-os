# Construye un árbol binario en el que cada nodo contiene un número entero. 
# Implementa una función que recorra el árbol en postorden 
# y devuelva el valor máximo encontrado entre todos los nodos del árbol.

# postorden nos permite procesar completamente los subárboles
# antes de analizar un nodo, lo cual es útil para comparar valores en un árbol 
# sin saltarse nodos.

# Definimos la clase Nodo, que representa cada nodo en el árbol
class Nodo:
    def __init__(self, key):
        # Inicializamos un nodo con el valor 'key'.
        # Un nodo tiene tres partes: el valor, el hijo izquierdo y el hijo derecho
        self.izq = None  # El hijo izquierdo inicial es None (vacío)
        self.der = None  # El hijo derecho inicial es None (vacío)
        self.val = key   # El valor que guarda el nodo es 'key'

# Función para recorrer el árbol en postorden y encontrar el valor máximo
def find_max_postorder(raiz):
    # Si el nodo es None (es decir, es vacío), retornamos un valor muy bajo
    # Esto ayuda a que no se considere cuando lleguemos a un nodo vacío
    if raiz is None:
        return float('-inf')  # Retorna -infinito si el nodo es vacío
    
# Recorremos el subárbol izquierdo del nodo
    max_izq = find_max_postorder(raiz.izq)
    
# Recorremos el subárbol derecho del nodo
    max_der = find_max_postorder(raiz.der)
    
# Comparamos el valor del nodo actual con los valores máximos de los subárboles izquierdo y derecho
# La función 'max' devuelve el valor más grande de los tres
    return max(raiz.val, max_izq, max_der)

# Construye un árbol binario de ejemplo
# Creamos el nodo raíz con el valor 10
raiz = Nodo(10)

# Añadimos los hijos del nodo raíz
raiz.izq = Nodo(5)  # El hijo izquierdo del nodo raíz tiene el valor 5
raiz.der = Nodo(15) # El hijo derecho del nodo raíz tiene el valor 15

# Añadimos hijos a los nodos 5 y 15
raiz.izq.izq = Nodo(2)  # El hijo izquierdo de 5 tiene el valor 2
raiz.izq.der = Nodo(7)  # El hijo derecho de 5 tiene el valor 7
raiz.der.izq = Nodo(12) # El hijo izquierdo de 15 tiene el valor 12
raiz.der.der = Nodo(20) # El hijo derecho de 15 tiene el valor 20

# Llamamos a la función find_max_postorder pasando la raíz del árbol
max_value = find_max_postorder(raiz)

# Mostramos el valor máximo encontrado en el árbol
print(f"El valor máximo en el árbol es: {max_value}")
