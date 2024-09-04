# Escribir un programa que almacene la cadena de caracteres prog1Div115 en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable

contrasenia = "prog1Div115"

contrasenia_usuario = input("Ingrese la contraseña: ")

if contrasenia_usuario == contrasenia:
    print("¡Genial, la contraseña ingresada coincide con la contraseña guardada!")
else:
    print ("La contraseña ingresada NO coincide con la contraseña guardada.")