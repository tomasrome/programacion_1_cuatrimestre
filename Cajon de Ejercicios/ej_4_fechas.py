"""
Escribir una función llamada validar_fecha que reciba tres valores enteros correspondientes al día, mes y año, y devuelva True si los valores recibidos corresponden a una fecha válida o False si no es válida.

La función debe considerar los siguientes aspectos:
1- Los meses de enero, marzo, mayo, julio, agosto, octubre y diciembre tienen 31 días.
2- Los meses de abril, junio, septiembre y noviembre tienen 30 días.
3- El mes de febrero tiene 28 días en años no bisiestos y 29 días en años bisiestos.
4- Un año es bisiesto si es divisible por 4, pero no por 100, a menos que también sea divisible por 400.

Ejemplos:
validar_fecha(30, 2, 2000) debe devolver False (febrero no tiene 30 días).
validar_fecha(12, 2, 1990) debe devolver True (12 de febrero de 1990 es una fecha válida).
"""


def validar_fecha(dia,mes,anio):

    anio_bisiesto = (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0
    mes_31_dias = dia > 0 and dia <= 31
    mes_30_dias = dia > 0 and dia <= 30
    mes_29_dias = dia > 0 and dia <= 29
    mes_28_dias = dia > 0 and dia <= 28

    match mes:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            if mes_31_dias:
                dia_validado = True
            else:
                dia_validado = False
        case 4 | 6 | 9 | 11:
            if mes_30_dias:
                dia_validado = True
            else:
                dia_validado = False
        case 2:
            if anio_bisiesto:
                if mes_29_dias:
                    dia_validado = True
                else:
                    dia_validado = False
            else:
                if mes_28_dias:
                    dia_validado = True
                else:
                    dia_validado = False
        case _:
            dia_validado = False       
            
    return dia_validado

print(validar_fecha(28, 5, 2000))
print(validar_fecha(10, 2, 1990))