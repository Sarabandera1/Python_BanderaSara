import os
listaOpciones:list
opciones:list
def crearmenu(listaOpciones,opciones):
    listaOpciones=['A' ,'B', 'F' ]
    opciones = ['A. Equipo goleador', 'B. Equipo más puntos' , 'F. Salir menú principal']
    os.system('cls')

    opcion = input("""


    ▗▖  ▗▗▄▄▄▗▖  ▗▗▖ ▗▖    ▗▄▄▖▗▄▄▄▗▄▄▖ ▗▄▖▗▄▄▗▄▄▄▗▄▄▄▖▗▄▄▖
    ▐▛▚▞▜▐▌  ▐▛▚▖▐▐▌ ▐▌    ▐▌ ▐▐▌  ▐▌ ▐▐▌ ▐▐▌ ▐▌█ ▐▌  ▐▌
    ▐▌  ▐▐▛▀▀▐▌ ▝▜▐▌ ▐▌    ▐▛▀▚▐▛▀▀▐▛▀▘▐▌ ▐▐▛▀▚▖█ ▐▛▀▀▘▝▀▚▖
    ▐▌  ▐▐▙▄▄▐▌  ▐▝▚▄▞▘    ▐▌ ▐▐▙▄▄▐▌  ▝▚▄▞▐▌ ▐▌█ ▐▙▄▄▗▄▄▞
    """)

    for item in opciones:
        print(item)
    try:
        op = input (':')
    except:
        print('error')
        os.system ('pause')
    else:
        print(op)