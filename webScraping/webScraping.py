import requests
from bs4 import BeautifulSoup

url = 'https://ticoticotaa.es/principal.php'

if __name__ == '__main__':
    response = requests.get(url)
    # print(response)
    if response.status_code == 200:
        contenido = response.text
        soup = BeautifulSoup(contenido, 'html.parser')
        print(soup.title)
        for elemento in soup.find_all('div'):
            print("Elemento encontrado")
            print(elemento.get_text(), '\n')
        print("\nEstilos")
        print(soup.find_all('style'))
        print('Fin de estilos')
        print("\nImagenes:")
        for imagen in soup.find_all('img'):
            print(imagen)
        # etiqueta
        titulo = soup.find('title')
        print("Etiqueta titulo\n")
        print(titulo)
        print(titulo.text)
        print(titulo.get_text())
        print(titulo.name)
        print(soup.find('h1'))
        print(soup.find_all('p'))
