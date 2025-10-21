"""
Ejercicio 20. Tabla de multiplicar.
Escribe un programa que muestre la tabla de multiplicar de un número introducido por teclado.
Autora: Lucía Rodríguez López
Fecha: 21/10/2025
"""

def tabla_multiplicar():
    """Muestra la tabla de multiplicar de un número entero introducido por el usuario."""
    num = int(input("Introduce un número para ver su tabla de multiplicar: "))
    
    print(f"Tabla de multiplicar del {num}:")
    for i in range(1, 11):
        resultado = num * i
        print(f"{num} x {i} = {resultado}")     

tabla_multiplicar()  


