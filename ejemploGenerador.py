import string
import random

caracteres = list(string.ascii_letters + string.digits + "!#@&%$()/\+")
# print(caracteres)


def dameClave():
    longitud = int(input("Que longitud le damos a la clave? "))
    # mezcla los caracteres
    random.shuffle(caracteres)
    clave = []
    for i in range(longitud):
        clave.append(random.choice(caracteres))
    random.shuffle(clave)
    return ("".join(clave))


if __name__ == "__main__":
    clave = dameClave()
    print(f"La clave seleccionada es: {clave}")
