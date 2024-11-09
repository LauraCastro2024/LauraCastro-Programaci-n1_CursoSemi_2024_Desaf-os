# Crea una función que tome una lista de números y devuelva la suma 
# y el promedio de esos números.

#Se define la función que se va a utilizar para calcular la suma y el promedio

def calcular(numeros): #numeros es la lista de números que la función va a procesar
  suma = sum(numeros) #La función suma toma una lista de números y devuelve la suma de todos los elementos en esa lista.
  promedio = suma / len(numeros) #Se calcula el promedio dividiendo la suma de los números por la cantidad de elementos en la lista
  return suma, promedio #Devuelve los valores calculados

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #Se crea una lista de números
suma, promedio = calcular(numeros) #Se llama a la función calcular_suma_y_promedio y se asignan los resultados a las variables suma y promedio
print("Los números son:", numeros) #Se imprime la lista de números
print("La suma de los números es:", suma) #Se imprime la suma de los números
print("El promedio de los números es:", promedio) #Se imprime el promedio de los números