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
        #///////////////Librerías\\\\\\\\\\\\\\\#

import sqlite3, tkinter as tkr

        #///////////////Variables estáticas\\\\\\\\\\\\\\\#

def conectado():
        print("Base de datos conectada con éxito.-")

nombres = []
desarrollador1 = []
desarrollador2 = []
desarrollador3 = []

        #///////////////Herramientas\\\\\\\\\\\\\\\#

def insercion(lista, orden, columnaa):
        lista = []
        cursor.execute(orden)
        codigos = cursor.fetchall()
        for i in codigos:
                lista.append(str(i))

        filaa = 2
        for j in range(0, len(lista)):
                filaa += 1
                valor = tkr.Label(mainQuery, text = lista[j])
                valor.grid(row = filaa, column = columnaa)
        
def Reinicio(mainQuery, reinicio, database):
        if reinicio:
                mainQuery.mainloop()
                mainQuery = tkr.Tk()
                title = mainQuery.title("Biblioteca de discos compactos")
                intro = tkr.Label(mainQuery, text = "Esta es una aplicación que muestra una biblioteca de discos compactos, digitales y no digitales.")
                intro.grid(row = 0, column = 0, columnspan = 4, sticky = "WE", pady = 25)

                cursor = conexion(database)
                ingreso = interfazBusqueda()

def busqueda():
        termino = ingreso.get()
        termino = "%" + str(termino) + "%"
        print(termino)
        # orden = "SELECT * FROM JUEGO WHERE JUEGO.NOMBRE LIKE '" + termino + "'"
        # id = "SELECT JUEGO.ID_JUEGOPS2 FROM JUEGO WHERE JUEGO.NOMBRE LIKE '" + termino + "'"
        insercion(nombres, "SELECT * FROM JUEGO WHERE JUEGO.NOMBRE LIKE '" + termino + "' ORDER BY NOMBRE ASC;", 0)
        insercion(desarrollador1, "SELECT JUEGO.NOMBRE,DESARROLLADOR.NOMBRE FROM JUEGO,DESARROLLADOR WHERE juego.ID_DESARROLLADOR=DESARROLLADOR.ID_DESARROLLADOR AND JUEGO.NOMBRE LIKE '" + termino + "' ORDER BY JUEGO.NOMBRE ASC;", 1)
        insercion(desarrollador2, "SELECT JUEGO.NOMBRE,DESARROLLADOR.NOMBRE FROM JUEGO,DESARROLLADOR WHERE juego.ID_DESARROLLADOR_2=DESARROLLADOR.ID_DESARROLLADOR AND JUEGO.NOMBRE LIKE '" + termino + "' ORDER BY JUEGO.NOMBRE ASC;", 2)
        insercion(desarrollador3, "SELECT JUEGO.NOMBRE,DESARROLLADOR.NOMBRE FROM JUEGO,DESARROLLADOR WHERE juego.ID_DESARROLLADOR_3=DESARROLLADOR.ID_DESARROLLADOR AND JUEGO.NOMBRE LIKE '" + termino + "' ORDER BY JUEGO.NOMBRE ASC;", 3)
        
        #///////////////Secciones del Programa\\\\\\\\\\\\\\\#

    #----# El programa esta pautado en secciones para mejorar la visibilidad de cada una de las partes al llamar a cada base de datos.

def conexion(database):
        base = sqlite3.connect(database)
        cursor = base.cursor()
        return cursor



def interfazBusqueda():
        aclaracion = tkr.Label(mainQuery,text = "Buscar por nombre")
        ingreso =  tkr.StringVar()
        buscar = tkr.Entry(mainQuery, textvar = ingreso)
        objetivo = tkr.Button(mainQuery, text = "Buscar", command = busqueda)
        aclaracion.grid(row = 1, column = 1, sticky = "E", padx = 15, pady = 10)
        buscar.grid(row = 1, column = 2, sticky = "WE", padx = 15, pady = 10)
        objetivo.grid(row = 1, column = 3, sticky = "W", padx = 5, pady = 10)
        return ingreso

def baseJuegos():
        nombresColumn = tkr.Label(mainQuery, text = "Nombres")
        desarrollador1Column = tkr.Label(mainQuery, text = "desarrollador1")
        desarrollador2Column = tkr.Label(mainQuery, text = "desarrollador2")
        desarrollador3Column = tkr.Label(mainQuery, text = "desarrollador3")

        nombresColumn.grid(row = 2, column = 0, sticky = "WE", pady = 15)
        desarrollador1Column.grid(row = 2, column = 1, sticky = "WE", pady = 15)
        desarrollador2Column.grid(row = 2, column = 2, sticky = "WE", pady = 15)
        desarrollador3Column.grid(row = 2, column = 3, sticky = "WE", pady = 15)

        insercion(nombres, "SELECT JUEGO.NOMBRE FROM JUEGO ORDER BY NOMBRE ASC;", 0)
        insercion(desarrollador1, "SELECT JUEGO.NOMBRE,DESARROLLADOR.NOMBRE FROM JUEGO,DESARROLLADOR WHERE juego.ID_DESARROLLADOR=DESARROLLADOR.ID_DESARROLLADOR ORDER BY JUEGO.NOMBRE ASC;", 1)
        insercion(desarrollador2, "SELECT JUEGO.NOMBRE,DESARROLLADOR.NOMBRE FROM JUEGO,DESARROLLADOR WHERE juego.ID_DESARROLLADOR_2=DESARROLLADOR.ID_DESARROLLADOR ORDER BY JUEGO.NOMBRE ASC;", 2)
        insercion(desarrollador3, "SELECT JUEGO.NOMBRE,DESARROLLADOR.NOMBRE FROM JUEGO,DESARROLLADOR WHERE juego.ID_DESARROLLADOR_3=DESARROLLADOR.ID_DESARROLLADOR ORDER BY JUEGO.NOMBRE ASC;", 3)
        conectado()
        

#=////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////=#


mainQuery = tkr.Tk()
title = mainQuery.title("Biblioteca de discos compactos")
intro = tkr.Label(mainQuery, text = "Esta es una aplicación que muestra una biblioteca de discos compactos, digitales y no digitales.")
intro.grid(row = 0, column = 0, columnspan = 4, sticky = "WE", pady = 25)



cursor = conexion("/home/fedenoodt/Documentos/BHSIAI/Protocolo 6/GitHub/BAPIOIX/anio1/Segundo_Cuatrimestre/BAPIOIX-Programacion_Objetos/Clase8--20210901_Miercoles/Parcial1/beta2/juegosPS2.db")
ingreso = interfazBusqueda()
baseJuegos()


mainQuery.mainloop()