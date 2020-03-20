# -*-coding:utf-8 -*-

import matplotlib.pyplot as plt

x=(4,8,13,15,23,24)
y=(50,62,84,80,35,43)
plt.plot(x,y,'b-.')
plt.ylabel('Etiqueta Y')
plt.xlabel('Etiqueta X')
plt.axis([5,30,50,100])
plt.title('Mi grafica')

#plt.scatter(x,y)
plt.show()
    