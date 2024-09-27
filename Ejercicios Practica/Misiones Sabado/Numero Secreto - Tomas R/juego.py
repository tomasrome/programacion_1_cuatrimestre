
def jugar(numero_secreto : int)->None:
    """La funcion recibe un número secreto entre el 1 y el 10. Pide al usuario ingresar cual cree que es ese número y si falla 3 veces se revela el numero generado.
    Args:
        numero_secreto (int): El número secreto que el jugador debe adivinar.
    
    Returns:
        None: No retorna ningun valor. Inicializa el juego.
    """
    
    print("\n\033[32m-COMIENZA EL JUEGO-\n\033[0m")
    numero_usuario = int(input("- Ingrese el Número Secreto: "))
    
    for i in range(1,3):
        if numero_usuario != numero_secreto:
            if i == 2:
                numero_usuario = int(input(f"Número incorrecto, te queda \033[31m1\033[0m intento. Vuelve a intentarlo: "))
            else:
                numero_usuario = int(input(f"Número incorrecto, te quedan \033[31m{3-i}\033[0m intentos. Vuelve a intentarlo: "))
        if numero_usuario == numero_secreto:
            print("\033[32m\n🧙¡Felicidades Padawan!. El Número Secreto a regresado y estas cada día más cerca de convertirte en un gran Maestro Jedi!\033[0m")
            break
        
    if numero_usuario != numero_secreto:
        print(f"\n\033[31mSe acabo el juego, el Número Secreto es \033[0m{numero_secreto}.\n\033[35m🧙 Pero no te desanimes, ¡Incluso los grandes Jedi han conocido la derrota!\033[0m")
        

