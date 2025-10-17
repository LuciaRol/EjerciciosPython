""" 
Ejercicio 10. Saludo.
Escribe un programa que pida una hora (0-23) y muestre "Buenos días", "Buenas tardes" o "buenas noches", según la hora. 
Se utilizarán los tramos 6 a 12, 13 a 20 y de 21 a 5, respectivamente. 
Autora: Lucía Rodríguez López
Fecha: 17/10/2025
"""

def saludos():
    """ Devuelve un saludo en función de la hora que introduzcamos por consola. """
    hora = int(input("Introduce una hora del día (0-23): "))
    saludo = ""

    if 6 >= hora <= 12:
        saludo = "¡Buenos días!"
    elif 13 >= hora <= 20:
        saludo = "¡Buenas tardes!"
    elif 21 >= hora <= 23 or 0 <= hora <= 5:
        saludo = "¡Buenas noches!"
    else:
        saludo = "Esa hora no existe."

    return saludo

print(saludos())
