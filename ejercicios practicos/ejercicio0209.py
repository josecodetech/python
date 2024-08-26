def suma(lista):
    suma = 0
    for i in lista:
        suma += i
        #suma = suma + i
    return suma


def multiplica(lista):
    multiplicacion = 1
    for i in lista:
        multiplicacion *= i
    return multiplicacion


lista = [1, 32, 53, 65, 35, 1, 3, 4, 6, 9, 10, 11]
print(suma(lista))
print(multiplica(lista))
