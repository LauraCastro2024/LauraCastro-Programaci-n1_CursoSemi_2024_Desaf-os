# Clase que representa a un Autor
class Autor:
    # El método __init__ es el constructor que se ejecuta cuando creamos un nuevo objeto Autor
    def __init__(self, nombre):
        self.nombre = nombre  # Guardamos el nombre del autor en el atributo 'nombre'
        self.libros = []  # Inicializamos una lista vacía llamada 'libros' para almacenar los libros del autor

    # Método para agregar un libro a la lista de libros del autor
    def agregar_libro(self, libro):
        # Agrega un libro a la lista de libros del autor.
        if libro not in self.libros:  # Verificamos si el libro no está ya en la lista
            self.libros.append(libro)  # Si no está, lo agregamos a la lista

    # Método para mostrar todos los libros del autor
    def mostrar_libros(self):
        # Muestra la lista de libros del autor.
        if self.libros:  # Si la lista de libros no está vacía
            print(f"Libros escritos por {self.nombre}:")
            for libro in self.libros:  # Recorremos la lista de libros
                # Mostramos el título, ISBN y género de cada libro
                print(f"- {libro.titulo} (ISBN: {libro.isbn}, Género: {libro.genero})")
        else:
            # Si no tiene libros, mostramos un mensaje indicando que el autor no ha escrito nada
            print(f"{self.nombre} no ha escrito ningún libro.")

# Clase que representa un Libro
class Libro:
    # El método __init__ es el constructor que se ejecuta cuando creamos un nuevo objeto Libro
    def __init__(self, titulo, genero, isbn, autor):
        self.titulo = titulo  # Guardamos el título del libro
        self.genero = genero  # Guardamos el género del libro
        self.isbn = isbn  # Guardamos el ISBN del libro
        self.autor = autor  # Guardamos el autor del libro (referencia al objeto Autor)
        autor.agregar_libro(self)  # Llamamos al método 'agregar_libro' del autor para agregar este libro a su lista

# Clase que representa la Biblioteca
class Biblioteca:
    # El método __init__ es el constructor que se ejecuta cuando creamos un nuevo objeto Biblioteca
    def __init__(self):
        self.autores = []  # Inicializamos una lista vacía para almacenar autores
        self.libros = {}   # Inicializamos un diccionario vacío para almacenar libros, donde la clave será el ISBN

    # Método para agregar un autor a la biblioteca
    def agregar_autor(self, autor):
        # Agrega un autor a la biblioteca.
        if autor not in self.autores:  # Verificamos si el autor no está ya en la lista de autores
            self.autores.append(autor)  # Si no está, lo agregamos

    # Método para agregar un libro a la biblioteca y asociarlo a un autor
    def agregar_libro(self, titulo, genero, isbn, autor):
        # Agrega un libro a la biblioteca y lo asocia a un autor.
        libro = Libro(titulo, genero, isbn, autor)  # Creamos un objeto Libro
        self.libros[isbn] = libro  # Agregamos el libro al diccionario usando su ISBN como clave

    # Método para mostrar todos los autores de la biblioteca
    def mostrar_autores(self):
        # Muestra la lista de autores en la biblioteca.
        print("Autores en la biblioteca:")
        for autor in self.autores:  # Recorremos la lista de autores
            print(f"- {autor.nombre}")  # Mostramos el nombre de cada autor

    # Método para mostrar todos los libros de la biblioteca
    def mostrar_libros(self):
        # Muestra la lista de libros en la biblioteca.
        print("Libros en la biblioteca:")
        for libro in self.libros.values():  # Recorremos los valores (libros) del diccionario
            # Mostramos el título, ISBN, nombre del autor y género de cada libro
            print(f"- {libro.titulo} (ISBN: {libro.isbn}, Autor: {libro.autor.nombre}, Género: {libro.genero})")

# Ejemplo de uso:
# Creamos una instancia de la clase Biblioteca (es como si estuviéramos creando una biblioteca física)
biblioteca = Biblioteca()

# Creamos dos autores
autor1 = Autor("Paulo Coelho")  # Autor 1: Paulo Coelho
autor2 = Autor("J.K. Rowling")  # Autor 2: J.K. Rowling

# Agregamos los autores a la biblioteca
biblioteca.agregar_autor(autor1)
biblioteca.agregar_autor(autor2)

# Creamos libros y los agregamos a la biblioteca, asociándolos con los autores correspondientes
biblioteca.agregar_libro("El Alquimista", "Novela", "978-3-16-148410-0", autor1)
biblioteca.agregar_libro("Adulterio", "Novela", "978-3-16-148411-7", autor1)
biblioteca.agregar_libro("Harry Potter y la piedra filosofal", "Fantasía", "978-3-16-148412-4", autor2)

# Mostramos los autores de la biblioteca
biblioteca.mostrar_autores()

# Mostramos los libros de la biblioteca
biblioteca.mostrar_libros()