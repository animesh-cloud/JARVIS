# spotify_control.py
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from secrets import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI


scope = "user-read-playback-state user-modify-playback-state user-read-currently-playing"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=scope
))

def play_music():
    devices = sp.devices()
    if devices["devices"]:
        device_id = devices["devices"][0]["id"]
        sp.start_playback(device_id=device_id)
        print("▶️ Playing music")
    else:
        print("❌ No active devices")

def pause_music():
    sp.pause_playback()
    print("⏸️ Music paused")

def skip_track():
    sp.next_track()
    print("⏭️ Skipped track")

def currently_playing():
    track = sp.current_playback()
    if track and track["is_playing"]:
        song = track["item"]["name"]
        artist = track["item"]["artists"][0]["name"]
        print(f"🎵 Now playing: {song} by {artist}")
    else:
        print("⏹️ Nothing is playing.")

def resume_music():
    sp.start_playback()

