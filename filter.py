#filter
num=[1,2,3,4,5,6,7,8,9,10,11,12]
pares=[] #lista vacia
#recorremos lista
for valor in num:
    if(valor%2==0):
        #añadimos a lista
        pares.append(valor)
print (pares)

#reducimos codigo con filter
def esPar(valor):
    return valor%2==0
print(list(filter(esPar,num)))

#reducimos mas con lambda
print(list(list(filter((lambda valor:valor%2==0),num))))
