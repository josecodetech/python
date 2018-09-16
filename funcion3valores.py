#funcion q devuelve 3 valores
#tipo json
def creaUsuario(nombre,apellido,edad):
	return{
	'nombre completo': "{}{}".format(nombre,apellido),
	'edad':edad
	}
rdo=creaUsuario('Jose','Ojeda',46)
print(rdo)