# Clase que representa un libro
class Libro:
    # (__init__) se ejecuta cuando se crea un nuevo objeto de la clase Libro
    def __init__(self, titulo, autor, isbn):
        self._titulo = titulo  # Atributo privado para almacenar el título del libro
        self._autor = autor    # Atributo privado para almacenar el autor del libro
        self._isbn = isbn      # Atributo privado para almacenar el ISBN del libro

    # Métodos getter: Nos permite acceder a los atributos privados (de forma controlada)

    # Método getter para obtener el título del libro
    @property
    def titulo(self):
        return self._titulo  # Retorna el título almacenado en el atributo privado _titulo

    # Método getter para obtener el autor del libro
    @property
    def autor(self):
        return self._autor  # Retorna el autor almacenado en el atributo privado _autor

    # Método getter para obtener el ISBN del libro
    @property
    def isbn(self):
        return self._isbn  # Retorna el ISBN almacenado en el atributo privado _isbn

    # Métodos setter: Nos permiten modificar los atributos privados de manera controlada

    # Método setter para establecer o modificar el título del libro
    @titulo.setter
    def titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo  # Asigna el nuevo valor al atributo privado _titulo

    # Método setter para establecer o modificar el autor del libro
    @autor.setter
    def autor(self, nuevo_autor):
        self._autor = nuevo_autor  # Asigna el nuevo valor al atributo privado _autor

    # Método setter para establecer o modificar el ISBN del libro
    @isbn.setter
    def isbn(self, nuevo_isbn):
        self._isbn = nuevo_isbn  # Asigna el nuevo valor al atributo privado _isbn

# Ejemplo de uso de la clase Libro:
# Creamos un objeto de la clase Libro con un título, autor e ISBN iniciales
libro = Libro("Cien años de soledad", "Gabriel García Márquez", "978-3-16-148410-0")

# Accedemos a los atributos del libro usando los métodos getter
# Los getters nos permiten acceder a los atributos privados de manera segura
print(f"Título: {libro.titulo}")   # Accedemos al título
print(f"Autor: {libro.autor}")     # Accedemos al autor
print(f"ISBN: {libro.isbn}")       # Accedemos al ISBN

# Modificamos los atributos del libro usando los métodos setter
# Los setters nos permiten cambiar los valores de los atributos privados
libro.titulo = "El otoño del patriarca"  # Cambiamos el título del libro
libro.autor = "Gabriel García Márquez"   # Cambiamos el autor del libro
libro.isbn = "978-3-16-148411-7"        # Cambiamos el ISBN del libro

# Accedemos a los atributos modificados usando los getters
print(f"Título modificado: {libro.titulo}")  # Mostramos el nuevo título
print(f"Autor modificado: {libro.autor}")    # Mostramos el nuevo autor
print(f"ISBN modificado: {libro.isbn}")      # Mostramos el nuevo ISBN