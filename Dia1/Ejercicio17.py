#Solicita la calificación del estudiante y pregunta si hizo tareas adicionales. Si la respuesta es "sí",
#añade un 5% extra a la calificación, pero si la calificación supera 100, ajústala a 100. Si la respuesta
#es "no", simplemente muestra la calificación original.
def tareasadicionales (nota, respuesta):
    match str (respuesta):
        case "si":
          return nota + 5
        case "no":
          return nota
        case _:
            return "respuesta invalida"

nota= float(input("¿Cual es su nota:  "))
respuesta= input("¿Hizo trabajo adicional?:")
resultado = tareasadicionales(nota, respuesta)
notaMaxima = 100
if nota>= notaMaxima:
    print("su nota final fue: ", notaMaxima)
else:
    print("su nota final fue: ", resultado)

    