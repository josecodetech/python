#reduce
#tenemos que importar functools para usar esta funcion
import functools
num=[1,2,3,4,5,6,7,8,9,10,11,12]
resultado=0
#sin reduce
#recorremos lista
for valor in num:
    resultado=resultado + valor
print(resultado)

#con reduce y lambda
print(str(functools.reduce((lambda x,resultado:x+resultado),num)))
