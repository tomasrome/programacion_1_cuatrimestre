"""Escribir un programa que imprima un patrón como el siguiente teniendo
como input un 5 (puede ser en Código o diagrama):

123454321
1234 4321
123   321
12     21
1       1  
"""

def pantalones(numero):

    for i in range(numero):
        for j in range(1, numero-i+1):
            print(j, end = "")
            
        if i > 0:
            cantidad_espacio = (i * 2) - 1
            print(" " * cantidad_espacio, end="" )
            
        if i == 0:
            for j in range(numero - 1, 0, -1):
                print(j, end = "")
        else:
            for j in range(numero - i, 0, -1):
                print(j, end = "")
        print()


pantalones(5)











