import os
#instala paquetes o librerias
paquete=input('Que paquete instalamos? ')
paquete=str(paquete)
while True:
    try:
        codigo='pip install '+paquete
        os.system(codigo)
        print('Paquete instalado')
    except:
        print('Error al instalar paquete')
    continuar=input('Quieres instalar otro? ')
    continuar=str(continuar)
    if continuar=='S' or continuar=='s' or continuar=='si' or continuar=='SI':
        paquete=input('Que paquete instalamos? ')
        paquete=str(paquete)
    else:
        break
print('Fin')