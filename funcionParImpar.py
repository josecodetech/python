#FUNCION PAR IMPAR
def es_par(numero):
    if numero%2==0:
        return True
    else:
        return False
#PEDIMOS NUMERO AL USUARIO
numero=int(input("Dime un numero y te dire si es par o no : "))
if(es_par(numero)==True):
    print("El numero es par")
else:
    print("El numero es impar")
parImpar=es_par(numero)
print("El resultado devuelto a la variable parImpar es = ",parImpar)
