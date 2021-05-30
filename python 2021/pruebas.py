def menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Salir\n")
    opcion = int(input())
    return opcion


def operacion(operador, num1, num2):
    if operador == "suma":
        resultado = num1 + num2
    elif operador == "resta":
        resultado = num1 - num2
    elif operador == "multiplica":
        resultado = num1 * num2
    elif operador == "divide":
        if num1 == 0:
            print("No se puede dividir por 0")
            resultado = 0
        else:
            resultado = num1 / num2
    return resultado


def solicitaDatos():
    num1 = int(input("Dime el primer numero "))
    num2 = int(input("Dime el segundo numero "))
    return num1, num2


while True:
    opcion = menu()
    if opcion == 1:
        num1, num2 = solicitaDatos()
        print(f"El resultado de {num1} + {num2} es :")
        print(operacion("suma", num1, num2))
    elif opcion == 2:
        num1, num2 = solicitaDatos()
        print(f"El resultado de {num1} - {num2} es :")
        print(operacion("resta", num1, num2))
    elif opcion == 3:
        num1, num2 = solicitaDatos()
        print(f"El resultado de {num1} * {num2} es :")
        print(operacion("multiplica", num1, num2))
    elif opcion == 4:
        num1, num2 = solicitaDatos()
        print(f"El resultado de {num1} / {num2} es :")
        print(operacion("divide", num1, num2))
    elif opcion == 0:
        break
    else:
        print("Introduce opcion valida")
    print("\n")
print("Salimos")
