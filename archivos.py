# guardar datos en archivo
# abrimos el archivo
escritura = open("archivo.txt", "w")
escritura.write(
    "Esto se escribe en el archivo \ny esto en la linea siguiente \n\t\t\tY esto en otra linea tabulado")
escritura.close()

# lectura de fichero
lectura = open("archivo.txt", "r")
# leemos una linea
leeLinea = lectura.readline()
print("Leyendo una linea \n"+leeLinea)
lectura.close()
# leemos todo el fichero
lectura = open("archivo.txt", "r")
# podemos usar readlines, que devuelve una lista con cada linea
leeTodo = lectura.read()
# print(type(leeTodo))
print("leemos todo \n"+leeTodo)
lectura.close()
