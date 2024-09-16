#Escribe un programa que genere un número aleatorio entre 1 y 100 y permita al usuario
#adivinarlo. El programa debe dar pistas si el número ingresado es mayor o menor que el número
#secreto. Usa un ciclo while para permitir al usuario seguir intentando hasta que adivine el
#número
import random

numero_secreto = random.randint(1, 100)

print("Adivina el número")

adivinanza = None

while adivinanza != numero_secreto:
    adivinanza = int(input("coloca el número: "))

    if adivinanza < numero_secreto:
        print("Ese no es")
    elif adivinanza > numero_secreto:
        print("Ese tampoco")
    else:
        print(f" Le diste al blanco: {numero_secreto}.")