# Supón que estás desarrollando un juego de video con distintos tipos 
# de personajes y armas. 
# Los requerimientos cambian con frecuencia, añadiendo nuevos personajes y 
# habilidades. 
# Mantener y actualizar TADs en este escenario podría ser una tarea titánica.

# Definimos una clase base para las Armas 
class Arma:
    def __init__(self, nombre, dano):
        """Inicializa el arma con un nombre y un daño."""
        self.nombre = nombre  # Nombre del arma (Ej. "Espada", "Bastón Mágico")
        self.dano = dano      # Daño que causa el arma (Ej. 15, 20)

    def atacar(self):
        """Método que simula un ataque con el arma."""
        return self.dano  # Devuelve el daño del ataque (esto es lo que hace el arma al atacar)


# Definimos una clase base para los Personajes
class Personaje:
    def __init__(self, nombre, vida):
# Inicializa el personaje con un nombre y una cantidad de vida.
        self.nombre = nombre  # Nombre del personaje 
        self.vida = vida    # Vida del personaje (la cantidad de vida que tiene)
        self.arma = None      # Inicialmente, el personaje no tiene arma

    def equipar_arma(self, arma):
# Permite al personaje equipar un arma.
        self.arma = arma  # Asigna el arma que recibe al personaje

    def atacar(self):
# Método que permite al personaje atacar.
        if self.arma:  # Verifica si el personaje tiene un arma
            return self.arma.atacar()  # Si tiene arma, devuelve el daño de esa arma
        else:
            return 0  # Si no tiene arma, el daño es 0 (no puede atacar)

    def recibir_dano(self, dano):
# Método que permite al personaje recibir daño.
        self.vida -= dano  # Reduce la vida del personaje con el daño recibido
        if self.vida < 0:  # Si la vida es menor que 0, establecemos la vida en 0
            self.vida = 0

    def esta_vivo(self):
# Verifica si el personaje está vivo.
        return self.vida > 0  # Devuelve True si la vida es mayor que 0, es decir, el personaje está vivo


# Definimos una clase para un tipo específico de personaje: Guerrero
class Guerrero(Personaje):
    def __init__(self, nombre):
#Inicia un Guerrero con un nombre y vida específica.
        super().__init__(nombre, vida=100)  # Llama al constructor de la clase base con vida 100
        self.arma = Arma("Espada", 15)  # Equipamos al Guerrero con una espada que causa 15 de daño


# Definimos una clase para otro tipo de personaje: Mago
class Mago(Personaje):
    def __init__(self, nombre):
# Inicia un Mago con un nombre y vida específica.
        super().__init__(nombre, vida=80)  # Llama al constructor de la clase base con vida 80
        self.arma = Arma("Bastón Mágico", 20)  # Equipamos al Mago con un bastón mágico que causa 20 de daño


# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Creamos un Guerrero y un Mago
    guerrero = Guerrero("Guerrero")  # Creamos un objeto Guerrero llamado "Guerrero"
    mago = Mago("Mago")  # Creamos un objeto Mago llamado "Mago"

    # Mostramos la vida inicial de los personajes
    print(f"{guerrero.nombre} tiene {guerrero.vida} vidas.")  # Muestra la vida del Guerrero
    print(f"{mago.nombre} tiene {mago.vida} vidas.")  # Muestra la vida del Mago

    # El Guerrero ataca al Mago
    dano_atacado = guerrero.atacar()  # El Guerrero ataca usando su espada
    print(f"{guerrero.nombre} ataca a {mago.nombre} causando {dano_atacado} de daño.")  # Muestra el daño causado
    mago.recibir_dano(dano_atacado)  # El Mago recibe el daño del Guerrero

    # Mostramos la vida del Mago después del ataque
    print(f"{mago.nombre} ahora tiene {mago.vida} vidas.")  # Muestra la nueva vida del Mago

    # El Mago ataca al Guerrero
    dano_atacado = mago.atacar()  # El Mago ataca usando su bastón mágico
    print(f"{mago.nombre} ataca a {guerrero.nombre} causando {dano_atacado} de daño.")  # Muestra el daño causado
    guerrero.recibir_dano(dano_atacado)  # El Guerrero recibe el daño del Mago

    # Mostramos la vida del Guerrero después del ataque
    print(f"{guerrero.nombre} ahora tiene {guerrero.vida} vidas.")  # Muestra la nueva vida del Guerrero

    # Verificamos si los personajes están vivos
    print(f"{guerrero.nombre} está {'vivo' if guerrero.esta_vivo() else 'muerto'}.")  # Verifica si el Guerrero está vivo
    print(f"{mago.nombre} está {'vivo' if mago.esta_vivo() else 'muerto'}.")  # Verifica si el Mago está vivo
