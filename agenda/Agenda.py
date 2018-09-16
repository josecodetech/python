#AGENDA PYTHON
#CON SQLITE
#IMPORTA MODULO
from tkinter import *
from BDatos import *
from tkinter import messagebox
#VARIABLES
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
#funcion pruebas
def mostrarMensaje():
    print("Pruebas")
#FUNCIONES
def mensaje(titulo,texto):
    messagebox.showinfo(titulo,texto)
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
    textLista.insert(INSERT,"id\tNombre\t\tApellidos\t\tTelefono\n")
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
        mensaje("Guardar","Faltan datos")
    else:
        limpiar()
        creaTabla()
        inserta(no,ap,tf,em)
        mensaje("Guardar","Datos guardados")
    listar()
def modificar():
    id=ID.get()
    no=nombre.get()
    ap=apellidos.get()
    tf=telefono.get()
    em=email.get()
    if((no=="")or(ap=="")or(id=="")):
        mensaje("Modificar","Faltan datos")
    else:
        try:
            limpiar()
            modifica(id,no,ap,tf,em)
            mensaje("Modificar","Contacto modificado")
            listar()
        except:
            mensaje("Modificar","Error al modificar")
def borrar():
    try:
        id=ID.get()    
        if(id==""):
            mensaje("Borrar","Debes insertar el codigo")
        else:
            borra(id)
            limpiar()
            listar()
            mensaje("Borrar","Mensaje borrado")
    except:
        mensaje("Error","Error al borrar, inserta codigo")
def buscar():
    id=ID.get()
    if (id==""):
        mensaje("Buscar","Inserta identificador")
    else:
        tupla=busca(id)
        nombre.set(tupla[0])
        apellidos.set(tupla[1])
        telefono.set(tupla[2])
        email.set(tupla[3])
        mensaje("Buscar","Contacto encontrado")
#VENTANA
ventana=Tk()
ventana.config(bg=colorVentana)
ventana.geometry(anchoAlto+posicionX+posicionY)
ventana.title("Agenda")
#Variables cajas
ID=IntVar()
nombre=StringVar()
apellidos=StringVar()
telefono=StringVar()
email=StringVar()
#Widgets
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
#Botones
botonAñadir=Button(ventana,text="Añadir",command=guardar).place(x=150,y=500)
botonBorrar=Button(ventana,text="Borrar",command=borrar).place(x=200,y=500)
botonBuscar=Button(ventana,text="Buscar",command=buscar).place(x=250,y=500)
botonModificar=Button(ventana,text="Modificar",command=modificar).place(x=300,y=500)
listar()
ventana.mainloop()
