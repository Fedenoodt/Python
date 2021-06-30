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