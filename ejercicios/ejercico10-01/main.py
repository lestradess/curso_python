from tkinter import *

root = Tk()
root.geometry("150x150")
root.title("Elegir opción")


def seleccion():
    label.config(text="Eres {}".format(opcion.get()))


def reset():
    opcion.set("None")
    label.config(text="")


opcion = StringVar()
opcion.set("None")

Radiobutton(root, text="Hola", var=opcion,
            value=" Español", command=seleccion).pack()
Radiobutton(root, text="Hello", var=opcion,
            value=" Inglés", command=seleccion).pack()
Radiobutton(root, text="Hallo", var=opcion,
            value=" Alemán", command=seleccion).pack()

label = Label(root)
label.pack()

Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()
