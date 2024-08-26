import pickle
#lista
colores=['rojo','amarillo','verde','azul','blanco','negro','naranja']
#escritura fichero
fichero=open('colorFich','wb')
pickle.dump(colores,fichero)
fichero.close()
print('Grabado')
#lectura fichero
fichero=open('colorFich','rb')
coloresLista=pickle.load(fichero)
fichero.close()
print(coloresLista)
print('lista recuperada')