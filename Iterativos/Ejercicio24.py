"""
Ejercicio 24. Positivos-negativos.
Escribe un programa que pida al usuario 10 números y 
muestre por pantalla cuántos son positivos y cuántos negativos.
Autora: Lucía Rodríguez López
Fecha: 21/10/2025
"""

def positivos_negativos():
    """ ... """
    positivos = 0
    negativos = 0

    for i in range(1,11):
        num = int(input("Introduce un número: "))

        if num >= 0:
            positivos = positivos +1
        else:
            negativos = negativos +1
    print("Cantidad de números positivos: ", positivos)
    print("Cantidad de números negativos: ", negativos)

positivos_negativos()

