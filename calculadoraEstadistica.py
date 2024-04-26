'''
Calculadora de Estadísticas Básicas

Objetivo: Crear una calculadora que pueda calcular algunas estadísticas básicas de un conjunto de números dados, como la media,
la mediana, la desviación estándar, etc.
Tips:
Investiga las fórmulas necesarias para calcular la media, la mediana, la desviación estándar, etc.
Utiliza funciones para modularizar tu código y hacerlo más legible.
Considera cómo manejar entradas de usuario para diferentes conjuntos de datos.
Resultado: Una calculadora que pueda calcular la media, la mediana, la desviación estándar,
y otras estadísticas básicas de un conjunto de números.
'''

import math

# Definimos una lista vacía para almacenar los números
numeros = []

# Función que pide al usuario que introduzca los números
def introducir_numeros():
    print("Introduce los números uno por uno. Ingresa una letra para terminar.")
    while True:
        entrada = input("Introduce un número: ")
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            break

# Función que muestra el menú de opciones
def menu():
    print("1. Calcular la media")
    print("2. Calcular la mediana")
    print("3. Calcular la varianza")
    print("4. Calcular la desviación estándar")
    print("5. Calcular la moda")
    print("6. Calcular el rango")
    print("7. Calcular la suma")
    print("8. Calcular el producto")
    print("9. Calcular la potencia")
    print("10. Calcular el factorial")
    print("11. Calcular el coeficiente binomial")
    print("12. Salir")

# Función que muestra el resultado de la operación seleccionada
def mostrar_resultado(opcion):
    if opcion == 1:
        print("La media es:", media(numeros))
    elif opcion == 2:
        print("La mediana es:", mediana(numeros))
    elif opcion == 3:
        print("La varianza es:", varianza(numeros))
    elif opcion == 4:
        print("La desviación estándar es:", desviacion_estandar(numeros))
    elif opcion == 5:
        print("La moda es:", moda(numeros))
    elif opcion == 6:
        print("El rango es:", rango(numeros))
    elif opcion == 7:
        print("La suma es:", suma(numeros))
    elif opcion == 8:
        print("El producto es:", producto(numeros))
    elif opcion == 9:
        base = float(input("Introduce la base: "))
        exponente = int(input("Introduce el exponente (debe ser un número entero): "))
        print("La potencia es:", potencia(base, exponente))
    elif opcion == 10:
        numero = int(input("Introduce un número entero positivo: "))
        print("El factorial es:", factorial(numero))
    elif opcion == 11:
        n = int(input("Introduce n: "))
        k = int(input("Introduce k: "))
        print("El coeficiente binomial es:", coeficiente_binomial(n, k))

# Función que calcula la media de un conjunto de números
def media(numeros):
    return sum(numeros) / len(numeros)

# Función que calcula la mediana de un conjunto de números
def mediana(numeros):
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    if n % 2 == 0:
        return (numeros_ordenados[n // 2 - 1] + numeros_ordenados[n // 2]) / 2
    else:
        return numeros_ordenados[n // 2]
    
# Función que calcula la varianza de un conjunto de números
def varianza(numeros):
    n = len(numeros)
    media_numeros = media(numeros)
    return sum((x - media_numeros) ** 2 for x in numeros) / n

# Función que calcula la desviación estándar de un conjunto de números
def desviacion_estandar(numeros):
    return math.sqrt(varianza(numeros))

# Función que calcula la moda de un conjunto de números
def moda(numeros):
    numeros_ordenados = sorted(numeros)
    moda = max(set(numeros_ordenados), key=numeros_ordenados.count)
    return moda

# Función que calcula el rango de un conjunto de números
def rango(numeros):
    return max(numeros) - min(numeros)

# Función que calcula la suma de un conjunto de números
def suma(numeros):
    return sum(numeros)

# Función que calcula el producto de un conjunto de números
def producto(numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

# Función que calcula la potencia de un número
def potencia(base, exponente):
    return base ** exponente

# Función que calcula el factorial de un número
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)
    
# Función que calcula el coeficiente binomial de dos números
def coeficiente_binomial(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

# Llamamos a la función para introducir números
introducir_numeros()

# Bucle principal del programa
while True:
    # Mostramos el menú
    menu()
    # Pedimos al usuario que seleccione una opción
    opcion = input("Selecciona una opción: ")
    # Verificamos si la opción es válida
    if opcion.isdigit() and 1 <= int(opcion) <= 12:
        opcion = int(opcion)
        # Si la opción es 12, salimos del bucle y terminamos el programa
        if opcion == 12:
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break
        else:
            # Mostramos el resultado de la operación seleccionada
            mostrar_resultado(opcion)
    else:
        print("Opción no válida. Por favor, selecciona un número del 1 al 12.")