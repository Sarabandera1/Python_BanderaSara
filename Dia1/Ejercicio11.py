#Solicita al usuario que ingrese una temperatura y una escala (C o F). Convierte la temperatura a la
#escala opuesta usando match .
fahrenheit= 17.2
Celsius= 33.8
def temperaturas(celsius, fahrenheit, operacion):
    match operacion:
        case 'Celsius ': 
            return (Celsius*9/5) + 32
        case 'fahrenheit':
            return (fahrenheit -32) *5/9
        case _:
            return "operacion no valida"
Celsius= float(input("ingrese primer numero: "))
fahrenheit= float(input("ingrese segundo numero: "))
operacion= input("Ingrese tipo de operacion quiere hacer, Celsius o fahrenheit " )
resultado= temperaturas (Celsius, fahrenheit, operacion)
print ("resultado: ", resultado)
