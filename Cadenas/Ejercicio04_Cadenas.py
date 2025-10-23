"""
Ejercicio 4 - Cadenas de caracteres.
Realizar un programa que dada una cadena de caracteres por teclado, genere otra cadena resultado de invertir la primera.
Autora: Lucía Rodríguez López
Fecha: 22/10/2025
"""

def invertir_cadena():
    """Invierte una cadena dada por teclado"""

    # Introducimos una cadena por teclado por teclado.
    cadena = input("Introduce una cadena de texto: ")

    # Creamos una nueva variable cadena_invertida, igual a la cadena original, con : la tomamos entera y con el -1 le decimos que se ordene al revés.
    cadena_invertida = cadena[::-1]
        
    # Mostramos la cadena invertida.
    mensaje = f"La cadena {cadena} invertida es {cadena_invertida}."
    return mensaje


print(invertir_cadena())

