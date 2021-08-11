import numpy as np
lista1 = [1, 2, 3, 4, 5, 6, 3, 2, 8, 9]
array1 = np.array(lista1)
print(lista1)
print(type(array1))
print(array1)
lista2 = [[1, 2, 4], [2, 5, 3], [9, 4, 2]]
array2 = np.array(lista2)
print(array2)

# arrays generacion automatica
array = np.arange(2, 25, 3)
print(array)
matrizCeros = np.zeros((4, 5))
print(matrizCeros)
matrizUnos = np.ones((3, 5))
print(matrizUnos)
# matriz de 40 elementos con valores del 2 al 6
matriz = np.linspace(2, 6, 40)
print(matriz)
# matriz identidad
matrizIdentidad = np.eye(7)
print(matrizIdentidad)
# numeros aleatorios
matrizAleatoria = np.random.rand(3, 4)
print(matrizAleatoria)
matrizAleatoriaNormal = np.random.randn(4)
print(matrizAleatoriaNormal)
matrizAleatoriaEnteros = np.random.randint(1, 51, 20)
print(matrizAleatoriaEnteros)
# tamaños arrays
array = np.random.randint(1, 201, 30)
print(array)
matriz = array.reshape(5, 6)
print(matriz)
# max y min
array = np.random.randint(1, 901, 200)
print(array)
maximo = array.max()
print(f"El valor maximo es {maximo}")
print(array.argmax())
minimo = array.min()
print(f"El valor minimo es {minimo}")
print(array.argmin())
# mostrar elementos
array = np.arange(1, 11)
print(array)
print(array[2])
print(array[5:])
print(array[:6])
# copia de array
array2 = array.copy()
print(array)
print(array2)
array2[4] = 9999
print(array)
print(array2)
# operaciones con la matriz
print(matriz)
print(matriz[0])  # primera fila
print(matriz[:2])
print(matriz[1, 2])
print(matriz[:, 1])
print(matriz[:, :1])
print(matriz)
print(matriz+10)
print(matriz+matriz)
print(matriz*10)
print(matriz*matriz)
print(np.max(matriz))
condicion = matriz > 100
print(matriz)
print(condicion)
print(matriz[condicion])
# numeros impares
condicion = (matriz % 2 != 0)
print(matriz[condicion])

# ejercicio
lista = np.arange(5, 41)
print("Mostrando lista dimension uno")
print(lista)
print("Mostrando lista dimension modificada a 3 * 12")
lista = lista.reshape(3, 12)
print(lista)
print("Mostrando valor del indice 2,4")
print(lista[2, 4])
# combinacion primitiva
arrayPrimitiva = np.random.randint(1, 50, 6)
print(f"La combinacion ganadora de la primitiva sera {arrayPrimitiva}")
