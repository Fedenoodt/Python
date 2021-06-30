import sqlite3
llamadaaBiblioteca = sqlite3.connect('C:/Users/Eduardo/Acceso Directo a Juegos/PS2/juegosPS2.db')

cursor = llamadaaBiblioteca.cursor()

########################################################################################################################

def cartel():
    print('                          _______________    _______________    _______________              ')
    print('                         |               |  |                                  |')
    print('                         |               |  |                                  | ')
    print('                         |_______________|  |_______________    _______________|')
    print('                         |                                  |  |               ')
    print('                         |                                  |  |              ')
    print('                         |                   _______________|  |_______________              ')
    print('------------------------------------------Sony PlayStation 2®------------------------------------------')
    print('                                      Intergalactic Software 1.0')
    print('                              "Biblioteca de Juegos de PS2 de Fedenoodt"')


########################################################################################################################


def juego():
    cursor.execute('SELECT JUEGO.NOMBRE FROM JUEGO')

    juego = cursor.fetchall()

    for i in juego:
        print(i)

def desarrollador1():
    cursor.execute('SELECT DESARROLLADOR.NOMBRE FROM DESARROLLADOR')

    desarrollador = cursor.fetchall()

    for i in desarrollador:
        print(i)

def todo():
    print('Inventario de Todos los juegos de Fedenoodt:')
    print('--------------------------------------------')

    cursor.execute('SELECT JUEGO.NOMBRE,DESARROLLADOR.NOMBRE FROM JUEGO,DESARROLLADOR WHERE juego.ID_DESARROLLADOR=DESARROLLADOR.ID_DESARROLLADOR or JUEGO.ID_DESARROLLADOR_2=DESARROLLADOR.ID_DESARROLLADOR or JUEGO.ID_DESARROLLADOR_3=DESARROLLADOR.ID_DESARROLLADOR')

    todo = cursor.fetchall()

    for i in todo:
        print(i)

def dudas():
    dudas = input('¿Algúna duda de alguna entrega en especifico?')
    print('Si es así, ingrese el ID (numero previo al nombre) del juego.')

########################################################################################################################

cartel()

todo()