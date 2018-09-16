#ejecucion si se llama directamente, en caso de importarlo se ejecutara desde otro script
def funcion():
	print('esta es funcion de modulo')
#esto se ejecuta si se ejecuta directamente
if __name__=="__main__":
	print('se ejecuta como script')