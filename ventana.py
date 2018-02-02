# VENTANAS CON PYTHON
# IMPORTAMOS MODULO
from tkinter import *

ventana = Tk()
ventana.config(bg="red")
ventana.geometry("460x360")
ventana.resizable(width=FALSE, height=TRUE)
ventana.title("Ventana de Python")
widget = Label(ventana, text='Bienvenido')
widget.pack(expand=NO, fill=BOTH)  # YES BOTH NO NONE
ventana.mainloop()
