#Utiliza match para implementar una calculadora simple.
def calculadora(num1, num2, operacion):
    match operacion:
        case '+': 
            return num1+num2
        case '-':
            return num1-num2
        case '/':
            return num1/num2 
        case '*':
            return num1*num2
        case _:
            return "operacion no valida"
num1= float(input("Ingrese el primer numero: "))
num2= float(input("Ingrese el segundo numero: "))
operacion= input("ingrese que tipo de operacion realizara (+,*,/,-)" )
resultado= calculadora (num1, num2, operacion)
print ("resultado: ", resultado)



    