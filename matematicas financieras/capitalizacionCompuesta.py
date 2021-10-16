def interesEquivalente(tipoInteres, tiempoInteres):
    tipoInteres = tipoInteres / 100
    if tiempoInteres == "anual":
        tipoInteres = tipoInteres
    elif tiempoInteres == "semestral":
        tipoInteres = ((1+tipoInteres)**(1/2))-1
    elif tiempoInteres == "cuatrimestral":
        tipoInteres = ((1+tipoInteres)**(1/3))-1
    elif tiempoInteres == "trimestral":
        tipoInteres = ((1+tipoInteres)**(1/4))-1
    elif tiempoInteres == "bimensual":
        tipoInteres = ((1+tipoInteres)**(1/6))-1
    elif tiempoInteres == "mensual":
        tipoInteres = ((1+tipoInteres)**(1/12))-1
    elif tiempoInteres == "diario":
        tipoInteres = ((1+tipoInteres)**(1/365))-1
    return tipoInteres


def capitalCompuesto(capitalInicial, tipoInteres, tiempo, tiempoInteres="anual"):
    tipo = interesEquivalente(tipoInteres, tiempoInteres)
    interes = capitalInicial * (((1+(tipo))**tiempo)-1)
    capitalFinal = capitalInicial + interes
    print(f"El interes generado es de {round(interes,2)}")
    print(f"El capital final es de {round(capitalFinal,2)}")
    return capitalFinal, interes


if __name__ == "__main__":
    # print(interesEquivalente(12, "mensual"))
    # cap1, interes1 = capitalSimple(500, 12, 3, "trimestral")
    # cap2, interes2 = capitalSimple(700, 12, 1, "semestral")
    # print(f"El resultado final es = {cap1+cap2}")
    # cap1, int1 = capitalCompuesto(6000, 18, 1, "anual")
    # cap2, int2 = capitalCompuesto(6000, 18, 2.5, "anual")
    # print(interesEquivalente(17, "mensual")*100)
    # print(interesEquivalente(17, "trimestral")*100)
    # capitalCompuesto(6500, 14, 27, "mensual")
    #print(interesEquivalente(17, "mensual")*100)
    #print(interesEquivalente(17, "cuatrimestral")*100)
    capitalCompuesto(6527.5336576821965, 17.647058823529413, 0.5, "anual")
