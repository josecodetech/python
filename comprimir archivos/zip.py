# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 08:25:30 2020

@author: Jose
"""

import zipfile
#creacion archivo comprimido
with zipfile.ZipFile('comprimidos.zip','w') as fzip:
    fzip.write('archivo01.txt')
    fzip.write('archivo02.txt')
    fzip.write('archivo03.txt')
    fzip.write('archivo04.txt')
    fzip.write('archivo05.txt')
    print('Archivos comprimidos')
#listar contenido del archivo zip
fzip = zipfile.ZipFile('comprimidos.zip')
print(fzip.printdir())
listaArchivos = fzip.namelist()
print(listaArchivos)
#obtenemos mas informacion
info = fzip.infolist()
for archivo in info:
    print(archivo.filename,archivo.date_time,archivo.compress_size)
#descomprimir fichero
fzip.extractall() #()(path='ruta archivo')