#Escribe un programa que solicite al usuario ingresar el día, el mes y el año de
#una fecha. Luego, verifica si la fecha es válida o no. Considera los diferentes
#casos, como los días de cada mes y si el año es bisiesto. Muestra un mensaje
#indicando si la fecha es válida o no.

import calendar

def es_bisiesto(anio):
    return calendar.isleap(anio)


def es_fecha_valida(dia, mes, anio):
    if mes < 1 or mes > 12:
        return False
    

    if dia < 1 or dia > calendar.monthrange(anio, mes)[1]:
        return False
    
    return True


dia = int(input("Ingresa el día (1-31): "))
mes = int(input("Ingresa el mes (1-12): "))
anio = int(input("Ingresa el año: "))


if es_fecha_valida(dia, mes, anio):
    print(f"La fecha {dia}/{mes}/{anio} es válida.")
else:
    print(f"La fecha {dia}/{mes}/{anio} es inválida.")