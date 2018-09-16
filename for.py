#tabla multiplicar
tabla=int(input('dime tabla del...'))
print('muestro la tabla del '+str(tabla))
#bucle repeticion
for i in range(1,11):
	mult=tabla*i
	print(str(tabla)+' por '+str(i)+'='+str(mult))
print('fin')