
## Definimos la clase base Libro 
class Libro:
    def __init__(self, titulo, autor):
      # Inicializa un libro con un título y un autor.
        self.titulo = titulo  ## Título del libro (nombre del libro)
        self.autor = autor    ## Autor del libro (quién escribió el libro)

    def __str__(self):
       # Devuelve una representación en forma de cadena del libro.
        # Este método convierte el objeto libro en una cadena para imprimirlo
        return f"{self.titulo} por {self.autor}"


# Definimos la subclase LibroEspecializado que hereda de Libro
class LibroEspecializado(Libro):
    def __init__(self, titulo, autor, campo_estudio, nivel_especializacion):
       # Inicializa un libro especializado con título, autor, campo de estudio y nivel de especialización.
        super().__init__(titulo, autor)  ## Llama al constructor de la clase base Libro para inicializar el título y autor
        self.campo_estudio = campo_estudio  ## Campo de estudio del libro especializado (por ejemplo, Informática)
        self.nivel_especializacion = nivel_especializacion  ## Nivel de especialización del libro (básico, intermedio, avanzado)

    def __str__(self):
        # Devuelve una representación en forma de cadena del libro especializado.
        # Este método convierte el objeto libro especializado en una cadena para imprimirlo
        return f"{self.titulo} por {self.autor} - Campo: {self.campo_estudio}, Nivel: {self.nivel_especializacion}"


# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Creamos un libro normal
    libro1 = Libro("1984", "George Orwell")  ## Se crea un libro con título "1984" y autor "George Orwell"
    print(libro1)  ## Imprimimos el libro normal

    # Creamos un libro especializado
    libro_especializado = LibroEspecializado("Introducción a la Programación", "John Doe", "Informática", "Básico")  
    # Se crea un libro especializado con título "Introducción a la Programación", autor "John Doe", 
    # campo de estudio "Informática" y nivel de especialización "Básico"
    print(libro_especializado)  ## Imprimimos el libro especializado
