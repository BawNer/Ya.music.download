from yandex_music import Client
import json
import os.path
from token import TOKEN


def open_json():
    global tracks
    if os.path.exists('db_tracks.json'):
        tracks = json.load(open('db_tracks.json'))
    else:
        tracks = []
    return tracks


def change_tracks(track_name):
    append = {"id_track": info.id,
              "track_name": info.title,
              "artist_name": artists}
    if len(tracks) == 0:
        tracks.append(append)
        info.download("tracks\\" + track_name)
    elif info.id in tracks[count].values():
        pass
    else:
        tracks.append(append)
        info.download("tracks\\" + track_name)


def file_name():
    for j in info.artists:
        artists.append(j.name)
    track_name = info.title + " - " + f"{', '.join(artists)}.mp3"

    return track_name


client = Client(TOKEN).init()
tracks = open_json()
print(len(tracks))
count = 0
artist_count = 0
artists = []
if os.path.exists("tracks"):
    pass
else:
    os.mkdir("tracks")
for i in client.users_likes_tracks():
    info = i.fetch_track()
    change_tracks(file_name())
    artists = []
    if count < len(tracks) - 1:
        count += 1
json.dump(tracks, open('db_tracks.json', 'w'))
