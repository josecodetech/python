from tkinter import *
from tkinter import messagebox


def salir():
    opcion = messagebox.askquestion("Salir", "Quieres salir de la aplicacion")
    # print(opcion)
    if opcion == "yes":
        ventana.destroy()


ventana = Tk()
ventana.geometry("640x520")
barraMenu = Menu(ventana)
ventana.config(menu=barraMenu)
menuArchivo = Menu(barraMenu, tearoff=0)
menuArchivo.add_command(label="Abrir")
menuArchivo.add_separator()
menuArchivo.add_command(label="Salir", command=salir)
menuAyuda = Menu(barraMenu, tearoff=0)
menuAyuda.add_command(label="Acerca de")
barraMenu.add_cascade(label="Archivo", menu=menuArchivo)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)
ventana.mainloop()
