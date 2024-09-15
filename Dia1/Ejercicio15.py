#Solicita al usuario su salario bruto y su país de residencia. Calcula el salario neto aplicando
#impuestos: el 20% para residentes de "País A", el 15% para "País B" y el 10% para "País C". Si el
#país no está en la lista, aplica un 25% de impuestos.

def sal (salario, residencia):
     match str (residencia):
        case 'A': 
            return salario* (1-0.20)
        case 'B':
            return salario* (1-0.15) 
        case 'C':
            return salario* (1-0.10)
        case _:
            return salario* (1-0.25)
        
salario= float(input("Ingrese su salario bruto: "))
residencia= input("Ingrese su lugar de residencia (A, B, C, u otro): ")
resultado= sal (salario, residencia)
print ("su salario neto es: ", resultado)

