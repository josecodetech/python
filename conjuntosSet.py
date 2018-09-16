#set, conjuntos
#no puede tener duplicados
numeros={1,2,3,4}
#imprime tipo
print(type(numeros))
#comprueba si existe
print(2 in numeros)
#añade, borra y cuenta
numeros.add(8)
numeros.remove(2)
print(numeros)
print(len(numeros))
#operaciones con 2 conjuntos
uno={1,2,3,4}
dos={4,5,6,7}
#union, el duplicado no entra
print(uno|dos)
#interseccion, solo el 4
print(uno&dos)
#simetrica
print(uno^dos)
