import os 
import modules.ui as ui
import modules.mensajes as msg
if (__name__ == "__main__"):
    ligaBetPlay=[]
    isActive= True
    opMenu= 0
    while (isActive): 
        try: 
            os.system('cls')
            print(msg.tituloMenuPrincipal)
            print (ui.menu)
            opMenu = int(input('.....'))
            match opMenu:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case _:
                    print('La opción ingresada no esta permitida en el menú')
                    os.system('pause')
            isActive = False
        except ValueError:
            print ('La opción ingresada es invalida')
            os.system('pause')
            continue
pass
       