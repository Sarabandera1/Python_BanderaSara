#El costo de estacionamiento se calcula de la siguiente manera: Primera hora: $5
#Segunda a cuarta hora: $4 por hora
#Más de cuatro horas: $3 por cada hora adicional
#Solicita al usuario el número de horas de estacionamiento y calcula el costo total.

nummaterias= int(input("Ingrese el numero de materias que ha cursado: "))
materias_aprobadas = 0
for i in rango (nummaterias):
    puntaje = float(input(f"Ingrese el puntaje para la materia {i + 1} ")):
    
    if puntaje >= 60:
        print("La materia se aprobó")
        materiasAprobadas += 1
    else:
        print("Reprobaste")

creditosTotales = materiasAprobadas * 3

print(f"El total de los creditos es: {creditosTotales}")