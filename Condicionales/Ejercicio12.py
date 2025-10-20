"""
Ejercicio 12. Ecuación de primer grado.
Escribe un programa que resuelva una ecuación de primer grado (ax+b = 0). 
Autora: Lucía Rodríguez López
Fecha: 17/10/2025
"""

def ecuacion_primer_grado():
    """ Despeja la x en la ecuación de primer grado (ax+b = 0)"""
    a = float(input("Introduce el valor de a: "))
    b = float(input("Introduce el valor de b: "))
    mensaje = ""

    if a == 0:
        if b == 0:
            mensaje = "La ecuación tiene infinitas soluciones."
        else:
            mensaje = "La ecuación no tiene solución real."
    else:
        x = (-b)/a
        mensaje = f"La solución es: x = {x}."

    return mensaje

print(ecuacion_primer_grado())


