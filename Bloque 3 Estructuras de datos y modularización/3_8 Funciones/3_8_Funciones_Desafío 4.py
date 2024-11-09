 # Algoritmo MCD El Máximo Común Divisor (MCD) es un concepto matemático 
# que ha sido estudiado desde tiempos antiguos. 
# Atribuido a Euclides, el algoritmo para determinarlo es elegante y eficiente. 
# Tu tarea es implementar una función que calcule el MCD de dos 
# números utilizando el algoritmo de Euclides.

def mcd(a, b):
# Calcula el Máximo Común Divisor (MCD) de dos números utilizando el 
# algoritmo de Euclides.

    while b != 0:  # Mientras b no sea cero, continuamos con el algoritmo
        a, b = b, a % b  # Actualiza a con el valor de b, y b con el resto de a dividido por b
    return a  # Cuando b es cero, a contiene el MCD

# Ejemplo de uso
numero1 = 48  # Primer número para calcular el MCD
numero2 = 18  # Segundo número para calcular el MCD
resultado = mcd(numero1, numero2)  # Llama a la función mcd con los dos números

# Imprimir el resultado
print(f"El MCD de {numero1} y {numero2} es: {resultado}")  # Muestra el resultado del cálculo del MCD

def mcd(a, b):
# Calcula el Máximo Común Divisor (MCD) de dos números utilizando el 
# algoritmo de Euclides.
    while b != 0:  # Mientras b no sea cero, continuamos con el algoritmo
        a, b = b, a % b  # Actualiza a con el valor de b, y b con el resto de a dividido por b
    return a  # Cuando b es cero, a contiene el MCD

# Ejemplo de uso
numero1 = 48  # Primer número para calcular el MCD
numero2 = 18  # Segundo número para calcular el MCD
resultado = mcd(numero1, numero2)  # Llama a la función mcd con los dos números

# Imprimir el resultado
print(f"El MCD de {numero1} y {numero2} es: {resultado}")  # Muestra el resultado del cálculo del MCD