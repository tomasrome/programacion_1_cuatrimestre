
def validar_km(km):

    if km.isdigit():
        return km
    else:
        while not km.isdigit():
            km = input("Valor invalido. Vuelva a ingresar: ")



nombre_perro = input("Nombre del perro")
km_recorridos = validar_km(input("Km recorridos: "))

