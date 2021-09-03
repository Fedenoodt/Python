#import CAJA_HERRAMIENTAS

#=////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////=#

#~~#TAREA ACTUAL:#~~#

#=////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////=#

#~~#Separadores#~~#
#=////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////=#
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #####RESOLVER######ACA##########

#~~#Titulos#~~#
        #///////////////\\\\\\\\\\\\\\\#

#~~#Subtitulos#~~#
        #~~~~~~~~~~~~~//\\~~~~~~~~~~~~~#
        #=#  #=# #~~~~~~~~~~~~~//\\~~~~~~~~~~~~~#

#~~#Asuntos puntuales#~~#
    #----# Texto

#=////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////=#

import sqlite3, tkinter as tkr

nombres = []
desarrollador1 = []
desarrollador2 = []
desarrollador3 = []

def insercion(lista, orden, columnaa):
        lista = []
        cursor.execute(orden)
        codigos = cursor.fetchall()
        for i in codigos:
                lista.append(str(i))

        filaa = 1
        for j in range(0, len(lista)):
                filaa += 1
                valor = tkr.Label(mainQuery, text = lista[j])
                valor.grid(row = filaa, column = columnaa)

mainQuery = tkr.Tk()
title = mainQuery.title("Biblioteca de discos compactos")
intro = tkr.Label(mainQuery, text = "Esta es una aplicación que muestra una biblioteca de discos compactos, digitales y no digitales.")
nombresColumn = tkr.Label(mainQuery, text = "Nombres")
desarrollador1Column = tkr.Label(mainQuery, text = "desarrollador1")
desarrollador2Column = tkr.Label(mainQuery, text = "desarrollador2")
desarrollador3Column = tkr.Label(mainQuery, text = "desarrollador3")


intro.grid(row = 0, column = 0, columnspan = 4, sticky = "WE", pady = 25)
nombresColumn.grid(row = 1, column = 0, sticky = "WE", pady = 15)
desarrollador1Column.grid(row = 1, column = 1, sticky = "WE", pady = 15)
desarrollador2Column.grid(row = 1, column = 2, sticky = "WE", pady = 15)
desarrollador3Column.grid(row = 1, column = 3, sticky = "WE", pady = 15)

base1 = sqlite3.connect('/home/fedenoodt/Documentos/BHSIAI/Protocolo 6/GitHub/Python/#MODULO_0#/Articulos/juegosPS2.db')
cursor = base1.cursor()
print("Base de datos conectada con éxito a SQLite.-")
"""
orden = "SELECT JUEGO.NOMBRE FROM JUEGO ORDER BY NOMBRE ASC"
cursor.execute(orden)
codigos = cursor.fetchall()
for i in codigos:
        nombres.append(str(i))
        """
insercion(nombres, "SELECT JUEGO.NOMBRE FROM JUEGO ORDER BY NOMBRE ASC;", 0)
insercion(desarrollador1, "SELECT JUEGO.NOMBRE,DESARROLLADOR.NOMBRE FROM JUEGO,DESARROLLADOR WHERE juego.ID_DESARROLLADOR=DESARROLLADOR.ID_DESARROLLADOR ORDER BY JUEGO.NOMBRE ASC;", 1)
insercion(desarrollador2, "SELECT JUEGO.NOMBRE,DESARROLLADOR.NOMBRE FROM JUEGO,DESARROLLADOR WHERE juego.ID_DESARROLLADOR_2=DESARROLLADOR.ID_DESARROLLADOR ORDER BY JUEGO.NOMBRE ASC;", 2)
insercion(desarrollador3, "SELECT JUEGO.NOMBRE,DESARROLLADOR.NOMBRE FROM JUEGO,DESARROLLADOR WHERE juego.ID_DESARROLLADOR_3=DESARROLLADOR.ID_DESARROLLADOR ORDER BY JUEGO.NOMBRE ASC;", 3)


mainQuery.mainloop()