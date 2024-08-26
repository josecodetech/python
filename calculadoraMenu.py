def menu():
    print('\nOpciones\n')
    print('1. Suma')
    print('2. Resta')
    print('3. Salir')
def suma(num1,num2):
    print('La suma es {}'.format(num1+num2))
def resta(num1,num2):
    print('La resta es {}'.format(num1-num2))
while True:
    menu()
    opcion=int(input())
    if opcion==3:
        exit()
    elif opcion==1:
        num1=int(input('Primer numero = '))
        num2=int(input('Segundo numero = '))
        suma(num1,num2)
    elif opcion==2:
        num1=int(input('Primer numero = '))
        num2=int(input('Segundo numero = '))
        resta(num1,num2)
    else:
        print('opcion invalida')