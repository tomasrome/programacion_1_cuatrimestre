# Calcula la suma de todos los números pares del 1 al 50 utilizando un bucle for.

acumulador_suma = 0

for i in range(1,51):
    if i % 2 == 0:
        acumulador_suma += i
        print(i)

print(acumulador_suma)