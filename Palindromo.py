'''
Vamos a crear un programa que determine si una cadena de texto ingresada por el usuario es un palíndromo o no.
Un palíndromo es una palabra, frase, número o cualquier otra secuencia de caracteres que se lee igual hacia adelante que hacia atrás.

Utiliza la función input() para pedir al usuario que ingrese una cadena de texto.
Implementa una función para verificar si la cadena es un palíndromo.
Puedes eliminar los espacios en blanco y convertir toda la cadena a minúsculas para simplificar la comparación.
Compara la cadena original con su versión invertida para determinar si es un palíndromo.
Imprime un mensaje indicando si la cadena es un palíndromo o no.
'''
palindromo = input("Ingrese una cadena de texto: ")

# Función para verificar si una cadena es un palíndromo
def es_palindromo(cadena):
    cadena = cadena.lower()
    cadena_sin_espacios = ''.join(c for c in cadena if c.isalnum())  # Ignorar espacios y caracteres no alfanuméricos
    return cadena_sin_espacios == cadena_sin_espacios[::-1]

# Verificar si la cadena es un palíndromo e imprimir el resultado
if es_palindromo(palindromo):
    print(f"{palindromo} es un palíndromo.")
else:
    print(f"{palindromo} no es un palíndromo.")
