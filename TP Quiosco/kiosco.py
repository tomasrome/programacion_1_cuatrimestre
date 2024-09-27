from validates import validar_producto_vender, validar_cantidad_producto

def vender(inventario):
    
    continuar = "s"
    total_a_pagar = 0
    largo_lista= len(inventario)
    
    while continuar == "s":

        print("\nProductos para vender: ")

        # Imprimimos el inventario con el número del producto
        for i in range(len(inventario)): 
            print(f"[{i+1}] {inventario[i][0]} | ${inventario[i][2]}")

        #El usuario ingresa los datos
        print("---------------------------")
        numero_producto = input("Ingrese el número del producto a vender: ")
        numero_producto = validar_producto_vender(numero_producto, largo_lista)
        cantidad = input("Ingrese la cantidad: ")
        
        cantidad_disponible = inventario[numero_producto-1][1]

        cantidad = validar_cantidad_producto(cantidad, cantidad_disponible)
        '''#Validamos que la cantidad ingresara no supere al stock disponible
        
        while cantidad_disponible - cantidad < 0:
            print("¡Cantidad no disponible!")
            print(f"Stock disponible: {cantidad_disponible}")
            cantidad = int(input("Ingrese una cantidad valida:"))'''
        
        #Descontamos el producto del inventario y calculamos el total a pagar
        inventario[numero_producto-1][1] = cantidad_disponible - cantidad
        total_a_pagar = total_a_pagar + inventario[numero_producto-1][2] * cantidad

        continuar = input("¿Desea vender otro producto? s / n: ").lower()

    mensaje_final = f'''\n¡OPERACIÓN EXITOSA!
    Total a pagar: ${total_a_pagar}
'''
    print(mensaje_final)

    return inventario


