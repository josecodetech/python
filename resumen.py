# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:39:27 2020

@author: Jose
"""

#tipos de datos
#bool int float str
# verdadero=True
# entero=56
# decimal=3.45
# cadena="hola2"
# print(type(verdadero))
# print(type(entero))
# print(type(decimal))
# print(type(cadena))
# print(verdadero)
# print(entero)
# print(decimal)
# print(cadena)

#>operadores numericos
# + - * / ** % //
# print(1+5)
# print(6-4)
# print(3*23)
# print(7/3)
# print(3**2)
# print(7%4)
# print(9//4)

#operadores de comparacion
# == != < > <= >=
# print(1==2)
# print(1!=0)
# print(1<2)
# print(1>3)
# print(1<=2)
# print(1>=3)

#operadores booleanos
# and or not
# print(1==0 and 1!=2)
# print(1<2 or 1>9)
# print( not 1==4 or 1<5)

#variables
# precio=20
# cantidad=3
# total=precio*cantidad
# print(total)

#strings o cadenas
# cadena1="hola "
# cadena2="usuario"
# print(cadena1+cadena2)
# print(len(cadena1))
# print(cadena2[2])
# print(cadena2[1:3])

#entrada y salida de datos
# nombre=input("Dime tu nombre : ").strip()
# edad=int(input("Dime tu edad : "))
# print("Hola "+nombre+ " tienes "+str(edad)+" años")

#decisiones
# n=int(input("Adivina mi numero : "))
# if n == 15:
#     print("Acertastes")
    
# elif n < 15:
#     print("El numero es menor")
# else:
#     print("Perdistes")

#bucles
# for n in range(10,51,5):
#     print(n)
# cadena="hola, mundo!!!"
# for caracter in cadena:
#     print(caracter)
# #bucle condicional
# nombre=input('Dime tu nombre : ')
# while nombre!="":
#     print("Hola, "+nombre)
#     nombre=input()
# print("salistes")

#funciones
# def suma(num1,num2):
#     total=num1+num2
#     print(total)
#     return total
# suma(1,56)
# total=suma(34,45)
# print(total*4)

#listas
lista=[]
print(lista)
lista=[1,2,3,4]
print(lista)
lista.append(5)
print(lista)
lista.pop()
print(lista)
lista.remove(2)
print(lista)

#diccionarios
meses={'ene':1,'feb':2,'mar':3}
print(meses)
print(meses['feb'])
meses['abr']=4
print(meses)
del meses['ene']
print(meses)
for clave, valor in meses.items():
    print(clave+" "+str(valor))


