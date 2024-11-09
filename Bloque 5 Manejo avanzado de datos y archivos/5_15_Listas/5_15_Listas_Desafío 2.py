# Un sistema de inventario tiene una lista con los códigos de productos. 
# Desarrolla un programa que permita al usuario introducir un código 
# de producto y que determine si ese código está en la lista. 
# Si el código se encuentra, el programa debe devolver la posición 
# en la que aparece; si no está, debe mostrar un mensaje indicando 
# que no se ha encontrado el código.

# Definimos una lista de códigos de productos 
# Cada código en la lista representa un producto único
codigos_productos = ["A123", "B456", "C789", "D012"] # La lista codigos_productos almacena los códigos. 

# Solicitamos al usuario que introduzca un código de producto para buscar en la lista
# El código introducido por el usuario se almacena en la variable codigo_usuario
codigo_usuario = input("Introduce el código del producto: ")

# Verificamos si el código del usuario está en la lista de códigos de productos
# Usamos in para comprobar si codigo_usuario está presente en codigos_productos
if codigo_usuario in codigos_productos:
# Si el código está en la lista, obtenemos su posición usando el método index
# Usamos index() para obtener la posición donde encuentra el elemento en la lista
    posicion = codigos_productos.index(codigo_usuario)
    
# Mostramos al usuario el código introducido y su posición en la lista
    print(f"El código {codigo_usuario} se encuentra en la posición: {posicion}.")
else:
# Si el código no está en la lista, mostramos un mensaje de error
    print("El código no se ha encontrado.")