from tkinter import *
from tkinter import messagebox
from modulos.archiva import *
from modulos.cesar import *


def codificar():
    texto = textoSinCodificar.get()
    if texto != "":
        textoCodificado.set(codifica(texto))
        mensaje("Info", "Texto codificado")
    else:
        mensaje("Error", "Error al codificar texto")


def descodificar():
    texto = textoCodificado.get()
    if texto != "":
        textoSinCodificar.set(descodifica(texto))
        mensaje("Info", "Texto descodificado")
    else:
        mensaje("Error", "Error al descodificar texto")


def cargar():
    try:
        textoCodificado.set(carga())
        descodificar()
    except:
        mensaje("Error", "Error al cargar el archivo")


def guardar():
    texto = textoCodificado.get()
    if texto != "":
        guarda(texto)
        mensaje("Info", "Mensaje guardado")
    else:
        mensaje("Error", "Error al guardar texto")


def borrar():
    textoCodificado.set("")
    textoSinCodificar.set("")


def mensaje(titulo, texto):
    messagebox.showinfo(titulo, texto)


ventana = Tk()
ventana.title("Codifica")
ventana.config(bg="gray")
ventana.geometry("380x380")
frame = Frame()
frame.config(width=340, height=340)
frame.config(bg="cyan")
frame.pack()
textoSinCodificar = StringVar()
textoCodificado = StringVar()
etiquetaSinCodificar = Label(
    frame, text="Texto sin codificar").grid(row=3, column=1)
cajaSin = Entry(frame, textvariable=textoSinCodificar).grid(row=3, column=2)
etiquetaCodificada = Label(
    frame, text="Texto codificado").grid(row=4, column=1)
cajaCod = Entry(frame, textvariable=textoCodificado).grid(row=4, column=2)
botonCodificar = Button(frame, text="Codificar",
                        command=codificar).grid(row=5, column=1)
botonDescodificar = Button(frame, text="Descodificar",
                           command=descodificar).grid(row=5, column=2)
botonGrabar = Button(frame, text="Grabar",
                     command=guardar).grid(row=6, column=1)
botonCargar = Button(frame, text="Cargar",
                     command=cargar).grid(row=6, column=2)
botonBorrar = Button(frame, text="Borrar",
                     command=borrar).grid(row=7, column=1)
ventana.mainloop()
