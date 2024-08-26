# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:51:27 2018

@author: Jose
"""
import os
def archivaImprime(di,me,an,texto):
    #guarda texto en archivo con nombre fecha
    fecha=str(an)+str(me)+str(di)
    fecha=str(fecha+".txt")
    escritura=open(fecha,"w")
    escritura.write(texto)
    escritura.close()
    #imprime en impresora
    print(texto)
    os.startfile(fecha,"print")
    print("fichero grabado e imprimido")
    
#llamamos a la funcion
archivaImprime(12,10,18,"prueba de impresion")
