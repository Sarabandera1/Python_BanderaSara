
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
        os.system('clear')
        nombreTeam = input('Ingrese el nombre del equipo participante\n')
        
        diccionario={
            jugador={
            "nombre":nombreTeam,
            "golesAfavor":golesAfavor,
            "tarjetasAm": tarjetasAm,
            "tarjetasRo": tarjetasRo,
            "totaldeFaltasC": totaldeFaltasC
            }
        }
        lstLiga.append (diccionario)
        for key, value in jugador.items():
            print(f'{key}: {value}')
        print(f'Jugador {nombreTeam} agregado correctamente')
        respuesta = input('Desea agregar otro equipo al torneo? s(si) N(no)\n').lower()
        if respuesta != 's':
            isAddTeam = False
        return
    
        isAddTeam = uc.ValidateResponse('Desea agregar otro equipo al torneo s(si) N(no)')


