#obtener datos del usuario
#devuelve una cadena y con strip eliminamos espacios 
#iniciales y finales
nombre = input('Dime tu nombre : ').strip()
#con int delante convertimos el string a entero
edad = int(input('Dime tu edad : '))
#mostramos lo obtenido en pantalla
#con str volvemos a convertir el entero en cadena
print("Hola, "+nombre+" tienes "+str(edad)+" años.")
#mostramos el tipo de cada variable
print(type(nombre))
print(type(edad))