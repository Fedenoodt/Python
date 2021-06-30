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