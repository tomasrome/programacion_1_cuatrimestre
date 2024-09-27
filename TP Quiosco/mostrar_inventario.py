

def mostrar(inventario):
        print("\nINVENTARIO")
        for i in range(len(inventario)): 
                print(f"[{i+1}] Nombre: {inventario[i][0]} | Stock: {inventario[i][1]} | Precio: ${inventario[i][2]}")

                print("-------------------------------------")