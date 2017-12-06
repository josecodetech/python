#VENTANAS CON PYTHON
#AÑADIMOS ETIQUETA, CASILLA ENTRADA Y BOTONES
#IMPORTAMOS MODULO
from tkinter import *
from tkinter import messagebox
def minimizar():
    ventana.iconify()
def mensaje():
    messagebox.showinfo("mensaje","Has escrito: "+texto.get())
ventana=Tk()
ventana.config(bg="white")
ventana.geometry("460x360")
ventana.resizable(width=TRUE, height=TRUE)
ventana.title("Ventana de Python")
#definimos 2 botones
boton1=Button(ventana,text="Minimizar",command=minimizar).grid(row=2,column=1)
boton2=Button(ventana,text="Mensaje",command=mensaje).grid(row=2,column=4)
#definimos etiqueta
etiqueta1=Label(ventana,text="Operaciones con botones").grid(row=1,column=2)
#definimos entrada
texto=StringVar()
texto.set("Introduce texto para mensaje")
entrada1=Entry(ventana,width=50,bg="blue",fg="yellow",textvariable=texto).grid(row=3,column=2)
ventana.mainloop()
               
