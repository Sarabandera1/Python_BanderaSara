#Crea un programa que solicite al usuario ingresar una contraseña y
#verifique si cumple con los siguientes
#requisitos: debe tener al menos 8
#caracteres y contener al menos un
#número. Si la contraseña cumple con
#los requisitos, muestra el
#mensaje"Contraseña válida". De lo
#contrario, muestra el mensaje
#"Contraseña inválida".

def es_contrasena_valida(contrasena):
    
    if len(contrasena) < 8:
        return False
    
 
    tiene_numero = any(char.isdigit() for char in contrasena)
    
    return tiene_numero


contrasena = input("Ingresa una contraseña: ")


if es_contrasena_valida(contrasena):
    print("Contraseña válida")
else:
    print("Contraseña inválida")
