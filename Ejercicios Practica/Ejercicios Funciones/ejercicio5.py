# Realizar una función llamada par_o_impar:

# 1-Recibirá un número por parámetro
# 2-Imprimirá Par si el número es par
# 3-Imprimirá Impar si el número es impar
# 4-Si se ingresa algo que no sea número debe indicar 
# que se ingrese un número. (Para pensar un poco más)

def par_o_impar(num):
    pass

numero = input("Ingrese un número: ")
print(type(numero))

while type(numero) != int:
    numero = input("Valor incorrecto, vuelva a ingresar un número: ")
    print(type(numero))