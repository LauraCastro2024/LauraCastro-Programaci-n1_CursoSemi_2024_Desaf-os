# Crea una función llamada es_palindromo que tome una una 
# cadena y devuelva true si es palindromo o false si no lo es.

def es_palindromo(cadena):
#Devuelve True si la cadena es un palíndromo, de lo contrario False.
    # Normalizamos la cadena: eliminamos espacios y convertimos a minúsculas
    cadena_normalizada = ''.join(cadena.split()).lower()  # Quita los espacios y convierte a minúsculas

    # Comparamos la cadena normalizada con su reverso
    return cadena_normalizada == cadena_normalizada[::-1]  # Retorna True si son iguales, indicando que es un palíndromo

# Ejemplo de uso
cadena1 = "Anita lava la tina"  # Cadena que se comprobará como palíndromo
cadena2 = "Hola mundo"  # Cadena que no es un palíndromo

resultado1 = es_palindromo(cadena1)  # Debe devolver True para cadena1
resultado2 = es_palindromo(cadena2)  # Debe devolver False para cadena2

# Imprimir los resultados
print(f"¿La cadena '{cadena1}' es un palíndromo?", resultado1)  # Muestra el resultado para cadena1
print(f"¿La cadena '{cadena2}' es un palíndromo?", resultado2)  # Muestra el resultado para cadena2