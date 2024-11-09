# Crea una función recursiva que calcule el máximo común divisor (MCD) 
# de dos números. 
# El MCD de dos números es el número más grande que puede dividir 
# ambos números sin dejar un residuo. 
# Por ejemplo, el MCD de 8 y 12 es 4.
# Pista: Puedes usar el algoritmo de Euclides, que establece que 
# el MCD de dos números también divide al residuo de su división. 
# Por lo tanto, el MCD de a y b (donde a > b) es el mismo que el MCD 
# de b y a % b.


# Definimos una función recursiva para calcular el MCD (Máximo Común Divisor) de dos números
def mcd(a, b):
    # Caso base: si b es 0, el MCD es a
    # Esto se debe a que el MCD de un número y 0 es el número mismo.
    if b == 0:
        return a
    # Caso recursivo: llama a la función con (b, a % b)
    # La operación 'a % b' devuelve el residuo de dividir 'a' entre 'b'.
    # La función se llama a sí misma con los nuevos valores (b, a % b) hasta llegar al caso base (cuando b sea 0).
    else:
        return mcd(b, a % b)  # Se llama a sí misma con los nuevos valores

# Ejemplo de uso de la función mcd:
# Imprimimos el resultado de calcular el MCD de dos números

print(mcd(8, 12))  # Debería imprimir 4, ya que el MCD de 8 y 12 es 4
print(mcd(48, 18))  # Debería imprimir 6, ya que el MCD de 48 y 18 es 6
