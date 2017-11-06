#TABLA DE MULTIPLICAR CON FOR
tablaDel=int(input("Que tabla quieres calcular? "))
print("Tabla del: ",tablaDel)
#BUCLE FOR, SE REPITE MIENTRAS CONTADOR MENOR QUE 11
for contador in range(1,11): #incremento con pasos (1,11,2)
    #CALCULAMOS EL RESULTADO
    multiplica=tablaDel*contador
    #MOSTRAMOS EN PANTALLA
    print(tablaDel," por ",contador," es igual a ",multiplica)
#SE MUESTRA AL SALIR DEL BUCLE, FINAL
print("Fin de la tabla")
