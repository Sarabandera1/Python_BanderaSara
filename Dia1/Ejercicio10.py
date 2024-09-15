#Solicita una nota numérica y clasifícala como A (90-100), B (80-89), C (70-79), D (60-69), o F (<60).
notas= int(input("ingrese su calificacion: "))
if 90 <= notas <= 100:
    print("A")
elif 80 <= notas <= 89: 
    print("B")
elif 70 <= notas <= 79: 
    print("C")
elif 60 <= notas <= 69: 
    print("D")
else:
    print ("F")
    