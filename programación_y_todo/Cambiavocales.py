vocalElegida = input("Ingrese una vocal: ").lower()[0]
frase = input("ingrese su frase: ")

for j in ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]:
    frase = frase.replace(j, vocalElegida)
print(frase)