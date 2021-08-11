from tkinter import *
from PIL import ImageTk, Image

ventana = Tk()
ventana.geometry("640x520")
imagen = ImageTk.PhotoImage(Image.open("logo_python.jpg"))
imgLabel = Label(ventana, image=imagen).place(x=100, y=150)
ventana.mainloop()
