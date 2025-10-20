"""
Ejercicio 14. Horóscopo.
Escribe un programa que nos muestre el horóscopo a partir del día y mes de nacimiento.
Autora: Lucía Rodríguez López
Fecha: 17/10/2025
"""

def horoscopo():
    """ Determina el horóscopo al introducir una fecha. """
    dia = int(input("Introduce un día de nacimiento (1-31): "))
    mes = int(input("Introduce un mes de nacimiento (1-12): "))
    mensaje = ""

    if mes < 1 or mes > 12 or dia < 1 or dia > 31:
        mensaje ="Esa fecha no existe."
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        mensaje = "Tu signo es Acuario."
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        mensaje = "Tu signo es Piscis."
    elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        mensaje = "Tu signo es Aries."
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        mensaje = "Tu signo es Tauro."
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        mensaje = "Tu signo es Géminis."
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        mensaje = "Tu signo es Cáncer."
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        mensaje = "Tu signo es Leo."
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        mensaje = "Tu signo es Virgo."
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        mensaje = "Tu signo es Libra."
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        mensaje = "Tu signo es Escorpio."
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        mensaje = "Tu signo es Sagitario."
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        mensaje = "Tu signo es Capricornio."
    return mensaje

print(horoscopo())
