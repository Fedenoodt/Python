piedras = True
meChoqueconUna = 0
reactivacion = False

while piedras:
    while meChoqueconUna <=20:
        otraPiedra = 1
        meChoqueconUna = meChoqueconUna + otraPiedra
        input()
        print('Fede volvió a codear')
    vuelta = input('¿Querés reactivarte? (s/n)'.lower())

    while vuelta != 's' and vuelta != 'n':
        print('Ingresó una respuesta incorrecta, escriba solo "s" o "n"')
        vuelta = input('¿Querés reactivarte? (s/n)'.lower())
    if vuelta:
        piedras = False

if piedras == False:
    reactivacion = True

if reactivacion:
    nombre = input('¿Como te llamás?')
    edad = input('¿Cuantos años tenés?')
    estatura = input('¿Cuánto medís? (más o menos)')
    peso = input('¿Cuánto pesas? (más o menos)')
    largoPelo = input('¿Cuán largo tenes el pelo? (Escribir solo largo/mediano/corto)').lower()
    colorPelo = input('¿De que color tenés el pelo?')
    while largoPelo != 'largo' and largoPelo != 'mediano' and largoPelo != 'corto':
        print('Ingresó mal el largo de su pelo, vuelva a ingresar.')
        largoPelo = input('¿Cuán largo tenes el pelo? (Escribir solo largo/mediano/corto)').lower()
    colorOjos = input('¿Cuál es tu color de ojos?')

class Persona:
    def __init__(self):
        self.Nombre = nombre
        self.Edad = edad
        self.Estatura = estatura
        self.Peso = peso
        self.LargoPelo = largoPelo
        self.ColorPelo = colorPelo
        self.ColorOjos = colorOjos