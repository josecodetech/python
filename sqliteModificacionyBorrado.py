#SQLITE
import sqlite3



#CONECTAMOS
conexion=sqlite3.connect("agenda.db")
#CURSOR
consulta=conexion.cursor()
#MODIFICACION DE DATOS
consulta.execute("UPDATE agenda SET TELEFONO = 38874997 where ID= 2")
consulta.close()
conexion.commit()
conexion.close()
#CONECTAMOS
conexion=sqlite3.connect("agenda.db")
#CURSOR
consulta=conexion.cursor()
#BORRADO DE DATOS
consulta.execute("DELETE from agenda where ID= 2")
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
