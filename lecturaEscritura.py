#Escritura fichero
fichero= open("fichero.txt", "w")
fichero.write("Escribo este texto en el fichero")
fichero.close()
#lectura fichero
fichero = open("fichero.txt", "r")
print(fichero.read())
fichero.close()