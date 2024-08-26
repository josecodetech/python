import ejercicio20BaseDatos02 as db


def menu():
    print("*"*48)
    print("""
          1. Insertar 
          2. Consultar
          3. Modificar
          4. Borrar
          5. Salir
          """)
    print("*"*48)
    opcion = int(input())
    return opcion


while True:
    opcion = menu()
    if opcion == 1:
        nombre = input("Dime el nombre a insertar : ")
        nota = int(input("Dime la nota que le corresponde : "))
        datos = (nombre, nota)
        db.insertar(datos)
    elif opcion == 2:
        db.consultar()
    elif opcion == 3:
        identificador = int(input("Dime el identificador : "))
        nota = int(input("Dime la nota a modificar : "))
        #datos = (identificador, nota)
        db.modificar(identificador, nota)
    elif opcion == 4:
        identificador = int(input("Dime el identificador : "))
        db.borrar(identificador)
    elif opcion == 5:
        print("Hasta pronto!!!")
        break
    else:
        print("Indica una opcion correcta \n")
