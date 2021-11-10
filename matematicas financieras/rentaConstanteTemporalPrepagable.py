def valorActual(capital, tiempo, interes):
    interes = interes/100
    valorActual = capital * (1+interes)*((1-(1+interes)**(-tiempo))/interes)
    print(f"El valor actual de la renta es igual a {round(valorActual,2)}")
    # return valorActual


def valorFinal(capital, tiempo, interes):
    interes = interes/100
    valorFinal = capital * (1+interes)*((((1+interes)**tiempo)-1)/interes)
    print(f"El valor final de la renta es igual a {round(valorFinal,2)}")
    # return valorFinal


if __name__ == "__main__":
    valorActual(1200, 12, 5.83)
    valorFinal(1200, 12, 5.83)
