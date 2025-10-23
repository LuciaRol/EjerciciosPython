
"""
Ejercicio 7 - Cadenas de caracteres.
Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa.
Autora: Lucía Rodríguez López
Fecha: 23/10/2025
"""

def mayusculas_minusculas():
    """ Dada una cadena por teclado, convierte las mayúsculas en minúsculas y viceversa. """

    # Introducimos una cadena de caracteres por teclado.
    cadena = input("Introduce un texto: ")

    # Usamos el método swapcase que pasa las mayúsculas a minúsculas y viceversa.
    cadena_modificada = cadena.swapcase()

    # Guardamos una respuesta en una variable
    mensaje = f"La cadena {cadena} modificada es: {cadena_modificada}"

    # Devolvemos el mensaje
    return mensaje

# Llamamos a la función
print(mayusculas_minusculas())

