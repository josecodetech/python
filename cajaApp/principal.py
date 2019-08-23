#archivo principal ejecucion
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
import time
from archiva import *
from baseDatos import *

class Ventana():
    colorFondo="#007"
    colorLetra="#FFF"

    #constructor
    def __init__(self):
        #pass
		#creacion ventana              
        ANCHO=360
        ALTO=300
        global colorFondo
        global colorLetra
        self.tituloVentana="Cajas"
        self.anchoAlto=str(ANCHO)+"x"+str(ALTO)
        self.ventana=Tk()
        self.ventana.geometry(self.anchoAlto)
        self.ventana.title(self.tituloVentana)		
        self.ventana.configure(background=self.colorFondo)
        #COMPONENTES VENTANA Y VARIABLES
        self.componentes(self.ventana)       
        #borrado o inicio
        self.borrar()
        self.dameFechaAnterior()
        #ejecucion ventana
        self.ventana.mainloop()
    #metodos clase

    def componentes(self,ventana):
        global colorFondo
        global colorLetra
        
        self.efectivoTi01=DoubleVar(value='0.0')
        #damos valor
        #efectivoTi01.set(25.0)
        #efectivoTi01.set(0.0)
        self.tarjetasTi01=DoubleVar(value='0.0')
        self.efectivoTi02=DoubleVar(value='0.0')
        self.tarjetasTi02=DoubleVar(value='0.0')
        self.ventaTi01=DoubleVar(value='0.0')
        self.ventaTi02=DoubleVar(value='0.0')

        self.dia=StringVar(value='00')
        self.mes=StringVar(value='00')
        self.año=StringVar(value='00')
        #campo fecha
        etFecha=Label(self.ventana,text="Fecha (dd/mm/yy)",bg=self.colorFondo,fg=self.colorLetra).place(x=20,y=15)
        cjDia=Entry(self.ventana,textvariable=self.dia).place(x=140,y=15,width=20)
        cjMes=Entry(self.ventana,textvariable=self.mes).place(x=165,y=15,width=20)
        cjAño=Entry(self.ventana,textvariable=self.año).place(x=190,y=15,width=20)

        #tienda01
        etTienda01=Label(self.ventana,text="Tienda 01",bg=self.colorFondo,fg=self.colorLetra).place(x=90,y=40)
        etEfectivo01=Label(self.ventana,text="Efectivo",bg=self.colorFondo,fg=self.colorLetra).place(x=20,y=70)
        cjEfectivo01=Entry(self.ventana,textvariable=self.efectivoTi01).place(x=90,y=70,width=70)
        etTarjetas01=Label(self.ventana,text="Tarjetas",bg=self.colorFondo,fg=self.colorLetra).place(x=20,y=100)
        cjTarjetas01=Entry(self.ventana,textvariable=self.tarjetasTi01).place(x=90,y=100,width=70)
        #Total Tienda01
        etTotal01=Label(self.ventana,text="Total",bg=self.colorFondo,fg=self.colorLetra).place(x=20,y=130)
        cjTotal01=Entry(self.ventana,textvariable=self.ventaTi01).place(x=90,y=130,width=70)
        
        #tienda02
        etTienda02=Label(self.ventana,text="Tienda 02",bg=self.colorFondo,fg=self.colorLetra).place(x=190,y=40)
        cjEfectivo02=Entry(self.ventana,textvariable=self.efectivoTi02).place(x=190,y=70,width=70)
        cjTarjetas02=Entry(self.ventana,textvariable=self.tarjetasTi02).place(x=190,y=100,width=70)
        #Total Tienda01
        cjTotal02=Entry(self.ventana,textvariable=self.ventaTi02).place(x=190,y=130,width=70)
        
        botonGuardar=Button(self.ventana,text="Guardar",command=self.guardar,bg=self.colorFondo,fg=self.colorLetra).place(x=110,y=165)
        botonBorrar=Button(self.ventana,text="Borrar",command=self.borrar,bg=self.colorFondo,fg=self.colorLetra).place(x=180,y=165)
        #Informes
        self.dia1=StringVar(value='00')
        self.mes1=StringVar(value='00')
        self.año1=StringVar(value='00')
        etInforme=Label(self.ventana,text="Ventas entre fechas indicadas",bg=self.colorFondo,fg=self.colorLetra).place(x=20,y=190)
        etFecha1=Label(self.ventana,text="Fecha inicial",bg=self.colorFondo,fg=self.colorLetra).place(x=20,y=220)
        cjDia1=Entry(self.ventana,textvariable=self.dia1).place(x=100,y=220,width=20)
        cjMes1=Entry(self.ventana,textvariable=self.mes1).place(x=130,y=220,width=20)
        cjAño1=Entry(self.ventana,textvariable=self.año1).place(x=160,y=220,width=20)        
        self.dia2=StringVar(value='00')
        self.mes2=StringVar(value='00')
        self.año2=StringVar(value='00')
        etFecha1=Label(self.ventana,text="Fecha final",bg=self.colorFondo,fg=self.colorLetra).place(x=20,y=250)
        cjDia1=Entry(self.ventana,textvariable=self.dia2).place(x=100,y=250,width=20)
        cjMes1=Entry(self.ventana,textvariable=self.mes2).place(x=130,y=250,width=20)
        cjAño1=Entry(self.ventana,textvariable=self.año2).place(x=160,y=250,width=20)       
        botonMostrar=Button(self.ventana,text="Mostrar",command=self.mostrar,bg=self.colorFondo,fg=self.colorLetra).place(x=200,y=230)
    def mostrar(self):
        self.di1=self.dia1.get()
        self.me1=self.mes1.get()
        self.an1=self.año1.get()
        self.di2=self.dia2.get()
        self.me2=self.mes2.get()
        self.an2=self.año2.get()
        #obtenemos venta total
        Total=ventaTotal(self.di1,self.me1,self.an1,self.di2,self.me2,self.an2)
        #venta por tienda
        Tiendas=ventaTienda(self.di1,self.me1,self.an1,self.di2,self.me2,self.an2)
        textoMensaje="La venta total es de "+str(Total)+"\n"
        textoMensaje=textoMensaje+"Tienda 01\tTienda 02\n"
        textoMensaje=textoMensaje+str(Tiendas['TIENDA 01'])+"\t\t"+str(Tiendas['TIENDA 02'])
        messagebox.showinfo("Ventas",textoMensaje)
    def guardar(self):
        print('guardado')
        #total venta y desglose iva
        self.totalEfectivo=round(float(self.efectivoTi01.get()+self.efectivoTi02.get()),2)
        self.totalTarjetas=round(float(self.tarjetasTi01.get()+self.tarjetasTi02.get()),2)
        self.venta01=round(float(self.efectivoTi01.get()+self.tarjetasTi01.get()),2)
        self.venta02=round(float(self.efectivoTi02.get()+self.tarjetasTi02.get()),2)
        self.ventaTi01.set(self.venta01)
        self.ventaTi02.set(self.venta02)
        
        self.totalVenta=round(float(self.totalEfectivo+self.totalTarjetas),2)
        self.iva=round(float(self.totalVenta)*(21/121),2)
        self.base=round(float(self.totalVenta)*(100/121),2)
        self.comisionBanco=round(float(self.totalTarjetas*(0.75/100)),2)
        
        #PREPARACION TEXTO A GUARDAR
        self.texto="\n"
        self.texto=self.texto+"Concepto\t\tTienda 01\tTienda 02\t\t\t\t\n\n"
        self.texto=self.texto+"Efec Ingreso\t\t"+str(round(self.totalEfectivo,2))+"\t\t\t\t\t\t\n\n"
        self.texto=self.texto+"Banco tarjetas\t\t"+str(self.tarjetasTi01.get())+"\t\t"+str(self.tarjetasTi02.get())+"\t\t\t\t\n\n"
        self.texto=self.texto+"Total Ventas\t\t"+str(self.venta01)+"\t\t"+str(self.venta02)+"\t\t\t\t\n\n\n\n"
        self.texto=self.texto+"\tBase Imponible = "+str(round(self.base,2))+"\tIVA = "+str(round(self.iva,2))+"\tTOTAL = "+str(round(self.totalVenta,2))+"\n\n"
        self.texto=self.texto+"\tcomis tarjetas = "+str(round(self.comisionBanco,2))+"\n\n"
        self.di=self.dia.get()
        self.me=self.mes.get()
        self.an=self.año.get()

        #archiva
        try:    
            archiva(self.di,self.me,self.an,self.texto)
        except:
            print("error al archivar")
        #imprime
        try:
            imprime(self.di,self.me,self.an)
        except:
            print("error al imprimir")
        #guarda en BD sqlite
        try:
            creaBaseVentas()
            creaBaseTotales()
            insertaBaseVentas(self.di,self.me,self.an,"TIENDA 01",self.ventaTi01.get(),self.efectivoTi01.get(),self.tarjetasTi01.get())
            insertaBaseVentas(self.di,self.me,self.an,"TIENDA 02",self.ventaTi02.get(),self.efectivoTi02.get(),self.tarjetasTi02.get())
            insertaBaseTotales(self.di,self.me,self.an,self.totalEfectivo,self.totalVenta,self.base,self.iva,self.totalTarjetas)
        except:
            print("error al guardar en BD")


    def borrar(self):
        #print('borrando')
        self.efectivoTi01.set(0.0)
        self.tarjetasTi01.set(0.0)
        self.efectivoTi02.set(0.0)
        self.tarjetasTi02.set(0.0)
        self.ventaTi01.set(0.0)
        self.ventaTi02.set(0.0)
        self.dameFechaAnterior()
    def dameFechaAnterior(self):
        #toma fecha dia anterior
        diaAct=time.strftime("%d")
        mesAct=time.strftime("%m")
        añoAct=time.strftime("%y")
        if int(diaAct)==1:
            diaAct=1
        else:
            diaAct=int(diaAct)-1
        if int(diaAct)<10:
            diaAct="0"+str(diaAct)
        self.año.set(añoAct)
        self.mes.set(mesAct)
        self.dia.set(str(diaAct))
        self.año1.set(añoAct)
        self.mes1.set(mesAct)
        self.dia1.set(str("01"))
        self.año2.set(añoAct)
        self.mes2.set(mesAct)
        self.dia2.set(str(diaAct))        
if __name__=='__main__':
    #pruebas
    #print('probando')
    ventana=Ventana()

