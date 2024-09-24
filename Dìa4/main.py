from Jugadores import getPlayers, insertPlayer
from partido import getPartidos, insertMatch
from etecnico import cuerpoTecnico,insertPlayer
from menureportes import crearmenu as mkMenu


def menuPrincipal():
    while True:
        try:
            opcion=input ("""
      LIGA BETPLAY
                                                                                      
    Opciones disponibles:
    1. menu jugadores.
    2. menu partidos.
    3. menu cuerpo tecnico.
                                                           

seleccione una opcion: """)
            if (opcion=='1'):
                menuJugadores()
            elif (opcion =='2'):
                menuPartidos()
            elif (opcion == '3'):
                menuTecnico()
            elif (opcion == '4'):
                isreport= True
                while isreport:
                    opr = mr.crearmenu
                menureportes()
            else:
                return opcion
        except:
            pass
        

def menuJugadores():
    
    opcion = input("""
    MENU JUGADORES

    1. obtener todos los jugadores.
    2. insertar un nprint("opcion no valida ")uevo jugador.
Ingrese una opcion: """)
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
        print('Vuelva a intentarlo')
        menuJugadores()


def menuPartidos():
    opcion = input("""
                                                                          
    Menu Partidos
                   
    1. Obtener partidos.
    2. Insertar Partido
                   

Ingrese una opcion: """)
    
    try: 
        opcion = int(opcion)

    except ValueError:
        print('Ingrese opcion valida')
        
def menuTecnico():
    
    opcion = input("""
    CUERPO TECNICO                                                                                                                                                     

    1. obtener todo el cuerpo tecnico.
    2. insertar nuevo tecnico.

Ingrese una opcion: """)
    try:
        opcion=int(opcion)
        if opcion == 1:
            cuerpoTecnico()
        elif opcion == 2:
            insertPlayer()
    except ValueError:
        print('Opcion no valida')
        menuTecnico()

menuPrincipal()








