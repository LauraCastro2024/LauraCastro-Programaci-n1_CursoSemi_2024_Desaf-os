# Investiga y utiliza al menos tres funciones del módulo string 
# que puedan ser útiles para mejorar nuestro procesador de texto.

import string

# Imprime todas las letras, dígitos y puntuación para mostrar sus valores
print("Letras:", string.ascii_letters)
print("Dígitos:", string.digits)
print("Puntuación:", string.punctuation)

# Contar letras en un texto ignorando puntuación
texto = "¡Hola, compañeros! Este curso de programación está buenísimo."
letras = sum(c in string.ascii_letters for c in texto)
print(f"Número de letras en el texto: {letras}")
