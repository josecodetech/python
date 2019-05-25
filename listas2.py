#listas
l1=[1,2,3,4]
l2=[5,2,7,2,8]
#Inserta elemento en (pos, val)
l1.insert(1,10)
print(l1)
#Union listas
l1.extend(l2)
print(l1)
#Veces q aparece
print(l1.count(2))
#Posic donde aparece 10
print(l1.index(10))
#Añade al final 21
l1.append(21)
print(l1)
print(l2)
#Borra lista2
l2.clear()
print(l2)
#borra ultimo y el valor 5
l1.pop()
l1.remove(5)
#Da la vuelta a lista
l1.reverse()
print(l1)
#Ordena la lista
l1.sort()
print(l1)