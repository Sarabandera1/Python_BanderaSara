def ValiData(mensajes:str):
    global isAllow 
    flagFunction = True 
    opciones = ('N','n','S', 's')
    accion= input(f'{mensajes}')
    if (accion not in opciones):
        print ("La opcion que usted ingreso es invalida...")
        ValiData()
    elif(accion=='N'):
        flagFunction = False
    elif (bool(accion) == 'S'):
        flagFunction = True
    return flagFunction
             