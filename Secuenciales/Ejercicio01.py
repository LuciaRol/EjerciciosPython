""" 
Ejercicio 1. Cambio de signo.
Diseña un algoritmo que pida un número y muestre por pantalla el número por pantalla cambiado de signo
Autora: Lucía Rodríguez López
Fecha: 16/10/2025
"""

def cambia_signo():
    num = int(input ("Introduce un número entero: "))

    num_signo_cambiado = num * -1
    print("Este es el número con el signo cambiado : ", num_signo_cambiado)

#Llamamos a la función cambia_signo()
cambia_signo()