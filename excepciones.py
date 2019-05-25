def divide(num1,num2):
	try:
		print('resultado')
		print(num1/num2)
	except ZeroDivisionError:
		print('no se puede dividir por 0')
	except Exception as e:
		print('error : ')
		print(type(e).__name__)
divide(9,0)
divide(6,'dfg#')
divide(4,2)