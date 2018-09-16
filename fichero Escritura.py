#escribe fichero txt
#podemos incluir ruta absoluta
#lo abrimos en modo escritura 'w'
fichero=open('fichero.txt','w')
fichero.write('primera escritura en fichero')
print('fichero creado')
#siempre cerrarlo al terminar operaciones
fichero.close()