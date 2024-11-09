# Escribe una función que calcule el factorial de un número entero positivo. 
# Maneja las excepciones si el número ingresado es negativo, no es entero,
# o es demasiado grande para ser procesado.

import math  # Importamos la librería math para usar la función factorial

def calcular_factorial():
    try:
        # Solicitamos al usuario que ingrese un número y lo convertimos a entero
        numero = int(input("Ingrese un número entero positivo: "))
        
        # Si el número es negativo, lanzamos un error
        if numero < 0:
            raise ValueError("El número no puede ser negativo.")

        # Calculamos el factorial y lo imprimimos
        resultado = math.factorial(numero)
        print(f"El factorial de {numero} es {resultado}")

    # Capturamos errores de valor incorrecto o negativo
    except ValueError as ve:
        print(f"Error: {ve}")

    # Capturamos el error si el número es muy grande para calcular su factorial
    except OverflowError:
        print("Error: El número es demasiado grande para calcular su factorial.")

# Llamamos a la función para que se ejecute
calcular_factorial()