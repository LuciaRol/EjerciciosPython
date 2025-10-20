"""
Ejercicio 13. Caída.
Escribe un programa que calcule el tiempo que tardará en caer un objeto desde una altura h. 
Autora: Lucía Rodríguez López
Fecha: 17/10/2025
"""
import math

def caida():
    """ Determina el tiempo que tarda en caer un objeto """
    h = float(input("Introduce la altura (en metros): "))

    mensaje = ""
    g = 9.81

    if h < 0:
        mensaje = "La altura no puede ser negativa."
    else:
        t = math.sqrt((2*h)/g)
        mensaje = f"El tiempo de caída es de {t} segundos."
    
    return mensaje

print(caida())
