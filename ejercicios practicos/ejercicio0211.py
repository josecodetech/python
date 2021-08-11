def esVocal(c):
    c = c.lower()
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        return True
    else:
        return False


print(esVocal("G"))
