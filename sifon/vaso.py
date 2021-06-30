class Lleno(Exception):
    def __str__(self):
        return 'El vaso está lleno.'

class Vaso:
    def __init__(self, n):
        self.capacidad = n
        self.lleno = False

    def llenar(self):
        if self.lleno:
            raise Lleno
        else:
            self.lleno = True

    def beber(self):
        if self.capacidad <= 0:
            print('El vaso esta vacío.')
            self.lleno = False
        else:
            self.capacidad = self.capacidad - 1
            self.lleno = False

capacidadVaso = int(input('Ingrese la capacidad de su vaso. '))

vaso = Vaso(capacidadVaso)

print('Tragos Restantes: ', vaso.capacidad, 'Estado del vaso: ', vaso.lleno)

accion = ''
print('''       Opción 1 para llenar.'
      'Opción 2 para beber.'
      'Opcion 3 para salir.''')
while accion != '3':
    accion = input('→    ')

    if int(accion) == 1:
        try:
            vaso.llenar()
        except Lleno:
            print('El vaso está lleno.')
        print('Tragos Restantes: ', vaso.capacidad, 'Estado del vaso: ', vaso.lleno)

    elif int(accion) == 2:
        vaso.beber()
        print('Tragos Restantes: ', vaso.capacidad, 'Estado del vaso: ', vaso.lleno)

    else:
        print('Ingresó una opción incorrecta. Intentelo de nuevo.')
        accion2 = input('→    ')
        accion = accion2