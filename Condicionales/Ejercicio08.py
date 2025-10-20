""" 
Ejercicio 8. Suma dos números.
Escribe un programa que pida dos números y calcule la suma de ellos. 
Mostrará en pantalla ”La suma es mayor que cero” o ”La suma NO es mayor que cero” 
en función del resultado.
Autora: Lucía Rodríguez López
Fecha: 17/10/2025
"""

def suma_dos_numeros():
    """ Suma dos números y determina si el resultado es mayor o menor que 0."""
    num1 = float(input("Introduce un número: "))
    num2 = float(input("Introduce un segundo número: "))

    suma = num1+num2

    if suma > 0:
         print(f"La suma ({suma}) es mayor que 0.")
    else:
        print(f"La suma ({suma}) NO es mayor que 0.")

suma_dos_numeros()

