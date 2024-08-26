from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.geometry("320x180")
ventana.title('Saludar')

# Funciones


def mensaje():
    messagebox.showinfo("Mensaje", "Hola, "+texto.get())


def borrar():
    texto.set("")


# variable nombre
texto = StringVar()

# componentes de la ventana
etiqueta_nombre = Label(ventana, width=40, text="Nombre",
                        bg="white", fg="red").place(x=20, y=30)
caja_nombre = Entry(ventana, width=40, bg="white", fg="blue",
                    textvariable=texto).place(x=20, y=70)
btn_Saludar = Button(ventana, text="Saludar",
                     command=mensaje).place(x=20, y=100)
btn_Borrar = Button(ventana, text="Borrar", command=borrar).place(x=260, y=100)
# no olvidar
ventana.mainloop()
