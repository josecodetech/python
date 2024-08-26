def dividir():
    num1 = int(input("Dime el primer numero: "))
    num2 = int(input("Dime el segundo numero: "))
    try:
        division = num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir por cero")
        division = 0
    finally:
        return division


def damePares():
    pares = []
    for i in range(1, 51):
        if i % 2 == 0:
            pares.append(i)
    return pares


def main():
    print(damePares())


if __name__ == "__main__":
    # print(dividir())
    main()
