import json
from urllib import request
url = 'https://my.api.mockaroo.com/pruebas.json?key=b7cebbb0'

respuesta = request.urlopen(url)
print(respuesta)
contenido = respuesta.read()
print(contenido)
json_obtenido = json.loads(contenido.decode('utf-8'))
print(json_obtenido)
for persona in json_obtenido:
    print(persona)
