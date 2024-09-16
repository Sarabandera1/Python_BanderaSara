#El programa genera un número aleatorio entre 1 y 10. El usuario debe adivinar el número, y el programa indica si el número ingresado es mayor, menor o igual al número generado.
import random
num= int(input("Ingrese el numero"))
numeroescondido= (random.randint(1, 10))
if (num>numeroescondido):
    print ("El numero es menor")
elif (num<numeroescondido):
    print ("El numero es mayor")
else:
    print ("¡adivinaste!")
    

