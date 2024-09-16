#Solicita al usuario que ingrese una temperatura y una escala (C o F). Convierte la temperatura a la
#escala opuesta usando match .
def termometro(grado, temperatura):
    match str (grado):
        case 'Celsius': 
            return (temperatura* 9/5) + 32
        case 'fahrenheit':
            return (temperatura -32) * 5/9
        case _:
            return "operacion no valida"
        
temperatura= float(input("ingrese numero de grados: "))
grado= float(input("Que tipo de convercion desea (celsius o fahrenheit) "))
resultado= termometro (grado, temperatura)
print ("resultado de la convercion: ", resultado)
