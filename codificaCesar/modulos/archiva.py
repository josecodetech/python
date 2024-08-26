import pickle


def guarda(texto):
    fichero = open('datos.pckl', 'wb')
    pickle.dump(texto, fichero)
    #print("fichero guardado")
    fichero.close()


def carga():
    fichero = open('datos.pckl', 'rb')
    dato = pickle.load(fichero)
    # print(dato)
    fichero.close()
    return dato


if __name__ == '__main__':
    guarda("Hola")
    carga()
