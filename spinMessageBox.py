#Combo o Spin y MessageBox
from tkinter import *
from tkinter import messagebox
def mostrar():
    messagebox.showinfo("Mensaje","El valor es : "+valor.get())

ventana=Tk()
ventana.geometry("400x400")
ventana.title("Spinbox Python")
#variable
valor=StringVar()
etiqueta=Label(ventana,text="Spinbox").place(x=20,y=20)
combo=Spinbox(ventana,from_=1,to=10,textvariable=valor).place(x=20,y=60)
boton=Button(ventana,text="Valor",command=mostrar).place(x=20,y=100)

ventana.mainloop()
