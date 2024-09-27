# Escribe una función llamada busqueda_varias_apariciones(lista, objetivo) que 
# implemente la búsqueda lineal para encontrar todas las posiciones donde el número aparece.

# Pistas:
# -Utiliza un bucle para recorrer la lista.
# -Guarda cada índice donde el número aparece en una nueva lista.
# -Si no encuentras el número en ninguna posición, devuelve una lista vacía.
# -¡NOO se permite utilizar append!


def busqueda_varias_apariciones(lista, objetivo):

    resultado = []

    for i in range(len(lista)):
        if lista[i] == objetivo:
            resultado += [i]

    return resultado


lista = [1,3,5,7,45,232,5,12,5]

print(busqueda_varias_apariciones(lista,5))