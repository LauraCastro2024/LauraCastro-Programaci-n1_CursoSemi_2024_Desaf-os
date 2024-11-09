# Evaluación de Expresiones Matemáticas con Árboles. 
# Construir y evaluar un árbol de expresiones para una expresión matemática dada. 
# Tu tarea es escribir un programa en Python que haga lo siguiente:
# Construir el Árbol de Expresiones: Dada una expresión matemática en forma 
# de cadena, construir el árbol de expresiones correspondiente. 
# Puedes asumir que la expresión está bien formada y solo contiene
# números enteros, y los operadores +, -, , /. 
# Evaluar el Árbol de Expresiones: Una vez construido el árbol, evaluarlo 
# y devolver el resultado de la expresión. 
# Prueba tu Programa: Utiliza la expresión "5 + 3 * 4" para probar tu programa. 
# El resultado debería ser 17.
# Consejos Puedes crear una clase Nodo para representar los nodos 
# en tu árbol de expresiones. 
# Cada nodo debería tener un valor y dos hijos (izquierdo y derecho). 
# Puedes crear funciones auxiliares para ayudarte a construir y 
# evaluar el árbol de expresiones.
# Recuerda seguir las reglas de precedencia de operadores al construir el árbol.
 
# Definimos la clase Nodo para representar cada nodo en el árbol de expresiones.
class Nodo:
    def __init__(self, valor):
        self.valor = valor  # Este es el valor del nodo (puede ser un número o un operador)
        self.izq = None     # Este es el hijo izquierdo del nodo
        self.der = None     # Este es el hijo derecho del nodo

# Función para construir el árbol de expresiones a partir de una lista de elemento
def construir_arbol(elementos):
    stack = []  # Usamos una lista como pila para construir el árbol

    # Recorremos cada elemento en la lista de elementos
    for elemento in elementos:
        # Verificamos si el elemento es un número
        if elemento.isdigit():  # Si el elemento es un número (por ejemplo, "5")
            # Creamos un nodo con el número y lo añadimos a la pila
            stack.append(Nodo(int(elemento)))  # Convertimos el elemento a entero y creamos un nodo
        else:
            # Si el elemento es un operador (por ejemplo, "+", "-", "*", "/")
            # Sacamos los dos últimos nodos de la pila
            nodo_der = stack.pop()  # Este será el hijo derecho del operador
            nodo_izq = stack.pop()  # Este será el hijo izquierdo del operador
            
            # Creamos un nuevo nodo con el operador
            nodo = Nodo(elemento)
            # Asignamos los nodos izquierdo y derecho al nuevo nodo
            nodo.izq = nodo_izq
            nodo.der = nodo_der
            # Añadimos el nuevo nodo a la pila
            stack.append(nodo)

    # El último nodo en la pila es la raíz del árbol
    return stack.pop()  # Sacamos y devolvemos la raíz del árbol

# Función para evaluar el árbol de expresiones
def evaluar_arbol(nodo):
    # Verificamos si el nodo es una hoja (sin hijos)
    if nodo.izq is None and nodo.der is None:  # Si no tiene hijos, es un número
        return nodo.valor  # Devolvemos el valor del nodo

    # Evaluamos los subárboles izquierdo y derecho de manera recursiva
    valor_izq = evaluar_arbol(nodo.izq)  # Evaluamos el hijo izquierdo
    valor_der = evaluar_arbol(nodo.der)  # Evaluamos el hijo derecho

    # Aplicamos el operador en el nodo actual
    if nodo.valor == '+':  # Si el operador es suma
        return valor_izq + valor_der  # Devolvemos la suma de los valores
    elif nodo.valor == '-':  # Si el operador es resta
        return valor_izq - valor_der  # Devolvemos la resta de los valores
    elif nodo.valor == '*':  # Si el operador es multiplicación
        return valor_izq * valor_der  # Devolvemos el producto de los valores
    elif nodo.valor == '/':  # Si el operador es división
        return valor_izq / valor_der  # Devolvemos la división de los valores

# Ejemplo de uso del código
if __name__ == "__main__":
    # Segun el ejercicio tenemos la expresión "5 + 3 * 4"
    # La representamos en notación de postfijo (RPN): "5 3 4 * +"
    elementos = ["5", "3", "4", "*", "+"]  # Lista de elementos que representa la expresión

    # Construimos el árbol de expresiones a partir de los elementos
    arbol = construir_arbol(elementos)

    # Evaluamos el árbol y guardamos el resultado
    resultado = evaluar_arbol(arbol)
    # Imprimimos el resultado de la evaluación
    print("El resultado de la expresión es:", resultado)  # Debería imprimir: 17