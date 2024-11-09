# Lista original de libros con sus códigos de identificación
libros = [
    {"titulo": "El Quijote", "codigo": 102},          # Libro con título y código 102
    {"titulo": "Cien años de soledad", "codigo": 101}, # Libro con título y código 101
    {"titulo": "La Odisea", "codigo": 103},            # Libro con título y código 103
    {"titulo": "1984", "codigo": 104}                  # Libro con título y código 104
]

# Usar sorted() para ordenar los libros por código en orden decreciente
libros_ordenados = sorted(libros, key=lambda libro: libro["codigo"], reverse=True)

# Imprimir la lista original de libros
print("Lista original:")
print(libros)

# Imprimir la lista ordenada por código en orden decreciente
print("\nLista ordenada por código en orden decreciente:")
print(libros_ordenados)
