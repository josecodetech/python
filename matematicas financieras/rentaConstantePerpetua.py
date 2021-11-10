def valorActualPospagable(capital, interes):
    interes = interes/100
    valorActual = capital * (1/interes)
    print(f"El valor actual de la renta es igual a {round(valorActual,2)}")
    # return valorActual


def valorActualPrepagable(capital, interes):
    interes = interes/100
    valorActual = capital * ((1+interes)/interes)
    print(f"El valor actual de la renta es igual a {round(valorActual,2)}")
    # return valorFinal


if __name__ == "__main__":
    valorActualPospagable(1400, 7.23)
    valorActualPrepagable(1400, 7.23)
