n1 = 1
cuenta = 0
maximo = int(input("Numero maximo ? "))
suma = 0
while True:
    if((3*n1) > maximo):
        break
    if((3*n1) % 2 == 0):
        print(3*n1)
        cuenta = cuenta + 1
        suma = suma + (3*n1)
    n1 = n1 + 1
print(f"Hay {cuenta} multiplos de 3 y 2")
print(f"La suma es {suma}")
