#leemos fichero txt
#podemos incluir ruta absoluta
#lo abrimos en modo escritura 'r''
fichero=open('fichero.txt','r')
contenido=fichero.read()
print(contenido)
#siempre cerrarlo al terminar operaciones
fichero.close()