'''
crearemos un programa que convierta un número decimal en su equivalente en el sistema binario.

Pide al usuario que ingrese un número decimal.
Utiliza el operador de división entera // y el operador de módulo % para dividir el número decimal sucesivamente por 2
y obtener los residuos.
Guarda los residuos en una lista en orden inverso, ya que los residuos se leen del último al primer dígito del número binario.
Finalmente, imprime los residuos guardados en la lista para obtener el número binario.
'''

# Función para convertir un número decimal en binario
def decimal_a_binario(decimal):
    binario = []
    while decimal > 0:
        binario.append(decimal % 2) # Obtener el residuo de la división por 2
        decimal //= 2
    return binario[::-1]  # Invertir la lista antes de devolverla

numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal en binario e imprimir el resultado
print(f"El número binario equivalente es: {''.join(str(d) for d in decimal_a_binario(numero_decimal))}")
