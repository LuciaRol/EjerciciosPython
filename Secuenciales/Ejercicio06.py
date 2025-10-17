""" 
Ejercicio 6. Salario semanal.
Escribe un programa que calcule el salario semanal de un empleado según las horas trabajadas, 
a razón de 12€ la hora.
Autora: Lucía Rodríguez López
Fecha: 17/10/2025
"""

def salario_semanal():
    horas = float(input("Introduce las horas semanales trabajadas: "))
    salario = horas*12
    print(f"El salario para {horas} semanales trabajadas es {salario} euros.")

salario_semanal()