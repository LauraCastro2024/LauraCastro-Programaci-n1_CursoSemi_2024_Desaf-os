# Crea un módulo personalizado que contenga funciones para cambiar 
# el formato del texto (por ejemplo, a negrita, itálica, etc.) 
# e impórtalo en un nuevo programa.

# Importamos el módulo personalizado donde definimos las funciones de formato de texto.
import formato_texto

# Definimos la función principal que ejecutará nuestro programa.
def main():
    # Definimos el texto que queremos formatear.
    texto = "Hola, mundo!"

    # Llamamos a las funciones del módulo formato_texto para aplicar diferentes formatos al texto.
    texto_negrita = formato_texto.en_negrita(texto)     # Aplicamos el formato de negrita
    texto_italica = formato_texto.en_italica(texto)     # Aplicamos el formato de itálica
    texto_subrayado = formato_texto.en_subrayado(texto) # Aplicamos el formato de subrayado

    # Imprimimos el texto original y luego cada versión formateada.
    print("Texto original:", texto)               # Imprime el texto sin formato
    print("Texto en negrita:", texto_negrita)     # Imprime el texto en negrita
    print("Texto en itálica:", texto_italica)     # Imprime el texto en itálica
    print("Texto subrayado:", texto_subrayado)    # Imprime el texto subrayado

# Esta línea verifica si estamos ejecutando este archivo directamente (no importándolo desde otro).
# Si es así, llama a la función main() para ejecutar el programa.
if __name__ == "__main__":
    main()
