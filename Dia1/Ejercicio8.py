#Solicita al usuario que ingrese un año y determina si es bisiesto (divisible entre 4, pero no entre 100, salvo que sea divisible entre 400).
def aniobisiesto(anio):
    if(anio % 4==0 and anio % 100 !=0) or (anio % 400 ==0):
        return True
    else:
        return False
anio= int(input("Ingrese el año que desea saber si es bisiesto"))
if aniobisiesto (anio):
    print ("¡El año es bisiesto!")
else:
    ("El año no es bisiesto")
        

               