def descuentoCompuesto(nominal, tipoDescuento, tiempo):
    efectivo = nominal*((1+(tipoDescuento/100))**(-tiempo))
    descuento = nominal - efectivo
    print(f"El descuento aplicado es de {round(descuento,2)}")
    print(f"El efectivo obtenido es de {round(efectivo,2)}")
    # return nominal, descuento


def interesEquivalente(tipoDescuento):
    tipoDescuento = tipoDescuento/100
    interes = (tipoDescuento/(1-tipoDescuento))*100
    print(f"El interes equivalente es igual a {(interes)}")
    # return interes


if __name__ == "__main__":
    tiempo = 4 / 12
    descuentoCompuesto(1500, 13, tiempo)
    # interesEquivalente(15)
