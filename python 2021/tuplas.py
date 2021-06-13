colores = ("verde", "amarillo", "rojo", "azul")
print(type(colores))
print(colores)
print(colores[:2])
tupla = ()
print(tupla)
print(type(tupla))

# print(colores[4]) #cuidado con indices inexistentes
# colores[2] = "rosa" #cuidado asignacion de valores

print(len(colores))
tuplaUnitaria = (50,)
print(type(tuplaUnitaria))
print(len(tuplaUnitaria))

# empaquetado de tuplas
a = 10
b = 'Jose'
c = 22.34
tupla = a, b, c
print(tupla)
print(type(tupla))

# desenpaquetado de tuplas
a, b, c = tupla
print(a)
print(b)
print(c)
