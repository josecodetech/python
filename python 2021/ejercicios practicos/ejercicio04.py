cuenta = 0
print("Numeros Pares ")
for i in range(1, 51):
    if(i % 2 == 0):
        print(i)
        cuenta = cuenta + 1
print(f"Tenemos {cuenta} numeros pares")
