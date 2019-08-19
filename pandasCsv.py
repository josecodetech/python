# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 08:18:00 2019

@author: Jose
"""
import pandas as pd

url='http://winterolympicsmedals.com/medals.csv'

datos=pd.read_csv(url,header=0,sep=',')
#print(datos.columns)
filtro=datos[['Year','Sport','Medal']]
#print(filtro)
print(datos.describe())

#print(datos)
#print(datos.index)
#print(datos.columns)
#print(datos.head(10))
#print(datos.tail(10))
#print(datos.describe())
#print(datos.info())

#print(datos.isna())
print(filtro)
filtro=filtro.drop('Sport',axis=1)
#print(filtro)
#print(filtro[10:30])
filtro=filtro['Year']==2006
print(filtro)