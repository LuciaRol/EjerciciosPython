""" 
Ejercicio 9. Asignatura.
Escribe un programa que pida el día de la semana y muestre qué asignatura toca a primera hora.
Autora: Lucía Rodríguez López
Fecha: 17/10/2025
"""

def asignatura():
    """ ... """
    # Al introducir una cadena de caracteres, lower() convierte todos los caracteres a minúsculas
    dia = input("Introduce un día de la semana: ").lower()
    respuesta = ""  

    if dia == "lunes":
        respuesta = "Toca POO."
    elif dia == "martes":
        respuesta = "Toca Análisis de datos en Python."
    elif dia == "miercoles" or dia == "miércoles":
        respuesta = "Toca Análisis de datos en Python."
    elif dia == "jueves":
        respuesta = "Toca POO."
    elif dia == "viernes":
        respuesta = "Toca estructuras de control en Python."
    elif dia == "sabado" or dia == "sábado":
        respuesta = "Es sábado, no hay clase."
    elif dia == "domingo":
        respuesta = "Es domingo, no hay clase."
    else:
        return "Día no válido."

    return respuesta

print(asignatura())

