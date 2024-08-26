import os
numero1 = 45
numero2 = 0
try:
    resultado = numero1 / numero2
except:
    resultado = 0
    print("Ha ocurrido un error")
finally:
    print(resultado)
    print("Esto se ejecuta siempre")
try:
    os.remove(os.getcwd()+"/archi454.txt")
except FileNotFoundError:
    print("El archivo no se encuentra en el directorio, no puedo borrarlo")
finally:
    print("Fin de la ejecucion del script")
