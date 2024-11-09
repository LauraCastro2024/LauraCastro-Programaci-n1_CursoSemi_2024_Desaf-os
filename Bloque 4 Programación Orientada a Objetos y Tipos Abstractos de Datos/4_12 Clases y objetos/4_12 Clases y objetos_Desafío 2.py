# Crea una clase Libro con atributos como título, género e ISBN. 
# ¿Cómo podrías relacionar esta clase con la clase Autor?

# Definimos la clase Autor, que representa a un autor de libros
class Autor:
    # El método __init__ es el constructor de la clase, se ejecuta cuando creamos un nuevo autor
    def __init__(self, nombre):
        self.nombre = nombre  # Guardamos el nombre del autor en el atributo 'nombre'
        self.libros = []  # Inicializamos una lista vacía llamada 'libros' donde guardaremos los libros del autor

    # Método para agregar un libro a la lista de libros del autor
    def agregar_libro(self, libro):
        #Agrega un libro a la lista de libros del autor.
        # Verificamos si el libro no está ya en la lista de libros del autor
        if libro not in self.libros:
            self.libros.append(libro)  # Si el libro no está, lo agregamos a la lista
            print(f"Libro '{libro.titulo}' agregado a la lista de {self.nombre}.")  # Imprimimos un mensaje
        else:
            # Si el libro ya está en la lista, mostramos un mensaje diciendo que ya existe
            print(f"El libro '{libro.titulo}' ya está en la lista de {self.nombre}.")

    # Método para eliminar un libro de la lista de libros del autor
    def eliminar_libro(self, libro):
        # Elimina un libro de la lista de libros del autor.
        # Verificamos si el libro está en la lista de libros del autor
        if libro in self.libros:
            self.libros.remove(libro)  # Si el libro está en la lista, lo eliminamos
            print(f"Libro '{libro.titulo}' eliminado de la lista de {self.nombre}.")
        else:
            # Si el libro no está en la lista, mostramos un mensaje diciendo que no se encuentra
            print(f"El libro '{libro.titulo}' no se encuentra en la lista de {self.nombre}.")

    # Método para mostrar todos los libros del autor
    def mostrar_libros(self):
        # Muestra la lista de libros del autor.
        # Si el autor tiene libros en la lista, los mostramos
        if self.libros:
            print(f"Libros escritos por {self.nombre}:")
            for libro in self.libros:
                # Mostramos el título, ISBN y género de cada libro en la lista
                print(f"- {libro.titulo} (ISBN: {libro.isbn}, Género: {libro.genero})")
        else:
            # Si el autor no tiene libros, mostramos un mensaje diciendo que no ha escrito nada
            print(f"{self.nombre} no ha escrito ningún libro.")

# Definimos la clase Libro, que representa a un libro
class Libro:
    # El método __init__ es el constructor de la clase, se ejecuta cuando creamos un nuevo libro
    def __init__(self, titulo, genero, isbn, autor):
        self.titulo = titulo  # Guardamos el título del libro
        self.genero = genero  # Guardamos el género del libro
        self.isbn = isbn  # Guardamos el ISBN del libro (un identificador único)
        self.autor = autor  # Guardamos la referencia al autor que escribió el libro
        autor.agregar_libro(self)  # Llamamos al método 'agregar_libro' del autor para agregar este libro a su lista

# Ejemplo de uso:

# Creamos un autor con el nombre 'Paulo Coelho'
autor = Autor("Paulo Coelho")

# Creamos dos libros, pasando el autor como parámetro para asignarlo al autor
libro1 = Libro("El Alquimista", "Novela", "978-3-16-148410-0", autor)
libro2 = Libro("Adulterio", "Novela", "978-3-16-148411-7", autor)

# Mostramos los libros que tiene el autor
autor.mostrar_libros()

# Eliminamos un libro de la lista de libros del autor
autor.eliminar_libro(libro1)

# Mostramos nuevamente los libros que tiene el autor después de la eliminación
autor.mostrar_libros()