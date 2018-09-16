#map
#codigo sin map
num=[1,2,3,4,5]
resultado=[] #lista vacia
#recorremos lista
for valor in num:
    #añadimos a lista
    resultado.append(valor*2)
print (resultado)

#reducimos codigo con map
def resultado(valor):
    return valor*2
print(list(map(resultado,num)))

#reducimos mas con lambda
print(list(map((lambda valor:valor*2),num)))
