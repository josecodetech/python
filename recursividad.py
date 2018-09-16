#factorial
def factorial(x):
	if x==1:
		return 1
	else:
		return x*factorial(x-1)
while True:
	num=int(input('Dime un numero (0 sale)'))
	if num==0:
		break;
	print(factorial(num))
	
	