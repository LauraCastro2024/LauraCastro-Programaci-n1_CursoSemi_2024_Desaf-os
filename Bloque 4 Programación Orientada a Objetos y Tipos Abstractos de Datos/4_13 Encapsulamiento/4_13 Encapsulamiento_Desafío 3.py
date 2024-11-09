
# Definimos la clase Autor, que representa a un autor de libros.
class Autor:
    # El constructor (__init__) se ejecuta cuando creamos un objeto de la clase Autor.
    def __init__(self, nombre, fecha_nacimiento, nacionalidad, biografia=""):
        # Inicializamos los atributos del autor con los valores proporcionados.
        self._nombre = nombre  # Nombre del autor (atributo privado)
        self._fecha_nacimiento = fecha_nacimiento  # Fecha de nacimiento del autor
        self._nacionalidad = nacionalidad  # Nacionalidad del autor (atributo privado)
        self.biografia = biografia  # Biografía del autor, valor por defecto es una cadena vacía
        self.libros = []  # Inicializamos una lista vacía para almacenar los libros del autor

    # Métodos getter para obtener el nombre y la nacionalidad del autor
    @property
    def nombre(self):
        return self._nombre  # Devuelve el nombre del autor

    @property
    def nacionalidad(self):
        return self._nacionalidad  # Devuelve la nacionalidad del autor

    # Métodos setter para modificar el nombre y la nacionalidad del autor
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre  # Modifica el nombre del autor

    @nacionalidad.setter
    def nacionalidad(self, nueva_nacionalidad):
        self._nacionalidad = nueva_nacionalidad  # Modifica la nacionalidad del autor

    # Método para agregar un libro a la lista de libros del autor.
    def agregar_libro(self, libro):
        """Agrega un libro a la lista de libros del autor."""
        if libro not in self.libros:
            self.libros.append(libro)  # Agrega el libro a la lista si no está ya en ella.

    # Método para eliminar un libro de la lista de libros del autor.
    def eliminar_libro(self, libro):
        """Elimina un libro de la lista de libros del autor."""
        if libro in self.libros:
            self.libros.remove(libro)  # Elimina el libro de la lista si está en ella.

    # Método para mostrar la lista de libros que ha escrito el autor.
    def mostrar_libros(self):
        """Muestra la lista de libros del autor."""
        if self.libros:
            print(f"Libros escritos por {self.nombre}:")
            # Iteramos sobre la lista de libros e imprimimos el título y el ISBN de cada uno.
            for libro in self.libros:
                print(f"- {libro.titulo} (ISBN: {libro.isbn})")
        else:
            # Si no hay libros, mostramos un mensaje indicando que el autor no ha escrito libros.
            print(f"{self.nombre} no ha escrito ningún libro.")

    # Método para mostrar toda la información del autor, incluidos sus libros.
    def mostrar_informacion(self):
        """Muestra la información completa del autor."""
        print(f"Nombre: {self.nombre}")
        print(f"Fecha de nacimiento: {self._fecha_nacimiento}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Biografía: {self.biografia}")
        # Llamamos al método mostrar_libros() para mostrar los libros del autor.
        self.mostrar_libros()


# Clase Libro que representa a un libro escrito por un autor.
class Libro:
    # El constructor (__init__) se ejecuta cuando creamos un objeto de la clase Libro.
    def __init__(self, titulo, autor, isbn):
        # Inicializamos los atributos del libro con los valores proporcionados.
        self._titulo = titulo  # Título del libro (atributo privado)
        self._autor = autor    # Autor del libro (atributo privado)
        self._isbn = isbn      # ISBN del libro (atributo privado)

    # Métodos getter para obtener el título, autor e ISBN del libro
    @property
    def titulo(self):
        return self._titulo  # Devuelve el título del libro

    @property
    def autor(self):
        return self._autor  # Devuelve el autor del libro

    @property
    def isbn(self):
        return self._isbn  # Devuelve el ISBN del libro


# Ejemplo de uso del código:

# Creamos un objeto de la clase Autor con los datos de Gabriel García Márquez.
autor = Autor("Gabriel García Márquez", "1927-03-06", "Colombiano", "Escritor y periodista colombiano.")

# Creamos dos objetos de la clase Libro, asociando un título, autor e ISBN.
libro1 = Libro("Cien años de soledad", autor, "978-3-16-148410-0")
libro2 = Libro("El otoño del patriarca", autor, "978-3-16-148411-7")

# Agregamos los libros al autor usando el método agregar_libro().
autor.agregar_libro(libro1)
autor.agregar_libro(libro2)

# Mostramos toda la información del autor, incluidos los libros que ha escrito.
autor.mostrar_informacion()

# Modificamos el nombre y la nacionalidad del autor utilizando los setters.
autor.nombre = "Gabriel García"  # Modificamos el nombre del autor
autor.nacionalidad = "Colombiano y Mexicano"  # Modificamos la nacionalidad del autor

# Mostramos la información actualizada del autor después de modificarla.
print("\nInformación actualizada del autor:")
autor.mostrar_informacion()