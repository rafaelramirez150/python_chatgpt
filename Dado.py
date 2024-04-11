'''
crearemos un programa que simule el lanzamiento de un dado.

Utiliza la biblioteca random para generar números aleatorios.
Pide al usuario que ingrese el número de veces que quiere lanzar el dado.
Usa un bucle para simular los lanzamientos del dado.
Genera un número aleatorio entre 1 y 6 para representar las caras del dado.
Imprime el resultado de cada lanzamiento.
'''

import random

# Pide al usuario que ingrese el número de veces que quiere lanzar el dado
lanzamientos = int(input("¿Cuántas veces quieres lanzar el dado?: "))

print("Resultado de los lanzamientos: ")

# Bucle para simular los lanzamientos del dado
for i in range(1, lanzamientos + 1):
    # Genera un número aleatorio entre 1 y 6 para representar las caras del dado
    resultado = random.randint(1, 6)
    # Imprime el resultado de cada lanzamiento
    print(f"Lanzamiento {i}: {resultado}")