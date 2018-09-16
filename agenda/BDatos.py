#SQLITE
import sqlite3
from tkinter import messagebox
#CREA TABLA
def creaTabla():
    conexion=sqlite3.connect("agenda.db")
    consulta=conexion.cursor()
    sql="""CREATE TABLE IF NOT EXISTS agenda(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
 nombre VARCHAR(20) NOT NULL, apellidos VARCHAR(20) NOT NULL, telefono VARCHAR(14) NOT NULL,
 email VARCHAR(20) NOT NULL)"""
    if(consulta.execute(sql)):
        print("Tabla creada")
    else:
        print("No se pudo crear la tabla")
    conexion.close()
#INSERTAR DATOS
def inserta(nombre,apellidos,telefono,email):
    conexion=sqlite3.connect("agenda.db")
    consulta=conexion.cursor()
    datos=(nombre,apellidos,telefono,email)
    sql="""INSERT INTO agenda(nombre,apellidos,telefono,email) VALUES (?,?,?,?)"""
    if(consulta.execute(sql,datos)):
         print("Datos guardados")
    else:
        print("No se pudo guardar el dato")
    conexion.commit()
    conexion.close()
def modifica(id,nombre,apellidos,telefono,email):
    conexion=sqlite3.connect("agenda.db")
    consulta=conexion.cursor()
    consulta.execute("""UPDATE agenda SET nombre = ?,apellidos = ?,
telefono = ?,email = ? WHERE id= ?""",(nombre,apellidos,telefono,email, str(id)))
    consulta.close()
    conexion.commit()
    conexion.close()
#BORRAR DATOS
def borra(id):
    conexion=sqlite3.connect("agenda.db")
    consulta=conexion.cursor()
    consulta.execute("DELETE from agenda WHERE id="+str(id))
    consulta.close()
    conexion.commit()
    conexion.close()
#BUSCAR DATOS
def busca(id):
    conexion=sqlite3.connect("agenda.db")
    consulta=conexion.cursor()
    try:
        consulta.execute("SELECT * FROM agenda WHERE id="+str(id))
        for i in consulta:
            nombre=i[1]
            apellidos=i[2]
            telefono=i[3]
            email=i[4]
            return (nombre,apellidos,telefono,email)
        conexion.commit()
        conexion.close()
    except:
        messagebox.shorinfo("Buscar","Error al buscar")

    
