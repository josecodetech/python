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
    return tipoInteres / 100


def capitalSimple(capitalInicial, tipoInteres, tiempo, tiempoInteres="anual"):
    tipo = (interesEquivalente(tipoInteres, tiempoInteres))
    interes = round((capitalInicial*tipo*tiempo), 2)
    capitalFinal = capitalInicial + interes
    print(f"El interes generado es de {interes}")
    print(f"El capital final es de {capitalFinal}")
    return capitalFinal, interes


if __name__ == "__main__":
    #print(interesEquivalente(12, "mensual"))
    #cap1, interes1 = capitalSimple(500, 12, 3, "trimestral")
    #cap2, interes2 = capitalSimple(700, 12, 1, "semestral")
    #print(f"El resultado final es = {cap1+cap2}")
    #cap1, inter1 = capitalSimple(6000, 18, 1, "anual")
    #cap2, inter2 = capitalSimple(6000, 18, 2.5, "anual")
    capitalSimple(100000, 12.5, 8, "anual")
