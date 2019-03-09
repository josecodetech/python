# -*- coding: utf-8 -*-
class Vehiculo:
    def __init__(self,color,tipo):
        self.color=color
        self.tipo=tipo
        self.velocidad=0
    def __str__(self):
        return "Es de tipo {}".format(self.tipo)
    def acelerar():
        self.velocidad=self.velocidad+10
        return self.velocidad
    def frenar():
        self.velocidad=0
        return self.velocidad
class Deportivo(Vehiculo):
    def __init__(self,color,tipo):
        super().__init__(color,tipo)
        self.deportivo=True
    def __str__(self):
        return "Es deportivo? {}".format(self.deportivo)
miCoche=Deportivo("rojo","gasolina")
print(miCoche)
tuCoche=Vehiculo("amarillo","diesel")
print(tuCoche)
print(tuCoche.acelerar)
