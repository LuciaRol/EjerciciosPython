"""
Ejercicio 3 - Cadenas de caracteres.
Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado.
Autora: Lucía Rodríguez López
Fecha: 22/10/2025
"""

def cadena_que_empieza_por_subcadena():
    """Comprueba si una cadena comienza con una subcadena introducida por teclado."""

    # Introducimos por teclado una cadena y una subcadena.
    cadena = input("Introduce una frase o cadena de texto larga: ")
    subcadena = input("Introduce una palabra subcadena: ")

    # Usamos método lower() para que todos los caracteres introducidos por teclado pasen a minúsculas
    # Para comparar ambas cadenas usamos el método nativo de Python, startswith(), que verifica si la cadena comienza por la subcadena.
    if cadena.lower().startswith(subcadena.lower()):
        mensaje = f"La cadena '{cadena}' comienza con la subcadena '{subcadena}'."
    else:
        mensaje = f"La cadena '{cadena}' NO comienza con la subcadena '{subcadena}'."

    return mensaje


print(cadena_que_empieza_por_subcadena())


