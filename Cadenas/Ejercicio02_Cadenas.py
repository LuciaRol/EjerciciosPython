"""
Ejercicio 2 - Cadenas de caracteres.
Escribe un programa que muestre tu horario de clase. 
Cada módulo o asignatura debe mostrarse en un color diferente.
Autora: Lucía Rodríguez López
Fecha: 21/10/2025
"""
# REPASAR ESTE EJERCICIO

# Creamos variables a las que les asignamos colores ANSI mediante su código correspondiente
RESET = "\033[0m"
ROJO = "\033[91m"
VERDE = "\033[92m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
AMARILLO = "\033[93m"
GRIS = "\033[90m"

# Creamos dos listas que contengan los días de la semana y las horas
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
horas = ["08:00", "09:00", "10:00"]

# Creamos un diccionario en el que la clave es el día de la semana y el valor una lista con las asignaturas.
clases = {
    "Lunes": ["Matemáticas", "Lengua", "Historia"],
    "Martes": ["Física", "Química", "Arte"],
    "Miércoles": ["Inglés", "Música", "Educación Física"],
    "Jueves": ["Biología", "Geografía", "Informática"],
    "Viernes": ["Literatura", "Filosofía", "Matemáticas"],
    "Sábado": ["No hay clase"] * len(horas),
    "Domingo": ["No hay clase"] * len(horas),
}

# Asignamos un color a cada asignatura
colores = {
    "Matemáticas": ROJO,
    "Lengua": VERDE,
    "Historia": AMARILLO,
    "Física": AZUL,
    "Química": MAGENTA,
    "Arte": CYAN,
    "Inglés": ROJO,
    "Música": VERDE,
    "Educación Física": AMARILLO,
    "Biología": AZUL,
    "Geografía": MAGENTA,
    "Informática": CYAN,
    "Literatura": ROJO,
    "Filosofía": VERDE,
    "No hay clase": GRIS
}

# Encabezado
print(f"{'Hora':<10}", end="")
for dia in dias:
    print(f"{dia:<20}", end="")
print()
print("-" * (10 + 20 * len(dias)))

# Filas con colores
for i, hora in enumerate(horas):
    print(f"{hora:<10}", end="")
    for dia in dias:
        asignatura = clases[dia][i]
        color = colores.get(asignatura, RESET)
        print(f"{color}{asignatura:<20}{RESET}", end="")
    print()
