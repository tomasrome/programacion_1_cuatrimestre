# Escribir un programa que imprima los números del 1 al 100, 
# pero para múltiplos de tres imprimir 'Fizz' en lugar del número 
# y para los múltiplos de cinco imprimir 'Buzz'. Para los números 
# que son múltiplos tanto de tres como de cinco imprimir "FizzBuzz" 



for i in range(1,101):
    
    fizz = i % 3 == 0
    buzz = i % 5 == 0

    if fizz and buzz:
        print("FizzBuzz")
    elif fizz:
        print("Fizz")
    elif buzz:
        print("Buzz")
    else:
        print(i)


