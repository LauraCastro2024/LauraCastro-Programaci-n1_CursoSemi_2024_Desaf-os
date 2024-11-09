# Piensa en otros atributos y 
# métodos que podrías agregar a la clase Autor para hacerla más completa.


# Clase que representa a un Autor
class Autor:
    # (__init__) se ejecuta cuando se crea un nuevo objeto Autor
    def __init__(self, nombre, fecha_nacimiento, nacionalidad, biografia=""):
        self.nombre = nombre  # Guardamos el nombre del autor
        self.fecha_nacimiento = fecha_nacimiento  # Guardamos la fecha de nacimiento
        self.nacionalidad = nacionalidad  # Guardamos la nacionalidad del autor
        self.biografia = biografia  # Guardamos la biografía, por defecto está vacía si no se proporciona
        self.libros = []  # Lista vacía para almacenar los libros escritos por el autor
        self.premios = []  # Lista vacía para almacenar los premios ganados por el autor

    # Método para agregar un libro a la lista de libros del autor
    def agregar_libro(self, libro):
        #Agrega un libro a la lista de libros del autor.
        if libro not in self.libros:  # Verificamos si el libro ya no está en la lista
            self.libros.append(libro)  # Si no está, lo agregamos a la lista

    # Método para eliminar un libro de la lista de libros del autor
    def eliminar_libro(self, libro):
        # Elimina un libro de la lista de libros del autor.
        if libro in self.libros:  # Verificamos si el libro está en la lista
            self.libros.remove(libro)  # Si está, lo eliminamos de la lista

    # Método para agregar un premio a la lista de premios del autor
    def agregar_premio(self, premio):
        # Agrega un premio a la lista de premios del autor.
        if premio not in self.premios:  # Verificamos si el premio ya no está en la lista
            self.premios.append(premio)  # Si no está, lo agregamos a la lista

    # Método para eliminar un premio de la lista de premios del autor
    def eliminar_premio(self, premio):
        # Elimina un premio de la lista de premios del autor.
        if premio in self.premios:  # Verificamos si el premio está en la lista
            self.premios.remove(premio)  # Si está, lo eliminamos de la lista

    # Método para mostrar toda la información del autor (nombre, fecha de nacimiento, etc.)
    def mostrar_informacion(self):
        # Muestra la información completa del autor.
        # Mostramos información básica del autor
        print(f"Nombre: {self.nombre}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Biografía: {self.biografia}")
        # Mostramos los premios, si existen
        print(f"Premios: {', '.join(self.premios) if self.premios else 'Ninguno'}")
        self.mostrar_libros()  # Llamamos a 'mostrar_libros' para mostrar los libros del autor

    # Método para mostrar la lista de libros escritos por el autor
    def mostrar_libros(self):
        # Muestra la lista de libros del autor.
        if self.libros:  # Si la lista de libros no está vacía
            print(f"Libros escritos por {self.nombre}:")
            for libro in self.libros:  # Recorremos cada libro en la lista
                # Mostramos el título, ISBN y género del libro
                print(f"- {libro.titulo} (ISBN: {libro.isbn}, Género: {libro.genero})")
        else:
            # Si no tiene libros, mostramos un mensaje indicando que no tiene ninguno
            print(f"{self.nombre} no ha escrito ningún libro.")

    # Método que devuelve la cantidad de libros escritos por el autor
    def contar_libros(self):
        # Devuelve el número total de libros escritos por el autor.
        return len(self.libros)  # Retornamos el tamaño de la lista de libros

# Ejemplo de uso:
# Creamos un objeto de la clase Autor con nombre, fecha de nacimiento, nacionalidad y biografía
autor = Autor("Gabriel García Márquez", "1927-03-06", "Colombiano", "Escritor y periodista colombiano.")
# Agregamos premios al autor
autor.agregar_premio("Premio Nobel de Literatura")
autor.agregar_premio("Premio Neustadt de Literatura")

# Suponemos que la clase Libro ya está definida (la clase Libro debe existir previamente para esto funcione)
libro1 = Libro("Cien años de soledad", "Novela", "978-3-16-148410-0", autor)
libro2 = Libro("El otoño del patriarca", "Novela", "978-3-16-148411-7", autor)

# Mostrar toda la información del autor
autor.mostrar_informacion()

# Mostrar cuántos libros ha publicado el autor
print(f"Número de libros publicados: {autor.contar_libros()}")