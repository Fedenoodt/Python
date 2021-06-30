def uno():
    file = open("probandoDescubriendo1.txt", "r")
    print(file.read())
    file.close()

def dos():
    usuario = input("Ingrese comentario...")
    escritura = open("probandoDescubriendo1.txt", "a")
    escritura.write(". ")
    escritura.write(usuario)
    escritura.close()

dos()
uno()