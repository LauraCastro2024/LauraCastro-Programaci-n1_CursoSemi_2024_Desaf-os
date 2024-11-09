# Crea dos funciones y un main que te permita trabajar con números primos, 
# un concepto matemático fundamental. En este desafío, deberás:
# Crear una función que verifique si un número es primo.
# Crear otra función que cuente la cantidad de números primos dentro 
# de una lista dada.
# Implementar un main que integre estas funciones y muestre los resultados. 
# Asegúrate de que tu código esté bien documentado y que las funciones 
# sean reutilizables.

#Se define la función que se va a utilizar para verificar y calcular si un número es primo o no.
def primo(numero):#Funcion para saber si un numero es primo o no

    if numero < 2:#Si el numero es menor que 2 no es primo
        return False #Retorna falso
    for i in range(2, int(numero**0.5) + 1):#Recorre los numeros desde 2 hasta la raiz cuadrada del numero
        if numero % i == 0:#Si el numero es divisible por algun numero entre 2 y la raiz cuadrada del numero retornará falso o verdadero
            return False #Retorna falso
    return True #Retorna verdadero

def contar(lista):#Funcion para contar los numeros primos de una lista
    return sum(1 for numero in lista if primo(numero))#Retorna la suma de los numeros primos de la lista

def main():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("Lista de números:", numeros) #Imprime la lista de numeros
    cantidad = contar(numeros) #Contar números primos en la lista

    print("Cantidad de números primos en la lista:", cantidad)#Imprime la cantidad de numeros primos en la lista

if __name__ == "__main__":
    main() #Llama a la funcion main