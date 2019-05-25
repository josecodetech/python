# -*- coding: utf-8 -*-
"""
Created on Sat May 25 07:47:27 2019

@author: Jose
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try: 
    html = urlopen("http://ticoticotaa.es/ejemplowebscraping.php")
except HTTPError as e:
    print(e)
except URLError:
    print("Servidor caido o dominio incorrecto")
else:
    resultado = BeautifulSoup(html.read(),"html5lib")
    #print(resultado.title)
    articulo = resultado.findAll("div",{"class":["articulo"]})
    #print(articulo)
    descripcion=resultado.findAll("div",{"class":["descripcion"]})
    precio=resultado.findAll("div",{"class":["precio"]})
    descripcionLista=[]
    precioLista=[]
    for desc in descripcion:
        descripcionLista.append(desc.getText().strip())
    print(descripcionLista)
    for prec in precio:
        precioLista.append(prec.getText().strip())
    print(precioLista)
    for i in range(len(descripcionLista)):
        if int(precioLista[i])<150:
            print(descripcionLista[i]+' : '+precioLista[i]+' €')
            print(' *** esta por debajo de 150 € *** ')
        else:
            print(descripcionLista[i]+' : '+precioLista[i]+' €')            