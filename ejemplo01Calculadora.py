#CALCULADORA
#FUNCION MENU
def menu():
    print("Selecciona la operacion (1,2,3,4)")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    opcion=int(input())
    return opcion
#FUNCION RESULTADO
def dameResultado(seleccion):
    operador1=int(input("Dime el primer numero "))
    operador2=int(input("Dime el segundo numero "))
    if(seleccion==1):
        resultado=operador1+operador2
    elif(seleccion==2):
        resultado=operador1-operador2
    elif(seleccion==3):
        resultado=operador1*operador2
    else:
        #CONTROLAMOS DIVISION POR CERO
        try:
            resultado=operador1/operador2
        except ZeroDivisionError: #podemos obviar la especificacion del error
            resultado=0
        #finally:  #podemos omitir el finally
            #este codigo se usaria pase lo que pase
    return resultado
#PROGRAMA PRINCIPAL
continua=True
while(continua):
    seleccion=menu()
    resultado=dameResultado(seleccion)
    print(str(resultado))
    print("Quieres continuar (s/n)? ")
    if(input()=="s" or input()=="S"):
        continua=True
    else:
        continua=False
        print("Fin del programa")

