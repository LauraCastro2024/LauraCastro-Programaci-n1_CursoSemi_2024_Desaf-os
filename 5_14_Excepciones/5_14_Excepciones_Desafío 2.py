# Crea un programa que tome una lista de valores 
# y realice operaciones matemáticas sobre ellos. 
# Implementa el manejo de varias excepciones comunes 
# como ZeroDivisionError, TypeError, y ValueError.

try: # try: Ejecuta el código para manejo de errores.
    # Creamos una lista con valores
    valores = [10, 'a', 5, 0] # valores: Define una lista que incluye enteros y un string para causar errores intencionados.
    
    for valor in valores: # for valor in valores: Itera sobre cada elemento en la lista.
        resultado = 10 / valor  # Divide 10 entre cada valor en la lista
        print(f"10 dividido por {valor} es {resultado}")

# Capturamos errores de división por cero
except ZeroDivisionError: # da un error y muestra un mensaje.
    print("Error: No se puede dividir por cero.")

# Capturamos errores si el valor no es numérico
except TypeError:
    print("Error: Tipo de dato no válido para la operación.")

# Capturamos errores de valor no correcto
except ValueError:
    print("Error: Valor no válido.")
