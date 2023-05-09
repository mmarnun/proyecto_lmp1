import requests
import json
import os

url_base = "http://ws.audioscrobbler.com/2.0/"
api_key = os.environ["api_key"]

print("Este programa te mostrará una pequeña descricpión sobre el genero musical que introduzcas \ny el número de artistas que cantan el genero.")
print()
genero = input("Introduce el nombre de un género musical: ")
print()

payload = {
    "method": "tag.getinfo",
    "tag": genero,
    "api_key": api_key,
    "format": "json"
}

response = requests.get(url_base, params=payload)

if response.status_code == 200:
    data = json.loads(response.text)
    if "error" in data:
        print("Error: {}".format(data["message"]))
    else:
        tag_info = data["tag"]
        print("- Nombre del género: {}".format(tag_info["name"]))
        print()
        print("- Descripción: {}".format(tag_info["wiki"]["content"]))
        print()
        print("- Número de artistas etiquetados: {}".format(tag_info["total"]))
else:
    print("Ha ocurrido un error al realizar la petición.")
