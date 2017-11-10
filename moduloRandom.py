from random import randint as azar
continua=input("Empezamos (s/n)? ")
while(continua=="s" or continua =="S"):
    lanzaDado=azar(1,6)
    print("Has sacado un "+str(lanzaDado))
    continua=input("Quieres continuar (s/n)? ")
print("Se acabo, adios")
