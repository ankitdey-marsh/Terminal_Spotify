import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

client_id= '2a54670dc23b4656ae17ab2c86949c8c'
client_secret= '939856e1200b47d484a017a5f126ab39'
redirect_uri = 'https://localhost:8080/'

sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=['user-read-playback-state', 'user-modify-playback-state', 'streaming'])
sp=spotipy.Spotify(auth_manager=sp_oauth)