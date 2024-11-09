# Utiliza el modulo creado procesador_texto para resaltar 
# recursivamente todas las ocurrencias 
# de una palabra clave en un texto largo.


# Definimos una función recursiva para resaltar cada ocurrencia de una palabra en el texto
def resaltar_palabra(texto, palabra, indice=0):
    # Dividimos el texto en palabras para analizarlas una por una
    palabras = texto.split()  # .split() divide el texto en una lista de palabras, separadas por espacios

    # Caso base: si el índice es igual al número de palabras, terminamos el procesamiento
    if indice >= len(palabras):
        return ""  # Devolvemos una cadena vacía cuando ya no hay más palabras que procesar

    # Resalta la palabra si coincide, si no la deja igual
    # Si la palabra actual coincide con la palabra que estamos buscando, la resaltamos con asteriscos
    palabra_actual = f"**{palabra}**" if palabras[indice] == palabra else palabras[indice]

    # Llamada recursiva: procesamos la siguiente palabra en el texto
    # Sumamos la palabra procesada actual con la llamada recursiva para la siguiente palabra
    return palabra_actual + " " + resaltar_palabra(texto, palabra, indice + 1)

# Prueba de la función
texto_prueba = "Me gusta mucho hacer los ejercicios de programación y programación es fundamental para mi formación."
# Llamamos a la función para resaltar todas las ocurrencias de la palabra "programación"
print(resaltar_palabra(texto_prueba, "programación"))  # Debería resaltar cada "programación"
