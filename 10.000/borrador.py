def puntuador(cadaCara, primerTiro, dados):
    puntos = 0
    noTirar = 0
    if primerTiro:
        if cadaCara[0] == 3:
            puntos = puntos + 1000
            noTirar = 3
        else:
            puntos = puntos + cadaCara[0] * 100
            noTirar = cadaCara[0]
        si = True
        for i in range(0, len(cadaCara)-1):
            if cadaCara[i] !=1:
                si=False
        if si:
            puntos = puntos + 1500 - 150
            noTirar = 5
    else:
        puntos = puntos + cadaCara[0] * 100
        noTirar = cadaCara[0]
    for i in (1, 2, 3, 5):
        if cadaCara[i] == 3:
            puntos = puntos + (i + 1) * 100
            noTirar = noTirar + cadaCara[i]
    puntos = puntos + cadaCara[4] * 50
    noTirar = noTirar + cadaCara[4]
    if noTirar == dados:
        dadosvuelta = 5
    else:
        dadosvuelta = dados - noTirar
    return puntos, dadosvuelta

cadaCara = [1, 1, 1, 1, 1, 0]
primerTiro = True
dados = 5
puntaje,dados = puntuador(cadaCara, primerTiro, dados)

print(puntaje, dados)