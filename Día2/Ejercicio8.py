#Escribe un programa que solicite al usuario
#ingresar un número y luego muestre la tabla
#de multiplicar de ese número del 1 al 10

num=int(input("ingrese un numero: "))
tablaInicio=1

while tablaInicio<=10:
    print(f'{num}*{tablaInicio} = {num*tablaInicio} ')
    tablaInicio=tablaInicio+1