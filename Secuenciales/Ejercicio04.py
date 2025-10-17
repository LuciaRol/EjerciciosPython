""" 
Ejercicio 4. Volumen de un cono.
Diseña un algoritmo que calcule el volumen de un cono.
Autora: Lucía Rodríguez López
Fecha: 16/10/2025
"""

def volumen_cono():
    pi = 3.1416
    radio = float(input("Introduce el radio (cm): "))
    altura = float(input("Introduce la altura (cm): "))
    volumen = (pi * radio * radio * altura) / 3
    print(f"El volumen del cono es: {volumen} cm\u00B3.")

# Llamamos a la función volumen_cono()
volumen_cono()