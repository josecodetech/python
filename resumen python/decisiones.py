#adivina numero
from random import randint
#numero aleatorio
numeroPensado = randint(1,3)
numeroUsuario = int(input("Que numero he pensado del 1 al 3?"))
if numeroUsuario == numeroPensado:
    print('Acertastes')
elif numeroUsuario < numeroPensado:
    print('El numero pensado es mayor')
else:
    print('El numero pensado es menor')

