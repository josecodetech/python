# -*-coding:utf-8 -*-

"""
Created on Fri Dic 06 07:48:08 2019

@author: Jose
"""
import random

intentos=0
print("Hola, ¿como te llamas?")
nombre=input()

numero=random.randint(1,50)
print(nombre+" estoy pensando un numero entre 1 y 50")

while intentos<5:
    print("Adivinalo")
    numeroUsuario=int(input())
    intentos=intentos+1
    if numeroUsuario<numero:
        print("Tu numero es mas bajo")
    if numeroUsuario>numero:
        print("Tu numero es mayor")
    if numeroUsuario==numero:
        intentos=str(intentos)
        print("Buen trabajo, "+nombre+" lo has conseguido en "+intentos+" intentos")
        break
if numeroUsuario!=numero:
    numero=str(numero)
    print("Fallastes, el numero pensado era el "+numero)
    
        
    