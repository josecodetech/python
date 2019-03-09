import random
def azar():
	num=random.randint(1,100)
	return num
def dame():
	user=int(input('dame un numero '))
	return user
num=azar()
user=dame()
while True:
	if num==user:
		print('acertastes')
		break
	elif num<user:
		print('el mio es menor')
		user=dame()
	else:
		print('el mio es mayor')
		user=dame()
		