class Quemado(Exception):
    def __str__(self):
        return '¡Cuidado!¡Te quemaste!'

class Mate:
    def __init__(self, n):
        self.cebadas = n
        self.lleno = False

    def cebar(self):
        if self.lleno:
            raise Quemado
        else:
            self.lleno = True

    def beber(self):
        if self.cebadas <= 0:
            print('El mate está lavado.')
            self.lleno = False
        else:
            self.cebadas = self.cebadas - 1
            self.lleno = False

capacidadMate = int(input('Ingrese la capacidad de cebadas de su mate. '))

mate = Mate(capacidadMate)

print('Cebadas Restantes: ', mate.cebadas,'Estado del mate: ', mate.lleno)

accion = ''
print('''       Opción 1 para cebar.'
      'Opción 2 para beber.'
      'Opcion 3 para salir.''')
while accion != '3':
    accion = input('→    ')

    if int(accion) == 1:
        try:
            mate.cebar()
        except Quemado:
            print('¡Cuidado!¡Te quemaste!')
        print('Cebadas Restantes: ', mate.cebadas,'Estado del mate: ', mate.lleno)

    elif int(accion) == 2:
        mate.beber()
        print('Cebadas Restantes: ', mate.cebadas,'Estado del mate: ', mate.lleno)
