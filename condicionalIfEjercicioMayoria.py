edad = int(input("Dime tu edad : "))
if 0 < edad < 18:
    print("No puedes continuar")
elif edad <= 0:
    print("No puedes tener esa edad")
else:
    print("Puedes continuar")
print("Ya hemos evaluado la condicion\nHemos terminado")
