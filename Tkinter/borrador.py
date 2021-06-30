from tkinter import *

root = Tk()
root.geometry("410x400")
root.title("CALCULATOR 5000")
root.configure(bg='#000110')

display = Entry(root, width=30, borderwidth=2)
display.grid(row=1, column=2, padx=0)
display.configure(bg='#d2dafa')
display.config(highlightbackground='#263c9b')

def display():
    return

uno = Button(root, text='1', padx=30, command=display)
uno.grid(row=3, column=1, padx=5)
uno.configure(bg='#697fda')
uno.config(highlightbackground='#263c9b')