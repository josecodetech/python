#LISTAS
lista_compras=["pan","patatas","naranjas","kiwis"]
print(lista_compras)
print(type(lista_compras))
#PEDIDO
piezas_pan=5
precio=0.40
total=precio*piezas_pan
pedido1=[piezas_pan,precio,total]
pedido2=[2,0.4,0.80]
pedido3=[3,0.3,0.90]
pedidos=[pedido1,pedido2,pedido3]
print(pedidos)
#lista[inicio:fin:step]
print(pedido1[1:2])
#recorrer lista
lista=[1,2,3,4,5,6,7,8,9]
for elemento in lista:
    print("el numero es ",elemento)
#INSERTAR ELEMENTOS
lista.append(45)
print(lista)
lista.insert(1,99)
print(lista)
lista.pop()
print(lista)
lista.remove(1)
print(lista)
print(len(lista))

