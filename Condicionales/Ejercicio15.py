"""
Ejercicio 15. Medianoche.
Escribe un programa que dada una hora determinada (horas y minutos), 
calcule el número de segundos que faltan para llegar a la medianoche. 
Autora: Lucía Rodríguez López
Fecha: 17/10/2025
"""

def medianoche():
    """ Calcula los segundos que faltan para medianoche. """
    hora = int(input("Introduce la hora (0-23): "))
    minutos = int(input("Introduce los minutos (0-59): "))
    mensaje = ""

    if hora < 0 or hora > 23 or minutos < 0 or minutos > 59:
        mensaje = "Hora no válida."
    else:
        segundos_restantes = ((23-hora)*3600)+((59-minutos)*60)+60
        mensaje = f"Faltan {segundos_restantes} segundos para la medianoche."
    
    return mensaje

print(medianoche())
    