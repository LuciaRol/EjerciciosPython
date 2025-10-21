"""
Ejercicio 16. Ordenar 3.
Escribe un programa que ordene 3 números enteros introducidos por teclado. 
Autora: Lucía Rodríguez López
Fecha: 17/10/2025
"""

def ordenar_numeros(a, b, c):
    """Recibe tres números enteros y devuelve una lista con ellos ordenados de menor a mayor."""
    numeros = [a, b, c]
    numeros.sort()
    return numeros


num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))


ordenados = ordenar_numeros(num1, num2, num3)
mensaje = f"Los números ordenados son: {ordenados}."

print(mensaje)

