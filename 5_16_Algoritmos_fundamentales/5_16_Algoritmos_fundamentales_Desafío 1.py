# Recorrido de estudiantes por niveles 
# Dado un árbol que representa los grupos de estudiantes en una escuela, 
# implementa un recorrido por niveles para mostrar los estudiantes 
# de cada grupo, comenzando por el nivel más alto (ej. grado 12) 
# y descendiendo hasta el nivel más bajo (ej. grado 1). 
# Cada nodo del árbol representa un grado y sus estudiantes.

# Definición de la clase Nodo, que representa cada grado en el árbol
class Nodo:
    def __init__(self, grado):
        self.grado = grado  # Almacena el grado (nivel educativo) del nodo
        self.estudiantes = []  # Lista para almacenar los nombres de estudiantes en este grado
        self.hijos = []  # Lista para almacenar nodos hijos (los grados inferiores que dependen de este)

# Función para agregar estudiantes a un grado específico
def agregar_estudiante(nodo, estudiante):
    # Añade un estudiante a la lista de estudiantes del nodo correspondiente al grado
    nodo.estudiantes.append(estudiante)

# Función para agregar un nodo hijo a un nodo padre
def agregar_hijo(nodo_padre, nodo_hijo):
    # Añade el nodo hijo (grado inferior) a la lista de hijos del nodo padre (grado superior)
    nodo_padre.hijos.append(nodo_hijo)

# Función para recorrer el árbol de grados por niveles y mostrar estudiantes en cada grado
def recorrido_por_niveles(nodo):
    if not nodo:  # Verifica si el nodo es None (si no hay nodo, no hace nada)
        return
    # Muestra el grado actual y los estudiantes en él
    print(f"Grado {nodo.grado}: {', '.join(nodo.estudiantes)}")
    
    # Recorre cada nodo hijo del grado actual, llamando a la función recursivamente para recorrer grados inferiores
    for hijo in nodo.hijos:
        recorrido_por_niveles(hijo)

# Creación del árbol de grados (estructura jerárquica de niveles educativos)
# Crea el nodo raíz (grado más alto) y le añade estudiantes y grados inferiores,
# mostrando luego la estructura completa.
# Creamos el nodo raíz, que representa el grado más alto 
raiz = Nodo("12")  # Nodo para el grado 12
# Añadimos un estudiante al grado 12
agregar_estudiante(raiz, "Estudiante A")

# Creamos nodos para los grados inferiores y les agregamos estudiantes
hijo1 = Nodo("11")  # Nodo para el grado 11
agregar_estudiante(hijo1, "Estudiante B")  # Añadimos un estudiante al grado 11

hijo2 = Nodo("10")  # Nodo para el grado 10
agregar_estudiante(hijo2, "Estudiante C")  # Añadimos un estudiante al grado 10

# Relacionamos el grado 12 con los grados 11 y 10, formando la estructura jerárquica
agregar_hijo(raiz, hijo1)  # Agrega el grado 11 como hijo del grado 12
agregar_hijo(raiz, hijo2)  # Agrega el grado 10 como hijo del grado 12

# Llamamos a la función para recorrer y mostrar el árbol por niveles, empezando desde el grado 12
recorrido_por_niveles(raiz)
