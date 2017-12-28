from tkinter import *
def mostrar():
    print("Hola: "+nombre.get()+" "+apellido.get()+" "+str(edad.get()))

ventana=Tk()
ventana.geometry("400x400")
ventana.title("Ficha datos")
#variables
nombre=StringVar()
apellido=StringVar()
edad=IntVar()
nombre.set("nombre")
#elementos
etiqueta1=Label(ventana,text="Escribe tu nombre: ").place(x=10,y=10)
nombreCaja=Entry(ventana,textvariable=nombre).place(x=170,y=10)
etiqueta2=Label(ventana,text="Escribe tu apellido: ").place(x=10,y=40)
apellidoCaja=Entry(ventana,textvariable=apellido).place(x=170,y=40)
etiqueta3=Label(ventana,text="Escribe tu edad: ").place(x=10,y=70)
edadCaja=Entry(ventana,textvariable=edad).place(x=170,y=70)
boton=Button(ventana,text="Mostrar",command=mostrar).place(x=10,y=140)
ventana.mainloop()
