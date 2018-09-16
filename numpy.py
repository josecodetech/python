#libreria numpy
import numpy as np
num1=[2,3,6,2,7]
num2=[7,8,2,5,1]
npNum1=np.array(num1)
npNum2=np.array(num2)
rdo=npNum1*npNum2
print(rdo)
#comprobamos rdo mayor 14
print(rdo>14)
#prueba sin numpy, dara error
#mira el error que te da
rdo=num1*num2