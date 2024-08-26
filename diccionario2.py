#Diccionario
colores={'amarillo':'yellow','negro':'black','blanco':'white'}
print(colores['amarillo'])
print(colores.get('rojo','no existe'))
print(colores.keys())
print(colores.values())
print(colores.items())
for c,v in colores.items():
    print(c+' '+v)
#Borra por clave
colores.pop('amarillo','no existe')
print(colores)
#Borra todo
colores.clear()
print(colores)