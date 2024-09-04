# Solicitarle al usuario que ingrese una palabra y que nuestro
# algoritmo cuente cuántas vocales tiene utilizando un bucle for.


palabra = input("Ingrese una palabra: ")

contador_vocales = 0

for i in palabra:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        contador_vocales += 1

print(contador_vocales)