import random

#======================================================================================================================#



def eleccion(items):
    eleccion = random.choices(items)
    return eleccion

#======================================================================================================================#

print(
    "  _____________________    _           _____             _              _      _       ____       ________          ")
print(
    " /               |        / \         |     \             \            /      / \     |    \     /                  ")
print(
    " \_____          |       /___\        |_____/              \    /\    /      /___\    |____/     \______            ")
print(
    "        \        |      /     \       |   \                 \  /  \  /      /     \   |   \             \           ")
print(
    "  ______/        |     /       \      |    \______           \/    \/      /       \  |    \____________/           ")
print("                                        -Intergalactic Software 3.2-")
print("                                           'Sorteador Galactico'")

print("¿Como te llamas, extraño?   ")
print(" ")
nombre = input("")
print(" ")
print("Bienvenido", nombre + "...")
print(" ")
print("¿Una nueva adquisición para tus estanterías", nombre + "? Ja! ¿De que se trata esta vez?")


print(" ")





repetir = 'si'

personajes = ''
naves = ''
Articulos_Especiales = ''
caminos = ''


while repetir == 'si' or repetir == 'Si' or repetir == 'SI' or repetir == 'S' or repetir == 's':
    contador = 0
    cosas = []
    cosasTemporaria = []
    print("♦ Personajes~Naves~Articulos Especiales ♦")
    print(" ")
    caminos = input("►  ")

    if caminos == "personajes" or caminos == "Personajes" or caminos == "PERSONAJES":
        print("Cuenteme todos los personajes a sortear, y digame '*' cuando haya terminado.    ")
        personajes = input("")
        contador = contador + 1
        print(contador)
    elif caminos == "Naves" or caminos == "naves" or caminos == "NAVES":
        print("Cuenteme todas las naves a sortear, y digame '*' cuando haya terminado.    ")
        naves = input("")
        contador = contador + 1
        print(contador)
    elif caminos == "Articulos Especiales" or caminos == "articulos especiales" or caminos == "Artículos Especiales" or caminos == "artículos especiales" or caminos == "ARTICULOS ESPECIALES" or caminos == "ARTÍCULOS ESPECIALES":
        print("Cuenteme todos los Artículos Especiales a sortear, y digame '*' cuando haya terminado.    ")
        Articulos_Especiales = input("")
        contador = contador + 1
        print(contador)

    while caminos != "personajes" and caminos != "Personajes" and caminos != "PERSONAJES" and caminos !=  "Naves" and caminos != "naves" and caminos != "NAVES" and caminos != "Articulos Especiales" and caminos != "articulos especiales" and caminos != "Artículos Especiales" != "artículos especiales" and caminos != "ARTICULOS ESPECIALES" and caminos != "ARTÍCULOS ESPECIALES":
        print("¿Como? ¿Vas a ingresar contenido? Por favor, selecciona algúna de las opciones.  ")
        caminos = input("►  ")
        if caminos == "personajes" or caminos == "Personajes" or caminos == "PERSONAJES":
            print("Cuenteme todos los personajes a sortear, y digame '*' cuando haya terminado.    ")
            personajes = input("")
            contador = contador + 1
            print(contador)
        elif caminos == "Naves" or caminos == "naves" or caminos == "NAVES":
            print("Cuenteme todas las naves a sortear, y digame '*' cuando haya terminado.    ")
            naves = input("")
            contador = contador + 1
            print(contador)
        elif caminos == "Articulos Especiales" or caminos == "articulos especiales" or caminos == "Artículos Especiales" or caminos == "artículos especiales" or caminos == "ARTICULOS ESPECIALES" or caminos == "ARTÍCULOS ESPECIALES":
            print("Cuenteme todos los Artículos Especiales a sortear, y digame '*' cuando haya terminado.    ")
            Articulos_Especiales = input("")
            contador = contador + 1
            print(contador)

    while (caminos != "*"):
        caminos = input(" ")
        contador = contador + 1
        print(contador)
        cosas.append(caminos)

    cosas.remove('*')
    n = int(input("Bueno, ahora digame cuantos quieres que sean los ganadores.  "))
    cosasTemporaria = cosas

    for i in range(n):
        cantGanadores = eleccion(cosasTemporaria)
        cosasTemporaria.remove(cantGanadores[0])
        print("Ganador/es:", cantGanadores)

    volvio = input('¿Desea hacer otro sorteo? (Si/No)')
    repetir = volvio

print("Eso ha sido todo,", nombre + ", espero haya quedado satisfech@ con los ganadores, y que la fuerza le acompañe...")