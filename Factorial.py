'''
programa que calcule el factorial de un número ingresado por el usuario

Utiliza la función input() para pedir al usuario que ingrese un número.
Usa la función int() para convertir el valor ingresado a un entero.
Implementa una función para calcular el factorial. Puedes hacerlo usando un bucle for o un enfoque recursivo.
Maneja el caso especial del factorial de 0, que es 1.
Imprime el resultado del factorial.
'''
# se define una función llamada calcular_factorial que toma un número como argumento y devuelve su factorial.
def calcular_factorial(numero):
    if numero == 0:
        return 1
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

# se maneja el ingreso del número por parte del usuario y se llama a la función calcular_factorial.
try:
    numero = int(input("Ingrese un número entero positivo: "))
    if numero < 0:
        print("Error: Debe ingresar un número positivo.")
    else:
        resultado = calcular_factorial(numero)
        print("El factorial de", numero, "es", resultado)
except ValueError: # se maneja el caso en que el usuario ingrese un valor no entero.
    print("Error: Debe ingresar un número entero.")

'''
la lógica de cálculo del factorial a una función separada para mejorar la modularidad y reutilización del código.
Además, puedes agregar un manejo de error para asegurarte de que el usuario ingrese un número positivo.
'''