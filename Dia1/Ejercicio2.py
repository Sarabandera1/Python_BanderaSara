#Solicita al usuario una calificación y determina si la nota es aprobatoria (>= 60) o reprobatoria (<60).
nota=int (impot ("ingrese nota final"))
aprobado=nota>60
reprobado=nota<60
if (nota>=60):
    print (aprobado)
else:
    Print (reprobado)