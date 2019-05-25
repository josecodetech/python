#Listas
colores=['rojo','amarillo','verde','azul']
print(type(colores))
print(colores)
print(colores[2])
#añadir
colores.append('naranja')
colores.insert(0,'rosa')
print(colores)
#borrar
del colores[2]
colores.pop()
colores.remove('rosa')
print(colores)