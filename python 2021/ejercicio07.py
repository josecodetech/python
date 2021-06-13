contador = 1
sumaPares = 0
cuentaPares = 0
sumaImpares = 0
cuentaImpares = 0
while contador <= 50:
    print(contador)
    if contador % 2 == 0:
        sumaPares += contador
        cuentaPares += 1  # cuentaPares = cuentaPares + 1
    else:
        sumaImpares += contador
        cuentaImpares += 1
    contador += 1
print(f"La suma de los pares es {sumaPares}")
print(f"Tenemos {cuentaPares} pares")
print(f"La suma de los impares es {sumaImpares}")
print(f"Tenemos {cuentaImpares} impares")
