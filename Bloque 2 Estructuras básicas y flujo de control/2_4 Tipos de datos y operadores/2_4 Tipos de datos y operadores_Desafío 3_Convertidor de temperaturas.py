# TENER EN CUENTA QUE:
# 0 grados Celsius es igual a 32 grados Fahrenheit.
# La fórmula para convertir de Celsius a Fahrenheit es: (°C * 9/5) + 32
# 0 grados Celsius es igual a 273,15 grados Kelvin.
# La fórmula para convertir de Celsius a Kelvin es: °C + 273.15

# Paso 1: Solicitar temperatura en grados Celsius
# Se solicita al usuario que ingrese un valor de temperatura en °C, y el valor se convierte a un número decimal (float)
temperatura_celsius = float(input("Ingresa el valor de la temperatura en °C:"))

# Paso 2: Agregar la unidad de medida a la temperatura en Celsius
# Se convierte el valor numérico de la temperatura en Celsius a texto y se le añade la unidad "°C" para mostrarla de forma clara
temperatura_celsius_str = str(temperatura_celsius) + " °C"

# Paso 3: Conversión de Celsius a Fahrenheit
# Se usa la fórmula (°C * 9/5) + 32 para convertir la temperatura de Celsius a Fahrenheit
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

# Paso 4: Conversión de Celsius a Kelvin
# Se usa la fórmula °C + 273.15 para convertir la temperatura de Celsius a Kelvin
temperatura_kelvin = temperatura_celsius + 273.15

# Paso 5: Mostrar los resultados de las conversiones
# Se imprimen las tres temperaturas: en Celsius, Fahrenheit y Kelvin, cada una con su respectiva unidad
print("Temperatura en Celsius:", temperatura_celsius_str)
print("Temperatura en Fahrenheit:", str(temperatura_fahrenheit) + " °F")
print("Temperatura en Kelvin:", str (temperatura_kelvin) + " K")