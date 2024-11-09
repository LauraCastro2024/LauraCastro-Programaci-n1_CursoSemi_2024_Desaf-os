# formato_texto.py

# Definimos la función en_negrita para aplicar formato de negrita al texto.
def en_negrita(texto):
    """Devuelve el texto en negrita."""
    # Usamos "\033[1m" para activar el formato de negrita y "\033[0m" para restablecer el formato.
    # Esto envuelve el texto en códigos ANSI para mostrarlo en negrita en la terminal.
    return f"\033[1m{texto}\033[0m"

# Definimos la función en_italica para aplicar formato de itálica al texto.
def en_italica(texto):
    """Devuelve el texto en itálica."""
    # Usamos "\033[3m" para activar el formato itálico y "\033[0m" para restablecer el formato.
    # Al igual que en la función anterior, esto formatea el texto usando códigos ANSI.
    return f"\033[3m{texto}\033[0m"

# Definimos la función en_subrayado para aplicar un subrayado al texto.
def en_subrayado(texto):
    """Devuelve el texto subrayado."""
    # Usamos "\033[4m" para activar el subrayado y "\033[0m" para desactivar el formato.
    # Este código hace que el texto se muestre subrayado en la terminal.
    return f"\033[4m{texto}\033[0m"