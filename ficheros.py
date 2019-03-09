#Escribir
texto="Primera linea\nSegunda linea"
fichero=open('fichero.txt','w')
fichero.write(texto)
fichero.close()
#Leer
fichero=open('fichero.txt','r')
texto2=fichero.read()
fichero.close()
print(texto2)