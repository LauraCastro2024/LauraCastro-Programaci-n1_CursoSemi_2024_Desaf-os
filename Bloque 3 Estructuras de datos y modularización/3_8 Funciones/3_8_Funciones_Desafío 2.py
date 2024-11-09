# Diseña una función que tome una cadena y devuelva la misma cadena, 
# pero con el primer carácter de cada palabra en mayúsculas.

#Se define la función que se va a utilizar para que tome una cadena y devuelva la misma cadena
def formatear_texto(cadena):

    return cadena.title() # Se utiliza el método title() para que la primera letra de cada palabra comience con mayúscula.

texto = "estamos realizando el desafío 2 del tema funciones" #Se crea una variable "texto" que contiene una cadena de texto.

resultado = formatear_texto(texto)
print(resultado)  #Se imprime el resultado de la función formatear_texto()