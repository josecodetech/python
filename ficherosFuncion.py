#Escribir
def escribe(fichero,texto):
    fichero=open(fichero,'w')
    fichero.write(texto)
    fichero.close()
#Leer
def lee(fichero):
    fichero=open(fichero,'r')
    texto=fichero.read()
    fichero.close()
    return texto
escribe('fichero.txt','hola desde llamada funcion')
print(lee('fichero.txt'))