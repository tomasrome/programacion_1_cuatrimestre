
def validar_edad(edad:int)->int: 
    
    if edad.isdigit():
        return edad
    else:
        while not edad.isdigit():
            edad = input("Valor invalido. Reingrese la edad: ")

def validar_sintomas(sintoma):
    SINTOMAS = ["fiebre","dolor de cabeza"]
    
    if sintoma in SINTOMAS:
        return sintoma
    else:
        while not  sintoma in SINTOMAS:
            sintoma = input("Sintoma invalido. Vuelva a ingresar: ")