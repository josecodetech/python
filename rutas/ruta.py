import os
import pandas as pd

# directorio actual
directorio_actual = os.getcwd()
print(directorio_actual)
# directorio datos
directorio_datos = os.path.join(directorio_actual, 'datos')
print(directorio_datos)
print("Existe el directorio ? ")
print(os.path.exists(directorio_datos))
print("Es una carpeta o directorio ? ")
print(os.path.isdir(directorio_datos))
# listar archivos de datos
listado = [os.path.join(directorio_datos, item)
           for item in os.listdir(directorio_datos)]
print(listado)
print(os.listdir(directorio_datos))
# crear carpeta
try:
    carpeta_nueva = os.mkdir(os.path.join(directorio_actual, "nueva"))
    print(carpeta_nueva)
except FileExistsError:
    print("La carpeta ya existe")

# Abrimos fichero fuera de datos
fichero_exterior = os.path.join(directorio_actual, "datos.csv")
df_exterior = pd.read_csv(fichero_exterior)
print("Mostramos fichero exterior")
print(df_exterior)
# Abrimos fichero dentro de datos
fichero_interior = os.path.join(directorio_datos, "datos.csv")
df_interior = pd.read_csv(fichero_interior)
print("Mostramos fichero interior")
print(df_interior)
# Abrimos sin indicar ruta
fichero = "datos.csv"
df = pd.read_csv(fichero)
print("Fichero sin indicar ruta")
print(df)
