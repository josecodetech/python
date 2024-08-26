# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 08:18:00 2019

@author: Jose
"""
import pandas as pd

columnas=['Nombre','Edad','Codigo']
indice01=['Jose','Lucia','Mar']
indice02=['Juan','Eva','Maria']
datos01=pd.DataFrame([['Jose',47,1273],['Lucia',40,2363],['Mar',44,2834]],index=indice01,columns=columnas)
datos02=pd.DataFrame([['Juan',57,1273],['Eva',None,2363],['Maria',24,2834]],index=indice02,columns=columnas)
#print(datos01)
#print(datos02)
datos=pd.concat([datos01,datos02])
#print(datos)
datos=datos.drop('Nombre',axis=1)
#print(datos)
#print(datos.index)
#print(datos.columns)
#print(datos.head(2))
#print(datos.tail(2))
#print(datos.describe())
#print(datos.info())
#print(datos.isna())
print(datos['Edad'])
print(datos01.drop('Codigo',axis=1))
print(datos01.drop('Nombre',axis=1))
print(datos01.head())