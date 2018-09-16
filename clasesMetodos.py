#metdos de clases
class Coche:
	#constructor
	def __init__(self,marca,color):
		self.marca=marca
		self.color=color
	#metodo
	def arranca(self):
		print('En marcha '+self.marca)
#instancia objeto
miCoche=Coche('peugeot','gris')
tuCoche=Coche('opel','rojo')
#mostramos caracteristicas
print(miCoche.marca)
print(tuCoche.color)
#arrancamos
miCoche.arranca()
tuCoche.arranca()