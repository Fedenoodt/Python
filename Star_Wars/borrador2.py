import sqlite3

llamadaaBiblioteca = sqlite3.connect('C:/Users/Eduardo/Desktop/Accesos Directos/DB Browser for SQLite/Ideas_Propias/Star Wars/Proyecto Biblioteca Jedi/Biblioteca.db')

c = llamadaaBiblioteca.cursor()



todoPlanetas = c.execute("""SELECT NOMBRE FROM A_PLANETAS""")

def mostrar():
    c.execute(todoPlanetas)
    respuesta = c.fetchall()
    for i in respuesta:
        print('{}'.format(i[0]))
mostrar()