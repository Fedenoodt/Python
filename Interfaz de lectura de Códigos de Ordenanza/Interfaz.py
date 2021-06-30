#======================================================CONEXIÓN========================================================#

import sqlite3
baseCodigos = sqlite3.connect('C:\\Users\Eduardo\Desktop\Republica\Black Hawk Security Informatics Anonymous Incorporation\Protocolo 4\Base_de_datos_de_Codigos_de_ordenanza.db')

cursor = baseCodigos.cursor()

print("Base de datos creada y conectada con éxito a SQLite.-")

for i in range(0, 5):
    print( )

#=====================================================VARIABLES========================================================#

orden = 0

C0 = 'SELECT * FROM _C0_INTRODUCCION'
C1 = 'SELECT * FROM _C1_CODIGOS_DE_RELACIONES_HUMANITARIAS_Y_PERSONALES'
CE1 = 'SELECT * FROM _CE1_CODIGOS_DE_RELACIONES_HUMANITARIAS_Y_PERSONALES'
C2 = 'SELECT * FROM _C2_CODIGOS_RELACIONALES_A_SISTEMAS_INFORMATICOS'
CE2 = 'SELECT * FROM _CE2_CODIGOS_RELACIONALES_A_SISTEMAS_INFORMATICOS'
P2 = 'SELECT * FROM _P2_CODIGOS_RELACIONALES_A_SISTEMAS_INFORMATICOS'
C3 = 'SELECT * FROM _C3_CODIGOS_DE_OPERACIONES_MOVILES_Y_TRANSPORTES'
CE3 = 'SELECT * FROM _CE3_CODIGOS_DE_OPERACIONES_MOVILES_Y_TRANSPORTES'
C4 = 'SELECT * FROM _C4_OBJETOS_DE_VALOR_CLASIFICADOS'
C5 = 'SELECT * FROM _C5_CODIGOS_DE_ORDEN_ESTRUCTURAL'
P5 = 'SELECT * FROM _P5_CODIGOS_DE_ORDEN_ESTRUCTURAL'

directivas = [C0, C1, CE1, C2, CE2, P2, C3, CE3, C4, C5, P5]

#====================================================DEFINICIONES======================================================#

def cartel():
    print('                   /\                                                ')
    print('                  /  \                                               Black Hawk Security Informatics')
    print('                 /    \                                                  Anonymous Incorporation')
    print('________________/      \________________                             ')
    print('\                                      /                             ')
    print(' \                                    /                                  Interfaz de lectura de')
    print('  \                                  /                                    Codigos de Ordenanza')
    print('   \                                /                                ')
    print('   /                                \                                ')
    print('  /                                  \                               ')
    print(' /                                    \                                Intergalactic Software 1.0')
    print('/_______________        _______________\                               ---------------------------')
    print('                \      /                                             ')
    print('                 \    /                                              ')
    print('                  \  /                                               ')
    print('                   \/                                                ')

def bienvenida():
    print('Bienvenido a la interfaz de lectura de los Codigos de Ordenanza.')
    print('Aqui estan registrados todos los codigos del protocolo del Organismo de la Liga de la Memoria.')
    print(' ')
    print('Indique que desea consultar...')
    print(' ')
    grilla()

def grilla():
    print('  1| Códigos de relaciones humanitarias y personales.')
    print('  2| Codigos de emergencia de relaciones humanitarias y personales.')
    print('  3| Codigos relacionales a sistemas informaticos.')
    print('  4| Codigos de emergencia relacionales a sistemas informaticos.')
    print('  5| Protocolos relacionales a sistemas informaticos.')
    print('  6| Codigos de operaciones moviles y transportes.')
    print('  7| Codigos de emergencia de operaciones moviles y transportes.')
    print('  8| Objetos de valor clasificados.')
    print('  9| Codigos de orden estructural.')
    print(' 10| Plataformas del orden estructural.')
    print('  *| Salir')






#=======================================================CUERPO=========================================================#

cartel()
bienvenida()

orden = input('►    ')

while orden != '*':
    orden = int(orden)
    cursor.execute(directivas[orden])
    codigos = cursor.fetchall()

    for i in codigos:
        print(i)
    print('¿Desea consultar algo más?')
    orden = input('►    ')

print('<Proteger y servir. Espero haber ayudado, hasta luego.>')