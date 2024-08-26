lista_usuario = input('Dame una lista de colores separados por comas : ')
lista_usuario = set(lista_usuario.split(','))
lista_colores = []
for color in lista_usuario:
    lista_colores.append(color)
lista_colores.sort()
print(lista_colores)
