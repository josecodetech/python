#Lista Funcion
#Valor menor y mayor
def ValorMenor(lista):
    menor=lista[0]
    for x in range(1,len(lista)):
        if lista[x]<menor:
            menor=lista[x]
    return menor
def ValorMayor(lista):
    mayor=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>mayor:
            mayor=lista[x]
    return mayor
#cargamos de valores una lista
datos=[1,4,2,7,89,34,25,100,6,8,98]
print("El valor mayor es : ",ValorMayor(datos))
print("El valor menor es : ",ValorMenor(datos))
