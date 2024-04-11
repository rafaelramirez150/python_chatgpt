'''
crear un programa que genere una lista de números primos en un rango dado. Aquí tienes algunos consejos:

Utiliza la función input() para pedir al usuario que ingrese un rango de números (inicio y fin).
Usa la función int() para convertir los valores ingresados a enteros.
Implementa una función para verificar si un número dado es primo.
Utiliza un bucle para iterar sobre todos los números en el rango y verifica si son primos utilizando la función creada en el paso anterior.
Agrega los números primos a una lista.
Imprime la lista de números primos.
'''
inicio = int (input("Ingrese el inicio del rango de números: "))
fin = int (input("Ingrese el final del rango de números: "))

# Función para verificar si un número es primo
def es_primo(numero):
    if numero < 2: # Agregado para que los números menores a 2 no sean considerados primos
        return False
    if numero ==2: # Agregado para que el 2 sea considerado primo
        return True
    for i in range(2, numero): # Cambiado el rango de 2 a numero
        if numero % i == 0:
            return False
    return True

# Lista de números primos
primos = []

# Iterar sobre el rango de números y agregar los primos a la lista
for i in range(inicio, fin + 1 ):
    if es_primo(i):
        primos.append(i)

# Imprimir la lista de números primos
print(primos)