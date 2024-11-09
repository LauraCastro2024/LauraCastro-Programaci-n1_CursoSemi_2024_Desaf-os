
# Clase base Autor: Representa a un autor en general
class Autor:
    def __init__(self, nombre, fecha_nacimiento, nacionalidad):
        # Método constructor que inicializa los atributos del autor.
        self.nombre = nombre  # Atributo para almacenar el nombre del autor
        self.fecha_nacimiento = fecha_nacimiento  # Atributo para almacenar la fecha de nacimiento
        self.nacionalidad = nacionalidad  # Atributo para almacenar la nacionalidad

    def biografia(self):
        # Método que devuelve una biografía básica del autor.
        # Retorna una cadena con el nombre, fecha de nacimiento y nacionalidad
        return f"{self.nombre} es un autor nacido el {self.fecha_nacimiento} de nacionalidad {self.nacionalidad}."

# Clase Escritor: Hereda de la clase Autor, representando a un escritor específico
class Escritor(Autor):
    def __init__(self, nombre, fecha_nacimiento, nacionalidad, genero):
        # Método constructor que inicializa los atributos del escritor, llamando al constructor de la clase base.
        super().__init__(nombre, fecha_nacimiento, nacionalidad)  # Llama al constructor de la clase Autor
        self.genero = genero  # Atributo para almacenar el género literario del escritor

    def biografia(self):
        # Método sobrescrito que devuelve una biografía más detallada del escritor.
        # Retorna una cadena que incluye el género literario del escritor
        return f"{self.nombre} es un escritor de {self.genero} nacido el {self.fecha_nacimiento} de nacionalidad {self.nacionalidad}."

# Instanciando un objeto de la clase Escritor
escritor = Escritor("Gabriel García Márquez", "1927-03-06", "Colombiano", "realismo mágico")
# Aquí creamos un objeto llamado 'escritor' que es una instancia de la clase Escritor

# Accediendo al método biografia de ambas clases
# Primero, creamos un objeto de la clase Autor y mostramos su biografía
print("Biografía desde la clase Autor:")
autor = Autor("Isaac Asimov", "1920-01-02", "Americano")  # Instanciamos un objeto de la clase Autor
print(autor.biografia())  # Llamamos al método biografia de la clase Autor

# Luego, mostramos la biografía del escritor, que es una versión más específica
print("\nBiografía desde la clase Escritor:")
print(escritor.biografia())  # Llamamos al método biografia de la clase Escritor (sobrescrito)