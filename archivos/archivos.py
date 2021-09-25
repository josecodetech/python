import os

carpeta = "D:\\workspace\\WorkspaceTutorialPython\\archivos\\micarpeta"
# print(carpeta)
listado = os.listdir(carpeta)
print(listado)
print(type(listado))
# filtrado
# for archivo in listado:
# if archivo.endswith(".txt"):
#print("Fichero mp3 encontrado!!! ")
#print(f"Nombre de fichero: {archivo}")
# otra forma de filtrar
filtrado = [archivo for archivo in listado if archivo.endswith(".zip")]
print(type(filtrado))
print(filtrado)
# cambio de directorio
os.chdir("D:\\workspace\\WorkspaceTutorialPython\\archivos\\micarpeta")
# renombrar
#os.rename("comprimido.zip", "cambiadoNombreComprimido.zip")
# borrar
os.chdir("D:\\workspace\\WorkspaceTutorialPython\\archivos\\micarpeta")
# os.remove("cambiadoNombreComprimido.zip")
filtrado = [archivo for archivo in listado if archivo.endswith(".zip")]
print(filtrado)


# renombrar varios archivos a la vez
contador = 1
listado = os.listdir(carpeta)
# print(listado)
# print("fin listado inicial")
# for archivo in os.listdir():
#     nombre, extension = os.path.splitext(archivo)
#     print(nombre)
#     print(extension)
#     nuevoNombre = f'renombrado{str(contador)}_{nombre}{extension}'
#     contador += 1
#     os.rename(archivo, nuevoNombre)
# listado = os.listdir(carpeta)
# print("Listado renombrado")
# print("\n\n")
# print(listado)

# copiar contenido de un fichero a otro
# try:
#     fichero = open("testNoExiste.txt", 'r')
#     nuevoFichero = open("nuevoTest.txt", 'w')
#     os.chdir("D:\\workspace\\WorkspaceTutorialPython\\archivos\\micarpeta")
#     for linea in fichero:
#         nuevoFichero.write(linea)
#     fichero.close()
#     nuevoFichero.close()
# except FileNotFoundError:
#     print("No se ha encontrado el fichero")

# otra forma con with
try:
    os.chdir("D:\\workspace\\WorkspaceTutorialPython\\archivos\\micarpeta")
    with open("test.txt") as fichero:
        with open("nuevoFichero.txt", "w") as nuevoFichero:
            for linea in fichero:
                nuevoFichero.write(linea)
except FileNotFoundError:
    print("Fichero no encontrado")
