# Escribí un programa que solicite al usuario el ingreso de dos números diferentes y muestre en pantalla al mayor de los dos.
# Y si son iguales tambien mostrar por pantalla que son iguales.

primer_numero = float(input("Ingrese el primero número: "))
segundo_numero = float(input("Ingrese el segundo número: "))

if primer_numero > segundo_numero:
    print(f"{primer_numero} es mayor a {segundo_numero}")
elif primer_numero < segundo_numero:
    print(f"{segundo_numero} es mayor a {primer_numero}")
else:
    print("Los números son iguales.")