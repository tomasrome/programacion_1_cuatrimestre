# Escribe una función llamada calculo_de_imc que reciba una altura y el peso
# e indique el indice de masa CORPORAL (IMC) de una persona.
# Peso inferior al normal	imc < de 18.5
# Normal imc entre 18.5 – 24.9
# Peso superior al normal  imc entre 25.0 – 29.9
# Obesidad	imc > de 30.0

def calculo_de_imc(peso,altura):
    
    imc = peso / altura ** 2
    if imc > 30:
        res_imc = "Obesidad"
    elif imc > 25:
        res_imc = "Peso superior al normal "
    elif imc > 18.5:
        res_imc = "Normal"
    else:
        res_imc = "Peso inferior al normal"
    
    return print(f"Masa corporal (IMC): {res_imc}")

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura en metros: "))

calculo_de_imc(peso,altura)