from reglas import mostrar_reglas
from juego import jugar
import random

salida = False

print('\n\033[32m¡BIENVENIDO A "EL RETORNO DEL NÚMERO SECRETO"!\033[0m')

while salida == False:
    mensaje_menu = '''
    MENU:    
    \033[34m1-\033[0m JUGAR
    \033[34m2-\033[0m MOSTRAR LAS REGLAS DEL JUEGO
    \033[34m3-\033[0m SALIR

    Elegir entre una de las opciones \033[34m1\033[0m - \033[34m2\033[0m - \033[34m3\033[0m: '''

    eleccion_menu = int(input(mensaje_menu))
    while eleccion_menu != 1 and eleccion_menu != 2 and eleccion_menu != 3:
        eleccion_menu = int(input("Valor invalido. Reingrese su elección: "))
    
    match eleccion_menu:
        case 1:
            numero_secreto = random.randint(1,10)
            jugar(numero_secreto)
        case 2:
            mostrar_reglas()
        case _:
            print("¡Gracias por jugar!")
            salida = True