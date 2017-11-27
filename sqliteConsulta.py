#SQLITE
import sqlite3


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
#CONSULTA DE DATOS INSERTADOS
conexion=sqlite3.connect("agenda.db")
consulta=conexion.cursor()
consulta.execute("SELECT id,nombre,apellidos,telefono from agenda")
for i in consulta:
    print("ID= ", i[0])
    print("NOMBRE= ", i[1])
    print("APELLIDOS= ", i[2])
    print("TELEFONO= ", i[3],"\n")
conexion.close()
