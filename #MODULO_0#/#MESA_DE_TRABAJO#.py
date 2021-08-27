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

        #~~~~~~~~~~~~~//Funciones\\~~~~~~~~~~~~~#

turnosA = open("turnosA.txt", "a")
turnosB = open("turnosB.txt", "a")
turnosC = open("turnosC.txt", "a")

def versionador():
    ruta = tramite.get()
    a = 'A'
    b = 'B'
    c = 'C'
    contadorA = 0
    contadorB = 0
    contadorC = 0
    
    if str(ruta) == "reclamo":
        if contadorA >= 100:
            contadorA = -1
        contadorA += 1
        turnoA = a + '-' + str(contadorA)
        turnosA.writelines(turnoA + ";" + str(dni))
    elif str(ruta) == "altaBaja":
        if contadorB >= 100:
            contadorB = -1
        contadorB += 1
        turnoB = b + '-' + str(contadorB)
        turnosB.writelines(turnoB + ";" + str(dni))
    elif str(ruta) == "consulta":
        if contadorC >= 100:
            contadorC = -1
        contadorC += 1
        turnoC = c + '-' + str(contadorC)
        turnosC.writelines(turnoC + ";" + str(dni))

def muestra():
    ruta = tramite.get()
    if str(ruta) == "reclamo":
        pass
    elif str(ruta) == "altaBaja":
        pass
    elif str(ruta) == "consulta":
        pass
def salir():
    opcion = messagebox.askokcancel('¡Atención!', '¿Confirma que desea salir?')
    if opcion:
        exit()

        #~~~~~~~~~~~~~//Llamadas\\~~~~~~~~~~~~~#

import tkinter as tkr
from tkinter import IntVar, StringVar, messagebox

mainroot = tkr.Tk()

        #~~~~~~~~~~~~~//Encabezado\\~~~~~~~~~~~~~#

title = mainroot.title("Alimentador de mascotas confiable")
intro = tkr.Label(mainroot, text = "Por favor. Ingrese el tipo de trámite para recibir un turno.")

        #~~~~~~~~~~~~~//Zona de ingresos\\~~~~~~~~~~~~~#

txtDNI = tkr.Label(mainroot, text = "DNI:")
dni = IntVar()
entryDNI = tkr.Entry(mainroot, variable = dni, command = versionador)
txtTramite = tkr.Label(mainroot, text = "Trámite")
tramite = StringVar()
rdbtnReclamo = tkr.Radiobutton(mainroot, text = "Reclamo", variable = tramite, value = "reclamo", command = versionador)
rdbtnAltaBaja = tkr.Radiobutton(mainroot, text = "Alta / Baja", variable = tramite, value = "altaBaja", command = versionador)
rdbtnConsulta = tkr.Radiobutton(mainroot, text = "Consulta", variable = tramite, value = "consulta", command = versionador)
btnConfirma = tkr.Button(mainroot, text = "Confirmar", command = muestra)
btnSalir = tkr.Button(mainroot, text = "Salir", command = salir)


        #~~~~~~~~~~~~~//Resultado\\~~~~~~~~~~~~~#



        #~~~~~~~~~~~~~//Declaración de posiciones\\~~~~~~~~~~~~~#

intro.grid(row = 0, column = 0, columnspan = 2)
txtDNI.grid(row = 1, column = 0)
entryDNI.grid(row = 1, column = 1)
txtTramite.grid(row = 2, column = 0, columnspan = 2)
rdbtnReclamo.grid(row = 3, column = 0, columnspan = 2)
rdbtnAltaBaja.grid(row = 4, column = 0, columnspan = 2)
rdbtnConsulta.grid(row = 5,column = 0, columnspan = 2)
btnConfirma.grid(row = 6, column = 0, sticky = "WE")
btnSalir.grid(row = 6, column = 1, sticky = "WE")

        #~~~~~~~~~~~~~//Cierre\\~~~~~~~~~~~~~#

mainroot.mainloop()
turnosA.close()
turnosB.close()
turnosC.close()