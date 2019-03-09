# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 08:27:06 2019

@author: Jose
"""
def cuentaAtras(num):
    if num>0:
        print(num)
        num-=1
        cuentaAtras(num)
    else:
        print("fin de la cuenta atras")
cuentaAtras(20)
