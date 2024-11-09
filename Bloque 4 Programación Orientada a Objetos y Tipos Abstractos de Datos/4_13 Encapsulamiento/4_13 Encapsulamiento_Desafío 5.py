
# Clase Autor que representa a un autor de libros
class Autor:
    # (__init__) se ejecuta cuando creamos un objeto de la clase Autor
    def __init__(self, nombre, fecha_nacimiento, nacionalidad, biografia=""):
        # Iniciamos los atributos del autor con los valores proporcionados
        self._nombre = nombre  # Nombre del autor (atributo privado)
        self._fecha_nacimiento = fecha_nacimiento  # Fecha de nacimiento del autor
        self._nacionalidad = nacionalidad  # Nacionalidad del autor (atributo privado)
        self.biografia = biografia  # Biografía del autor, valor por defecto es una cadena vacía
        self._libros = []  # Inicializamos una lista privada para almacenar los libros del autor

    # Método getter para obtener el nombre del autor
    @property
    def nombre(self):
        return self._nombre  # Devuelve el nombre del autor

    # Método getter para obtener la nacionalidad del autor
    @property
    def nacionalidad(self):
        return self._nacionalidad  # Devuelve la nacionalidad del autor

    # Método para agregar un libro a la lista de libros del autor
    def agregar_libro(self, libro):
        """Agrega un libro a la lista de libros del autor."""
        if libro not in self._libros:  # Verificamos si el libro no está ya en la lista
            self._libros.append(libro)  # Si no está, lo agregamos a la lista

    # Método para obtener la cantidad de libros que el autor ha escrito
    def cantidad_libros(self):
        """Devuelve la cantidad de libros escritos por el autor."""
        return len(self._libros)  # Devuelve el número de libros en la lista

    # Método para mostrar la información completa del autor
    def mostrar_informacion(self):
        """Muestra la información completa del autor."""
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Cantidad de libros: {self.cantidad_libros()}")  # Llamamos al método cantidad_libros para mostrar el número de libros

# Clase Libro para representar un libro, con un título, autor e ISBN
class Libro:
    # El constructor (__init__) se ejecuta cuando creamos un objeto de la clase Libro
    def __init__(self, titulo, autor, isbn):
        # Inicializamos los atributos del libro con los valores proporcionados
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

# Función que recibe una lista de autores y devuelve el autor con más libros
def autor_con_mas_libros(autores):
    """Devuelve el autor que ha escrito el mayor número de libros."""
    if not autores:  # Si la lista de autores está vacía
        return None  # Retorna None si no hay autores

    # Inicializamos el autor con más libros como el primer autor de la lista
    autor_max = autores[0]

    # Iteramos sobre la lista de autores
    for autor in autores:
        # Si el autor actual tiene más libros que el autor con más libros registrado
        if autor.cantidad_libros() > autor_max.cantidad_libros():
            autor_max = autor  # Actualizamos el autor con más libros

    return autor_max  # Devolvemos el autor con más libros

# Ejemplo de uso:

# Creamos tres autores con diferentes nombres, fechas de nacimiento y nacionalidades
autor1 = Autor("Gabriel García Márquez", "1927-03-06", "Colombiano")
autor2 = Autor("J.K. Rowling", "1965-07-31", "Británica")
autor3 = Autor("Isaac Asimov", "1920-01-02", "Americano")

# Creamos varios libros, asociando cada uno con un autor y un ISBN
libro1 = Libro("Cien años de soledad", autor1, "978-3-16-148410-0")
libro2 = Libro("El otoño del patriarca", autor1, "978-3-16-148411-7")
libro3 = Libro("Harry Potter y la piedra filosofal", autor2, "978-3-16-148412-4")
libro4 = Libro("Harry Potter y la cámara secreta", autor2, "978-3-16-148413-1")
libro5 = Libro("Fundación", autor3, "978-3-16-148414-8")

# Agregamos los libros a los autores correspondientes
autor1.agregar_libro(libro1)
autor1.agregar_libro(libro2)
autor2.agregar_libro(libro3)
autor2.agregar_libro(libro4)
autor3.agregar_libro(libro5)

# Creamos una lista de autores
lista_autores = [autor1, autor2, autor3]

# Usamos la función autor_con_mas_libros para encontrar al autor que ha escrito más libros
autor_mas_libros = autor_con_mas_libros(lista_autores)

# Si encontramos al autor con más libros, mostramos su información
if autor_mas_libros:
    print("\nAutor que ha escrito el mayor número de libros:")
    autor_mas_libros.mostrar_informacion()  # Mostramos la información del autor con más libros
else:
    print("No hay autores en la lista.")  # Si no hay autores en la lista, mostramos un mensaje