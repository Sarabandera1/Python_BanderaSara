from Jugadores import getPlayers
etecnico =[

]

def cuerpoTecnico():
    for i in tecnico:
        tecnico = i
        for a,e in tecnico.items():
            print(f'{a}:{e}')
        print('***********************')

getPlayers()
def insertPlayer():
    nombre = input(f'ingrese nombre del tecnico: ')
    print('***********************')

    newTecnico = {
        "nombre":nombre
    }

    etecnico.append(newTecnico)
    cuerpoTecnico()
insertPlayer()
