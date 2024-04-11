'''
crear un programa que genere una contraseña segura de forma aleatoria.
Una contraseña segura suele tener una combinación de letras (mayúsculas y minúsculas), números y caracteres especiales.
Aquí tienes algunos consejos para construir el programa:

Utiliza la biblioteca random para generar caracteres aleatorios.
Define una lista de caracteres que puedas usar para crear la contraseña, incluyendo letras (mayúsculas y minúsculas),
números y caracteres especiales.
Pide al usuario que ingrese la longitud deseada para la contraseña.
Utiliza un bucle para seleccionar caracteres aleatorios de la lista y construir la contraseña.
Imprime la contraseña generada y asegúrate de que sea lo suficientemente segura.
'''

import random
import string

def generar_contrasena():

     # lista de caracteres que se pueden usar para generar la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    longitud = int(input("Ingrese la longitud de la contraseña: "))
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud)) # lista de comprensión que genera la contraseña
    return contrasena

print(generar_contrasena())