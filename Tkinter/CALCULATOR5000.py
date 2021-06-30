from tkinter import *
import numpy

root = Tk()
root.geometry("412x400")
root.title("CALCULATOR 5000")
root.configure(bg='#000110')


relleno3 = Label(root, text='    ')
relleno3.grid(row=0, column=2, padx=0)
relleno3.configure(bg='#000110')

pantalla = Entry(root, width=30, borderwidth=2)
pantalla.grid(row=1, column=1, padx=0, columnspan=3)
pantalla.configure(bg='#d2dafa')
pantalla.config(highlightbackground='#263c9b')
#======================================================================================================================#

def display(character):
    current = pantalla.get()
    pantalla.delete(0, END)
    pantalla.insert(0, current + character)

def DELdisplay():
    pantalla.delete(0, END)



def operacion01():
    first_number = pantalla.get()
    global f_number01
    global math
    math = 'Suma'
    f_number01 = float(first_number)
    pantalla.delete(0, END)

def operacion02():
    first_number = pantalla.get()
    global f_number02
    global math
    math = 'Resta'
    f_number02 = float(first_number)
    pantalla.delete(0, END)

def operacion03():
    first_number = pantalla.get()
    global f_number03
    global math
    math = 'Multiplicacion'
    f_number03 = float(first_number)
    pantalla.delete(0, END)

def operacion04():
    first_number = pantalla.get()
    global f_number04
    global math
    math = 'Division'
    f_number04 = float(first_number)
    pantalla.delete(0, END)

def operacion05():
    first_number = pantalla.get()
    global f_number05
    global math
    math = 'Potencia'
    f_number05 = float(first_number)
    pantalla.delete(0, END)

'''def operacion05bis():
    for i in range(1, second_number):
        first_number'''

def operacion06():
    pass

def operacion07():
    first_number = pantalla.get()
    global abrir
    abrir = True
    global f_number
    f_number = float(first_number)

def operacion08():
    first_number = pantalla.get()
    global cerrar
    cerrar = True
    global f_number
    f_number = float(first_number)


def operacion09():
    pass

def operacion10():
    pass

def operacion11():
    pass

def operacion12():
    pass

def operacion13():
    pass

def operacion14():
    pass

def resultado():
    global second_number
    second_number = pantalla.get()
    pantalla.delete(0, END)
    if math == 'Suma':
        pantalla.insert(0, f_number01 + float(second_number))
    if math == 'Resta':
        pantalla.insert(0, f_number02 - float(second_number))
    if math == 'Multiplicacion':
        pantalla.insert(0, f_number03 * float(second_number))
    if math == 'Division':
        pantalla.insert(0, f_number04 / float(second_number))
    if math == 'Potencia':
        exponente = float(second_number)
        for i in range(0.0, exponente):
            pantalla.insert(0, f_number05 * float(f_number05))
        #pantalla.insert(0, f_number  float(second_number))






#======================================================================================================================#

separacion = Label(root, text=' HELLO ', fg='#d2dafa', padx=100)
separacion.grid(row=2, column=2, padx=0)
separacion.configure(bg='#000110')

uno = Button(root, text='1', padx=30, command=lambda: display('1'))
uno.grid(row=3, column=1, padx=5)
uno.configure(bg='#697fda')
uno.config(highlightbackground='#263c9b')

dos = Button(root, text='2', padx=30, command=lambda: display('2'))
dos.grid(row=3, column=2, padx=0)
dos.configure(bg='#697fda')
dos.config(highlightbackground='#263c9b')

tres = Button(root, text='3', padx=30, command=lambda: display('3'))
tres.grid(row=3, column=3, padx=0)
tres.configure(bg='#697fda')
tres.config(highlightbackground='#263c9b')

cuatro = Button(root, text='4', padx=30, command=lambda: display('4'))
cuatro.grid(row=4, column=1, padx=5)
cuatro.configure(bg='#697fda')
cuatro.config(highlightbackground='#263c9b')

cinco = Button(root, text='5', padx=30, command=lambda: display('5'))
cinco.grid(row=4, column=2, padx=0)
cinco.configure(bg='#697fda')
cinco.config(highlightbackground='#263c9b')

seis= Button(root, text='6', padx=30, command=lambda: display('6'))
seis.grid(row=4, column=3, padx=0)
seis.configure(bg='#697fda')
seis.config(highlightbackground='#263c9b')

siete = Button(root, text='7', padx=30, command=lambda: display('7'))
siete.grid(row=5, column=1, padx=5)
siete.configure(bg='#697fda')
siete.config(highlightbackground='#263c9b')

ocho = Button(root, text='8', padx=30, command=lambda: display('8'))
ocho.grid(row=5, column=2, padx=0)
ocho.configure(bg='#697fda')
ocho.config(highlightbackground='#263c9b')

nueve = Button(root, text='9', padx=30, command=lambda: display('9'))
nueve.grid(row=5, column=3, padx=0)
nueve.configure(bg='#697fda')
nueve.config(highlightbackground='#263c9b')

cero = Button(root, text='0', padx=30, command=lambda: display('0'))
cero.grid(row=6, column=1, padx=5)
cero.configure(bg='#697fda')
cero.config(highlightbackground='#263c9b')

calcular = Button(root, text='Calcular', padx=7, command=resultado)
calcular.grid(row=6, column=3, padx=0)
calcular.configure(bg='#697fda')
calcular.config(highlightbackground='#263c9b')

borrar = Button(root, text='Borrar', padx=14, command= DELdisplay)
borrar.grid(row=6, column=2, padx=0)
borrar.configure(bg='#697fda')
borrar.config(highlightbackground='#263c9b')



#======================================================================================================================#

decoracion1 = Button(root, text=' \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ ', padx=0, pady=0, state=DISABLED)
decoracion1.grid(row=8, column=1, padx=0, columnspan=1)
decoracion1.configure(bg='#473521')
decoracion1.config(highlightbackground='#474645')

calculator5000 = Button(root, text='I AM YOUR CALCULATOR 5000', fg='#1c6f64', padx=0, pady=0, state=DISABLED)
calculator5000.grid(row=8, column= 2, padx=0, columnspan=1)
calculator5000.configure(bg='#1ba28f')
calculator5000.config(highlightbackground='#025247', font=('Arial Black', 12))

decoracion2 = Button(root, text=' /////////////// ', padx=0, pady=0, state=DISABLED)
decoracion2.grid(row=8, column=3, padx=0, columnspan=1)
decoracion2.configure(bg='#473521')
decoracion2.config(highlightbackground='#474645')

sumar01 = Button(root, text='+', padx=16, pady=2, command=operacion01)
sumar01.grid(row=9, column=1, padx=0)
sumar01.configure(bg='#697fda')
sumar01.config(highlightbackground='#263c9b')

restar02 = Button(root, text='-', padx=20, pady=2, command=operacion02)
restar02.grid(row=9, column=2, padx=0)
restar02.configure(bg='#697fda')
restar02.config(highlightbackground='#263c9b')

multiplicar03 = Button(root, text='x', padx=15, pady=2, command=operacion03)
multiplicar03.grid(row=9, column=3, padx=0)
multiplicar03.configure(bg='#697fda')
multiplicar03.config(highlightbackground='#263c9b')

dividir04 = Button(root, text='%', padx=15, pady=2, command=operacion04)
dividir04.grid(row=10, column=1, padx=0)
dividir04.configure(bg='#697fda')
dividir04.config(highlightbackground='#263c9b')

potencia05 = Button(root, text='^', padx=17, pady=2, command=operacion05)
potencia05.grid(row=10, column=2, padx=0)
potencia05.configure(bg='#697fda')
potencia05.config(highlightbackground='#263c9b')

raiz06 = Button(root, text='√', padx=15, pady=2, command=lambda: display())
raiz06.grid(row=10, column=3, padx=0)
raiz06.configure(bg='#697fda')
raiz06.config(highlightbackground='#263c9b')

abrir07 = Button(root, text='(', padx=19, pady=2, command=lambda: display('('))
abrir07.grid(row=11, column=1, padx=0)
abrir07.configure(bg='#697fda')
abrir07.config(highlightbackground='#263c9b')

cerrar08 = Button(root, text=')', padx=20, pady=2, command=lambda: display(')'))
cerrar08.grid(row=11, column=2, padx=0)
cerrar08.configure(bg='#697fda')
cerrar08.config(highlightbackground='#263c9b')

logaritmo10_09 = Button(root, text='log', padx=10, pady=3, command=lambda: display())
logaritmo10_09.grid(row=11, column=3, padx=0)
logaritmo10_09.configure(bg='#697fda')
logaritmo10_09.config(highlightbackground='#263c9b')

logNatural10 = Button(root, text='ln', padx=16, pady=2, command=lambda: display())
logNatural10.grid(row=12, column=1, padx=0)
logNatural10.configure(bg='#697fda')
logNatural10.config(highlightbackground='#263c9b')

hiperbolicas11 = Button(root, text='hyp', padx=11, pady=2, command=lambda: display())
hiperbolicas11.grid(row=12, column=2, padx=0)
hiperbolicas11.configure(bg='#697fda')
hiperbolicas11.config(highlightbackground='#263c9b')

seno12 = Button(root, text='sin', padx=10, pady=2, command=lambda: display())
seno12.grid(row=12, column=3, padx=0)
seno12.configure(bg='#697fda')
seno12.config(highlightbackground='#263c9b')

coseno13 = Button(root, text='cos', padx=10, pady=2, command=lambda: display())
coseno13.grid(row=13, column=1, padx=0)
coseno13.configure(bg='#697fda')
coseno13.config(highlightbackground='#263c9b')

decimal14 = Button(root, text='.', padx=21, pady=2, command=lambda: display('.'))
decimal14.grid(row=13, column=2, padx=0)
decimal14.configure(bg='#697fda')
decimal14.config(highlightbackground='#263c9b')

tangente15 = Button(root, text='tan', padx=10, pady=2, command=lambda: display())
tangente15.grid(row=13, column=3, padx=0)
tangente15.configure(bg='#697fda')
tangente15.config(highlightbackground='#263c9b')







#======================================================================================================================#


air01 = Label(root, text='  ')
air01.grid(row=49, column=1, padx=0,columnspan=1)
air01.configure(bg='#000110')
air01.config(font=('Courier', 9))

software = Label(root, text='Intergalactic Software 1.0', fg='white')
software.grid(row=50, column=1, padx=0, columnspan=3)
software.configure(bg='#000110')
software.config(font=('Courier', 9))

introduccion = Label(root, text='Developmented by Fedenoodt', fg='white')
introduccion.grid(row=51, column=1, padx=0, columnspan=3)
introduccion.configure(bg='#000110')
introduccion.config(font=('Courier', 9))



root.mainloop()