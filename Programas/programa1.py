import requests
import os
import json

url_base = "http://ws.audioscrobbler.com/2.0/"
api_key = os.environ["api_key"]

print("Este programa buscará información sobre la biografía del artista que introduzcas, \nasimismo también te mostrará el top 5 de sus canciones mas populares.")
print()
artista = input("Introduce el nombre del artista: ")
print()
payload_bio = {
    "method": "artist.getinfo",
    "artist": artista,
    "api_key": api_key,
    "format": "json"
}

response_bio = requests.get(url_base, params=payload_bio)

if response_bio.status_code == 200:
    data_bio = json.loads(response_bio.text)
    if "error" in data_bio:
        print("Error: {}".format(data_bio["message"]))
    else:
        bio = data_bio["artist"]["bio"]["content"]
        print("Biografía de {}: \n{}".format(artista, bio))

        payload_top = {
            "method": "artist.gettoptracks",
            "artist": artista,
            "api_key": api_key,
            "format": "json",
            "limit": 5
        }

        response_top5 = requests.get(url_base, params=payload_top)

        if response_top5.status_code == 200:
            data_top = json.loads(response_top5.text)
            if "error" in data_top:
                print("Error: {}".format(data_top["message"]))
            else:
                top_tracks = data_top["toptracks"]["track"]
                print("\nTop 5 canciones de {}: ".format(artista))
                for i, track in enumerate(top_tracks):
                    print("{}. {}".format(i+1, track["name"]))
        else:
            print("Ha ocurrido un error al obtener el top de canciones.")
else:
    print("Ha ocurrido un error al realizar la petición de la biografía.")   
