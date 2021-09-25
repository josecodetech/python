class Vehiculo:
    """
    Documentacion de mi clase
    Esto es mi documentacion
    """

    def __init__(self, color, velocidadMaxima, marca):
        '''
        Documentacion del constructor
        '''
        self.color = color
        self.velocidadMaxima = velocidadMaxima
        self.velocidad = 0
        self.marca = marca

    def arrancar(self):
        print('Arrancado')

    def acelerar(self):
        if self.velocidad == 0:
            self.velocidad = 10
        else:
            self.velocidad = self.velocidad + 10
        print(f"Velocidad = {self.velocidad}")

    def frenar(self):
        if self.velocidad > 10:
            self.velocidad = self.velocidad - 10
        else:
            self.velocidad = 0
        print(f"Velocidad = {self.velocidad}")

    def muestraEstado(self):
        print(
            f"Soy de la marca {self.marca}, con un color {self.color} y velocidad maxima de {self.velocidadMaxima}")


class Moto(Vehiculo):
    def __init__(self, color, velocidaMaxima, marca, ruedas=2):
        Vehiculo.__init__(self, color, velocidaMaxima, marca)
        self.ruedas = ruedas

    def muestraEstado(self):
        print(
            f"Soy de la marca {self.marca}, con un color {self.color},\n velocidad maxima de {self.velocidadMaxima} y tengo {self.ruedas} ruedas")


class Coche(Vehiculo):
    def __init__(self, color, velocidaMaxima, marca, ruedas=4):
        Vehiculo.__init__(self, color, velocidaMaxima, marca)
        self.ruedas = ruedas

    def muestraEstado(self):
        print(
            f"Soy de la marca {self.marca}, con un color {self.color},\n velocidad maxima de {self.velocidadMaxima} y tengo {self.ruedas} ruedas")


peugeot = Coche('rojo', 120, 'Peugeot', 4)
peugeot.arrancar()
peugeot.acelerar()
peugeot.muestraEstado()
peugeot.acelerar()
renault = Coche('verde', 130, 'Renault', 4)
renault.arrancar()
renault.acelerar()
renault.acelerar()
renault.muestraEstado()
yamaha = Moto('azul', 140, 'Yamaha', 2)
yamaha.arrancar()
yamaha.acelerar()
yamaha.acelerar()
yamaha.frenar()
yamaha.muestraEstado()
