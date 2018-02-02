#MessageBox
from tkinter import *
from tkinter import messagebox
def info():
    messagebox.showinfo("Mensaje","Mensaje")
def advertencia():
    messagebox.showwarning("Mensaje","Mensaje Advertencia")
def pregunta():
   # messagebox.askquestion("Mensaje","Quieres salir?")
   # messagebox.askokcancel("Mensaje","Quieres salir?")
   # messagebox.askyesno("Mensaje","Quieres salir?")
    messagebox.askretrycancel("Mensaje","Quieres salir?")
ventana=Tk()
ventana.geometry("400x400")
ventana.title("Message Box Python")

boton1=Button(ventana,text="Info",command=info).place(x=20,y=100)
boton2=Button(ventana,text="Advertencia",command=advertencia).place(x=20,y=120)
boton3=Button(ventana,text="Pregunta",command=pregunta).place(x=20,y=140)

ventana.mainloop()
