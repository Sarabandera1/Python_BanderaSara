import os
def crearmenu(): 
    lstopciones = ['A' ,'B', 'F' ]
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
    op= input (':')
except:
    print: ('Error en la opción')
    os.system ('pause')
else:
    return op