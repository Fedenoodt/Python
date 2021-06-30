#====================================================CONSTANTES========================================================#

#-----------Constantes de Juego------------------------

posiciones = [1, 2, 3, 4, 5, 6, 7, 8, 9]

turnos = 0

graficoCirculo = '○'
graficoCuadrado = '■'

#-----------Constantes de Validación-------------------

tateti = False

#===================================================DEFINICIONES=======================================================#

#-----------Definiciones de Bienvenida-----------------

def jugador1():
    print('El jugador 1 usará ○...')
    print('    ¿Como te llamas?')
    jugador1 = input('  ')
    return jugador1

def jugador2():
    print('Y el jugador 2 usará ■...')
    print('    ¿Cuál es su nombre?')
    jugador2 = input('  ')
    return jugador2

def bienvenida():
    print(" ______________________________")
    print("|          |         |         |                Bienvenido al...")
    print("|    ○     |    ○    |    ■    |                            TA")
    print("|__________|_________|_________|                                TE")
    print("|          |         |         |                                    TI")
    print("|    ■     |    ■    |    ○    |")
    print("|__________|_________|_________|")
    print("|          |         |         |")
    print("|    ○     |    ■    |    ■    |")
    print("|__________|_________|_________|                    Comenzemos...")
    print('')


#-----------Definiciones del Juego---------------------

def tabla():
    print("                                          ▼                ☼")
    print("                           ▼                            ☼")
    print("          ♦                     ▼                    ☼  ")
    print("              ♦  ________________________________  ☼")
    print("                |          |          |          |  ")
    print("                |    ", posiciones[0], "   |    ",posiciones[1] , "   |    ",posiciones[2] , "   |        ◄")
    print("       ►       |__________|__________|__________|    ◄")
    print("        ►      |          |          |          |  ")
    print("                |    ", posiciones[3], "   |    ", posiciones[4], "   |    ", posiciones[5], "   |  ")
    print("     ►         |__________|__________|__________|  ")
    print("       ►       |          |          |          | ◄")
    print("           ►   |    ", posiciones[6], "   |    ", posiciones[7], "   |    ", posiciones[8], "   |   ◄")
    print("         ►     |__________|__________|__________|        ◄")
    print("             ☼   ▲                               ♦")
    print("          ☼                     ▲                   ♦")
    print("       ☼             ▲                                 ♦              ")
    print("                         ▲                                ♦          ")
    print("                      ▲                                      ")

def agregarCirculo():
    circulo = int(input('Ingrese posición ○...     '))
    posiciones.remove(circulo)
    posiciones.insert(circulo-1, graficoCirculo)
    return circulo

def agregarCuadrado():
    cuadrado = int(input('ingrese posición ■...     '))
    posiciones.remove(cuadrado)
    posiciones.insert(cuadrado-1, graficoCuadrado)
    return cuadrado

#-----------Definiciones Validadoras-------------------

def validador(posiciones):
    gano = False
    ficha=''
    if posiciones[0] == posiciones[1] and posiciones[1] == posiciones[2]:
        gano = True
        ficha=posiciones[0]
    if posiciones[3] == posiciones[4] and posiciones[4] == posiciones[5]:
        gano = True
        ficha = posiciones[3]
    if posiciones[6] == posiciones[7] and posiciones[7] == posiciones[8]:
        gano = True
        ficha = posiciones[6]
    if posiciones[0] == posiciones[3] and posiciones[3] == posiciones[6]:
        gano = True
        ficha = posiciones[7]
    if posiciones[1] == posiciones[4] and posiciones[4] == posiciones[7]:
        gano = True
        ficha = posiciones[1]
    if posiciones[2] == posiciones[5] and posiciones[5] == posiciones[8]:
        gano = True
        ficha = posiciones[2]
    if posiciones[0] == posiciones[4] and posiciones[4] == posiciones[8]:
        gano = True
        ficha = posiciones[0]
    if posiciones[2] == posiciones[4] and posiciones[4] == posiciones[6]:
        gano = True
        ficha = posiciones[2]
    lista=[gano,ficha]
    return lista


#==============================================CUERPO DEL PROGRAMA=====================================================#


#-----------Bienvenida al juego------------------------

bienvenida()
jug1 = jugador1()
jug2 = jugador2()



#-----------Juego--------------------------------------
relacion = {graficoCirculo : jug1, graficoCuadrado : jug2}

tabla()


while not tateti and turnos < 9:
    jugador1 = agregarCirculo()
    tabla()
    turnos = turnos + 1
    print('turno: ', turnos)

    jugador2 = agregarCuadrado()
    tabla()
    turnos = turnos + 1
    print('turno: ', turnos)
    informacion = validador(posiciones)
    tateti=informacion[0]
    if tateti:
        print ('¡ Victoria !    ¡ Gano', relacion.get(informacion[1]), '!')

