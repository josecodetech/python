# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 07:46:30 2019

@author: Jose
"""

import random
intentos=0
print('Hola, como te llamas? ')
nombre=input()
numeroMaquina=random.randint(1,20)
print(nombre+', voy a pensar un numero entre 1 y 20')
for intentos in range(9):
    print('Intentalo : ')
    numeroUsuario=int(input())
    if numeroUsuario<numeroMaquina:
        print('Tu numero es mas bajo')
    if numeroUsuario>numeroMaquina:
        print('Tu numero es mayor')
    if numeroUsuario==numeroMaquina:
        break
if numeroUsuario==numeroMaquina:
    print('Acertastes!!!')
    intentos=str(intentos+1)
    print('En '+intentos+' veces')
if numeroUsuario!=numeroMaquina:
    numeroMaquina=str(numeroMaquina)
    print('El numero pensado era '+numeroMaquina)