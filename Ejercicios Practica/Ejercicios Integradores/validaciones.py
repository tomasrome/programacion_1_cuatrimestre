
def validar_cantidad_gustos(cantidad:str):
    gusto_validado = False

    while gusto_validado == False:
        if (cantidad.isdigit()):
            cantidad = int(cantidad)
            if cantidad > 0 and cantidad <= 4:
                gusto_validado = True
            else:
                cantidad = input("Cantidad invalida. Vuelva a ingresar: ")
        else:
            cantidad = input(f'"{cantidad}" no es un número. Vuelva a ingresar: ')
    return cantidad

def validar_calorias(calorias):
    calorias_validadas = False

    while calorias_validadas == False:
        if (calorias.isdigit()):
            calorias = int(calorias)
            if calorias > 0:
                calorias_validadas = True
            else:
                calorias = input("Cantidad invalida. Vuelva a ingresar: ")
        else:
            calorias = input(f'"{calorias}" no es un número. Vuelva a ingresar: ')
    return calorias

def validar_importe(importe):
    importe_validado = False

    while importe_validado == False:
        if (importe.isdigit()):
            importe = int(importe)
            if importe > 0:
                importe_validado = True
            else:
                importe = input("Cantidad invalida. Vuelva a ingresar: ")
        else:
            importe = input(f'"{importe}" no es un número. Vuelva a ingresar: ')
    return importe + 50

