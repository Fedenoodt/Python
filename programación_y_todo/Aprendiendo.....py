cambiovocal = input("ingrese una vocal: ")
frase = input("Ingrese su frase: ")

for j in ["a", "e", "i", "o", "u"]:
    frase = frase.replace(j, cambiovocal)
print(frase)