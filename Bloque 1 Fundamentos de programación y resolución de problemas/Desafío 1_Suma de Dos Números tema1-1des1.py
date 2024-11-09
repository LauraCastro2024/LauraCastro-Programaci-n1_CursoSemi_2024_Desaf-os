# Objetivo: Crear un programa que sume dos números predefinidos 
# y muestre el resultado. 

# Paso 1: Definir dos variables
# Se define una función llamada sumar que recibe dos parámetros, a y b. 
# Las funciones permiten reutilizar el código y encapsular operaciones. 
# En este caso, se define una función que tomará dos números (variables a, b)
# para sumarlos.
def sumar(a, b):
    # Paso 2: Sumar los dos números y almacenar el resultado en una tercera variable
    return a + b  # Esta línea suma los dos números a y b, y luego devuelve 
                   # el resultado de la suma. La palabra return permite que el 
                   # resultado se devuelva desde la función para poder usarlo 
                   # en otras partes del programa.

# Se definen dos números específicos
numero1 = 475  # Primer número
numero2 = 863  # Segundo número

# Se llama a la función sumar con los valores numero1 y numero2. 
# Esos valores reemplazan a las variables a y b dentro de la función. 
# El resultado de la suma se almacena en la variable resultado.
resultado = sumar(numero1, numero2)

# Paso 3: Mostrar el resultado de la suma
print("El resultado de la suma es:", resultado)  # Esta línea utiliza la función print() 
                                                  # para mostrar el resultado en la pantalla. 
                                                  # Combina un texto (el mensaje "El resultado de la suma es:") 
                                                  # con el valor almacenado en la variable resultado, 
                                                  # que es el valor devuelto por la función sumar.