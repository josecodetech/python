# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 11:11:45 2019

@author: Jose
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datos=pd.DataFrame(np.random.randint(200,size=(50,4)),columns=['a','b','c','d'])
print(datos.head(5))
#histograma
#datos['a'].hist()
#datos['c'].hist()
#area
#datos[['c','d']].plot.area()
#barras
#datos.plot.bar(stacked=True)
#scatter
#datos.plot.scatter(x='a',y='b',c='c',cmap='coolwarm')
#caja
#datos.plot.box()
#densidad
#datos.plot.density()
#con matplotlib
x=datos['a']
y=datos['d']
plt.plot(x,y,'green')
plt.title("Grafico")
plt.xlabel("eje X")
plt.ylabel("eje Y")
figura=plt.figure(figsize=(10,3))
grafico=figura.add_axes([0.1,0.1,0.9,0.9])
grafico.plot(x,y,color='r',linewidth=10,alpha=1,linestyle='-')
plt.show()