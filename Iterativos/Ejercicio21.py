"""
Ejercicio 21. Caja fuerte.
Realiza un programa que pida un número de 4 cifras. 
Si no acertamos se mostrará el mensaje ”Lo siento, esa no es la combinación” y 
si acertamos se nos dirá ”La caja fuerte se ha abierto”. Disponemos de 4 intentos.
Autora: Lucía Rodríguez López
Fecha: 21/10/2025
"""

def caja_fuerte():
    """Simula una caja fuerte con una combinación de 4 cifras y un máximo de 4 intentos."""
    clave = "1234"
    intentos = 4

    for i in range(intentos):
        num = input("Introduce la combinación de 4 cifras: ")
        if num == clave:
            return "La caja fuerte se ha abierto."
        intentos_restantes = intentos - (i + 1)
        if intentos_restantes > 0:
            mensaje = f"Lo siento, esa no es la combinación. Te quedan {intentos_restantes} intentos."
        else:
            return "Lo siento, has agotado todos los intentos."
    
        return mensaje

print(caja_fuerte())

