# Solicita al usuario dos números enteros e implementa un try-except 
# que maneje la división por cero y los valores no numéricos. 
# Muestra mensajes de error apropiados en cada caso.

try: # Se utiliza para intentar ejecutar el código que puede causar un error.
    # Solicitamos al usuario el primer número
    a = int(input("Ingrese el primer número: ")) # imput: Solicita una entrada del usuario
            # int(): Convierte la entrada a un número entero. Esto puede generar un Error si el usuario ingresa texto.

    # Solicitamos al usuario el segundo número
    b = int(input("Ingrese el segundo número: "))
    
    # Realizamos la división
    resultado = a / b # resultado = a / b: Realiza la división. Esto da un Error si b es 0.
    print(f"El resultado es: {resultado}")

# Si ocurre una división por cero, mostramos un mensaje específico
except ZeroDivisionError: # except ZeroDivisionError: Captura el error específico de división por cero y muestra un mensaje.
    print("Error: No se puede dividir por cero.")

# Si el valor ingresado no es un número, mostramos otro mensaje específico
except ValueError: # except ValueError: Captura el error de valor no numérico y muestra un mensaje.
    print("Error: Por favor ingrese un número válido.")