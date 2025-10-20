"""
Ejercicio 17. Nota programación.
Escribe un programa que pide las notas de dos exámenes de programación. 
Si la media es mayor o igual a 5, el alumno estará aprobado y se mostrará la media. 
Si no, Se preguntará al usuario ¿Cuál ha sido el resultado de la recuperación? (apto/no apto). 
Si el resultado es apto, la nota será 5, en caso contrario se mantendrá la media anterior.
Autora: Lucía Rodríguez López
Fecha: 20/10/2025
"""

def nota_programacion():
    """ Función que determina la nota media de un alumno y si está o no aprobado. """

    nota1 = int(input("Introduce la primera nota: "))
    nota2 = int(input("Introduce la segunda nota: "))
    nota_media = (nota1+nota2)/2
    mensaje = ""

    if nota_media >= 5:
        mensaje = f"¡Enhorabuena! Tu nota media es de {nota_media}, has aprobado."
    else:
        pregunta = input("¿Cuál ha sido el resultado de la recuperación?(apto/no apto) ").lower()
        if pregunta == "apto":
            mensaje = "¡Enhorabuena! Tu nota es un 5, has aprobado."
        elif pregunta == "no apto":
            mensaje = f"Lo siento, tu nota media es de {nota_media}."
        else:
            mensaje = "Respuesta no válida."

    return mensaje

print(nota_programacion())

