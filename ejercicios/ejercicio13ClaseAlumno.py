class Alumno():
    def __init__(self,nombre,calificacion):
        self.nombre = nombre
        self.calificacion = calificacion
    def __str__(self):
        return "El alumno {}, ha sacado un {}".format(self.nombre, self.calificacion)
    def aprobado(self):
        if self.calificacion < 5:
            return False
        else:
            return True  
jose = Alumno('Jose',6)
print(jose)
aprobado = jose.aprobado()
if aprobado:
    print('Esta aprobado')
else:
    print('Esta suspendido')  