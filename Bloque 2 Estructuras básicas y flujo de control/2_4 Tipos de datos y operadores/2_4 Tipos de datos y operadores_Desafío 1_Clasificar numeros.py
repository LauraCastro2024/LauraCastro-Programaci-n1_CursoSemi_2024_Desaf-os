#Determinar las variables
a = 5   # Asignamos el valor 5 a la variable 'a'
b = 27  # Asignamos el valor 27 a la variable 'b'
c = 73  # Asignamos el valor 73 a la variable 'c'

# Comprobar si a es menor que b y si b es menor que c
condición_encadenada = a < b < c  # Verifica si a es menor que b y b es menor que c
print("Comparacion encadenada (a < b < c):", condición_encadenada)  # Imprime el resultado de la comparación encadenada

# Comprobar si a es mayor que b o si b es mayor que c
condición_encadenada = a > b > c  # Verifica si a es mayor que b y b es mayor que c en una sola expresión
print("Comparacion encadenada (a > b > c):", condición_encadenada)  # Imprime el resultado de la comparación encadenada

# Comprobar si a es igual que b o si b es diferente que c
condición_encadenada = a == b != c  # Verifica si a es igual a b y b es diferente de c
print("Comparacion encadenada (a == b != c):", condición_encadenada)  # Imprime el resultado de la comparación encadenada

# Comprobar si a es menor que b y b es menor que c
condición1 = a < b and b < c  # Verifica si a es menor que b y b es menor que c usando el operador lógico 'and'
print("condición 1 (a < b y b < c):", condición1)  # Imprime el resultado de la condición

# Comprobar si a es igual a b o si b es igual a c
condición2 = a == b or b == c  # Verifica si a es igual a b o b es igual a c usando el operador lógico 'or'
print("condición 2 (a == b o b == c):", condición2)  # Imprime el resultado de la condición

# Negar la condición
condición3 = not condición1  # Invierte el valor de 'condición1' usando el operador lógico 'not'
print("condición 3 (not condición1):", condición3)  # Imprime el resultado de la condición negada