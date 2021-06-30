numeroDistinto = False

impares = [1, 1, 3, 3, 5, 7, 7, 9, 9]

while numeroDistinto == False:
    for i in range(0,8):
        print(impares[i])
        if impares[i] != impares[i+1] and impares[i] != impares[i-1]:
            numeroDistinto = True
            print('El numero impar, sin par, es:', impares[i], '.')