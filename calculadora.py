'''
Proyecto 1: Calculadora Simple

Objetivo: Crear una calculadora que pueda realizar operaciones básicas como suma, resta, multiplicación y división.
Tips:
Utiliza las operaciones aritméticas básicas de Python: +, -, *, /.
Puedes utilizar la función input() para obtener la entrada del usuario.
Asegúrate de manejar casos de error, como la división por cero.
Resultado: Una calculadora que pueda realizar operaciones aritméticas básicas.
'''
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

# Verificar si los números ingresados son válidos
try:
    numero1 = float(numero1)
    numero2 = float(numero2)
except ValueError:
    print("Error: Por favor ingresa números válidos.")
    exit()

print("Selecciona la operación que deseas realizar:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

operacion = input("Introduce el número de la operación que deseas realizar: ")

# Verificar si la operación ingresada es válida
if operacion not in ['1', '2', '3', '4']:
    print("Operación no válida")
    exit()

if operacion == '1':
    print(f"El resultado de la suma es: {numero1 + numero2}")
elif operacion == '2':
    print(f"El resultado de la resta es: {numero1 - numero2}")
elif operacion == '3':
    print(f"El resultado de la multiplicación es: {numero1 * numero2}")
elif operacion == '4':
    if numero2 == 0:
        print("Error: No se puede dividir entre 0")
    else:
        print(f"El resultado de la división es: {numero1 / numero2}")
else:
    print("Operación no válida")