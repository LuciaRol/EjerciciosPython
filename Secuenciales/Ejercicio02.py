""" 
Ejercicio 2. Media aritmética.
Diseña un algoritmo que pida dos números y calcule la media de ambos.
Autora: Lucía Rodríguez López
Fecha: 16/10/2025
"""

def media_aritmetica():
    num1 = float(input("Introduce un número: "))
    num2 = float(input("Introduce un segundo número: "))
    media = (num1 + num2) / 2
    print(f"La media de {num1} y {num2} es: {media}")

# Llamamos a la función media_aritmetica()
media_aritmetica()
