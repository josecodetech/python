num=0
while num<20:
	print(num)
	if num==5:
		print('saltamos en ',num)
		num=num+1
		continue
	if num==7:
		print('rompemos en ',num)
		break
	num=num+1
print('se quedo en ',num)