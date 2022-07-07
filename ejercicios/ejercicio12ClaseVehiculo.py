class Vehiculo():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    def __str__(self):
        return "El vehiculo de marca {}, es de color {}".format(self.marca,self.color)
class Coche(Vehiculo):
    def __init__(self,marca,color,potencia,motor):
        Vehiculo.__init__(self,marca,color)
        self.potencia = potencia
        self.motor = motor
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} Cv y motor de {}".format(self.potencia, self.motor)

mi_Vehiculo = Vehiculo('seat','verde')
print(mi_Vehiculo)
mi_Coche = Coche('seat','rojo','1400','gasolina')
print(mi_Coche)
