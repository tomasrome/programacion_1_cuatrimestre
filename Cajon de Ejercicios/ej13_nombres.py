"""
# Buscar los nombres comunes en ambas listas guardarlos en otra e imprimirla
lista_a = ['Oralie' ,'Imojean' ,'Michele', 'Ailbert', 'Stevy']
lista_b = ['Jayson', 'Oralie' ,'Michele', 'Stevy', 'Alwyn']
"""

lista_a = ['Oralie' ,'Imojean' ,'Michele', 'Ailbert', 'Stevy']
lista_b = ['Jayson', 'Oralie' ,'Michele', 'Stevy', 'Alwyn']

nombres_comunes = []

for nombre in lista_a:
    if nombre in lista_b:
        nombres_comunes.append(nombre)

print(nombres_comunes)

