from packages.package import *
import playsong as ps
import time

os.system('cls' if os.name == 'nt' else 'clear')
devices=sp.devices()
if len(devices['devices'])==0:
    print("\033[31m"+"Open spotify on a device first"+"\033[0m\t")
    exit()
else:
    print("\033[32m"+f"{len(devices['devices'])} active device(s) found"+"\033[0m\t"+"\n")
device_count=0
for device in devices['devices']:
    print("\033[33m"+f"{device_count+1}. {device['name']}"+"\033[0m\t")
    device_count+=1
def select_device(device_count):
    device_count2=1
    device_no=int(input(("\033[34m"+"Enter device to connect to : "+"\033[0m\t")))
    for device_id in devices['devices']:
        if device_count2==device_no:
            sp.transfer_playback(device_id=device_id['id'])
        elif device_no>device_count:
            print("\033[33m"+"Enter a valid number"+"\033[0m\t")
            print(device_no," ",device_count)
            select_device(device_count)
        device_count2+=1
select_device(device_count)
current_song=""
results = sp.currently_playing()
try:
    if results['is_playing']:
        track_name = results['item']['name']
        artist_name = ', '.join([artist['name'] for artist in results['item']['artists']])
        current_song="\033[36m"+f'{track_name}'+"\033[0m"+' -- '+ "\033[34m"+f'{artist_name}'+"\033[0m"
        current_song="Now playing:      \t"+current_song
    ps.pause_song()
except:
    pass
while(True):
    print("\033[36m"+"1 to play new song"+"\033[0m\t")
    print("\033[36m"+"2 to pause song"+"\033[0m\t")
    print("\033[36m"+"3 to resume song\t\t "+"\033[0m\t\t"+"\033[32m"+current_song+"\033[0m\t")
    print("\033[36m"+"4 to add song to queue"+"\033[0m\t")
    print("\033[36m"+"5 to go to next song"+"\033[0m\t")
    print("\033[36m"+"6 to go to previous song"+"\033[0m\t")
    print("\033[36m"+"7 to change device"+"\033[0m\t")
    print("\033[36m"+"8 to exit out of app"+"\033[0m\t")

    choice = int(input("Enter choice : "))
    match choice:
        case 1:
            ps.start_song()
            results = sp.currently_playing()
            if results['is_playing']:
                track_name = results['item']['name']
                artist_name = ', '.join([artist['name'] for artist in results['item']['artists']])
                current_song="\033[36m"+f'{track_name}'+"\033[0m"+' -- '+ "\033[34m"+f'{artist_name}'+"\033[0m"
                current_song="Now playing:      \t"+current_song
        case 2:
            current_state = sp.current_playback()
            if current_state['is_playing']:
                ps.pause_song()
                print("Track is currently paused.")
            else:
                print("Track is currently paused.")
            time.sleep(0.5)
            results = sp.currently_playing()
            if results['is_playing']:
                track_name = results['item']['name']
                artist_name = ', '.join([artist['name'] for artist in results['item']['artists']])
                current_song="\033[36m"+f'{track_name}'+"\033[0m"+' -- '+ "\033[34m"+f'{artist_name}'+"\033[0m"
                current_song="Now playing:      \t"+current_song
        case 3:
            current_state = sp.current_playback()
            if current_state['is_playing']:
                print("Track is currently playing.")
            else:
                sp.start_playback()
                print("Track is currently playing.")
            results = sp.currently_playing()
            if results['is_playing']:
                track_name = results['item']['name']
                artist_name = ', '.join([artist['name'] for artist in results['item']['artists']])
                current_song="\033[36m"+f'{track_name}'+"\033[0m"+' -- '+ "\033[34m"+f'{artist_name}'+"\033[0m"
                current_song="Now playing:      \t"+current_song
        case 4:
            ps.addtoqueue()
            results = sp.currently_playing()
            if results['is_playing']:
                track_name = results['item']['name']
                artist_name = ', '.join([artist['name'] for artist in results['item']['artists']])
                current_song="\033[36m"+f'{track_name}'+"\033[0m"+' -- '+ "\033[34m"+f'{artist_name}'+"\033[0m"
                current_song="Now playing:      \t"+current_song
        case 5:
            try:
                print("Playing next track")
                sp.next_track()
                time.sleep(1)
            except spotipy.SpotifyException as e:
                print("No tracks left in queue")
            results = sp.currently_playing()
            if results['is_playing']:
                track_name = results['item']['name']
                artist_name = ', '.join([artist['name'] for artist in results['item']['artists']])
                current_song="\033[36m"+f'{track_name}'+"\033[0m"+' -- '+ "\033[34m"+f'{artist_name}'+"\033[0m"
                current_song="Now playing:      \t"+current_song
        case 6:
            try:
                print("Playing previous track")
                sp.previous_track()
            except spotipy.SpotifyException as e:
                print("No previous tracks left")
            results = sp.currently_playing()
            if results['is_playing']:
                track_name = results['item']['name']
                artist_name = ', '.join([artist['name'] for artist in results['item']['artists']])
                current_song="\033[36m"+f'{track_name}'+"\033[0m"+' -- '+ "\033[34m"+f'{artist_name}'+"\033[0m"
                current_song="Now playing:      \t"+current_song
        case 7:
            results = sp.currently_playing()
            if results['is_playing']:
                track_name = results['item']['name']
                artist_name = ', '.join([artist['name'] for artist in results['item']['artists']])
                current_song="\033[36m"+f'{track_name}'+"\033[0m"+' -- '+ "\033[34m"+f'{artist_name}'+"\033[0m"
                current_song="Now playing:      \t"+current_song
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                if len(devices['devices'])==0:
                    print("\033[31m"+"Open spotify on a device first"+"\033[0m\t")
                    exit()
                else:
                    print("\033[32m"+f"{len(devices['devices'])} active device(s) found"+"\033[0m\t"+"\n")
                    device_count=0
                for device in devices['devices']:
                    print("\033[33m"+f"{device_count+1}. {device['name']}"+"\033[0m\t")
                    device_count+=1
                select_device(device_count)
                ps.pause_song()
            except:
                print("\033[32m"+"Wait while we handle some errors"+"\033[0m\t")
                time.sleep(2)
        case 8: 
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        case 0:   #to refresh the terminal
            results = sp.currently_playing()
            if results['is_playing']:
                track_name = results['item']['name']
                artist_name = ', '.join([artist['name'] for artist in results['item']['artists']])
                current_song="\033[36m"+f'{track_name}'+"\033[0m"+' -- '+ "\033[34m"+f'{artist_name}'+"\033[0m"
                current_song="Now playing:      \t"+current_song         
    
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


