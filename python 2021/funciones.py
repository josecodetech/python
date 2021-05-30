def esPar(numero):
    if numero % 2 == 0:
        # print("El numero es par")
        return True
    else:
        # print("El numero es impar")
        return False


numero = int(input("Dime un numero y te indicare si es par o no "))
resultado = esPar(numero)
if resultado:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")
