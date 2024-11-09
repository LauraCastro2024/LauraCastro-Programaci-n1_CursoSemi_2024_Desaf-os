# Vas a simular una carrera de autos. 
# Cada auto tiene una velocidad aleatoria (puedes usar la biblioteca 
# random de Python) y cada ciclo del bucle representa un segundo de la carrera. 
# Al final de cada segundo, cada auto avanza una distancia igual a su velocidad.
# La carrera dura 10 segundos. Al final de la carrera, debes imprimir el auto 
# ganador. Si hay un empate, debes imprimir todos los autos que empataron. 
# Nota: Este desafío puede requerir que aprendas sobre conceptos adicionales, 
# por ejemplo cómo generar números aleatorios.

import random  # Importamos el módulo random para generar números aleatorios

# Definimos la clase Auto
class Auto:
    def __init__(self, nombre):
# Clase auto. Inicia el nombre, la velocidad y la distancia del auto.
        self.nombre = nombre  # Nombre del auto
        self.velocidad = random.randint(1, 20)  # Asigna una velocidad aleatoria entre 1 y 20
        self.distancia = 0  # Inicia la distancia recorrida en 0

    def avanzar(self):
# Método para avanzar el auto en función de su velocidad actual
        self.distancia += self.velocidad  # Incrementa la distancia acumulada por la velocidad

# Función para simular la carrera entre los autos
def simular_carrera(autos, duracion):
# La carrera se ejecuta por la cantidad de segundos especificada en "duracion"
    for segundo in range(duracion):
        print(f"Segundo {segundo + 1}:")  # Imprime el segundo actual de la carrera
        for auto in autos:
            auto.avanzar()  # Cada auto avanza una cantidad de unidades igual a su velocidad
            print(f"{auto.nombre} avanza {auto.velocidad} unidades. Distancia total: {auto.distancia}")
        print("-" * 30)  # Línea divisoria para mejor visualización de cada segundo

# Determinar el ganador
    max_distancia = max(auto.distancia for auto in autos)  # Encuentra la distancia máxima alcanzada por los autos
    ganadores = [auto.nombre for auto in autos if auto.distancia == max_distancia]  # Lista de autos que lograron la distancia máxima

    return ganadores, max_distancia  # Devuelve los ganadores y la distancia máxima alcanzada

# Lista de nombres de los autos participantes en la carrera
nombres_autos = ["Auto 1", "Auto 2", "Auto 3", "Auto 4", "Auto 5"]
autos = [Auto(nombre) for nombre in nombres_autos]  # Crea una instancia de Auto para cada nombre

# Configuración de la carrera
duracion_carrera = 10  # Duración de la carrera en segundos
ganadores, distancia_ganadora = simular_carrera(autos, duracion_carrera)  # Ejecuta la simulación

# Imprimimos el resultado final de la carrera
if len(ganadores) == 1:
    print(f"El ganador es: {ganadores[0]} con una distancia de {distancia_ganadora} unidades.")
else:
    print(f"Los ganadores son: {', '.join(ganadores)} con una distancia de {distancia_ganadora} unidades.")
