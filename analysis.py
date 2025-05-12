import pandas as pd
from collections import Counter
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import matplotlib.pyplot as plt

def estilo_artistas(sp, timeRange):
    result = sp.current_user_top_artists(limit=50, time_range=timeRange)

    generos = []
    for artist in result['items']:
        generos.extend(artist['genres'])

    contagem = Counter(generos)
    mais_comuns = contagem.most_common(10)

    df = pd.DataFrame(mais_comuns, columns=['gênero', 'frequência'])

    df.set_index('gênero')['frequência'].plot.pie(autopct='%1.1f%%')
    plt.title("Distribuição de gêneros entre os top artistas")
    plt.ylabel("")
    plt.show()

def estilo_musicas(sp, timeRange):
    top_musicas = sp.current_user_top_tracks(limit=50, time_range=timeRange)

    id_artistas = []
    for musica in top_musicas['items']:
        id_artistas.append(musica['artists'][0]['id'])

    generos = []
    for i in range(0, len(id_artistas), 50):
        artistas = sp.artists(id_artistas[i:i+50])['artists']
        for artist in artistas:
            generos.extend(artist['genres'])

    contagem = Counter(generos)
    df = pd.DataFrame(contagem.most_common(10), columns=["gênero", "frequência"])

    df.set_index('gênero')['frequência'].plot.pie(autopct='%1.1f%%')
    plt.title("Distribuição de gêneros entre os top artistas")
    plt.ylabel("")
    plt.show()

def musicas_mais_ouvidas(sp, timeRange):
    top_musicas = sp.current_user_top_tracks(limit=10, time_range=timeRange)
    
    musicas = []
    for musica in top_musicas['items']:
        musicas.append({
            "nome": musica['name'],
            "artista": musica['artists'][0]['name'],
            "álbum": musica['album']['name'],
            "popularidade": musica['popularity'],
            "duração": musica['duration_ms'] // 1000
        })
    df = pd.DataFrame(musicas)
    print(df)

def artistas_mais_ouvidos(sp, timeRange):
    top_artistas = sp.current_user_top_artists(limit=10, time_range=timeRange)   
    df = pd.DataFrame(top_artistas['items'], columns=['name', 'popularity'])
    print(df)