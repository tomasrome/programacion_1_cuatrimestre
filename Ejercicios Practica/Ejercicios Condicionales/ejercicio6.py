# Escribir un programa que pida al usuario dos números y devuelva su división. Si el usuario introduce el divisor cero debera imprimir un mensaje de error.

primer_numero = float(input("Ingrese el primero número: "))
segundo_numero = float(input("Ingrese el segundo número: "))

if segundo_numero == 0:
    print("¡ERROR! No se puede dividir por 0.")
else:
    print("Resultado:",primer_numero / segundo_numero)