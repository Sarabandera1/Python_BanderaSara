import modules.utils as uc
import os
nombreTeam = input('Ingrese el nombre del equipo participante\n')
def addTea(lstLiga):
    golesAfavor = int(input('Ingrese los goles: '))
    tarjetasAm = int(input('Ingrese el numero de tarjetas amarrillas: '))
    tarjetasRo = int(input('Ingrese el numero de tarjetas rojas: '))
    totaldeFaltasC = int(input('Ingrese el total de falta cometidas: '))
    isAddTeam =True
    while (isAddTeam):
        os.system('cls')
        nombreTeam = input('Ingrese el nombre del equipo participante\n')
        
        diccionario={
            "nombre":nombreTeam,
            "golesAfavor":golesAfavor,
            "tarjetasAm": tarjetasAm,
            "tarjetasRo": tarjetasRo,
            "totaldeFaltasC": totaldeFaltasC
        }
        lstLiga.append (diccionario)
        isAddTeam = uc.ValidateResponse('Desea agregar otro equipo al torneo s(si) N(no)')


