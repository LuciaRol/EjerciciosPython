""" 
Ejercicio 7. Calcular nota.
Realiza un programa que calcule la nota que hace falta sacar en el segundo examen de Programación para obtener la media deseada, 
teniendo en cuenta que el primer examen cuenta el 40% y el segundo el 60%
Autora: Lucía Rodríguez López
Fecha: 17/10/2025
"""

def calcular_nota():
    nota1 = float(input("Introduce la nota de tu primer examen: "))
    media = float(input("Introduce la media que quieres conseguir: "))

    nota2 = (media-(nota1*0.4))/0.6
    print(f"La segunda nota que tienes que conseguir para llegar a una media de {media} es {nota2}.")

calcular_nota()