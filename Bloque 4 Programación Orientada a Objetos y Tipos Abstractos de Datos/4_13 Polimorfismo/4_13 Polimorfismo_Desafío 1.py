# Clase base Musico que representa a un músico en general
class Musico:
    def __init__(self, nombre):
        # Constructor que inicializa el nombre del músico.
        self.nombre = nombre  # Atributo que guarda el nombre del músico

    def instrumento(self):
        # Método que debe ser sobrescrito por las subclases.
        # Este método no hace nada aquí, solo lanza un error para que las subclases lo implementen
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases.")

# Clase Guitarrista que hereda de la clase Musico
class Guitarrista(Musico):
    def instrumento(self):
        # Implementa el método instrumento para el guitarrista.
        # Retorna una cadena indicando que el guitarrista toca la guitarra
        return f"{self.nombre} toca la guitarra."

# Clase Baterista que también hereda de la clase Musico
class Baterista(Musico):
    def instrumento(self):
        # Implementa el método instrumento para el baterista.
        # Retorna una cadena indicando que el baterista toca la batería
        return f"{self.nombre} toca la batería."

# Función para mostrar el instrumento que toca un músico
def mostrar_instrumento(musico):
    # Función que recibe un músico y muestra el instrumento que toca.
    # Llama al método instrumento del músico y lo imprime
    print(musico.instrumento())

# Ejemplo de uso:

# Creamos un objeto de la clase Guitarrista con el nombre "Carlos Santana"
guitarrista = Guitarrista("Carlos Santana")

# Creamos un objeto de la clase Baterista con el nombre "John Bonham"
baterista = Baterista("John Bonham")

# Demostrando polimorfismo:
# Llamamos a la función mostrar_instrumento pasando el guitarrista
# El resultado será que la función muestra que Carlos Santana toca la guitarra
mostrar_instrumento(guitarrista)  # Carlos Santana toca la guitarra.

# Llamamos a la función mostrar_instrumento pasando el baterista
# El resultado será que la función muestra que John Bonham toca la batería
mostrar_instrumento(baterista)     # John Bonham toca la batería.