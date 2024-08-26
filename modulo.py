#Importa modulo
import saludo
saludo.saludar()
#saludar() daria error
#De esta forma ya no
from saludo import saludar
saludar()
#Con alias
import saludo as s
s.saludar()
