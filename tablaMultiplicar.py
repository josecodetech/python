#Tabla multiplicar
tablaDel=int(input('Dime la tabla que quieres? '))
for num in range(1,11):
    print("{} × {} = {}".format(tablaDel,num,tablaDel*num))