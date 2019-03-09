#Num parametros indeterminados
def suma(*args):
	suma=0
	for arg in args:
		suma+=arg
	return suma
#Llama 2 veces a funcion con distintos parametros
print(suma(2,7))
print(suma(2,3,4,8,10))