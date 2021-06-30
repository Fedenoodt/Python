class Muerto(Exception):
    print('Has Muerto')

class Personaje():
    def __init__(self):
        self.nombre = ''
        self.vida = 100
        self.posicion = 0
        self.velocidad = 25
    def recibir_ataque(self, daño):
        self.vida -= daño
        if self.vida <= 0:
            raise Muerto
    def mover(self):
        self.posicion += self.velocidad

class Soldado(Personaje):
    def __init__(self, nombre, vida, posicion, velocidad, ataque):
        self.ataque = ataque
        super().__init__(nombre, vida, posicion, velocidad)

    def atacar(self):
        return self.ataque

class Campesino(Personaje):
    def __init__(self, nombre, vida, posicion, velocidad, cosecha):
        self.cosecha = cosecha
        super().__init__(nombre, vida, posicion, velocidad)

    def cosechar(self):
        return self.cosecha

#A continuación se ingresan los atributos de dos soldados de distinto bando, y un campesino.

#Atributos del primer soldado...

nombre_soldado1 = input('Ingrese nombre del primer soldado.')
vida_soldado1 = float(input('Ingrese la vida del primer soldado.'))
posicion_soldado1 = 1
velocidad_soldado1 = float(input('Ingrese la velocidad del primer soldado.'))
ataque_soldado1 = float(input('Ingrese la potencia de ataque del primer soldado.'))

soldado1 = Soldado(nombre_soldado1, vida_soldado1, posicion_soldado1, velocidad_soldado1, ataque_soldado1)

#Atributos del segundo soldado...

nombre_soldado2 = input('Ingrese nombre del segundo soldado.')
vida_soldado2 = float(input('Ingrese la vida del segundo soldado.'))
posicion_soldado2 = 2
velocidad_soldado2 = float(input('Ingrese la velocidad del segundo soldado.'))
ataque_soldado2 = float(input('Ingrese la potencia de ataque del segundo soldado.'))

soldado2 = Soldado(nombre_soldado1, vida_soldado1, posicion_soldado1, velocidad_soldado1, ataque_soldado1)

#Atributos del campesino...

nombre_campesino = input('Ingrese nombre del campesino.')
vida_campesino = float(input('Ingrese la vida del campesino.'))
posicion_campesino = 0
velocidad_campesino = 5
cosecha_campesino = float(input('Ingrese la capacidad de cosecha del campesino.'))

campesino = Campesino(nombre_campesino, vida_campesino, posicion_campesino, velocidad_campesino, cosecha_campesino)

