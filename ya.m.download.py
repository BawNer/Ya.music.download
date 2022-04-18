from yandex_music import Client
import json
import os.path


def json_append():
    append = {"id_track": info.id,
              "track_name": info.title,
              "artist_name": artists}
    return append


def check_file():
    global tracks
    if os.path.exists('db_tracks.json'):
        tracks = json.load(open('db_tracks.json'))
    else:
        tracks = []
    return tracks


def check_json(track_name):
    if len(tracks) == 0:
        tracks.append(json_append())
        info.download("tracks\\" + track_name)
    elif info.id in tracks[count].values():
        pass
    else:
        tracks.append(json_append())
        info.download("tracks\\" + track_name)


def file_name():
    global artists
    for j in info.artists:
        artists.append(j.name)
    track_name = info.title + " - " + f"{', '.join(artists)}.mp3"

    return track_name


client = Client('AQAAAAAtHbJmAAG8XlK-3Ut_WE4Fmk5HPfYOfmk').init()
tracks = check_file()
print(len(tracks))
count = 0
artist_count = 0
artists = []

for i in client.users_likes_tracks():
    info = i.fetch_track()
    check_json(file_name())
    artists = []
    if count < len(tracks) - 1:
        count += 1


json.dump(tracks, open('db_tracks.json', 'w'))
