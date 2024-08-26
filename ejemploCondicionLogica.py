#Solicitamos texto y comprobamos
#si cumple la condicion
cadena=input('Dame un texto - ')
condicion=len(cadena)>4 and len(cadena)<12
print('el texto es mayor q 4 y menor q 12? '+str(condicion))