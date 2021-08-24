import math
import random

        #///////////////A\\\\\\\\\\\\\\\#

#=# 1 #=# #~~~~~~~~~~~~~//Operaciones Básicas\\~~~~~~~~~~~~~#

def sumar(x, y):
    suma = x + y
    return suma

def restar(x, y):
    restar = x - y
    return restar

def multiplicar(x, y):
    multiplicar = x * y
    return multiplicar

def dividir(x, y):
    dividir = x / y
    return dividir

def divisionEntera(x, y):
    divisionEntera = x // y
    return divisionEntera

def divisionResto(x, y):
    divisionResto = x % y
    return divisionResto

def potenciacion(x, y):
    potenciacion = x ** y
    return potenciacion

def raiz(x, y):
    raiz = pow(x, (1 / y))
    'raiz = round(pow(x, (1 / y)))'
    return raiz

        #=# 2 #=# #~~~~~~~~~~~~~//Calculadora\\~~~~~~~~~~~~~#

    import math as matematica

def calculadora():
    def sumar(a, b):
        c = a + b
        return c

    def restar(a, b):
        c = a - b
        return c

    def multiplicar(a, b):
        c = a * b
        return c

    def dividir(a, b):
        c = a / b
        return c

    def exponenciacion(a, b):
        c = a ** b
        return c

    def raiz(a, b):
        c = float(a) ** (1 / float(b))
        return c

    operaciones = [sumar, restar, multiplicar, dividir, exponenciacion, raiz]


    for i in range(0, 10):
        print('')
    print('Bienvenid@ a la calculadora. Las opciones que disponemos son:')

    accion = ''

    while accion != '*':
        print('1_____________________________Sumar')
        print('2_____________________________Restar')
        print('3_____________________________Multiplicar')
        print('4_____________________________Dividir')
        print('5_____________________________Exponenciación')
        print('6_____________________________Raíz de...')
        print(' _____________________________(todas las elevaciones con el segundo número) ')
        print('*_____________________________Salir')
        for i in range(0,4):
            print('')
        accion = ''
        while accion != '1' and accion != '2' and accion != '3' and accion != '4' and accion != '5' and accion != '6' and accion != '*':
            print('')
            accion = input('Ingrese el numero de lo que desea hacer. =>    ')
            if accion != '1' and accion != '2' and accion != '3' and accion != '4' and accion != '5' and accion != '6' and accion != '*':
                print('Ingresó una opción erronea.')
                print('')
                print('1_____________________________Sumar')
                print('2_____________________________Restar')
                print('3_____________________________Multiplicar')
                print('4_____________________________Dividir')
                print('5_____________________________Exponenciación')
                print('6_____________________________Raíz de...')
                print(' _____________________________(todas las elevaciones con el segundo número) ')
                print('*_____________________________Salir')
        if accion != '*':
            primera = int(input('Ingrese primer número.     => '))
            segunda = int(input('Ingrese segundo número.     => '))
            print('resultado =', operaciones[int(accion) - 1](primera, segunda))
            input('Presione cualquier tecla para continuar.')


    for i in range(0, 30):
        print('')
    print('Espero haberlo ayudado. Hasta luego.')


        #///////////////B\\\\\\\\\\\\\\\#

        #=# 1 #=# #~~~~~~~~~~~~~//10.000\\~~~~~~~~~~~~~#

def diezMil():

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

        #=# 2 #=# #~~~~~~~~~~~~~//Ahorcado\\~~~~~~~~~~~~~#
            
def ahorcado():

    def bienvenida():
        print("                                             _________________________")
        print("                                           /|_______________________  |")
        print("                                           ||                      |  |")
        print("                                           ||                      |  |Bienvenido")
        print("                                         _///_                     |  |")
        print("                                        / | | \                    |  |")
        print("                                       |   7   |                   |  |al")
        print("                                        \_---_/                    |  |")
        print("                                          |=|                      |  |")
        print("                                       __/|_|\__                   |  |Ahorcado")
        print("                                      /   ___   \                  |  |")
        print("                                     | | /■ ■\ | |                 |  |")
        print("                                     |_| \|||/ |_|                 |  |")
        print("                                     |||_______|||                 |  |")
        print("                                        |  ||  |                   |  |")
        print("                                        /  ||  \                   |  |")
        print("                                        |  ||  |                   |  |")
        print("                                        |  ||  |                   |  |")
        print("                                        |__||__|                   |__|")
        print("                                        |==||==|                  /    \ ")
        print("                                        \__/\__/                 /      \ ")
        print("                            ================================================")

    def entrada():
        print("                                             _________________________")
        print("                                           /|_______________________  |")
        print("                                           ||                      |  |")
        print("                                           ||                      |  |")
        print("                                           \|                      |  |")
        print("                                            /                      |  |")
        print("                                           /                       |  |")
        print("                                           \                       |  |")
        print("                                           /\                      |  |")
        print("                                           \/                      |  |")
        print("                                                                   |  |")
        print("                                                                   |  |")
        print("                                                                   |  |")
        print("                                                                   |  |")
        print("                                                                   |  |")
        print("                                                                   |  |")
        print("                                                                   |  |")
        print("                                                                   |  |")
        print("                                                                   |__|")
        print("                                                                  /    \ ")
        print("                                                                 /      \ ")
        print("                            ================================================")

    def unaPerdida():
        print("                                             _________________________")
        print("                                           /|_______________________  |")
        print("                                           ||                      |  |")
        print("                                           ||                      |  |")
        print("                                         _///_                     |  |")
        print("                                        / | | \                    |  |")
        print("                                       |   7   |                   |  |")
        print("                                        \_---_/                    |  |")
        print("                                                                   |  |")
        print("                                                                   |  |")
        print("                                                                   |  |")
        print("                                                                   |  |")
        print("                                                                   |  |")
        print("                                                                   |  |")
        print("                                                                   |  |")
        print("                                                                   |  |")
        print("                                                                   |  |")
        print("                                                                   |  |")
        print("                                                                   |__|")
        print("                                                                  /    \ ")
        print("                                                                 /      \ ")
        print("                            ================================================")

    def dosPerdidas():
        print("                                             _________________________")
        print("                                           /|_______________________  |")
        print("                                           ||                      |  |")
        print("                                           ||                      |  |")
        print("                                         _///_                     |  |")
        print("                                        / | | \                    |  |")
        print("                                       |   7   |                   |  |")
        print("                                        \_---_/                    |  |")
        print("                                          |=|                      |  |")
        print("                                       __/|_|\__                   |  |")
        print("                                     /_|  ___  |_\                 |  |")
        print("                                       | /■ ■\ |                   |  |")
        print("                                       | \|||/ |                   |  |")
        print("                                       |_______|                   |  |")
        print("                                      /_/\_____\                   |  |")
        print("                                                                   |  |")
        print("                                                                   |  |")
        print("                                                                   |  |")
        print("                                                                   |__|")
        print("                                                                  /    \ ")
        print("                                                                 /      \ ")
        print("                            ================================================")

    def tresPerdidas():
        print("                                             _________________________")
        print("                                           /|_______________________  |")
        print("                                           ||                      |  |")
        print("                                           ||                      |  |")
        print("                                         _///_                     |  |")
        print("                                        / | | \                    |  |")
        print("                                       |   7   |                   |  |")
        print("                                        \_---_/                    |  |")
        print("                                          |=|                      |  |")
        print("                                       __/|_|\__                   |  |")
        print("                                      /   ___  |_\                 |  |")
        print("                                     | | /■ ■\ |                   |  |")
        print("                                     |_| \|||/ |                   |  |")
        print("                                     |||_______|                   |  |")
        print("                                       /________\                  |  |")
        print("                                                                   |  |")
        print("                                                                   |  |")
        print("                                                                   |  |")
        print("                                                                   |__|")
        print("                                                                  /    \ ")
        print("                                                                 /      \ ")
        print("                            ================================================")

    def cuatroPerdidas():
        print("                                             _________________________")
        print("                                           /|_______________________  |")
        print("                                           ||                      |  |")
        print("                                           ||                      |  |")
        print("                                         _///_                     |  |")
        print("                                        / | | \                    |  |")
        print("                                       |   7   |                   |  |")
        print("                                        \_---_/                    |  |")
        print("                                          |=|                      |  |")
        print("                                       __/|_|\__                   |  |")
        print("                                      /   ___   \                  |  |")
        print("                                     | | /■ ■\ | |                 |  |")
        print("                                     |_| \|||/ |_|                 |  |")
        print("                                     |||_______|||                 |  |")
        print("                                       /________\                  |  |")
        print("                                                                   |  |")
        print("                                                                   |  |")
        print("                                                                   |  |")
        print("                                                                   |__|")
        print("                                                                  /    \ ")
        print("                                                                 /      \ ")
        print("                            ================================================")

    def cincoPerdidas():
        print("                                             _________________________")
        print("                                           /|_______________________  |")
        print("                                           ||                      |  |")
        print("                                           ||                      |  |")
        print("                                         _///_                     |  |")
        print("                                        / | | \                    |  |")
        print("                                       |   7   |                   |  |")
        print("                                        \_---_/                    |  |")
        print("                                          |=|                      |  |")
        print("                                       __/|_|\__                   |  |")
        print("                                      /   ___   \                  |  |")
        print("                                     | | /■ ■\ | |                 |  |")
        print("                                     |_| \|||/ |_|                 |  |")
        print("                                     |||_______|||                 |  |")
        print("                                        |  ||_/                    |  |")
        print("                                        /  |                       |  |")
        print("                                        |  |                       |  |")
        print("                                        |  |                       |  |")
        print("                                        |__|                       |__|")
        print("                                        |==|                      /    \ ")
        print("                                        \__/                     /      \ ")
        print("                            ================================================")

    def muerte():
        print("                                             _________________________")
        print("                                           /|_______________________  |       |\    /| ")
        print("                                           ||                      |  |       | \  / | ")
        print("                                           ||                      |  |       |  \/  | ")
        print("                                         _///_                     |  |            ")
        print("                                        / X X \                    |  |       |      | ")
        print("                                       |   7   |                   |  |       |      | ")
        print("                                        \_vvv_/                    |  |        \____/  ")
        print("                                          |=|                      |  |           ")
        print("                                       __/|_|\__                   |  |        _______  ")
        print("                                      /   ___   \                  |  |       |_____    ")
        print("                                     | | /■ ■\ | |                 |  |       |_______  ")
        print("                                     |_| \|||/ |_|                 |  |         ____   ")
        print("                                     |||_______|||                 |  |        |    |  ")
        print("                                        |  ||  |                   |  |        |---\  ")
        print("                                        /  ||  \                   |  |        |     \  ")
        print("                                        |  ||  |                   |  |         _____    ")
        print("                                        |  ||  |                   |  |           |    ")
        print("                                        |__||__|                   |__|           |     ")
        print("                                        |==||==|                  /    \         _____")
        print("                                        \__/\__/                 /      \       /     \ ")
        print("                            ======                     =====================    \_____/")
        print("                                  \                   /")
        print("                                   \                 /")
        print("                                    \               /")

    def gano():
        print("                                             _________________________")
        print("                                           /|_______________________  |        ____")
        print("                                           ||                      |  |       /   ")
        print("                                           ||                      |  |      |    ---|")
        print("                  _///_                    \|                      |  |       \_____/ ")
        print("                 / ^ ^ \                    /                      |  |")
        print("                |   7   |                  /                       |  |         /\ ")
        print("                 \_\_/_/                   \                       |  |        /--\ ")
        print("                   | |                     /\                      |  |       /    \ ")
        print("                __/|_|\__                  \/                      |  |")
        print("               /   ○ ○   \                                         |  |        |\  |")
        print("              | |   7   | |                                        |  |        | \ |")
        print("              |_| \___/ |_|                                        |  |        |  \| ")
        print("              |||_______|||                                        |  |        ")
        print("                 |  ||  |                                          |  |        _____   | ")
        print("                 /  ||  \                                          |  |       /     \  | ")
        print("                 |  ||  |                                          |  |       \_____/  . ")
        print("                 |  ||  |                                          |  |")
        print("                 |__||__|                                          |__|")
        print("                 |==||==|                                         /    \ ")
        print("                 \__/\__/                                        /      \ ")
        print("              ====================                     =====================")
        print("                                  \                   /")
        print("                                   \                 /")
        print("                                    \               /")

    #====================================================CONSTANTES========================================================#

    import random

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
    bienvenida()
    palabraSorpresa = guiones(palabra, seleccion)
    nombreJugador = nombre()
    nombreJugador = nombre()
    while not exito and vidasPerdidas < 6 and seleccion != '*':
        listaLetras = []
        dibujos[vidasPerdidas]()
        muestraPalabraSorpresa(palabraSorpresa)
        print('')
        print(tema)
        valorIngresado = input('Ingrese la letra o palabra a adivinar ►► ►  ')

        palabraSorpresa, exito, adivino = validador(valorIngresado, palabra, palabraSorpresa)

        if not adivino:
            vidasPerdidas = vidasPerdidas + 1

    if exito:
        gano()
        muestraPalabraSorpresa(palabraSorpresa)
        print('')
        print(palabra)
        print('')
        print('¡', nombreJugador, 'felicidades ! Has ganado este ahorcado.')
        preguntar()
    else:
        muerte()
        print('')
        print('Lo siento', nombreJugador, '. Has muerto.')
        preguntar()
        
        #=# 3 #=# #~~~~~~~~~~~~~//Juego de Rol\\~~~~~~~~~~~~~#

def juegoRol():
    class Muerto(Exception):
        def __str__(self):
            'Has muerto.'

    class Personaje:
        def __init__(self, vida, posicion, velocidad):
            self.vida = vida
            self.posicion = posicion
            self.velocidad = velocidad

        def recibir_ataque(self, daño):
            self.vida -= daño
            if self.vida <= 0:
                raise Muerto
        def __str__(self):
            return 'Vida:' + str(self.vida) + ', Posición: ' + str(self.posicion) + ', Velocidad: ' + str(self.velocidad)


    class Soldado(Personaje):
        def __init__(self, vida, posicion, velocidad, ataque):
            self.ataque = ataque
            super().__init__(vida, posicion, velocidad)

        def atacar(self):
            return self.ataque

    class Campesino(Personaje):
        def __init__(self, vida, posicion, velocidad, cosecha):
            self.cosecha = cosecha
            super().__init__(vida, posicion, velocidad)

        def cosechar(self):
            return self.cosecha


    Soldado_Ryan = Soldado(12, 1, 6, 5)
    Soldado_Thomas = Soldado(30, 2, 12, 2)

    print(Soldado_Ryan)
    print(Soldado_Thomas)

    for i in range(0,100):

        try:
            Soldado_Ryan.recibir_ataque(Soldado_Thomas.ataque)
        except Muerto:
            print('El soldado Ryan ha muerto.')
            exit()

        try:
            Soldado_Thomas.recibir_ataque(Soldado_Ryan.ataque)
        except Muerto:
            print('El soldado Thomas ha muerto.')
            exit()

        print(Soldado_Ryan)
        print(Soldado_Thomas)

        #=#  #=# #~~~~~~~~~~~~~//Sifón\\~~~~~~~~~~~~~#
        
def sifon():
    class Lleno (Exception):
        def __str__(self):
            return 'Su vaso esta lleno.'

    class Vacio (Exception):
        def __str__(self):
            return 'Su vaso esta vacío.'

    class Sifon:
        def __init__(self, capacidad, velocidadKmH):
            self.capacidadLitros = capacidad
            self.velocidadDrenaje = velocidadKmH

    class Vaso:
        def __init__(self, capacidadMl):
            self.estadoVaso = 0
            self.capacidadMilimitros = capacidadMl
            self.lleno = False

        def llenar(self):
            if self.lleno:
                print('¡Cuidado!')
                raise Lleno
            else:
                self.lleno = True
                self.estadoVaso += self.capacidadMilimitros

        def beber(self):
            if self.estadoVaso >= 0:
                self.estadoVaso -= 20
            else:
                raise Vacio





    Sifon(1,1)
    Vaso(80)



    print('Elija "1" para llenar el vaso.')
    print('Elija "2" para beber.')
    print('Elija "3" para dejar de beber soda y alejarse de la mesa.')

    def veredicto():
        eleccion = int(input('  >'))
        return eleccion


    eleccion = veredicto()

    while eleccion != 3:
        if eleccion != 3:
            if eleccion == 1:
                try:
                    Vaso.llenar()
                except Lleno:
                    print('Su vaso esta lleno.')
            elif eleccion == 2:
                try:
                    Vaso.beber()
                except Vacio:
                    print('Su vaso esta vacío.')

            elif eleccion == 3:
                print('Decides no tomar soda, y te alejas de la mesa.')
                exit()
            else:
                print('Ingreso la opción incorrecta, intente de nuevo.')
                veredicto()
                
                
def sorteadorGalactico():
    import random

    #======================================================================================================================#



    def eleccion(items):
        eleccion = random.choices(items)
        return eleccion

    #======================================================================================================================#

    print(
        "  _____________________    _           _____             _              _      _       ____       ________          ")
    print(
        " /               |        / \         |     \             \            /      / \     |    \     /                  ")
    print(
        " \_____          |       /___\        |_____/              \    /\    /      /___\    |____/     \______            ")
    print(
        "        \        |      /     \       |   \                 \  /  \  /      /     \   |   \             \           ")
    print(
        "  ______/        |     /       \      |    \______           \/    \/      /       \  |    \____________/           ")
    print("                                        -Intergalactic Software 3.3-")
    print("                                           'Sorteador Galactico'")

    print("¿Como te llamas, extraño?   ")
    print(" ")
    nombre = input("")
    print(" ")
    print("Bienvenido", nombre + "...")
    print(" ")
    print("¿Una nueva adquisición para tus estanterías", nombre + "? Ja! ¿De que se trata esta vez?")


    print(" ")





    repetir = 'si'

    personajes = ''
    naves = ''
    Articulos_Especiales = ''
    caminos = ''


    while repetir == 'si' or repetir == 'Si' or repetir == 'SI' or repetir == 'S' or repetir == 's':
        contador = 0
        cosas = []
        cosasTemporaria = []
        print("♦ Personajes~Naves~Articulos Especiales ♦")
        print(" ")
        caminos = input("►  ")

        if caminos == "personajes" or caminos == "Personajes" or caminos == "PERSONAJES":
            print("Cuenteme todos los personajes a sortear, y digame '*' cuando haya terminado.    ")
            personajes = input("")
            contador = contador + 1
            print(contador)
        elif caminos == "Naves" or caminos == "naves" or caminos == "NAVES":
            print("Cuenteme todas las naves a sortear, y digame '*' cuando haya terminado.    ")
            naves = input("")
            contador = contador + 1
            print(contador)
        elif caminos == "Articulos Especiales" or caminos == "articulos especiales" or caminos == "Artículos Especiales" or caminos == "artículos especiales" or caminos == "ARTICULOS ESPECIALES" or caminos == "ARTÍCULOS ESPECIALES":
            print("Cuenteme todos los Artículos Especiales a sortear, y digame '*' cuando haya terminado.    ")
            Articulos_Especiales = input("")
            contador = contador + 1
            print(contador)

        while caminos != "personajes" and caminos != "Personajes" and caminos != "PERSONAJES" and caminos !=  "Naves" and caminos != "naves" and caminos != "NAVES" and caminos != "Articulos Especiales" and caminos != "articulos especiales" and caminos != "Artículos Especiales" != "artículos especiales" and caminos != "ARTICULOS ESPECIALES" and caminos != "ARTÍCULOS ESPECIALES":
            print("¿Como? ¿Vas a ingresar contenido? Por favor, selecciona algúna de las opciones.  ")
            caminos = input("►  ")
            if caminos == "personajes" or caminos == "Personajes" or caminos == "PERSONAJES":
                print("Cuenteme todos los personajes a sortear, y digame '*' cuando haya terminado.    ")
                personajes = input("")
                contador = contador + 1
                print(contador)
            elif caminos == "Naves" or caminos == "naves" or caminos == "NAVES":
                print("Cuenteme todas las naves a sortear, y digame '*' cuando haya terminado.    ")
                naves = input("")
                contador = contador + 1
                print(contador)
            elif caminos == "Articulos Especiales" or caminos == "articulos especiales" or caminos == "Artículos Especiales" or caminos == "artículos especiales" or caminos == "ARTICULOS ESPECIALES" or caminos == "ARTÍCULOS ESPECIALES":
                print("Cuenteme todos los Artículos Especiales a sortear, y digame '*' cuando haya terminado.    ")
                Articulos_Especiales = input("")
                contador = contador + 1
                print(contador)

        while (caminos != "*"):
            caminos = input(" ")
            contador = contador + 1
            print(contador)
            cosas.append(caminos)

        cosas.remove('*')
        n = int(input("Bueno, ahora digame cuantos quieres que sean los ganadores.  "))
        cosasTemporaria = cosas

        for i in range(n):
            cantGanadores = eleccion(cosasTemporaria)
            cosasTemporaria.remove(cantGanadores[0])
            print("Ganador/es:", cantGanadores[0])
        volvio = input('¿Desea hacer otro sorteo? (Si/No)')
        repetir = volvio

    print("Eso ha sido todo,", nombre + ", espero haya quedado satisfech@ con los ganadores, y que la fuerza le acompañe...")
    
        #=# 6 #=# #~~~~~~~~~~~~~//Randomizador de Coordenadas\\~~~~~~~~~~~~~#
    
def randomCoordenadas():
    import random
    def enter():
        print('')
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=


    def banner():
        print('~~~  ~~ ~   ~ ~~  ~~~ ~~~  ~~ ~   ~ ~~  ~~~ ~~~  ~~ ~   ~ ~~  ~~~ ~~~  ~~ ~   ~ ~~  ~~~ ~~~  ~~ ~   ~ ~~  ~~~ ')
        print('~~~  ~~ ~   ~ ~~  ~~~ ~~~  ~~ ~   ~ ~~  ~~~ ~~~  ~~ ~   ~ ~~  ~~~ ~~~  ~~ ~   ~ ~~  ~~~ ~~~  ~~ ~   ~ ~~  ~~~ ')
        print('~~~  ~~ ~   ~ ~~  ~~~ ~~~  ~~ ~   ~ ~~  ~~~ XXXX-XXXX-XXXX ~~~  ~~ ~   ~ ~~  ~~~ ~~~  ~~ ~   ~ ~~  ~~~ ~~~  ')
        print('~~~  ~~ ~   ~ ~~  ~~~ ~~~  ~~ ~   ~ ~~ RANDOMIZADOR DE COORDENADAS ~~~  ~~ ~   ~ ~~  ~~~ ~~~  ~~ ~   ~ ~~  ~~~')
        print('                                      Intergalactic Software 1.3')
        enter()

    def bienvenida():
        print('Bienvenido usuario del eje de coordenadas, este es un dispositivo para generar una coordenada aldeatoria de')
        print('un eje de coordenadas que usted necesite, espero le sea de utilidad.')
        enter()



    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
    banner()
    bienvenida()

    x1 = int(input('Ingrese el valor menor del intervalo de X: '))
    x2 = int(input('Ingrese el valor mayor del intervalo de X: '))

    y1 = int(input('Ingrese el valor menor del intervalo de Y: '))
    y2 = int(input('Ingrese el valor mayor del intervalo de Y: '))

    z1 = int(input('Ingrese el valor menor del intervalo de Z: '))
    z2 = int(input('Ingrese el valor mayor del intervalo de Z: '))


    x3 = random.randrange(x1, x2)
    y3 = random.randrange(y1, y2)
    z3 = random.randrange(z1, z2)

    enter()
    print('La coordenada que usted obtuvo es', 'X:', x3, ';', 'Y:', y3, ';', 'Z:', z3)
    enter()
    print('Gracias por haber usado el Randomizador de Coordenadas.')
    print('Que la fuerza lo acompañe. ☺')
    
        #=# 7 #=# #~~~~~~~~~~~~~//Dado\\~~~~~~~~~~~~~#

def dado():
    import random
    continuidad = ''
    while continuidad != '*':
        dado = []
        for i in range(0, 6):
            dado.append(random.randint(1, 6))
        print(' ----- \n|', dado[0], dado[1], '|\n|',
        dado[2], dado[3],
        '|\n|', dado[4], dado[5], '|\n ----- ')
        print('\n\n Siga presionando Enter para seguir dando tiradas.',
        '\nPresione "*" antes de Enter para salir.')
        continuidad = input(' ')
        if continuidad == '*':
            print('\nQue tenga un buen día...')
    
        #///////////////C\\\\\\\\\\\\\\\#
    
        #=# 1 #=# #~~~~~~~~~~~~~//Calculador de triángulo rectángulo\\~~~~~~~~~~~~~#
    
def trianguloRectangulo():
    print('(Se pueden ingresar en decimales.)')
    ladoMenor = float(input('Ingrese el lado menor del triángulo:\n '))
    ladoMayor = float(input('Ingrese el lado mayor del triángulo:\n '))
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    superficie = ladoMayor * ladoMenor
    perimetro = ladoMayor * 2 + ladoMenor * 2
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    superficie = round(superficie, 2)
    perimetro = round(perimetro, 2)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    print('La superficie del triángulo rectángulo, es',
    superficie, 'y el perímetro es', perimetro, end='.')
    
        #=# 2 #=# #~~~~~~~~~~~~~//Calculador de área y volumen esferico\\~~~~~~~~~~~~~#    
    
def areavolumenEsfera():
    import math
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    print('(Se puede ingresar en decimales.)')
    radio = float(input('Ingrese el radio de la esfera:\n '))
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    area = 4 * math.pi * radio ** 2
    volumen = (4 * math.pi * radio ** 3) / 3
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    area = round(area, 2)
    volumen = round(volumen, 2)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    print('El área de la esfera es', area, ', y su volumen',
    volumen, end='.')
    
        #///////////////D\\\\\\\\\\\\\\\#
    
        #=# 1 #=# #~~~~~~~~~~~~~//Lector de dias de un mes\\~~~~~~~~~~~~~#

def diasMes():
    #~~~~~~~~~~~~~//definiciones\\~~~~~~~~~~~~~#
    def fallo():
        print('Ingresó mal alguno de los datos. Vuelva a ingresar.')
    meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo',
    'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre',
    'Noviembre', 'Diciembre')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    diasMes = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31,
    6 : 30, 7 : 31, 8 : 31, 9 : 30,
    10 : 31, 11 : 30, 12 : 31}
    bisiesto = {2 : 29}
    #=////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////=#
    #~~~~~~~~~~~~~//funciones\\~~~~~~~~~~~~~#
    def anioBisiesto(anio):
        if anio % 4 == 0 and anio % 100 != 0:
            diasMes.update(bisiesto)
    #=////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////=#
    try:
        mes = int(input('Ingrese el mes en número:\n '))
        anio = int(input('Ingrese el año:\n '))
        anioBisiesto(anio)
        print('El mes de', meses[mes - 1], 'del año', anio,
        ', tiene en total', diasMes[mes], 'días.')
    except:
        fallo()
    
        #=# 2 #=# #~~~~~~~~~~~~~//Conversor de temperaturas\\~~~~~~~~~~~~~#
    
def cfkCelsiusFahrenheitKelvin():
    ingreso_datos = False
    continuar = True
    fallo = 'Ingresó mal alguno de los datos, vuelva a intentarlo.'
    repite = 'Estado_Inicial'

        #---------------------------------#

    def Valor(ingreso_datos):
        if type(valor) == float:
            Tipo(ingreso_datos)
        
    def Tipo(ingreso_datos):
        if tipo == 1 or tipo == 2 or tipo == 3:
            Convertir(ingreso_datos)

    def Convertir(ingreso_datos):
        if convertir == 1 or convertir == 2 or convertir == 3:
            Decimales(ingreso_datos)

    def Decimales(ingreso_datos):
        if type(decimales) == int:
            ingreso_datos = True
        else:
            print(fallo)
        return ingreso_datos


        #-------------Prints--------------#

    f = 'Fahrenheit'
    c = 'Celsius'
    k = 'Kelvin'

    r = 'El resultado de la conversión'
    x = '.\nAdemás le informo, que dicha medida de'
    g = 'grados'

    #########################################################################

    def celsiusFahrenheit(valor, tipo, convertir):
        if tipo == 1 and convertir == 2:
            valor = (valor - 32) / 1.8
            valor = round(valor, decimales)
            print(r, c, 'a', f, ', es:', valor, g, f, x, c, 'en', k, ', sería:', celsiusKelvin(valor, tipo, convertir), g, k, '.')
            return valor
            
    def celsiusKelvin(valor, tipo, convertir):
        if tipo == 1 and convertir == 3:
            valor = valor - 273.15
            valor = round(valor, decimales)
            print(r, c, 'a', k, ', es:', valor, g, k, x, c, 'en', f, ', sería:', celsiusFahrenheit(valor, tipo, convertir), g, f, '.')
            return valor
        
        #---------------------------------#
        
    def fahrenheitCelsius(valor, tipo, convertir):
        if tipo == 2 and convertir == 1:
            valor = valor * 1.8 + 32
            valor = round(valor, decimales)
            print(r, f, 'a', c, ', es:', valor, g, c, x, f, 'en', k, ', sería:', fahrenheitKelvin(valor, tipo, convertir), g, k , '.')
            return valor
            
    def fahrenheitKelvin(valor, tipo, convertir):
        if tipo == 2 and convertir == 3:
            valor = (valor - 273.15) * 1.8 + 32
            valor = round(valor, decimales)
            print(r, f, 'a', k, ', es:', valor, g, k, x, f, 'en,', c, ', sería:', fahrenheitCelsius(valor, tipo, convertir), g, c, '.')
            return valor
        
        #---------------------------------#
        
    def kelvinCelsius(valor, tipo, convertir):
        if tipo == 3 and convertir == 1:
            valor = valor + 273.15
            valor = round(valor, decimales)
            print(r, k, 'a', c, ', es:', valor,  g, c, x, k , 'en', f, ', sería:', kelvinFahrenheit(valor, tipo, convertir), g, f, '.')
            return valor
        
    def kelvinFahrenheit(valor, tipo, convertir):
        if tipo == 3 and convertir == 2:
            valor = (valor - 32) / 1.8 + 273.15
            valor = round(valor, decimales)
            print(r, k, 'a', f, ', es:', valor, g, f, x, k, 'en', c, ', sería:', kelvinCelsius(valor, tipo, convertir), g, f, '.')
            return valor
        
        #---------------------------------#
        
    def esLoMismo(valor, tipo, convertir):
        if tipo == convertir:
            print('El valor de grados, es el mismo que el del ingreso.')

    #########################################################################

    while continuar:    
        while ingreso_datos == False:
            valor = float(input('Ingrese el valor de grados a convertir:\n '))
            tipo = int(input('Ingrese, en número, que tipo de grado es:\n1- Celsius\n2- Fahrenheit\n3- Kelvin\n\n- '))
            convertir = int(input('Ingrese, en número, a que tipo lo desea convertir:\n1- Celsius\n2- Fahrenheit\n3- Kelvin\n\n- '))
            decimales = int(input('\nÚltima pregunta, y no por eso menos importante. ¿Cantidad de decimales que desea ver?\n '))
            Valor(ingreso_datos)
            ingreso_datos = Convertir(ingreso_datos)
        
    #########################################################################

        funciones = [celsiusFahrenheit(valor, tipo, convertir), celsiusKelvin(valor, tipo, convertir),
                     fahrenheitCelsius(valor, tipo, convertir), fahrenheitKelvin(valor, tipo, convertir),
                     kelvinCelsius(valor, tipo, convertir), kelvinFahrenheit(valor, tipo, convertir),
                     esLoMismo(valor, tipo, convertir)]
        ingreso_datos = False
        repite = input('\n\n¿Desea continuar? S/N:   ').upper()
        if repite == 'S':
            print('\n\n\n Reiniciando... \n\n\n')
        elif repite == 'N':
            continuar = False
            print('Adiós. Que le vaya bien...')
        else:
            print(fallo)
            continuar = False
            print('(Reiniciar programa para ingresar.)')
            
        #///////////////E\\\\\\\\\\\\\\\#
            
        #=# 1 #=# #~~~~~~~~~~~~~//Ingresos automáticos\\~~~~~~~~~~~~~#
            
def ingresosAutomaticos():
    print('/// CUIDADO: INGRESOS AUTOMÁTICOS ACTIVADOS. ///')

        
 
#=////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////=#

def indice():
    print('''
    Indice:
    A: Matemática
        1- Operaciones Básicas:
            sumar(x, y)
            restar(x, y)
            multiplicar(x, y)
            dividir(x, y)
            divisionEntera(x, y)
            divisionResto(x, y)
            potenciacion(x, y)
            raiz(x, y)
        2- Calculadora()

        

    B: Juegos
        1- 10.000 (diezMil())
        2- Ahorcado()
        3- juegoRol()
        4- sifon()
        5- Sorteador Galáctico 3.3 (sorteadorGalactico())
        6- Randomizador de Coordenadas (randomCoordenadas())
        7- dado()
        
    C: Geometría
        1- Calculador de triángulo rectángulo (trianguloRectangulo())
        2- Calculador de área y volumen esferico (areavolumenEsfera())
        
    D: Utilidades
        1- Lector de dias de un mes(diasMes())
        2- Conversor de temperaturas (cfkCelsiusFahrenheitKelvin())
        
    E: Mensajes
        1- ingresosAutomaticos()

    ''')

#=////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////=#
 
def maximalMain():
    indice()
 
#=////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////=#

