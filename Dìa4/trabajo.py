from Jugadores import getPlayers, insertPlayer
from partido  import getPartidos, insertMatch


def menuJugadores():

    opcion = input("""
                   
 ▗▖  ▗▖▗▄▄▄▖▗▖  ▗▖▗▖ ▗▖    ▗▄▄▖ ▗▄▄▖ ▗▄▄▄▖▗▖  ▗▖ ▗▄▄▖▗▄▄▄▖▗▄▄▖  ▗▄▖ ▗▖
▐▛▚▞▜▌▐▌   ▐▛▚▖▐▌▐▌ ▐▌    ▐▌ ▐▌▐▌ ▐▌  █  ▐▛▚▖▐▌▐▌     █  ▐▌ ▐▌▐▌ ▐▌▐▌
▐▌  ▐▌▐▛▀▀▘▐▌ ▝▜▌▐▌ ▐▌    ▐▛▀▘ ▐▛▀▚▖  █  ▐▌ ▝▜▌▐▌     █  ▐▛▀▘ ▐▛▀▜▌▐▌
▐▌  ▐▌▐▙▄▄▖▐▌  ▐▌▝▚▄▞▘    ▐▌   ▐▌ ▐▌▗▄█▄▖▐▌  ▐▌▝▚▄▄▖▗▄█▄▖▐▌   ▐▌ ▐▌▐▙▄▄▖

                   
Ingrese una opcion:
    
    1.obtener todos los jugadores.
    2.insertar un nuevo jugador.
""")
    try:
        opcion=int(opcion)
        if opcion == 1:
            getPlayers()
        elif opcion == 2:
            insertPlayer()
        elif opcion==3:
            menuPartidos()
        else:
            print('opción no valida')
            menuJugadores()
    except ValueError:
        print('Error')
        menuJugadores()



def menuPartidos():
    opcion = input("""
        Menu Partidos

Ingrese una opcion: 
    
Obtener partidos.
Insertar Partido
""")

    try: 
        opcion = int(opcion)

    except ValueError:
        print('Ingrese opcion valida')


def menu():
    opcion = input("""
 Menu LigBetPlay
    
Menu Juadores
Menu partidos.
""")
    try:
        opcion = int(opcion)

        if opcion == 1 :
            menuJugadores()
        if opcion == 2:
            pass
            # menuPartidos()
        else:
            print(' opcion invalida')
            menu()

    except ValueError:
        print('ingresar solo numeros')
        menu()


menuJugadores()
