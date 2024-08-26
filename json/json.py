# -*- coding: utf-8 -*-
"""
Created on Sun May 31 07:35:03 2020

@author: Jose
"""
import json
datos = {
    "a":{'nombre':'Jose','nota':5.2},
    "b":{'nombre':'Lucia','nota':8.5},
    "c":{'nombre':'Eva','nota':8.0}
    }
# print(datos)
# print(type(datos))

#guardamos en archivo
with open("datos.json","w") as fichero:
    json.dump(datos,fichero)
    print("Fichero guardado")
#recuperamos datos de fichero
with open("datos.json") as fichero:
    datosJSON = json.load(fichero)
    print("Fichero cargado")
#mostramos datos recuperados
print("Mostrando datos desde fichero JSON")
print(datosJSON)
print("\n")
print("Datos de alumno B")
print(datosJSON["b"])
print("Nombre de alumno C")
print(datosJSON["c"]["nombre"])

