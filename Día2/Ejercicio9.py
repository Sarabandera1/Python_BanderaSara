#Crea un programa que solicite al usuario
#ingresar una serie de números positivos y
#luego calcule e imprima el promedio de los
#números ingresados utilizando un bucle while.
#El programa debe terminar cuando el usuario
#ingrese un número negativo.

total = 0
contador = 0

while True:
    numero = float(input("Ingresa un número positivo (o un número negativo para terminar): "))
    
    if numero < 0:
        break 
    
    total += numero
    contador += 1

if contador > 0:
    promedio = total / contador
    print(f"El promedio de los números ingresados es: {promedio:.2f}")
else:
    print("No ingresaste ningún número positivo.")