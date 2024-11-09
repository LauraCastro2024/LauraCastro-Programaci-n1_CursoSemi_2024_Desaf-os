
# Definimos la clase Autor, que representa a un autor de libros.
class Autor:
    # El constructor (__init__) se ejecuta cuando se crea un objeto de la clase Autor.
    def __init__(self, nombre, fecha_nacimiento, nacionalidad, biografia=""):
        # Asignamos los valores pasados como parámetros a los atributos del autor.
        self.nombre = nombre  # Nombre del autor
        self.fecha_nacimiento = fecha_nacimiento  # Fecha de nacimiento del autor
        self.nacionalidad = nacionalidad  # Nacionalidad del autor
        self.biografia = biografia  # Biografía del autor (es opcional, por defecto es una cadena vacía)
        self.libros = []  # Inicializamos una lista vacía para almacenar los libros del autor.

    # Método para agregar un libro a la lista de libros del autor.
    def agregar_libro(self, libro):
    # Agrega un libro a la lista de libros del autor.
        # Si el libro no está ya en la lista de libros, lo agregamos.
        if libro not in self.libros:
            self.libros.append(libro)

    # Método para eliminar un libro de la lista de libros del autor.
    def eliminar_libro(self, libro):
        #Elimina un libro de la lista de libros del autor.
        # Si el libro está en la lista de libros, lo eliminamos.
        if libro in self.libros:
            self.libros.remove(libro)

    # Método para mostrar la lista de libros del autor.
    def mostrar_libros(self):
        #Muestra la lista de libros del autor.
        # Si el autor tiene libros, los mostramos.
        if self.libros:
            print(f"Libros escritos por {self.nombre}:")
            # Iteramos sobre los libros y mostramos el título y el ISBN de cada uno.
            for libro in self.libros:
                print(f"- {libro.titulo} (ISBN: {libro.isbn})")
        else:
            # Si no hay libros, mostramos un mensaje indicando que no ha escrito libros.
            print(f"{self.nombre} no ha escrito ningún libro.")

    # Método para mostrar toda la información del autor.
    def mostrar_informacion(self):
      # Muestra la información completa del autor.
        # Mostramos la información básica del autor (nombre, fecha de nacimiento, etc.)
        print(f"Nombre: {self.nombre}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Biografía: {self.biografia}")
        # Llamamos al método mostrar_libros() para mostrar los libros del autor.
        self.mostrar_libros()

# Definimos la clase Libro, que representa un libro escrito por un autor.
class Libro:
    # El constructor (__init__) se ejecuta cuando se crea un objeto de la clase Libro.
    def __init__(self, titulo, autor, isbn):
        # Asignamos los valores pasados como parámetros a los atributos del libro.
        self._titulo = titulo  # Título del libro (atributo privado)
        self._autor = autor    # Autor del libro (atributo privado)
        self._isbn = isbn      # ISBN del libro (atributo privado)

    # Método getter para obtener el título del libro.
    @property
    def titulo(self):
        return self._titulo  # Retorna el título del libro.

    # Método getter para obtener el autor del libro.
    @property
    def autor(self):
        return self._autor  # Retorna el autor del libro.

    # Método getter para obtener el ISBN del libro.
    @property
    def isbn(self):
        return self._isbn  # Retorna el ISBN del libro.

# Ejemplo de uso del código:

# Creamos un autor con su nombre, fecha de nacimiento, nacionalidad y biografía.
autor = Autor("Gabriel García Márquez", "1927-03-06", "Colombiano", "Escritor y periodista colombiano.")

# Creamos dos libros, asignándoles un título, un autor y un ISBN.
libro1 = Libro("Cien años de soledad", autor, "978-3-16-148410-0")
libro2 = Libro("El otoño del patriarca", autor, "978-3-16-148411-7")

# Agregamos los libros al autor usando el método agregar_libro().
autor.agregar_libro(libro1)
autor.agregar_libro(libro2)

# Finalmente, mostramos toda la información del autor, incluyendo sus libros.
autor.mostrar_informacion()