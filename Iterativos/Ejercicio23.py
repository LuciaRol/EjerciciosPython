"""
Ejercicio 23. Fibonacci.
Escribe un programa que muestre los n primeros términos de la serie de Fibonacci. 
El valor de n será introducido por teclado.
Autora: Lucía Rodríguez López
Fecha: 21/10/2025
"""

def fibonacci():
    """ ... """

    num = int(input("Introduce cuántos números de la serie de Fibonacci quieres ver: "))

    if num <= 0:
        mensaje = "Introduce un número positivo, por favor."
    else:
        a = 0
        b = 1
        mensaje = "La serie de Fibonacci es la siguiente: "
        print(a)

        if num > 1:
            print(b)
        
        for i in range(0, num-2):
            suma = a+b
            a = b
            b = suma
            print(suma)
        
        return mensaje

    
fibonacci()

