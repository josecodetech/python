def mayor(num1, num2):
    if num1 < num2:
        return num2
    elif num1 > num2:
        return num1
    else:
        return False


elMayor = mayor(4, 54)
if(elMayor == False):
    print("Los numeros son iguales")
else:
    print(f"El mayor es el {elMayor}")
