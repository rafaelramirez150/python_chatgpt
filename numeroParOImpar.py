'''
vamos a hacer un programa que determine si un número ingresado por el usuario es par o impar.

Utiliza la función input() para pedir al usuario que ingrese un número.
Usa la función int() para convertir el valor ingresado a un entero.
Utiliza el operador % (módulo) para verificar si el número es divisible por 2.
Si el resto de dividir el número por 2 es 0, entonces es par; de lo contrario, es impar.
Imprime un mensaje indicando si el número es par o impar.
'''
numero = int(input("Ingrese un numero:"))

if numero % 2 ==0:
    print("El numero es par")
else:
    print("El numero es impar")