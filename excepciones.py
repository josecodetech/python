#EXCEPCIONES
numero1=int(input("Primer numero :"))
numero2=int(input("Segundo numero :"))
#CONTROL DE EXCEPCION
try:
    resultado=numero1/numero2
    print("El resultado es = ",resultado)
except ZeroDivisionError: #podemos obviar la especificacion del error
    print("No se puede dividir por cero")
finally:
    #SE EJECUTA SIEMPRE
    print("Esto se ejecuta pase lo que pase")
    
