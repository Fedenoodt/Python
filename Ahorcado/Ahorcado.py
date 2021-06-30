#====================================================CONSTANTES========================================================#

import random
import dibujo

#-------Temas del Ahorcado-----------------------------

artes = ['Da Vinci', 'Mona Lisa', 'Beethoven', 'George Lucas', 'John Williams', 'Picasso', 'El Grito', 'Hombre de Vitruvio', 'Miguel Angel', 'Michael Giacchino']
ciencia = ['Pitágoras', 'Einstein', 'Edisson', 'Favaloro', 'Steve Jobs', 'Amstrong', 'Darwin', 'atomo', 'oxigeno', 'nasa']
deportes = ['Messi', 'Maradona', 'gol', 'tanto', 'yarda', 'tacle', 'Caño', 'fifa', 'afa', 'tennis']
entretenimiento = ['Star Wars', 'lectura', 'deportes', 'videojuegos', 'programar', 'cine IMAX', 'viajes', 'series', 'peliculas', 'coleccionismo']
geografia = ['Cumulus Nimbus', 'meandro', 'savana', 'oceano', 'pradera', 'bosque', 'selva', 'desierto', 'montañas', 'valle']
historia = ['Egipto', 'Grecia', 'revolución francesa', 'revolución industrial', 'Julio', 'revolución de Mayo', 'Jueves Negro', 'Mayo', 'Sarmiento', 'Cabildo']

temas = {'Artes' : artes, 'Ciencia' : ciencia, 'Deportes' : deportes, 'Entretenimiento' : entretenimiento, 'Geografia' : geografia, 'Historia' : historia}

#===================================================DEFINICIONES=======================================================#

#-------Definiciones de Introducción-------------------

def introduccion():
    print()
    print(
        'Esta es una modalidad de Ahorcado diferente, usted puede disponer del modo de juego "Temático"(se muestra la')
    print(
        'tematica del juego, sin mostrar ninguna letra), o "Extremos"(No se muestra la Temática, pero sin la primera y')
    print('última letra de la palabra).')
    print('')
    print('¿Cuál prefiere?')
    print('')
    print('♦ 1: Temático')
    print('♦ 2: Extremos')
    print('♦ *: Salir del Juego')
    print('')
    eleccion = ''
    while eleccion != '1' and eleccion != '2' and eleccion != '*':
        eleccion = input('►  ')
    return eleccion

def nombre():
    print('Por cierto... ¿Cómo se llama?')
    nombre = input('►        ►     ')
    return nombre

#-------Definiciones de Juego--------------------------

def guiones(palabra, seleccion):
    secreto = []
    if seleccion == '1':
        for i in range(0, len(palabra)):
            secreto.append('__')
    elif seleccion == '2':
        secreto.append(palabra[0])
        for j in range(1, len(palabra)-1):
            secreto.append('__')
        secreto.append(palabra [-1])
    return secreto

def validador(ingreso, palabraEscondida, guiones):
    exito = False
    adivino = False
    if len(ingreso) == 1:
        for i in range(0, len(palabraEscondida)):
            if ingreso == palabraEscondida[i]:
                guiones[i] = ingreso
                adivino = True
        if '__' not in guiones:
            exito = True
    elif ingreso == palabraEscondida:
            exito = True
    return guiones, exito, adivino

def muestraPalabraSorpresa(palabraSorpresa):
    for i in palabraSorpresa:
        print(i, end=' ')
    print('\n ')

def preguntar():
    respuesta = input('¿Desea seguír jugando?')
    print('')
    print('"1" para SI')
    print('"2" para NO')
    return respuesta

def analisis(respuesta):
    if respuesta == '1':
        respuesta = True
    elif respuesta == '2':
        respuesta = False
    else:
        print('¿Como? No entendí el carácter ingresado...')
        preguntar()
    return respuesta

#==============================================CUERPO DEL PROGRAMA=====================================================#
#-------Random de Ahorcado-----------------------------


ahorcado = random.choice(list(temas.items()))
tema=ahorcado[0]
palabra=random.choice(ahorcado[1])

#-------Cuerpo en si-----------------------------------

vidasPerdidas = 0
exito = False
adivino = False

seleccion = introduccion()
dibujo.bienvenida()
palabraSorpresa = guiones(palabra, seleccion)
nombreJugador = nombre()
nombreJugador = nombre()
while not exito and vidasPerdidas < 6 and seleccion != '*':
    listaLetras = []
    dibujo.dibujos[vidasPerdidas]()
    muestraPalabraSorpresa(palabraSorpresa)
    print('')
    print(tema)
    valorIngresado = input('Ingrese la letra o palabra a adivinar ►► ►  ')

    palabraSorpresa, exito, adivino = validador(valorIngresado, palabra, palabraSorpresa)

    if not adivino:
        vidasPerdidas = vidasPerdidas + 1

if exito:
    dibujo.gano()
    muestraPalabraSorpresa(palabraSorpresa)
    print('')
    print(palabra)
    print('')
    print('¡', nombreJugador, 'felicidades ! Has ganado este ahorcado.')
    preguntar()
else:
    dibujo.muerte()
    print('')
    print('Lo siento', nombreJugador, '. Has muerto.')
    preguntar()