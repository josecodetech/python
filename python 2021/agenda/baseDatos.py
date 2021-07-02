import sqlite3


def conectar():
    conexion = sqlite3.connect("agenda.db")
    cursor = conexion.cursor()
    return conexion, cursor


def crearTabla():
    conexion, cursor = conectar()
    sql = """
        CREATE TABLE IF NOT EXISTS agenda(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre VARCHAR(20) NOT NULL,
            apellidos VARCHAR(20) NOT NULL,
            telefono VARCHAR(14) NOT NULL,
            email VARCHAR(20) NOT NULL
        )
    """
    if(cursor.execute(sql)):
        print("Tabla creada")
    else:
        print("No se pudo crear la tabla")
    conexion.close()


def insertar(datos):
    conexion, cursor = conectar()
    sql = """
    INSERT INTO agenda(nombre,apellidos,telefono,email) VALUES (?,?,?,?)
    """
    if(cursor.execute(sql, datos)):
        print("Datos guardados")
    else:
        print("No se pudieron guardar los datos")
    conexion.commit()
    conexion.close()


def consultar():
    conexion, cursor = conectar()
    sql = "SELECT id,nombre,apellidos,telefono,email from agenda"
    cursor.execute(sql)
    listado = []
    for fila in cursor:
        listado.append(fila)
        # print("ID = ", fila[0])
        # print("Nombre = ", fila[1])
        # print("Telefono = ", fila[2], "\n")
    listado.sort()
    conexion.close()
    return listado


def dameContacto(id):
    conexion, cursor = conectar()
    sql = "SELECT * from agenda where id="+str(id)
    cursor.execute(sql)
    contacto = cursor.fetchall()
    conexion.close()
    return contacto


def modificar(id, nombre, apellidos, telefono, email):
    conexion, cursor = conectar()
    sql = "UPDATE agenda SET nombre='"+nombre+"',apellidos='"+apellidos + \
        "', telefono='"+telefono+"', email='"+email+"' where ID="+str(id)
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()


def borrar(id):
    conexion, cursor = conectar()
    sql = "DELETE from agenda where ID="+str(id)
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()
