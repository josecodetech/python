def es_primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            #print(f'El numero {numero} no es primo, {i} es divisor')
            return False
        elif numero % numero == 0 and numero % 1 == 0:
            #print(f'El numero {numero} es primo')
            return True


print(es_primo(142))
print(es_primo(256))
print(es_primo(1303))
es_primo = es_primo(1303)
if es_primo:
    print('El numero 1303 es primo')
else:
    print('El numero 1303 no es primo')
