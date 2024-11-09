import math  ## Importamos el módulo math para usar funciones matemáticas,como pi

# Definimos la clase base Figura
class Figura:
    def area(self):
        # Método que debe ser sobrescrito por las subclases para 
        # calcular el área.
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")  ## Lanza un error si no se sobrescribe


# Definimos la subclase Circulo que hereda de Figura
class Circulo(Figura):
    def __init__(self, radio):
        # Inicializa un círculo con un radio específico.
        self.radio = radio  # Asigna el valor del radio al atributo de la instancia

    def area(self):
        # Calcula el área del círculo.
        return math.pi * (self.radio ** 2)  # Devuelve el área usando la fórmula π * r^2


# Definimos la subclase Cuadrado que hereda de Figura
class Cuadrado(Figura):
    def __init__(self, lado):
        # Inicializa un cuadrado con un lado específico.
        self.lado = lado  ## Asigna el valor del lado al atributo de la instancia

    def area(self):
        # Calcula el área del cuadrado.
        return self.lado ** 2  ## Devuelve el área usando la fórmula lado^2


# Ejemplo de uso del sistema
if __name__ == "__main__":
    ## Creamos una instancia de Circulo con un radio de 5
    circulo = Circulo(5)  ## Se crea un objeto de tipo Circulo con radio 5
    print(f"El área del círculo es: {circulo.area()}")  ## Imprimimos el área del círculo usando el método 'area'

    ## Creamos una instancia de Cuadrado con un lado de 4
    cuadrado = Cuadrado(4)  ## Se crea un objeto de tipo Cuadrado con lado 4
    print(f"El área del cuadrado es: {cuadrado.area()}")  ## Imprimimos el área del cuadrado usando el método 'area'
