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
    fecha=str(di)+"/"+str(me)+"/"+str(an)
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
    fecha=str(di)+"/"+str(me)+"/"+str(an)

    parametros=(fecha,efectivo,totalVenta,base,iva,tarjetas)
    sql="INSERT INTO TOTALES VALUES (NULL, ?, ?, ?, ?, ?, ?)"
    #print(sql)
    cursor.execute(sql,parametros)
    con.commit()
    con.close()

if __name__=='__main__':
     creaBaseVentas()
     creaBaseTotales()            
     insertaBaseVentas(1,10,21,"TIENDA 01",1500,150.2,123.23)
     insertaBaseVentas(1,10,21,"TIENDA 02",1525,2500,1500)
     insertaBaseTotales(1,10,21,1525,2500,1500,150.2,123.23)
     insertaBaseTotales(1,10,21,1525,2500,1500,150.2,123.23)

