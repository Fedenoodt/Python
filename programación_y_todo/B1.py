import random



def eleccion(cosas):
    eleccion = random.choices(cosas)
    return eleccion


contador = 0
cosas = []

algo = input("ingrese caca")
contador = contador + 1
print(contador)
cosas.append(algo)

while (algo != "*"):
    algo = input("ingrese caca")
    contador = contador + 1
    print(contador)
    cosas.append(algo)
n = int(input("Ingrese valor"))

for i in range(n):
    prueba = eleccion(cosas)
    print(prueba)
