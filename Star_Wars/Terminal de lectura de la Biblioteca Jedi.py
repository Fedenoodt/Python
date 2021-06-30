#====================================================CONSTANTES========================================================#

#-----------Constantes de Enlace-----------------------

import sqlite3

llamadaaBiblioteca = sqlite3.connect('C:/Users/Eduardo/Desktop/Accesos Directos/DB Browser for SQLite/Ideas_Propias/Star Wars/Proyecto Biblioteca Jedi/Biblioteca.db')

c = llamadaaBiblioteca.cursor()

#-----------Constantes de Lectura----------------------



#===================================================DEFINICIONES=======================================================#

#-----------Definiciones de Lectura--------------------

def lecturaPlanetas():
    c.execute('''SELECT NOMBRE FROM A_PLANETAS''')
    respuesta = c.fetchall()
    for i in respuesta:
        print('{}'.format(i[0]))


#==============================================CUERPO DEL PROGRAMA=====================================================#

#-----------Entrada al Programa------------------------

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
print("                                        -Intergalactic Software 1.5-")
print("                                           'Sorteador Galactico'")

#-----------Bienvenida a la Biblioteca-----------------



#-----------Programa-----------------------------------

print(lecturaPlanetas())