import os
def addPlantel(lstLiga:list):
    isFound= False
    equipo =input('Ingrese el nombre del equipo a buscar: ')
    if (len(lstLiga) > 0):
        for team in lstLiga:
            if(equipo in team):
                print(team)
                os.system('pause')
                isFound = True
    if(isFound==False): 
        print('El equipo no se encuentra participanto...')
        os.system ('pause')
    else:
        os.system('cls')
        print ('No hay equipos registrados, agregue un equipo primero a la lista')
        os.system('pause')