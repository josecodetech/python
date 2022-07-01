def area_triangulo(base, altura):
    area = (base*altura)/2
    return area


base = float(input('Indicame la base del triangulo: '))
altura = float(input('Indicame la altura del triangulo: '))
area = area_triangulo(base, altura)
print(f'El area del triangulo con base {base} y altura {altura} es {area}')
