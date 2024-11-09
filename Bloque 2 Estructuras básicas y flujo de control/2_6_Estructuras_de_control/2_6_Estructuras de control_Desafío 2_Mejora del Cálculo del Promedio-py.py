#Cálculo del promedio de calificaciones, donde se piden todas las calificaciones al mismo tiempo (el estudiante ingresa las calificaciones separadas por comas) y luego se calcula el promedio.

#Declaramos las variables
suma_calificaciones = 0
contador_asignaturas = 0

#Solicitamos que se ingresen las calificaciones separadas por comas
calificaciones = input("Introduce las calificaciones separadas por comas: ") #Por medio de la función input() se le solicita al profesor que ingrese las calificaciones separadas por comas que se guardan en la variable calificaciones

#Convertimos la entrada en una lista de calificaciones
#Al usar float(calificacion) cada elemento se convierte en un número flotante dentro de la lista calificaciones.
calificaciones = [float(calificacion) for calificacion in calificaciones.split(",")] #La función split(",") divide la cadena en una lista de elementos separados por comas.

# Utilizamos un bucle for para iterar sobre la lista de calificaciones.

for calificacion in calificaciones:
    if calificacion != 0: #Verificamos si la calificación actual es diferente de 0.
        suma_calificaciones += calificacion # Si esto se cumple, se agrega a suma_calificaciones
        contador_asignaturas += 1 # y se incrementa contador_asignaturas en 1.
if contador_asignaturas > 0:
    promedio = suma_calificaciones / contador_asignaturas #Al verificar que se ingresaron las calificaciones se calcula el promedio dividiendo la suma de las calificaciones por el contador de asignaturas.

    print(f"El promedio de las calificaciones es: {promedio:.2f}") #Imprimimos el resultado utilizando una f-string con dos decimales