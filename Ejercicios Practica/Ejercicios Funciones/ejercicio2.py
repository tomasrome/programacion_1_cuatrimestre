# Escribir una función a la que se le pase una cadena <nombre> y 
# muestre por pantalla el saludo ¡hola <nombre>!.
# Llamarla dos veces con diferentes cadenas (nombre) en cada llamada


nombre = "Enzo"

def saludo(name):
    print(f"¡Hola {name}!")

saludo(nombre)

nombre = "Fernando"

saludo(nombre)