#Liga betplay
#N cantidad de equipos
#cada equipo contiene un cuerpo técnico, jugadores, 
#estadística y en donde esa estadística esta marcada por los partidos que han ganado, 
# los que han perdido, los que han empatado, los goles a favor y los goles en contra. También tienen un total de puntos.
#El primer objetivo es permitir el registro de los equipos del torneo
#hacer el registro del plantel
#programar partidos con fechas
#Registrar resultados de fecha
#Los jugadores tienen un #dorsal, pos.juego, un nombre y programar quien juega con quien, 
# debe existir un equipo logar y un equipo visitante.
#cada partido perdido es 0 puntos. empatados 1 punto y ganados 3 puntos

jugadores=[
    {
        "nombre": "Messi", 
        "numero": 10, 
        "posicion": "delantero"
    },
    {
        "nombre": "Ronaldo",
        "numero": 15, 
        "posicion": "delantero"
    }

]

def getplayers():
    for i in jugadores:
        jugador= i
        for a,e in jugador.items():
            print(f'{a}:{e}')
        print('****************')
        
#getPlayers()
def insertPlayer():
    nombre = input(f'ingrese nombre del jugador: ')
    numero = input(f'numero del jugador: ')
    posicion = input(f'posicion del jugador: ')

    newPlayer = {
        "nombre":nombre,
        "numero":numero,
        "posicion":posicion
    }

    jugadores.append(newPlayer)
    getplayers()

#insertPlayer()
