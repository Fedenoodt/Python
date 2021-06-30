import apoyo
respuesta = ''
while respuesta != '*':
    for i in range(10):
        print('')
    print('Buenas, ingrese 1 Sumar')
    print('Ingrese 2 para restar')
    print('ingrese 3 para multiplicar')
    print('ingrese 4 para dividir')
    print('ingrese "*" para salir.')
    respuesta = ''
    while respuesta != '1' and respuesta != '2' and respuesta != '3' and respuesta != '4' and respuesta != '*':
        for i in range(10):
            print('')
        respuesta = input('=>       ')
        if respuesta != '1' and respuesta != '2' and respuesta != '3' and respuesta != '4' and respuesta != '*':
            print('Ingreso respuesta erronea')

    if respuesta != '*':
        primera = float(input('Ingrese primer número      '))
        segunda = float(input('Ingrese segundo numero     '))
        print('resultado =', apoyo.operaciones[int(respuesta) - 1](primera, segunda))
        input('Presione cualquier tecla para continuar.')