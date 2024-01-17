# datos iniciales
capital_inicial = 10000
tasa_interes = 0.06
periodos = 3

# interes simple
interes_simple = capital_inicial * tasa_interes * periodos
# interes compuesto
interes_compuesto = capital_inicial * (1 + tasa_interes) ** periodos - capital_inicial
print(f"El interes simple es de : {interes_simple}")
print(f"El interes compuesto es de : {round(interes_compuesto,2)}")
# diferencia en los intereses
diferencia = interes_compuesto - interes_simple
print("La diferencia de los intereses es de: "+str(round(diferencia,2)))