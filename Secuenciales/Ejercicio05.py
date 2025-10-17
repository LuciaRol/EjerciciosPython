""" 
Ejercicio 5. Operaciones aritméticas.
Escribe un programa que sume, reste, multiplique y divida dos números introducidos por teclado.
Autora: Lucía Rodríguez López
Fecha: 16/10/2025
"""

def calculadora():
    num1 = float(input("Introduce un número: "))
    num2 = float(input("Introduce un segundo número: "))

    suma = num1+num2
    resta = num1-num2
    multiplicacion = num1*num2
    division = num1/num2

    print(f"La suma de {num1} y {num2} es: {suma}")
    print(f"La resta de {num1} y {num2} es: {resta}")
    print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
    print(f"La división de {num1} entre {num2} es: {division}")

calculadora()
