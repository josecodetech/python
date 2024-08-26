palabra = input("Dime una palabra: ")
palabraAlReves = palabra[::-1]
print(palabra)
print(palabraAlReves)
if(palabra == palabraAlReves):
    print("Es palindromo")
else:
    print("No es palindromo")
