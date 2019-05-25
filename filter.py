#Filtrado con lambda
num=[2,5,6,8,9,2,23,43,44,56,32]
#devolvemos impares
impares=list(filter(lambda num:num%2!=0,num))
print(impares)