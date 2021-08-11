from tkinter import *
from tkinter import messagebox


def info():
    messagebox.showinfo("Mensaje", "Menasaje desde messagebox")


def advertencia():
    messagebox.showwarning("Mensaje", "Mensaje de advertencia")


def pregunta():
    messagebox.askyesno("Mensaje", "Quieres continuar?")


ventana = Tk()
ventana.geometry("640x520")
boton1 = Button(ventana, text="Info", command=info).place(x=20, y=100)
boton2 = Button(ventana, text="Advertencia",
                command=advertencia).place(x=20, y=140)
boton3 = Button(ventana, text="Pregunta", command=pregunta).place(x=20, y=180)
ventana.mainloop()
