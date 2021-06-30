

class Eliminado(Exception):
    def __str__(self):
        'Nave perdida.'

class Nave:
    def __init__(self, nombre, modelo, tipo, coraza, escudo):
        self.nombre = nombre
        self.modelo = modelo
        self.tipo = tipo
        self.coraza = coraza
        self.escudo = escudo

        self.vidaTotal = coraza + escudo

    def recibir_daño(self, daño):
        disyuntor = 1
        self.escudo -= daño
        if self.escudo <= 0:
            if disyuntor == 1:
                self.coraza = self.escudo + self.coraza
                disyuntor = 2
            elif disyuntor == 2:
                self.coraza -= daño
                validador = 2
                disyuntor = validador
                if self.coraza <= 0:
                    raise Eliminado

    def impresion(self):
        print('Coraza: ', self.coraza)
        print('Escudo: ', self.escudo)

class NaveCombate(Nave):
    def __init__(self, nombre, modelo, tipo, coraza, escudo, ataque):
        self.ataque = ataque
        super().__init__(nombre, modelo, tipo, coraza, escudo)

    def atacar(self):
        return self.ataque

naveA1 = NaveCombate('Efiell', 'Nebulon-B', 'Fragata', 67, 74, 58)
naveA2 = NaveCombate('Conformidad', 'Corelliano', 'Corveta', 45, 48, 26)
naveA3 = NaveCombate('Asillon', 'Corelliano', 'Corveta', 45, 48, 26)

Flota_Rebelde = [naveA1, naveA2, naveA3]

naveB1 = NaveCombate('Seguro', 'Destructor Estelar', 'Nave de linea', 115, 95, 82)
naveB2 = NaveCombate('Devastador', 'Destructor Estelar', 'Nave de linea', 115, 95, 82)

Flota_Imperial = [naveB1, naveB2]

Nave.impresion(self=naveA1)

print('^ Primeros dos valores originales ^')

for i in range(0, 3):
    try:
        naveA1.recibir_daño(naveB2.ataque)

    except Eliminado:
        'a'

    Nave.impresion(self=naveA1)