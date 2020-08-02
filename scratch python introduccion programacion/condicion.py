num1=int(input('Dime un numero : '))
num2=int(input('Dime otro numero : '))
if (num2!=0) or (num1>0):
    resultado = num1 / num2
    print('El resultado es : '+str(resultado))
else:
    print('No puedo realizar la division.')