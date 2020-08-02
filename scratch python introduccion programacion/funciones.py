num1 = int(input("Dime el primer numero : "))
num2 = int(input("Dime el siguiente numero : "))

def sumar(num1,num2):
    resultado = num1+num2
    return resultado

def mostrar(resultado):
    print("La suma es "+str(resultado))
    
resultado = sumar(num1,num2)
mostrar(resultado)

#mostrar(sumar(num1,num2))    

