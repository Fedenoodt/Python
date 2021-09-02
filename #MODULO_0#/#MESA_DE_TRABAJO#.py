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

import sqlite3

base1 = sqlite3.connect('/home/fedenoodt/Documentos/BHSIAI/Protocolo 6/GitHub/Python/#MODULO_0#/Articulos/juegosPS2.db')
cursor = base1.cursor()
print("Base de datos creada y conectada con éxito a SQLite.-")

orden = "SELECT * FROM JUEGO"
cursor.execute(orden)
codigos = cursor.fetchall()
for i in codigos:
        print(i)