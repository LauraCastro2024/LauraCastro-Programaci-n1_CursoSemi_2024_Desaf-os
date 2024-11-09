# Tienes dos listas de números enteros de diferentes longitudes. 
# Desarrolla un programa que sume los elementos de las listas 
# en las posiciones correspondientes. 
# Si una lista es más corta que la otra, los elementos que falten deben 
# considerarse como 0 en la suma.

# Definimos dos listas de diferentes longitudes
lista1 = [1, 2, 3]
lista2 = [4, 5]

# Iniciamos una lista para almacenar los resultados
suma_resultante = []

# Usamos un bucle para sumar los elementos correspondientes
for i in range(max(len(lista1), len(lista2))):  # Iteramos hasta la longitud de la lista más larga
    
    # Usamos el operador ternario para manejar listas de diferentes longitudes
    # Permite manejar listas de diferentes longitudes, asignando 0 
    # a los elementos que no existen en la lista más corta.
    # Usamos append() para añadir los resultados de la suma a la lista
    
    elemento1 = lista1[i] if i < len(lista1) else 0  # Si hay un elemento, lo tomamos; de lo contrario, usamos 0
    elemento2 = lista2[i] if i < len(lista2) else 0  # Lo mismo para la segunda lista
    suma_resultante.append(elemento1 + elemento2)  # Sumamos y añadimos el resultado a la lista

# Imprimimos la lista resultante
print("Suma de elementos:", suma_resultante)