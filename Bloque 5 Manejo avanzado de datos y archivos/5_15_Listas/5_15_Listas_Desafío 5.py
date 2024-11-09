# Usa una "list comprehension" para crear una lista llamada potencias 
# que contenga las potencias de 2 de los números del 0 al 9 
# (es decir, 2 elevado a la potencia de cada número). 
# Imprime la lista resultante.


# Usamos una list comprehension para generar las potencias de 2 de los números del 0 al 9
potencias = [2 ** x for x in range(10)]  # Calculamos 2 elevado a la potencia de cada número del 0 al 9

# Imprimimos la lista resultante
print("Potencias de 2:", potencias)  # Esto imprimirá la lista de potencias