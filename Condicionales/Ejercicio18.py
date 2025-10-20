"""
Ejercicio 19. Piedra, papel, tijera.
Escribe un programa que implemente este juego para dos usuarios. 
Si alguno introduce una opción incorrecta se mostrará un mensaje de error. 
Autora: Lucía Rodríguez López
Fecha: 20/10/2025
"""

def piedra_papel_tijera():
    """Juego de piedra, papel o tijera para dos jugadores."""

    jugador1 = input("Jugador 1, escoge tu opción (piedra/papel/tijera): ").lower()
    jugador2 = input("Jugador 2, escoge tu opción (piedra/papel/tijera): ").lower()
    mensaje = ""

    opciones = ["piedra", "papel", "tijera"]

    if jugador1 not in opciones or jugador2 not in opciones:
        mensaje = "Opción no válida."
    elif jugador1 == jugador2:
        mensaje = "Empate. Ambos eligieron lo mismo."
    elif (
        (jugador1 == "piedra" and jugador2 == "tijera") or
        (jugador1 == "papel" and jugador2 == "piedra") or
        (jugador1 == "tijera" and jugador2 == "papel")
    ):
        mensaje = "¡Ha ganado el jugador 1!"
    else:
        mensaje = "¡Ha ganado el jugador 2!"

    return mensaje


print(piedra_papel_tijera())

