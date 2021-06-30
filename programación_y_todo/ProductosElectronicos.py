import sqlite3
from CONSTANTES import SQL

def opciones():
    validas=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','*']
    ingreso=input('Ingrese la opción deseada o "*" para salir =>   ')
    while ingreso not in validas:
        print('Ingreso una opción no valida, por favor vuelva a intentarlo')
        ingreso = input('Ingrese la opción deseada o "*" para salir =>   ')
    return ingreso
def impresion(respuesta):
    for i in range(len(respuesta)-1):
        print(respuesta[i])


base=sqlite3.connect('C:/Users/Eduardo/PycharmProjects/programación_y_todo/productos electronicos.db')
c = base.cursor()

print("Ingrese opcion deseada, * para salir")
print ("1.- Obtener los nombres de los productos de la tienda.")
print ("2.-Obtener los nombres y los precios de los productos de la tienda.")
print ("3.-Obtener el nombre de los productos que cuesten menos de 200.")
print ("4.-Obtener el nombre de los productos que cuesten entre 200 y 500.")
print ("5.-Obtener el nombre y el precio en u$s de todos los productos.")
print ("6.-Obtener el promedio de los precios de los productos.")
print ("7.-Obtener el promedio de los precios del fabricante 2.")
print ("8.-Obtener la cantidad de artículos que cuesten más que 100.")
print ("9.-Obtener el nombre y precio de los artículos cuyo precio sea mayor a 180 "
       "y ordenarlos descendentemente por precio y luego ascendentemente por nombre.")
print ("10.-Obtener un listado de los artículos incluyendo nombre del artículo y nombre del fabricante.")
print ("11.-Obtener un listado completo de los artículos incluyendo nombre y precio del artículo y nombre del fabricante.")
print ("12.-Obtener el precio medio de los productos de cada fabricante, mostrando sólo los códigos de fabricante.")
print ("13.-Obtener el precio medio de los productos de cada fabricante, mostrando el nombre del fabricante.")
print ("14.-Obtener los nombres de los fabricantes que ofrezcan productos cuyo precio medio sea mayor o igual a 150.")
print ("15.-Obtener el nombre y el precio del artículo más barato.")
print ("16.-Obtener una lista con el nombre y precio de los artículos más caros de cada fabricante (incluyendo el nombre del proveedor).")
print ('17.-Cambiar el nombre del producto 8 a "Impresora Laser".')
print ("18.-Aplicar un 10% de descuento a todos los productos. Actualizando los valores.")
print ("19.-Aplicar un descuento de 10% a todos los productos cuyo precio sea mayor o igual a 120.")
opcion=opciones()

while opcion != "*":
    if opcion == "1":
        c.execute (SQL[0])
        respuesta = c.fetchall()
        impresion(respuesta)
    elif opcion == "2":
        c.execute (SQL[1])
        respuesta = c.fetchall()
        impresion(respuesta)
    elif opcion == "3":
        c.execute(SQL[2])
        respuesta = c.fetchall()
        impresion(respuesta)
    opcion=opciones()
print("Un placer ayudarllo...")
