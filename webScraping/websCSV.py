import requests
from bs4 import BeautifulSoup
import csv
url = 'https://ticoticotaa.es/principal.php'

if __name__ == '__main__':
    response = requests.get(url)
    # print(response)
    if response.status_code == 200:
        contenido = response.text
        soup = BeautifulSoup(contenido, 'html.parser')
        fichero = csv.writer(open("urls.csv", "a"))
        print("Obteniendo links \n")
        for link in soup.find_all('a'):
            print(link.get('href'))
            fichero.writerow([link.get('href')])
        print("Hemos terminado de obtener los links")
