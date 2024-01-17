# datos iniciales
capital_inicial = 1000
tasa_interes = 0.05
periodos = 3 
# formula
capital_final = capital_inicial * (1+tasa_interes)**periodos
# resultado
print("El capital final es de :"+str(round(capital_final,2)))
intereses = capital_final - capital_inicial
print("Los intereses generados son de: "+str(round(intereses,2)))