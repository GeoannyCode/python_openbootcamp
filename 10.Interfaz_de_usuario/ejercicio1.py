"""
En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado 
y que contenga un botón de reinicio para que deje todo como al principio.

Al principio no tiene que haber una opción seleccionada.
"""

from tkinter import * 

def seleccionar():
    monitor.config(text= "{}".format(opcion.get()))

def reset():
    opcion.set(None)
    monitor.config(text="")

#configuracion
root = Tk()

opcion = IntVar()

Radiobutton(root, text="Opcion 1", variable=opcion, value=1, command=seleccionar).pack()
Radiobutton(root, text="Opcion 2", variable=opcion, value=2, command=seleccionar).pack()
Radiobutton(root, text="Opcion 3", variable=opcion, value=3, command=seleccionar).pack()


monitor = Label(root)
monitor.pack()

Button(root, text="Reiniciar", command=reset).pack()

#bucle de la aplicacion 
root.mainloop()