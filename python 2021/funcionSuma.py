def suma(num1, num2):
    resultado = num1 + num2
    return resultado


num1 = int(input("Dime el primer numero "))
num2 = int(input("Dime el segundo numero "))
# llamada a la funcion
resultado = suma(num1, num2)
# mostramos resultado
print(f"La suma es igual a {resultado}")
