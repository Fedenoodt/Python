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
