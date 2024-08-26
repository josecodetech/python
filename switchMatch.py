color = 'rosa'
match color:
    case 'rojo':
        print('Es rojo')
    case 'azul':
        print('Es azul')
    case 'verde':
        print('Es verde')
    case _:
        print('Ese color no esta aqui')

mes = 10
match mes:
    case 1:
        print('Enero')
    case 2:
        print('Febrero')
    case 3:
        print('Marzo')
    case 4:
        print('Abril')
    case 5:
        print('Mayo')
    case 6:
        print('Junio')
    case 7:
        print('Julio')
    case 8:
        print('Agosto')
    case 9:
        print('Septiembre')
    case 10:
        print('Octubre')
    case 11:
        print('Noviembre')
    case 12:
        print('Diciembre')
    case _:
        print('codigo invalido')
