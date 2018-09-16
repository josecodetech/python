#depuracion
def comprueba(mensaje):
    while True:
        try:
            dato=float(input("Dame el "+mensaje))
            return dato
        except ValueError:
            print("Dato entero o decimal")
numero1=comprueba("primer numero ")
numero2=comprueba("segundo numero ")
resultado=numero1+numero2
print("El resultado es "+str(resultado))
