#CLASE PADRE
class animal:
    def __init__(self,nombre,color):
        self.nombre=nombre
        self.color=color
#CLASE QUE HEREDA
class gato(animal):
    def maulla(self):
        print ("miau!!!")
#CREAMOS OBJETO DE CLASE GATO
tobby=gato("Tobby","marron")
print(tobby.color)
print(tobby.nombre)
tobby.maulla()

