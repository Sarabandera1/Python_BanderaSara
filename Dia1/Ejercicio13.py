#Solicita al usuario que ingrese tres números y determina cuál es el mayor.
num1=int (input ("ingrese el primer numero"))
num2 = int (input("Ingrese el segundo numero: "))
num3=int (input ("ingrese el tercero numero"))

if num1>num2 and num1>num3:
    print ("El primero numero que ingresaste es mayor")
elif num2>num1 and num2>num3:
    print ("El segundo numero que ingresaste es mayor")
else:
    print ("El tercer numero que ingresaste es mayor")
