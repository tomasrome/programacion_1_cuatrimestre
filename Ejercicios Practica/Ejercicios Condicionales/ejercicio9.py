# Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es vocal”. 

letra = input("Ingrese una letra: ")

match letra:
    case "A" | "a":
        print("Es vocal")
    case "E" | "e":
        print("Es vocal")
    case "I" | "i":
        print("Es vocal")
    case "O" | "o":
        print("Es vocal")
    case "U" | "u":
        print("Es vocal")
    case _:
        print("NO es vocal.")