#Captura error
def divide(num1,num2):
    try:

       print (num1 / num2)

       print("division resuelta")

    except ZeroDivisionError:

       print("error al dividir por cero")
    finally:
        print('esto se ejecuta pase lo que pase')

divide(9,0)
divide(9,3)