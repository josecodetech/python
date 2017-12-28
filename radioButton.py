#RadioButton
from tkinter import *
def operacion():
    numero=num.get()
    if opcion.get()==1:
        total=numero*numero
    else:
        total=numero*numero*numero
    print("El resultado es: "+str(total))

ventana=Tk()
ventana.geometry("400x400")
ventana.title("Calcula cubo o cuadrado")
#variables
opcion=IntVar()
num=IntVar()

#elementos
etiqueta1=Label(ventana,text="Escribe el numero: ").place(x=20,y=20)
cajaNumero=Entry(ventana,textvariable=num).place(x=130,y=20)
etiqueta2=Label(ventana,text="Marca la opcion ").place(x=20,y=50)
cuadrado=Radiobutton(ventana,text="x2",value=1,variable=opcion).place(x=20,y=80)
cubo=Radiobutton(ventana,text="x3",value=2,variable=opcion).place(x=70,y=80)
boton=Button(ventana,text="Ver",command=operacion).place(x=20,y=120)
ventana.mainloop()
