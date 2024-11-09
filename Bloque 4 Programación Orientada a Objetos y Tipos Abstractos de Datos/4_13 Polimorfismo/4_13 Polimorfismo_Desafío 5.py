# Definimos la clase base Operacion
class Operacion:
    def resultado(self):
        # Método que debe ser sobrescrito por las subclases para calcular el resultado de la operación.
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")  ## Nos da un error si no se sobrescribe


# Definimos la subclase Suma que hereda de Operacion
class Suma(Operacion):
    def __init__(self, a, b):
        # Inicia la operación de suma con dos números.
        self.a = a  # Asigna el primer número al atributo de la instancia
        self.b = b  ## Asigna el segundo número al atributo de la instancia

    def resultado(self):
      # Calcula el resultado de la suma.
        return self.a + self.b  ## Devuelve la suma de a y b


# Definimos la subclase Multiplicacion que hereda de Operacion
class Multiplicacion(Operacion):
    def __init__(self, a, b):
        # Inicializa la operación de multiplicación con dos números.
        self.a = a  ## Asigna el primer número al atributo de la instancia
        self.b = b  ## Asigna el segundo número al atributo de la instancia

    def resultado(self):
        # Calcula el resultado de la multiplicación.
        return self.a * self.b  ## Devuelve el producto de a y b


# Ejemplo de uso del sistema
if __name__ == "__main__":
    ## Creamos una instancia de Suma con los números 5 y 3
    suma = Suma(5, 3)  ## Se crea un objeto de la clase Suma con los números 5 y 3
    print(f"El resultado de la suma es: {suma.resultado()}")  ## Imprimimos el resultado de la suma usando el método 'resultado'

    ## Creamos una instancia de Multiplicacion con los números 4 y 2
    multiplicacion = Multiplicacion(4, 2)  ## Se crea un objeto de la clase Multiplicacion con los números 4 y 2
    print(f"El resultado de la multiplicación es: {multiplicacion.resultado()}")  ## Imprimimos el resultado de la multiplicación usando el método 'resultado'
