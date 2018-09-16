#funcion sin conocer cantidad de parametros
#usamos *
def suma(*args):
	total=0
	#bucle recorre todos los parametros
	for valor in args:
		total+=valor
	return total
#llamada a funcion
print(suma(2,3))
print(suma(1,4,5,6,9,12,3,4))