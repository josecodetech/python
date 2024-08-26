# tabla de multiplicar con FOR
tabla = int(input("Que tabla quieres ver? "))
print(f"Tabla del {tabla}")
# repetir mientras sea menor que 11
for contador in range(1, 11):
    resultado = tabla * contador
    print(f"{tabla} por {contador} es igual a {resultado}")
print("Fin de la tabla")

# ejemplo For con lista
nombres = ["Jose", "M Mar", "Lucia", "Eva"]
for nombre in nombres:
    print(f"Hola, {nombre}")

# mostrar 100 numeros
for numero in range(100):
    print(numero+1)
