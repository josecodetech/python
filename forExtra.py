lista_colores = ['rojo', 'amarillo', 'verde', 'azul']
mi_color = 'rosa'
for color in lista_colores:
    print(color)
    if color == mi_color:
        print('color encontrado')
        break
else:
    print(f'No he encontrado el color {mi_color}')

rango_largo = range(1, 10000)
print(rango_largo)
for numero in rango_largo:
    print(numero)
    if numero == 999999:
        print(f'Encontado el numero {numero}')
        break
        # continue
else:
    print('No he encontrado el numero indicado')
