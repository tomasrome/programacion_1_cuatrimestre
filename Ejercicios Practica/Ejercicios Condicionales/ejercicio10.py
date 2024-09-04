# Dos equipos de futbol están disputando el saque inicial del juego. 
# Los capitanes de cada equipo deciden jugar el clásico juego "Piedra, papel o tijera" para definir quien hace el saque. 
# Las reglas son las usuales: Piedra vence a Tijera, Tijera vence a Papel y Papel vence a Piedra.
# Juegan una sola vez.


primer_capitan = input("- Primer capitan: Elegir en entre Piedra | Papel | Tijera: ")
segundo_capitan = input("- Segundo capitan: Elegir en entre Piedra | Papel | Tijera: ")

match primer_capitan:
    case "Piedra":
        match segundo_capitan:
            case "Piedra":
                print("Empatan")
            case "Papel":
                print("Saca el segundo capitan.")
            case "Tijera":
                print("Saca el primer capitan.")
    case "Papel":
        match segundo_capitan:
            case "Piedra":
                print("Saca el primer capitan.")
            case "Papel":
                print("Empatan")
            case "Tijera":
                print("Saca el segundo capitan.")
    case "Tijera":
        match segundo_capitan:
            case "Piedra":
                print("Saca el segundo capitan.")
            case "Papel":
                print("Saca el primer capitan.")
            case "Tijera":
                print("Empatan.")

