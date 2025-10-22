"""
Ejercicio 1 - Cadenas de caracteres.
Escribe un programa que muestre por pantalla 10 palabras en inglés 
junto a su correspondiente traducción al castellano. 
Las palabras deben estar distribuidas en dos columnas y alineadas a la izquierda.
Autora: Lucía Rodríguez López
Fecha: 21/10/2025
"""

def traduccion():
    """ Muestra dos columnas alineadas a la izda, la primera con palabras en inglés y la segunda con traducciones al español """
    
    # Creamos un diccionario para que la clave se corresponda con la palabra en inglés y el valor con la traducción en español
    vocabulario = {
        "computer" : "ordenador",
        "student" : "alumno\\a", # Para que la \a se vea, se pone una barra antes. 
        "cat" : "gato",
        "penguin" : "pingüino",
        "machine" : "máquina",
        "nature" : "naturaleza",
        "light" : "luz",
        "green" : "verde",
        "book" : "libro",
        "pyramid" : "pirámide"
    }

    # Creamos un encabezado para la tabla alineado a la izda y cada palabra con un espacio de 15
    print(f"{'Inglés':<15}{'Español':<15}") 
    # Repetimos 30 veces el carácter - para crear una línea que separe el encabezado del cuerpo
    print("-" * 30) 
    
    # Devuelve una lista con los pares clave-valor del diccionario que hemos creado anteriormente
    for ingles, espanol in vocabulario.items(): 
        print(f"{ingles:<15}{espanol:<15}") # Alineado a la izda y cada palabra ocupa 15

traduccion()
   


