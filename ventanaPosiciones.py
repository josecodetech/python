from tkinter import *
def mostrar():
    print("Has pulsado el boton 2")
ventana=Tk()
ventana.geometry("400x360")
ventana.title("Titulo de ventana")

#creamos 2 botones
boton1=Button(ventana,text="Minimizar",fg="red",command=ventana.iconify)
#boton1.pack(side=LEFT)
boton1.place(x=34,y=45)
boton2=Button(ventana,text="Muestra",fg="blue",command=mostrar)
#boton2.pack(side=RIGHT)
boton2.place(x=45,y=70)
ventana.mainloop()
