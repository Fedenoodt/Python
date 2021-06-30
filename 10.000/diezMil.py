#====================================================CONSTANTES========================================================#

#-------Bibliotecas Importadas-------------------------

import random

#-------Constantes-------------------------------------

nombre = ''

jugadores = []

habilitado = []

puntajeJugador = []

gano = False

#===================================================DEFINICIONES=======================================================#

#-------Definiciones de Juego--------------------------

def cubilete(cantidadDados, dado):
    tirada = []
    for i in range(0, cantidadDados):
        azar = random.randint(1, dado)
        tirada.append(azar)
    return tirada

def evaluador(tirada):
    cantidadCaras = []
    for i in range(1, 7):
        conteo = tirada.count(i)
        cantidadCaras.append(conteo)
    return cantidadCaras

def puntuador(cadaCara, primerTiro, dados):
    puntos = 0
    noTirar = 0
    if primerTiro:
        if cadaCara[0] == 3:
            puntos = puntos + 1000
            noTirar = 3
        else:
            puntos = puntos + cadaCara[0] * 100
            noTirar = cadaCara[0]
        si = True
        for i in range(0, len(cadaCara)-1):
            if cadaCara[i] !=1:
                si=False
        if si:
            puntos = puntos + 1500 - 150
            noTirar = 4
    else:
        puntos = puntos + cadaCara[0] * 100
        noTirar = cadaCara[0]
    for i in (1, 2, 3, 5):
        if cadaCara[i] == 3:
            puntos = puntos + (i + 1) * 100
            noTirar = noTirar + cadaCara[i]
    puntos = puntos + cadaCara[4] * 50
    noTirar = noTirar + cadaCara[4]
    if noTirar == dados:
        dadosvuelta = 5
    else:
        dadosvuelta = dados - noTirar
    return puntos, dadosvuelta

def mostrarResultadosRepetidos(cadaCara):
    cara = 0
    for x in range(0, len(cadaCara)):
        cara = cara + 1
        print(cara, "=", int(cadaCara[x]))

#==============================================CUERPO DEL PROGRAMA=====================================================#

#-------Introducción a los Jugadores-------------------

while nombre != '*':
    print('Ingrese nombres de los jugadores ("*" para salir)  ')
    nombre = input(' ►   ')
    if nombre != '*':
        jugadores.append(nombre)
        habilitado.append(False)
        puntajeJugador.append(0)

#-------Cuerpo del Juego-------------------------------

while not gano:
    i = 0
    while i < len(jugadores) and not gano:
        print('Tira', jugadores[i])
        input()
        dados = 5
        puntajeJugada = -1
        primerTiro = True
        puntajeGenerico = 0
        llegoHabilitado = False
        recienHabilitado = False
        while puntajeJugada != 0 and not llegoHabilitado:
            tiro = cubilete(dados, 6)
            print('')
            print('         CU')
            print('              BI')
            print('    ', tiro)
            print('         LE')
            print('              TE')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            print('Caras obtenidas:')
            cadaCara = evaluador(tiro)
            mostrarResultadosRepetidos(cadaCara)
            puntajeJugada, dados = puntuador(cadaCara, primerTiro,dados)
            puntajeGenerico = puntajeGenerico + puntajeJugada
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            print('Dados a tirar:', dados, '.')
            print('Puntaje de ronda:', puntajeJugada, '.')
            print('Puntaje total:', puntajeGenerico, '.')
            input()
            primerTiro = False
            if habilitado[i] == False and puntajeGenerico >= 450:
                habilitado[i] = True
                llegoHabilitado = True
                recienHabilitado = True
                print('Ahora esta habilitado.')
            #Salto de prolijidad
            for j in range(0, 2):
                print()
        if habilitado [i] and not recienHabilitado:
            if puntajeJugador[i] + puntajeGenerico > 10000:
                print('Excedió el puntaje de 10.000, conserva el anterior,', puntajeJugador[i], '.')
            elif puntajeJugador[i] + puntajeGenerico < 10000:
                puntajeJugador[i] = puntajeJugador[i] + puntajeGenerico
                print('Usted tiene:', puntajeJugador[i],'puntos.')
            else:
                print('¡ Tenemos un ganador ! ¡', jugadores[i], '!')
                gano = True
        i = i + 1

