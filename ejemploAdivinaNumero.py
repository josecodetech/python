#adivina numero
from random import*
numPc=randint(1,100)
intento=0
fin=False
while not fin:
	intento=intento+1
	numUser=int(input('Dime un numero (1 a 100) '))
	if numUser==numPc:
		print('Adivinastes en ',intento,' intentos')
		fin=True
	else:
		if numUser<numPc:
			print('pense uno mayor')
		else:
			print('pense uno menor')