#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3

def conecta():
    con=sqlite3.connect('ventas.sqlite')
    return con
def creaBaseVentas():
    con=conecta()        
    cursor=con.cursor()
    sql="""CREATE TABLE IF NOT EXISTS "VENTAS" (
	"ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"FECHA"	DATE NOT NULL,
	"TIENDA"	TEXT NOT NULL,
	"TOTAL"	REAL NOT NULL,
	"EFECTIVO"	REAL NOT NULL,
	"TARJETAS"	REAL NOT NULL
    )"""
    cursor.execute(sql)
    #print("tabla creada")
    con.close()
def creaBaseTotales():
    con=conecta()
    cursor=con.cursor()
    sql="""CREATE TABLE IF NOT EXISTS "TOTALES" (
	"ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"FECHA"	DATE NOT NULL,
	"EFECTIVO"	REAL NOT NULL,
	"TOTALVENTA"	REAL NOT NULL,
	"BASE"	REAL NOT NULL,
	"IVA"	REAL NOT NULL,
	"TARJETAS"	REAL NOT NULL
)"""
    cursor.execute(sql)
    #print("tabla creada")
    con.close()
def insertaBaseVentas(di,me,an,tienda,tVenta,tEfectivo,tTarjeta):    
    #conectar
    con=conecta()
    cursor=con.cursor()
    #fecha=str(di)+"/"+str(me)+"/"+str(an)
    fecha="20"+str(an)+"-"+str(me)+"-"+str(di)
    parametros=(fecha,tienda,tVenta,tEfectivo,tTarjeta)
    sql="INSERT INTO VENTAS VALUES (NULL, ?, ?, ?, ?, ?)"
    #print(sql)
    cursor.execute(sql,parametros)
    con.commit()
    con.close()
def insertaBaseTotales(di,me,an,efectivo,totalVenta,base,iva,tarjetas):
    #conectar
    con=conecta()
    cursor=con.cursor()
    fecha="20"+str(an)+"-"+str(me)+"-"+str(di)

    parametros=(fecha,efectivo,totalVenta,base,iva,tarjetas)
    sql="INSERT INTO TOTALES VALUES (NULL, ?, ?, ?, ?, ?, ?)"
    #print(sql)
    cursor.execute(sql,parametros)
    con.commit()
    con.close()
def ventaTotal(di1,me1,an1,di2,me2,an2):
    fechaIni="20"+str(an1)+"-"+str(me1)+"-"+str(di1)
    fechaFin="20"+str(an2)+"-"+str(me2)+"-"+str(di2)
    sql="SELECT SUM(totalVenta) as VentaTotal FROM totales WHERE (FECHA>=\""+fechaIni+"\") AND (FECHA<=\""+fechaFin+"\")"
    con=conecta()
    cursor=con.cursor()
    cursor.execute(sql)
    for i in cursor:
        ventaTotal=i[0]
    return ventaTotal
def ventaTienda(di1,me1,an1,di2,me2,an2):
    fechaIni="20"+str(an1)+"-"+str(me1)+"-"+str(di1)
    fechaFin="20"+str(an2)+"-"+str(me2)+"-"+str(di2)
    sql="SELECT tienda,SUM(total) as TotalVenta,tienda FROM ventas WHERE (FECHA>=\""+fechaIni+"\") AND (FECHA<=\""+fechaFin+"\") GROUP BY tienda"  
    con=conecta()
    cursor=con.cursor()
    #print(cursor)
    cursor.execute(sql)
    ventaTienda={}
    for i in cursor:
        ventaTienda[i[0]]=i[1]
    return ventaTienda
if __name__=='__main__':
    
     creaBaseVentas()
     creaBaseTotales()            
     insertaBaseVentas(1,11,19,"TIENDA 01",1500,150.2,123.23)
     insertaBaseVentas(1,11,19,"TIENDA 02",1525,2500,1500)
     insertaBaseTotales(1,11,19,1525,2500,1500,150.2,123.23)
     insertaBaseTotales(1,11,19,1525,2500,1500,150.2,123.23)
     print(ventaTienda(1,11,19,6,11,21))
