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

def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

if es_palindromo(palindromo):
    print(f"{palindromo} es un palíndromo.")
else:
    print(f"{palindromo} no es un palíndromo.")
