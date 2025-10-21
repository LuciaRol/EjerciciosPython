"""
Ejercicio 22. Media números.
Escribe un programa que calcule la media de una serie de números positivos. 
El usuario indicará que ha terminado de introducir datos cuando introduzca un número negativo.
Autora: Lucía Rodríguez López
Fecha: 21/10/2025
"""

def media_num():
    """ ... """
    suma = 0
    i = 0

    num = int(input("Introduce un número (introduce un número entero negativo para terminar): "))
    while num>=0:
        suma = suma + num
        i = i+1
        num = int(input("Introduce otro número: "))
    
    if i >= 0:
        media = suma/i
        mensaje = f"La media de los {i} números es: {media:.2f}"
    else:
        mensaje = "Se ha detenido el programa."
    
    return mensaje

print(media_num())

