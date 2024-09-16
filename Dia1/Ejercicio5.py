#Solicita al usuario un número del 1 al 7 y muestra el día de la semana correspondiente (1 = Lunes,7 = Domingo).
def diasdelasemana(dias):
    match str (dias):
        case '1': 
            return "lunes"
        case '2':
            return "martes"
        case '3':
            return  "miercoles" 
        case '4':
            return "jueves"
        case '5':
            return "viernes"
        case '5':
            return "sabado"
        case '6':
            return "domingo"
        case _:
            return "invalido"
dias = int(input("ingrese el numero del dia que quiere ver"))
diaseleccionado = diasdelasemana (dias)
print ("El dia de la semana es: " , diaseleccionado) 


