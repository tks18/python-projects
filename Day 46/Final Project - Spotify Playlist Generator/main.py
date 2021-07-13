from bs4 import BeautifulSoup
from spotify import spotify
import requests
from dateutil.parser import parse


def get_songs_html_data(date):
    request = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
    html = request.text
    return html


def get_user_id():
    user = spfy.current_user()
    return user["id"]


def create_playlist(user_id, scrap_date):
    playlist = spfy.user_playlist_create(
        user_id,
        name=f"{scrap_date} - Billboard Top 100",
        public=True,
        description=f"Billboard's Top 100 for {scrap_date}",
    )
    return playlist["id"]


def add_track_to_playlist(user_id, plylist_id, song_uris):
    plylist_tracks_add = spfy.user_playlist_add_tracks(user_id, plylist_id, song_uris)
    if plylist_tracks_add["snapshot_id"]:
        print("Successfully Generated Playlist")


scrap_date = input("Enter a Date to Generate Top 100 Billboard Playlist: (YYYY-MM-DD) ")
parsed_date = parse(scrap_date)

html_data = get_songs_html_data(scrap_date)
soup = BeautifulSoup(html_data, "html.parser")
spfy = spotify()

song_titles = soup.select(".chart-element__information__song")
song_uris = []
for title in song_titles:
    song_title = title.getText()
    song_search = spfy.search(
        q=f"track: {song_title} year: {parsed_date.year}", limit=1, type="track"
    )
    try:
        song_uris.append(song_search["tracks"]["items"][0]["uri"])
    except:
        print("Song Not Found")

user_id = get_user_id()
plylist_id = create_playlist(user_id=user_id, scrap_date=scrap_date)
add_track_to_playlist(user_id=user_id, plylist_id=plylist_id, song_uris=song_uris)
