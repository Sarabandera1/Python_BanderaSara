#Escribe un programa que solicite al usuario ingresar números enteros indefinidamente. El
#programa debe sumar los números siempre que sean pares, pero debe detenerse si el usuario
#ingresa un número impar. Usa un ciclo while para lograr esto.
suma = 0
print("Ingresa un número par: ")

while True:
    numero = int(input("Ingresa un número entero: "))
    if numero % 2 != 0:
        break

    if numero % 2 == 0:
        suma += numero

print(f"la suma de los números enteros es: {suma}")