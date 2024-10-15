"""
Hacer una función llamada Redondear que reciba como parámetro un número float y devuelva un número entero con el redondeo del mismo. NO SE PUEDEN UTILIZAR FUNCIONES INTEGRADAS DE PYTHON 

Por ejemplo:
Si recibe 7.78, debe devolver 8.
Si recibe 7.48, debe devolver 7.
Si recibe 7.5, debe devolver 8.
"""

def redondear(numero:float)->int:
    
    parte_entera = int(numero)

    parte_decimal = numero - parte_entera

    if parte_decimal > 0.4:
        return parte_entera + 1
    else:
        return parte_entera



print(redondear(7.34))
print(redondear(7.83))
print(redondear(2.33))