import spotipy
from spotipy.oauth2 import SpotifyOAuth
from env import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

def spotify():
    scope = "user-library-read,playlist-modify-private,playlist-modify-public"
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=scope,
            show_dialog=True,
            cache_path="token.txt",
        )
    )
    return sp