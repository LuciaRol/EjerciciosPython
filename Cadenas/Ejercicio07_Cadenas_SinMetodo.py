
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

    # Inicializamos la variable que va a contener el texto de salida.
    mensaje = ""

    # Recorremos la cadena introducida caracter a caracter
    for letra in cadena:
        if letra.islower():
            mensaje += letra.upper() # Si un caracter está en minúscula, lo pasa a mayúscula
        elif letra.isupper():
            mensaje += letra.lower() # Si un caracter está en mayúscula, lo pasa a minúscula
        else:
            mensaje += letra # Si el caracter no es una letra, lo deja como está
    
    # Devolvemos el mensaje modificado respecto a la cadena original
    return mensaje

# Llamamos a la función
print(mayusculas_minusculas())

