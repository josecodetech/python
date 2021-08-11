import requests
from bs4 import BeautifulSoup

url = 'https://ticoticotaa.es/principal.php'

if __name__ == '__main__':
    response = requests.get(url)
    if response.status_code == 200:
        contenido = response.text
        soup = BeautifulSoup(contenido, 'html.parser')
        # mostramos cabecera
        print(soup.head)
        print(soup.prettify())
        print(type(soup.head))
