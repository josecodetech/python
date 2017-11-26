#SQLITE
import sqlite3
#CONEXION
conexion=sqlite3.connect("agenda.db")
#CURSOR
consulta=conexion.cursor()
#CREA TABLA
sql="""
CREATE TABLE IF NOT EXISTS agenda(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
nombre VARCHAR(20) NOT NULL,
apellidos VARCHAR(20) NOT NULL,
telefono VARCHAR(14) NOT NULL
)
"""
#EJECUTAR CONSULTA
if(consulta.execute(sql)):
    print("Tabla creada")
else:
    print("Error al crear tabla")
#CERRAMOS
consulta.close()
conexion.commit()
conexion.close()

#INSERTAR DATOS
nombre=input("Dime el nombre\n")
apellidos= input("Dime el apellido\n")
telefono=input("Dime el telefono\n")
#CONECTAMOS
conexion=sqlite3.connect("agenda.db")
#CURSOR
consulta=conexion.cursor()
#DATOS
datos=(nombre,apellidos,telefono)
sql="""
INSERT INTO agenda(nombre,apellidos,telefono) VALUES (?,?,?)"""
if(consulta.execute(sql,datos)):
    print("datos guardados")
else:
    print("error al guardar datos")
consulta.close()
conexion.commit()
conexion.close()
