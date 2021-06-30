frase = input("Ingrese su frase: ")


fraseLista = frase.append(frase)

consonantes = ["q", "w", "r", "t", "y", "p", "s", "d", "f", "g", "h", "j", "k", "l", "ñ", "z", "x", "c", "v", "b", "n",
               "m"]
vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]

fraseConsonante = fraseLista.remove(vocales)
print(fraseConsonante)