# Escribe una función llamada celsius_a_fahrenheit que tome una temperatura 
# en grados Celsius como argumento y devuelva su equivalente en grados Fahrenheit.

def celsius_a_fahrenheit(temperatura):

    fahrenheit = temperatura * 9/5 + 32
    
    return print(f"{temperatura}° Celsius = {fahrenheit}° Fahrenheit")

celsius_a_fahrenheit()