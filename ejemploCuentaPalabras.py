def cuentaPalabras(texto):
    palabras = texto.split(" ")
    palabrasContadas = {}
    contador = 0
    longitud = len(palabras)
    for i in range(0, longitud):
        primera = palabras[i]
        # print(primera)
        for j in range(0, longitud):
            segunda = palabras[j]
            if primera == segunda:
                contador += 1  # contador = contador + 1
        palabrasContadas[primera] = contador
        contador = 0
    return palabrasContadas


try:
    fichero = open("ejemploCuentaPalabras.txt", "r", encoding='utf-8')
    texto = fichero.read()
    #print("Fichero correcto")
    # fichero.close()
except:
    print("No se ha podido leer el fichero")
finally:
    #print("Fichero cerrado")
    fichero.close()
#texto = input("Dime un texto para contar sus palabras repetidas : ")
#texto = "Esto es un texto de ejemplo donde veremos cuantas veces aparece cada palabra dentro de este texto palabra palabra texto dentro donde veremos"
cuentaPalabras = cuentaPalabras(texto)
print(cuentaPalabras)
