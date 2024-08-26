# -*-coding:utf-8 -*-

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
velocidad=[99,25,32,35,64,84,78,91,84,82,74,120,111,114,84,99,95,76,32,140,132,118,155,95]
media=np.mean(velocidad)
mediana=np.median(velocidad)
moda=stats.mode(velocidad)
desviacionEstandar=np.std(velocidad)
varianza=np.var(velocidad)
percentil=np.percentile(velocidad,25)
print("Los datos obtenidos son: ")
print("La media de los datos es : ",media)
print("La moda de los datos es : ",moda)
print("La mediana de los datos es : ",mediana)
print("La desviacion de los datos es : ",desviacionEstandar)
print("La varianza de los datos es : ",varianza)
print("El percentil de los datos es : ",percentil)
plt.hist(velocidad,7)
plt.show()
