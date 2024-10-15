"""
EnergiaPlus tiene un lote de registros con la información de las ventas de cada una de las estaciones de servicio que posee. 
Por cada estación hay un registro con la siguiente información:
- Código de estación, cantidad de nafta vendida y cantidad de gasoil vendido.
El lote termina cuando se ingresa un código de estación igual a 0. Se pide calcular e informar:
a) La cantidad de estaciones.
b) El código de estación que vendió mayor cantidad de nafta.
c) El promedio general de gasoil vendido entre todas las estaciones.
"""

codigo_estacion = 1
lista_estaciones = []


def validar_es_numero(valor_input:str)->int:
    '''
    Verifica que el valor ingresado no sea un string vacio y que sea un número entero positivo. Finalmente convierte el str a int.
    Parametro: valor_input (str)
    Retorno: valor_input (int)
    '''
    while valor_input == "" or not valor_input.isdigit() or valor_input.startswith("-") or "." in valor_input:
        valor_input = input("Debe ingresar un número valido. Vuelva a intentar: ")
    valor_input = int(valor_input)
    return valor_input

def agregar_estacion(codigo_estacion, cantidad_nafta, cantidad_gasoil):

    estaciones = [codigo_estacion, cantidad_nafta, cantidad_gasoil]

    return estaciones


def estacion_mayor_venta_nafta(estaciones):

    cantidad_nafta_mayor = estaciones[0][1]
    codigo_estacion_nafta_mayor = estaciones[0][0]

    for i in range(len(estaciones)):
        if estaciones[i][1] > cantidad_nafta_mayor:
            cantidad_nafta_mayor = estaciones[i][1]
            codigo_estacion_nafta_mayor = estaciones[i][0]
    
    return codigo_estacion_nafta_mayor


def cantidad_estaciones(lista_estaciones):

    cantidad_estaciones = len(lista_estaciones)

    return cantidad_estaciones


def promedio_general_gasoil(lista_estaciones):

    total_gasoil = 0

    for i in range(len(lista_estaciones)):
        total_gasoil += lista_estaciones[i][2] 
    
    promedio_general_gasoil = total_gasoil // len(lista_estaciones)
    return promedio_general_gasoil

while codigo_estacion != 0:

    codigo_estacion = input("Ingrese el codigo de la estacion, para terminar ingresar 0: ")
    codigo_estacion = validar_es_numero(codigo_estacion)

    if codigo_estacion != 0:
        cantidad_nafta = input("Ingrese la cantidad de nafta vendida en L: ")
        cantidad_nafta = validar_es_numero(cantidad_nafta)

        cantidad_gasoil = input("Ingrese la cantidad de gasoil vendido en L: ")
        cantidad_gasoil = validar_es_numero(cantidad_gasoil)

        lista_estaciones.append(agregar_estacion(codigo_estacion, cantidad_nafta, cantidad_gasoil))
    else:
        lista_estaciones = [[0,0,0]]


print(f"La estacion que vendio mas nafta fue la estacion N° {estacion_mayor_venta_nafta(lista_estaciones)}")
print(f"Total de estaciones: {cantidad_estaciones(lista_estaciones)}")
print(f"El promedio de gasoil es de: {promedio_general_gasoil(lista_estaciones)} Litros")


