# Buscar un libro por autor en un archivo de texto 
# Dado un archivo libros.txt que contiene una lista 
# de libros y sus autores, implementa una función 
# que busque todos los libros escritos por un autor específico y los muestre. 
# Si el autor no tiene libros en la lista, 
# debe mostrar un mensaje indicando que no hay coincidencias.

# Definimos una función para buscar libros por autor en un archivo
def buscar_libros_por_autor(nombre_archivo, autor): 
    # Creamos una lista vacía para almacenar los libros encontrados
    libros_encontrados = []
    
    # Abrimos el archivo en modo lectura ("r" significa "read")
    with open(nombre_archivo, "r") as archivo:
        # Leemos línea por línea el contenido del archivo
        for linea in archivo:
            # Supongamos que cada línea está en el formato "Título;Autor"
            # El método strip() elimina espacios en blanco extra al principio y al final de la línea
            # El método split(";") divide la línea en dos partes usando el punto y coma como separador
            titulo, autor_libro = linea.strip().split(";")
            
            # Comparamos si el autor de la línea (autor_libro) coincide con el autor que buscamos
            # Convertimos ambos a minúsculas para hacer la comparación sin importar mayúsculas o minúsculas
            if autor_libro.lower() == autor.lower():
                # Si coinciden, agregamos el título del libro a la lista de libros encontrados
                libros_encontrados.append(titulo)
    
    # Si encontramos libros, los mostramos en pantalla
    if libros_encontrados:
        print(f"Libros encontrados de {autor}: {', '.join(libros_encontrados)}")
    else:
        # Si no encontramos libros del autor, mostramos un mensaje indicando que no se encontraron
        print(f"No se encontraron libros de {autor}.")

# Llamamos a la función con un autor de ejemplo y un archivo de libros
buscar_libros_por_autor("libros.txt", "Paulo Coelho")
