from tkinter import *


def click():
    cadena = "Pulsastes "
    if(color01.get()):
        cadena += "Rojo "
        ventana.config(bg="red")
    if(color02.get()):
        cadena += "Azul "
        ventana.config(bg="blue")
    if(color03.get()):
        cadena += "Amarillo "
        ventana.config(bg="yellow")
    if (not color01.get() and not color02.get() and not color03.get()):
        cadena = "No hay nada pulsado"
        ventana.config(bg="white")
    etiqueta.config(text=cadena)


ventana = Tk()
ventana.title("OptionButton")
ventana.geometry("640x360")
frame = Frame()
frame.pack()
color01 = IntVar()  # 1 o 0
color02 = IntVar()
color03 = IntVar()
chkRojo = Checkbutton(frame, text="Rojo", variable=color01,
                      onvalue=1, offvalue=0, command=click)
chkRojo.grid(column=1, row=2)
chkAzul = Checkbutton(frame, text="Azul", variable=color02,
                      onvalue=1, offvalue=0, command=click)
chkAzul.grid(column=1, row=3)
chkAmarillo = Checkbutton(frame, text="Amarillo", variable=color03,
                          onvalue=1, offvalue=0, command=click)
chkAmarillo.grid(column=1, row=4)

etiqueta = Label(frame, text="Selecciona opcion")
etiqueta.grid(column=1, row=6)
ventana.mainloop()
