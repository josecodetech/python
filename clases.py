#CLASE COCHE Y METODOS
class coche:
    #CONSTRUCTOR DE LA CLASE
    def __init__(self,color,puertas):
        self.color=color
        self.puertas=puertas
    #METODO DE LA CLASE
    def arranca(self):
        print("Arrancando!!!")
miCoche1=coche("rojo",5)
print(miCoche1.color)
print(miCoche1.puertas)
miCoche1.arranca()
miCoche2=coche("verde",3)
print(miCoche2.color)
print(miCoche2.puertas)
miCoche2.arranca()
