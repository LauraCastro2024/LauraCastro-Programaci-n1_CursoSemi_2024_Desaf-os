#Crea una función recursiva que invierta las palabras en una oración 
# sin utilizar funciones incorporadas de Python 
# para invertir cadenas o listas. 


# Definimos una función recursiva para invertir las palabras de una oración
def invertir_palabras(oracion):
    # Dividimos la oración en una lista de palabras
    palabras = oracion.split()  # .split() divide la oración en palabras, usando los espacios como separadores

    # Caso base: si hay una o ninguna palabra, devolvemos la oración tal cual
    # Si la lista de palabras tiene 1 o menos palabras, no hay nada que invertir, por lo que devolvemos la oración original
    if len(palabras) <= 1:
        return oracion

    # Tomamos la última palabra y llamamos a la función con el resto de las palabras
    # Tomamos la última palabra de la lista con palabras[-1], luego usamos la recursión para invertir el resto de las palabras
    # " ".join(palabras[:-1]) toma todas las palabras menos la última y las une en una nueva cadena de texto
    return palabras[-1] + " " + invertir_palabras(" ".join(palabras[:-1]))

# Ejemplo de uso
# Invertimos las palabras de la oración "Este ejercicio es para programación"
print(invertir_palabras("Este ejercicio es para programación"))  
# Debería imprimir "programación para es ejercicio Este"
