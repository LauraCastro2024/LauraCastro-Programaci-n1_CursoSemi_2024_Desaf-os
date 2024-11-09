# Construye una función que tome dos listas y 
# devuelva True si tienen al menos un elemento en común, de lo contrario, 
# que devuelva False.

def tienen_elemento_comun(lista1, lista2):
    """Devuelve True si las dos listas tienen al menos un elemento en común, de lo contrario False."""
    # Convertimos la primera lista en un conjunto para una búsqueda más eficiente
    conjunto1 = set(lista1)  # Crear un conjunto a partir de lista1, eliminando duplicados y permitiendo búsquedas rápidas

    # Iteramos sobre la segunda lista y verificamos si algún elemento está en el conjunto
    for elemento in lista2:  # Recorrer cada elemento en lista2
        if elemento in conjunto1:  # Verificar si el elemento actual de lista2 está en conjunto1
            return True  # Si encontramos un elemento común, retornamos True
    return False  # Si no se encontró ningún elemento común, retornamos False

# Ejemplo de uso
lista_a = [1, 2, 3, 4]  # Definir la primera lista
lista_b = [5, 6, 7, 3]  # Definir la segunda lista con un elemento en común (3)
lista_c = [8, 9, 10]    # Definir la tercera lista sin elementos en común con lista_a

resultado1 = tienen_elemento_comun(lista_a, lista_b)  # Debe devolver True porque 3 está en ambas listas
resultado2 = tienen_elemento_comun(lista_a, lista_c)  # Debe devolver False porque no hay elementos comunes

# Imprimir los resultados
print("¿Lista A y Lista B tienen elementos en común?", resultado1)  # Mostrar el resultado de la comparación entre lista_a y lista_b
print("¿Lista A y Lista C tienen elementos en común?", resultado2)  # Mostrar el resultado de la comparación entre lista_a y lista_c
