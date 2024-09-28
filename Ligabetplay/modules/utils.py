def ValiData(mensajes:str):
    global isAllow 
    flagFunction = True 
    opciones = ('N','n','S', 's')
    accion= input(f'{mensajes}')
    if (accion not in opciones):
        print ("La opcion que usted ingreso es invalida...")
        ValiData()
    elif(accion=='N'):
        flagFunction = True
    elif (bool(accion) == 'S'):
        flagFunction = False
    return flagFunction
def ValidateResponse(mensajes:str):
    global isAllow 
    flagFunction = True 
    opciones = ('N','n','S', 's')
    accion= input(f'{mensajes}')
    if (accion not in opciones):
        print ("La opcion que usted ingreso es invalida...")
        ValiData()
    elif(accion=='N'):
        flagFunction = True
    elif (bool(accion) == 'S'):
        flagFunction = False
    return flagFunction

