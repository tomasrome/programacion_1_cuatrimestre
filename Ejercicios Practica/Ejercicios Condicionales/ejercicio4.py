# Cree un programa que calcule el IMC (Indice de masa corporal). Formula --> IMC=Peso/Altura2 (Peso sobre altura al cuadrado)
# El usuario debera ingresar su peso y su altura (su nombre si quieren y despues imprimirlo concatenado) y el programa ademas de 
# calcular el IMC debera decir en que clasificacion se encuentra.
# La clasificacion la encontraran el archivo de imagen: IMC_clasificacion.jpg


nombre = input("Ingrese su nombre: ")
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / altura ** 2

if imc >= 40:
    clasificacion = "Obesidad grado 3"
elif imc >= 35:
    clasificacion = "Obesidad grado 2"
elif imc >= 30:
    clasificacion = "Obesidad grado 1"
elif imc >= 25:
    clasificacion = "Sobrepeso"
elif imc >= 18.5:
    clasificacion = "Adecuado"
else:
    clasificacion = "Bajo peso"


mensaje_final = f'''
- {nombre}
- {peso} Kg
- {altura} Metros

- IMC = {imc}
- Clasificación: {clasificacion}
'''

print(mensaje_final)