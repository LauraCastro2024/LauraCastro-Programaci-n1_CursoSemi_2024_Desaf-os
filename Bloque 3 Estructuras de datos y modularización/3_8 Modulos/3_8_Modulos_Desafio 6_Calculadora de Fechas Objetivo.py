# Escribir un programa en Python que permita calcular 
# la diferencia entre dos fechas, utilizando el módulo datetime.

# Importamos el módulo datetime para trabajar con fechas y horas en Python.
from datetime import datetime

# Pedimos al usuario que ingrese dos fechas en formato día/mes/año.
# La función input() obtiene la entrada del usuario como un texto.
fecha1 = input("Ingresa la primera fecha (dd/mm/yyyy): ")
fecha2 = input("Ingresa la segunda fecha (dd/mm/yyyy): ")

# Convertimos las fechas ingresadas (que están como texto) a objetos datetime.
# datetime.strptime() toma el texto y lo convierte a un objeto datetime según el formato especificado.
# "%d/%m/%Y" significa que la fecha está en formato día/mes/año (por ejemplo: 25/12/2024).
fecha1 = datetime.strptime(fecha1, "%d/%m/%Y")
fecha2 = datetime.strptime(fecha2, "%d/%m/%Y")

# Calculamos la diferencia entre las dos fechas.
# La resta de dos objetos datetime da un objeto timedelta, del cual podemos obtener la diferencia en días.
# Usamos abs() para asegurarnos de que la diferencia sea positiva, sin importar cuál fecha sea mayor.
diferencia = abs((fecha2 - fecha1).days)

# Imprimimos la diferencia entre las dos fechas en días.
print(f"La diferencia entre las fechas es de {diferencia} días.")
