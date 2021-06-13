def menu():
    print("Selecciona la operacion (1,2,3,4)")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplica")
    print("4. Divide")
    opcion = int(input())
    return opcion


def dameResultado(seleccion):
    num1 = int(input("Dime el primer numero "))
    num2 = int(input("Dime el segundo numero "))
    if (seleccion == 1):
        resultado = num1 + num2
    elif (seleccion == 2):
        resultado = num1 - num2
    elif (seleccion == 3):
        resultado = num1 * num2
    elif (seleccion == 4):
        try:
            resultado = num1 / num2
        except:
            print("Error al dividir")
            resultado = 0
    else:
        print("Selecciona una opcion correcta")
    return resultado


continua = True
while continua:
    seleccion = menu()
    resultado = dameResultado(seleccion)
    print(f"El resultado es {resultado}")
    print("Quieres continuar (s/n)? ")
    respuesta = input()
    if (not respuesta == "s" or not respuesta == "S"):
        continua = True
    else:
        continua = False
        print("Fin del calculo")
