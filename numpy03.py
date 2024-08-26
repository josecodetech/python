# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 08:55:45 2019

@author: Jose
"""

import numpy as np
lista=[1,2,4,5,3,8,72,32,9,2,7]
a=np.array(lista)
multiplicado=a*5
print(help(np.zeros))
b=np.arange(20).reshape(4,5)
print(b.shape)
print(b.ndim)
print(b.size)
print(len(b))
indices=[0,2,3]
print(a[indices])
ceros=np.zeros((4,5))
unos=np.ones((3,3))
unos=np.ones((4,5))
multiplica=ceros*unos
print(a.sum())
print(a.mean())
print(a.min())
print(a.max())
print(a[1:3])
c=a[:]
a=a*2
c=a[:].copy()
print(a)
print(c)
