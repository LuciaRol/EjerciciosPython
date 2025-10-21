"""
Ejercicio 25. Números.
Escribe un programa que pida números hasta que se introduzca un número negativo. 
Se mostrará cuántos números se han introducido, la media de los impares y el mayor de los pares. 
El número negativo solo se utiliza para finalizar.
Autora: Lucía Rodríguez López
Fecha: 21/10/2025
"""

def numeros():
    """Pide números hasta que se introduce un negativo.
    Calcula la cantidad de números introducidos, la media de los impares 
    y el mayor de los pares.
    """
    i = 0
    suma_impares = 0
    cantidad_impares = 0
    mayor_par = None 

    num = int(input("Introduce un número (introduce un número entero negativo para terminar): "))

    while num >= 0:
        i += 1

        if num % 2 == 0: 
            if mayor_par is None or num > mayor_par:
                mayor_par = num
        else: 
            suma_impares += num
            cantidad_impares += 1

        num = int(input("Introduce otro número: "))

  
    mensaje = f"Cantidad de números introducidos: {i}"

    if cantidad_impares > 0:
        media_impares = suma_impares / cantidad_impares
        # Al poner += hace que los mensajes posteriores no sobreescriban a los anteriores, es decir, se añaden
        mensaje += f"Media de los números impares: {media_impares:.2f}"
    else:
        mensaje += "No se introdujeron números impares."

    if mayor_par is not None:
        mensaje += f"El mayor de los números pares es: {mayor_par}"
    else:
        mensaje += "No se introdujeron números pares."

    return mensaje


print(numeros())


