#import CAJA_HERRAMIENTAS

#=////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////=#

#~~#TAREA ACTUAL:#~~#


#=////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////=#
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #///////////////\\\\\\\\\\\\\\\#
        #~~~~~~~~~~~~~//\\~~~~~~~~~~~~~#
        #=#  #=# #~~~~~~~~~~~~~//\\~~~~~~~~~~~~~#
        #####RESOLVER######ACA##########

#=////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////=#

inmuebles = open("C:/Users/eduno/OneDrive/Documents/Fede/BAPIOIX-Introduccion_Programacion/Actividades/Ejercicio_inmuebles/inmuebles.csv", "r")

        #=# 1 #=# #~~~~~~~~~~~~~//Lista de Vendedores\\~~~~~~~~~~~~~#

        #~~~~~~~~~~~~~//Definiciones\\~~~~~~~~~~~~~#

listado = {}
titulos = []
listaNativa = []
data = []

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
referencia = []
fecha_alta = []
tipo = []
operacion = []
provincia = []
superficie = []
precio_venta = []
fecha_venta = []
vendedor = []

        #~~~~~~~~~~~~~//Funciones\\~~~~~~~~~~~~~#

def operacionador(linea, valor, almacenaje):
    for l in linea:
        if l == ';' or l == '\n' or l == '"' or l == '':
            if valor != '':    
                almacenaje.append(valor)
            valor = ''
        else:
            valor += l

def primeraLinea(titulos):
    titulo = ''
    lineaUno = inmuebles.readline()
    operacionador(lineaUno, titulo, titulos)
    
def crearDiccionario():
    primeraLinea(titulos)
    for t in range(len(titulos)):
        listado[titulos[t]] = []
    return listado

def informacion(listaNativa):
    detalle = ''
    for linea in inmuebles:
        operacionador(linea, detalle, listaNativa)
        
    return data

def versionador(listaNativa):
    for d in range(9, len(listaNativa)):
        print(listaNativa[d])
        return listaNativa

        #####RESOLVER######ACA##########
        # Hace falta completar esta funcion, que va a insertar en cada lista, la informacion.

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def main(data):
    listado = crearDiccionario()
    linea = inmuebles.readline()
    listaNativa = informacion(listaNativa)
            

    print(listado)
            
        #~~~~~~~~~~~~~//Cuerpo\\~~~~~~~~~~~~~#


# main(listaNativa)

listaNativa = informacion(listaNativa)

print(listaNativa[9])
for d in range(9, len(listaNativa)):
    data.append(listaNativa[d])

print(data)
        #####RESOLVER######ACA##########
