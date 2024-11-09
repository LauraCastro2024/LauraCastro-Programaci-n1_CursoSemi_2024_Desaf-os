# Desarrolla un programa que, dado un conjunto de tres números enteros 
# introducidos por el usuario, determine cuál de ellos es el mayor. 
# Considera la posibilidad de que algunos o todos los números sean iguales. 
# El programa debe imprimir un mensaje claro con el número mayor 
# o indicar si todos los números son iguales.
# Pedimos al usuario que introduzca tres números enteros
# Usamos una lista llamada numeros para almacenar los tres números 
# introducidos por el usuario. 
# Esto permite manejar una mejor forma los números.

numeros = []  # Inicializamos una lista vacía para almacenar los números

# Usamos un bucle para recibir tres números del usuario
# Usamos un bucle for para solicitar al usuario que ingrese tres números. 
# Esto evita la repetición de código y hace que la entrada sea más dinámica.
for i in range(3):
    numero = int(input(f"Introduce el número {i + 1}: "))  # Convertimos la entrada a entero
    numeros.append(numero)  # Añadimos el número a la lista

# Comparamos los números para encontrar el mayor
if numeros[0] == numeros[1] == numeros[2]:
    print("Todos los números son iguales.")
else:
    mayor = max(numeros)  # Usamos la función max para encontrar el mayor en la lista
    print(f"El número mayor es: {mayor}")  # Imprimimos el número mayor