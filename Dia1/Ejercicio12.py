#Solicita al usuario su peso (en kg) y su altura (en metros). Calcula el IMC y clasifícalo en bajo peso
#(<18.5), peso normal (18.5-24.9), sobrepeso (25-29.9), o obesidad (>=30).
 
def calcular_Imc(peso, altura):

    formula = peso/altura**2

    if (formula<18.5):
        print("Bajo peso")
    elif(18.5 <= formula <= 24.9):
        print("Peso ideal")
    elif(25 <= formula <= 29.9):
        print("Sobrepeso")
    else:
        print("obesidad")
    return formula

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
resultadoImc = calcular_Imc(peso, altura)
print("su indice de masa corporal es: ", resultadoImc)