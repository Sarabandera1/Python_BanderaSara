#Crea un programa que pida al usuario ingresar el nombre de un país y luego
#determine en qué continente se encuentra.Utiliza estructuras condicionales para
#asociar cada país con su respectivo continente y muestra un mensaje con el
#continente correspondiente.

def determinar_continente(pais):
   
    america = ['canada', 'mexico', 'argentina', 'brasil', 'chile', 'colombia']
    europa = ['españa', 'francia', 'alemania', 'italia', 'portugal', 'reinounido']
    asia = ['china', 'japon', 'india', 'corea', 'tailandia', 'rusia']
    africa = ['nigeria', 'sudafrica', 'kenia', 'egipto', 'marruecos', 'etiopia']
    oceania = ['australia', 'nuevazelanda', 'fiyi', 'papuanuevaguinea', 'samoa']

    
    pais = pais.lower()

    
    if pais in america:
        return "América"
    elif pais in europa:
        return "Europa"
    elif pais in asia:
        return "Asia"
    elif pais in africa:
        return "África"
    elif pais in oceania:
        return "Oceanía"
    else:
        return "País no reconocido"


pais = input("Ingresa el nombre de un país: ")
continente = determinar_continente(pais)
print(f"El país {pais.title()} se encuentra en {continente}.")