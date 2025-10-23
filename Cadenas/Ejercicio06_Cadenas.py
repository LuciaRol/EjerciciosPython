"""
Ejercicio 6 - Cadenas de caracteres.
Pide una cadena y dos caracteres por teclado (valida que sea un carácter), 
sustituye la aparición del primer carácter en la cadena por el segundo carácter.
Autora: Lucía Rodríguez López
Fecha: 22/10/2025
"""

def sustituir_caracter():
    """Sustituye un carácter en una cadena por otro carácter dado por el usuario."""
    # Introducimos una cadena de caracteres
    cadena = input("Introduce un texto: ")

    # Pedimos el carácter a sustituir. Validamos que sea un único carácter
    while True:
        caracter1 = input("Introduce el carácter que quieres sustituir: ")
        if len(caracter1) == 1:
            break
        else:
            print("Introduce un único carácter, por favor.")

    # Pedimos el carácter de sustitución. Volvemos a validar que sea un único carácter
    while True:
        caracter2 = input("Introduce el carácter por el que lo quieres sustituir: ")
        if len(caracter2) == 1:
            break
        else:
            print("Introduce un único carácter, por favor.")

    # Sustituimos y mostramos el resultado
    nueva_cadena = cadena.replace(caracter1, caracter2)
    print("Resultado:", nueva_cadena)

sustituir_caracter()
