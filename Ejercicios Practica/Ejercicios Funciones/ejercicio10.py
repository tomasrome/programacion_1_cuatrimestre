# Debe crear un programa que permita ingresar una edad (entre 1 y 99 años, validar mediante una funcion) 
# y un género (‘F’, ‘M’,  ‘X’, validar mediante una funcion). En caso de ingresar valores erróneos 
# (edad fuera de rango, o generos inexistentes), informar de esa situación mostrando un mensaje
#  y terminar el programa. Si todos los datos fueron bien ingresados, 
# el programa debe ser capas de indicar, sabiendo que las mujeres se jubilan a los 60 años o mas, 
# los hombres con 65 años o mas, para los no binarios establecemos un promedio de ambas edades.
# Determinar mediante funciones si una persona puede o no jubilarse.


def validar_edad(edad):

    edad_correcta = True

    if edad < 1 and edad > 99:
        edad_correcta = False
    
    return edad_correcta

def validar_genero(genero):

    genero_correcto = True

    if genero != "F" or genero != "M" or genero != "X":
        genero_correcto = False
    
    return genero_correcto

edad = int(input("Ingrese su edad: "))
validar_edad(edad)
genero = input("Ingrese su genero F / M / X: ")
validar_genero(genero)

