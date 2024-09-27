

def validar_producto_vender(producto, largo_lista):

    #validamos que no se ingrese un string vacio, que el número no sea negativo y que el número(str) ingresado sea un número.
    while producto == "" or producto.startswith("-") or not producto.isdigit():
        producto = input("Debe ingresar un número valido. Vuelva a intentar: ")

    #validamos que el número este dentro del rango de la lista, si la lista tiene 10 posiciones el número no puede valer 11
    producto = int(producto)
    while producto > largo_lista:
        producto = input("Número fuera de rango. Vuelva a intentar: ")
        #volvemos a hacer la primer validación
        while producto == "" or producto.startswith("-") or not producto.isdigit():
            producto = input("Debe ingresar un número valido. Vuelva a intentar: ")
        producto = int(producto)

    return producto


def validar_cantidad_producto(cantidad, cantidad_disponible):

    while cantidad == "" or cantidad.startswith("-") or not cantidad.isdigit():
        cantidad = input("Debe ingresar un número valido. Vuelva a intentar: ")

    cantidad = int(cantidad)    

    while cantidad_disponible - cantidad < 0:
        print("¡Cantidad no disponible!")
        print(f"Stock disponible: {cantidad_disponible}")
        cantidad = input("Ingrese una cantidad valida:")

        while cantidad == "" or cantidad.startswith("-") or not cantidad.isdigit():
            cantidad = input("Debe ingresar un número valido. Vuelva a intentar: ")
        cantidad = int(cantidad)
    
    return cantidad
