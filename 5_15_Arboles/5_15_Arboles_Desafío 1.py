# Construye un árbol binario simple con al menos 3 niveles de profundidad. 
# Cada nodo debe contener un número entero como valor. 
# Una vez construido el árbol, implementa una función que imprima 
# los valores de los nodos siguiendo un recorrido en preorden.

# Definimos la clase Nodo, que representa cada nodo en el árbol.
# La clase Nodo establece una estructura de árbol básico, 
# donde cada nodo tiene espacio para un valor y referencias 
# a dos nodos hijos (izquierdo y derecho), 
# permitiendo representar estructuras jerárquicas.

class Nodo:
    def __init__(self, key):
        # Creamos la estructura básica del nodo para contener un valor y enlaces a posibles hijos.
        # Esto es necesario para representar un árbol en programación.
        self.izq = None  # Se inicia el hijo izquierdo del nodo como None (vacío), ya que aún no tiene hijos.
        self.der = None  # Se inicia el hijo derecho del nodo como None (vacío).
        self.val = key   # Se guarda el valor del nodo, que puede ser cualquier dato, en este caso es un número.

# Función para realizar un recorrido en preorden.
def print_preorder(raiz):
    # Este tipo de recorrido se utiliza para visitar y mostrar primero el nodo raíz,
    # luego su hijo izquierdo y finalmente su hijo derecho.
    if raiz:  # Validamos que el nodo actual no sea None para evitar errores.
        print(raiz.val, end=" ")  # Imprimimos el valor del nodo actual.
        print_preorder(raiz.izq)  # Llamamos recursivamente a la función para recorrer el hijo izquierdo.
        print_preorder(raiz.der)  # Llamamos recursivamente para recorrer el hijo derecho.

# Creamos el nodo raíz y sus hijos para construir un árbol de ejemplo de 3 niveles.
raiz = Nodo(1)       # Creamos la raíz del árbol con el valor 1, punto inicial del árbol.
raiz.izq = Nodo(2)   # Agregamos un nodo a la izquierda de la raíz.
raiz.der = Nodo(3)   # Agregamos un nodo a la derecha de la raíz.
raiz.izq.izq = Nodo(4)  # Agregamos un nodo al subárbol izquierdo, extendiendo la estructura.
raiz.izq.der = Nodo(5)  # Continuamos agregando nodos para agrandar el árbol.
raiz.der.izq = Nodo(6)
raiz.der.der = Nodo(7)

# Llamamos a la función para mostrar el recorrido en preorden.
# La función print_preorder organiza la manera en que los nodos son visitados. 
# Es útil para visualizar o procesar un árbol desde la raíz hacia sus ramas, 
# de izquierda a derecha.
print_preorder(raiz)  # Esto imprimirá los valores en el orden preorden esperado.




