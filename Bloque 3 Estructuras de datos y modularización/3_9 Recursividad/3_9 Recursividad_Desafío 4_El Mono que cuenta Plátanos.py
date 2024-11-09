# Imagina que tenemos un mono que intenta contar plátanos. 
# Sin embargo, nuestro mono es un poco distraído y olvida cuántos plátanos 
# ha contado cada vez que empieza a contar de nuevo. Cada vez que termina 
# una secuencia de conteo, se olvida de los plátanos contados antes y vuelve
# a empezar, sumando todos desde el principio. Implementa una función 
# recursiva que simule cómo el mono cuenta plátanos.
# Reglas: 
# • El mono puede contar un plátano a la vez. 
# • Cada vez que el mono termina de contar una pila de plátanos, 
# tiene que volver a contar desde cero, pero sigue acumulando el total.
# Por ejemplo: • Si el mono tiene 5 plátanos en la pila, contará 
# uno por uno, luego olvida y vuelve a empezar, acumulando la suma.


# Definimos una función recursiva para contar plátanos
def contar_platanos(total_platanos, contados=0, acumulado=0):
    # Si el número de plátanos contados es igual al total, devolvemos el acumulado
    # Esto es el caso base: si ya hemos contado todos los plátanos, devolvemos el total acumulado
    if contados == total_platanos:
        return acumulado

    # Incrementamos el conteo en 1 y acumulamos el conteo total
    # Sumamos 1 al número de plátanos contados
    contados += 1
    # Sumamos 1 al acumulado para mantener el total de plátanos contados
    acumulado += 1

    # Llamada recursiva: el mono vuelve a contar desde cero, pero mantiene el total acumulado
    # Llamamos a la función nuevamente para seguir contando plátanos
    return contar_platanos(total_platanos, contados, acumulado)

# Ejemplo de uso
# Llamamos a la función para contar 5 plátanos
print(contar_platanos(5))  # Debería imprimir 5

# Llamamos a la función para contar 10 plátanos
print(contar_platanos(10))  # Debería imprimir 10
