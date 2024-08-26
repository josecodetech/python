DOLAREURO = 0.90


def cambiarDolar(dolares):
    euros = dolares * DOLAREURO
    return euros


def cambiarEuros(euros):
    dolares = euros / DOLAREURO
    return dolares


def solicitarCantidad(tipo):
    cantidad = float(input(f"Cuanta cantidad de {tipo} vas a cambiar? "))
    return cantidad


if __name__ == '__main__':
    menu = """
        Cambio de monedas
        Selecciona una opcion
        1. Cambio a Euros
        2. Cambio a Dolares
        3. Salir
    """
    while True:
        opcion = int(input(menu))
        if opcion == 1:
            cantidad = solicitarCantidad("dolares")
            euros = round(cambiarDolar(cantidad), 2)
            print(
                f"El resultado de cambiar {cantidad} dolares es de {euros} euros")
        elif opcion == 2:
            cantidad = solicitarCantidad("euros")
            dolares = round(cambiarEuros(cantidad), 2)
            print(
                f"El resultado de cambiar {cantidad} euros es de {dolares} dolares")
        else:
            print("Adios!!!")
            break
