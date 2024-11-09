# Definimos la clase Autor, que representa a un autor de libros
class Autor:
    # El método __init__ es el constructor de la clase, se llama cuando creamos una nueva instancia de Autor
    def __init__(self, nombre):
        self.nombre = nombre  # Guardamos el nombre del autor en el atributo 'nombre'
        self.libros = []  # Inicializamos una lista vacía llamada 'libros' donde guardaremos los libros del autor

    # Método para agregar un libro a la lista de libros del autor
    def agregar_libro(self, libro):
        """Agrega un libro a la lista de libros del autor."""
        # Verificamos si el libro ya está en la lista de libros del autor
        if libro not in self.libros:
            self.libros.append(libro)  # Si el libro no está, lo agregamos a la lista
            print(f"Libro '{libro}' agregado a la lista de {self.nombre}.")
        else:
            # Si el libro ya está en la lista, mostramos un mensaje indicando que ya existe
            print(f"El libro '{libro}' ya está en la lista de {self.nombre}.")

    # Método para eliminar un libro de la lista de libros del autor
    def eliminar_libro(self, libro):
        """Elimina un libro de la lista de libros del autor."""
        # Verificamos si el libro está en la lista de libros del autor
        if libro in self.libros:
            self.libros.remove(libro)  # Si el libro está en la lista, lo eliminamos
            print(f"Libro '{libro}' eliminado de la lista de {self.nombre}.")
        else:
            # Si el libro no está en la lista, mostramos un mensaje indicando que no se encuentra
            print(f"El libro '{libro}' no se encuentra en la lista de {self.nombre}.")

    # Método para mostrar todos los libros del autor
    def mostrar_libros(self):
        """Muestra la lista de libros del autor."""
        # Si el autor tiene libros, mostramos la lista
        if self.libros:
            print(f"Libros escritos por {self.nombre}:")
            for libro in self.libros:
                print(f"- {libro}")  # Mostramos cada libro en la lista
        else:
            # Si el autor no tiene libros, mostramos un mensaje indicando que no ha escrito ninguno
            print(f"{self.nombre} no ha escrito ningún libro.")

# Ejemplo de uso:
# Creamos una nueva instancia de la clase Autor con el nombre 'Paulo Coelho'
autor = Autor("Paulo Coelho")

# Agregamos algunos libros a la lista de libros del autor
autor.agregar_libro("El alquimista")  # Agregamos El alquimista
autor.agregar_libro("Adulterio")  # Agregamos Adulterio

# Mostramos los libros que tiene el autor
autor.mostrar_libros()

# Eliminamos un libro de la lista de libros del autor
autor.eliminar_libro("Adulterio")  # Eliminamos Adulterio

# Mostramos nuevamente los libros que tiene el autor después de la eliminación
autor.mostrar_libros()