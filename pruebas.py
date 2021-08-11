import sqlite3
# forma parte de la libreria estandar de python no hace falta instalar
# comprobar browser sqlite


def conectar():
    conexion = sqlite3.connect("miBD.db")
    cursor = conexion.cursor()
    return conexion, cursor


def crearTabla(conexion, cursor):
    sql = """CREATE TABLE IF NOT EXISTS agenda(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nombre VARCHAR(20) NOT NULL,
        telefono VARCHAR(14) NOT NULL)"""
    if(cursor.execute(sql)):
        print("Tabla creada")
    else:
        print("No se pudo crear la tabla")
    conexion.close()


def insertar(conexion, cursor, datos):
    sql = """INSERT INTO agenda(nombre,telefono) VALUES (?,?)"""
    if(cursor.execute(sql, datos)):
        print("Datos guardados")
    else:
        print("No se pudieron guardar los datos")
    conexion.commit()
    conexion.close()


def modificar(conexion, cursor, id, telefono):
    cursor.execute("UPDATE agenda SET TELEFONO ="+telefono+" where ID="+id)
    cursor.close()
    conexion.commit()
    conexion.close()


def borrar(conexion, cursor, id):
    cursor.execute("DELETE from agenda where ID="+id)
    cursor.close()
    conexion.commit()
    conexion.close()


def consultar(conexion, cursor):
    cursor.execute("SELECT id,nombre,telefono from agenda")
    for fila in cursor:
        print("ID = ", fila[0])
        print("Nombre = ", fila[1])
        print("Telefono = ", fila[2], "\n")
    conexion.close()


conexion, cursor = conectar()
crearTabla(conexion, cursor)
conexion, cursor = conectar()
insertar(conexion, cursor, ("Jose", "646506422"))
conexion, cursor = conectar()
insertar(conexion, cursor, ("Jose2", "646506222"))
conexion, cursor = conectar()
insertar(conexion, cursor, ("Jose3", "645506422"))
conexion, cursor = conectar()
consultar(conexion, cursor)
conexion, cursor = conectar()
modificar(conexion, cursor, "6", "1000000")
conexion, cursor = conectar()
borrar(conexion, cursor, "3")
conexion, cursor = conectar()
consultar(conexion, cursor)
