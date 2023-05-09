import requests
import json
import os

url_base = "http://ws.audioscrobbler.com/2.0/"
api_key = os.environ["api_key"]

print("Este programa buscará información sobre la cancion especificada.")
print()
artista = input("Introduce el nombre del artista: ")
cancion = input("Introduce el nombre de la canción de " + artista + ": ")
print()
payload = {
    "method": "track.getInfo",
    "artist": artista,
    "track": cancion,
    "api_key": api_key,
    "format": "json"
}

response = requests.get(url_base, params=payload)

if response.status_code == 200:
    data = json.loads(response.text)
    if "error" in data:
        print("Error: {}".format(data["message"]))
    else:
        track_info = data["track"]
        print("- Información de la canción {}: ".format(track_info['wiki']['summary']))
        print()
        print("- Nombre del artista: {}".format(track_info["artist"]["name"]))
        print()
        print("- Nombre de la canción: {}".format(track_info["name"]))
        print()
        print("- URL de la página de la canción: {}".format(track_info["url"]))
        print()
        print("- Duración: {} segundos".format(track_info["duration"]))
        print()
        print("- Número de reproducciones: {}".format(track_info["playcount"]))
else:
    print("Ha ocurrido un error al realizar la petición.")
