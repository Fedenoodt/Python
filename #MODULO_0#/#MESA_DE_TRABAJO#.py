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

        #///////////////Ejercicio 6\\\\\\\\\\\\\\\#

        #~~~~~~~~~~~~~//Llamadas\\~~~~~~~~~~~~~#

import tkinter as tkr
from tkinter import messagebox

mainroot = tkr.Tk()

        #~~~~~~~~~~~~~//Funciones\\~~~~~~~~~~~~~#

def calcular():
    resultado = var.get()
    if btnPerro.get():
        resultado += 'Perro'
    elif btnGato.get():
        resultado += 'Gato'


def salir():
    opcion = messagebox.askokcancel('¡Atención!', '¿Confirma que desea salir?')
    if opcion:
        exit()

        #~~~~~~~~~~~~~//Encabezado\\~~~~~~~~~~~~~#

title = mainroot.title("Alimentador de mascotas fiable")
intro = tkr.Label(mainroot, text = "Este es un instrumento para medir el alimento de su perro o gato.")

        #~~~~~~~~~~~~~//Zona de ingresos\\~~~~~~~~~~~~~#

    #----# Textos y entradas
lblPeso = tkr.Label(mainroot, text = "Ingrese el peso de su animal:")
txtPeso = tkr.Entry(mainroot)
lblMascota = tkr.Label(mainroot, text = "Marqué que animal es su mascota.")
    #----# Botones
btnPerro = tkr.IntVar()
btnGato = tkr.IntVar()
chkPerro = tkr.Checkbutton(mainroot, text = "Perro", variable = btnPerro)
chkGato = tkr.Checkbutton(mainroot, text = "Gato", variable = btnGato)
btnGeneral = tkr.Button(mainroot, text = "Calcular", command = calcular)
btnSalir= tkr.Button(mainroot, text = "Salir", command = salir)

        #~~~~~~~~~~~~~//Resultado\\~~~~~~~~~~~~~#

var = tkr.StringVar()
valor = tkr.Label(mainroot, text = "", variable = var)

        #~~~~~~~~~~~~~//Declaración de posiciones\\~~~~~~~~~~~~~#

    #----# Textos y entradas
intro.grid(row = 0, column = 0, padx = 10, pady = 5)
lblPeso.grid(row = 1, column = 0, padx = 10, pady = 5)
txtPeso.grid(row = 1, column = 1, padx = 10, pady = 5)
lblMascota.grid(row = 3, column = 0, padx = 10, pady = 5)
    #----# Botones
chkPerro.grid(row = 2, column = 0, padx = 10, pady = 5)
chkGato.grid(row = 2, column = 1, padx = 10, pady = 5)
btnGeneral.grid(row = 3, column = 0, sticky = "WE", padx = 10, pady = 5)
btnSalir.grid(row = 3, column = 1, sticky = "WE", padx = 10, pady = 5)
    #----# Resultados
var.grid(row = 4, column = 0, sticky = "WE", padx = 10, pady = 5)

        #~~~~~~~~~~~~~//Cierre del bucle\\~~~~~~~~~~~~~#

mainroot.mainloop()