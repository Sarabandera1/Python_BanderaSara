import os
def addPlantel(lstLiga:list):
    isFound= False
    equipo =input('Ingrese el nombre del equipo a buscar: ')
    if (len(lstLiga) > 0):
        for team in lstLiga:
            if(equipo in team):
               addPerson(team)
            break
    if(isFound == False): 
        print('El equipo no se encuentra participanto...')
        os.system ('pause')
    else:
        os.system('clear')
        print ('No hay equipos registrados, agregue un equipo primero a la lista')
        os.system('pause')

def addPerson(lstPersons:list):
    isAddPersons = True
    while (isAddPersons):
        nombre = input('Digite el nombre de la persona: ')
        cargo = input('Escriba el cargo de la persona')
        person = [nombre,cargo]
        lstPersons[1].append(persons)