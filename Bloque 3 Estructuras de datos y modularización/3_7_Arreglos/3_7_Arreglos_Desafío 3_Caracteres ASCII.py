# Eres un desarrollador creando una herramienta educativa que muestra 
# los caracteres ASCII correspondientes a una lista de números. 
# Se recomienda usar la función chr() para convertir los números en caracteres.

def mostrar_ascii(numeros):
    # Imprime la cabecera de la tabla que mostrará los números y sus caracteres ASCII
    print("\nNúmero | Carácter ASCII")
    print("---------------------")
    # Recorre cada número en la lista de números
    for numero in numeros:
        try:
            # Intenta convertir el número a su carácter ASCII correspondiente
            caracter = chr(numero)
            # Imprime el número y su carácter ASCII
            print(f"{numero:6d} | {caracter}")
        except ValueError:
            # Si el número está fuera del rango de valores ASCII, se maneja la excepción
            print(f"{numero:6d} | Fuera de rango")

def obtener_numeros():
    numeros = []  # Lista para almacenar los números ingresados
    print("Ingrese los números ASCII (0-127). Ingrese un número negativo para terminar.")
    # Bucle que permite al usuario ingresar números hasta que ingrese un negativo
    while True:
        try:
            # Solicita al usuario que ingrese un número
            numero = int(input("Ingrese un número: "))
            if numero < 0:
                break  # Sale del bucle si el número es negativo
            numeros.append(numero)  # Agrega el número a la lista
        except ValueError:
            # Maneja la excepción si el ingreso no es un número válido
            print("Por favor, ingrese un número válido.")
    return numeros  # Devuelve la lista de números ingresados

def main():
    # Mensaje de bienvenida al programa
    print("Bienvenido a la herramienta educativa de caracteres ASCII")
    numeros = obtener_numeros()  # Llama a la función para obtener números del usuario
    mostrar_ascii(numeros)  # Llama a la función para mostrar los números y sus caracteres ASCII

# Comprobar si el script se está ejecutando directamente
if __name__ == "__main__":
    main()  # Llama a la función principal para iniciar el programa