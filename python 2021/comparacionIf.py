numero1 = int(input("Dime el primer numero "))
numero2 = int(input("Dime el segundo numero y te indico cual es mayor "))

if (numero1 > numero2):
    print(f"El numero {numero1} es mayor que el numero {numero2}")
elif(numero1 < numero2):
    print(f"El numero {numero1} es menor que el numero {numero2}")
else:
    print("Los dos numeros son iguales")

print("Hemos terminado de comparar")

# segundo ejemplo, edades para tarifa

edad = int(input("Dime tu edad y te indico tu tarifa "))
if edad < 5:
    precio = 0
elif edad < 15:
    precio = 5
elif edad < 65:
    precio = 20
else:
    precio = 15
print("Tu tarifa para entrar es de "+str(precio))
