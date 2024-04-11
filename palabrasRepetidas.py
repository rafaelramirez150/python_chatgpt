'''
crearemos un programa que calcule la frecuencia de palabras en un texto dado.
Este programa contará cuántas veces aparece cada palabra en el texto y mostrará el resultado al usuario.

Pide al usuario que ingrese el texto en el que desea contar las palabras.
Divide el texto en palabras utilizando el método split() de las cadenas.
Utiliza un diccionario para almacenar las palabras y su frecuencia.
Itera sobre la lista de palabras y actualiza el diccionario de frecuencias.
Finalmente, imprime el diccionario de frecuencias para mostrar la cantidad de veces que aparece cada palabra.
'''
palabras = input("Ingrese un texto: ").lower().split()  # Convertir el texto a minúsculas y luego dividirlo en palabras
frecuencia = {} # Diccionario para almacenar la frecuencia de las palabras

# Iterar sobre la lista de palabras y actualizar el diccionario de frecuencias
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1 # Incrementar la frecuencia si la palabra ya está en el diccionario
    else:
        frecuencia[palabra] = 1 # Agregar la palabra al diccionario con una frecuencia inicial de 1

print(frecuencia)