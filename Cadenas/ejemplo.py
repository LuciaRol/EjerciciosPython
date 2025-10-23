def leer_numero(mensaje="Introduce un número entero: ", error= "Error, no se introdujo un entero."):
    """ ... """
    while(True):
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print(error)


leer_numero()

def leer_entero_minimo(minimo=0, mensaje="Introduce un número entero: ", error= "Error, no se introdujo un entero."):
    """ ... """

    while(numero := leer_numero(mensaje, error)<minimo):
        pass
    return numero


numero = leer_numero(0, "Introduce un número >= 0: ")

