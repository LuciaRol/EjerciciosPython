"""
Ejercicio 5 - Cadenas de caracteres.
Si tenemos una cadena con un nombre y apellidos, realizar un programa que muestre las iniciales en mayúsculas.
Autora: Lucía Rodríguez López
Fecha: 22/10/2025
"""

def invertir_cadena():
    """Muestra las iniciales en mayúsculas."""

    # Introducimos por teclado el nombre y los apellidos.
    nombre_completo = input("Introduce un nombre: ").lower()

    # Creamos una variable para almacenar las palabras que se han separado con el método split a partir de nombre_completo
    palabras_separadas = nombre_completo.split() # El método split() extrae por separado las palabras separadas por un espacio dentro de la cadena de texto.
    
    # Las palabras almacenadas en iniciales_mayusculas las une en una única cadena con join(), las convierte a mayúsculas con upper() y las va iterando para hacerlo una a una.
    iniciales_mayusculas = "".join([palabra[0].upper() for palabra in palabras_separadas])
        
    # Mostramos solo las iniciales en mayúsculas
    mensaje =  f"Las iniciales son: {iniciales_mayusculas}"
    return mensaje


print(invertir_cadena())
