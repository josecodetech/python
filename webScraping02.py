# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 19:33:53 2019

@author: Jose
"""

import bs4, requests

def damePrecio(url,identificador):
    res=requests.get(url)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    elemento=soup.select(identificador)
    precio=elemento[0].text.strip()
    return precio
def comparaPrecio(precio01,precio02):
    if precio01>precio02:
        print("El articulo primero vale mas")
    elif precio01<precio02:
        print("El articulo segundo vale mas")
    else:
        print("Los precios son iguales")
        
precio01=damePrecio('https://www.marypaz.com/es_es/alpargata-pulsera-ante-negro-81772','#product-price-37924')
print(precio01)

precio02=damePrecio('https://www.marypaz.com/es_es/sandalia-cu-a-esparto-ante-azul-marino-79027','#product-price-37987')
print(precio02)
comparaPrecio(precio01,precio02)
