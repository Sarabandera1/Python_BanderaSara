#Escribe un programa que solicite al
#usuario ingresar su calificación en un
#examen y determine si ha aprobado o
#no. Si la calificación es igual o mayor a
#60, muestra el mensaje "Has aprobado".
#De lo contrario, muestra el mensaje "Has
#reprobado".

nota=float(input("ingrese su nota final: "))


aprobado=nota>=60
reprobado=nota<60
    
if (nota>=60):
    print("Aprobado")
else:
    print("Reprobado")