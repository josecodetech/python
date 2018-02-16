#AGENDA PYTHON
#CON SQLITE
#IMPORTAMOS MODULO
from tkinter import *
from tkinter import messagebox
from BDatos import *
#Variables
listado=[]
ANCHO=560
ALTO=540
POSX=400
POSY=400
anchoAlto=(str(ANCHO)+"x"+str(ALTO))
posicionX="+"+str(POSX)
posicionY="+"+str(POSY)
colorVentana="blue"
colorFondo="blue"
colorLetra="white"
#FUNCIONES
def limpiar():
        ID.set("")
        nombre.set("")
        apellidos.set("")
        telefono.set("")
        email.set("")    
def guardar():
    no=nombre.get()
    ap=apellidos.get()
    tf=telefono.get()
    em=email.get()
    if((no=="")or(ap=="")):
        mensaje("Guardar","faltan datos")
    else:
        limpiar()
        creaTabla()
        inserta(no,ap,tf,em)
        mensaje("Guardar","contacto guardado")
        listar()
def modificar():
    id=ID.get()
    no=nombre.get()
    ap=apellidos.get()
    tf=telefono.get()
    em=email.get()
    if((no=="")or(ap=="")):
        mensaje("Modificar","faltan datos")
    else:
        try:
            limpiar()
            modifica(id,no,ap,tf,em)
            mensaje("Modificar","contacto modificado")
            listar()
        except:
            mensaje("Modificar","error al modificar")
def borrar():
    id=ID.get()
    if(id==""):
        mensaje("Borrar","inserta codigo")
    else:
        borra(id)
        limpiar()
        mensaje("Borrar","contacto borrado")
        listar() 
def buscar():
    id=ID.get()         
    if(id==""):
        mensaje("Buscar","inserta codigo")
    else:
        try:
                tupla=busca(id)
                nombre.set(tupla[0])
                apellidos.set(tupla[1])
                telefono.set(tupla[2])
                email.set(tupla[3])
                mensaje("Buscar","contacto encontrado")
                listar()
        except:
                mensaje("Buscar","error al buscar")                     
def listar():
        if(len(listado)>0):            
                #borra lista
                listado.clear()

        conexion=sqlite3.connect("agenda.db")
        consulta=conexion.cursor()
        consulta.execute("SELECT id,nombre,apellidos,telefono,email from agenda")
        for i in consulta:
                id=(i[0])
                nombre=(i[1])
                apellidos=(i[2])
                telefono=(i[3])
                email=(i[4])
                listado.append(i)
                listado.sort()
        conexion.close()
        try:
                textLista.delete(1.0,END)
        except:
                mensaje("Listado","error en listado")
        textLista.insert(INSERT,"Id\tNombre\t\tApellidos\t\ttelefono\n")
        for elemento in listado:
               id=elemento[0]
               nombre=elemento[1]
               apellidos=elemento[2]
               telefono=elemento[3]
               textLista.insert(INSERT,id)
               textLista.insert(INSERT,"\t")
               textLista.insert(INSERT,nombre)
               textLista.insert(INSERT,"\t")
               textLista.insert(INSERT,"\t")
               textLista.insert(INSERT,apellidos)
               textLista.insert(INSERT,"\t")
               textLista.insert(INSERT,"\t")
               textLista.insert(INSERT,telefono)
               textLista.insert(INSERT,"\t")
               textLista.insert(INSERT,"\n")
def mensaje(titulo,texto):
        messagebox.showinfo(titulo,texto)        
#Ventana
ventana=Tk()
ventana.config(bg=colorVentana)
ventana.geometry(anchoAlto+posicionX+posicionY)#ancho alto pos x pos y
ventana.title("Ventana de Python")
#variables cajas textos
ID=IntVar()
nombre=StringVar()
apellidos=StringVar()
telefono=StringVar()
email=StringVar()
#Etiqueta
etiquetaID=Label(ventana,text="ID:").place(x=50,y=50)
cajaID=Entry(ventana,textvariable=ID).place(x=130,y=50)
etiquetaNombre=Label(ventana,text="Nombre:").place(x=50,y=90)
cajaNombre=Entry(ventana,textvariable=nombre).place(x=130,y=90)
etiquetaApellidos=Label(ventana,text="Apellidos:").place(x=50,y=130)
cajaApellidos=Entry(ventana,textvariable=apellidos).place(x=130,y=130)
etiquetaTelefono=Label(ventana,text="Telefono:").place(x=50,y=170)
cajaTelefono=Entry(ventana,textvariable=telefono).place(x=130,y=170)
etiquetaEmail=Label(ventana,text="Email:").place(x=50,y=210)
cajaEmail=Entry(ventana,textvariable=email).place(x=130,y=210)
textLista=Text(ventana)
textLista.place(x=50,y=240,width=400,height=200)
#Boton
botonAñadir=Button(ventana,text="Añadir",command=guardar).place(x=150,y=500)
botonBorrar=Button(ventana,text="Borrar",command=borrar).place(x=200,y=500)
botonBuscar=Button(ventana,text="Buscar",command=buscar).place(x=250,y=500)
botonModificar=Button(ventana,text="Modificar",command=modificar).place(x=300,y=500)
#Listamos en caso de tener registros
listar()
ventana.mainloop()
