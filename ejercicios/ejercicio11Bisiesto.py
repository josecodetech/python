def bisiesto(año):
    if año % 4 != 0:
        return False
    elif año % 4 == 0 and año % 100 != 0:
        return True
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
        return False
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
        return True


print(bisiesto(2019))
print(bisiesto(2020))
print(bisiesto(2100))
print(bisiesto(2025))
