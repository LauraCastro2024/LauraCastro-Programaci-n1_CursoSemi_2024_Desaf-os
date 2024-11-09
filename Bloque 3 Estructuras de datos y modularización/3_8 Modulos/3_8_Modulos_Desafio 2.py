# Utiliza el módulo random de Python para crear un programa que 
# genere una contraseña aleatoria de 8 caracteres que incluya 
# letras minúsculas, letras mayúsculas y números.

import string  # Importamos el módulo string para acceder a caracteres predefinidos como letras y dígitos
import random  # Importamos el módulo random para generar valores aleatorios

# Definimos los caracteres posibles para la contraseña.
# Usamos string.ascii_letters para obtener todas las letras (mayúsculas y minúsculas).
# Usamos string.digits para obtener todos los números del 0 al 9.
caracteres = string.ascii_letters + string.digits

# Genera una contraseña aleatoria de 8 caracteres.
# ''.join(...) une los caracteres seleccionados en una cadena de texto.
# random.choice(caracteres) selecciona un carácter aleatorio de la lista de caracteres posibles.
# El bucle for _ in range(8) repite el proceso 8 veces para crear una contraseña de 8 caracteres.
contraseña = ''.join(random.choice(caracteres) for _ in range(8))

# Muestra la contraseña generada en pantalla.
print(f"Contraseña generada: {contraseña}")