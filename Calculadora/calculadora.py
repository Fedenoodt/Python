import soporte


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
        print('resultado =', soporte.operaciones[int(accion) - 1](primera, segunda))
        input('Presione cualquier tecla para continuar.')


for i in range(0, 30):
    print('')
print('Espero haberlo ayudado. Hasta luego.')