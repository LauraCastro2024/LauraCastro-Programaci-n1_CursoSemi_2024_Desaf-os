# Crea una excepción personalizada llamada NegativeNumberError 
# que se dispare si el usuario intenta ingresar un número negativo 
# en un programa de cálculo de raíces cuadradas. 
# Implementa el manejo de esta excepción en el programa.

# Definimos una excepción para números negativos
class NegativeNumberError(Exception):
    pass

try:
    # Solicitamos al usuario que ingrese un número y lo convertimos a float
    numero = float(input("Ingrese un número: "))
    
    # Si el número es negativo, lanzamos nuestra excepción
    if numero < 0:
        raise NegativeNumberError("No se permite un número negativo.")
    else:
        # Calculamos y mostramos la raíz cuadrada del número
        print(f"La raíz cuadrada de {numero} es {numero ** 0.5}")

# Imprimimos el error para números negativos
except NegativeNumberError as e:
    print(f"Error: {e}")