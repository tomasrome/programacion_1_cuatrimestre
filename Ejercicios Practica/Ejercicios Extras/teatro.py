"""
Una sala teatral asigna el valor a las entradas de acuerdo al siguiente criterio:
- Lunes y martes: 70% de la tarifa total
- Miércoles: 50% de la tarifa total.
- Jueves a domingos: 100 % de la tarifa total ($ 15000).

Hacer un programa para que dados un día de la semana (1 a 7), y una cantidad, se informe el importe de las entradas.
"""

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

def validar_dia_semana(dia:str)->int:
    '''
    Verifica que el valor ingresado se encuentre entre los 7 dias de la semana.
    Parametro: dia (str)
    Retorno: dia (int)
    '''
    dia = validar_es_numero(dia)

    while dia < 1 or dia > 7:
        dia = input("El número ingresado no corresponde a ningun día de la semana. Vuelva a ingresar: ")
        dia = validar_es_numero(dia)
    return dia

VALOR_ENTRADA = 15000
descuento_por_dia = [70,70,50,100,100,100,100]

dia = input("Ingrese el dia de la semana (1 - 7): ")
dia = validar_dia_semana(dia)

cantidad_entradas = input("Ingrese la cantidad de entradas: ")
cantidad_entradas = validar_es_numero(cantidad_entradas)

importe_total = (VALOR_ENTRADA * (descuento_por_dia[dia - 1]) // 100) * cantidad_entradas

print(f"Importe total: ${importe_total}")