# Dado un conjunto de números enteros únicos, construye un árbol de búsqueda 
# binaria (ABB) que inserte los valores de manera que el subárbol izquierdo 
# de cada nodo contenga solo nodos con valores menores, 
# y el subárbol derecho solo nodos con valores mayores. 
# Una vez construido el árbol, implementa una función para buscar 
# un número dado y devuelva si ese número existe en el árbol o no.

# Definimos la clase Nodo para representar cada nodo en el árbol.
class Nodo: # Representa un nodo en el árbol, con un valor y punteros a sus hijos izquierdo y derecho.
    def __init__(self, key):
        self.val = key  # Valor del nodo
        self.izq = None  # Hijo izquierdo
        self.der = None  # Hijo derecho

# Definimos la clase para el Árbol de Búsqueda Binaria (ABB)
class ArbolBusquedaBinaria: # Representa el árbol de búsqueda binaria, con métodos para insertar y buscar valores
    def __init__(self):
        self.raiz = None  # Inicialmente, el árbol está vacío

# Método para insertar un nuevo valor en el árbol 
    def insertar(self, key):
        if self.raiz is None:
            self.raiz = Nodo(key)  # Si el árbol está vacío, el nuevo nodo es la raíz
        else:
            self._insertar_recursivo(self.raiz, key)  # Llamamos al método recursivo para insertar

# Método recursivo para insertar un nuevo nodo en el árbol de manera recursiva, 
# asegurando que los valores a la izquierda sean menores y 
# los de la derecha sean mayores.
    def _insertar_recursivo(self, nodo, key):
        if key < nodo.val:  # Si el valor es menor, vamos al subárbol izquierdo
            if nodo.izq is None:
                nodo.izq = Nodo(key)  # Insertamos el nuevo nodo aquí
            else:
                self._insertar_recursivo(nodo.izq, key)  # Continuamos en el subárbol izquierdo
        else:  # Si el valor es mayor o igual, vamos al subárbol derecho
            if nodo.der is None:
                nodo.der = Nodo(key)  # Insertamos el nuevo nodo aquí
            else:
                self._insertar_recursivo(nodo.der, key)  # Continuamos en el subárbol derecho

# Método para buscar un valor en el árbol, retornando True si lo encuentra y False si no.
    def buscar(self, key):
        return self._buscar_recursivo(self.raiz, key)  # Llamamos al método recursivo de búsqueda

# Método recursivo para buscar un valor en el árbol
    def _buscar_recursivo(self, nodo, key):
        if nodo is None:  # Si el nodo es nulo, el valor no está en el árbol
            return False
        if nodo.val == key:  # Si encontramos el valor, retornamos True
            return True
        elif key < nodo.val:  # Si el valor buscado es menor, buscamos en el subárbol izquierdo
            return self._buscar_recursivo(nodo.izq, key)
        else:  # Si el valor buscado es mayor, buscamos en el subárbol derecho
            return self._buscar_recursivo(nodo.der, key)

# Ejemplo de uso 
# Se crea un árbol, se insertan algunos números y se realizan búsquedas 
# para demostrar el funcionamiento del árbol.
if __name__ == "__main__":
# Creamos un árbol de búsqueda binaria
    abb = ArbolBusquedaBinaria()
    
# Insertamos algunos números en el árbol
    numeros = [7, 3, 9, 1, 5, 8, 10]
    for num in numeros:
        abb.insertar(num)

# Buscamos algunos números en el árbol
    print("Buscar 5:", abb.buscar(5))  # Imprime y muestra Verdadero
    print("Buscar 2:", abb.buscar(2))  # Imprime y muestra Falso
    print("Buscar 10:", abb.buscar(10))  # Imprime y muestra Verdadero
