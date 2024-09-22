from Jugadores import getplayers, insertPlayer

def menuJugadores():
    opcion = input("""
                                menu de jugadores

                       1. obtener todos los jugadres.
                       2. agregar un jugador.
opcion:  """)
    
    try:
        opcion = int(opcion)
        
        if opcion == 1:
            getplayers()
            menuJugadores()
        elif opcion == 2:
            insertPlayer()
            menuJugadores()
        else: 
            print("Opción no válida")
            menuJugadores()
    
    except ValueError:
        print("Por favor, ingrese un número válido.")
        menuJugadores()
menuJugadores()