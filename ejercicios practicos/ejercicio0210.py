def cadenaReves(palabra):
    alReves = ""
    contador = len(palabra)
    indice = -1
    while contador >= 1:
        alReves += palabra[indice]
        indice = indice + (-1)
        contador -= 1
        #contador = contador - 1
    return alReves


print(cadenaReves("Derecho"))
