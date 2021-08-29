import requests
from bs4 import BeautifulSoup
import re

url = 'https://cortefiel.com/es/es/hombre/polos-y-camisetas/camiseta-estampada-manga-corta/2199653.html?dwvar_2199653_color=87'
# print(url)

if __name__ == '__main__':
    # evitamos error 403 probar y mostrar el error
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    # print(response)
    if response.status_code == 200:
        web = response.text
        # print(contenido)
        soup = BeautifulSoup(web, 'html.parser')
        div = soup.find('div', {'_class': 'product-Price'})
        print(div)
        print("\n\n")
        # print(soup.title.get_text())
        #selector = "kindle-price"
        #resultado = soup.select('span.priceItem')
        #resultado = soup.find_all("h1", {"class": "scope_fixedBar"})
        #resultado = soup.span
        #resultado = soup.span.text
        etiquetas = soup.find_all('span')
        for etiqueta in etiquetas:
            print(etiqueta)
        input_tag = soup.findAll(True, {'class': re.compile(r'\bpriceItem\b')})
        #input_tag = soup.find_all('data-price')
        print(input_tag)
# for elemento in elementos:
#print(elemento, "\n")

else:
    print("Error")
