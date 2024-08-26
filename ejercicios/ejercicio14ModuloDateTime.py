from datetime import datetime

actual = datetime.now().time()
print(actual)
hora_salida = 19
minuto_salida = 30
if (hora_salida == actual.hour) and (minuto_salida == actual.minute):
    print("Ya puedes salir")
elif ((hora_salida < actual.hour) and (minuto_salida < actual.minute)):
    print("Ya se ha pasado la hora, vete ya!!!")
else:
    faltan_horas = hora_salida - actual.hour
    faltan_minutos = minuto_salida - actual.minute
    if faltan_minutos < 0:
        faltan_horas = faltan_horas - 1
        faltan_minutos = (-1*faltan_minutos)+30
    print(f"Quedan {faltan_horas} horas y {faltan_minutos} minutos")
