#Nuestra misión:
#Crear un algoritmo en Python que imprima por pantalla si un año es bisiesto o no lo es.

#Para esta misión nos proporcionan la siguiente ayuda:
#El año es bisiesto si es divisible por 4 y no es divisible por 100 o es divisible por 400.

anio = int(input("Ingrese un año para saber si es bisiesto o no: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print(f"(っ＾▿＾)っ {anio} es un año bisiesto.")
else:
    print(f"( ˘︹˘ ) {anio} NO es un año bisiesto.")























