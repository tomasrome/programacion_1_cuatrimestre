
continuar = "s"
km_totales = 0
contador_perros = 0
contador_mas_4km = 0
lista_perros = []

def validar_km(km:str)->int:

    if km.isdigit():
        km = int(km)
        return km
    else:
        while not km.isdigit():
            km = input("Valor invalido. Vuelva a ingresar: ")
    km = int(km)
    return km

def cargar_perros(nombre,km):

    perros = [nombre,km]
    return perros


def perro_mayor_km_recorridos(lista):

    km_mayor = lista[0][1]
    perro = 0

    for i in range(len(lista)):
        if lista[i][1] > km_mayor:
            km_mayor = lista[i][1]
            perro = i
    return lista[perro]

def perro_menor_km_recorridos(lista):

    km_minimo = lista[0][1]
    posicion_perro = 0

    for i in range(len(lista)):
        if lista[i][1] < km_minimo:
            km_minimo = lista[i][1]
            posicion_perro = i
    return lista[posicion_perro]

def mensaje_promedio_km(km_recorridos):

    if km_recorridos > 5:
        mensaje = "¡Excelente rendimiento!"
    elif km_recorridos > 1:
        mensaje = "Buen trabajo"
    else:
        mensaje = "Debes caminar más."
    
    return mensaje

while continuar == "s":

    nombre_perro = input("Nombre del perro: ")
    km_recorridos = validar_km(input("Km recorridos: "))

    print(mensaje_promedio_km(km_recorridos))

    lista_perros.append(cargar_perros(nombre_perro,km_recorridos))

    contador_perros += 1
    km_totales += km_recorridos

    if km_recorridos > 3:
        contador_mas_4km += 1

    print("------------------------------")
    continuar = input("¿Desea seguir agregando perros? s / n: ").lower()


promedio_km_total = km_totales / contador_perros
perro_mayor_km = perro_mayor_km_recorridos(lista_perros)
perro_menor_km = perro_menor_km_recorridos(lista_perros)

mensaje = f'''

- El promedio es km recorridos es de: {promedio_km_total} km.
- Cantidad de perros que caminaron más de 4 km: {contador_mas_4km} perros.
- El perro que recorrio más km fue: {perro_mayor_km[0]} con {perro_mayor_km[1]}km.
- El perro que recorrio menos km fue: {perro_menor_km[0]} con {perro_menor_km[1]}km.


'''

print(mensaje)