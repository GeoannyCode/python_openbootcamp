"""
En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista 
de elementos seleccionables, también debe de tener un label con el texto que queráis.
"""

from tkinter import *

#configuracion 
root = Tk()
root.title("Cafeteria")

py = IntVar()
js = IntVar()
jv = IntVar()
rs = IntVar()
c = IntVar()

frame = Frame(root).pack(side=RIGHT)

Label(frame,text="¿Lenjuages de programación?\n").pack(anchor="w")

Checkbutton(frame, text="Phython", variable=py, onvalue=1, offvalue=0).pack(anchor="w")
Checkbutton(frame, text="JavaScript", variable=js, onvalue=1, offvalue=0).pack(anchor="w")
Checkbutton(frame, text="Java", variable=jv, onvalue=1, offvalue=0).pack(anchor="w")
Checkbutton(frame, text="Rust", variable=rs, onvalue=1, offvalue=0).pack(anchor="w")
Checkbutton(frame, text="C#", variable=c, onvalue=1, offvalue=0).pack(anchor="w")

monitor = Label(root)
monitor.pack()

root.mainloop()