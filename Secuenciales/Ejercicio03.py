""" 
Ejercicio 3. Conversor euros-pesetas
Diseña un algoritmo que pida la cantidad de euros y calcule cuántas pesetas son.
Autora: Lucía Rodríguez López
Fecha: 16/10/2025
"""

def conversor_euros_pesetas():
    euros = float(input("Introduce una cantidad en euros: "))
    pesetas = (euros*1000)/6
    print(f"La cantidad de {euros} euros equivalen a {pesetas} pesetas.")

conversor_euros_pesetas()


