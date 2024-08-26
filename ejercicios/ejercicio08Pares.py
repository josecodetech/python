inicio = int(input('Dime el numero inicial : '))
fin = int(input('Dime el numero final : '))
print('Te devuelvo los numeros pares en orden inverso\n')
for i in range(fin, inicio-1, -1):
    if i % 2 == 0:
        print(i)
