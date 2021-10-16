def interesEquivalente(tipoInteres, tiempoInteres):
    if tiempoInteres == "anual":
        tipoInteres = tipoInteres
    elif tiempoInteres == "semestral":
        tipoInteres = tipoInteres/2
    elif tiempoInteres == "cuatrimestral":
        tipoInteres = tipoInteres/3
    elif tiempoInteres == "trimestral":
        tipoInteres = tipoInteres/4
    elif tiempoInteres == "bimensual":
        tipoInteres = tipoInteres/6
    elif tiempoInteres == "mensual":
        tipoInteres = tipoInteres/12
    elif tiempoInteres == "diario":
        tipoInteres = tipoInteres/365
    return tipoInteres


def descuentoComercial(capitalInicial, tipoInteres, tiempo, tiempoInteres="anual"):
    tipo = round(interesEquivalente(tipoInteres, tiempoInteres), 2)
    descuentoComercial = round(capitalInicial*(tipo/100)*tiempo, 2)
    capitalFinalComercial = capitalInicial - descuentoComercial
    print(f"El descuento generado es de {descuentoComercial}")
    print(f"El capital final es de {capitalFinalComercial}")
    # return capitalFinalComercial, descuentoComercial


def descuentoRacional(capitalInicial, tipoInteres, tiempo, tiempoInteres="anual"):
    tipo = round(interesEquivalente(tipoInteres, tiempoInteres), 2)
    descuentoRacional = round(
        (capitalInicial*(tipo/100)*tiempo)/(1+((tipo/100)*tiempo)), 2)
    capitalFinalRacional = capitalInicial - descuentoRacional
    print(f"El descuento generado es de {descuentoRacional}")
    print(f"El capital final es de {capitalFinalRacional}")
    # return capitalFinalRacional,descuentoRacional


if __name__ == "__main__":
    print(interesEquivalente(14, "mensual"))
    #descuentoComercial(6000, 11, 4, "mensual")
    #descuentoComercial(3500, 12, 3, "mensual")
    descuentoRacional(2400, 10, 8, "mensual")
