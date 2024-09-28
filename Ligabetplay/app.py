import os 
import modules.ui as ui
import modules.mensajes as msg
import modules.utils as uc
import modules.teams as tm
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
                    isAddTeam = True
                    opMenuTeam = 0
                    while (isAddTeam):
                        try:
                            os.system('cls')
                            print(ui.menuEquipos)
                            opMenuTeam = int(input(''))
                        except ValueError:
                            print ('Error en el dato ingresado...')
                            os.system('pause')
                            continue
                        else: 
                            match opMenuTeam:
                                case 1:
                                    tm.addTeam(ligaBetPlay)
                                    print(ligaBetPlay)
                                    os.system('pause')
                                case 4:
                                    isAddTeam = uc.validateData(msg.msgExitOpcion)
                                case _:
                                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    isVActive = uc.validateData(msg.msgInfoAddTeam)
                case _:
                    print('La opción ingresada no esta permitida en el menú')
                    os.system('pause')
        except ValueError:
            print ('La opción ingresada es invalida')
            os.system('pause')
            continue
pass