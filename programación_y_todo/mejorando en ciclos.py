letras = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(len(letras))
largo = len(letras)
destino = []
for i in range(0, largo):
    print(letras[i])
    if letras[i] != "d":
        destino.append(letras[i])
print(letras)
print(destino)