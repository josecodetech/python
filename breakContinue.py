#break y continue
titulo='curso de python'
#break finaliza el ciclo
for caracter in titulo:
	if caracter == 'p':
		break
	print(caracter)
#continue salta a siguiente
for caracter in titulo:
	if caracter =='y':
		continue
	print(caracter)
print('fin')