import sqlite3


def conectar():
    conexion = sqlite3.connect("datos.db")
    cursor = conexion.cursor()
    return conexion, cursor


def crearTabla():
    conexion, cursor = conectar()
    sql = """
        CREATE TABLE IF NOT EXISTS alumnos(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre VARCHAR(25) NOT NULL,
            nota INTEGER NOT NULL
        )
    """
    if(cursor.execute(sql)):
        print("Tabla creada")
    else:
        print("No se pudo crear la tabla o ya estaba creada")
    conexion.close()


def insertar(datos):
    conexion, cursor = conectar()
    sql = """
        INSERT INTO alumnos(nombre, nota) VALUES(?,?)
    """
    if(cursor.execute(sql, datos)):
        print("Datos guardados")
        print("*"*25)
    else:
        print("No se pudieron guardar los datos")
    conexion.commit()
    conexion.close()


def consultar():
    conexion, cursor = conectar()
    sql = """SELECT id, nombre, nota from alumnos"""
    cursor.execute(sql)
    for fila in cursor:
        print("ID = ", fila[0])
        print("Nombre = ", fila[1])
        print("Nota = ", fila[2], "\n")
    conexion.close()


if __name__ == "__main__":
    crearTabla()
    for i in range(3):
        nombre = input("Dime el nombre del alumno : ")
        nota = input("Dime la nota que saco el alumno : ")
        datos = nombre, nota
        insertar(datos)
    consultar()
