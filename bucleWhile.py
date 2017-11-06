#TABLAS DE MULTIPLICAR
tablaDel=int(input("Que tabla quieres que calcule ? "))
contador=1
print("Tabla del ",tablaDel)
#ENTRAMOS EN EL BUCLE
while(contador<11):
    multiplicacion=tablaDel*contador
    #MOSTRAMOS EL RESULTADO EN PANTALLA
    print(tablaDel," por ",contador," es igual a ",multiplicacion)
    #INCREMENTAMOS CONTADOR
    contador=contador+1
#SE MUESTRA AL SALIR DEL BUCLE
print("fin de la tabla")
