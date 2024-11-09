# Tienes una lista de números en la que algunos elementos están repetidos. 
# Desarrolla un programa que elimine todos los elementos duplicados y 
# deje únicamente una aparición de cada uno. 
# La salida debe mostrar la lista original y la lista sin duplicados.

# Definimos una lista de números llamada 'numeros' que contiene algunos valores repetidos
# Esto es solo un ejemplo, pero podríamos tener cualquier tipo de valores en la lista
numeros = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8 ]

# Usamos set para eliminar los duplicados
# Esto no permite elementos repetidos, por lo que al convertir la lista en un conjunto,
# se eliminan automáticamente los duplicados
numeros_sin_duplicados = list(set(numeros))  # Usamos set para eliminar duplicados, convirtiendo el conjunto de nuevo a lista para mantener el tipo de dato original

# Imprimimos la lista original para que el usuario pueda ver los duplicados
print("Lista original:", numeros)

# Imprimimos la lista sin duplicados, donde los valores repetidos han sido eliminados
print("Lista sin duplicados:", numeros_sin_duplicados)
