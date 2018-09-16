#metdos de clases
class Coche:
	#constructor
	def __init__(self,marca,color):
		self.marca=marca
		self.color=color
	#metodo
	def arranca(self):
		print('En marcha '+self.marca)
#creamos clase deportivo que hereda de coche
class Deportivo(Coche):
	def puertas(self):
		print('tengo 2 puertas')
#instancia objeto
miCoche=Deportivo('peugeot','gris')
tuCoche=Coche('opel','rojo')
#mostramos caracteristicas
print(miCoche.marca)
print(tuCoche.color)
#arrancamos
miCoche.arranca()
tuCoche.arranca()
miCoche.puertas()
#lo siguiente da error pq no es deportivo
tuCoche.puertas()