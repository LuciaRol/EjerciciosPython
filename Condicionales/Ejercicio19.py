"""
Ejercicio 20. Desayuno
Escribe un programa que calcule el precio de un desayuno. 
Primero pregunta al usuario que ha tomado para comer: tostada, churros o donuts. 
Los churros valen 1,50€ y el donut 1€. 
En caso de tomar tostada, debe preguntar si es básica (1,20€) o especial (1,60€). 
Por último preguntará la bebida, zumo o café, a 1,80€ y 1,20€ respectivamente.
Autora: Lucía Rodríguez López
Fecha: 20/10/2025
"""

def desayuno():
    """Calcula el precio total de un desayuno según las opciones elegidas por el usuario."""

    opciones_comida = ["tostada", "churros", "donuts", ""]
    opciones_bebida = ["zumo", "cafe", ""]

    comida = input("¿Qué has tomado para comer? (tostada/churros/donuts): ").lower().strip()

    if comida not in opciones_comida:
        return "Esa comida no está en la carta."

    if comida == "churros":
        precio_comida = 1.50
    elif comida == "donuts":
        precio_comida = 1.00
    elif comida == "":
        precio_comida = 0.00
    elif comida == "tostada":
        tipo_tostada = input("¿Has tomado una tostada básica o especial?: ").lower()
        if tipo_tostada == "basica":
            precio_comida = 1.20
        elif tipo_tostada == "especial":
            precio_comida = 1.60
        else:
            return "Ese tipo de tostada no está en el menú."


    bebida = input("¿Qué has tomado para beber? (zumo/cafe): ").lower()

    if bebida not in opciones_bebida:
        return "Esa bebida no está en la carta."
    if bebida == "zumo":
        precio_bebida = 1.80
    elif bebida == "cafe":
        precio_bebida = 1.20
    elif bebida == "":
        precio_bebida = 0.00

    precio_total = precio_comida + precio_bebida

    mensaje = f"El precio total de tu desayuno es: {comida} ({precio_comida}) más {bebida} ({precio_bebida}) es de {precio_total:.2f} €."
    return mensaje


print(desayuno())


    
