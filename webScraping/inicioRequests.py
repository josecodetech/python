import requests

url = 'https://ticoticotaa.es/principal.php'

if __name__ == '__main__':
    response = requests.get(url)
    # print(response)
    if response.status_code == 200:
        contenido = response.text
        # print(contenido)
        with open('contenidoWeb.txt', 'w+') as fichero:
            fichero.write(contenido)
