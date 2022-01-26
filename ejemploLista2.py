def solicitar():
    lista = []
    num = None
    while num != 0:
        num = int(input("Dime un numero: (0 para terminar) "))
        if num > 0:
            lista.append(num)
        elif num == 0:
            break
        else:
            print("El numero debe ser mayor que 0")
    return lista


def ordenar(lista):
    lista.sort()
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares


# print(solicitar())
lista = solicitar()
print("Imprimimos la lista")
print(lista)
pares, impares = ordenar(lista)
print("Imprimimos la lista de numeros pares")
print(pares)
print("Imprimimos la lista de numeros impares")
print(impares)
