import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

client_id= 'YOUR-CLIENT-ID'
client_secret= 'YOUR-CLIENT-SECRET'
redirect_uri = 'YOUR-REDIRECT-URI'

sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=['user-read-playback-state', 'user-modify-playback-state', 'streaming'])
sp=spotipy.Spotify(auth_manager=sp_oauth)
