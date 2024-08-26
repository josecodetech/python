meses={'ene':1, 'feb':2,'mar':3}
print('Muestra diccionario')
print(meses)
print('Mostramos Febrero')
print(meses['feb'])
#añadimos otro par clave valor
meses['abr']=4
print(meses)
#borramos un valor
del meses['ene']
print(meses)
print('Recorremos el diccionario')
for clave, valor in meses.items():
    print(clave+ " "+str(valor))