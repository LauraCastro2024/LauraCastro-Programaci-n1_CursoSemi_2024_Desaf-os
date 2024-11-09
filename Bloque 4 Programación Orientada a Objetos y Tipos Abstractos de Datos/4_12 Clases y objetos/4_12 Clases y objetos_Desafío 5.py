

# Definimos la clase Libro para representar un libro en la biblioteca
class Libro:
    def __init__(self, titulo, autor, isbn):
        # Inicializamos un libro con título, autor e ISBN
        self.titulo = titulo  # Título del libro
        self.autor = autor    # Autor del libro
        self.isbn = isbn      # ISBN del libro (un identificador único)

    def __str__(self):
        # Este método devuelve una cadena con la información del libro
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn})"


# Definimos la clase Biblioteca para representar una biblioteca
class Biblioteca:
    def __init__(self):
        # Inicializamos la biblioteca con una lista vacía de libros
        self.libros = []  # Lista de libros en la biblioteca

    def agregar_libro(self, libro):
        # Este método agrega un libro a la lista de libros de la biblioteca
        self.libros.append(libro)  # Añadimos el libro a la lista

    def buscar_libro_por_titulo(self, titulo):
        # Busca libros por título (ignora mayúsculas y minúsculas)."""
        # Este método busca libros cuyo título contenga el texto dado
        # Utilizamos una lista por comprensión para filtrar los libros que coincidan
        resultados = [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]
        return resultados  # Devolvemos la lista de resultados encontrados

    def buscar_libro_por_autor(self, autor):
        # Busca libros por autor (ignora mayúsculas y minúsculas)."""
        # Este método busca libros cuyo autor contenga el texto dado
        # Utilizamos una lista por comprensión para filtrar los libros que coincidan
        resultados = [libro for libro in self.libros if autor.lower() in libro.autor.lower()]
        return resultados  # Devolvemos la lista de resultados encontrados

    def mostrar_resultados(self, resultados):
        # Muestra los resultados de la búsqueda.
        # Este método muestra los resultados de la búsqueda
        if resultados:  # Si hay resultados encontrados
            print("Resultados de la búsqueda:")  # Imprime un encabezado
            for libro in resultados:  # Para cada libro en los resultados
                print(libro)  # Imprime el libro
        else:
            print("No se encontraron resultados.")  # Si no hay resultados, imprime este mensaje


# Ejemplo de uso del código
if __name__ == "__main__":
    # Creamos una instancia de la biblioteca
    biblioteca = Biblioteca()

    # Agregamos algunos libros a la biblioteca
    biblioteca.agregar_libro(Libro("1984", "George Orwell", "123456789"))
    biblioteca.agregar_libro(Libro("El Principito", "Antoine de Saint-Exupéry", "987654321"))
    biblioteca.agregar_libro(Libro("Rebelión en la granja", "George Orwell", "123456788"))

    # Buscamos libros por título
    titulo_busqueda = "1984"  # Título a buscar
    resultados_titulo = biblioteca.buscar_libro_por_titulo(titulo_busqueda)  # Llamamos al método de búsqueda por título
    biblioteca.mostrar_resultados(resultados_titulo)  # Mostramos los resultados de la búsqueda por título

    # Buscamos libros por autor
    autor_busqueda = "George Orwell"  # Autor a buscar
    resultados_autor = biblioteca.buscar_libro_por_autor(autor_busqueda)  # Llamamos al método de búsqueda por autor
    biblioteca.mostrar_resultados(resultados_autor)  # Mostramos los resultados de la búsqueda por autor
