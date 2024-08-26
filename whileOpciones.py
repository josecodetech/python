print("""Menu
1. Entrar
2. Salir""")
opcion=int(input())
while True:
	if opcion==1:
		print('hola, estamos dentro')	
	elif opcion==2:
		print('sales, hasta pronto')
		break
	else:
		print('marca opcion valida')
	print("""Menu
1. Entrar
2. Salir""")
	opcion=int(input())