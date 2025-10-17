"""
Ejercicio 11. Salario semanal 2.
Ampliaremos el ejercicio anterior para considerar las horas extras. 
Las primeras 40h se pagan a 12 euros. Las siguientes se pagan a 16 euros.
Autora: Lucía Rodríguez López
Fecha: 17/10/2025
"""

def salario_semanal_dos():
    """ Calcula el salario semanal incluyendo horas extras """

    horas = float(input("Introduce las horas trabajadas en una semana: "))
    mensaje = ""

    if horas <= 0:
        mensaje = "No puedes recibir ningún sueldo, porque esta semana no has ido a trabajar."
    else:
        if 1 >= horas <= 40:
            salario = horas*12
        else:
            salario = 40*12 + (horas-40)*16
            mensaje = "El salario semanal del trabajador es: ", salario

    return mensaje

print(salario_semanal_dos())

