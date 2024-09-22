import validaciones as vali

contador_gustos = 0

cantidad_gustos_ingresado = input("- Ingrese la cantidad de gustos: ")
total_de_gustos = vali.validar_cantidad_gustos(cantidad_gustos_ingresado)
while contador_gustos < total_de_gustos:
    print("--------------------------------")
    nombre_gusto = input(f"- Nombre del {contador_gustos + 1}° gusto: ")
    calorias_gusto_ingresado = input("- Calorias: ")
    vali.validar_calorias(calorias_gusto_ingresado)
    contador_gustos +=1
print("--------------------------------")
importe_ingresado = input("- Importe: ")
importe_total = vali.validar_importe(importe_ingresado)
nombre_cliente = input("- Nombre del cliente: ")