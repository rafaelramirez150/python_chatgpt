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

numeros = input("Ingrese una lista de números separados por comas: ")

if len(numeros) < 1:
    print("No se ingresaron números")
else:
    lista = []
    for i in range(numeros):
        numeros.append(int(i))
    media, mediana, desviacion_estandar = calcular_estadisticas(numeros)
    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Desviación estándar: {desviacion_estandar}")


def calcular_media(numeros):
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    if n % 2 == 0:
        mediana = (numeros_ordenados[n//2 - 1] + numeros_ordenados[n//2]) / 2
    else:
        mediana = numeros_ordenados[n//2]
    return mediana

def calcular_desviacion_estandar(numeros):
    media = calcular_media(numeros)
    n = len(numeros)
    suma = sum((x - media) ** 2 for x in numeros)
    desviacion_estandar = (suma / n) ** 0.5
    return desviacion_estandar

def calcular_estadisticas(numeros):
    media = calcular_media(numeros)
    mediana = calcular_mediana(numeros)
    desviacion_estandar = calcular_desviacion_estandar(numeros)
    return media, mediana, desviacion_estandar
