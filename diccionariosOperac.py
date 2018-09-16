#diccionario
#almacena pares clave:valor
edad={'Jose':46,'Mar':43,'Javi':44,'Eli':42}
#devuelve valor
rdo=edad.get('Jose')
print(rdo)
#si no existe muestra mensaje
rdo=edad.get('Antonio','No existe')
print(rdo)
#pone valor por defecto
rdo=edad.setdefault('Dani',40)
print(rdo)
#devuelve las claves
rdo=edad.keys()
print(rdo)
#nos da clave valor
rdo=edad.items()
print(rdo)
#longitud
print(len(edad))
#elimina
del edad['Dani']
#esta tb elimina
edad.pop('Eli')
#este borra todo
edad.clear()