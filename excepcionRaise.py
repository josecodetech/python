#Creamos excepcion
num=float(input(':'))
if num==0:
    raise ValueError ('no puede ser 0')
else:
    print('no es cero')