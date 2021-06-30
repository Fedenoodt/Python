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

