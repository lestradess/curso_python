from tkinter import *

root = Tk()

listado = Listbox(root)
for item in ["Perro","Gato", "Oveja", "Ratón", "termera", "pato"]:
    listado.insert(0, item)
listado.pack()
label = Label(root, text="Listado animales").pack()

root.mainloop()
