
# Definimos la clase base Autor
class Autor:
    def __init__(self, nombre, nacionalidad):
        # Inicializa un autor con nombre y nacionalidad.
        self.nombre = nombre  ## Asigna el nombre del autor al atributo 'nombre'
        self.nacionalidad = nacionalidad  ## Asigna la nacionalidad del autor al atributo 'nacionalidad'

    def __str__(self):
        # Devuelve una representación en forma de cadena del autor.
        return f"{self.nombre}, {self.nacionalidad}"  ## Devuelve el nombre y nacionalidad del autor en formato de cadena


# Definimos la subclase Poeta que hereda de Autor
class Poeta(Autor):
    def __init__(self, nombre, nacionalidad, tipo_poesia):
        # Inicializa un poeta con nombre, nacionalidad y tipo de poesía.
        super().__init__(nombre, nacionalidad)  ## Llama al constructor de la clase base 'Autor' para inicializar nombre y nacionalidad
        self.tipo_poesia = tipo_poesia  ## Asigna el tipo de poesía que escribe el poeta al atributo 'tipo_poesia'

    def __str__(self):
        # Devuelve una representación en forma de cadena del poeta.
        return f"{super().__str__()}, Tipo de poesía: {self.tipo_poesia}"  ## Devuelve la información del autor junto con el tipo de poesía que escribe el poeta


# Ejemplo de uso
poeta = Poeta("Pablo Neruda", "Chileno", "Amor")  ## Creamos un objeto 'Poeta' con el nombre "Pablo Neruda", nacionalidad "Chileno" y tipo de poesía "Amor"
print(poeta)  ## Imprimimos la información del poeta, que llama al método '__str__' de la clase Poeta
