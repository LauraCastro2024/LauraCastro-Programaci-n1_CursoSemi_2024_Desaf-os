# Imagina un sistema de gestión de biblioteca que maneja libros, 
# usuarios, préstamos y multas. 
# Usar TADs separados para cada uno de estos elementos 
# podría complicar la interacción y gestión de relaciones entre ellos.


# Definimos la clase Libro para representar un libro en la biblioteca
class Libro:
    def __init__(self, titulo, autor, isbn):
        # Se inician los atributos del libro
        self.titulo = titulo  # Título del libro
        self.autor = autor    # Autor del libro
        self.isbn = isbn      # ISBN del libro (un identificador único)
        self.prestado = False # Inicialmente, el libro no está prestado

    def __str__(self):
        # Este método devuelve una cadena de texto para representar el libro
        # Mostramos el título, autor, ISBN y si el libro está prestado o disponible
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn}) - {'Prestado' if self.prestado else 'Disponible'}"


# Definimos la clase Usuario para representar a un usuario de la biblioteca
class Usuario:
    def __init__(self, nombre, id_usuario):
        # Constructor: se inicializan los atributos del usuario
        self.nombre = nombre  # Nombre del usuario
        self.id_usuario = id_usuario  # ID único del usuario
        self.prestamos = []  # Lista para guardar los préstamos realizados por el usuario

    def __str__(self):
# Este método devuelve una cadena de texto para representar al usuario
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


# Definimos la clase Prestamo para representar un préstamo de un libro a un usuario
class Prestamo:
    def __init__(self, libro, usuario):
# Se asocia un libro y un usuario al préstamo
        self.libro = libro  # El libro prestado
        self.usuario = usuario  # El usuario que hace el préstamo
        self.libro.prestado = True  # Marcamos el libro como prestado
        self.usuario.prestamos.append(self)  # Agregamos el préstamo a la lista de préstamos del usuario

    def devolver(self):
# Este método se llama para devolver el libro
        self.libro.prestado = False  # Marcamos el libro como disponible nuevamente
        self.usuario.prestamos.remove(self)  # Eliminamos el préstamo de la lista de préstamos del usuario

    def __str__(self):
# Este método devuelve una cadena de texto para representar el préstamo
        return f"Préstamo: {self.libro.titulo} a {self.usuario.nombre}"

# Definimos la clase Biblioteca para gestionar los libros y usuarios
class Biblioteca:
    def __init__(self):
        # Constructor: inicializa las listas de libros y usuarios en la biblioteca
        self.libros = []  # Lista de libros disponibles en la biblioteca
        self.usuarios = []  # Lista de usuarios registrados en la biblioteca

    def agregar_libro(self, libro):
# Este método agrega un libro a la biblioteca
        self.libros.append(libro)

    def agregar_usuario(self, usuario):
# Este método agrega un usuario a la biblioteca
        self.usuarios.append(usuario)

    def prestar_libro(self, isbn, id_usuario):
# Este método gestiona el préstamo de un libro a un usuario
# Buscamos el libro por su ISBN que no esté prestado
        libro = next((libro for libro in self.libros if libro.isbn == isbn and not libro.prestado), None)
# Buscamos el usuario por su ID
        usuario = next((usuario for usuario in self.usuarios if usuario.id_usuario == id_usuario), None)

# Si encontramos tanto el libro como el usuario, realizamos el préstamo
        if libro and usuario:
            prestamo = Prestamo(libro, usuario)  # Creamos un objeto de préstamo
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
            return prestamo  # Retornamos el objeto de préstamo
        else:
# Si no encontramos el libro o el usuario, mostramos un mensaje de error
            print("No se pudo realizar el préstamo. Verifique el ISBN del libro o el ID del usuario.")
            return None

    def devolver_libro(self, prestamo):
        # Este método permite devolver un libro previamente prestado
        prestamo.devolver()  # Llamamos al método devolver() de la clase Prestamo
        print(f"Libro '{prestamo.libro.titulo}' devuelto por {prestamo.usuario.nombre}.")

    def mostrar_libros(self):
        # Este método muestra todos los libros disponibles en la biblioteca
        print("Libros en la biblioteca:")
        for libro in self.libros:
            print(libro)  # Usamos el método __str__ de la clase Libro

    def mostrar_usuarios(self):
        # Este método muestra todos los usuarios registrados en la biblioteca
        print("Usuarios registrados:")
        for usuario in self.usuarios:
            print(usuario)  # Usamos el método __str__ de la clase Usuario


# Ejemplo de uso del programa
if __name__ == "__main__":
    # Creamos una instancia de la clase Biblioteca
    biblioteca = Biblioteca()

    # Agregar libros a la biblioteca
    libro1 = Libro("El alquimista", "Paulo Coelho", "123456789") 
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "987654321")
    biblioteca.agregar_libro(libro1)  # Agregamos el libro "El alquimista"
    biblioteca.agregar_libro(libro2)  # Agregamos el libro "El Principito"

    # Agregar usuarios a la biblioteca
    usuario1 = Usuario("Maria", "U001")
    usuario2 = Usuario("Laura", "U002")
    biblioteca.agregar_usuario(usuario1)  # Agregamos al usuario María
    biblioteca.agregar_usuario(usuario2)  # Agregamos al usuario Laura

    # Mostrar los libros y usuarios registrados
    biblioteca.mostrar_libros()
    biblioteca.mostrar_usuarios()

    # Realizar un préstamo de un libro
    prestamo1 = biblioteca.prestar_libro("123456789", "U001")  # María pide el libro con ISBN "123456789"

    # Mostrar el estado de los libros después del préstamo
    biblioteca.mostrar_libros()

    # Devolver el libro prestado
    if prestamo1:
        biblioteca.devolver_libro(prestamo1)

    # Mostrar el estado de los libros después de la devolución
    biblioteca.mostrar_libros()
