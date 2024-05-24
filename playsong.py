import os
from spotipy.oauth2 import SpotifyOAuth
from packages.package import *

def play_song():
    song_name=[]
    singer_name=[]
    song_id=[]
    query=input("Enter track name: ")
    results= sp.search(q= query,type= 'track')
    def fetch_singer():
        for item in results['tracks']['items']:
            item2=item['album']['artists']
            listofsingers=[]
            for i in item2:
                listofsingers.append(i['name'])
            singer_name.append(' , '.join(listofsingers))
 
    def fetch_trackid():
        for item in results['tracks']['items']:
            song_id.append(item['id'])
    

    def fetch_trackname():
        for item in results['tracks']['items']:
            song_name.append(item['name'])
    
    fetch_trackname()
    fetch_singer()
    fetch_trackid()

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[36m"+f"Showing search results for {query }: \n"+"\033[0m")
    song_info={'song_name':song_name,'singer_name':singer_name,'song_id':song_id}
    for i in range(0,5):
        print("\033[35m"+f"{i+1}. "+"\033[0m"+"\033[36m"+song_info['song_name'][i]+"\033[0m"+" -- "+"\033[34m"+song_info['singer_name'][i]+"\033[0m")
    return song_info

def start_song():
    song_info=play_song()
    track=int(input("\033[33m"+"Select track to play"+"\033[0m\t"))
    sp.start_playback(uris=['spotify:track:' + song_info['song_id'][track-1]])
    

def pause_song():
    sp.pause_playback()

def resume_song():
    sp.start_playback()

def addtoqueue():
    song_info=play_song()
    track=int(input("\033[33m"+"Select track to add to queue"+"\033[0m\t"))
    sp.add_to_queue(uri=song_info['song_id'][track-1])
